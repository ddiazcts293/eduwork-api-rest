from django.db import models
from django_enum import EnumField

# Create your models here. ** Usar PascalCase para los nombres de las clases y snake_case para los nombres de los atributos **

class CompanySector(models.Model):
    description = models.CharField(max_length=40, null=False, blank=False)

class City(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False, unique=True)
    state = models.CharField(max_length=60, null=False, blank=False)

class JobType(models.Model):
    description = models.CharField(max_length=40, null=False, blank=False, unique=True)

class Degree(models.Model):
    class DegreeType(models.TextChoices):
        DOCTORATE = 'D', 'DOCTORATE'
        MASTER = 'M', 'MASTER'
        ENGINEERING = 'E', 'ENGINEERING'
        BACHELOR = 'B', 'BACHELOR',
        TECHNICAL = 'T', 'TECHNICAL'
    name = models.CharField(max_length=60, null=False, blank=False, unique=True)
    type = EnumField(DegreeType, null=False, blank=False)

class Skill(models.Model):
    class SkillType(models.TextChoices):
        SOFT = 'S', 'SOFT'
        HARD = 'H', 'HARD'
    name = models.CharField(max_length=60, null=False, blank=False, unique=True)
    type = EnumField(SkillType, null=False, blank=False)

class StudentProfile(models.Model):
    class GenderType(models.TextChoices):
        MALE = 'M', 'MALE'
        FEMALE = 'F', 'FEMALE'
    first_name = models.CharField(max_length=60, null=False, blank=False)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    biografy = models.TextField(max_length=500, null=True, blank=True)
    gender = EnumField(GenderType, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    email_address = models.CharField(max_length=60, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False, unique=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)
    registered_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)

class CompanyProfile(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    biography = models.TextField(max_length=500, null=True, blank=True)
    sector_id = models.ForeignKey(CompanySector, on_delete=models.CASCADE, null=False, blank=False)
    email_address = models.CharField(max_length=60, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False, unique=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    establish_year = models.IntegerField(null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)
    registered_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)

class University(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)

class Career(models.Model):
    class StatusType(models.TextChoices):
        INTERNSHIP = 'I', 'INTERNSHIP'
        COMPLETED = 'C', 'COMPLETED'
        GRADUATED = 'G', 'GRADUATED'
        DEGREE_IN_PROGRESS = 'D', 'DEGREE_IN_PROGRESS'
        INCOMPLETE = 'U', 'INCOMPLETE'
    class TermType(models.TextChoices):
        SEMESTER = 'S', 'SEMESTER'
        FOUR_MONTH_TERM = 'F', 'FOUR_MONTH_TERM'
        OPEN = 'O', 'OPEN' 
    student_id = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=False, blank=False)
    university_id = models.ForeignKey(University, on_delete=models.CASCADE, null=False, blank=False)
    degree_id = models.ForeignKey(Degree, on_delete=models.CASCADE, null=False, blank=False)
    status = EnumField(StatusType, null=False, blank=False)
    term_type = EnumField(TermType, null=False, blank=False)
    starting_date = models.DateField(null=False, blank=False)
    finishing_date = models.DateField(null=True, blank=True) # Se agregará un check en el futuro una vez le comente a Danny lo de los serializers y como configurar ese aspecto

class Job(models.Model):
    class SalaryPeriodType(models.TextChoices):
        DAILY = 'D', 'DAILY'
        WEEKLY = 'W', 'WEEKLY'
        MONTHLY = 'M', 'MONTHLY'
        YEARLY = 'Y', 'YEARLY'
        PER_PROJECT = 'P', 'PER_PROJECT'
    class WorkplaceType(models.TextChoices):
        ON_SITE = 'O', 'ON_SITE'
        HYBRID = 'H', 'HYBRID'
        REMOTE = 'R', 'REMOTE'
    title = models.CharField(max_length=200, null=False, blank=False)
    company_id = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, null=False, blank=False)
    min_salary = models.DecimalField(max_digits=8, decimal_places=3, null=False, blank=False)
    max_salary = models.DecimalField(max_digits=8, decimal_places=3, null=False, blank=False)
    salary_period = EnumField(SalaryPeriodType, null=False, blank=False)
    workplace_type = EnumField(WorkplaceType, null=False, blank=False)
    degree_id = models.ForeignKey(Degree, on_delete=models.CASCADE, null=False, blank=False)
    type_id = models.ForeignKey(JobType, on_delete=models.CASCADE, null=False, blank=False)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    published_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)

class Application(models.Model):
    class StatusType(models.TextChoices):
        APPLIED = 'A', 'APPLIED'
        UNDER_REVIEW = 'U', 'UNDER_REVIEW'
        SHORTLISTED = 'S', 'SHORTLISTED'
        IN_PROGRESS = 'P', 'IN_PROGRESS'
        HIRED = 'H', 'HIRED'
        REJECTED = 'R', 'REJECTED'
        WITHDRAWN = 'W', 'WITHDRAWN'
    student_id = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=False, blank=False)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null=False, blank=False)
    status = EnumField(StatusType, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False)

class Interview(models.Model):
    class StatusType(models.TextChoices):
        SCHEDULED = 'S', 'SCHEDULED'
        PENDING_CONFIRMATION = 'P', 'PENDING_CONFIRMATION'
        RESCHEDULED = 'R', 'RESCHEDULED'
        COMPLETED = 'C', 'COMPLETED'
        CANCELLED = 'X', 'CANCELLED'
        NO_SHOW = 'N', 'NO_SHOW'
    application_id = models.ForeignKey(Application, on_delete=models.CASCADE, null=False, blank=False)
    scheduled_date = models.DateTimeField(null=False, blank=False)
    address_or_url = models.CharField(max_length=255, null=False, blank=False)
    status = EnumField(StatusType, null=False, blank=False)
    registered_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)

class StudentSkill(models.Model):
    student_id = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=False, blank=False)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE, null=False, blank=False)

class JobSkill(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null=False, blank=False)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE, null=False, blank=False)

class SavedJob(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null=False, blank=False)
    student_id = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=False, blank=False)
    saved_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)


