from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout

from accounts.forms import AuthenticationForm, RegistrationForm
# Create your views here.

def login(request):
    """
    Log in view
    """
    if request.user.is_authenticated():
        return redirect('/accounts/login_successful')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/accounts/login_successful')
            else:
                form_errors = 'User or password is wrong'
                return render_to_response('accounts/login.html', {
                        'form': form, 'formerrors': form_errors,
                            }, context_instance=RequestContext(request))
        else:
            form_errors = form.errors
            return render_to_response('accounts/login.html', {
                        'form': form, 'formerrors': form_errors,
                            }, context_instance=RequestContext(request))
    else:
        form = AuthenticationForm()
    return render_to_response('accounts/login.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def login_successful(request):
    """
    Login was successful
    """
    if request.user.is_authenticated():
        user = request.user
        user.ip = request.META.get('REMOTE_ADDR')
        user.save()
        return render(request, 'accounts/login_successful.html', {'ip': user.ip})
    else:
        return redirect('/accounts/login')

def register(request):
    """
    User registration view.
    """
    if not request.user.is_authenticated() or not request.user.is_admin:
        return render(request, 'accounts/permission_denied.html', {})
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.ip = request.META.get('REMOTE_ADDR')
            user.save()
            return redirect('/accounts/login')
    else:
        form = RegistrationForm()
    return render_to_response('accounts/register.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def logout(request):
    """
    Log out view
    """
    django_logout(request)
    return redirect('/accounts/login')
