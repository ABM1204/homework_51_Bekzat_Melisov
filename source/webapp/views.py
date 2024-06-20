from django.shortcuts import render, redirect
from .models import Cat


def index(request):
    return render(request, 'index.html')


def create_cat(request):
    if request.method == 'POST':
        cat_name = request.POST.get('cat_name')
        cat = Cat(cat_name)
        request.session['cat'] = cat.__dict__
        context = {
            'cat_name': cat.name,
            'age': cat.age,
            'satiety_level': cat.satiety_level,
            'happy_point': cat.happy_point,
            'is_sleeping': cat.is_sleeping,
            'image': cat.change_image()
        }
        return render(request, 'cat_view.html', context)
    return render(request, 'create_cat.html')


def cat_actions(request):
    if request.method == 'POST':
        cat_data = request.session.get('cat')
        if not cat_data:
            return redirect('index')

        cat = Cat(cat_data['name'])
        cat.__dict__.update(cat_data)

        action = request.POST.get('action')
        if action == 'feed':
            cat.feed_cat()
        elif action == 'play':
            cat.play_cat()
        elif action == 'sleep':
            cat.put_cat_to_bed()

        request.session['cat'] = cat.__dict__

        context = {
            'cat_name': cat.name,
            'age': cat.age,
            'satiety_level': cat.satiety_level,
            'happy_point': cat.happy_point,
            'is_sleeping': cat.is_sleeping,
            'image': cat.change_image()
        }
        return render(request, 'cat_view.html', context)
    return redirect('index')
