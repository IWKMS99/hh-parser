/**
 * Функция для загрузки вакансий с сервера и отображения их в таблице.
 */
function fetchVacancies() {
    const progressBar = document.querySelector('#progressBar'); // Найти элемент прогресс-бара
    progressBar.value = 0; // Установить значение прогресс-бара в 0
    statusText.innerText = 'Загрузка...'; // Обновить текст статуса

    // Выполнить GET-запрос на сервер для получения данных о вакансиях
    fetch('/update-vacancies', {
        method: 'GET'
    })
    .then(response => response.json()) // Преобразовать ответ сервера в формат JSON
    .then(data => {
        const tbody = document.querySelector('#vacanciesTable tbody'); // Найти тело таблицы вакансий
        tbody.innerHTML = ''; // Очистить текущее содержимое таблицы
        progressBar.value = 50; // Обновить прогресс-бар до 50%

        // Пройтись по всем полученным вакансиям и добавить их в таблицу
        data.forEach(vacancy => {
            const row = document.createElement('tr'); // Создать новый ряд таблицы
            row.innerHTML = `
                <td>${vacancy.vacancy_id}</td>
                <td>${vacancy.title}</td>
                <td>${vacancy.employer}</td>
                <td>${vacancy.location}</td>
                <td>${vacancy.employment}</td>
                <td>${formatSalary(vacancy.salary)}</td>
                <td>${vacancy.published_at}</td>
            `; // Заполнить ряд данными вакансии
            tbody.appendChild(row); // Добавить ряд в таблицу
        });

        progressBar.value = 100; // Обновить прогресс-бар до 100%
        statusText.innerText = ''; // Очистить текст статуса
    })
    .catch(error => {
        console.error('Ошибка при загрузке данных:', error); // Вывести ошибку в консоль
        progressBar.value = 0; // Сбросить прогресс-бар в случае ошибки
    });
}

/**
 * Функция для форматирования зарплаты.
 * @param {string|null|undefined} salary - Зарплата, которую нужно форматировать.
 * @returns {string} - Отформатированная зарплата.
 */
function formatSalary(salary) {
    if (salary === null || salary === undefined) {
        return 'Не указано'; // Если зарплата не указана, вернуть соответствующее сообщение
    } else {
        return salary.replace(/\bNone\b/g, 'Не указано'); // Заменить 'None' на 'Не указано'
    }
}
