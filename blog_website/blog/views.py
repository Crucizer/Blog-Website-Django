# We're Importing Some Stuff Here

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.contrib import messages
from .forms import UserRegister, UserUpdate, UserProfile 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.core.paginator import Paginator


# @login_required just makes the view so that It Must Require Login, So You Know No One Without A Account Can Get Into The App.
 
@login_required
def index(request):
	posts = Post.objects.all()
	# This is to load the template
	template = loader.get_template('blog/index.html')
	# inorder to provide the python variables to the html file we need to create a dictionary
	context = {
	'posts':posts
	}
	# This is just giving the data to the html file and displaying it when this view is called
	return HttpResponse(template.render(context, request))

# So, This Is A Generic View Class Of Home Page
class home(ListView):
	# We're saying in the next line that which model we want to play around with, which in this case is Post Model
	model = Post
	# We're Saying here that what name should we give to our dictionary which is automatically passed on the html page
	context_object_name = 'posts'
	# specing the html page which is by default-----<app_name>/<view_name>_<viewtype>.html
	template_name = 'blog/index.html'
	# we're saying here that how should we sort the page which in this case is the most recent posts first then the older ones
	ordering = ['-date']

	# paginate_by = 5


class User_Post_Profile(ListView):
    model = Post
    template_name = 'blog/user_profile.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


class create_post(LoginRequiredMixin, CreateView):
	# We're saying in the next line that which model we want to play around with, which in this case is Post Model
	model = Post
	# specing the html page which is by default-----<app_name>/<view_name>_<viewtype>.html
	template_name = 'blog/create_post.html'
	# specifing the Fields
	fields = ['title', 'content']

	def form_valid(self, form):
		# We're Saying Just Make The Author The Current User
		form.instance.author = self.request.user
		# I Couldn't Fully Understand this line but I thinks this tells django to just valid the form and is a small version of 
		# forms.py and just make the changes to the parent class
		return super().form_valid(form)


class update_post(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	# We're saying in the next line that which model we want to play around with, which in this case is Post Model
	model = Post
	# specing the html page which is by default-----<app_name>/<view_name>_<viewtype>.html
	template_name = 'blog/create_post.html'
	# specifing the Fields
	fields = ['title', 'content']

	def form_valid(self, form):
		# We're Saying Just Make The Author The Current User
		form.instance.author = self.request.user
		# I Couldn't Fully Understand this line but I thinks this tells django to just valid the form and is a small version of 
		# forms.py and just make the changes to the parent class
		return super().form_valid(form)

	# So Above We Imported A Module Object 'UserPassesTestMixin', So This module checks if the below function is true or false
	# if it is True It'll perform the function and if it ain't it won't
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

class delete_post(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'blog/delete_confirm.html'
	context_object_name = 'post'

	success_url = '/blog/'

	# Written About This Earlier
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False



def content(request, pk):
	# So Every Model Object Has A particular ID so, this just says when content/ID is called open a page for that particular ID
	post = Post.objects.get(pk=pk)
	template = loader.get_template('blog/content.html')
	context = {
	'post':post
	}
	# just showing up this html page when the url in entered and passing the dictionary
	return HttpResponse(template.render(context, request))

def register(request):
	# this is checking if the request is a POST request which basically means when the submit button is clicked
	if request.method == "POST":
		# this is our form (form.py) this is sum fields for User Registration
		form = UserRegister(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/blog/login')
			messages.success(request, "Acount Created! You Can Now Log In")
	# else basically means the request.method == request.GET for displaying the html page 
	else:
		form = UserRegister()
	return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdate(request.POST, instance=request.user)
        p_form = UserProfile(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('blog:profile')

    else:
        u_form = UserUpdate(instance=request.user)
        p_form = UserProfile(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'blog/profile.html', context)
	