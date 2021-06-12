from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request,"main/header.html",)

def Email_tab(request):
    return redirect("Email/Create_Campaign")

def Email_tabs(request,side_tab):
    #campaign_name = request.session['campaign_name']
    return render(request,"main/Email_tab/"+side_tab+".html"
       # {'campaign_name': campaign_name}
    )

def create_campaign(request,campaign_name):
    if campaign_name:
        request.session['campaign_name'] = campaign_name
        return render(request,"main/Email_tab/"+"Create_campaign"+".html",{
            'campaign_name':campaign_name
        })

    else:
        messages.error(request, "Select Campaign name")

def sub_side_tab(request,side_tab,sub_side_tab):
    campaign_name = request.session['campaign_name']
    return render(request, "main/Email_tab/" + side_tab + "/" +
                  sub_side_tab + ".html",{
        'campaign_name': campaign_name
    })
