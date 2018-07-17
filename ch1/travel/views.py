from django.shortcuts import render, redirect
from .models import Post,City
from .forms import PostForm, PostMForm


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


def local_detail_form(request, City ,pk):
    queryset = Post.objects.all()
    path = request.path
    print(path)
    filter = path.split('/')[4]
    print(filter)
    qs = queryset.filter(pk=filter)
    return render(request, 'travel/local_detail_form.html',{
        'local_detail': qs,
        'filter':filter,
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



def complete(request):
    return render(request, 'travel/complete.html')