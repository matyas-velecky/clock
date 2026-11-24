from datetime import datetime

from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Úvodní strana s analogovým ciferníkem a časem serveru."""
    now = datetime.now()
    return render_template("index.html", now=now)


@app.route("/api/time")
def api_time():
    """Aktuální čas serveru jako JSON (pro synchronizaci ciferníku)."""
    now = datetime.now()
    return jsonify(
        iso=now.isoformat(timespec="milliseconds"),
        hours=now.hour,
        minutes=now.minute,
        seconds=now.second,
        milliseconds=now.microsecond // 1000,
    )


if __name__ == "__main__":
    app.run(debug=True)
