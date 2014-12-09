from apps.core.forms import LoginForm

def loginFormToContext(request, context):
    if not request.user.is_authenticated():
        form = LoginForm()
        context['login_form'] = form
    return context
