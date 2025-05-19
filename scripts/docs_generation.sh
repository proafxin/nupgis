# /usr/bin/bash

cd docs/
uv run sphinx-apidoc -f -o source/ ../ ../tests/
make clean
make html
cd ..
