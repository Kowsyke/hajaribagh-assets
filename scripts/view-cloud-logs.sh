#!/bin/bash

HOST="132.226.135.26"
USER="ubuntu"
KEY="${HOME}/.ssh/id_ed25519"

echo "Connecting to live log stream on ${HOST}..."
echo "Press Ctrl+C to exit."
ssh -i "${KEY}" "${USER}@${HOST}" "sudo journalctl -u minecraft -f"
