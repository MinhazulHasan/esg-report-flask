from flask import Flask
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.base import SchedulerNotRunningError
from app.routes.esg_report import esg_report_bp
from app.routes.db_report import db_report_bp
from app.routes.user_query import user_query_bp
from app.schedulers.database_updater import update_all_companies

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Register blueprints
    app.register_blueprint(esg_report_bp, url_prefix='/api/esg_report')
    app.register_blueprint(db_report_bp, url_prefix='/api/db_report')
    app.register_blueprint(user_query_bp, url_prefix='/api/user_query')

    # Initialize the scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_all_companies, 'cron', day=1, hour=0, minute=0)  # Runs on the 1st of each month at midnight
    scheduler.start()
    app.logger.info("BackgroundScheduler has started.")

    # Store scheduler instance
    app.scheduler = scheduler
    
    # Register shutdown handler
    @app.teardown_appcontext
    def shutdown_scheduler(exception=None):
        if hasattr(app, 'scheduler') and app.scheduler.running:
            try:
                app.scheduler.shutdown(wait=False)
                app.logger.info("Scheduler has been shut down.")
            except SchedulerNotRunningError:
                app.logger.warning("Scheduler was not running at the time of shutdown.")
    
    return app
