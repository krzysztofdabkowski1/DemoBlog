from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def widok(request,*args, **kwargs):
	kontekst={
		'jakies_dane':'super mega dane',
		'lista':[12,34,45,56,67,87,90],
		'lista2':range(1,8),
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