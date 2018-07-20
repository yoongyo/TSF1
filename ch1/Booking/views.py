from django.shortcuts import render,redirect
from .forms import BookForm,BookMForm


def booking(request):
    if request.method == 'POST':
        form = BookMForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('Booking:complete')
    else:
        form = BookForm()
    return render(request, 'booking/booking.html', {
        'form': form,
    })

def complete(request):
    return render(request, 'booking/complete.html')