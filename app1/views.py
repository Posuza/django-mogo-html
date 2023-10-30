from django.shortcuts import render,redirect
from django.http import HttpResponse
from. import dbModel
import random
import pymongo


connection = pymongo.MongoClient('localhost',27017)
db = connection["ncc_dip2"]

#userdbUsers
dbUsers = db["user"]

#AdmindbUsers
admin = db["admin"]

#Dbposts
dbPosts = db["posts"]

#Dbcomments
dbComments = db["comments"]

#Dbcomments
dbsms = db["sms"]

largerID = 0
updateEmail =''
emailExit = False
nameExit = False
nullValue =False
inName = False
inEmail = False
inPhone = False
inPass = False
valiBio= False

#loginUser for userPostPage,chatsPage
user ={}

#usersfor chat and user mangement,postPage
users={}

##########    user

def home(request):
    global largerID,users
    users ={}
    context={}
    # for i in col.find({},{'_id':0}):
    for i in dbUsers.find():
        id,username,email,password,phone,info = i["_id"],i["username"],i["email"],i["password"],i["phone"],i["info"]
        dataform={id:{"name":username,"email":email,"password":password,"phone":phone,"info":info}}  
        users.update(dataform)
        largerID = max(0,id)
    
    context ={"datas":users}
    return render(request,'index.html',context)

#login

def loginPage(request):
     return render(request,'login.html')

def login(request):
    global user
    user={}
    if request.method == 'POST':
        loginEmail = request.POST.get("email")
        loginPassword = request.POST.get("password")

        print(loginEmail,loginPassword)

        for i in dbUsers.find():
            id,username,email,password,phone,info = i["_id"],i["username"],i["email"],i["password"],i["phone"],i["info"]
            if loginEmail == email and loginPassword == password:
                # print(loginEmail,email,loginPassword,password)
                user={"id":id,"name":username,"email":email,"password":password,"phone":phone,"info":info}  
                # user.update(dataform)

                return redirect(postsPage)

    return redirect(loginPage)

def register(request):
    context ={}
    errors={
            "nameError":"Invalid Username!",
            "emailError":"Invalid Email!",
            "phoneError":"Invalid phone",
            "passwordError":"Invalid Password",
                 }

    if nullValue == True:
        context ={"nameError":"Invalid Username!",
                "emailError":"Invalid Email!",
                "phoneError":"Invalid phone",
            "passwordError":"Invalid Password"}
        return render(request,'register.html',context)

    if emailExit == True:
        print("emailexit1")
        context={"emailError":"Email already take! place chose another"}
        return render(request,'register.html',context)
    
    elif nameExit == True:
        print("nameExitone")
        context={"nameError":"Name already take! plz chose another"}
        return render(request,'register.html',context)

    return render(request,'register.html',context)

def create(request):
    global emailExit,nameExit,nullValue,inName,inEmail,inPass,inPhone
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        if username and email and phone and password:
            dbEmail = dbUsers.find_one({"email":email}) 
            dbUsername = dbUsers.find_one({"username":username}) 
            if dbEmail !=None:
                print("emailExit")
                emailExit = True
                return redirect(register)
            
            elif dbUsername !=None :
                print("namExit")
                nameExit = True
                return redirect(register)

            else:
                id =largerID+1
                print(id)
                print(id,username,email,phone,password)

                info:str = "User data is Win"+str(id)+"id : "+str(id)

                data_form = {"_id": id, "username": username, "email": email, "password": password, "phone": phone,"info":info}

                ids = dbUsers.insert_one(data_form)
                print("inserted id :", ids.inserted_id)
                return redirect(home)
        else:
             
            # if username == '':   
            #     inName = True  
            
            nullValue = True
            return redirect(register)

#upadate Section
def updatePage(request,id):
    global updateEmail
    
    context = {}
    col = dbUsers.find_one({"_id":int(id)}) 
    context = {'data':col}
    print(col["email"])
    updateEmail = col["email"]
    return render(request,'update.html',context)

