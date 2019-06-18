from django.shortcuts import redirect

# Create your views here.
def index_redirect(request):
    return redirect('/myapp/')
