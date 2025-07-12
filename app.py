from flask import Flask
app = Flask(_name_)

@app.route("/")
def home():
    return "Hello from Flask deployed via Jenkins & Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
