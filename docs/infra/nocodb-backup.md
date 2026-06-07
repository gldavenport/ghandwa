# NocoDB Backup System

**Last updated:** 2026-06-07

Two-tier backup of the Ghandwa NocoDB SQLite database: nightly archive on the Ubuntu server, hourly rsync pull to the Mac.

---

## Ubuntu side

| Item | Value |
|---|---|
| Container name | `nocodb` |
| Live DB | `/home/g/nocodb/data/noco.db` (bind mount) |
| Compose file | `/srv/nocodb/compose.yml` |
| Volume type | bind mount — sqlite3 runs directly on host |
| Backup script | `/opt/ghandwa-backup/backup-ghandwa-db.sh` |
| Service unit | `/etc/systemd/system/ghandwa-db-backup.service` |
| Timer unit | `/etc/systemd/system/ghandwa-db-backup.timer` |
| Archive dir | `/srv/backups/ghandwa-db/archives/` |
| Log | `/srv/backups/ghandwa-db/logs/backup.log` |
| Schedule | Midnight Eastern (`America/New_York`) via systemd |
| Compression | `zstd --ultra -22 -q -T0` |
| Email | `gldavenport@icloud.com` via msmtp, success + failure |
| msmtp config | `/home/g/.msmtprc` |
| Server README | `/opt/ghandwa-backup/README.md` |

---

## Mac side

| Item | Value |
|---|---|
| Pull script (repo) | `tools/mac/pull-ghandwa-db-backups.sh` |
| Pull script (live) | `~/Library/Scripts/pull-ghandwa-db-backups.sh` |
| launchd plist (repo) | `tools/mac/local.ghandwa-db-backup-pull.plist` |
| launchd plist (live) | `~/Library/LaunchAgents/local.ghandwa-db-backup-pull.plist` |
| SSH key | `~/.ssh/ghandwa_backup_pull` (ed25519, no passphrase) |
| Backup user on server | `ghpull` (home `/home/ghpull`) |
| Archive destination | `~/Library/Application Support/Ghandwa/NocoDB/` |
| Pull log | `~/Library/Logs/ghandwa-db-backup/pull.log` |
| launchd log | `~/Library/Logs/ghandwa-db-backup/launchd.log` |
| Schedule | Hourly (`StartInterval 3600`), runs at load |

### Notes

- Script lives in `~/Library/Scripts/` due to macOS 15 TCC restrictions — launchd agents cannot access `~/Documents/` without Full Disk Access. Repo copy in `tools/mac/` is the source of truth for edits; sync to `~/Library/Scripts/` after any change.
- Destination is `~/Library/Application Support/Ghandwa/NocoDB/` rather than iCloud Drive for the same TCC reason.
- The pre-existing system `backup` account (uid 34, home `/var/backups`, shell `nologin`) was not modified. `ghpull` is a separate dedicated user.
- `--ignore-existing` means only new archives are transferred; existing files are never overwritten.

---

## Restore procedure (from Mac)

```bash
# List available archives
ls ~/Library/Application\ Support/Ghandwa/NocoDB/

# Extract a specific archive
cd /tmp
tar -I zstd -xf ~/Library/Application\ Support/Ghandwa/NocoDB/ghandwa-db-TIMESTAMP.tar.zst

# Restore to server (stop NocoDB first)
ssh g@10.1.1.103 'docker stop nocodb'
scp /tmp/noco.db g@10.1.1.103:/home/g/nocodb/data/noco.db
ssh g@10.1.1.103 'docker start nocodb'
```

---

## Monthly restore test

1. Pick the most recent archive from `~/Library/Application Support/Ghandwa/NocoDB/`
2. Extract it to `/tmp`:
   ```bash
   cd /tmp
   tar -I zstd -xf ~/Library/Application\ Support/Ghandwa/NocoDB/ghandwa-db-TIMESTAMP.tar.zst
   ls -lh /tmp/noco.db
   ```
3. Verify the file is non-zero and undamaged:
   ```bash
   sqlite3 /tmp/noco.db 'PRAGMA integrity_check;'
   sqlite3 /tmp/noco.db 'SELECT count(*) FROM nc_models_v2;'
   ```
4. Confirm row count is plausible (should be ~700+).
5. Clean up: `rm /tmp/noco.db`

A full live restore (stopping NocoDB, swapping the file, restarting) is only needed if verifying recovery from actual data loss. The integrity check and row count are sufficient for routine monthly verification.

---

## Deferred

- Disk-space warning on Ubuntu (suggested threshold: 20 GB free)
- SSH hardening on `ghpull` (restrict command, source IP)
- Monthly restore test
