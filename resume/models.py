from django.db import models

from datetime import datetime


class Skills(models.Model):

    name = models.CharField(max_length=100)

    icon = models.ImageField(upload_to='Skills Icons', null=True, blank=True)

    description = models.TextField(max_length=100)

    created_date = models.DateField(default=datetime.now)
    
    def __str__(self):

        return self.name
    
    class Meta:

        verbose_name=verbose_name_plural = "Skills"


class Interests(models.Model):
    
    interests = models.CharField(max_length=100)

    def __str__(self):

        return self.interests

    
    class Meta:
        verbose_name = verbose_name_plural = "Interests"


class WorkExperience(models.Model):

    position = models.CharField(max_length=100)

    from_to_and_status = models.CharField(max_length=200)

    employer = models.CharField(max_length=100)

    description = models.TextField(max_length=200)

    created_date = models.DateField(default=datetime.now)

    def __str__(self):

        return self.position


class Education(models.Model):

    course_name = models.CharField(max_length=100)

    from_to_and_status = models.CharField(max_length=100)

    institution = models.CharField(max_length=100)

    created_date = models.DateField(default=datetime.now)

    def __str__(self):

        return self.course_name


class CoursesCertifications(models.Model):

    name = models.CharField(max_length=200)

    link = models.URLField(null=True, blank=True)

    certificate = models.ImageField(upload_to="Certifications")

    created_date = models.DateField(default=datetime.now)

    def __str__(self):

        return self.name

    
    class Meta:

        verbose_name = verbose_name_plural = "Courses & Certifications"


class Projects(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    github_link = models.URLField(blank=True, null=True)

    created_date = models.DateField(default=datetime.now)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = verbose_name_plural = "Projects"


class CurriculumVitae(models.Model):

    cv = models.FileField(upload_to='CV')
    
    def __str__(self):
    
        return str(self.cv)

    class Meta:

        verbose_name = verbose_name_plural = " Curriculum Vitae"