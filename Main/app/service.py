import requests

# Функция fill_db заполняет базу данных вакансиями, полученными с API hh.ru
def fill_db(db, Vacancy):
    # Удаляем все существующие записи в таблице Vacancy
    db.session.query(Vacancy).delete()
    db.session.commit()

    # Проходимся по 10 страницам вакансий
    for x in range(10):
        # Отправляем GET-запрос к API hh.ru для получения вакансий с текстом 'python'
        response = requests.get('https://api.hh.ru/vacancies', params={'text': 'python', 'page': x, 'per_page': 100})
        # Получаем список вакансий из ответа API
        vacancies = response.json()['items']

        # Проходимся по каждой вакансии в списке
        for vac in vacancies:
            # Создаем новый объект Vacancy с данными из API
            new_vacancy = Vacancy(
                vacancy_id=vac['id'],
                title=vac['name'],
                employer=vac['employer']['name'],
                location=vac['area']['name'],
                employment=vac['employment']['name'],
                salary=f"{vac['salary']['from']} - {vac['salary']['to']}" if vac['salary'] else None,
                published_at=vac['published_at']
            )
            # Добавляем новый объект Vacancy в сессию
            db.session.add(new_vacancy)

    # Коммитим все изменения в базу данных
    db.session.commit()
