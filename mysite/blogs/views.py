from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from blogs.models import Post

def home(request):
    post_list = Post.objects.all()
    return render_to_response('home.html', locals())

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})
def about(request):
	return render(request, 'about.html')