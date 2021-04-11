from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Blog, BlogAuthor, BlogComment
from django.views import generic
from .forms import BlogCommentForm, BlogForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import datetime


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = Blog.objects.all().count()
    num_authors = BlogAuthor.objects.count()
    num_comments = BlogComment.objects.count()

    context = {
        'num_blogs': num_blogs,
        'num_authors': num_authors,
        'num_comments': num_comments,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model = Blog

class BlogDetailView(generic.DetailView):
    model = Blog

class AuthorListView(generic.ListView):
    model = BlogAuthor

class AuthorDetailView(generic.DetailView):
    model = BlogAuthor

@login_required
def blogcomment_new(request, pk):
    if request.method == "POST":
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.user = request.user
            x.blog = get_object_or_404(Blog, pk=pk)
            x.save()
            return redirect('blog-detail', pk=pk)
    else:
        form = BlogCommentForm()
    return render(request, 'blog/blog_comment.html', {'form': form})

@login_required
def blog_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.pub_date = datetime.date.today()
            x.author = BlogAuthor.objects.get(user=request.user)
            x.save()
            return redirect('allblogs')
    else:
        form = BlogForm()
        return render(request, 'blog/blog_post.html', {'form': form})
