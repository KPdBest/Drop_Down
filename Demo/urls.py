from django.contrib import admin
from django.conf.urls import url , include
from Select import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^data/', include('Select.urls'))

]