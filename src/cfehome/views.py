from django.shortcuts import render
from visits.models import PageVisits

def index(request):
  qs= PageVisits.objects.all().count()
  PageVisits.objects.create()
  title = "Abihsolo"
  return render(request,"index.html",{"title" : title,"data" : qs})
