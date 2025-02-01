from flask import Flask
from dotenv import load_dotenv
from app.routes import analysis_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(analysis_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
