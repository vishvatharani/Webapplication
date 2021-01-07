from django.shortcuts import render


def about(request):
    # return HttpResponse("about")
    return render(request, 'about.html')


def homepage(request):
    # return HttpResponse("Home Page")
    return render(request, 'homepage.html')

