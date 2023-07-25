from django.db import models

class ProfilePhoto(models.Model):

    about_me_photo = models.ImageField(upload_to="Profile Photo")


    def __str__(self):

        return str(self.about_me_photo)

    class Meta:

        verbose_name = "Profile Photo"

        verbose_name_plural = "Profile Photo"




class PersonalInfo(models.Model):

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    title = models.CharField(max_length=100)

    email = models.EmailField()

    nationality = models.CharField(max_length=50)

    languages = models.CharField(max_length=150)

    address = models.CharField(max_length=100)

    phone_1 = models.CharField(max_length=30)

    phone_2 = models.CharField(max_length=30, blank=True)


    class Meta:

        verbose_name = "Personal Information"

    
    def __str__(self):

        return self.first_name


class SocialMedia(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    icon = models.CharField(max_length=100, null=True)

    def __str__(self):

        return self.name
