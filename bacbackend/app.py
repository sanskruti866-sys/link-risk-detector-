from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Link Risk Detector backend is running"})

@app.route("/check", methods=["POST"])
def check_link():
    data = request.get_json(silent=True) or {}
    url = data.get("url", "").strip()

    if not url:
        return jsonify({"error": "Please enter a URL"}), 400

    suspicious = any(word in url.lower() for word in
                     ["login-verify", "free-gift", "account-suspended"])

    return jsonify({
        "url": url,
        "result": "Suspicious" if suspicious else "Needs further checking"
    })

if __name__ == "__main__":
    app.run()
