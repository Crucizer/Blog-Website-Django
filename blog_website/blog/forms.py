# We're Importing Some Basic Stuff Here
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# So This Is A Form Class To Display The Registration Fields, This Is BluidIn In Django
class UserRegister(UserCreationForm):
	# We're Just Saying Here That We Want A Email Field In Our Page
	email = forms.EmailField()# The Required=True Is By Default But I've Still Written It.

	# The Meta Class Is like the information of class 
	# But In This Particular Meta Class We're Writing The Fields And In Which Order We Want To Display Them
	class Meta:
		# We're Saying The We Want To Play Around With The User Model Here
		model = User
		# We're Giving The Fields And The Order In Which We Want To Display Them
		fields = ['username','email','password1', 'password2']

# This Is The Form In Which The User Can Update His Profile, This Is Also BluidIn In Django
class UserUpdate(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		# We're Saying The We Want To Play Around With The User Model Here
		model = User
		fields = ['username','email']

# This Is The Form In Which The User Can Update His Profile Picture, This Is Also BluidIn In Django
class UserProfile(forms.ModelForm):
	class Meta:
		# We're Saying The We Want To Play Around With The Profile Model Here
		model = Profile
		fields = ['image']
