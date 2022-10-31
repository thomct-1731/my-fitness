from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import *
from .forms import *
from .decorators import *
from .helpers import *
from .filters import *

# Create your views here.
def home(request):
    foods = Food.objects.filter().order_by('-pk')
    myfilter = FoodFilter(request.GET, queryset=foods)
    foods = myfilter.qs

    paginator = Paginator(foods, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={'myfilter': myfilter, 'page_obj': page_obj, 'cnt': foods.count()}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def addFood(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Create new food successfully!')
            return redirect('home')
    form = FoodForm()
    context={'form': form}
    return render(request, 'foods/foodForm.html', context)

@login_required(login_url='login')
def updateFood(request, id):
    try:
        food = Food.objects.get(pk = id)
    except Food.DoesNotExist:
        return redirect('home')
    if request.method=="POST":
        form = FoodForm(request.POST, instance = food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update food successfully!')
            return redirect('home')
    form = FoodForm(instance = food)
    context={'form': form, 'food': food}
    return render(request, 'foods/foodForm.html', context)

@login_required(login_url='login')
def deleteFood(request, id):
    try:
        food = Food.objects.get(pk = id)
    except Food.DoesNotExist:
        return redirect('home')
    food.delete()
    messages.success(request, 'Delete food successfully!')
    return redirect('home')

@login_required(login_url='login')
def profile(request):
    try:
        profile = UserProfile.objects.get(user_id = request.user.id)
    except UserProfile.DoesNotExist:
        return redirect('createProfile')
    bmr_base = round((10*profile.weight) + (6.25*profile.height) - (5*profile.age))
    bmr = bmr_base + 5 if profile.gender == 'Male' else bmr_base - 161
    calories_day = round(bmr*profile.activity.score)
    calories_day_format = '{:,}'.format(calories_day)
    calories_week = calories_day*7
    activities = []
    for act in Activity.objects.all():
        activities.append({
            'id': act.id,
            'name': act.name,
            'calories': '{:,}'.format(round(bmr*act.score)),
        })
    max_h = profile.height if profile.height < 100 else profile.height - 100
    min_h = round(max_h*0.8)
    bmi = round((profile.weight*10000)/(profile.height*profile.height), 2)
    cutting_calories = calories_day - 500
    cutting_calories_format = '{:,}'.format(cutting_calories)
    bulking_calories = calories_day + 500
    bulking_calories_format = '{:,}'.format(bulking_calories)
    context = {
        'profile': profile,
        'calories': {
            'day': calories_day_format,
            'week': '{:,}'.format(calories_week),
        },
        'bmr': '{:,}'.format(bmr),
        'activities': activities,
        'weight': {'max':  max_h, 'min': min_h},
        'bmi': bmi,
        'bmi_scores': [
            {'name': 'Underweight', 'score': '< 18.5', 'valid': bmi < 18.5},
            {'name': 'Normal Weight', 'score': '18.5 – 24.99', 'valid': 18.5 <= bmi<=  24.99},
            {'name': 'Overweight', 'score': '25 – 29.99', 'valid': 25 <= bmi <= 29.99},
            {'name': 'Obese', 'score': '30+', 'valid': bmi > 30},
        ],
        'macros': [
            {
                'name': 'maintenance',
                'intro': f'These macronutrient values reflect your maintenance calories of <strong>{calories_day_format}</strong> calories per day.',
                'data': getMacrosData(calories_day),
            },
            {
                'name': 'cutting',
                'intro': f'These macronutrient values reflect your cutting calories of <strong>{cutting_calories_format}</strong> calories per day, which is a <strong>500</strong> calorie per day deficit from your maintenance of <strong>{calories_day_format}</strong> calories per day.',
                'data': getMacrosData(cutting_calories),
            },
            {
                'name': 'bulking',
                'intro': f'These macronutrient values reflect your bulking calories of <strong>{bulking_calories_format}</strong> calories per day, which is <strong>+500</strong> calories per day from your maintenance of <strong>{calories_day_format}</strong> calories per day.',
                'data': getMacrosData(bulking_calories),
            }
        ]
    }
    return render(request, 'profile/profile.html', context)

@login_required(login_url='login')
def createProfile(request):
    user=request.user
    try:
        UserProfile.objects.get(user_id = user.id)
        return redirect('profile')
    except UserProfile.DoesNotExist:
        pass
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.user = user
            form.save()
            return redirect('profile')
    form = UserProfileForm()
    context={'form': form}
    return render(request, 'profile/userProfileForm.html', context)


@login_required(login_url='login')
def updateProfile(request, id):
    try:
        profile = UserProfile.objects.get(pk = id)
    except UserProfile.DoesNotExist:
        return redirect('createProfile')
    if request.method=="POST":
        form = UserProfileForm(request.POST, instance = profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update profile successfully!')
            return redirect('profile')
    form = UserProfileForm(instance = profile)
    context = {'form': form, 'profile_id': profile.pk}
    return render(request, 'profile/userProfileForm.html', context)

@login_required(login_url='login')
def deleteProfile(request, id):
    try:
        profile = UserProfile.objects.get(pk = id)
    except UserProfile.DoesNotExist:
        return redirect('home')
    profile.delete()
    return redirect('home')

@unauthorized_user
def registerUser(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            form.cleaned_data.get('email')
            messages.success(request, 'Account created for '+username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

@unauthorized_user
def loginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is invalid!')
    return render(request,'login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
