from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Class_Type, Level

# Create your views here.

def all_classes(request):
    """ A view to show the class/timetable page and all for some filtering """

    class_types = Class_Type.objects.all()
    query = None
    levels = None

    if request.GET:
        if 'level' in request.GET:
            levels = request.GET['level'].split(',')
            print(levels)
            class_types = class_types.filter(level__friendly_name__in=levels)
            print(class_types)
            levels = Level.objects.filter(friendly_name__in=levels)

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "Your search didn't match any of our results")
            return redirect(reverse('classes'))

        queries = Q(name__icontains=query) | Q(teacher__icontains=query) | Q(day__icontains=query)
        class_types = class_types.filter(queries)

    context = {
        'class_types': class_types,
        'search_term': query,
        'current_levels': levels,
    }

    return render(request, 'classes/classes.html', context )


def class_info(request, class_type_id):
    """ A view to show the class descriptions page """

    class_type = get_object_or_404(Class_Type, pk=class_type_id)

    context = {
        'class_type': class_type,
    }

    return render(request, 'classes/class_type.html', context )