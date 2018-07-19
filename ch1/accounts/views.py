from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404,resolve_url

from django.contrib.auth import login as auth_login
from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import LoginForm, SignupForm,ProfileForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .models import Profile

import sys
sys.path.append('..')
from travel.models import Post



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
    return render(request, 'accounts/profile.html',{
        'profiles':pf,
        'list':post
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
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('travel:post_new')
    else:
        form = ProfileForm()
    return render(request, 'accounts/newprofile.html', {
        'form':form,
    })


def profileEdit(request):
    profile = get_object_or_404(Profile, User=user_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect(profile)
        else:
            form = ProfileForm(instance=profile)
        return render(request, 'accounts/newprofile.html',{
            'form':form,
        })