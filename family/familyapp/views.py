from django.shortcuts import render, get_object_or_404 
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MemberSerializer
from .models import Member
from rest_framework import generics


class MemberList(generics.ListCreateAPIView): 
    queryset = Member.objects.all() 
    serializer_class = MemberSerializer

class MemberDetail(generics.RetrieveDestroyAPIView): 
    queryset = Member.objects.all() 
    serializer_class = MemberSerializer

class CreateMember(generics.CreateAPIView): 
    queryset = Member.objects.all() 
    serializer_class = MemberSerializer



# class based view using apiview

# class MemberList(APIView):
#     def get(self, request):
#         members=Member.objects.all()
#         data=MemberSerializer(members,many=True).data
#         return Response(data)


# class MemberDetail(APIView):
#     def get(self, request,pk):
#         member=get_object_or_404(Member,pk=pk)
#         data=MemberSerializer(member,).data
#         return Response(data)

# function based view

# def member_list(request): 
#     MAX_OBJECTS = 20
#     member = Member.objects.all()[:MAX_OBJECTS]
#     data = {"results": list(member.values("name", "alias", "date_of_birth"))}
#     return JsonResponse(data)


# def member_detail(request, pk):
#     member = get_object_or_404(Member, pk=pk) 
#     data = {"results": {
#             "name": member.name,
#             "alias": member.alias,
#             "date_of_birth": member.date_of_birth
#     }}
#     return JsonResponse(data)