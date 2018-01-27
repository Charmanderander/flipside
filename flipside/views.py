from django.shortcuts import render
from flipside.forms import Form

def index(request):
    return render(request, 'index.html', {'form' : Form})

def team1(request):
    return render(request, 'team1.html', {'form' : Form})

def team2(request):
    return render(request, 'team2.html', {'form' : Form})

def team3(request):
    return render(request, 'team3.html', {'form' : Form})

def experience(request):
    return render(request, 'experience.html', {'form' : Form})

def faq(request):
    return render(request, 'faq.html', {'form' : Form})

def blog(request):
    return render(request, 'blog.html', {'form' : Form})

def contact(request):
    return render(request, 'contact.html', {'form' : Form})

