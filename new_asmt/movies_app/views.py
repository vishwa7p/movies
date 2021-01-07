from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response

from movies_app.models import Movies, Poster


class AddPoster(APIView):
    def post(self, request):
        try:
            json_data = request.data
            self.poster = json_data['poster']
        except Exception as e:
            print(e)
            return Response('json_key_error', status=status.HTTP_406_NOT_ACCEPTABLE)
        picture = Poster(poster=self.poster)
        picture.save()
        poster = str(picture.id) + '_' + str(picture.poster)
        response_data = {"Status": "Success",
                         "message": "poster uploaded successfully",
                         "data": poster}
        return Response(response_data, status=status.HTTP_200_OK)


class AddMovies(APIView):
    def post(self, request):
        try:
            json_data = request.data
            self.group = json_data['group']
            self.poster_id = json_data['poster_id']
            self.name = json_data['movie_name']
            self.director = json_data['movie_director']
        except Exception as e:
            print(e)
            return Response('json_key_error', status=status.HTTP_406_NOT_ACCEPTABLE)
        if self.group == "admin":
            movie = Movies(name=self.name, director=self.director, poster_id=self.poster_id)
            movie.save()
            response_data = {"Status": "Success",
                             "message": "movie added successfully",
                             "data": {}}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response("access denied", status=status.HTTP_400_BAD_REQUEST)


class UpdateMovies(APIView):
    def post(self, request, pk):
        try:
            json_data = request.data
            self.group = json_data['group']
            self.poster_id = json_data['poster_id']
            self.name = json_data['movie_name']
            self.director = json_data['movie_director']
        except Exception as e:
            print(e)
            return Response('json_key_error', status=status.HTTP_406_NOT_ACCEPTABLE)
        if self.group == "admin":
            movie = Movies.objects.filter(pk=pk).update(name=self.name, director=self.director)
            response_data = {"Status": "Success",
                             "message": "updated successfully",
                             "data": {}}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response("access denied", status=status.HTTP_400_BAD_REQUEST)


class DeleteMovies(APIView):
    def post(self, request, pk):
        json_data = request.data
        self.group = json_data['group']
        if self.group == "admin":
            movie = Movies.objects.get(pk=pk)
            movie.delete()
            response_data = {"Status": "Success",
                             "message": "deleted successfully",
                             "data": {}}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response("access denied", status=status.HTTP_400_BAD_REQUEST)


class MoviesList(APIView):
    def get(self, request):
        my_list = []
        for i in Movies.objects.all():
            my_dict = {}
            my_dict["movie"] = i.name
            my_dict["movie_director"] = i.director
            my_dict["poster_id"] = i.poster_id
            my_list.append(my_dict)
        response_data = {"Status": "Success",
                         "data": my_list}
        return Response(response_data, status=status.HTTP_200_OK)


# class Registration(APIView):
#     def post(self, request):
#         try:
#             json_data = request.data
#             self.username = json_data['username']
#             self.password = json_data['password']
#             self.group = json_data['group']
#         except:
#             return Response({'message': 'json key error'})
#
#         if not self.username:
#             response_data = {"message": "username cannot be blank"}
#             return Response(response_data, status=status.HTTP_404_NOT_FOUND)
#         else:
#             user = User(username=self.username)
#             user.save()
#             users = User.objects.get(username=self.username)
#             users.set_password(self.password)
#             users.save()
#             my_group = Group.objects.get_or_create(name=self.group)
#             print(my_group)
#             my_group.user_set.add(self.group)
#             response_data = {"Status": "Success",
#                              "message": "registration success",
#                              "data": {}}
#             return Response(response_data, status=status.HTTP_200_OK)


# class Login(APIView):
#     def post(self, request):
#         try:
#             token = request.META["HTTP_AUTHORIZATION"]
#             json_data = request.data
#             username = json_data['username']
#             password = json_data['password']
#         except:
#             return Response({'message': 'json key error'})
#
#         if not username:
#             response_data = {"message": 'username necessary'}
#             return Response(response_data, status=status.HTTP_404_NOT_FOUND)
#         if not password:
#             response_data = {"message": 'password required for login'}
#             return Response(response_data, status=status.HTTP_404_NOT_FOUND)
#         user = User.objects.get(username=username)
#         print(user)
#         user1 = authenticate(username=username, password=password)
#         print(user1, 'user')
#         if user:
#             token1 = Token.objects.filter(key=token)
#             print(token1, 'token')
#             if token1:
#                 token1.delete()
#             token1 = Token.objects.create(user=user)
#             print(token1.key)
#             token1.save()
#             return Response('Login successfully')
#         return Response('token')
