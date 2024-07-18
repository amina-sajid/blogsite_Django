from django.contrib import messages
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import PostForm, CommentForm,SubscribeForm
from .models import Post, Register, Comment
from django.conf import settings




# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Successfully subscribed'
            message = 'You have subscribed to Blogscrib Blogs '
            recipient = form.cleaned_data.get('email')
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('/index/')
    form = SubscribeForm()
    posts = Post.objects.all()

    return render(request, 'index.html', {'form': form, 'posts': posts})


def view_comments(request):
    id1 = Post.objects.get(id=request.POST.get("pid"))
    print(id1.id)
    abc=Comment.objects.filter(post=request.POST.get("pid"))
    com = CommentForm()
    print("1")
    return render(request,'comment.html',{"post":id1,"abc":abc,"com":com})


def comment (request):


    if request.method == "POST":
        print("hiiiiiiiiiiii")

        id1 = Post.objects.get(id=request.POST.get("pid"))
        co = Comment(post=id1,name=request.POST.get("comment_name"),description=request.POST.get("comment_des"))
        co.save()
        print("2")
        abc = Comment.objects.filter(post=request.POST.get("pid"))
    com = CommentForm()
    return render(request,'comment.html', {'com': com,'post':id1,'abc':abc})






def post_details(request):
    obj = PostForm()
    if request.method == "POST":
        ob  = PostForm(request.POST,request.FILES)
        if ob.is_valid():
            ob.save()
            return redirect('/index/')

    return render(request, 'post_details.html', {'obj':obj})



def register(request):

    if request.method=="POST":
        print("mmmmmm")
        username=request.POST.get('username')
        print (username)
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2 = request.POST.get('re_password')

        if pass1== pass2:
            if Register.objects.filter(username=username).exists():
                messages.error(request,"Username already taken")
            if Register.objects.filter(email=email).exists():
                messages.error(request,"Email already taken")

            else:
                reg=Register(username=username,email=email,password=pass1,re_password=pass2)
                reg.save()
                messages.error(request,"Sucessfully registered ")

        else:
            messages.error(request,"Both passwords are not matching")

    return render(request,'registration.html')


def login(request):

    if request.method == "POST":

        u=request.POST.get('username')
        p=request.POST.get('password')
        print(u)
        regg=Register.objects.filter(username=u,password=p)

        if regg.exists():

            reg_details=Register.objects.get(username=u,password=p)
            id=reg_details.id
            username_reg=reg_details.username
            print(id)
            print(username_reg)
            request.session['id']=id
            request.session['username'] = username_reg
            return redirect('/index/')

        else:
            messages.error(request, "Incorrect username or password")
            return render(request,'login.html')


    return render(request,'login.html')








def userbase(request):
    return render(request,'user/userbase.html')
def userreg(request):
    return render(request,'user/userreg.html')





def home(request):
    print('illlllll')
    id = request.session['id']
    username = request.session['username']
    return render(request,'home.html',{'id':id,'name':username})


def logout(request):
    print("9")
    Session.objects.all().delete()
    return render(request,'login.html')