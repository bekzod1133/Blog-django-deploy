from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import PostModel
from .forms import PostForm


# Create your views here.

# def homePage(request):
#     return render(request, 'posts/home.html')

class HomePage(generic.ListView):
    model = PostModel
    template_name = 'posts/home.html'
    context_object_name = 'posts'


class DetailPage(generic.DetailView):
    model = PostModel
    template_name = 'posts/detail.html'
    context_object_name = 'post'


class UpdatePage(generic.edit.UpdateView):
    model = PostModel
    fields = ['title', 'image', 'body']
    template_name = 'posts/update.html'
    success_url = reverse_lazy('home')



class DeletePage(generic.edit.DeleteView):
    model = PostModel
    success_url = reverse_lazy('home')
    template_name = 'posts/delete.html'


class CreatePage(generic.edit.CreateView):
    model = PostModel
    fields = ['title', 'image', 'body']
    template_name = 'posts/create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)