from django.shortcuts import render
from django.contrib import messages

from app1.models import Facultyreg,Studentreg,SessionModel,SchdexamsModel,AssignmentModel,SubmitAssignment
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request,"index.html")


def dept(request):
    return render(request,"dept.html")

def placement(request):
    return render(request,"placements.html")

def examsView(request):
    exams =SchdexamsModel.objects.all()
    return render(request,"Views exams.html",{"exams":exams})

def contact(request):
    return render(request,"contact.html")


#Admin

def admin(request):
    return render(request,"admin.html")


def adminHome(request):
    name = request.POST.get('t1')
    pwd = request.POST.get('t2')
    if name == 'admin' and pwd == 'admin':
        return render(request,"adminhome.html")
    else:
        return render(request, 'admin.html', {'error': 'login fail'})

def welcomeAdmin(request):
    return render(request,"adminhome.html")


def schdSessions(request):
    return render(request,"Schdses.html")

def seshses(request):
    subj = request.POST.get("t1")
    fac = request.POST.get("t2")
    da = request.POST.get("t3")
    t = request.POST.get("t4")
    dur = request.POST.get("t5")

    print(subj, fac, da, t, dur, )
    try:
        SessionModel(subn=subj,facname=fac,date=da,time=t,duration=dur).save()
        return render(request, "Schdses.html", {'msg': 'Session Schduled Successfully'})
    except SessionModel.DoesNotExist:
        return render(request, 'Schdses.html', {'msg': 'not saved'})

def schdExams(request):
    return render(request,"Schd Exams.html")

def saveExams(request):
    sem = request.POST.get("t1")
    date = request.POST.get("t2")
    time = request.POST.get("t3")
    fee = request.POST.get("t4")
    dura = request.POST.get("t5")
    tb = request.FILES["t6"]
    print(sem , date)
    try:
        SchdexamsModel(sem=sem,date=date,time=time,fee=fee,duration=dura,timetable=tb).save()
        return render(request,"Schd Exams.html",{"msg":'Exam Schduled Successfully'})
    except SchdexamsModel.DoesNotExist:
        return render(request,"Schd Exams.html", {'msg': 'not saved'})

def viewFac(request):
    faculty = Facultyreg.objects.all()
    return render(request,"View Faculty.html",{"faculty":faculty})

def facDelete(request):
    d=request.GET.get('del')
    Facultyreg.objects.filter(fno=d).delete()
    messages.success(request,'Deleted successfully')
    return redirect('viewfac')

def viewStud(request):
    student = Studentreg.objects.all()
    return render(request,"view students.html",{"student":student})

def studDelete(request):
    d=request.GET.get('del')
    Studentreg.objects.filter(sno=d).delete()
    messages.success(request,'Deleted successfully')
    return redirect('viewstud')

#Faculty

def fReg(request):
  return render(request,"Freg.html")

def fsign(request):
    na = request.POST.get("a1")
    un = request.POST.get("a2")
    d = request.POST.get("a3")
    em = request.POST.get("a4")
    cn = request.POST.get("a5")
    paa = request.POST.get("a6")
    Facultyreg(fname=na, uname=un, dept=d, email=em, contact=cn, password=paa).save()
    messages.success(request, 'registered success')
    return redirect('Freg')

def flogin(request):
    un = request.POST.get('t1')
    pa = request.POST.get('t2')
    try:
        fn = Facultyreg.objects.get(uname=un,password=pa)
        return render(request, "Fhome.html", {'name': un})
    except Facultyreg.DoesNotExist:
        return render(request, "faclogin.html", {"msg": 'Username or Password is incorrect'})


def fHome(request):
    uname = request.GET.get("un")
    return render(request,"Fhome.html",{'name':uname})

def sessions(request):
    detail = SessionModel.objects.all()
    return render(request,"Views sessions.html",{"detail": detail})

def assignment(request):
    return render(request,"assignment.html")

def saveAssign(request):
    sub = request.POST.get("t1")
    date = request.POST.get("t2")
    assgn = request.FILES["t3"]
    try:
        AssignmentModel(subject=sub,date=date,assign=assgn).save()
        return render(request, "assignment.html", {"msg": 'Submisson Successfully'})
    except AssignmentModel.DoesNotExist:
        return render(request, "assignment.html", {'msg': 'not saved'})

def subAssignments(request):
    data = SubmitAssignment.objects.all()
    return render(request,"Subassignment.html",{"data":data})


#Student
def sreg(request):
    return render(request,"Sreg.html")

def signin(request):
    na = request.POST.get("a1")
    un = request.POST.get("a2")
    d = request.POST.get("a3")
    em = request.POST.get("a4")
    cn = request.POST.get("a5")
    paa = request.POST.get("a6")
    Studentreg(sname=na,uname=un,depart=d,emailid=em,contactno=cn,pwd=paa).save()
    messages.success(request, 'registered success')
    return redirect('Sreg')


def slogin(request):
    un = request.POST.get('a1')
    pa = request.POST.get('a2')
    try:
        sn = Studentreg.objects.get(uname=un, pwd=pa)
        return render(request, "Shome.html", {'name': un})
    except Studentreg.DoesNotExist:
        return render(request, "slogin.html", {"msg": 'Username or Password is incorrect'})


def shome(request):
    uname =request.GET.get("un")
    return render(request,"Shome.html",{"name":uname})


def swelcome(request):
    uname = request.GET.get("un")
    return render(request,"Shome.html",{"name":uname})

def studSessions(request):
    uname = request.GET.get("un")
    detail = SessionModel.objects.all()
    return render(request,"Student Session.html",{"detail": detail,"name":uname})


def assignView(request):
    uname = request.GET.get("un")
    asg = AssignmentModel.objects.all()
    return render(request,"SviewAss.html",{"asg":asg,"name":uname})


def studSubmit(request):
    uname = request.GET.get("un")
    #sno = request.GET.get("Stud")
    stu = Studentreg.objects.get(uname=uname)
    return render(request,"Student Submit.html",{"name":uname , "data":stu})


def saveDB(request):
    sub = request.POST.get("t1")
    file = request.FILES["t3"]
    sno = request.POST.get("a1")
    print(sub)


    try:
        #sno = Studentreg.objects.get(sno=uname)
        SubmitAssignment(Subject=sub,submit=file,student_reg_id=sno).save()
        return render(request, "Student Submit.html",{"msg": 'Submisson Successfully'})
    except SubmitAssignment.DoesNotExist:
        return render(request, "Student Submit.html", {'msg': 'not saved'})




