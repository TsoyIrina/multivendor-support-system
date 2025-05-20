from django.shortcuts import render, redirect
from django.urls import reverse

from api import authenticate


def auth(request):
    context = {
        'error': ''
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        res = authenticate(username, password)
        if res['is_ok']:
            if res['user'] == 'client':
                return redirect(reverse('client:profile'))
            elif res['user'] == 'employee':
                return redirect(reverse('employee:application'))
        else:
            context = {
                'error': res['response']
            }
    return render(request, 'auth.html', context)
