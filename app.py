from pathlib import Path
from datetime import datetime, timezone
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import uuid

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024  # 8 MB
ALLOWED_MIME = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp"}

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/upload")
def upload():
    photo = request.files.get("photo")
    consent = request.form.get("consent")
    if consent != "yes":
        return jsonify(ok=False, message="Consent is required."), 400
    if not photo or not photo.filename:
        return jsonify(ok=False, message="No image was received."), 400
    ext = ALLOWED_MIME.get(photo.mimetype)
    if not ext:
        return jsonify(ok=False, message="Please upload a JPG, PNG, or WebP image."), 415

    # Use a generated filename; never trust a client-supplied path.
    filename = f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}_{uuid.uuid4().hex[:10]}{ext}"
    photo.save(UPLOAD_DIR / secure_filename(filename))
    return jsonify(ok=True, message="Photo uploaded successfully.", filename=filename)

@app.errorhandler(413)
def too_large(_error):
    return jsonify(ok=False, message="Image is too large. Maximum size is 8 MB."), 413

if __name__ == "__main__":
    # Local development only. For public access, deploy behind HTTPS.
    app.run(host="127.0.0.1", port=5000, debug=False)
