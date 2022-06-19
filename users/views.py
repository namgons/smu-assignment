from django.views.generic import DetailView
from . import models


class ProfileView(DetailView):

    model = models.User
    context_object_name = "user_obj"
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ob = context["object"]
        context["reviews"] = ob.reviews.all().order_by("-created")
        return context


""" 
class FavsView(View):
    pass
 """
