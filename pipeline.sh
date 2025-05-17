# /usr/bin/bash

uv run bash scripts/formatting_check.sh
uv run bash scripts/test_coverage.sh
uv run bash scripts/type_check.sh
