from django.shortcuts import render, redirect,get_object_or_404

from ch1 import travel
from .forms import BookMForm,PostMForm
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import Post,Country,Booking
from .models import City as ct
import os
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


import sys
sys.path.append('..')
from accounts import models

def main(request):
    return render(request, 'travel/_main.html')

def local_list(request):
    queryset = ct.objects.all()

    queryset1 = Post.objects.all()

    seoul = queryset1.filter(representation='True', City__city='Seoul', confirm='True')
    busan = queryset1.filter(representation='True', City__city='Busan', confirm='True')
    jeonju = queryset1.filter(representation='True', City__city='Jeonju', confirm='True')
    jeju = queryset1.filter(representation='True', City__city='Jeju', confirm='True')
    gyeongju = queryset1.filter(representation='True', City__city='Gyeongju', confirm='True')
    return render(request, 'travel/local_list.html', {
        'local' : queryset,
        'seoul': seoul,
        'jeju': jeju,
        'busan': busan,
        'jeonju' : jeonju,
        'gyeongju': gyeongju,
    })

def local_detail(request, City):
    queryset = Post.objects.all()
    qs = queryset.filter(City__city=City, confirm='True')
    img = ct.objects.all()
    img = img.filter(city=City)
    for i in img:
        img = i.img
        print(img.url)
    return render(request, 'travel/local_detail.html',{
        'local_list': qs,
        'img':img
    })


def local_detail_form(request, City, pk):
    queryset = Post.objects.all()


    qs = queryset.filter(pk=pk)
    qs1 = Post.objects.get(pk=pk)
    pf = models.Profile.objects.all()
    pf = pf.filter(user=qs1.user)
    FY, FM, FD = str(qs1.SeasonFrom).split('-')
    TY, TM, TD = str(qs1.SeasonTo).split('-')
    SH, SM = str(qs1.MeetingTime).split(':')
    H1, M1 = str(qs1.Duration).split(':')
    H = int(SH)+int(H1)
    M = int(SM)+int(M1)
    l = len(qs1.NotDate.split(','))
    b=[]
    for i in range(l):
        a = qs1.NotDate.split(',')[i].split('-')
        a[1] = str(int(a[1])-1)
        s = ','.join(a)
        b.append(s)
    for i in pf:
        z = i.nextCountry.all()
    for i in pf:
        k = i.visitedCountry.all()
    print(qs1.Map)
    return render(request, 'travel/local_detail_form.html',{
        'local_detail': qs,
        'filter': filter,
        'profiles': pf,
        'FY': FY,
        'FM': FM,
        'FD': FD,
        'TY': TY,
        'TM': TM,
        'TD': TD,
        'SH': SH,
        'SM': SM,
        'M': M,
        'H': H,
        'H1': H1,
        'M1': M1,
        'b': b,
        'z': z,
        'k': k,
    })



def post_new(request):
    if request.method == 'POST':
        form = PostMForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('travel:complete')
    else:
        form = PostMForm()
    return render(request, 'travel/post_form.html', {
        'form': form,
    })

def post_edit(request, City, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostMForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('accounts:profile')
    else:
        form = PostMForm(instance=post)
    return render(request, 'travel/post_form_edit.html',{
        'form':form,
    })

def post_delete(reuqest, City ,pk):
    delete = get_object_or_404(pk=pk)
    delete.delete()


def postcomplete(request):
    return render(request, 'travel/complete.html')


def booking(request, City, pk):
    content = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = BookMForm(request.POST, request.FILES)
        if form.is_valid():
            print('false')
            booking = form.save(commit=False)
            booking.content = content
            booking.save()
            return HttpResponseRedirect(reverse('travel:bookingcomplete', args=[City, pk]))
        else:
            print(form.errors)
    else:
        form = BookMForm()

    qs1 = Post.objects.get(pk=pk)
    post = Post.objects.all()
    post = post.filter(pk=pk)
    l = len(qs1.NotDate.split(','))
    b=[]
    for i in range(l):
        a = qs1.NotDate.split(',')[i].split('-')
        a[1] = str(int(a[1])-1)
        s = '-'.join(a)
        b.append(s)
    print(b)
    for i in b:
        print(i)
    return render(request, ['travel/booking.html','widgets/booking_date.html'], {
        'form': form,
        'post': post,
        'b': b,
    })

def bookingcomplete(request, City, pk):

    return render(request, 'travel/bookingcomplete.html')


def country_list(request):
    qs = Country.objects.all()
    q = request.GET.get('q')
    qs = qs.filter(name__icontains=q)
    results = [{'id': country.id, 'text': country.name} for country in qs]
    return JsonResponse({
        'results': results,
    })

def datewidget(request, City, pk):
    qs1 = Post.objects.get(pk=filter)
    l = len(qs1.NotDate.split(','))
    b = []
    for i in range(l):
        a = qs1.NotDate.split(',')[i].split('-')
        a[1] = str(int(a[1]) - 1)
        s = ','.join(a)
        b.append(s)
    return render(request, 'widgets/booking_date.html', {
        'b': b,
    })

def notbooking(request, City, pk):
    qs1 = Post.objects.get(pk=pk)
    post = Post.objects.all()
    post = post.filter(pk=pk)
    l = len(qs1.NotDate.split(','))
    b = []
    for i in range(l):
        a = qs1.NotDate.split(',')[i].split('-')
        a[1] = str(int(a[1]) - 1)
        s = ','.join(a)
        b.append(s)
    return render(request, 'widgets/booking_date.html', {
        'b':b
    })