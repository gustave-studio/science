from django.shortcuts import render

# Create your views here.
def topfunc(request):
  return render(request, 'top.html')