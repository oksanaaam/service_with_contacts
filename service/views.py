from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer


class ContactSearchView(APIView):
    def get(self, request):
        query = request.query_params.get("query", "")
        contacts = Contact.objects.filter(
            Q(email__icontains=query)
            | Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
        )
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
