from django.shortcuts import render
from invoices.forms import ProjectSelect

# Create your views here.
def project_select(request):
	if request.method == 'POST':
		form = ProjectSelect(data=request.POST, request=request)

	else:
		form = ProjectSelect(request=request)

	return render(request, template_name='invoices/project_select.html', context={'form': form,})