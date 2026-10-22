#!/bin/bash
set -euo pipefail

# Always run from the repo root, whatever directory the script is called from.
cd "$(dirname "$0")/.."

# Override any of these with environment variables, for example:
#   HZ_KEY=~/.ssh/my_key ./scripts/deploy-to-cloud.sh
HOST="${HZ_HOST:-132.226.135.26}"
REMOTE_USER="${HZ_USER:-ubuntu}"
KEY="${HZ_KEY:-${HOME}/.ssh/id_ed25519}"
TARGET_DIR="~/minecraft-server"

if [ ! -f "${KEY}" ]; then
  echo "SSH key not found at ${KEY}. Set HZ_KEY to the path of your private key." >&2
  exit 1
fi

echo "Deploying datapacks to ${HOST}..."
scp -i "${KEY}" -r datapacks/* "${REMOTE_USER}@${HOST}:${TARGET_DIR}/world/datapacks/"

# server.properties belongs in the server root, not in config/, and the live copy
# on the VM is the source of truth, so it is not sent.
echo "Deploying configs to ${HOST}..."
for item in configs/*; do
  if [ "$(basename "${item}")" = "server.properties" ]; then
    continue
  fi
  scp -i "${KEY}" -r "${item}" "${REMOTE_USER}@${HOST}:${TARGET_DIR}/config/"
done

echo "Deployment complete."
echo "If you updated datapacks, run '/reload' in game to apply changes without restarting."
echo "If you updated configs, restart with: ssh -i ${KEY} ${REMOTE_USER}@${HOST} \"sudo systemctl restart minecraft.service\""
