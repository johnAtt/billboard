from django.shortcuts import render, HttpResponseRedirect
from .models import Quote
from django.views.decorators.csrf import csrf_protect
import time
@csrf_protect
def index(request):
    date_post = time.strftime("%Y/%m/%d")
    title = request.POST.get("title")
    description = request.POST.get("description")
    author = request.POST.get("author")
    if title and description and author:
        my_quote = Quote(title=title, description=description, author=author)
        my_quote.save()
        return HttpResponseRedirect("/")
    all_quotes = Quote.objects.all()
    context = {
        "all_quotes": all_quotes,
        "date_post" : date_post,
    }
    return render(request, 'billboard/index.html', context)

