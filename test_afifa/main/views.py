import traceback

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def fetch_users(request):
    try:
        pass
    except:
        traceback.print_exc()
        return Response({'error': 'Something went wrong'}, status=500)
