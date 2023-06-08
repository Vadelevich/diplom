from django.urls import path

from diagnostic.apps import DiagnosticConfig
from diagnostic.views import HomePageView, DoctorDetailView, AboutCompanyView, GalleryView, GalleryDetailView, \
    ContactView, SearchResultsView, CreateClient, CreateSubscription

app_name = DiagnosticConfig.name

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('gallery/', GalleryView.as_view(), name='galery'),
    path('about/', AboutCompanyView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('new_client/', CreateClient.as_view(), name='new_client'),
    path('new_subsc/',CreateSubscription.as_view(),name='new_subsc'),
    path('doctor_detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('gallery_detail/<int:pk>/', GalleryDetailView.as_view(), name='gallery_detail'),
]


