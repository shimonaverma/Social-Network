from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from .  import views
from django.contrib.auth.views import (
    login , logout , password_reset ,
     password_reset_done,password_reset_confirm ,password_reset_complete
)

urlpatterns = [
    # url(r'^$', views.home_page , name='home_page'),
    url(r'^login/$',login,{'template_name':'app/login.html'},name='login'),
    url(r'^logout/$',logout,{'template_name':'app/logout.html'},name='logout'),
    # url(r'^app/$', views.home_page,name='home_page'),
    url(r'^SignUp/$',views.SignUp,name='SignUp'),
    url(r'^profile/$', views.profile ,name='profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile ,name='profile_with_pk'),

    url(r'^profile/edit-profile/$',views.edit_profile,name='edit_profile'),
    url(r'^change-password/$', views.change_password ,name='password'),

    url(r'^reset-password/$' , password_reset,{'template_name':'app/reset_password.html',
    'post_reset_redirect':'app:password_reset_done','email_template_name':'app/reset_password_email.html'},  name="reset_password"),

    url(r'^reset-password/done/$', password_reset_done,{'template_name': 'app/reset_password_done.html'}, name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm ,{'template_name':'app/reset_password_confirm.html',
    'post_reset_redirect':'app:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset_password/complete/$' ,password_reset_complete , {'template_name':'app/reset_password_complete.html'},name='password_reset_complete')
]


# {'template_name':'app/reset_password.html',
# 'post_reset_redirect':'app:reset_password_done.html',
# 'email_template_name':'app/reset_password_email.html'},
# ,{'template_name':'app/reset_password_done.html'}
# 'email_template_name':'app/reset_password_email.html'
