#!/bin/bash
set -e

HOST="132.226.135.26"
USER="ubuntu"
KEY="${HOME}/.ssh/id_ed25519"
TARGET_DIR="~/minecraft-server"

echo "Deploying datapacks to ${HOST}..."
scp -i "${KEY}" -r datapacks/* "${USER}@${HOST}:${TARGET_DIR}/world/datapacks/"

echo "Deploying configs to ${HOST}..."
scp -i "${KEY}" -r configs/* "${USER}@${HOST}:${TARGET_DIR}/config/" 2>/dev/null || true

echo "Deployment complete."
echo "If you updated datapacks, run '/reload' in game to apply changes without restarting."
