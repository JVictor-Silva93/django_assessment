from django.shortcuts import render
from .models import Post  # Assuming you have a model named 'Post'
from .forms import CommentForm
# is there anything else you need to import?

def index(request):
    return render(request, 'blog/index.html')

def post_list(request):
    # TODO: Retrieve all the blog posts from the database.
    # TODO: Render them on the post_list.html template.
    return render(request, 'blog/post_list.html', {})

def post_detail(request, pk):
    # TODO: Retrieve a specific blog post using the 'pk' (primary key).
    # TODO: Render the post on the post_detail.html template.
    # Bonus: Implement comment submission in this view.
    return render(request, 'blog/post_detail.html', {})
