#!/usr/bin/env bash
set -euo pipefail

. /app/venv/bin/activate
PORT=${PORT:-8765}
exec uvicorn app:app --host 0.0.0.0 --port $PORT