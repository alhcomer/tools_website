from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("tools:index")


    form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
