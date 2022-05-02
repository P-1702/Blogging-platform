from typing import Reversible
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment,Form
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import ModelForm
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib import messages
from django.db.models import Avg
from django.http import HttpResponse

from dashboard import models
import json
import urllib.request

def home(request):
     context = {
        'posts': Post.objects.all()
    }
     return render(request,"dashboard/home.html",context)

class PostListView(ListView):
    model=Post
    template_name="dashboard/home.html"
    context_object_name='posts'



class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
         form.instance.author = self.request.user
         return super().form_valid(form)
 
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
         form.instance.author = self.request.user
         return super().form_valid(form)

    def test_func(self):
         post = self.get_object()
         if self.request.user == post.author:
             return True
         return False    

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url = '/dashboard/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
             return True
        return False

def form_submit(request):
    model=Form
    if request.method== "POST":
        name= request.GET.get('name','default')
        email= request.GET.get('email','default')
        message= request.GET.get('message','default')
        messages.success(request,f'Query Submitted!') 
    return render(request,"dashboard/form_submit.html")   


def about(request):
    return render(request,"dashboard/about.html",{'title':'About'})

def city(request):
    if request.method == 'POST':
        city=request.POST['city']
        res=urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d70f15774d77ed48f06acd2e70090872").read()
        json_data=json.loads(res)
        data={
            "country_code": str(json_data['sys']['country']),
            "location": str(json_data['coord']['lat'])+" , "+str(json_data['coord']['lon']),
        }

    else:
        city=" "
        data={}
    return render(request,"dashboard/weather.html",{'city':city,'data':data})


@login_required  
def post_detailview(request, pk):
    post=Post.objects.get(id=pk)
    ied=pk
    comments=Comment.objects.filter(post=post).order_by("-pk")

    if request.method == 'POST':
        cf=CommentForm(request.POST or None)
        if cf.is_valid():
            content=request.POST.get('content')
            comment=Comment.objects.create(post=post,user=request.user,content=content)
            comment.save()
            return redirect(post.get_absolute_url())
    else:
        cf=CommentForm()
        context = {
            'comment_form':cf,
            'comments':comments,
        }
        return render(request,"dashboard/discussion.html",context)

@login_required         
def deletecomment(request,id):
    comment=get_object_or_404(Comment,id=id)
    if request.method == 'POST':         
        comment.delete()                   
        messages.success(request,f'Comment deleted!')
        context = {
        'posts': Post.objects.all()
                }
    return render(request,"dashboard/home.html",context)

    
class UpdateCommentVote(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'next'
    def get(self, request, *args, **kwargs):
        comment_id = self.kwargs.get('comment_id', None)
        opinion = self.kwargs.get('opinion', None) 
        comment = get_object_or_404(models.Comment, id=comment_id)
        return HttpResponseRedirect(Reversible('comment'))
        
 



