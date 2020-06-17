from django.shortcuts import render


def homepage(request):
    context = {
        'full_name': 'Pavel Harkusha',
        'job_list': ['PHP', 'Python', 'JavaScript', 'VueJs'],
        'contact': {
            "tele": '12151',
            'email': 'mymail',
            'addr': 'none'
        }
    }
    return render(request, 'portfolio/index.html', context)


def print_context(request):
    context = {
        'friends': ['Pavel', 'Sasha', 'Leonid']
    }

    return render(request, 'portfolio/context.html', context)

