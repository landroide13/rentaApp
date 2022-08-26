from django.shortcuts import render

# Create your views here.

def home(request):
    #question_list = Question.objects.all()
    #context = {'questions': question_list}
    return render(request, 'home.html')

    
