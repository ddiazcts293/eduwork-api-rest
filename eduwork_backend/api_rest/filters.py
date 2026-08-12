import django_filters
from .models import *

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

class ApplicationFilter(django_filters.FilterSet):
    student_id = django_filters.NumberFilter(field_name='student__id')
    job_id = django_filters.NumberFilter(field_name='job__id')
    status = django_filters.CharFilter(field_name='status', lookup_expr='exact')

    class Meta:
        model = Application
        fields = [
            'student_id',
            'job_id',
            'status',
        ]

class CareerFilter(django_filters.FilterSet):
    student_id = django_filters.NumberFilter(field_name='student__id')
    university_id = django_filters.NumberFilter(field_name='university__id')
    degree_id = django_filters.NumberFilter(field_name='degree__id')
    status = django_filters.CharFilter(field_name='status', lookup_expr='exact')
    term_type = django_filters.CharFilter(field_name='term_type', lookup_expr='exact')

    class Meta:
        model = Career
        fields = [
            'student_id',
            'university_id',
            'degree_id',
            'status',
            'term_type',
        ]

class CompanyProfileFilter(django_filters.FilterSet):
    sector_id = django_filters.NumberFilter(field_name='sector__id')
    city_id = django_filters.NumberFilter(field_name='city__id')

    class Meta:
        model = CompanyProfile
        fields = [
            'sector_id',
            'city_id',
        ]

class StudentProfileFilter(django_filters.FilterSet):
    city_id = django_filters.NumberFilter(field_name='city__id')
    year = django_filters.NumberFilter(field_name='date_of_birth', lookup_expr='year')
    year_lt = django_filters.NumberFilter(field_name='date_of_birth', lookup_expr='year__lt')
    year_gt = django_filters.NumberFilter(field_name='date_of_birth', lookup_expr='year__gt')
    skills = django_filters.ModelMultipleChoiceFilter(
        queryset=Skill.objects.all(),
        field_name='skills__id',
        to_field_name='id',
        conjoined=False
    )

    class Meta:
        model = StudentProfile
        fields = [
            'city_id',
            'year',
        ]

class InterviewFilter(django_filters.FilterSet):
    application_id = django_filters.NumberFilter(field_name='application__id')
    status = django_filters.CharFilter(field_name='status', lookup_expr='exact')

    class Meta:
        model = Interview
        fields = [
            'application_id',
            'status',
        ]

class JobSkillFilter(django_filters.FilterSet):
    job_id = django_filters.NumberFilter(field_name='job__id')
    skill_id = django_filters.NumberFilter(field_name='skill__id')

    class Meta:
        model = JobSkill
        fields = [
            'job_id',
            'skill_id',
        ]

class SavedJobFilter(django_filters.FilterSet):
    job_id = django_filters.NumberFilter(field_name='job__id')

    class Meta:
        model = SavedJob
        fields = [
            'job_id',
        ]

class StudentSkillFilter(django_filters.FilterSet):
    student_id = django_filters.NumberFilter(field_name='student__id')
    skill_id = django_filters.NumberFilter(field_name='skill__id')

    class Meta:
        model = StudentSkill
        fields = [
            'student_id',
            'skill_id',
        ]
