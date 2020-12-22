from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authors.models import Authors
from authors.serializers import AuthorsSerializer


@api_view(['GET', 'POST'])
def authors_list(request, format=None):
    
    if request.method == 'GET':
        authors = Authors.objects.all()
        serializer = AuthorsSerializer(authors, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AuthorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)