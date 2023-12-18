from django.urls import path
from luxuaryvillaApp import views


urlpatterns=[
        path('indexfun/',views.indexfun,name="indexfun"),
        path('addcat_fn/',views.addcat_fn,name="addcat_fn"),
        path('Savecategory/',views.Savecategory,name="Savecategory"),
        path('displaycat_fn/',views.displaycat_fn,name="displaycat_fn"),
        path('editcat_fun/<int:dataid>/',views.editcat_fun,name="editcat_fun"),
        path('updatecat_fn/<int:dataid>/',views.updatecat_fn,name="updatecat_fn"),
        path('deletecat_fn/<int:dataid>/', views.deletecat_fn, name="deletecat_fn"),
        path('displaycontactfn/', views.displaycontactfn, name="displaycontactfn"),


        path('addproduct_fn/',views.addproduct_fn,name="addproduct_fn"),
        path('saveproduct_fn/',views.saveproduct_fn,name="saveproduct_fn"),
        path('displayproduct_fun/', views.displayproduct_fun, name="displayproduct_fun"),
        path('editproductfn/<int:dataid>/',views.editproductfn,name="editproductfn"),
        path('updateproduct_fun/<int:dataid>/',views.updateproduct_fun,name="updateproduct_fun"),
        path('deleteproduct_fn/<int:dataid>/',views.deleteproduct_fn,name="deleteproduct_fn"),

        path('login_page/',views.login_page,name="login_page"),
        path('admin_login/',views.admin_login,name="admin_login"),
        path('admin_logout/',views.admin_logout,name="admin_logout"),

        # path('Agentadmin_fn/',views.Agentadmin_fn,name="Agentadmin_fn"),
        path('addAgent/',views.addAgent,name="addAgent"),
        path('saveAgent_page/',views.saveAgent_page,name="saveAgent_page"),
        path('displayAgent_fun/',views.displayAgent_fun,name="displayAgent_fun"),
        path('editAgent/',views.editAgent,name="editAgent"),
        path('updateAgent_fun/',views.updateAgent_fun,name="updateAgent_fun"),
        path('deleteAgent_fn/',views.deleteAgent_fn,name="deleteAgent_fn"),


]