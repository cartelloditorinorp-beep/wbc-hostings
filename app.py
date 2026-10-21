
from flask import Flask, render_template_string, jsonify
import os
import psutil

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>W.B.C. Hosting</title>
<style>
body {
  margin: 0;
  padding: 25px;
  background: #0b0b0d;
  color: #f5f5f5;
  font-family: Arial, sans-serif;
}
.card {
  max-width: 650px;
  margin: 35px auto;
  padding: 25px;
  background: #17171b;
  border: 1px solid #b99748;
  border-radius: 16px;
}
h1 { color: #d5b15e; }
p { color: #c5c5c5; }
button {
  background: #d5b15e;
  color: #111;
  border: 0;
  padding: 12px 18px;
  border-radius: 8px;
  font-weight: bold;
}
</style>
</head>
<body>
<div class="card">
  <h1>⟦ W.B.C. HOSTING ⟧</h1>
  <p>West • Block • Crew</p>
  <hr>
  <h2>Dashboard</h2>
  <p>Backend: <strong>ONLINE</strong></p>
  <p>CPU server: {{ cpu }}%</p>
  <p>RAM utilizzata: {{ ram }}%</p>
  <button onclick="location.href='/api/status'">
    Controlla stato
  </button>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        cpu=psutil.cpu_percent(interval=0.2),
        ram=psutil.virtual_memory().percent
    )

@app.route("/api/status")
def status():
    return jsonify({
        "hosting": "W.B.C. Hosting",
        "backend": "online",
        "cpu_percent": psutil.cpu_percent(),
        "ram_percent": psutil.virtual_memory().percent
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
