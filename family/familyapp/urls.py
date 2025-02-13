
from django.urls import path
from .views import CreateMember, MemberDetail, MemberList, MemberViewSet
from rest_framework.routers import DefaultRouter
# from .apiviews import PollViewSet


router = DefaultRouter()
router.register('members', MemberViewSet, basename='members')

urlpatterns = [
    path("members/", MemberList.as_view(), name="member_list"),
    path("members/create", CreateMember.as_view(), name="create_member"),
    
    
    path("members/<int:pk>/", MemberDetail.as_view(), name="member_detail")
]

urlpatterns += router.urls
