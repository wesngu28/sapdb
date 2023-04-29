from django.shortcuts import render
from sapi.views import getFoods

def my_view(request):
    response = getFoods(request)
    data = { "data": response.data }
    return render(request, 'my_template.html', data)
