from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

# from .serializers import ProductSerializer, QuestionSerializer, UserResponseSerializer
# from .models import Product, Questions, UserResponse
from .serializers import QuestionSerializer, UserResponseSerializer
from .models import Questions, UserResponse


# Create your views here.

"""@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>/',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>/',
        'Delete': '/product-detail/<int:id>/',
    }
    return Response(api_urls);
"""

# @api_view(['GET'])
# def ShowAll(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def ViewProduct(request, pk):
#     product = Product.objects.get(id=pk)
#     serializer = ProductSerializer(product, many=False)
#     print(serializer.data)
#     return Response(serializer.data)



# @api_view(['POST'])
# def CreateProduct(request):
#     serializer = ProductSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)



# @api_view(['POST'])
# def updateProduct(request, pk):
#     product = Product.objects.get(id=pk)
#     serializer = ProductSerializer(instance=product, data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['GET'])
# def deleteProduct(request, pk):
#     product = Product.objects.get(id=pk)
#     product.delete()

#     return Response('Items delete successfully!')


#getting questions as json
@api_view(['GET'])
def getQuestions(request):
    questions = Questions.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createQuestions(request):
    serializer = QuestionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()


    return Response(serializer.data)

#ML model 
@api_view(['POST'])
def diagnoseUser(request):
    serializer = UserResponseSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        #can add ML process here
        return Response("isvalid")
    return Response(serializer.data)
#can return ML result