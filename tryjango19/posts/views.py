from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

# Create your views here.
# functional view receive request, and send response
def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request):
    instance = get_object_or_404(Post, id=1)
    # variable to be passed to the view
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
