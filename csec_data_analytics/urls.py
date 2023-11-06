"""
URL configuration for csec_data_analytics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from csec_data_analytics_app.views.views_vulnerability import VulnerabilityList, VulnerabilityDetail


router = DefaultRouter()
router.register(r'vulnerabilities', CVEItemViewSet)

urlpatterns = [
    path('vulnerability/', vulnerabilitylist.as_view(), name='vulnerability_list'),
    path('vulnerability/<int:pk>/', VulnerabilityDetail.as_view(), name='vulnerability-detail')
]


