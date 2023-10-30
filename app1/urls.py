from django.urls import path
from. import views

urlpatterns = [
    path('',views.home, name="home"),
    path('superuser',views.superuser, name="superuser"),

    path('loginPage',views.loginPage, name="loginPage"),
    path('login',views.login, name="login"),
    path('register',views.register, name="register"),
    path('create',views.create, name="create"),

    path('updatePage/<id>',views.updatePage, name="updatePage"),
    path('updated',views.updated, name="updated"),
    
    path('delete/<id>',views.delete, name="delete"),
    path('cancel',views.cancel, name="cancel"),


    # post
    
    path('posts',views.postsPage, name="posts"),
    path('userPostsPage',views.userPostsPage, name="userPostsPage"),
    path('newPost',views.newPost, name="newPost"),
    path('updatePost',views.updatePost, name="updatePost"),
    path('delePost',views.delePost, name="delePost"),


    #comments
    path('updateComment',views.updateComment, name="updateComment"),



    path('chats',views.chatsPage, name="chatsPage"),
    path('sms/<fri_email>',views.smsPage, name="sms"),
    path('newsms',views.newSms, name="newsms"),
    # path('deleteuser/<int:userID>',views.deleteUser, name="home"),
]