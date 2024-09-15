#!/bin/bash
python3 -m venv v_env
source v_env/bin/activate
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "env working"
    pip install matplotlib
else
    echo "env not working"
fi