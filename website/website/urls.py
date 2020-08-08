from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls import url


urlpatterns = [

	url(r'^admin/', admin.site.urls),
    url(r'^blog/',include('blogg.urls')),
    url(r'^test/',include('testapp.urls')),

]
