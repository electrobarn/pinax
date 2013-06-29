from django.conf.urls.defaults import *
from django.views.generic import TemplateView


urlpatterns = patterns("",
    url(r"^list_signup/$", "pinax.apps.waitinglist.views.list_signup", name="waitinglist_list_signup"),
    url(r"^success/$", TemplateView.as_view(template_name="waitinglist/success.html"), name="waitinglist_success"),
)
