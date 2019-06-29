
from django.shortcuts import render
from rest_framework import status
from .models import Toy
from .serializers import ToySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True)
        return Response(toys_serializer.data)
    elif request.method == 'POST':
        toy_serializer = ToySerializer(data=request.data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(toy_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def toy_detail(request, pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return Response(toy_serializer.data)
    elif request.method == 'PUT':
        toy_serializer = ToySerializer(toy, data=request.data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data)
        return Response(toy_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# a = Toy.objects.filter(pk=2).values()
#
# In [14]: type(a)
# Out[14]: django.db.models.query.QuerySet
#
# In [15]: a[0]
# Out[15]:
# {'id': 2,
#  'created': datetime.datetime(2019, 5, 15, 0, 45, 50, 828926, tzinfo=<UTC>),
#  'name': 'Hawaiian Barbie',
#  'description': 'Barbie loves Hawaii',
#  'toy_category': 'Dolls',
#  'release_date': datetime.datetime(2019, 5, 14, 17, 42, 13, 29376, tzinfo=<UTC>),
#  'was_included_in_home': True}

# In [23]: Toy.objects.all().values('name')
# Out[23]: <QuerySet [{'name': 'Clash Royale play set'}, {'name': 'Formal Test Methodology'},
#                     {'name': 'Hawaiian Barbie'}, {'name': 'Snoopy talking action figure'},
#                     {'name': 'System Test fundamental'}, {'name': 'Wonderboy puzzle'}]>