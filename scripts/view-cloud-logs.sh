#!/bin/bash

# Override with HZ_HOST, HZ_USER, or HZ_KEY if you use a different host or key.
HOST="${HZ_HOST:-132.226.135.26}"
REMOTE_USER="${HZ_USER:-ubuntu}"
KEY="${HZ_KEY:-${HOME}/.ssh/id_ed25519}"

echo "Connecting to live log stream on ${HOST}..."
echo "Press Ctrl+C to exit."
ssh -i "${KEY}" "${REMOTE_USER}@${HOST}" "sudo journalctl -u minecraft -f"
