from django.shortcuts import render

# Create your views here.
def reviews(request):
    """ Return homepage """
    return render(request, 'reviews/reviews.html')