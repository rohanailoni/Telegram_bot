from django.shortcuts import render
from app.models import Document,user
from django.http import HttpResponseRedirect
from app.forms import DocumentForm
# Create your views here.
import uuid
import hashlib
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

from django.template import RequestContext, context
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
def hashText(text):
    
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + text.encode()).hexdigest() + ':' + salt
    
def matchHashedText(hashedText, providedText):
   
    _hashedText, salt = hashedText.split(':')
    return _hashedText == hashlib.sha256(salt.encode() + providedText.encode()).hexdigest()
def user_handle(request):

    return render(request,"login.html",)
# def login_auth(user1,password):
#     obj=user.objects.get(userid=user1)
#     if(matchHashedText(obj.password,password)):
#         return True
#     else:
#         return False


# def login_handle(request):
#     id=request.POST.get('userid')
#     password=request.POST.get('epassword')
#     if login_auth(id,password):

#         return render(request,"succ.html")
#     else:
#         return HttpResponseRedirect('/login')

# def register_handle(request):
#     id=request.POST.get('user')
#     password=request.POST.get('password')
#     email=request.POST.get('email')
#     #print(id,email,password)
#     password=hashText(password)
#     m=user(userid=id,email_id=email,password=password,member="student")
#     m.save()
    
#     return render(request,'succ.html')


def login_auth2(request):
    id=request.POST.get('userid')
    password=request.POST.get('epassword')
    user_auth=authenticate(username=id,password=password)
    #print(user_auth,id,password)
    if user_auth is not None:
        #return render(request,"succ.html",{"user":id})
        login(request,user_auth)
        print("i am inside loop")
        user1=User.objects.get(username=id)
        user2=user.objects.get(userid=user1)
        print(user2.member)
        if(user2.member=="student"):
            Doc=Document.objects.all()
            context={"documents":Doc}
            return render(request,"download.html",context)
        return HttpResponseRedirect("/list")
    else:
        return HttpResponseRedirect("/")


def register_auth2(request):
    id=request.POST.get('user')
    password=request.POST.get('password')
    email=request.POST.get('email')
    user8=User.objects.create_user(username=id,password=password,email=email)
    
    user1=user(userid=user8,member="student")
    user1.save()
    return render(request,"hype.html")



def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            user_fech=request.user
            if user_fech.is_authenticated==False:
                return HttpResponseRedirect("/login")
            newdoc = Document(user_acess=user_fech,docfile = request.FILES['docfile'])
            newdoc.save()

            
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.filter(user_acess=request.user)

    # Render list page with the documents and the form
    return render(request,'succ.html',{'documents': documents, 'form': form})