from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from  django.contrib import messages
from .models import Post
from .forms import EditPostForm
#from.forms import EditBlog

def home(request):
    post =Post.objects.all()
    
    return HttpResponse('post')
   
    
    # return render(request ,{'post':post})

def register(request):

    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password1']
        
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,last_name=last_name)
            user.save();
            messages.info(request,'User Created')
            return redirect('login')


    
    else:
        return render(request, {'register':register})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,{'login':login})
def logout(request):
    auth.logout(request)
    return redirect('register')

def post(request):
    if request.method =="POST": # suppose data apn send krt ahot
        user =request.POST.get('user') # to receive title data get('name)
        text =request.POST.get('text')
        
        post = Post(user = user, text= text)# 1st title related to model nd 2nd is above title
        post.save()
        messages.success(request,"post has been submited successfully")
        return redirect('post') # blog is url
    return render(request , "post.html")

def PostDetail(request , id):
    post =Post.objects.get(id=id) # get use whene we have only one value ie unique value
    return render(request , "detail.html",{'post':post})


def delete(request,id):
    post= Post.objects.get(id=id)
    post.delete()
    messages.success(request,'post has been deleted')
    return redirect('/')

def edit(request, id):
    post= Post.objects.get(id=id)
    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            
            return render(request, 'edit.html')  
        else:
            form = EditPostForm(instance=post)
    else:
        form = EditPostForm(instance=post)
    return render(request, 'edit.html', {'form':form, 'post':post})


    
