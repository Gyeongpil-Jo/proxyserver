from django.urls import path
from . import views


app_name = 'dna'


urlpatterns = [
    path('', views.input_dna, name='input'),
    path('<int:job_id>/dna_output', views.output_dna, name='output'),
]
