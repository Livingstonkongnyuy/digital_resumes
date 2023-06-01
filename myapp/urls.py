from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),



    path('digitalresume/blog', views.blog, name='blog'),    
    path('digitalresume/blog/update_blog<str:pk>', views.update_blog, name='update_blog'),    
    path('digitalresume/blog/delete_blog<str:pk>', views.delete_blog, name='delete_blog'),    
    path('digitalresume/blog/add_blog', views.add_blog, name='add_blog'),    
    path('digitalresume/blog/blog_detail<str:pk>', views.blog_detail, name='blog_detail'),    
    
    
    path('digitalresume/certificate/certificates', views.certificates, name = 'certificates'),
    path('digitalresume/blog/certificate/add_certificate', views.add_certificate, name = 'add_certificate'),
    path('digitalresume/blog/certificate/certificate_details<str:pk>', views.certificate_details, name = 'certificate_details'),
    path('digitalresume/blog/certificate/certificate_update<str:pk>', views.certificate_update, name = 'certificate_update'),
    path('digitalresume/blog/certificate/certificate_delete<str:pk>', views.certificate_delete, name = 'certificate_delete'),
    
    
    path('digitalresume/resume', views.resume, name='resume'),    
    path('digitalresume/contact', views.contact, name='contact'),    


    path('digitalresume/add_profile', views.add_profile, name='add_profile'),
    path('digitalresume/update_profile', views.update_profile, name='update_profile'),
    
    
    path('digitalresume/testimonies', views.testimonies, name='testimonies'),
    path('digitalresume/view_testimonies', views.view_testimonies, name='view_testimonies'),
    path('digitalresume/delete_testimonie<str:name>', views.delete_testimonie, name='delete_testimonie'),
    path('digitalresume/update_testimonie<str:name>', views.update_testimonie, name='update_testimonie'),
    path('digitalresume/create_testimonie', views.create_testimonie, name='create_testimonie'),


    path('digitalresume/portfolio', views.portfolio, name='portfolio'), 
    path('portfolioresume/add_portfolio', views.add_portfolio, name='add_portfolio'), 
    path('portfolioresume/delete_portfolio<str:pk>', views.delete_portfolio, name='delete_portfolio'), 
    path('portfolioresume/update_portfolio<str:pk>', views.update_portfolio, name='update_portfolio'), 
    path('portfolioresume/portfolio_detail<str:pk>', views.portfolio_detail, name='portfolio_detail'), 




    path('digitalresume/services', views.services, name='services'), 
    path('portfolioresume/add_service', views.add_service, name='add_service'), 
    path('portfolioresume/delete_service<str:pk>', views.delete_service, name='delete_service'), 
    path('portfolioresume/update_service<str:pk>', views.update_service, name='update_service'), 
    path('portfolioresume/services_content<str:pk>', views.services_content, name='services_content'), 

    # path('digitalresume/services', views.services, name='services'),    




    path('signup', views.signup, name='signup'),
    path('signin', views.login, name='login'),
    path('signout', views.signout, name = 'signout')
]