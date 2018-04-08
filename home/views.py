from django.shortcuts import render
from django.views.generic import DetailView
from .models import UserInvoiceProfile

# Create your views here.
class UserInvoiceProfileDetail(DetailView):
    model = UserInvoiceProfile

# Create your views here.
def home(request):
	return render(request, template_name='home.html')