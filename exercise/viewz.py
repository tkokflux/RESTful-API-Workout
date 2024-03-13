from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WorkOut
from .serializers import WorkOutSerializer

@api_view(['GET'])
def getworkout(request):
   
    exercises = WorkOut.objects.all()  
    serializer = WorkOutSerializer(exercises, many=True)  
    return Response(serializer.data)  