from django .shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')


def team(request):
    return render(request, 'team.html')


def quote(request):
    return render(request, 'quote.html')
