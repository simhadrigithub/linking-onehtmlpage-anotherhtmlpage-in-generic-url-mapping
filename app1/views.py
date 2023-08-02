from django.shortcuts import render

# Create your views here.
def first_image(request):
    return render(request,'first_image.html')