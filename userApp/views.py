from django.shortcuts import render,redirect
from luxuaryvillaApp.models import CategoryDb,ProductDb,AgentsDb,ContactDb,feedbackDb
from userApp.models import UserRegistrationDb
from userApp.models import bookslot,payment
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from luxuaryvillaApp.models import feedbackDb
# Create your views here.
def homepage_fn(req):
    data=CategoryDb.objects.all()
    # messages.success(req, "slot booked successfully...!")

    return render(req,"home.html",{'data':data})

def about_fn(req):
    return render(req,"about.html")

def contact_fn(req):
    return render(req,"Contact.html")

def Product_fn(req,cat_name):
    data = CategoryDb.objects.all()
    pro = ProductDb.objects.filter(c_name=cat_name)
    return render(req,"ProductPage.html",{'data':data,'pro':pro})


def Service(request):
    return render(request, "ServicePage.html")

def registerform_fun(req):
    return render(req,"registrationform.html")

def agent_fn(req):
    data=AgentsDb.objects.all()
    return render(req,"Agents.html",{'data':data})

def saveAgents(req):
    if req.method=="POST":
        an=req.POST.get('agent_name')
        a_id=req.POST.get('agent_id')
        a_mob=req.POST.get('agent_mob')
        a_mail=req.POST.get('agent_email')
        obj=AgentsDb(Agent_name=an,Agent_id=a_id,Mobile=a_mob,Email=a_mail)
        obj.save()
        return redirect(agent_fn)

def SaveRegister(req):

        if req.method == "POST":

            un = req.POST.get('username')
            uem = req.POST.get('email')
            upwd = req.POST.get('pass')
            umob = req.POST.get('mobile')
            # ui = req.FILES['pic']
            obj = UserRegistrationDb(uname=un,uemail=uem,upass=upwd,umob=umob)
            obj.save()
            messages.success(req, "successfully logout")

            return redirect(registerform_fun)

def Signin_fn(req):
    if req.method == 'POST':
        un = req.POST.get('username')
        upwd = req.POST.get('password')
        if UserRegistrationDb.objects.filter(uname=un, upass=upwd).exists():
            req.session['username']=un
            req.session['password']=upwd
            messages.success(req,'User Login Successfully')
            req.session['username'] = un
            req.session['password'] = upwd
            return redirect(homepage_fn)
        else:
            messages.error(req,'Invalid User')
            return redirect(registerform_fun)
    return redirect(registerform_fun)

def UserLogout_fn(req):
    del req.session['username']
    del req.session['password']
    messages.success(req,"successfully logout")
    return redirect(registerform_fun)

def bookingPage(req):
    return render(req,"bookingPage.html")

def Savebooking(req):
    if req.method=="POST":
        fn=req.POST.get('fname')
        ln=req.POST.get('lname')
        eml=req.POST.get('email')
        tk=req.POST.get('token')
        obj=bookslot(fname=fn,lname=ln,email=eml,token=tk)
        obj.save()
        messages.success(req, "slot booking successfully...!")
    return redirect(Payment_page)


def Payment_page(request):
    return render(request, "paymentPage.html")

def savepayment(req):
    if req.method=="POST":
        cn=req.POST.get('cardnumber')
        na=req.POST.get('name')
        cnn=req.POST.get('cardnum')
        exp=req.POST.get('expire')
        cv=req.POST.get('cvv')
        obj=payment(cardnum=cn,name=na,cardnumber=cnn,expire=exp,cvv=cv)
        obj.save()
        messages.success(req, "payment successfully...!")
    return redirect(homepage_fn)


def singleproduct_fn(req,dataid):
    prod =ProductDb.objects.get(id=dataid)

    return render(req,"singleProduct.html",{'prod':prod})

def feedback_fn(req):
    messages.success(req, "Thank You for Your feedback...!")

    return render(req,"feedback.html")


def Savefeedback(req):
    if req.method=="POST":
        na=req.POST.get('Name')
        em=req.POST.get('Email')
        sub=req.POST.get('Subject')
        msg=req.POST.get('Message')
        obj=feedbackDb(name=na,email=em, subject=sub,message=msg)
        obj.save()
        messages.success(req, "feedback send successfully...!")
    return redirect(homepage_fn)


def SaveContact(req):
    if req.method=="POST":
        na=req.POST.get('Name')
        em=req.POST.get('Email')
        sub=req.POST.get('Subject')
        msg=req.POST.get('Message')
        obj=ContactDb(name=na,email=em, subject=sub,message=msg)
        obj.save()
        messages.success(req, "message send successfully...!")
    return redirect(contact_fn)




def search(request):
    if request.method=="GET":
        search=request.GET.get('q')
        cat=CategoryDb.objects.filter(cat_name__icontains=search)
        pro=ProductDb.objects.filter(Pro_name__icontains=search)
        return render(request,"search.html",{'cat':cat,'pro':pro})

# def admin_login(request):
#             if request.method == "POST":
#                 uname = request.POST.get('username')
#                 pwd = request.POST.get('pass')
#                 if User.objects.filter(username__contains=uname).exists():
#                     user = authenticate(username=uname, password=pwd)
#                     if user is not None:
#                         login(request, user)
#
#                         messages.success(request, "Login Successfully")
#                         request.session['username'] = uname
#                         request.session['password'] = pwd
#                         return redirect(indexfun)
#                     else:
#                         messages.error(request, "invalid username or password")
#                         return redirect(login_page)
#                 else:
#                     messages.error(request, "invalid username or password")
#                     return redirect(login_page)
#
#     def admin_logout(request):
#         del request.session['username']
#         del request.session['password']
#         return redirect(login_page)

#
def user_logout(request):
    logout(request)
    return homepage_fn(request)
