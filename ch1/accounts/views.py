from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404,resolve_url

from django.contrib.auth import login as auth_login
from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import LoginForm, SignupForm,ProfileMForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .models import Profile

import sys
sys.path.append('..')
from travel.models import Post, Booking



class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return resolve_url('profile')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('accounts:profile')

signup = SignupView.as_view()


def skignup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            auth_login(request, user)  # 로그인 처리


            return redirect('accounts:profile')
        else:
            form = SignupForm()
        return render(request, 'accounts/signup_form.html',{
            'form':form,
        })

@login_required     # settings.LOGIN_URL
def profile(request):
    pf = Profile.objects.all()
    pf = pf.filter(user=request.user)
    post = Post.objects.all()
    post = post.filter(user=request.user)
    bk = Booking.objects.filter(content__user=request.user)
    for i in pf:
        z = i.nextCountry.all()
    for i in pf:
        k = i.visitedCountry.all()


    return render(request, 'accounts/profile.html',{
        'profiles': pf,
        'list': post,
        'bk': bk,
        'k' : k,
        'z' : z,
    })


def login(request):
    providers = []
    for provider in get_providers():     # settings/INSTALLED_APPS 내에서 활성화된 목록
        # social_app속성은 provider에는 없는 속성입니다.
        try:
            # 실제 Provider 별 Client id/secret 이 등록이 되어있는가?
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    return auth_login(request,
        authentication_form=LoginForm,
        template_name='accounts/login_form.html',
        extra_context={'providers': providers})

def new_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileMForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('travel:post_new')
        else:
            print(form.errors)
    else:
        form = ProfileMForm(instance=profile)
    return render(request, 'accounts/newprofile.html', {
        'form':form,
    })


def profileEdit(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileMForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('accounts:profile')
        else:
            print(form.errors)
    else:
        form = ProfileMForm(instance=profile)
    return render(request, 'accounts/profile_edit.html', {
        'form':form,
    })

import requests
from bs4 import BeautifulSoup
import sqlite3
import urllib.request

def country(request):
    url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states'

    html = requests.get(url).text

    soup = BeautifulSoup(html,'html.parser')

    nationayliy = soup.select('b .flagicon img')
    country = soup.select('b .flagicon + a')
    m=[]
    for i in country:
        l = i.text
        m.append(l)

    conn = sqlite3.connect('/Users/javis/Desktop/TFS-master/ch1/mysite/db44.sqlite3')
    curs = conn.cursor()

    k=0
    http = 'https:'
    for j, i in enumerate(nationayliy):
        image = i.get('src')
        img = http + image
        urllib.request.urlretrieve(img, '/home/todayfriend/TSF1/ch1/mysite/mysite/media/{}.png'.format(j))
        curs.execute('insert into accounts_country values ("{}","{}","{}.png")'.format(k, m[k], k))
        k = k+1

    conn.commit()
    conn.close()
    return render(request, 'accounts/country.html')