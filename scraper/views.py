# scraper/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .forms import URLForm
from .scraping import scrape_website

def index(request):
    form = URLForm()
    return render(request, 'scraper/index.html', {'form': form})

# def scrape(request):
#     if request.method == 'POST':
#         form = URLForm(request.POST)
#         if form.is_valid():
#             url = form.cleaned_data['url']
#             data = scrape_website(url)
#             return JsonResponse(data)
#     return JsonResponse({'error': 'Invalid request'}, status=400)

# views.py
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def scrape(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            data = scrape_website(url)
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Invalid URL'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
