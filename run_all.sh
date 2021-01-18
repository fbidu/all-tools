#! /bin/bash
SEP="-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"

echo "Black:"
poetry run black . --check
echo $SEP

echo "Hypothesis:"
poetry run hypothesis
echo $SEP
