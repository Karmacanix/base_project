from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .forms import AccountDetailsForm
from .models import AccountDetails

# Create your views here.
def home(request):
	return render(request, template_name='home.html')


class AccountDetailsUpdate(UpdateView):
	model = AccountDetails
	form_class = AccountDetailsForm
	template_name = 'account_details.html'

	def get_queryset(self):
		return AccountDetails.objects.get(user__id=self.kwargs['pk'])