from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .models import register, Comment
# from .forms import *
from django.http import *
from django.contrib import auth
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from . forms import UserForm
from django.contrib.auth.forms import UserChangeForm
from .forms import EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Create your views here.

@csrf_exempt
def savecomment(request):
    type=request.GET.get('news_type')
    if request.method=='POST':
        com=Comment.objects.create(name=str(request.POST.get('name')), email=str(request.POST.get('email')), website=str(request.POST.get('website')), comment=str(request.POST.get('comment')), type=type)
        com.save()
        if request.GET.get('news_type') == 'breaking':
            return redirect((reverse('breaking')))
        elif request.GET.get('news_type') == 'political':
            return redirect((reverse('political')))
        elif request.GET.get('news_type') == 'business':
            return redirect((reverse('business')))
        elif request.GET.get('news_type') == 'entertainment':
            return redirect((reverse('entertainment')))
        elif request.GET.get('news_type') == 'health':
            return redirect((reverse('health')))
        elif request.GET.get('news_type') == 'lifestyle':
            return redirect((reverse('lifestyle')))
        elif request.GET.get('news_type') == 'technology':
            return redirect((reverse('technology')))
        elif request.GET.get('news_type') == 'videos':
            return redirect((reverse('videos')))
        elif request.GET.get('news_type') == 'sports':
            return redirect((reverse('sports')))
        else:
            return redirect(type)
    else:
        return redirect(type)

def admin(request):
    return HttpResponseRedirect(reverse('admin:index'))

def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return redirect('website:index')

def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    import requests
    import bs4

    res = requests.get('https://www.geo.tv/category/amazing')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    news_data = []
    for list_element in soup.select('.list'):
        list_element.find('a')['target'] = '_blank'
        news_data.append(str(list_element))

    res2 = requests.get('https://www.theguardian.com/world')
    type(res2)
    soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')
    type(soup2)
    news_data2 = []
    for list_element2 in soup2.select('.headline-list__link'):
        list_element2.find('a')['target'] = '_blank'
        news_data2.append(str(list_element2))

    # if request.user.is_authenticated:
    return render(request, 'website/index.html', {'elements': news_data,'elements2':news_data2})
    # else:
    #     return HttpResponseRedirect(reverse('health'))


def base(request):

    return render(request, 'website/base.html')

