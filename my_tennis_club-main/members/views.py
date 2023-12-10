from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

"""def member_list(request):
    all_members = Member.objects.all()
    teenage_members = Member.objects.filter(age__lt=20)
    adult_members = Member.objects.filter(age__gte=20)

    return render(request, 'member_list.html', {
        'all_members': all_members,
        'teenage_members': teenage_members,
        'adult_members': adult_members,
    })

def court_list(request):
    courts = Court.objects.all()
    return render(request, 'court_list.html', {'courts': courts})

def court_detail(request, court_id):
    court = Court.objects.get(pk=court_id)
    return render(request, 'court_detail.html', {'court': court})
"""