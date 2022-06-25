from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect)
from .models import TodoItem
from .forms import ItemCreateForm
# Create your views here.

def index(request):
    context = {}

    form = ItemCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
        
    context["form"] = form
    context["dataset"] = TodoItem.objects.all()


    return render(request, "index.html", context)


def deleteItem(request, id):
    item = TodoItem.objects.get(id = id)
    item.delete()

    return HttpResponseRedirect('/')