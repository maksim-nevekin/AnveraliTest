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
        "text_on_page": "Необходимо создать сайт на Django, который \n\
            включает в себя админ панель и две формы \n\
            регистрации для заказчиков и исполнителей\n\
            соответственно. Минимальный набор полей в\n\
            профилях (имя, контактные данные, опыт).\n\
            БД PostgreSQL",
    }

    return render(request, "main/about.html", context)

project = "https://github.com/maksim-nevekin/AnveraliTest/tree/main"

def info(request):
    context = {
        "title": "Тестовое задание от Anverali",
        "content": "Исполнитель - Невекин Максим",
        "text_on_page": f"Страница проекта - {project}\n\
            Telegram - https://t.me/Jothis20\n\
            Почта - maksim.new99@gmail.com\n\
            Телефон - 89200394763",
    }

    return render(request, "main/info.html", context)
