from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import *
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'trkr/home.html', )


@login_required
def client_list(request):
    client = Client.objects.filter(created_date__lte=timezone.now())
    # paginator = Paginator(customer, 10)  # Show 10 rows per page.
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    return render(request, 'trkr/client_list.html', {'client': client})

@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        # update
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            c_date = form.cleaned_date["date"]
            client = form.save(commit=False)
            client.birth_date = c_date
            client.updated_date = timezone.now()
            client.save()
            client = Client.objects.filter(created_date__lte=timezone.now())
            # paginator = Paginator(customer, 10)  # Show 10 rows per page.
            # page_number = request.GET.get('page')
            # page_obj = paginator.get_page(page_number)

            return render(request, 'trkr/client_list.html',
                         {'client': client})
    else:
        # edit
        form = ClientForm(instance=client).as_p()
    return render(request, 'trkr/client_edit.html', {'form': form})

@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('trkr:client_list')

@login_required
def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            # 'name', 'nick_name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',
            c_date = form.cleaned_data["date"]
            c_name = form.cleaned_data["name"]
            c_nick_name = form.cleaned_data["nick_name"]
            c_address = form.cleaned_data["address"]
            c_city = form.cleaned_data["city"]
            c_state = form.cleaned_data["state"]
            c_zipcode = form.cleaned_data["zipcode"]
            c_email = form.cleaned_data["email"]
            c_cell_phone = form.cleaned_data["cell_phone"]
            client = Client()
            client.name = c_name
            client.nick_name = c_nick_name
            client.address = c_address
            client.city = c_city
            client.state = c_state
            client.zipcode = c_zipcode
            client.email = c_email
            client.cell_phone = c_cell_phone
            # client = form.save(commit=False)
            client.birth_date = c_date
            client.created_date = timezone.now()
            client.save()
            client = Client.objects.filter(created_date__lte=timezone.now())
            return render(request, 'trkr/client_list.html',
                         {'client': client})
    else:
        form = ClientForm().as_p()
        # print("Else")
    return render(request, 'trkr/client_new.html', {'form': form})


@login_required
def exercise_list(request):
    exercise = Exercise.objects.all()
    return render(request, 'trkr/exercise_list.html', {'exercise': exercise})

@login_required
def exercise_edit(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == "POST":
        # update
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.save()
            exercise = Exercise.objects.all()

            return render(request, 'trkr/exercise_list.html',
                         {'exercise': exercise})
    else:
        # edit
        form = ExerciseForm(instance=exercise)
    return render(request, 'trkr/exercise_edit.html', {'form': form})

@login_required
def exercise_delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    exercise.delete()
    return redirect('trkr:exercise_list')

@login_required
def exercise_new(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.save()
            exercise = Exercise.objects.all()
            return render(request, 'trkr/exercise_list.html',
                         {'exercise': exercise})
    else:
        form = ExerciseForm()
        # print("Else")
    return render(request, 'trkr/exercise_new.html', {'form': form})

@login_required
def activity_list(request):
    activity = Activity.objects.all()
    return render(request, 'trkr/activity_list.html', {'activity': activity})

@login_required
def activity_edit(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        # update
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            a_date = form.cleaned_data["date"]
            a_type = form.cleaned_data["type"]
            a_client = form.cleaned_data["client"]
            a_duration = form.cleaned_data["duration"]
            a_note = form.cleaned_data["note"]
            activity = Activity()
            activity.client_id = a_client.id
            activity.type_id = a_type.id
            activity.date = a_date
            activity.note = a_note
            activity.duration = a_duration
            # activity = form.save(commit=False)
            activity.save()
            activity = Activity.objects.all()

            return render(request, 'trkr/activity_list.html',
                         {'activity': activity})
    else:
        # edit
        form = ActivityForm(instance=activity).as_p()
    return render(request, 'trkr/activity_edit.html', {'form': form})

@login_required
def activity_delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    activity.delete()
    return redirect('trkr:activity_list')

@login_required
def activity_new(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            a_date = form.cleaned_data["date"]
            a_type = form.cleaned_data["type"]
            a_client = form.cleaned_data["client"]
            a_duration = form.cleaned_data["duration"]
            a_note = form.cleaned_data["note"]
            activity = Activity()
            activity.client_id = a_client.id
            activity.type_id = a_type.id
            activity.date = a_date
            activity.note = a_note
            activity.duration = a_duration
            # activity = form.save(commit=False)
            activity.save()
            activity = Activity.objects.all()
            return render(request, 'trkr/activity_list.html',
                         {'activity': activity})
    else:
        form = ActivityForm().as_p()
        # print("Else")
    return render(request, 'trkr/activity_new.html', {'form': form})

def get_test(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            a_type = form.cleaned_data["your_name"]
            a_date = form.cleaned_data["date"]
            # redirect to a new URL:
            return HttpResponseRedirect('/home/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm().as_p()

    return render(request, 'trkr/test.html', {'form': form})
