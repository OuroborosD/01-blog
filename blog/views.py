from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def lista_posts(request):
    pass

def post(request):
    return render(request,'blog/post.html')