# Импортируем db из текущего пакета (предположительно, из модуля, где определен db)
from . import db

# Определяем класс Vacancy, наследующийся от db.Model (это базовый класс SQLAlchemy для моделей)
class Vacancy(db.Model):
    # Определяем поля модели Vacancy
    id = db.Column(db.Integer, primary_key=True)  # Первичный ключ (автоинкрементируемое поле типа Integer)
    vacancy_id = db.Column(db.Integer, nullable=False)  # Идентификатор вакансии (Integer, обязательное поле)
    title = db.Column(db.String(255), nullable=False)  # Название вакансии (String до 255 символов, обязательное поле)
    employer = db.Column(db.String(255), nullable=False)  # Работодатель (String до 255 символов, обязательное поле)
    location = db.Column(db.String(255), nullable=False)  # Местоположение (String до 255 символов, обязательное поле)
    employment = db.Column(db.String(255), nullable=False)  # Тип занятости (String до 255 символов, обязательное поле)
    salary = db.Column(db.String(255), nullable=True)  # Зарплата (String до 255 символов, может быть пустым)
    published_at = db.Column(db.DateTime, nullable=False)  # Дата публикации (DateTime, обязательное поле)
