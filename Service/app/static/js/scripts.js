// scripts.js

// Обработчик события DOMContentLoaded для загрузки страницы
document.addEventListener('DOMContentLoaded', function() {
    loadFilters(); // Загрузка данных для фильтров при загрузке страницы
    fetchFilteredVacancies(); // Загрузка и отображение изначальных данных таблицы

    // Обработчик события для формы фильтрации
    const filterForm = document.getElementById('filterForm');
    filterForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию
        fetchFilteredVacancies(); // Выполняем запрос на фильтрацию вакансий
    });

    // Обработчик события для выбора сортировки
    const sortSelect = document.getElementById('sort');
    sortSelect.addEventListener('change', function() {
        fetchFilteredVacancies(); // Выполняем запрос на фильтрацию вакансий при изменении сортировки
    });
});

// Функция для загрузки данных фильтров
function loadFilters() {
    fetch('/load-filters', { // Отправляем GET запрос на сервер для получения фильтров
        method: 'GET'
    })
    .then(response => response.json()) // Обрабатываем полученный ответ как JSON
    .then(data => {
        // Пополняем выпадающие списки данными
        populateDropdown('jobTitle', data.jobTitles);
        populateDropdown('employer', data.employers);
        populateDropdown('city', data.cities);
        populateDropdown('employmentType', data.employmentTypes);
    })
    .catch(error => console.error('Ошибка при загрузке фильтров:', error)); // Обрабатываем ошибки
}

// Функция для заполнения выпадающего списка данными
function populateDropdown(id, options) {
    const dropdown = document.getElementById(id);
    dropdown.innerHTML = '<option value="">Все</option>'; // Очищаем и добавляем первую опцию
    options.forEach(option => {
        dropdown.innerHTML += `<option value="${option}">${option}</option>`; // Добавляем опции из полученных данных
    });
}

// Функция для выполнения запроса на фильтрацию вакансий
function fetchFilteredVacancies() {
    const formData = new FormData(document.getElementById('filterForm')); // Получаем данные формы
    const sort = document.getElementById('sort').value; // Получаем выбранное значение сортировки

    formData.append('sort', sort); // Добавляем значение сортировки в FormData

    fetch('/filtered-vacancies', { // Отправляем POST запрос на сервер для получения отфильтрованных вакансий
        method: 'POST',
        body: formData // Передаем FormData в теле запроса
    })
    .then(response => response.json()) // Обрабатываем полученный ответ как JSON
    .then(data => {
        const tbody = document.querySelector('#filteredVacancies tbody');
        tbody.innerHTML = ''; // Очищаем текущие данные в таблице

        // Добавляем строки с данными в таблицу
        data.forEach(vacancy => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${vacancy.vacancy_id}</td>
                <td>${vacancy.title}</td>
                <td>${vacancy.employer}</td>
                <td>${vacancy.location}</td>
                <td>${vacancy.employment}</td>
                <td>${formatSalary(vacancy.salary)}</td>
                <td>${vacancy.published_at}</td>
            `;
            tbody.appendChild(row); // Добавляем строку в конец таблицы
        });
    })
    .catch(error => console.error('Ошибка при загрузке отфильтрованных данных:', error)); // Обрабатываем ошибки
}

// Функция для форматирования зарплаты
function formatSalary(salary) {
    if (!salary) {
        return 'Не указано'; // Возвращаем 'Не указано', если зарплата не указана
    } else {
        return salary.replace(/\bNone\b/g, 'Не указано'); // Заменяем 'None' на 'Не указано'
    }
}
