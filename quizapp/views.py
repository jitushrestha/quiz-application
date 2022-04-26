from turtle import title
from django.conf import settings
from django.dispatch import receiver
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from quizapp.form import quizappForm, QuestionForm, UserForm, UserLoginForm
from quizapp.models import AdminLogin, Question, User
from django.core.mail import send_mail


# Create your views here.
# def index(request):
#     data={
#         'message': 'hello world'
#     }
#     return render(request,"index.html", data)

#user index
def Index(request):
    username = request.session['username']
    return render (request,"userIndex.html",{'username': username})

#admin index
def adminIndex(request):
    username = request.session['username']
    return render (request,"index.html",{'username': username})


#admin
def adminlogin(request):
    loginform = quizappForm
    return render(request,"login.html",{'form':loginform})

def adminLoginpost(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    adminLoginForm = quizappForm()
    try:
        user = AdminLogin.objects.get(username=username)
        if(password == user.password):
            request.session['username'] = username
            return render(request, "index.html", {'username':username})
        else:
            msg = "Invalid Password"
            return render(request, "login.html", {'form':adminLoginForm, 'msg':msg })
    except:
        msg = "Invalid username"
        return render(request, "login.html", {'form':adminLoginForm, 'msg':msg })






    
def createQuestions(request):
    ques = QuestionForm
    return render(request, "createquestion.html", {'form':ques})
    

def saveQuestions(request):
    ques_form = QuestionForm
    try:
        question = request.POST.get("question")
        option1 = request.POST.get("option1")
        option2 = request.POST.get("option2")
        option3 = request.POST.get("option3")
        option4 = request.POST.get("option4")
        correctAns = request.POST.get("correctAns")

        ques = Question(question=question, option1 = option1, option2=option2, option3=option3, option4=option4, correctAns=correctAns)
        ques.save()
        msg = "Question Added Successfully!!!!"
        return render(request, "createquestion.html", {'form':ques_form, 'msg':msg})
    except:
        msg = "Error!!!"
        return render(request, "createquestion.html", {'form':ques_form, 'msg':msg}) 

def showAllQuestion(request):
    ques = Question.objects.all()
    return render(request, "showques.html", {'quesList':ques} )

def editques(request, note_id):
    view = Question.objects.get(id=note_id)
    return render(request, "edit.html", {'view':view})

def updateques(request):
    note_id = request.POST.get('id')  
    try:
        #data fetch by id
        view = Question.objects.get(id=note_id)  
        view.question = request.POST.get('question')
        view.option1 = request.POST.get('option1')
        view.option2 = request.POST.get('option2')
        view.option3 = request.POST.get('option3')
        view.option4 = request.POST.get('option4')
        view.correctAns = request.POST.get('correctAns')
        view.save()
        msg = "successfully updated"  
        all_question = Question.objects.all() 
        return render(request, "showques.html", {'msg':msg, 'quesList': all_question })
    except:
        msg = "Not update"
        view = Question.objects.get(id=note_id)
        return render(request, 'edit.html', {'view':view, 'msg':msg})    

def deleteques(request, note_id):
    data = Question.objects.get(id=note_id)
    data.delete()
    view = Question.objects.all()
    return render(request, 'showques.html', {'quesList':view}) 

def adminLogout(request):
    admin_login = quizappForm()
    if request.session.has_key('username'):
            del request.session['username']
            return render(request, "login.html",{'form' : admin_login})
    else:
            return render(request, "login.html",{'form' : admin_login})






#user registeration
def register(request):
    reg_form = UserForm()
    return render(request, "register.html", {'form': reg_form}) 

def userRegister(request):
    reg_form = UserForm()
    try:
        # if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            msg = "User Registered Successfully"
            return render(request, "register.html", {'form': reg_form, 'msg' : msg})
        else:
            msg = "Ivalid !!!!"
            return render(request, "register.html", {'form': reg_form, 'msg' : msg})

    except:
        msg = "Failed to register!!"
        return render(request, "register.html", {'form': reg_form, 'msg' : msg})




def userLoginForm(request):
    user_login = UserLoginForm()
    return render(request, 'userlogin.html', {'form': user_login} )

def userLogin(request):
    user_login = UserLoginForm()
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = User.objects.get(username = username)
        if(password == user.password):
            request.session['id'] = user.id
            request.session['username'] = user.username
            request.session['email'] = user.email
            return render(request, 'userIndex.html', {'username' : username})

        else:
            msg = "wrong password"
            return render(request, 'userlogin.html', {'form' : user_login, 'msg':msg})    
    except:
        msg = "Inavlid username!!!!"
        return render(request, 'userlogin.html', {'form' : user_login, 'msg':msg})



def startQuiz(request):
    username = request.session['username']
    allquestion = Question.objects.all()
    return render(request, 'quiz.html', {'allquestion': allquestion, 'username':username})    

def userProfile(request): 
    username = request.session['username']  
    user_id = request.session['id']
    user_details = User.objects.get(id=user_id)
    return render(request, "userprofile.html",{'data':user_details, 'username':username} )

def userLogout(request):
    user_login = UserLoginForm()
    if request.session.has_key('username'):
            del request.session['username']
            return render(request, "userlogin.html",{'form' : user_login})
    else:
            return render(request, "userlogin.html",{'form' : user_login})
    



def sendEmail(request):
    if request.method == "GET":
        marks = request.GET.get('marks', None)
        receiver = request.session['email']
        send_mail(
                subject = "Your Quiz Result",
                message = "You Score"  + marks +  "marks in the recent quiz",
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [receiver],
                fail_silently = False,
                
        )
        return JsonResponse ({"success": "Sent Successfully"}, status=200)
    else:
        return JsonResponse ({"error": "form.errors"}, status=400)
