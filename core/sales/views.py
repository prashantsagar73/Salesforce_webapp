from rest_framework.response import Response
from .serializers import ContactSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .utils import login
from .models import Contact


# validation and filter of user data 
class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @action(detail=True,methods=['post'],permission_classes=[AllowAny])
    # permission_classes=[AllowAny]
    def contact(self, request):
        sf = login()

        if request.method == 'POST':
            data = request.data.copy()
            serializer = ContactSerializer(data=data)
            if serializer.is_valid():
                return_dict = serializer.validated_data
                query = sf.Contact.create(return_dict)
                return Response(query)
            else:
                return Response(serializer.errors)
        else:
            data = sf.query("Select Id,Name from Contact")
            result = ContactSerializer(data['records'][0])
            return Response(result.data)