from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from .models import Post,Category
def index(request,pk):
    post_list=Post.objects.get(id=pk)
    return  render(request,'blogs/index.html',content_type={'post_list':post_list})
'''def detail(request,pk):
    post= get_object_or_404(Post,pk=pk)

    return render(request,'blogs/detail.html',context={'post':post})'''
def detail(request,pk):
    blogs =get_object_or_404(Post,id=pk)
    return render(request,"blogs/detail.html",{
        "blogs":blogs,'pk':pk,
    })
def category(request,pk):
    category= Category.objects.get(id=pk)
    post = category.post_set.order_by('-create_time')
    context = {'category':category,'posts':post}
    return render(request,'blogs/index.html',context)
def show(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list,1)
    page = request.GET.get('page')
    try:
        context=paginator.page(page)
    except PageNotAnInteger:
        context=paginator.page(1)
    except EmptyPage:
        context=paginator.page(paginator.num_pages)
    return render(request,'blogs/index.html',{'posts':context})
# Create your views here.
