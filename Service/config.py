import os

# Класс Config определяет конфигурационные параметры для приложения Flask
class Config:
    # SQLALCHEMY_DATABASE_URI задает URL-адрес для подключения к базе данных.
    # Значение берется из переменной окружения 'DATABASE_URL'.
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
    # SQLALCHEMY_TRACK_MODIFICATIONS отключает сигнализацию о модификациях объектов,
    # что позволяет сэкономить ресурсы. Значение False отключает эту функциональность.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
