tefrom flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Edited from Azure App Service (Flask)!"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # Local run
    app.run(host="0.0.0.0", port=8000)
