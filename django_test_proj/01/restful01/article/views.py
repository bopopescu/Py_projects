from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer


class ArticleView(APIView):
    # [26/Jun/2019 11:25:45] "GET /api/articles/ HTTP/1.1" 200 5202
    def get(self, request):
        articles = Article.objects.all()
        # without serializers
        # return Response({"articles": articles})
        # Add serializers
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    #
    # the list of articles is trying to be serialized/converted from an object into JSON.
    # If no class is created to serialize the Article objects, there will be error.
    # need to create an serializers.py
# Serializers allow complex data such as querysets and model instances to be converted
# to native Python datatypes that can then be easily rendered into JSON, XML
# or other content types.

# GET /api/articles/
# HTTP 200 OK
# Allow: GET, HEAD, OPTIONS
# Content-Type: application/json
# Vary: Accept
#
# {
#     "articles": []
# }

    def post(self, request):
        article = request.data.get('article')

        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})
