from django.http import HttpResponse ,  JsonResponse



def home_page(request):
    print("Home page requested")
    
    friends = ["harry", "hitesh", "harsh"]
    return JsonResponse ({'friends': friends})
    