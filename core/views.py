from django.shortcuts import render, HttpResponse
# import random
# from datetime import datetime

# Create your views here.

# =============================================================

# def test(request):
#     x = random.randint(1, 100)
#     return HttpResponse(f"А Теперь, ИДИ НАХУЙ! - {x} раз")

# def custom(request):
#     return HttpResponse("Привет ты на кастомной странице...")

# now = datetime.now()
# def homework(request):
#     return HttpResponse(f"Время: {now}")

# ==============================================================

# def test(request):
#     return render(request, 'index.html', {})

# def test2(request):
#     return render(request, 'second.html', {})

def mainVeiew(request):
    return render(request, 'main_page.html', {})

def contacts_page(request):
    return render(request, 'contacts_page.html', {})

