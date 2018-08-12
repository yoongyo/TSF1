from django.shortcuts import render,get_object_or_404, redirect
from . forms import reviewForm
import sys
sys.path.append('..')
from travel.models import Post,Booking

def review(request, title, pk):
    pk = get_object_or_404(Booking, pk=pk)
    title = get_object_or_404(Post, title=title)
    if request.method == 'POST':
        form = reviewForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = title
            form.booking = pk
            form.save()
            return redirect('Review:thanks')
    else:
        form = reviewForm()
    return render(request, 'Review/review.html', {
        'form':form,
    })

def thanks(request):
    return render(request, 'Review/thanks.html')