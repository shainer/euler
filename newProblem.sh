#!/bin/sh

if [ $# -ne 1 ]; then
	echo "This script requires EXACTLY one argument!"
	exit 1
fi

directory="${1}"

mkdir -p "${directory}" || exit $?
cp __main__.template.py "${directory}/__main__.py" || exit $?
chmod +x "${directory}/__main__.py" || $?

echo "All done correctly."
