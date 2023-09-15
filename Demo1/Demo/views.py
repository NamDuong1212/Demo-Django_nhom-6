from django.shortcuts import render, redirect
from Demo.forms import DemoForm
from Demo.models import Demo
# AddDemo

def create_blog(request):
    if request.method == "POST":
        form = DemoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('search/')
            except:
                pass
    else:
        form = DemoForm()
    return render(request, 'create.html', {'form':form})

#RetrieveDemo
def retrieve_blog(request):
    blogs = Demo.objects.all()
    return render(request,'search.html',{'blogs':blogs} )

#UpdateDemo
def update_blog(request,pk):
    blogs = Demo.objects.get(id=pk)
    form = DemoForm(instance=blogs)

    if request.method == 'POST':
        form = DemoForm(request.POST, instance=blogs)
        if form.is_valid():
            form.save()
            return redirect('/search')

    context = {
        'blogs': blogs,
        'form': form,
    }
    return render(request,'update.html',context)

#DeleteDemo
def delete_blog(request, pk):
    blogs = Demo.objects.get(id=pk)

    if request.method == 'POST':
        blogs.delete()
        return redirect('/search')

    context = {
        'blogs': blogs,
    }
    return render(request, 'remove.html', context)

def add(request):
    if request.method == "POST":
        form = DemoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search')
            except:
                pass
    else:
        form = DemoForm()
    return render(request, 'add.html', {'form':form})

