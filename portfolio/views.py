from django.shortcuts import render
from portfolio.models import Post


def homepage(request):
    context = {
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



def project_index(request):
    posts = Post
    context = {
        'posts': posts
    }
    return render(request, 'portfolio/index.html', context)