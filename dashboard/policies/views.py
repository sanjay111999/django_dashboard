from django.http import HttpResponse


def index(request):
    return HttpResponse("<H1>Hello, world.</H1> You're at the polls index.")