from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    # путь к templates и static относительно корня проекта
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates"),
        static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
    )

    # конфиг
    from app.config import Config
    app.config.from_object(Config)

    db.init_app(app)

    # импорт маршрутов
    from app.routes import main
    app.register_blueprint(main)

    return app
