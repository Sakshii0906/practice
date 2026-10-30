from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    data={
        "name":"Sakshi",
        "course":"Data Science",
        "city":"Vadodara"
    }
    return render(
        request,
        "College/home.html",
        data)
    

def about(request):
    data={
        "name":"Sakshi Singh",
        "course":"BCA",
        "city":"Vadodara"
    }
    return render(
        request,
        "College/about.html",
        {"template_name": "base.html"}
    )

def contact(request):
    return render(
        request,
        "College/contact.html",
        {"template_name": "base.html"}
    )

def courses(request):
    return render(request,'College/courses.html',{"template-name": "base.html"})

    