def breaking(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/amazing')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    news_data = []
    for list_element in soup.select('.list'):
        list_element.find('a')['target'] = '_blank'
        news_data.append(str(list_element))

    res2 = requests.get('https://www.theguardian.com/world')
    type(res2)
    soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')
    type(soup2)
    news_data2 = []
    for list_element2 in soup2.select('.headline-list__link'):
        list_element2.find('a')['target'] = '_blank'
        news_data2.append(str(list_element2))

    # if request.user.is_authenticated:
    return render(request, 'website/breaking.html', {'elements': news_data, 'elements2': news_data2, 'query': Comment.objects.filter(type='breaking'),'news_type':'breaking'})
    # else:
    #     return HttpResponseRedirect(reverse('health'))


def business(request):
    import requests
    import bs4
    res=requests.get('https://www.geo.tv/category/business')
    type(res)
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    type(soup)
    news_data = []
    for list_element in soup.select('.list'):
        list_element.find('a')['target'] = '_blank'
        news_data.append(str(list_element))

    res2 = requests.get('https://www.theguardian.com/world')
    type(res2)
    soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')
    type(soup2)
    news_data2 = []
    for list_element2 in soup2.select('.headline-list__link'):
        list_element2.find('a')['target'] = '_blank'
        news_data2.append(str(list_element2))

    # if request.user.is_authenticated:
    return render(request, 'website/business.html', {'elements': news_data, 'elements2': news_data2, 'query': Comment.objects.filter(type='business'),'news_type':'business'})
    # else:
    #     return HttpResponseRedirect(reverse('health'))


def contact(request):
    return render(request, 'website/contact.html')

def entertainment(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/entertainment')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    news_data = []
    for list_element in soup.select('.list'):
        list_element.find('a')['target'] = '_blank'
        news_data.append(str(list_element))

    res2 = requests.get('https://www.theguardian.com/world')
    type(res2)
    soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')
    type(soup2)
    news_data2 = []
    for list_element2 in soup2.select('.headline-list__link'):
        list_element2.find('a')['target'] = '_blank'
        news_data2.append(str(list_element2))

    # if request.user.is_authenticated:
    return render(request, 'website/entertainment.html', {'elements': news_data, 'elements2': news_data2, 'query': Comment.objects.filter(type='entertainment'),'news_type':'entertainment'})
    # else:
    #     return HttpResponseRedirect(reverse('health'))


def events(request):
    return render(request, 'website/events.html')

def lifestyle(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/health')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    news_data = []
    for list_element in soup.select('.list'):
        list_element.find('a')['target'] = '_blank'
        news_data.append(str(list_element))

    res2 = requests.get('https://www.theguardian.com/world')
    type(res2)
    soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')
    type(soup2)
    news_data2 = []
    for list_element2 in soup2.select('.headline-list__link'):
        list_element2.find('a')['target'] = '_blank'
        news_data2.append(str(list_element2))

    # if request.user.is_authenticated:
    return render(request, 'website/lifestyle.html', {'elements': news_data, 'elements2': news_data2, 'query': Comment.objects.filter(type='lifestyle'),'news_type':'lifestyle'})
    # else:
    #     return HttpResponseRedirect(reverse('health'))


# def loginform(request):
#     return render(request, 'website/index.html')

def political(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/pakistan')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    news_data = []
    for list_element in soup.select('.list'):
        list_element.find('a')['target'] = '_blank'
        news_data.append(str(list_element))

    res2 = requests.get('https://www.theguardian.com/world')
    type(res2)
    soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')
    type(soup2)
    news_data2 = []
    for list_element2 in soup2.select('.headline-list__link'):
        list_element2.find('a')['target'] = '_blank'
        news_data2.append(str(list_element2))

    # if request.user.is_authenticated:
    return render(request, 'website/political.html', {'elements': news_data, 'elements2': news_data2, 'query': Comment.objects.filter(type='political'),'news_type':'political'})
    # else:
    #     return HttpResponseRedirect(reverse('health'))


def sports(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/sports')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    news_data = []
    for list_element in soup.select('.list'):
        list_element.find('a')['target'] = '_blank'
        news_data.append(str(list_element))

    res2 = requests.get('https://www.theguardian.com/world')
    type(res2)
    soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')
    type(soup2)
    news_data2 = []
    for list_element2 in soup2.select('.headline-list__link'):
        list_element2.find('a')['target'] = '_blank'
        news_data2.append(str(list_element2))

    # if request.user.is_authenticated:
    return render(request, 'website/sports.html', {'elements': news_data, 'elements2': news_data2, 'query': Comment.objects.filter(type='sports'),'news_type':'sports'})
    # else:
    #     return HttpResponseRedirect(reverse('health'))


def technology(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/sci-tech')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    news_data = []
    for list_element in soup.select('.list'):
        list_element.find('a')['target'] = '_blank'
        news_data.append(str(list_element))

    res2 = requests.get('https://www.theguardian.com/world')
    type(res2)
    soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')
    type(soup2)
    news_data2 = []
    for list_element2 in soup2.select('.headline-list__link'):
        list_element2.find('a')['target'] = '_blank'
        news_data2.append(str(list_element2))

    # if request.user.is_authenticated:
    return render(request, 'website/technology.html', {'elements': news_data, 'elements2': news_data2, 'query': Comment.objects.filter(type='technology'),'news_type':'technology'})
    # else:
    #     return HttpResponseRedirect(reverse('health'))


def videos(request):
    return render(request, 'website/videos.html')

def health(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/health')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)

    news_data = []
    for list_element in soup.select('.list'):
        list_element.find('a')['target'] = '_blank'
        news_data.append(str(list_element))

    res2 = requests.get('https://www.theguardian.com/world')
    type(res2)
    soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')
    type(soup2)
    news_data2 = []
    for list_element2 in soup2.select('.headline-list__link'):
        list_element2.find('a')['target'] = '_blank'
        news_data2.append(str(list_element2))

    # if request.user.is_authenticated:
    return render(request, 'website/health.html', {'elements': news_data, 'elements2': news_data2, 'query': Comment.objects.filter(type='health'),'news_type':'health'})
    # else:
    #     return HttpResponseRedirect(reverse('health'))

def shortcodes(request):
    return render(request, 'website/shortcodes.html')

def single(request):
    return render(request, 'website/single.html')
def loginform(request):

    if request.method=='POST':

        # username2 = request.POST['username']
        # password2 = request.POST['password']
        #
        # register1=authenticate(name=username2, password=password2)
        #
        # # p=register.objects.filter(name=username2)
        #  # obj=register.objects.all()
        # # print (username2)
        #
        # if register1 is not None:
        #         auth.login(request, register)
        #         return render(request,'website/base.html')
        # else:
        #     return render(request, 'website/index.html')
        #
        #     messages.error(request,'username did not match ')



        username1=request.POST['usernamesignup']
        email=request.POST['emailsignup']
        password=request.POST['passwordsignup']
        print (username1)
        print (email)
        print (password)
        register.objects.create(name=username1,emailid=email,password=password)
        # reg=register.objects.create_user(name=username1,emailid=email,password=password)
        # reg.save()

        # disply data


        return HttpResponseRedirect('/loginform/')

    else:
        # return render(request, 'website/base.html')
        # obj = register.objects.all()

        return render(request, 'website/loginform.html')


def Admn(request):
    return render(request, 'Admn/index.html')

class UserFormView(View):
    form_class=UserForm
    template_name='website/registration_form.html'

    def get(self, request):
        form= self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('index')
        return render(request, self.template_name, {'form': form})

def profile(request):
        storage = messages.get_messages(request)
        args = {'user': request.user, 'message':storage}
        return render(request, 'website/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
            form = EditProfileForm(instance=request.user)
            args =  {'form': form}
            return render(request, 'website/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your new password has been saved!')
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
        else:
            return redirect('/change_password')

    else:
            form = PasswordChangeForm(user=request.user)
            args = {'form': form}
            return render(request, 'website/change_password.html', args)

