from django.urls import path, include
from rest_framework import urls
from rest_framework.routers import DefaultRouter
from .viewsets.student_profile_viewset import StudentProfileViewSet
from .viewsets.application_viewset import ApplicationViewSet
from .viewsets.career_viewset import CareerViewSet
from .viewsets.city_viewset import CityViewSet
from .viewsets.company_profile_viewset import CompanyProfileViewSet
from .viewsets.company_sector_viewset import CompanySectorViewSet
from .viewsets.degree_viewset import DegreeViewSet
from .viewsets.interview_viewset import InterviewViewSet
from .viewsets.job_skill_viewset import JobSkillViewSet
from .viewsets.job_type_viewset import JobTypeViewSet
from .viewsets.job_viewset import JobViewSet
from .viewsets.saved_job_viewset import SavedJobViewSet
from .viewsets.skill_viewset import SkillViewSet
from .viewsets.state_viewset import StateViewSet
from .viewsets.student_skill_viewset import StudentSkillViewSet
from .viewsets.university_viewset import UniversityViewSet

router = DefaultRouter()
router.register(r'student_profiles', StudentProfileViewSet, basename='student_profile')
router.register(r'applications', ApplicationViewSet, basename='application')
router.register(r'careers', CareerViewSet, basename='career')
router.register(r'cities', CityViewSet, basename='city')
router.register(r'company_profiles', CompanyProfileViewSet, basename='company_profile')
router.register(r'company_sectors', CompanySectorViewSet, basename='company_sector')
router.register(r'degrees', DegreeViewSet, basename='degree')
router.register(r'interviews', InterviewViewSet, basename='interview')
router.register(r'job_skills', JobSkillViewSet, basename='job_skill')
router.register(r'job_types', JobTypeViewSet, basename='job_type')
router.register(r'jobs', JobViewSet, basename='job')
router.register(r'saved_jobs', SavedJobViewSet, basename='saved_job')
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'states', StateViewSet, basename='state')
router.register(r'student_skills', StudentSkillViewSet, basename='student_skill')
router.register(r'universities', UniversityViewSet, basename='university')

urlpatterns = [
    path('', include(router.urls)),
]
