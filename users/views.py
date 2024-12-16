from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from .forms import UserUpdateForm, ProfileUpdateForm
from users.models import Profile

@login_required
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name)
                user.save()
                # Log the user in and redirect to the homepage
                user = authenticate(username=username, password=password,first_name=first_name)
                if user is not None:
                    login(request, user)
                    return redirect('posts-home')
                else:
                    messages.error(request, 'Something went wrong during authentication')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'users/register.html')


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        # print(self.request.POST)  # Print the POST data for debugging
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('posts-home')

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST,instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
#
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, 'Your account has been updated!')
#             return redirect('profile')
#
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         'u_form':u_form,
#         'p_form':p_form
#     }
#
#     return render(request, 'users/profile.html',context)


# views.py
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileUpdateForm
from .models import Profile

# def profile_update_view(request):
#     # Get the user's profile instance
#     profile = get_object_or_404(Profile, user=request.user)
#
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)  # Pass the existing instance
#         if form.is_valid():
#             form.save()  # Save the updated profile
#             return redirect('profile')  # Redirect to the profile page or another page
#     else:
#         form = ProfileUpdateForm(instance=profile)  # Load the existing instance into the form
#
#     return render(request, 'users/profile.html', {'p_form': form, 'profile': profile})


from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile  # Ensure Profile model is imported

def profile_update_view(request):
    # Get the user's profile instance
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)  # User update form
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)  # Profile update form

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Save updated user data
            profile_form.save()  # Save updated profile data
            return redirect('profile')  # Redirect after successful update
    else:
        user_form = UserUpdateForm(instance=request.user)  # Load existing user instance
        profile_form = ProfileUpdateForm(instance=profile)  # Load existing profile instance

    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile  # Ensure you import your Profile model

def deleteProfilePic(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        # Reset the profile image to default
        profile.image = 'default.jpg'
        profile.save()  # Save the changes to the database
        return redirect('profile')  # Redirect to the profile page after deletion

    return render(request, 'users/profile.html', {'profile': profile})  # Pass the profile to the template if needed


def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect_to_login(request.get_full_path())
    return render(request, 'users/user_profile.html', {'profile':profile})

def users(request):
    context = {
        'profiles': Profile.objects.all()
    }
    return render(request,'posts/chat_sidenav.html',context)