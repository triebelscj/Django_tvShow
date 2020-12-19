from django.urls import path
# Dont forget to import VIEWS --
from . import views

urlpatterns = [
    # ******* /// RENDER ROUTES \\\\\ ********
    path('', views.dashboard),
    path('shows', views.dashboard),
    path('shows/new', views.new_page),
    # <int: show_id> = means showing the ID thats created when a new show is added.
    path('shows/<int:show_id>/edit', views.updateShowDB),
    path('shows/<int:show_id>', views.show_page),

    # ********//// ACTION ROUTES \\\\********
    path('shows/<int:show_id>/delete', views.delete),
    path('shows/create', views.create_show),
    path('shows/<int:show_id>/updatePage', views.edit_page),
]
