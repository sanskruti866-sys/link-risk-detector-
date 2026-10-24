
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
        return jsonify({"error": "URL is required"}), 400

    return jsonify({
        "url": url,
        "message": "Backend received the URL",
        "note": "Risk analysis is not implemented yet"
    })

if __name__ == "__main__":
    app.run(debug=True)
