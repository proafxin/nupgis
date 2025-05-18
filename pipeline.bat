uv run pre-commit run --all-files
uv run pytest .
uv run coverage run --source=. -m pytest .
uv run coverage report -m --fail-under=95
uv run mypy .
