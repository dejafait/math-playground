#!/usr/bin/env bash
# Subscription-backed claude research loop; prompt: ./PROMPT.md.
set -euo pipefail
repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
exec python3 "$repo_dir/scripts/loop/runner.py" claude "$@"
