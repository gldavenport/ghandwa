# NocoDB MCP Setup

last_updated: 2026-06-06

## Infrastructure

| Component | Value |
|---|---|
| Server | Mac Mini 2014, Ubuntu 24.04.4 LTS |
| Server LAN IP | 10.1.1.103 (static) |
| Server hostname | A1347-DB |
| Desktop | iMac, macOS 15, IP 10.1.1.105 |
| NocoDB | Docker, `nocodb/nocodb:latest` |
| Docker Compose | `/home/g/nocodb/compose.yaml` |
| Host data path | `/home/g/nocodb/data/` |
| SQLite DB (host) | `/home/g/nocodb/data/noco.db` |
| SQLite DB (container) | `/usr/app/data/noco.db` |
| Port mapping | `0.0.0.0:8080->8080/tcp` |
| Restart policy | `unless-stopped` |
| Docker enabled on boot | yes (`systemctl is-enabled docker`) |

## Working Claude Desktop Config

File: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "NocoDB Base - ghandwa": {
      "command": "/usr/local/bin/npx",
      "args": [
        "-y",
        "mcp-remote@latest",
        "http://127.0.0.1:18080/mcp/ncl4t0ejzg6k0ugh",
        "--allow-http",
        "--header",
        "xc-mcp-token: <MCP_TOKEN>"
      ]
    }
  }
}
```

The URL is `127.0.0.1:18080`, not `10.1.1.103:8080` — see tunnel section below.

## MCP Token

Token lives in the SQLite DB, table `nc_mcp_tokens`:

| field | value |
|---|---|
| id | `ncl4t0ejzg6k0ugh` |
| title | `ghandwa` |
| base_id | `panfdqccovzm80c` |
| fk_workspace_id | `wmt63qlm` |

The token value is a 32-character string stored in the `token` column. To inspect or recover it without the GUI, SSH to the server and run:

```bash
sqlite3 /home/g/nocodb/data/noco.db \
  "SELECT id, title, token FROM nc_mcp_tokens;"
```

To regenerate the token via the NocoDB REST API (no GUI required):

```bash
# Get an auth token first
curl -s -X POST http://localhost:8080/api/v1/auth/user/signin \
  -H 'Content-Type: application/json' \
  -d '{"email":"<EMAIL>","password":"<PASSWORD>"}' | python3 -m json.tool

# Then use the auth token to create a new MCP token (consult NocoDB API docs for current endpoint)
```

**Rotate the token** if it has been exposed in logs or chat. Update `claude_desktop_config.json` after rotation.

## SSH Tunnel (Required)

### Why

Claude Desktop on macOS 15 cannot reach LAN IPs directly when using `mcp-remote` as a child process, even with Local Network privacy permission enabled in System Settings. The `mcp-remote` subprocess hits `EHOSTUNREACH` on `10.1.1.103:8080` despite the same URL being reachable from Terminal. This appears to be a sandbox entitlement limitation of Claude Desktop that goes beyond the standard Local Network toggle. Connections to `localhost`/`127.0.0.1` are not subject to this restriction.

The tunnel forwards `127.0.0.1:18080` on the desktop to `localhost:8080` on the server, bypassing the sandbox restriction.

### Persistent Tunnel via launchd

Plist: `~/Library/LaunchAgents/com.ghandwa.nocodb-tunnel.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.ghandwa.nocodb-tunnel</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/bin/ssh</string>
    <string>-N</string>
    <string>-o</string>
    <string>ExitOnForwardFailure=yes</string>
    <string>-o</string>
    <string>ServerAliveInterval=60</string>
    <string>-L</string>
    <string>18080:localhost:8080</string>
    <string>g@10.1.1.103</string>
  </array>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
</dict>
</plist>
```

**Requirements:** SSH key-based auth to the server (no password, no passphrase) — launchd cannot handle interactive authentication.

```bash
# Set up key-based auth (one time)
ssh-keygen -t ed25519 -C "ghandwa-tunnel"   # no passphrase
ssh-copy-id g@10.1.1.103

# Load the tunnel agent
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ghandwa.nocodb-tunnel.plist

# Verify
curl -I http://127.0.0.1:18080   # should return HTTP 200
```

**Note:** macOS will prompt "ssh is an item that can run in the background" — allow it.

To unload: `launchctl bootout gui/$(id -u) com.ghandwa.nocodb-tunnel`

## Failure Modes Encountered

| Error | Cause | Fix |
|---|---|---|
| `Authentication required - MCP token missing` | Request/config did not send the `xc-mcp-token` header correctly, or the wrong endpoint/token pairing was used | Verify the MCP endpoint ID from `nc_mcp_tokens.id`, verify the token from `nc_mcp_tokens.token`, and make sure the client sends `xc-mcp-token: <MCP_TOKEN>` |
| `Non-HTTPS URLs are only allowed for localhost` | `mcp-remote` blocks plain HTTP to non-localhost | Add `--allow-http` to args |
| `EHOSTUNREACH 10.1.1.103:8080` | macOS 15 Claude Desktop sandbox blocks LAN IP in child processes | SSH tunnel; use `127.0.0.1:18080` |
| `Bootstrap failed: 5: Input/output error` | launchd plist wrapped in spurious `<key>New item</key><dict>` nesting (editor artifact) | Keys must be direct children of top-level `<dict>`; validate with `plutil` |
| `Bootstrap failed: 5: Input/output error` (after plist fix) | SSH requires password; launchd cannot authenticate interactively | Set up passwordless key-based auth first |
| MCP timeout during initialize | Forcing `--transport sse-only` caused/participated in initialize timeout with this setup | Remove `--transport sse-only`; let `mcp-remote` auto-detect transport |

## Migration Notes

When migrating `noco.db` to a new host, the MCP token migrates with the DB file. Verify by inspecting `nc_mcp_tokens` before assuming the token needs to be regenerated. What does **not** migrate automatically: the SSH tunnel config, the launchd plist, and the Claude Desktop config URL.

When the browser workspace, tables, and rows are present after migration, that confirms the core SQLite DB migrated correctly. MCP tokens should be checked in `nc_mcp_tokens` before assuming they need to be regenerated. The MCP endpoint uses `nc_mcp_tokens.id` in the URL path and `nc_mcp_tokens.token` as the `xc-mcp-token` header.
