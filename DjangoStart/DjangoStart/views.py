from django.shortcuts import render, redirect
#from django.http import HttpResponseRedirect
#from django.urls import reverse
from django.contrib import messages

def home(request):
    if request.method == "POST":
        code = request.POST.get('code', '')
        if code == "original-monitor":
            #return HttpResponseRedirect(reverse('feed'))
            messages.success(request, "Code is correct! Redirecting to feed...")
            return redirect("feed")
        else:
            messages.error(request, "Invalid code! Please try again.")
    return render(request, 'homepage.html')

def host(request):
    return render(request, 'admin.html')

def feed(request):
    return render(request, 'feed-page.html')