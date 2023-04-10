from django.shortcuts import render
from .forms import CustomUserCreationForm

def register(request):
    if request.POST == 'POST':
        form = CustomUserCreationForm()
        if form.is_valid():
            form.save()
        # messages.success(request)

    else:
        form = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)