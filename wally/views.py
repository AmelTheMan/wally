
from email.mime import base
from urllib import request, response
from django.shortcuts import render , redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
from .models import Post
from django.http import  HttpResponseRedirect , HttpResponse,HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
from .forms import CommentForm



# Create your views here.
class StartingPageView(ListView):
    template_name ="wally/main.html"
    model = Post
    context_object_name="posts" 

def registerPage(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get("username")
            messages.success(request,"Account created for " + user)

            return redirect("login")

    context={"form":form}
    return render(request,"wally/includes/register.html",context)

def loginPage(request):
    if request.method =="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request, username=username, password=password) 

        if user is not None:
            login(request, user)
            return redirect("starting-page")
        else:
            messages.info(request,"Username or password is incorrect")

    context={}
    return render(request,"wally/includes/login.html",context)
    
def logoutUser(request):
    logout(request)
    return redirect("login")


class PostDetailView(View):
    def get(self,request,slug):
        post=Post.objects.get(slug=slug)#pojedinacni 
        context = {
            "post":post,
            "comment_form":CommentForm(),
            "comments": post.comments.all().order_by("-id")
            
           
        }
        return render(request, "wally/post-detail.html", context)
        
    def post(self,request ,slug):
        comment_form = CommentForm(request.POST)
        post=Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.post= post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))#pokupi slug posta i refresha stranicu
       
        context = {
            "post":post,
            "comment_form":comment_form,
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "wally/post-detail.html", context)
