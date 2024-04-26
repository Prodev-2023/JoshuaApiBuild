from django.shortcuts import render
import requests

# Create your views here.

# response_to_users = requests.get('https://freetestapi.com/api/v1/students')
# data = response_to_users.json()

response_to_users2 = requests.get('https://freetestapi.com/api/v1/actors')
data2 = response_to_users2.json()




def home(request):
    sliced_data2 = data2[0:10]
    # sliced_data = data[0:3]
    context = {'data2':sliced_data2} 
    return render(request, 'blog/home.html', context)


def about(request):
  
    return render(request, 'blog/about.html')