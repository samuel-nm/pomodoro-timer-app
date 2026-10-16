#!/bin/bash

REPO=$REPO
ACCESS_TOKEN=$TOKEN

cd /home/docker/actions-runner

# 1. Always wipe stale state on boot
rm -f .runner .credentials .credentials_rsaparams

echo "Configuring new ephemeral runner..."
REG_TOKEN=$(curl -sX POST -H "Authorization: token ${ACCESS_TOKEN}" -H "Accept: application/vnd.github+json" https://api.github.com/repos/${REPO}/actions/runners/registration-token | jq .token --raw-output)

# 2. Add --ephemeral and --replace flags
./config.sh --url https://github.com/${REPO} --token ${REG_TOKEN} --unattended --ephemeral --replace

# 3. Start the runner
./run.sh