from django.shortcuts import render
from .data import courses

# Create your views here.
def courses_list(request):
    return render(request, "list.html", {"courses_list": courses})

def courses_detail(request, courses_id):
    item_course = None
    for item in courses:
        if item['id'] == courses_id:
            item_course = item
            break

    return render(request, "detail.html", {"courses_list": courses, "item_course": item_course})