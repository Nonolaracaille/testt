from flask import Flask
import importlib.util

app = Flask(__name__)

@app.route("/")
def home():
    try:
        spec = importlib.util.spec_from_file_location("exploit", "CVE-2026-39987.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return "Le script a été exécuté ✅"

    except Exception as e:
        return f"Erreur : {str(e)}"

app = app
