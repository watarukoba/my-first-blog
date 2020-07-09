from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
    """
    request を引数に取ります。
    render という関数を呼び出して
    blog/post_list.html テンプレートを（色々なものを合わせて）組み立てる 得た値を return しています。
    """
