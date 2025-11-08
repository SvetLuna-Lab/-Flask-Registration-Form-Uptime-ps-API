# Flask Registration Form, Uptime & ps API

Small Flask application demonstrating:

- form validation with WTForms and custom validators;
- unit testing of validators and the `/registration` endpoint with pytest and Flask test client;
- system uptime endpoint (`/uptime`) based on the `uptime` command;
- current processes endpoint (`/ps`) that proxies the `ps` command with query args.

This project is inspired by a practical assignment about GET/POST requests, validators,
testing and interacting with system commands from Python.

## Endpoints

- `POST /registration`  
  Validates registration data and returns JSON with either a success message or validation errors.

- `GET /uptime`  
  Returns current system uptime as a human-readable string (using `uptime -p`).

- `GET /ps?arg=a&arg=u&arg=x`  
  Runs `ps` with the provided arguments and returns the output wrapped in `<pre>...</pre>`.

## How to run

```bash
python -m venv .venv

source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py



Running tests

pytest


Tech stack

Python

Flask

Flask-WTF / WTForms

pytest

subprocess (uptime, ps)
