from django.shortcuts import render,redirect
from . forms import PersonalizedForm
from . models import Personalized

def list(request):
    qs = Personalized.objects.all()

    return render(request, 'Personalized/list.html', {
        'list': qs,
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
        'form': form
    })