# /usr/bin/bash

set -e
uv venv
uv sync --all-extras --all-groups

uv run bash scripts/formatting_check.sh
uv run bash scripts/test_coverage.sh
uv run bash scripts/type_check.sh
uv run bash scripts/docs_generation.sh
