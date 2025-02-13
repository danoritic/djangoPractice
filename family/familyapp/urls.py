
from django.urls import path
from .views import CreateMember, MemberDetail, MemberList


urlpatterns = [
    path("members/", MemberList.as_view(), name="member_list"),
    path("members/create", CreateMember.as_view(), name="create_member"),
    
    
    path("members/<int:pk>/", MemberDetail.as_view(), name="member_detail")
]