"""
Контроллеры, определённые внутри приложения catalog.
"""

from django.shortcuts import render
from catalog.models import Product
from catalog.forms import ContactForm


def home_page(request):
    """
    Принимает и обрабатывает параметр request из шаблона home.html.
    :param request:
    :return:
    """
    recent_products = Product.objects.filter(category__name="Продукты")
    for product in recent_products:
        print("Последние %s товаров:" % len(recent_products))
        print(product)

    return render(request, "home.html", context={"data": recent_products})


# def contacts_page(request):
#     """
#     Принимает и обрабатывает параметр request из шаблона contacts.html.
#     :param request:
#     :return:
#     """
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         return HttpResponse(
#             "Спасибо %s! Ваш телефон - %s. Ваше сообщение  - %s."
#             % (name, phone, message)
#         )
#
#     return render(request, "contacts.html")


# Перепишем контроллер по-другому. Вместо HttpResponse просто выведем страницу success.html с сообщением.
def contacts_page(request):
    """Принимает и обрабатывает параметр request из шаблона contacts.html."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в таблицу catalog_contacts
            return render(request, "success.html")
    else:
        form = ContactForm()
    return render(request, "contacts.html", {"form": form})
