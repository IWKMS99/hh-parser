from . import db

# Определение модели Vacancy для работы с таблицей вакансий в базе данных
class Vacancy(db.Model):
    # Поле id: первичный ключ, уникальный идентификатор для каждой записи
    id = db.Column(db.Integer, primary_key=True)
    
    # Поле vacancy_id: идентификатор вакансии, обязательное поле
    vacancy_id = db.Column(db.Integer, nullable=False)
    
    # Поле title: название вакансии, обязательное поле
    title = db.Column(db.String(255), nullable=False)
    
    # Поле employer: название работодателя, обязательное поле
    employer = db.Column(db.String(255), nullable=False)
    
    # Поле location: местоположение вакансии, обязательное поле
    location = db.Column(db.String(255), nullable=False)
    
    # Поле employment: тип занятости (полная занятость, частичная занятость и т.д.), обязательное поле
    employment = db.Column(db.String(255), nullable=False)
    
    # Поле salary: зарплата, необязательное поле (может быть пустым)
    salary = db.Column(db.String(255), nullable=True)
    
    # Поле published_at: дата и время публикации вакансии, обязательное поле
    published_at = db.Column(db.DateTime, nullable=False)
