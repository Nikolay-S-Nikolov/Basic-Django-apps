from django.urls import path, include

from fruitipedia_app.fruit.views import FruitCreateView, FruitEditView, FruitDetailsView, FruitDeleteView

urlpatterns = (
    path('create/', FruitCreateView.as_view(), name='fruit-create'),
    path('<int:pk>/', include([
        path('details/', FruitDetailsView.as_view(), name='fruit-details'),
        path('edit/', FruitEditView.as_view(), name='fruit-edit'),
        path('delete/', FruitDeleteView.as_view(), name='fruit-delete'),
    ])),
)
