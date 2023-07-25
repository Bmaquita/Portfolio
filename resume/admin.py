from django.contrib import admin

from .models import Skills, Interests, WorkExperience, Education, CoursesCertifications, Projects, CurriculumVitae

admin.site.register([Skills,Interests, WorkExperience, Education, CoursesCertifications, Projects, CurriculumVitae])
