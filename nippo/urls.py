from django.urls import path,include
from .views import (
                    NippoListView ,
                    NippoDetailView, 
                    NippoCreateModelFormView, 
                    NippoUpdateModelFormView,
                    NippoDeleteView,
                    Nippo0View,
                    Nippo1View,
                    Nippo2View,
                    Nippo3View,
                  )

urlpatterns = [
  path("", NippoListView.as_view(), name="nippo-list"),
  path("detail/<slug:slug>/", NippoDetailView.as_view(), name="nippo-detail"),
  path("create/", NippoCreateModelFormView.as_view(), name="nippo-create"),
  path("update/<slug:slug>/", NippoUpdateModelFormView.as_view(), name="nippo-update"),
  path("delete/<slug:slug>/", NippoDeleteView.as_view(), name="nippo-delete"),
  path("0/", Nippo0View, name="nippo-0"),
  path("1/", Nippo1View, name="nippo-1"),
  path("2/", Nippo2View, name="nippo-2"),
  path("3/", Nippo3View, name="nippo-3"),
  
]