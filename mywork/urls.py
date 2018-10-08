from django.conf.urls import url, include
from django.contrib import admin
from mywork import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('app/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.login_redirect, name='login_redirect'),
    url(r'^app/',include(('app.urls', 'app'), namespace='app')),
    url(r'^home/',include(('home.urls', 'home'), namespace='home')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#
