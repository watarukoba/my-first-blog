from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
    """
    request を引数に取ります。
    render という関数を呼び出して
    blog/post_list.html テンプレートを（色々なものを合わせて）組み立てる 得た値を return しています。
    """
