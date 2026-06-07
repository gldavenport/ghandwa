# Handoff: Ghandwa NocoDB Backup System

**Date:** 2026-06-07  
**Status:** Complete — both Ubuntu server and Mac sides operational.

---

## What is built

Two-tier nightly backup of the Ghandwa NocoDB SQLite database:

1. **Ubuntu server** — nightly SQLite backup via systemd timer
2. **Mac** — hourly rsync pull to local Application Support via launchd

---

## Ubuntu side

### Confirmed parameters

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

### Verified working

- Script runs cleanly (~5s), produces ~290 KiB archive from 6.31 MiB DB
- Email delivers with correct line breaks
- Timer active, runs nightly at midnight Eastern
- Log clean

---

## Mac side

### Parameters

| Item | Value |
|---|---|
| Pull script (repo) | `tools/mac/pull-ghandwa-db-backups.sh` |
| Pull script (live) | `~/Library/Scripts/pull-ghandwa-db-backups.sh` |
| launchd plist (repo) | `tools/mac/local.ghandwa-db-backup-pull.plist` |
| launchd plist (live) | `~/Library/LaunchAgents/local.ghandwa-db-backup-pull.plist` |
| SSH key | `~/.ssh/ghandwa_backup_pull` (ed25519, no passphrase) |
| Backup user on server | `ghpull` (uid assigned by system, home `/home/ghpull`) |
| Archive destination | `~/Library/Application Support/Ghandwa/NocoDB/` |
| Pull log | `~/Library/Logs/ghandwa-db-backup/pull.log` |
| launchd log | `~/Library/Logs/ghandwa-db-backup/launchd.log` |
| Schedule | Hourly (`StartInterval 3600`), runs at load |

### Notes

- Script lives in `~/Library/Scripts/` (not `~/Documents/`) due to macOS 15 TCC restrictions — launchd agents cannot access `~/Documents/` without Full Disk Access. Repo copy in `tools/mac/` is the source of truth for edits; sync to `~/Library/Scripts/` after any change.
- Destination is `~/Library/Application Support/Ghandwa/NocoDB/` (not iCloud Drive) for the same TCC reason.
- The pre-existing system `backup` account (uid 34, home `/var/backups`, shell `nologin`) was not modified. A separate `ghpull` user was created for this purpose.
- `--ignore-existing` flag means only new archives are transferred; existing files are never overwritten.

### Verified working

- Archives pull cleanly; existing files skipped on subsequent runs
- launchd agent loads and runs on schedule
- Archives confirmed in destination directory

---

## Open items

```text
- Disk-space warning on Ubuntu (suggested threshold: 20 GB free) — deferred
- Optional SSH hardening on ghpull (restrict command, source IP) — deferred
- Monthly restore test — add to calendar
```

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
