from django.conf.urls import url, include

urlpatterns = [
    url(r"^", include("pinax.referrals.urls")),
]
