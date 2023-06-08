from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

import blog
from blog.form import CommentForm
from blog.models import Blog, Comment


class ArticleListView(ListView):
    model = Blog
    paginate_by = 1


class ArticleDetailView(DetailView):
    model = Blog
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blocks'] = Blog.objects.all().order_by('?')
        context_data['comments'] = Comment.objects.filter(object_id=self.kwargs['pk'])
        return context_data

    def get(self, request, pk):  # Переопределяем родительский метод для подсчета просмотров
        block_item = get_object_or_404(Blog, pk=pk)
        block_item.count += 1
        block_item.save()
        return super().get(self, request, pk)

    def post(self, request, *args, **kwargs):
        # Get the current pk from the method dictionary
        pk = kwargs.get('pk')
        all = {**kwargs}
        obj = self.model.objects.get(pk=pk)
        if request.method == 'POST':
            # Get the current object
            inputtxt = request.POST["comment"]
            obj_type = ContentType.objects.get_for_model(obj)
            obj = Comment.objects.create(content_type=obj_type, object_id=obj.id, author=request.user,text=inputtxt)
            obj.save()
            return redirect('blog:read', pk=pk)

