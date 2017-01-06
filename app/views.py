from django.shortcuts import render, render_to_response

# Create your views here.
def Start(request):
    return render_to_response('index.html');
