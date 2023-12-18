from django.urls import path
from userApp import views

urlpatterns=[
        path('homepage_fn/',views.homepage_fn,name="homepage_fn"),
        path('about_fn/',views.about_fn,name="about_fn"),
        path('contact_fn/',views.contact_fn,name="contact_fn"),
        # ................................................................................................................

        path('Service/',views.Service,name="Service"),
        path('agent_fn/',views.agent_fn,name="agent_fn"),
        path('saveAgents/',views.saveAgents,name="saveAgents"),
        path('Product_fn/<cat_name>',views.Product_fn,name="Product_fn"),
        # ................................................................................................................

        path('registerform_fun/',views.registerform_fun,name="registerform_fun"),
        path('SaveRegister/',views.SaveRegister,name="SaveRegister"),
        path('Signin_fn/',views.Signin_fn,name="Signin_fn"),
        path('UserLogout_fn/',views.UserLogout_fn,name="UserLogout_fn"),
        path('Payment_page/',views.Payment_page,name="Payment_page"),
        path('singleproduct_fn/<dataid>',views.singleproduct_fn,name="singleproduct_fn"),
        path('feedback_fn/',views.feedback_fn,name="feedback_fn"),
        path('search/',views.search,name="search"),
        path('bookingPage/',views.bookingPage,name="bookingPage"),
        path('Savebooking/',views.Savebooking,name="Savebooking"),
        path('SaveContact/',views.SaveContact,name="SaveContact"),
        path('savepayment/',views.savepayment,name="savepayment"),
        path('Savefeedback/',views.Savefeedback,name="Savefeedback"),
        path('user_logout/',views.user_logout,name="user_logout"),
]