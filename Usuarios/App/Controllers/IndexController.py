from django.shortcuts import render, HttpResponse

class IndexController():
    def index(request):
        #return HttpResponse('<h1>Isaac Fimbres<h1>%s' % anio)
        return render(request,'views/index.html')
    def home(request):
        #return HttpResponse('<h1>Isaac Fimbres<h1>%s' % anio)
        return render(request,'views/index.html')
    def about(request):
        #return HttpResponse('<h1>Isaac Fimbres<h1>%s' % anio)
        return render(request,'views/about.html')
    def admin(request):
        #return HttpResponse('<h1>Isaac Fimbres<h1>%s' % anio)
        return render(request,'views/about.html')