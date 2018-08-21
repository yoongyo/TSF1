from django.shortcuts import render,redirect,get_object_or_404
from . forms import PersonalizedForm,PersonalizedPostForm
from . models import Personalized,PersonalizedTour
import sys
sys.path.append('..')
from accounts import models

def list(request):
    qs = Personalized.objects.all()
    b=[]
    for i in qs:
        k = i.Password
        b.append(k)
    ps = PersonalizedTour.objects.all()
    for k in ps:
        print(k.content.personalized.title)
    return render(request, 'Personalized/list.html', {
        'list': qs,
        'b': b,
        'ps': ps,
    })


def list_new(request):
    if request.method == 'POST':
        form = PersonalizedForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            return redirect('Personalized:list')
        else:
            print(form.errors)
    else:
        form = PersonalizedForm()
    return render(request, 'Personalized/list_new.html', {
        'form': form,
    })

def personalized_edit(request, pk):
    edit = get_object_or_404(Personalized, pk=pk)
    if request.method == 'POST':
        form = PersonalizedForm(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            form = form.save()
            return redirect('Personalized:list')
        else:
            print(form.errors)
    else:
        form = PersonalizedForm(instance=edit)
    return render(request, 'Personalized/Personalized_edit.html', {
        'form': form,
    })

def new(request, pk):
    pk = get_object_or_404(Personalized, pk=pk)
    if request.method == 'POST':
        form = PersonalizedPostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.content = pk
            form.user = request.user
            print(form.content)
            form.save()
            return redirect('Personalized:complete')
    else:
        form = PersonalizedPostForm()
    return render(request, 'Personalized/new.html',{
        'form':form,
    })

def edit(request, pk):
    edit = get_object_or_404(PersonalizedTour, pk=pk)
    if request.method == 'POST':
        form = PersonalizedPostForm(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            form = form.save()
            return redirect('accounts:profile')
    else:
        form = PersonalizedPostForm(instance=edit)
    return render(request, 'Personalized/edit.html', {
        'form': form,
    })



def complete(request):
    return render(request, 'Personalized/complete.html')

def detail(request,pk):
    queryset = PersonalizedTour.objects.all()

    qs = queryset.filter(pk=pk)
    qs1 = PersonalizedTour.objects.get(pk=pk)
    pf = models.Profile.objects.all()
    pf = pf.filter(user=qs1.user)
    FY, FM, FD = str(qs1.SeasonFrom).split('-')
    TY, TM, TD = str(qs1.SeasonTo).split('-')
    SH, SM = str(qs1.MeetingTime).split(':')
    H1, M1 = str(qs1.Duration).split(':')
    H = int(SH) + int(H1)
    M = int(SM) + int(M1)
    l = len(qs1.NotDate.split(','))
    print(qs1.NotDate.split(','))
    b = []
    if l != 1:
        print(l)
        for i in range(l):
            a = qs1.NotDate.split(',')[i].split('-')
            a[1] = str(int(a[1]) - 1)
            s = ','.join(a)
            b.append(s)
    for i in pf:
        z = i.nextCountry.all()
    for i in pf:
        k = i.visitedCountry.all()
    print(qs1.Map)
    return render(request, 'Personalized/detail.html', {
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


