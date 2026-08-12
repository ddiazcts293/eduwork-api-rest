import django_filters
from .models import Job, Skill

class JobFilter(django_filters.FilterSet):
    company_id = django_filters.NumberFilter(field_name='company__id')
    salary_period = django_filters.CharFilter(field_name='salary_period', lookup_expr='exact')
    workplace_type = django_filters.CharFilter(field_name='workplace_type', lookup_expr='exact')
    degree_id = django_filters.NumberFilter(field_name='degree__id')
    job_type_id = django_filters.NumberFilter(field_name='job_type__id',)
    city_id = django_filters.NumberFilter(field_name='city__id')
    skills = django_filters.ModelMultipleChoiceFilter(
        queryset=Skill.objects.all(),
        field_name='skills__id',
        to_field_name='id',
        conjoined=False
    )

    class Meta:
        model = Job
        fields = [
            'company_id',
            'workplace_type',
            'salary_period',
            'degree_id',
            'job_type',
            'city_id',
            'is_active',
        ]
