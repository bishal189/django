from django.shortcuts import render

# Create your views here.
def dailynote(request):
    return render(request,'dailynote.html')