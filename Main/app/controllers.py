from flask import Blueprint, render_template, jsonify
from .models import db, Vacancy
from .service import fill_db

# Создаем Blueprint для организации маршрутов
main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    """
    Маршрут для главной страницы.
    Отображает HTML-шаблон index.html.
    """
    return render_template('index.html')

@main.route('/update-vacancies')
def update_vacancies():
    """
    Маршрут для обновления данных о вакансиях.
    1. Очищает текущие записи о вакансиях в базе данных.
    2. Заполняет базу данных новыми данными о вакансиях.
    3. Возвращает данные о вакансиях в формате JSON.
    """
    try:
        # Удаляем все записи о вакансиях из базы данных
        Vacancy.query.delete()
        # Заполняем базу данных новыми данными о вакансиях
        fill_db(db, Vacancy)

        # Формируем список данных о вакансиях для возврата в формате JSON
        vacancies_data = []
        for vacancy in Vacancy.query.all():
            vacancies_data.append({
                'vacancy_id': vacancy.vacancy_id,
                'title': vacancy.title,
                'employer': vacancy.employer,
                'location': vacancy.location,
                'employment': vacancy.employment,
                'salary': vacancy.salary,
                'published_at': vacancy.published_at
            })

        # Возвращаем данные о вакансиях в формате JSON
        return jsonify(vacancies_data)

    except Exception as e:
        # Обрабатываем ошибки и откатываем изменения в случае ошибки
        print(f"Ошибка при обновлении данных: {str(e)}")
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
