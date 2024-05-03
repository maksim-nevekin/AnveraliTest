from django.shortcuts import render


def index(request):

    context = {
        "title": "Главная",
        "content": "Тестовое задание от Anverali",
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Тестовое задание от Anverali",
        "content": "Суть задания",
        "text_on_page": "Необходимо создать сайт на Django,\
            который включает в себя админ панель и две формы регистрации для заказчиков и исполнителей соответственно.\
            Минимальный набор полей в профилях (имя, контактные данные, опыт). БД PostgreSQL",
    }

    return render(request, "main/about.html", context)

project = "https://github.com/maksim-nevekin/AnveraliTest/tree/main"

def info(request):
    context = {
        "title": "Тестовое задание от Anverali",
        "content": "Исполнитель - Невекин Максим",
        "text_on_page": f"Страница проекта - {project}\n\
            Telegram - \
            Почта - maksim.new99@gmail.com\
            Телефон - 89200394763",
    }

    return render(request, "main/info.html", context)