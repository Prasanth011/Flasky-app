from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Meghana and Prasanth getting married on novemeber 26, 2026. All are invited!"

app.run(host="0.0.0.0", port=5000)
