from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "Hello from Flask in Docker!"

if __name__ == "__main__":
    # 0.0.0.0 is critical so the app is reachable from outside the container
    app.run(host="0.0.0.0", port=5000)
