from django.shortcuts import render


def index(request):

    context = {
        "title": "Главная",
        "content": "Тестовое задание для Anverali",
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "О задании",
        "content": "О нас",
        "text_on_page": "Сайт включает в себя админ панель и две формы регистрации для заказчиков и исполнителей соответственно",
    }

    return render(request, "main/about.html", context)
