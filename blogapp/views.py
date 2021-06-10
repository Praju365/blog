from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic.edit import DeleteView
from .models import Post
from django.contrib.auth.models import User 
from django.views.generic import (
    TemplateView , 
    ListView ,
    DetailView ,
    CreateView ,
    UpdateView ,
    DeleteView
)

################################################ Index Page View ############################################

class IndexPageView(TemplateView):
    template_name   = 'blogapp/index.html'

############################################# Post List View ###############################################

class PostListView(LoginRequiredMixin , ListView):
    model               =  Post
    template_name       = 'blogapp/home.html' #<app_name>/<model>_<view_type>.html
    context_object_name = 'posts'  
    ordering            = ['-date_posted']
    paginate_by         = 2

##################################### User Related Post List View ###############################################

class UserPostListView(LoginRequiredMixin , ListView):
    model               =  Post
    template_name       = 'blogapp/user_post.html' #<app_name>/<model>_<view_type>.html
    context_object_name = 'posts' 
    paginate_by         = 2
 

    def get_queryset(self):
        user = get_object_or_404(User , username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')
########################################### Post Detail View ##############################################

class PostDetailView(DetailView):
    model               = Post 
    
########################################### Post Detail View ##############################################

class PostCreateView(CreateView):
    model               = Post 
    template_name       = 'blogapp/create.html'
    fields              = ['title' , 'content']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

########################################### Post Update View ##############################################

class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin , UpdateView):
    model               = Post 
    template_name       = 'blogapp/update.html'
    fields              = ['title' , 'content']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post            = self.get_object()
        if self.request.user == post.author:
            return True 
        else:
            return False

########################################### Post Delete View ##############################################

class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model               = Post
    template_name       = 'blogapp/delete.html'
    success_url         = reverse_lazy('blog-posts')

    def test_func(self):
        post            = self.get_object()
        if self.request.user == post.author:
            return True 
        else:
            return False





