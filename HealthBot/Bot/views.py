from django.shortcuts import render


# rendering the landing screen

def landingScreen(request):
    return render(request,template_name = 'landingscreen.html')


