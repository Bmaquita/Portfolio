from django.core.mail import BadHeaderError, send_mail

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import messages 

from django.shortcuts import render, redirect

from personal_info.models import ProfilePhoto, PersonalInfo, SocialMedia

from resume.models import Skills, Interests, WorkExperience, Education,  CoursesCertifications, Projects, CurriculumVitae

# Create your views here.
def index(request):
    #personal info app
    personal_informations = PersonalInfo.objects.all()

    profile_foto = ProfilePhoto.objects.first()

    contact_information = PersonalInfo.objects.first()

    social_media = SocialMedia.objects.all()

    #resume app

    skills = Skills.objects.all()

    interests = Interests.objects.all()

    work_expirience = WorkExperience.objects.all().order_by('-created_date')

    education = Education.objects.all().order_by('-created_date')

    #courses and certifications

    default_page = 1

    page = request.GET.get('page', default_page)

    courses_and_certifications = CoursesCertifications.objects.all().order_by('-created_date')

    courses_per_page = 3

    paginator = Paginator(courses_and_certifications, courses_per_page)

    try:

        course_page = paginator.page(page)
    
    except PageNotInteger:

        course_page = paginator.page(default_page)

    except:

        course_page = paginator.page(paginator.num_pages)
        


    ###########################################################

    projects = Projects.objects.all().order_by('-created_date')

    cv = CurriculumVitae.objects.first()

    context = {
        'personal_informations':personal_informations,
        'profile_foto':profile_foto,
        'social_media':social_media,
        'contact_information':contact_information,
        'skills':skills,
        'interests':interests,
        'work_expirience':work_expirience,
        'education':education,
        'course_page':course_page,
        'projects':projects,
        'cv':cv
    }

    return render(request, 'pages/static_content/index.html', context)


def contact_form(request):

    if request.method == "POST":

        name = request.POST["name"]

        from_email = request.POST["email"]

        subject = request.POST["subject"]

        message = request.POST["msg"]

        subject_sender =  f"From: <{from_email}> - Subject: {subject}"

        email_message = f"Name: {name}\n Message: {message} \n This message came from Bmaquita Portfolio "

        send_mail(
        subject_sender,
        email_message,
        from_email,
        ['dinomaquita@gmail.com', 'bernardinorafael1998@gmail.com'],
        fail_silently=False,
    )

        return render(request, "pages/static_content/thank-you.html")



