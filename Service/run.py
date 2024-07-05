from app import create_app

# Создаем экземпляр приложения Flask, используя функцию create_app
app = create_app()

# Убедимся, что код ниже выполняется только если скрипт запущен напрямую
if __name__ == '__main__':
    # Запускаем приложение Flask в режиме отладки
    app.run(debug=True, port=8000)
