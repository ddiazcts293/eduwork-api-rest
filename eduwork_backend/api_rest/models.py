from django.db import models

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
    DEGREE_TYPE = [
        ('D', 'DOCTORATE'),
        ('M', 'MASTER'),
        ('P', 'POSTGRADUATE'),
        ('E', 'ENGINEERING'),
        ('B', 'BACHELOR'),
        ('T', 'TECHNICAL'),
    ]
    name = models.CharField(max_length=60, null=False, blank=False, unique=True)
    type = models.CharField(max_length=1, choices=DEGREE_TYPE, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

class Skill(models.Model):
    SKILL_TYPE = [
        ('S', 'SOFT'),
        ('H', 'HARD'),
        ('L', 'LANGUAGE')
    ]
    name = models.CharField(max_length=60, null=False, blank=False, unique=True)
    type = models.CharField(max_length=1, choices=SKILL_TYPE, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

class City(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False, unique=True)
    state_id = models.ForeignKey(State, on_delete=models.RESTRICT, null=False, blank=False)

    def __str__(self) -> str:
            return self.name

class StudentProfile(models.Model):
    GENDER_TYPE = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('N', 'NON_BINARY'),
    ]
    first_name = models.CharField(max_length=60, null=False, blank=False)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    biografy = models.TextField(max_length=500, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_TYPE, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    email_address = models.CharField(max_length=60, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False, unique=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)
    registered_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self) -> str:
            return f"{self.first_name} {self.last_name}"

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

    def __str__(self) -> str:
            return self.name

class University(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self) -> str:
            return self.name

class Career(models.Model):
    STATUS_TYPE = [
        ('I', 'INTERNSHIP'),
        ('C', 'COMPLETED'),
        ('G', 'GRADUATED'),
        ('D', 'DEGREE_IN_PROGRESS'),
        ('U', 'INCOMPLETE'),
    ]
    TERM_TYPE = [
        ('S', 'SEMESTER'),
        ('F', 'FOUR_MONTH_TERM'),
        ('O', 'OPEN'),
    ]
    student_id = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=False, blank=False)
    university_id = models.ForeignKey(University, on_delete=models.CASCADE, null=False, blank=False)
    degree_id = models.ForeignKey(Degree, on_delete=models.CASCADE, null=False, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_TYPE, null=False, blank=False)
    term_type = models.CharField(max_length=1, choices=TERM_TYPE, null=False, blank=False)
    starting_date = models.DateField(null=False, blank=False)
    finishing_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
            return f"{self.starting_date}-{self.finishing_date}"

class Job(models.Model):
    SALARY_PERIOD_TYPE = [
        ('H', 'HOURLY'),
        ('D', 'DAILY'),
        ('W', 'WEEKLY'),
        ('M', 'MONTHLY'),
        ('Y', 'YEARLY'),
        ('P', 'PER_PROJECT'),
    ]
    WORKPLACE_TYPE = [
        ('O', 'ON_SITE'),
        ('H', 'HYBRID'),
        ('R', 'REMOTE'),
    ]
    title = models.CharField(max_length=200, null=False, blank=False)
    company_id = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, null=False, blank=False)
    min_salary = models.DecimalField(max_digits=8, decimal_places=3, null=False, blank=False)
    max_salary = models.DecimalField(max_digits=8, decimal_places=3, null=False, blank=False)
    salary_period = models.CharField(max_length=1, choices=SALARY_PERIOD_TYPE, null=False, blank=False)
    workplace_type = models.CharField(max_length=1, choices=WORKPLACE_TYPE, null=False, blank=False)
    degree_id = models.ForeignKey(Degree, on_delete=models.CASCADE, null=False, blank=False)
    type_id = models.ForeignKey(JobType, on_delete=models.CASCADE, null=False, blank=False)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    published_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self) -> str:
            return f"{self.title} ({self.published_on})"

class Application(models.Model):
    STATUS_TYPE = [
        ('A', 'APPLIED'),
        ('U', 'UNDER_REVIEW'),
        ('S', 'SHORTLISTED'),
        ('P', 'IN_PROGRESS'),
        ('H', 'HIRED'),
        ('R', 'REJECTED'),
        ('W', 'WITHDRAWN'),
    ]
    student_id = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=False, blank=False)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null=False, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_TYPE, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self) -> str:
            return f"#{self.pk} ({self.created_on})"

class Interview(models.Model):
    STATUS_TYPE = [
        ('S', 'SCHEDULED'),
        ('P', 'PENDING_CONFIRMATION'),
        ('R', 'RESCHEDULED'),
        ('C', 'COMPLETED'),
        ('X', 'CANCELLED'),
        ('N', 'NO_SHOW'),
    ]
    application_id = models.ForeignKey(Application, on_delete=models.CASCADE, null=False, blank=False)
    scheduled_date = models.DateTimeField(null=False, blank=False)
    address_or_url = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_TYPE, null=False, blank=False)
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
