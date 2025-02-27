from django.shortcuts import render, redirect
from .forms import MyModelForm 
# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def my_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succes')
            else:
                form = MyModelForm()
                return render(request, 'myapp/my_form.html', {'form': form})
