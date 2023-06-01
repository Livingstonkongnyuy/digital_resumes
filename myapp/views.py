from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import *
from django.contrib.auth.models import User, auth
from myapp.forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

#user authentification
def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('signup')
    else:
        form = UserSignupForm()

    context={
        'form' : form
    }

    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')


        user = auth.authenticate(username=username, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Credentials not satisfied')
            return redirect('login')
    else:
        return render(request,'login.html')
    

def signout(request):
    auth.logout(request)
    return redirect('/')
    return render(request, 'signout.html')


# def UserProfileForm(request):



def index(request):
    user_profile = UserProfile.objects.filter().first()
    blog = Blog.objects.order_by('-date_created')[:2]
    certificates = Certificate.objects.order_by('-date_issued')[:2]
    service = Services.objects.order_by('-date_created')[:2]
    portfolio = Portfolio.objects.order_by('-date_created')[:2]
    testimonies = Testimonies.objects.all()

    context = {
        'blog' : blog,
        'certificates' : certificates,
        'user_profile' : user_profile,
        'testimonies' : testimonies,
        'portfolio' : portfolio,
        'service' : service


    }
    return render(request, 'index.html', context)


def add_profile(request):
    if request.method == 'POST':
        form = Add_profileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Add_profileForm()

    context={
        'form' : form
    }
    return render(request, 'add_profile.html', context)

def update_profile(request):
    editProfile = Blog.objects.all()
    if request.method == 'POST':
        form = Add_profileForm(request.POST or None, request.FILES or None, instance = editProfile)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Add_profileForm(instance = editProfile)
    
    context={
        'form' : form,
        'editProfile' : editProfile
    }
    return render(request, 'update_profile.html', context)


def blog(request):
    blog = Blog.objects.all()

    context={
        'blog' : blog
    }
    return render(request, 'blogs/blog.html', context)
def add_blog(request):
    form = BlogForm()  # define form variable here
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    context={
        'blog_add' : form
    }
    return render(request, 'blogs/add_blog.html', context)

def update_blog(request, pk):
    blog = Blog.objects.get(id = pk)

    form = BlogForm(instance = blog)
    if request.method == 'POST':
        form = BlogForm(request.POST or None, request.FILES or None, instance = blog)
        if form.is_valid():
            form.save()
            return redirect('blog')
        
        
    context={
        'form' : form
       }
    return render(request,'blogs/update_blog.html', context)

def blog_detail(request, pk):
    blog = Blog.objects.get(id = pk)

    context={
        'blog' : blog
    }
    return render(request,'blogs/blog_detail.html', context)


def delete_blog(request, pk):
    blog_delete = Blog.objects.get(id = pk)
    blog_delete.delete()

    return redirect('blog')

    context={
        'blog_delete' : blog_delete
    }
    return render(request, 'delete_blog.html', context)


def testimonies(request):
    return render(request, 'testimoniess/testimonies.html')

def view_testimonies(request):
    testimonies = Testimonies.objects.all()

    context={
        'testimonies' : testimonies
    }
    return render(request, 'testimoniess/view_testimonies.html', context)

def create_testimonie(request):
    if request.method == 'POST':
        form = TestimoniesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_testimonies')
    else:
        form = TestimoniesForm()
        
    context={
        'form' : form
    }

    return render(request, 'testimoniess/create_testimonie.html', context)

def delete_testimonie(request, name):
    delete_user_testimonie = Testimonies.objects.get(id=name)
    delete_user_testimonie.delete()
    return redirect('view_testimonies')

def update_testimonie(request, name):
    testimonie = Testimonies.objects.get(id = name)
    if request.method == 'POST':
        form = TestimoniesForm(request.POST or None, request.FILES or None, instance = testimonie)
        if form.is_valid():
            form.save()
            return redirect('view_testimonies')
    else:
        form = TestimoniesForm(instance = testimonie)

    context={
        'testimonie' : testimonie,
        'form' : form
    }
    return render(request, 'testimoniess/update_testimonie.html', context)


def certificates(request):
    certificates = Certificate.objects.all()

    context={
        'certificates' : certificates
    }
    return render(request, 'certificates/certificates.html', context)


def add_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CertificateForm()
    
    context={
        'form' : form
    }
    return render(request, 'certificates/add_certificate.html', context)

def certificate_details(request, pk):
    certificate = Certificate.objects.get( id = pk)

    context={
        'certificate' : certificate
    }
    return render(request, 'certificates/certificate_details.html', context)

def certificate_update(request, pk):
    certificate = Certificate.objects.get(id = pk)
    if request.method == 'POST':
        form = CertificateForm(request.POST or None, request.FILES or None, instance = certificate)
        if form.is_valid():
            form.save()
            return redirect('certificates')
    
    else:
        form = CertificateForm(instance = certificate)

    context={
        'form' : form 
    }
    return render(request, 'certificates/certificate_update.html', context)

def certificate_delete(request, pk):
    certificate = Certificate.objects.get(id = pk)
    certificate.delete()
    return redirect('certificates')


def portfolio(request):
    portfolio = Portfolio.objects.all()

    context={
        'portfolio' : portfolio,
    }
    return render(request, 'portfolio/portfolio.html', context)

def add_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = PortfolioForm()

    context={
        'form' : form
    }
    return render(request, 'portfolio/add_portfolio.html', context)

def delete_portfolio(request, pk):
    portfolio = Portfolio.objects.get(id = pk)
    portfolio.delete()
    return redirect('portfolio')

def update_portfolio(request, pk):
    blog_update = Portfolio.objects.get(id = pk)

    if request.method == 'POST':
        form_update = PortfolioForm(request.POST or None, request.FILES or None, instance =blog_update)
        if form_update.is_valid():
            form_update.save()
            return redirect('portfolio')
    else:
        form_update = PortfolioForm(instance = blog_update)
    
    context={
        'form_update' : form_update
    }
    return render(request, 'portfolio/update_portfolio.html', context)

def portfolio_detail(request, pk):
    port_detail = Portfolio.objects.get(id = pk)

    context={
        'port_detail' : port_detail
    }
    return render(request, 'portfolio/portfolio_detail.html', context)


def resume(request):
    return render(request, 'resume.html')

def services(request):
    services = Services.objects.all()

    context={
        'services' : services
    }
    return render(request, 'services/services.html', context)

def add_service(request):
    if request.method == 'POST':
        form = ServicesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = ServicesForm()
    
    context={
        'form' : form
    }
    return render(request, 'services/add_service.html', context)

def update_service(request, pk):
    service = Services.objects.get(id = pk)

    if request.method == 'POST':
        form_update = ServicesForm(request.POST or None, request.FILES or None, instance = service)
        if form_update.is_valid():
            form_update.save()
            return redirect('services')
    else:
        form_update = ServicesForm(instance = service)
    
    context={
        'form_update' : form_update
    }
    return render(request, 'services/update_service.html', context)


def delete_service(request, pk):
    service = Services.objects.get(id = pk)
    service.delete()
    return redirect('services')


def services_content(request, pk):
    services = Services.objects.get(id = pk)

    context={
        'services' : services
    }
    return render(request, 'services/services_details.html', context)






# def contact(request):
    # if request.method == 'POST':
        # form = ContactForm(request.POST)
        # if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
# 
            # send_mail(
                # f'New message from {name}',
                # f'Name: {name}\nEmail: {email}\n\nMessage: {message}',
                # email,
                # [settings.DEFAULT_FROM_EMAIL],
                # fail_silently=False,
                    # )
            # return render(request, 'contact.html')
                # 
# 
            # form.save()
            # return redirect('contact')
    # else:  
        # form = ContactForm()
# 
    # context={
        # 'form' : form 
    # }
    # return render(request, 'contact/contact.html', context)
# 

def contact(request):
    contact = Contact.objects.filter().first()

    context={
        'contact' : contact
    }
    return render(request, 'contact/contact.html', context)