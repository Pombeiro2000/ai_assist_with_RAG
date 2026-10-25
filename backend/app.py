import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
import psycopg

load_dotenv()

app = Flask(__name__)
cors_origins = [o for o in os.getenv("CORS_ORIGINS", "http://localhost:4200").split(",") if o]
if cors_origins:
    CORS(app, origins=cors_origins)


@app.get("/api/health")
def health():
    try:
        with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
            conn.execute("SELECT 1")
        db = "ok"
    except Exception as e:
        db = f"error: {e}"
    return jsonify(status="ok", db=db)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
