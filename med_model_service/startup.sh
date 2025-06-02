#!/bin/bash

pip install uv
uv venv venv
uv pip install --system --requirements requirements.txt
