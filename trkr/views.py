from django.contrib.auth.decorators import login_required
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
            client = form.save(commit=False)
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
        form = ClientForm(instance=client)
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
            client = form.save(commit=False)
            client.created_date = timezone.now()
            client.save()
            client = Client.objects.filter(created_date__lte=timezone.now())
            return render(request, 'trkr/client_list.html',
                         {'client': client})
    else:
        form = ClientForm()
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
            activity = form.save(commit=False)
            activity.save()
            activity = Activity.objects.all()

            return render(request, 'trkr/activity_list.html',
                         {'activity': activity})
    else:
        # edit
        form = ActivityForm(instance=activity)
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
            activity = form.save(commit=False)
            activity.save()
            activity = Activity.objects.all()
            return render(request, 'trkr/activity_list.html',
                         {'activity': activity})
    else:
        form = ActivityForm()
        # print("Else")
    return render(request, 'trkr/activity_new.html', {'form': form})

