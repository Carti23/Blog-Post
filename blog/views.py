from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import CreateBlogPostForm, UpdateBlogPostForm
from users.models import Profile
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
def post(request):
    posts = BlogPost.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'blog/post.html', context)



def create_blog_view(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreateBlogPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Profile.objects.filter(email=request.user.email).first()
		obj.author = author
		obj.save()
		form = CreateBlogPostForm()
		return redirect('home')

	context['form'] = form

	return render(request, 'blog/create_blog.html', context)



def detail_blog_view(request, slug):

	context = {}
	blog_post = get_object_or_404(BlogPost, slug=slug)
	context['blog_post'] = blog_post

	return render(request, 'blog/detail_blog.html', context)




def edit_blog_view(request, slug):
	
	context = {}
	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	blog_post = get_object_or_404(BlogPost, slug=slug)
	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			blog_post = obj
			return redirect('home')
	
	form = UpdateBlogPostForm(
			initial={
					"title": blog_post.title, 
					"body": blog_post.body,
					"image": blog_post.image,
					"slug": slug,
				}
			)
	context['form'] = form

	return render(request, 'blog/edit_blog.html', context)