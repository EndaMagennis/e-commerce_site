from django.shortcuts import render

# Create your views here.
def profile(request):
    """ Display the user's profile. """
    
    return render(request, 'profiles/profile.html')
