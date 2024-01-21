from django.urls import path

from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path("afficher/<str:type>",views.afficher,name="afficher"),
   
    path("matieres/",views.matieres,name="gerer_matieres"),
    path("stock/",views.stock,name="gerer_stock"),
    

    path("achat/",views.achat_matieres,name="achat"),
    path("transferer/",views.transferer_matieres,name="tranferer"),
    path("achat_confirmation/",views.achat_confirmation,name="confirmer"),
    path("vente_confirmation/",views.vente_confirmation,name="vente_confirmer"),
    path("vente/",views.vente_matieres,name="vente"),
    path('table_produits/',views.afficher_table , name = 'list_produit'),
    path('add_product/<str:type>',views.add_product , name='add_product'),
     path('select_product/<int:id>/<str:type>',views.select , name = 'select_product'),
    path('edit_product/<int:id>/<str:type>',views.modify_product , name = 'edit'),
    path('delete_product/<int:id>/<str:type>',views.delete_product , name = 'delete'),
    path('search_product/',views.search_product , name = 'search_product'),
     path('choose_add/',views.choosing , name='choose'),
     path('regler_fournisseur/',views.regler_fournisseur , name='regler'),
     path('regler_fournisseur_sold/<int:id>/',views.regler_fournisseur_sold , name='regler_sold'),
      path('regler_client/',views.regler_client , name='regler_client'),
     path('regler_client_credit/<int:id>/',views.regler_client_credit , name='regler_credit'),

    path('table_team/<int:id>',views.afficher_team , name = 'list_team'),
    path('select_team/<int:id>',views.select_team , name = 'select_team'),
    path('pointage/<int:id>',views.pointage , name = 'pointage'),
    path('emprunt/<int:id>',views.emprunt , name = 'emprunt'),
    path('details_centre/<int:id>',views.details , name='details'),
     
]