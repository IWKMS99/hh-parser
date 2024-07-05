# Импортируем необходимые модули из Flask и его расширений
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Инициализируем экземпляры SQLAlchemy и Migrate
db = SQLAlchemy()
migrate = Migrate()

# Функция для создания приложения Flask
def create_app(config_class=Config):
    # Создаем экземпляр приложения Flask
    app = Flask(__name__)
    
    # Загружаем конфигурацию из указанного класса Config
    app.config.from_object(config_class)

    # Инициализируем SQLAlchemy для работы с приложением
    db.init_app(app)

    # Инициализируем Flask-Migrate для работы с миграциями базы данных
    migrate.init_app(app, db)

    # Импортируем и регистрируем blueprint'ы (контроллеры)
    from .controllers import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Создаем все таблицы базы данных в контексте приложения
    with app.app_context():
        db.create_all()

    # Возвращаем экземпляр приложения Flask
    return app
