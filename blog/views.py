from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def post_list(request,*args, **kwargs):
	obj=Post.objects.all().order_by('-date');
	kontekst={
		'front_obj':obj[0:3],
		'obj':obj[3:]
	}
	return render(request,'main.html',kontekst)

def show_post(request,slug,*args,**kwargs):
	# slug=Post(request.GET or None)
	
	obj=Post.objects.get(slug=slug)
	# obj.image.name=obj.image.name.strip('static')
	# image=String(obj.image)
	# print(type(image))
	context={
		'obj':obj
	}
	return render(request,'post.html',context)

def post_form(request,*args,**kwargs):
	form=PostForm(request.POST or None)
	if form.is_valid():
		form.save(commit=True)
		form=PostForm()
	context={
		'form':form
	}
	return render(request,'postform.html',context)