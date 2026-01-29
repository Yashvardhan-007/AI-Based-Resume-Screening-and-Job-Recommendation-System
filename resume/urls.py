from django.urls import path
from .views import add_resume, add_job, match_view

urlpatterns = [
    path('resume/', add_resume),
    path('job/', add_job),
    path('match/<int:rid>/<int:jid>/', match_view),
]
