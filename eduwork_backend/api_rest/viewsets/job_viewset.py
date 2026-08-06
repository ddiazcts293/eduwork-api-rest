from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Job
from ..serializers.job_serializer import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    # Motores de filtrado
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # Filtrado exacto
    filterset_fields = [
        'company',
        'salary_period',
        'workplace_type',
        'degree',
        'job_type',
        'city',
        'company__sector',
    ]
    # Búsqueda de texto
    search_fields = ['title', 'description', 'company__name']
    # Ordenamiento
    ordering_fields = ['min_salary', 'max_salary', 'published_on']
