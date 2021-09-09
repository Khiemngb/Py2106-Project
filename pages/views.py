from django.http import HttpResponse
from django.shortcuts import render

# Function will return to client
def home_page(request):
    data = {
        "products": [{
            "name": "Tivi 26 inch",
            "price": "10.000",
        }, {
            "name": "Tivi 27 inch",
            "price": "10.000",
        }, {
            "name": "Tivi 28 inch",
            "price": "10.000",
        }]
    }

    return render(request, 'pages/home.html', data)
