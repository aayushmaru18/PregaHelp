from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('blogs', views.blogs, name = 'blogs'),
    path('due_date_calculator', views.due_date_calculator, name = 'due_date_calculator'),
    path('consultation', views.consultation, name = 'consultation'),
    path('baby_weight', views.baby_weight, name = 'baby_weight'),
    path('maternal_health_risk', views.maternal_health_risk, name = 'maternal_health_risk'),
    path('calendar', views.calendar, name = 'calendar'),
    path('week-1', views.week_one, name = 'week_one'),
    path('book_appoitnment/<str:dr_name>?<str:hospital_name>', views.book_appoitnment, name = 'book_appoitnment'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)