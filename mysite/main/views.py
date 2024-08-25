from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, ToDoList
from .forms import CreateNewList

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():
        if response.method == 'POST':
            print(response.POST)

            for item in ls.item_set.all():  # type: ignore
                if response.POST.get('d' + str(item.id)) == 'delete':
                    item.delete()

            if response.POST.get("save"):
                for item in ls.item_set.all(): # type: ignore
                    if response.POST.get('c' + str(item.id)) == 'clicked':
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif response.POST.get("addItem"):
                txt = response.POST.get('New Item') # Gets POST by name (not 'value')

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False) # type: ignore
                else:
                    print('Invalid Input !')
        return render(response, "main/list.html", {"ls": ls})
    else:
        return render(response, "main/view.html", {})

def home(response):
    return render(response, "main/home.html", {})

def view(response):
    return render(response, 'main/view.html', {})

def create(response):
    #response.user

    if response.method == 'POST':
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" %t.id) # type: ignore
    
    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})