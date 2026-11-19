# CyberTrap — consent-based camera demo

## What it does
A dark-themed browser demo that asks the visitor to grant camera permission, requires an explicit consent checkbox, shows a preview, and uploads a snapshot only after the visitor presses **Upload photo**.

It does not activate the camera secretly or upload anything in the background.

## Run locally (Windows)
1. Install Python 3 if it is not already installed.
2. Open Command Prompt in this folder.
3. Create and activate a virtual environment:

   ```bat
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Install Flask:

   ```bat
   pip install -r requirements.txt
   ```

5. Start the server:

   ```bat
   py app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser.

## Run locally (Linux / Ubuntu)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```
Then open `http://127.0.0.1:5000`.

## To use on another device
Camera access on another device generally requires HTTPS. Deploy the app to a trusted hosting service with HTTPS enabled, and keep the upload endpoint protected. Do not expose the development server directly to the public internet. Get clear permission from each participant and explain who receives and stores the photo.

## Storage
Uploaded images are saved in `uploads/`. Keep this folder private, restrict access, and delete photos when they are no longer needed. Do not commit real photos or secrets to a public code repository.

## Limits
- JPG, PNG, and WebP uploads only.
- 8 MB maximum request size.
- This is a learning demo, not a production-secure photo storage service.


## Deploy to Render
1. Push this folder to a GitHub repository (include `app.py`, `Procfile`, `requirements.txt`, and `templates/index.html`).
2. In Render, create **New → Web Service**, connect the repository, and choose Python.
3. Set **Build Command** to `pip install -r requirements.txt`.
4. Set **Start Command** to `gunicorn app:app --bind 0.0.0.0:$PORT`.
5. Deploy. Render provides an HTTPS `onrender.com` address.

Important: Render's default filesystem is temporary. Files saved in `uploads/` may disappear after a restart or redeploy. Do not use this simple demo to collect other people's photos or store sensitive images. For a real consent-based project, add authenticated access, clear retention/deletion controls, and private persistent/object storage before collecting images.
