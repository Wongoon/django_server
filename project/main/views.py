from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog, Comment
from django.utils import timezone
# Create your views here.
def main(request):
    blog_list = Blog.objects.all()
    context = {'blog_list' : blog_list}
    return render(request, 'main.html', context)

def first(request):
    return render(request, 'index.html')

def detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        context = {'blog' : blog}
    except Blog.DoesNotExist:
        return render(request, 'blog_error.html')
    else:
        return render(request, 'detail.html', context)

def comment_create(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.comment_set.create(content = request.POST.get('content'), create_date = timezone.now())
    return redirect('main:detail', blog_id = blog.id)

