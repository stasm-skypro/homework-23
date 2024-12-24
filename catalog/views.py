"""
Контроллеры, определённые внутри приложения catalog.
"""

from django.http import HttpResponse

from django.shortcuts import render


def home_page(request):
    """
    Принимает и обрабатывает параметр request из шаблона home.html.
    :param request:
    :return:
    """
    return render(request, "home.html")


def contacts_page(request):
    """
    Принимает и обрабатывает параметр request из шаблона contacts.html.
    :param request:
    :return:
    """
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            "Спасибо %s! Ваш телефон - %s. Ваше сообщение  - %s."
            % (name, phone, message)
        )

    return render(request, "contacts.html")
