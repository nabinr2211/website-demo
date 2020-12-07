from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, CreateView, DetailView, DeleteView, UpdateView

# Create your views here.
from mysite.models import Post, Contact, Members, Categories, Tag
from mysite.froms import AddPostModelForm


# function base view for homepage
def index(request):
    member = Members.objects.all()
    post = Post.objects.all()
    return render(request, 'frontend/index.html', {'posts': post, 'members': member})


# function base view for dashboard
def dashboard(request):
    post = Post.objects.all()
    count = Post.objects.count()

    return render(request, 'backend/dashboard.html', {'posts': post, 'count': count})


# function base view for categories
def add_category(request):
    if request.method == "GET":
        return render(request, 'backend/add_category.html')
    elif request.method == "POST":
        category = Categories.objects.create(
            categories=request.POST['category']
        )
        return redirect('site:dashboard')


# function base view for add tag
def add_tag(request):
    if request.method == "GET":
        return render(request, 'backend/add_tag.html')
    elif request.method == "POST":
        tag = Tag.objects.create(
            tags=request.POST['tag']
        )
        return redirect('site:dashboard')


# function base view for adding member
def add_member(request):
    if request.method == "GET":
        return render(request, 'backend/add_member.html')
    elif request.method == "POST":
        member = Members.objects.create(
            name=request.POST['fullname'],
            address=request.POST['address'],
            phone_number=request.POST['phone_number'],
            email=request.POST['email'],
            description=request.POST['description'],
            positions=request.POST['position'],
            image=request.FILES['image'],
        )
        return redirect('site:dashboard')


# function base view for add post
def add_post(request):
    if request.method == 'GET':
        post_form = AddPostModelForm()
        return render(request, 'backend/add_post.html', {'post_form': post_form})
    elif request.method == 'POST':
        form = AddPostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('site:dashboard')
        else:
            return render(request, 'backend/add_post.html', {'post_form': form})


# # function base view for delete post
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('site:dashboard')


# class base view for post detail
class PostDetailView(DetailView):
    model = Post
    query_pk_and_slug = True
    slug_field = 'title'
    template_name = 'frontend/post_detail.html'


# class base view for post edit
def edit_post(request, id):
    edit_post = Post.objects.get(id=id)
    if request.method == 'GET':
        post_form = AddPostModelForm(instance=edit_post)
        return render(request, 'backend/add_post.html', {'post_form': post_form})
    elif request.method == "POST":
        post_form = AddPostModelForm(request.POST, request.FILES, instance=edit_post)
        if post_form.is_valid():
            post_form.save()
        else:
            return render(request, 'backend/add_post.html', {'post_form': post_form})
        return redirect('site:dashboard')


# function base view for contact
def contact(request):
    if request.method == "GET":
        return render(request, 'frontend/contact.html')
    elif request.method == "POST":
        contacts = Contact.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        return redirect('index')
