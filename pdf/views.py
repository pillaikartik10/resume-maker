from django import template
from django.shortcuts import render,redirect
from .models import Profile
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.urls import reverse
import os,sys, subprocess, platform

from django.conf import settings

import pdfkit
import io


# Create your views here.

def accept(request):

    if request.method == "POST":
        name = request.POST.get("name","")
        phone = request.POST.get("phone","")
        about_you = request.POST.get("about_you","")
        email = request.POST.get("email","")
        degree = request.POST.get("degree","")
        university = request.POST.get("university","")
        skill = request.POST.get("skill","")
        previous_work_title = request.POST.get("previous_work_title","")
        previous_work_company = request.POST.get("previous_work_company","")
        previous_work = request.POST.get("previous_work","")
        school = request.POST.get("school","")
        project_title = request.POST.get("project_title","")
        projects = request.POST.get("projects","")
        cgpa = request.POST.get("cgpa","")
        school_percentage = request.POST.get("school_percentage","")
        interests = request.POST.get("interests","")

        profile = Profile(name=name,phone=phone,about_you=about_you,email=email,degree=degree,university=university,skill=skill,previous_work=previous_work,school=school,projects=projects,cgpa=cgpa,school_percentage=school_percentage,previous_work_title=previous_work_title,previous_work_company=previous_work_company,project_title=project_title,interests=interests)
        profile.save()
        request.session['id'] = profile.pk
        #messages.success(request, 'Contact request submitted successfully.')
        return redirect('/options/')

    return render(request,"accept.html")

def options(request):
    return render(request,'options.html')

#older
#def resume(request,id):
def resume(request):
    #modification
    id = request.session.get('id')

    user_profile = Profile.objects.get(pk = id)
    template = loader.get_template("resume.html")
    html = template.render({'user_profile':user_profile})
    option = {
        'enable-local-file-access': None,
        'disable-smart-shrinking':'',
        'page-size': 'A4',
        'margin-top': '0.2cm',
        'margin-right': '0.2cm',
        'margin-bottom': '0.2cm',
        'margin-left': '0.5cm',
        'encoding': "UTF-8",
        'no-outline': None
    }
    #config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

    if platform.system() == "Windows":
        pdfkit_config = pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
    else:
        os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable) 
        WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')], 
            stdout=subprocess.PIPE).communicate()[0].strip()
        pdfkit_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)

    pdf = pdfkit.from_string(html,False,option,configuration = pdfkit_config)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response


def view_online(request):
    id = request.session.get('id')

    user_profile = Profile.objects.get(pk = id)
    return render(request,"resume.html",{'user_profile':user_profile})
