# /usr/bin/bash

uv run pytest .
uv run coverage run --source=. -m pytest .
uv run coverage report -m --fail-under=90
