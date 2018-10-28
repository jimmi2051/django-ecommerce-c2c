from django.shortcuts import render, redirect

# 0 Admin, 1 Customer, 2 Merchant, 3 Advertiser

def check_rule(request):
    if 'user' in request.session:
        user = request.session.get('user')
        print(user['role'])
        if 0 in user['role']:
            print(user)
            return 1
        return 0
    return 0

# Create your views here.
def login (request):
    if check_rule(request) == 1:
        return redirect('/admin/index')
    return render(request,'login/Login.html')

def index(request):
    if check_rule(request) == 0:
        return redirect('/admin/login')
    return render(request,'admin/index.html')
    
def users(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_users/manager_users.html')

def users_add(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_users/manager_users_detail.html')

def servies(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_servies_post/manager_servies_post.html')

def servies_add(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_servies_post/manager_servies_post_detail.html')

def payment(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_history_pay/manager_pay.html')
    
def payment_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_history_pay/manager_pay_detail.html')

def post(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_posted/manager_post.html')

def post_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_posted/manager_post_detail.html')

def ads(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_ads/manager_ads.html')
    
def ads_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_ads/manager_ads_detail.html')

def ads_register(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_ads/manager_ads_register.html')

def ads_register_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_ads/manager_ads_register_detail.html')
    
def products(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/manager_product.html')

def products_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/manager_product_detail.html')

def categories(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/manager_category.html')

def category_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/manager_category_detail.html')
