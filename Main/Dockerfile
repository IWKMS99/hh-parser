# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы с зависимостями
COPY requirements.txt requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем оставшиеся файлы
COPY . .

# Устанавливаем переменные окружения для Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Открываем порт
EXPOSE 5000

# Запускаем приложение
CMD ["flask", "run"]
