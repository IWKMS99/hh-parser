from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Создаем экземпляр SQLAlchemy для взаимодействия с базой данных
db = SQLAlchemy()
# Создаем экземпляр Migrate для управления миграциями базы данных
migrate = Migrate()

def create_app(config_class=Config):
    """
    Функция для создания и настройки экземпляра Flask приложения.
    :param config_class: Класс конфигурации, который будет использоваться для настройки приложения.
    :return: Настроенное Flask приложение.
    """
    # Создаем экземпляр Flask приложения
    app = Flask(__name__)
    # Загружаем конфигурацию из указанного класса
    app.config.from_object(config_class)

    # Инициализируем расширения с приложением
    db.init_app(app)
    migrate.init_app(app, db)

    # Импортируем и регистрируем blueprint (модуль) для маршрутов
    from .controllers import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Создаем все таблицы в базе данных, если они еще не созданы
    with app.app_context():
        db.create_all()

    return app
