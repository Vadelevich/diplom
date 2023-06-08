from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, ListView, CreateView

from blog.models import Blog
from diagnostic.models import Category, Doctor, Gallery, Client


def page_not_found_view(request, exception):
    return render(request, 'diagnostic/404.html', status=404)


class HomePageView(TemplateView):
    template_name = 'diagnostic/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category'] = Category.objects.all()
        context_data['doctor'] = Doctor.objects.all()
        context_data['blog'] = Blog.objects.all()[:3:-1]
        return context_data


class AboutCompanyView(TemplateView):
    template_name = 'diagnostic/about-us.html'


class DoctorDetailView(DetailView):
    model = Doctor


class GalleryView(TemplateView):
    template_name = 'diagnostic/gallery.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Gallery.objects.all()
        return context_data


class GalleryDetailView(TemplateView):
    template_name = 'diagnostic/gallery_detail.html'

    def get(self, request, pk):
        self.object = get_object_or_404(Category, pk=pk)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['gallery_list'] = Gallery.objects.filter(category_id=self.kwargs['pk'])
        return context_data


class ContactView(TemplateView):
    template_name = 'diagnostic/contact.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # Get the current object
            inputname = request.POST["field-header"]
            inputemail = request.POST["field-header2"]
            inputmessage = request.POST["field-header-3"]
            obj = Client.objects.create(name=inputname, email=inputemail, message=inputmessage)
            obj.save()
            return redirect('diagnostic:contact')


class SearchResultsView(ListView):
    template_name = 'diagnostic/search_result.html'

    def get_queryset(self):
        query = self.request.GET['s']
        print(query)
        object_list = Blog.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
        return object_list

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['name_search'] = self.request.GET['s']
        return context_data


class CreateClient(CreateView):
    model = Client

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            inputmessage = "Получить бесплатное обследование"
            inputphone = request.POST["your-phone"]
            values_for_update = {"phone": inputphone, "message": inputmessage}
            obj, created = Client.objects.update_or_create(phone=inputphone, defaults=values_for_update)
            obj.save()
            return redirect('diagnostic:home')


class CreateSubscription(CreateView):
    model = Client

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            inputemail = request.POST["EMAIL"]
            inputmessage = "Подписка"
            send_mail(
                subject="Добро пожаловать!",
                message=" Мы рады, что Вы хотите получать наши новости!",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[inputemail],
                fail_silently=True
            )
            values_for_update = {"message": inputmessage, "email": inputemail}
            obj, created = Client.objects.update_or_create(email=inputemail, defaults=values_for_update)
            obj.save()
            return redirect('diagnostic:home')
