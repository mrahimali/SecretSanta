from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import CSVUploadForm
from .utils import read_csv, read_previous_assignments, assign_secret_santa, generate_output_csv


class SecretSantaView(View):

    def get(self, request):

        form = CSVUploadForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            employees_file = request.FILES['employees_file']
            previous_file = request.FILES.get('previous_file')

            employees = read_csv(employees_file)
            previous_assignments = read_previous_assignments(previous_file) if previous_file else {}

            assignments = assign_secret_santa(employees, previous_assignments)
            if not assignments:
                return HttpResponse("Error: Could not assign Secret Santa. Try again.", status=400)

            response = HttpResponse(generate_output_csv(assignments), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="secret_santa_assignments.csv"'
            return response

        return render(request, 'index.html', {'form': form})
