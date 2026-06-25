from django.shortcuts import render

# Create your views here.


# Landig page (home)
def landingPage(request):
    return render(request, 'Base/base_index.html')
