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

