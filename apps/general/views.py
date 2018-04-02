from django.shortcuts import render

# Create your views here.

def index_view(request):
	return render(request, 'views/index.html')

def conocenos_index_view(request):
	return render(request, 'views/conocenosIndex.html')
