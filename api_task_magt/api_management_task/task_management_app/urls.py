from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Create a router to handle the viewset routes automatically
router = DefaultRouter()

# Register the TaskViewSet with the router
# This will generate URLs for CRUD operations on the 'tasks' resource
router.register(r'tasks', TaskViewSet, basename='task')

# Assign the generated URLs from the router to urlpatterns
urlpatterns = router.urls



