import traceback
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Users
from main.mongodb import users


@api_view(['POST'])
def fetch_users(request):
    try:
        if 'count' not in request.data.keys():
            return Response({'error': 'Count is required'}, status=422)

        count = request.data['count']

        response = requests.get(url="https://fakestoreapi.com/users", verify=False)

        if response.status_code != 200:
            return Response({'error': 'Unable to get data'}, status=422)

        return Response({'data': response.text}, status=200)
    except:
        traceback.print_exc()
        return Response({'error': 'Something went wrong'}, status=500)


@api_view(['GET'])
def get_users_from_postgres_db(request):
    try:
        all_users = list(Users.objects.all().values())
        return Response({"allUsers": all_users}, status=200)
    except:
        traceback.print_exc()
        return Response({'error': 'Something went wrong'}, status=500)


@api_view(['GET'])
def get_users_from_mongo_db(request):
    try:
        all_users = list(users.find({}, {'_id': 0}))
        return Response({"allUsers": all_users}, status=200)
    except:
        traceback.print_exc()
        return Response({'error': 'Something went wrong'}, status=500)
