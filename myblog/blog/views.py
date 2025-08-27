from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog, Comment
from .forms import CommentForm, BlogForm
from django.contrib import messages

# Create your views here.
def blog_list(request):
    posts = Blog.objects.all()
    corousel = Blog.objects.all().order_by('-id')[:4]
    return render(request, 'blog/list.html', {'posts': posts, 'corousel': corousel})

def blog_detail(request, pk):
    posts = get_object_or_404(Blog, pk = pk )
    comments = posts.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.posts = posts
            comment.save()

            return redirect('detail', pk = pk)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html',{'posts': posts, 'comments': comments, 'form': form})

def post_like(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    # get liked posts from session
    liked_posts = request.session.get('liked_posts', [])

    if pk in liked_posts:
        # already liked → undo like
        post.likes -= 1
        liked_posts.remove(pk)
    else:
        # not liked → add like
        post.likes += 1
        liked_posts.append(pk)

    post.save()
    request.session['liked_posts'] = liked_posts  # save back to session
    return redirect('detail', pk=pk)


def about_us(request):
    return render(request, 'blog/about.html')
def contact(request):
    return render(request, 'blog/contact.html')

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q','')
        result = Blog.objects.filter(title__icontains=query)

    return render(request, 'blog/search.html', {'query': query, 'result': result})

# blog/views.py
def posts_by_category(request, category_name):
    # Get posts that match the category, case-insensitively
    posts = Blog.objects.filter(category__iexact=category_name)
    
    # Get the 4 latest posts for the carousel (optional, can filter by same category too)
    corousel = Blog.objects.all().order_by('-id')[:4] 
    # Alternatively, for category-specific carousel:
    # corousel = posts.order_by('-id')[:4]
    
    context = {
        'posts': posts,
        'corousel': corousel,
        'category': category_name,
    }
    return render(request, 'blog/category_posts.html', context)

@login_required
def profile_view(request):

    user_posts = Blog.objects.filter(author=request.user).order_by('-date')
    # user_name = request.user.get_full_name() or request.user.username
    user_comments = Comment.objects.filter(email=request.user)

    # Calculate statistics
    post_count = user_posts.count()  
    comment_count = user_comments.count()  
    total_likes = sum(post.likes for post in user_posts)  # 
    most_popular_post = user_posts.order_by('-likes').first()  

    return render(request, 'blog/profile.html', {
        'user': request.user,
        'user_posts': user_posts,
        'user_comments': user_comments,  
        'post_count': post_count,
        'comment_count': comment_count,
        'total_likes': total_likes,  # Added total_likes
        'most_popular_post': most_popular_post,  
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_by = request.user.get_full_name() or request.user.username
            post.save()

            messages.success(request, 'Your post has been created successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BlogForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk = pk, author = request.user)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance= post)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form =BlogForm(instance= post)
    
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('profile')
    
    return render(request, 'blog/delete_post.html', {'post': post})