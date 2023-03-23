import traceback
import sys
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

from test_afifa.settings import REDIS_URL
from main.models import Users, Product
from main.mongodb import users
from main.tasks import add_users_to_db

from main.redis_cache import RedisDBConnector


redis_conn = RedisDBConnector(
    host=REDIS_URL,
    port=6379,
    password=''
)


# =====================================================
# add dummy data to product table
def add_data_to_product_table():
    try:
        with open('main/products.json', 'r') as f:
            d = json.load(f)

            for p in d:
                if not Product.objects.filter(product_name=p['productName']).exists():
                    Product.objects.create(
                        product_name=p['productName']
                    )
    except:
        traceback.print_exc()


if 'makemigrations' not in sys.argv or 'migrate' not in sys.argv:
    # do not execute during migrations
    add_data_to_product_table()
# =====================================================


@api_view(['POST'])
def fetch_users(request):
    try:
        if 'count' not in request.data.keys():
            return Response({'error': 'Count is required'}, status=422)

        count = request.data['count']

        for i in range(count):
            add_users_to_db.delay()

        return Response({'status': True}, status=200)
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


@api_view(['GET'])
def get_products_from_postgres_db(request):
    try:
        all_products = list(Product.objects.all().values())
        return Response({"allProducts": all_products}, status=200)
    except:
        traceback.print_exc()
        return Response({'error': 'Something went wrong'}, status=500)


@api_view(['GET'])
def get_product_by_id(request):
    try:
        if 'productID' not in request.query_params.keys():
            return Response({"error": "productID is required"}, status=422)

        id = request.query_params['productID']

        # try to fetch from redis cache
        product = redis_conn.get_product_by_id(int(id))

        # if not in cache fetch from database and add to cache
        if product is None:
            if not Product.objects.filter(id=int(id)).exists():
                return Response({"error": "Product not found"}, status=200)

            # fetch from database and serialize query set
            product = serializers.serialize('json', Product.objects.filter(id=int(id)))
            product = json.loads(product)[0]

            # add to redis cache
            redis_conn.add_product(product['pk'], product['fields'])
            product = product['fields']

        product['id'] = int(id)

        return Response({"product": product}, status=200)
    except:
        traceback.print_exc()
        return Response({'error': 'Something went wrong'}, status=500)

