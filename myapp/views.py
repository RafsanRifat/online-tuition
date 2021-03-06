from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from .models import Contact, Post
from .forms import ContactForm, PostForm
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib import messages


# Create your views here.


def home(request):
    name = ['Rifat', 'Tahsin', 'Asif', 'Arman']
    contex = {
        'name': name
    }
    return render(request, 'index.html', contex)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # text = form.cleaned_data['text']
            # obj = Contact(name=name, email=email, text=text)
            # obj.save()    # django form er khetre code gulo dorkar, r Model form use korle code gulo use na kore form.save() diyeai kaj hbe
            form.save()  # uporer code gulo na use kore eita use korleo form data save hobe database a
            messages.success(request, 'Form successfully  submitted ')  # we can also use here message.error,debug, warning,info
            return redirect('post')
        else:
            messages.error(request, 'Form successfully  submitted ')

    else:
        form = ContactForm()
    contex = {'form': form}

    return render(request, 'contact.html', contex)


class PostListView(ListView):  # List view
    template_name = 'postlist.html'
    model = Post
    context_object_name = 'postlist'


class PostDetailView(DetailView):
    model = Post
    template_name = 'postdetail.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'postcreate.html'

    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('postdetails', kwargs={'pk': id})


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('postlistview')


def post(request):
    post = Post.objects.all()
    contex = {'post': post}
    return render(request, 'post.html', contex)


def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            sub = form.cleaned_data['subject']
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in = form.cleaned_data['class_in']
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
            return HttpResponse('Your form is successfully submited')
    else:
        form = PostForm
    contex = {'form': form}
    return render(request, 'postcreate.html', contex)
