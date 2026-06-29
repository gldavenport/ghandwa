#!/bin/zsh
set -euo pipefail

SERVER_USER="ghpull"
SERVER_HOST="10.1.1.10"
REMOTE_DIR="/srv/backups/ghandwa-db/archives"
LOCAL_DIR="$HOME/Library/Application Support/Ghandwa/NocoDB"
LOG_DIR="$HOME/Library/Logs/ghandwa-db-backup"
LOG_FILE="$LOG_DIR/pull.log"
SSH_KEY="$HOME/.ssh/ghandwa_backup_pull"

mkdir -p "$LOCAL_DIR" "$LOG_DIR"

{
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Starting pull"

  /usr/bin/rsync -av \
    -e "/usr/bin/ssh -i $SSH_KEY -o IdentitiesOnly=yes" \
    --ignore-existing \
    --include='ghandwa-db-*.tar.zst' \
    --exclude='*' \
    "${SERVER_USER}@${SERVER_HOST}:${REMOTE_DIR}/" \
    "${LOCAL_DIR}/"

  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Pull complete"
} >> "$LOG_FILE" 2>&1
