from django.shortcuts import render,redirect
from luxuaryvillaApp.models import CategoryDb,ProductDb,AgentsDb,ContactDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def indexfun(req):
    return render(req,"index.html")

def addcat_fn(req):
    data = CategoryDb.objects.all()
    return render(req,"addcategory.html",{'data':data})

def Savecategory(req):
    if req.method=="POST":
        cat=req.POST.get('cat_name')
        CatImg=req.FILES['categoryImage']
        catDes=req.POST.get('cat_description')
        loc=req.POST.get('Location')
        obj=CategoryDb(cat_name=cat,categoryImage=CatImg,cat_description=catDes,Location=loc)
        obj.save()
        messages.success(req,"Category saved successfully")
        return redirect(addcat_fn)

def displaycat_fn(req):
    data=CategoryDb.objects.all()
    return render(req,'displaycat.html',{'data':data})

def editcat_fun(req,dataid):
    categorydata=CategoryDb.objects.get(id=dataid)
    return render(req,'editcategory.html',{'categorydata':categorydata})

def updatecat_fn(req,dataid):
    if req.method == "POST":
        cn = req.POST.get('cat_name')

        c_des = req.POST.get('cat_description')
        loc=req.POST.get('Location')
        try:
            cimg = req.FILES['cimage']
            fs = FileSystemStorage()
            file = fs.save(cimg.name, cimg)
        except MultiValueDictKeyError:
            file =CategoryDb.objects.get(id=dataid).categoryImage
        CategoryDb.objects.filter(id=dataid).update(cat_name=cn,categoryImage=file,cat_description=c_des,Location=loc)
        return redirect(displaycat_fn)

def deletecat_fn(req,dataid):
    data=CategoryDb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycat_fn)

def addproduct_fn(req):
    category = CategoryDb.objects.all()
    return render(req, 'addproduct.html', {'category': category})

def saveproduct_fn(req):
    if req.method == 'POST':
        cat_name = req.POST.get('c_name')
        p_name= req.POST.get('Pro_name')
        pimg = req.FILES['ProductImage']
        pri = req.POST.get('Price')
        pdes=req.POST.get('ProDescription')
        obj = ProductDb(c_name=cat_name, Pro_name=p_name, ProductImage=pimg, Price=pri,ProDescription=pdes)
        obj.save()
        messages.success(req,"product saved successfully")

        return redirect(addproduct_fn)

def displayproduct_fun(req):
    product=ProductDb.objects.all()
    return render(req,'displayproduct.html',{'product':product})

def editproductfn(req,dataid):
    productdata=ProductDb.objects.get(id=dataid)
    return render(req,'editProduct.html',{'productdata':productdata})

def updateproduct_fun(req,dataid):
    if req.method == "POST":
        cname=req.POST.get('c_name')
        pname = req.POST.get('pro_name')
        price = req.POST.get('price')
        description=req.POST.get('prodescription')
        try:
            proimage = req.FILES['pro_image']
            fs = FileSystemStorage()
            file = fs.save(proimage.name, proimage)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=dataid).ProductImage
        ProductDb.objects.filter(id=dataid).update(c_name=cname,Pro_name=pname,ProDescription=description, Price =price, ProductImage=file)
        return redirect(displayproduct_fun)

def deleteproduct_fn(req,dataid):
    data=ProductDb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct_fun )

def login_page(request):
    return render(request,"login.html")

def admin_login(request):
        if request.method == "POST":
            uname = request.POST.get('username')
            pwd = request.POST.get('pass')
            if User.objects.filter(username__contains=uname).exists():
                user = authenticate(username=uname, password=pwd)
                if user is not None:
                    login(request, user)

                    messages.success(request, "Login Successfully")
                    request.session['username'] = uname
                    request.session['password'] = pwd
                    return redirect(indexfun)
                else:
                    messages.error(request,"invalid username or password")
                    return redirect(login_page)
            else:
                messages.error(request, "invalid username or password")
                return redirect(login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)

# def Agentadmin_fn(req):
#     return render(req,"DisplayAgent.html")

def addAgent(req):
    data=AgentsDb.objects.all()
    return render(req,"addAgents.html",{'data':data})

def saveAgent_page(req):
    if req.method=="POST":
        ag_na=req.POST.get('Agent_name')
        ag_Id=req.POST.get('Agent_id')
        ag_mob=req.POST.get('Mobile')
        ag_mail=req.POST.get('Email')
        obj=AgentsDb(Agent_name=ag_na,Agent_id=ag_Id,Mobile=ag_mob,Email=ag_mail)
        obj.save()
        messages.success(req,"Agent saved Successfully...!")
        return redirect(addAgent)

def displayAgent_fun(req):
    Agent=AgentsDb.objects.all()
    return render(req,"DisplayAgent.html",{'Agent':Agent})


def editAgent(req,dataid):
    Agent=AgentsDb.objects.get(id=dataid)
    return render(req,'EditAgent.html',{'Agent':Agent})


def updateAgent_fun(req,dataid):
    if req.method == "POST":
        An=req.POST.get('Agent_name')
        Aid = req.POST.get('Agent_id')
        mob = req.POST.get('Mobile')
        mail=req.POST.get('Email')
        AgentsDb.objects.filter(id=dataid).update(Agent_name=An,Agent_id=Aid,Mobile=mob, Email =mail)
        return redirect(displayAgent_fun)

def deleteAgent_fn(req, dataid):
        Agent = AgentsDb.objects.filter(id=dataid)
        Agent.delete()
        return redirect(displayAgent_fun)


def displaycontactfn(req):
    data=ContactDb.objects.all()
    messages.success(req, "message send successfully...!")
    return render(req,"displaycontact.html",{'data':data})






