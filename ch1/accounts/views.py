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
from Personalized.models import PersonalizedTour



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
    for j in post:
        s = str(j.SeasonFrom)
        s = s.split('-')
        s = ','.join(s)
    for j in post:
        n = str(j.SeasonTo)
        n = n.split('-')
        n = ','.join(s)
    personal = PersonalizedTour.objects.all()
    ps = personal.filter(user=request.user)

    return render(request, 'accounts/profile.html',{
        'profiles': pf,
        'list': post,
        'bk' : bk,
        'k': k,
        'z': z,
        's': s,
        'n': n,
        'ps':ps,
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
        template_name='accounts/login.html',
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

    conn = sqlite3.connect('/Users/javis/Desktop/TFS-master/ch1/mysite/db12.sqlite3')
    curs = conn.cursor()

    k=0
    http = 'https:'
    for j, i in enumerate(nationayliy):
        image = i.get('src')
        img = http + image
        urllib.request.urlretrieve(img, '/Users/javis/Desktop/TFS-master/ch1/mysite/mysite/media/{}.png'.format(j))
        curs.execute('insert into accounts_country values ("{}","{}","{}.png")'.format(k, m[k], k))
        k = k+1

    conn.commit()
    conn.close()
    return render(request, 'accounts/country.html')