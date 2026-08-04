from django.db import models
from django_enum import EnumField
from users.models import EduWorkUser

# Create your models here.

class CompanySector(models.Model):
    description = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self) -> str:
        return self.description

class State(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False, unique=True)

    def __str__(self) -> str:
        return self.name

class JobType(models.Model):
    description = models.CharField(max_length=40, null=False, blank=False, unique=True)

    def __str__(self) -> str:
            return self.description

class Degree(models.Model):
    class DegreeType(models.TextChoices):
        DOCTORATE = 'DOCTORATE', 'Doctorate'
        MASTER = 'MASTER', 'Master'
        POSTGRADUATE = 'POSTGRADUATE', 'Postgraduate'
        ENGINEERING = 'ENGINEERING', 'Engineering'
        BACHELOR = 'BACHELOR', 'Bachelor'
        TECHNICAL = 'TECHNICAL', 'Technical'
    name = models.CharField(max_length=60, null=False, blank=False, unique=True)
    type = EnumField(DegreeType, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

class Skill(models.Model):
    class SkillType(models.TextChoices):
        SOFT = 'SOFT', 'Soft'
        HARD = 'HARD', 'Hard'
        LANGUAGE = 'LANGUAGE', 'Language'
    name = models.CharField(max_length=60, null=False, blank=False, unique=True)
    type = EnumField(SkillType, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

class City(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False, unique=True)
    state = models.ForeignKey(State, on_delete=models.RESTRICT, null=False, blank=False)

    def __str__(self) -> str:
            return self.name

class StudentProfile(models.Model):
    class GenderType(models.TextChoices):
        MALE = 'MALE', 'Male'
        FEMALE = 'FEMALE', 'Female'
        NON_BINARY = 'NON_BINARY', 'NonBinary'

    user = models.OneToOneField(EduWorkUser, on_delete=models.CASCADE, related_name='student_profile')
    first_name = models.CharField(max_length=60, null=False, blank=False)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    biografy = models.TextField(max_length=500, null=True, blank=True)
    gender = EnumField(GenderType, null=True, blank=True)
    date_of_birth = models.DateField(null=False, blank=False)
    email_address = models.EmailField(max_length=60, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False, unique=True)
    city = models.ForeignKey(City, on_delete=models.RESTRICT, null=False, blank=False)
    registered_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class CompanyProfile(models.Model):
    user = models.OneToOneField(EduWorkUser, on_delete=models.CASCADE, related_name='company_profile')
    name = models.CharField(max_length=60, null=False, blank=False)
    biography = models.TextField(max_length=500, null=True, blank=True)
    sector = models.ForeignKey(CompanySector, on_delete=models.RESTRICT, null=False, blank=False)
    email_address = models.EmailField(max_length=60, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False, unique=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    establish_year = models.IntegerField(null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.RESTRICT, null=False, blank=False)
    registered_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self) -> str:
            return self.name

class University(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self) -> str:
            return self.name

class Career(models.Model):
    class StatusType(models.TextChoices):
        INTERNSHIP = 'INTERNSHIP', 'Internship'
        COMPLETED = 'COMPLETED', 'Completed'
        GRADUATED = 'GRADUATED', 'Graduated'
        DEGREE_IN_PROGRESS = 'DEGREE_IN_PROGRESS', 'DegreeInProgress'
        INCOMPLETE = 'INCOMPLETE', 'Incomplete'
    class TermType(models.TextChoices):
        SEMESTER = 'SEMESTER', 'Semester'
        FOUR_MONTH_TERM = 'FOUR_MONTH_TERM', 'FourMonthTerm'
        OPEN = 'OPEN', 'Open'
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=False, blank=False)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=False, blank=False)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=False, blank=False)
    status = EnumField(StatusType, null=False, blank=False)
    term_type = EnumField(TermType, null=False, blank=False)
    starting_date = models.DateField(null=False, blank=False)
    finishing_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
            return f"{self.starting_date}-{self.finishing_date}"

class Job(models.Model):
    class SalaryPeriodType(models.TextChoices):
        HOURLY = 'HOURLY', 'Hourly'
        DAILY = 'DAILY', 'Daily'
        WEEKLY = 'WEEKLY', 'Weekly'
        MONTHLY = 'MONTHLY', 'Monthly'
        YEARLY = 'YEARLY', 'Yearly'
        PER_PROJECT = 'PER_PROJECT', 'PerProject'
    class WorkplaceType(models.TextChoices):
        ON_SITE = 'ON_SITE', 'OnSite'
        HYBRID = 'HYBRID', 'Hybrid'
        REMOTE = 'REMOTE', 'Remote'
    title = models.CharField(max_length=200, null=False, blank=False)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, null=False, blank=False)
    min_salary = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    max_salary = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    salary_period = EnumField(SalaryPeriodType, null=False, blank=False)
    workplace_type = EnumField(WorkplaceType, null=False, blank=False)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=False, blank=False)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    published_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self) -> str:
            return f"{self.title} ({self.published_on})"

class Application(models.Model):
    class StatusType(models.TextChoices):
        APPLIED = 'APPLIED', 'Applied'
        UNDER_REVIEW = 'UNDER_REVIEW', 'UnderReview'
        SHORTLISTED = 'SHORTLISTED', 'Shortlisted'
        IN_PROGRESS = 'IN_PROGRESS', 'InProgress'
        HIRED = 'HIRED', 'Hired'
        REJECTED = 'REJECTED', 'Rejected'
        WITHDRAWN = 'WITHDRAWN', 'Withdrawn'
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=False, blank=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=False, blank=False)
    status = EnumField(StatusType, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self) -> str:
            return f"#{self.pk} ({self.created_on})"

class Interview(models.Model):
    class StatusType(models.TextChoices):
        SCHEDULED = 'SCHEDULED', 'Scheduled'
        PENDING_CONFIRMATION = 'PENDING_CONFIRMATION', 'PendingConfirmation'
        RESCHEDULED = 'RESCHEDULED', 'Rescheduled'
        COMPLETED = 'COMPLETED', 'Completed'
        CANCELLED = 'CANCELLED', 'Cancelled'
        NO_SHOW = 'NO_SHOW', 'NoShow'
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=False, blank=False)
    scheduled_date = models.DateTimeField(null=False, blank=False)
    address_or_url = models.CharField(max_length=255, null=False, blank=False)
    status = EnumField(StatusType, null=False, blank=False)
    registered_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)

class StudentSkill(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=False, blank=False)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=False, blank=False)

class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=False, blank=False)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=False, blank=False)

class SavedJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=False, blank=False)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=False, blank=False)
    saved_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
