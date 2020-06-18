from django.shortcuts import render
from .models import Post
from .models import Portfolio


def homepage(request):
    posts = Post.objects.all()
    portfolio = Portfolio.objects.all()
    context = {
        'posts': posts,
        'portfolio': portfolio,
        'full_name': 'Pavel Harkusha',
        'job_list': ['PHP', 'Python', 'JavaScript', 'VueJs'],
        'contact': {
            "telephone": '0675004899',
            'email': 'kievlanservers@gmail.com',
            'address': 'none'
        }

    }


    return render(request, 'portfolio/index.html', context)


def print_context(request):
    context = {
        'friends': ['Pavel', 'Sasha', 'Leonid']
    }

    return render(request, 'portfolio/context.html', context)



