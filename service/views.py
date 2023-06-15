from django.contrib.postgres.search import SearchVector, SearchQuery
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer


class ContactSearchView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "query",
                openapi.IN_QUERY,
                description="Search query string",
                type=openapi.TYPE_STRING,
            )
        ]
    )
    def get(self, request):
        query = request.query_params.get("query", "")
        vector = SearchVector('email', 'first_name', 'last_name')
        search_query = SearchQuery(query)
        contacts = Contact.objects.annotate(search=vector).filter(search=search_query)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
