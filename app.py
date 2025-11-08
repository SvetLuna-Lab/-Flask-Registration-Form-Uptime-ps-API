# app.py

import subprocess
from typing import Any

from flask import Flask, jsonify, request

from forms import RegistrationForm

app = Flask(__name__)

# Secret key is required by Flask-WTF, even if CSRF is disabled
app.config["SECRET_KEY"] = "change-this-secret-key"
# For API-style usage with Postman and tests we disable CSRF
app.config["WTF_CSRF_ENABLED"] = False
app.config["TESTING"] = False


@app.route("/registration", methods=["POST"])
def registration() -> Any:
    """
    POST /registration
    Validates registration form fields using WTForms.
    Returns JSON with either success message or error messages.
    """

    if request.is_json:
        form = RegistrationForm(data=request.get_json())
    else:
        form = RegistrationForm(request.form)

    if form.validate():
        return jsonify({"message": "Registration successful!"}), 201
    else:
        return jsonify({"errors": form.errors}), 400


@app.route("/uptime", methods=["GET"])
def uptime() -> Any:
    """
    GET /uptime
    Returns current system uptime as a simple string.
    Uses `uptime -p` to get a human-readable value.
    """
    try:
        # uptime -p -> "up 10 hours, 3 minutes"
        result = subprocess.run(
            ["uptime", "-p"],
            capture_output=True,
            text=True,
            check=True,
        )
        uptime_str = result.stdout.strip()
        # Optionally remove leading "up "
        if uptime_str.startswith("up "):
            uptime_str = uptime_str[3:]

        return f"Current uptime is {uptime_str}\n", 200
    except Exception as exc:  # noqa: BLE001
        return f"Failed to get uptime: {exc}\n", 500


@app.route("/ps", methods=["GET"])
def ps() -> Any:
    """
    GET /ps?arg=a&arg=u&arg=x
    Runs the `ps` command with the provided arguments and returns
    the result wrapped in <pre>...</pre>.
    """
    args: list[str] = request.args.getlist("arg")
    cmd = ["ps"] + args

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
        )
        output = result.stdout
        return f"<pre>{output}</pre>", 200
    except subprocess.CalledProcessError as exc:
        return (
            f"<pre>Error running command: {exc}\n{exc.stdout}\n{exc.stderr}</pre>",
            500,
        )
    except Exception as exc:  # noqa: BLE001
        return f"<pre>Unexpected error: {exc}</pre>", 500


if __name__ == "__main__":
    # Server start in __main__ block, as required
    app.run(host="0.0.0.0", port=5000, debug=True)
