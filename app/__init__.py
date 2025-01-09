from flask import Flask
from flask_cors import CORS
from app.routes.esg_report import esg_report_bp
from app.routes.db_report import db_report_bp

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Register blueprints
    app.register_blueprint(esg_report_bp, url_prefix='/api/esg_report')
    app.register_blueprint(db_report_bp, url_prefix='/api/db_report')
    
    return app
