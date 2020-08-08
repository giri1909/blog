from django.conf.urls import url

from .views import bloggTest,Hello,Contact,Product,HelloTemplate,ProductStatic,ProductDynamicOneRecord,Products
from .views import BlogData

from .views import Contact,Thanks


from .views import Thanks,StudentInsert

from .views import BlogPost
from .views import Home
urlpatterns = [

    url(r'^hello/',Hello),
    url(r'^contact/',Contact),
    url(r'^product/',Product),
    url(r'^hellotemplate/',HelloTemplate),
    url(r'^productstatic/',ProductStatic),
    url(r'^productdynamic/',ProductDynamicOneRecord),
    url(r'^products/',Products),
	url(r'^blogdata/',BlogData),
	url(r'^bloggtest/',bloggTest),
    url(r'^contact/', Contact, name='contact'),
    url(r'^thanks/',Thanks),
	url(r'^studentinsert/',StudentInsert),
    url(r'^postblog/', BlogPost, name='postblog'),
    url(r'^$', Home, name='home'),
]


