# import built in User model
from django.contrib.auth.models import User

def project_context(request):

    context = {
        # turns keys to keywords available to templates
        'me': User.objects.first(),
    }
    return context