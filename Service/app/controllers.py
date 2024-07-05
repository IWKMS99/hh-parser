# Импортируем необходимые модули из Flask и текущего пакета
from flask import Blueprint, render_template, jsonify, request
from .models import db, Vacancy

# Создаем blueprint с именем 'main'
main = Blueprint('main', __name__)

# Маршрут для отображения главной страницы
@main.route('/')
def index():
    return render_template('index.html')

# Маршрут для загрузки фильтров вакансий
@main.route('/load-filters', methods=['GET'])
def load_filters():
    # Получаем уникальные значения для каждого фильтра из модели Vacancy
    job_titles = [vacancy.title for vacancy in Vacancy.query.distinct(Vacancy.title).all()]
    employers = [vacancy.employer for vacancy in Vacancy.query.distinct(Vacancy.employer).all()]
    cities = [vacancy.location for vacancy in Vacancy.query.distinct(Vacancy.location).all()]
    employment_types = [vacancy.employment for vacancy in Vacancy.query.distinct(Vacancy.employment).all()]

    # Возвращаем данные в формате JSON
    return jsonify({
        'jobTitles': job_titles,
        'employers': employers,
        'cities': cities,
        'employmentTypes': employment_types
    })

# Маршрут для фильтрации вакансий на основе переданных параметров
@main.route('/filtered-vacancies', methods=['POST'])
def filtered_vacancies():
    # Получаем фильтры из запроса POST
    filters = {
        'jobTitle': request.form.get('jobTitle', None),
        'employer': request.form.get('employer', None),
        'city': request.form.get('city', None),
        'employmentType': request.form.get('employmentType', None),
        'sort': request.form.get('sort', 'city')  # По умолчанию сортируем по городу
    }

    # Создаем базовый запрос Vacancy
    query = Vacancy.query

    # Применяем фильтры к запросу
    if filters['jobTitle']:
        query = query.filter_by(title=filters['jobTitle'])
    if filters['employer']:
        query = query.filter_by(employer=filters['employer'])
    if filters['city']:
        query = query.filter_by(location=filters['city'])
    if filters['employmentType']:
        query = query.filter_by(employment=filters['employmentType'])

    # Применяем сортировку к запросу вакансий
    if filters['sort'] == 'title':
        query = query.order_by(Vacancy.title)
    elif filters['sort'] == 'employer':
        query = query.order_by(Vacancy.employer)
    else:  # По умолчанию сортировка по городу
        query = query.order_by(Vacancy.location)

    # Выполняем запрос и получаем список вакансий
    vacancies = query.all()

    # Подготавливаем данные в формате JSON для отправки клиенту
    vacancies_data = []
    for vacancy in vacancies:
        vacancies_data.append({
            'vacancy_id': vacancy.vacancy_id,
            'title': vacancy.title,
            'employer': vacancy.employer,
            'location': vacancy.location,
            'employment': vacancy.employment,
            'salary': vacancy.salary,
            'published_at': vacancy.published_at.strftime('%Y-%m-%d') if vacancy.published_at else ''
        })

    # Возвращаем данные в формате JSON
    return jsonify(vacancies_data)