def updated(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        info = request.POST.get("bio")
        

        print(updateEmail)
        print(username,email,phone,password,info)
     
        dbUsers.update_one({"email":updateEmail},{"$set":{"username":username,"email":email,"phone":phone,"password":password,"info":info},})

    return redirect(home)


def delete(request,id):
    dbUsers.delete_one({"_id":int(id)}) 
    return redirect(home)

def cancel(request):
    global nullValue
    nullValue = False
    return redirect(home)


#Super Users
def superuser():
    pass


#############   POST Section

#PostPage
def postsPage(request):

    posts ={}
    comments = {}
    context={}

    for i in dbPosts.find():
        id,post,owner = i["_id"],i["post"],i["owner"]
        dataform={id:{"post":post,"owner":owner}}  
        posts.update(dataform)

    for i in dbComments.find():
        id,post_id,comment,com_email = i["_id"],i["post_id"],i["comment"],i["com_email"]
        dataform={id:{"post_id":post_id,"comment":comment,"com_email":com_email}}  
        comments.update(dataform)

    print(user)

    context ={"datas":posts,
              "comments":comments,
              "user":user,
               "postOwner":users
              }
    return render(request,'post.html',context)

#userPostPage
def userPostsPage(request):
    posts ={}
    comments = {}
    context={}

    for i in dbPosts.find():
        id,post,owner = i["_id"],i["post"],i["owner"]
        dataform={id:{"post":post,"owner":owner}}  
        posts.update(dataform)

    for i in dbComments.find():
        id,post_id,comment,com_email = i["_id"],i["post_id"],i["comment"],i["com_email"]
        dataform={id:{"post_id":post_id,"comment":comment,"com_email":com_email}}  
        comments.update(dataform)
    print(user)
    context ={"datas":posts,
              "comments":comments,
              "user":user
              }
    return render(request,'user_post.html',context)

def newPost(request):
    if request.method == 'POST':
        owner = request.POST.get("owner")
        newpost = request.POST.get("newpost")

        print(newpost)
        if newpost and owner:
            id = random.randint(10, 10000)
            data_form = {"_id": id,"post":newpost, "owner": owner}

            ids = dbPosts.insert_one(data_form)
            print("inserted id :", ids.inserted_id)

    return redirect(postsPage)


def updatePost(request):
    if request.method == 'POST':
        postId = request.POST.get("updateId")
        owner = request.POST.get("owner")
        updateValue = request.POST.get("updateValue")

        
        if postId and owner and updateValue:
            print("if",postId,owner,updateValue)
            dbPosts.update_one({"_id":int(postId)},{"$set":{"post":updateValue},})
            
    return redirect(postsPage)
        

def delePost(request):
    if request.method == 'POST':
        postId = request.POST.get("postId")
        owner = request.POST.get("owner")
        if postId and owner:
            print("deletePost")
            dbPosts.delete_one({"_id":int(postId)}) 
    return redirect(postsPage)




############  Comment Section


def updateComment(request):
    context = {}
    if request.method == 'POST':
        owner = request.POST.get("owner")
        comment = request.POST.get("comment")
        postId = request.POST.get("postId")
        comEmail = request.POST.get("comEmail")

        print(comment,postId,comEmail)
        if comment and postId and comEmail:
            id = random.randint(10, 10000)
            data_form = {"_id": id, "post_id":int(postId), "comment": comment,"com_email": comEmail}

            ids = dbComments.insert_one(data_form)
            print("inserted id :", ids.inserted_id)
        
        if owner:
            return redirect(userPostsPage)

    return redirect(postsPage)



######### Chats Section

def chatsPage(request):
    
    context ={"users":users,
              "owner":user
            }

    return render(request,'chats.html',context)


def smsPage(request,fri_email):

    messages = {}
    context={}

    for i in dbsms.find():
        id,message,sender,reciver = i["_id"],i["message"],i["sender"],i["reciver"]

        # print(user["email"])
        if sender == user["email"] or reciver == user["email"]:
            dataform={id:{"message":message,"sender":sender,"reciver":reciver}}  
            messages.update(dataform)
            
    context ={
              "messages":messages,
              "user":user,
              "friendEmail":fri_email
            }
    return render(request,"sms.html",context)


def newSms(request):
    message = request.POST.get("message")
    sender = request.POST.get("sender")
    reciver = request.POST.get("reciver")


    print(message,sender,reciver)
    if message and sender and reciver:
        id = random.randint(10, 10000)
        data_form = {"_id": id, "message":message, "sender": sender,"reciver": reciver}

        ids = dbsms.insert_one(data_form)
        print("inserted id :", ids.inserted_id)

    return redirect(smsPage,fri_email = reciver)

