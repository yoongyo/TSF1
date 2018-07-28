from django.shortcuts import render, redirect,get_object_or_404
from .forms import BookMForm,PostMForm
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import Post,City,Country,Booking
from django.core.urlresolvers import reverse
from django.http import HttpResponse

import sys
sys.path.append('..')
from accounts import models

def main(request):
    return render(request, 'travel/_main.html')

def local_list(request):
    queryset = City.objects.all()

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
    path = request.path
    print(path)
    filter = path.split('/')[3]
    print(filter)
    qs = queryset.filter(City__city=filter, confirm='True')

    return render(request, 'travel/local_detail.html',{
        'local_list': qs
    })


def local_detail_form(request, City, pk):
    queryset = Post.objects.all()

    path = request.path
    print(path)
    filter = path.split('/')[4]
    print(filter)
    qs = queryset.filter(pk=filter)
    qs1 = Post.objects.get(pk=filter)
    pf = models.Profile.objects.all()
    pf = pf.filter(user=qs1.user)
    FY, FM, FD = str(qs1.SeasonFrom).split('-')
    TY, TM, TD = str(qs1.SeasonTo).split('-')
    SH, SM = str(qs1.MeetingTime).split(':')
    H1, M1 = str(qs1.Duration).split(':')
    H = int(SH)+int(H1)
    M = int(SM)+int(M1)
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
    })



def post_new(request):
    if request.method == 'POST':
        form = PostMForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
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
            post = form.save()
            return redirect('accounts:profile')
    else:
        form = PostMForm(instance=post)
    return render(request, 'travel/post_form_edit.html',{
        'form':form,
    })


def postcomplete(request):
    return render(request, 'travel/complete.html')



def booking(request, City, pk):
    content = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookMForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.content = content
            booking.save()
            return redirect('accounts:profile')
            # return HttpResponseRedirect(reverse('travel:bookingcomplete', args=[City, pk]))
    else:
        form = BookMForm()

    path = request.path
    filter = path.split('/')[4]
    post = Post.objects.all()
    post = post.filter(pk=filter)
    return render(request, 'travel/booking.html', {
        'form': form,
        'post': post,
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