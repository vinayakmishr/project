from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SinUpForm

# Create your views here.
def frontpage(request):
    return render(request, 'app/frontpage.html')

def sinup(request):
    if request.method == 'POST':
        form = SinUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = SinUpForm()
    return render(request,'app/sinup.html',{'form':form})