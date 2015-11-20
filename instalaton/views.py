from django.shortcuts import render

# Create your views here.
def instalaton_list(request):
    return render(request,'instalaton/instalaton_list.html',{})