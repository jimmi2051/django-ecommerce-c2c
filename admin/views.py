from django.shortcuts import render

# Create your views here.
def login (request):
    return render(request, 'login/Login.html')
def index(request):
    return render(request,'admin/index.html')
def users(request):
    return render(request,'admin/manager_users/manager_users.html')
def users_add(request):
    return render(request,'admin/manager_users/manager_users_detail.html')
def servies(request):
    return render(request,'admin/manager_servies_post/manager_servies_post.html')
def servies_add(request):
    return render(request,'admin/manager_servies_post/manager_servies_post_detail.html')
def payment(request):
    return render(request,'admin/manager_history_pay/manager_pay.html')
def payment_detail(request):
    return render(request,'admin/manager_history_pay/manager_pay_detail.html')
def post(request):
    return render(request,'admin/manager_posted/manager_post.html')
def post_detail(request):
    return render(request,'admin/manager_posted/manager_post_detail.html')
def ads(request):
    return render(request,'admin/manager_ads/manager_ads.html')
def ads_detail(request):
    return render(request,'admin/manager_ads/manager_ads_detail.html')