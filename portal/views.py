from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Se você estiver vendo isso é porque deu certo, Parabéns</h1>")

def sobre(request):
    return HttpResponse("sobre")
