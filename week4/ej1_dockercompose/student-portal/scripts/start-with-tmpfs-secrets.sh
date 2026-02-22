#!/bin/sh
set -eu

SOURCE_SECRET_PATH="${SOURCE_SECRET_PATH:-./secrets/db_password.txt}"
TARGET_SECRET_PATH="${TARGET_SECRET_PATH:-/run/secrets/db_password}"

if [ ! -f "$SOURCE_SECRET_PATH" ]; then
  echo "Secret file not found: $SOURCE_SECRET_PATH" >&2
  exit 1
fi

mkdir -p "$(dirname "$TARGET_SECRET_PATH")"
cp "$SOURCE_SECRET_PATH" "$TARGET_SECRET_PATH"
chmod 600 "$TARGET_SECRET_PATH"

exec "$@"
