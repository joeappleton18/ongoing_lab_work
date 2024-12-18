from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("api.urls")),
    path("admin/", admin.site.urls),
    path("datawizard/", include("data_wizard.urls")),
    path('api-auth/', include('rest_framework.urls'))

]
