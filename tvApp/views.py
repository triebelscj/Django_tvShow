from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# DONT FORGET TO IMPORT *** MODELS (.models)***
from .models import Show


# ******* RENDER PAGES - Displaying the pages *********
def dashboard(request):
    # CONTEXT gets all the Shows held in the DB
    context = {
        "shows": Show.objects.all()
    }
    return render(request, 'dashboard.html', context)


# Takes user to page to CREATE A NEW SHOW
def new_page(request):
    context = {
        "shows": Show.objects.all()
    }
    # renders new.html page // link with Path in urls.py
    return render(request, 'new.html', context)


#  -- This displays EDIT.HTML --
def edit_page(request, show_id):
    each_show = Show.objects.get(id=show_id)
    context = {
        "show": each_show
    }
    return render(request, "edit.html", context)


#  -- This displays SHOW.HTML --
# // We need a show ID to get information from the DB for that specific show.
def show_page(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        "show": show
    }
    return render(request, 'show.html', context)


# ******** Action Routes - This ACTUALLY CHANGES/UPDATES things in our DataBase **********
def delete(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    context = {
        "show": show
    }
    return redirect('/shows', context)


# This IS the LOGIC that actually CREATES a New Show
def create_show(request):
    # TO CREATE A NEW SHOW -- "show.objects.create(*** all the names from the FORM AREA ***)"
    # Make sure all variable names match Models Variable names.
    print("****************************************hi")
    print(request.POST)
    if request.method == "POST":
        errors = Show.objects.validateShow(request.POST)
        print(errors, "?????????????????????")
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            Show.objects.create(
                title=request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['release_date'],
                description=request.POST['description'],

            )
        print(request.POST)
        # return redirect(f'/shows/{new_show.id}')
    return redirect('/shows')


# This actually changes stuff when I UPDATE the EDIT page
def updateShowDB(request, show_id):
    # DONT FORGET IF STATEMENT since we are UPDATING/POSTING data to the DB.
    if request.method == "POST":
        # Need to set variable to GET whatever ID you intend to EDIT/Update.
        show = Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
    return redirect("/")
