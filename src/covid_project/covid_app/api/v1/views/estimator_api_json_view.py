# third party imports
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# covid_app imports
from src.covid_project.covid_app.api.v1.serializers.estimator_serializer import EstimatorSerializer

# import estimator.py
from src import estimator


class EstimatorJSONAPIView(APIView):

    def post(self, request):
        try:
            estimator_serializer = EstimatorSerializer(data=request.data)
            if estimator_serializer.is_valid():
                data = estimator.estimator(data=estimator_serializer.data)
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                raise Exception('One or more params are invalid')
        except Exception as e:
            print(e)
            response = {
                'status': '400 - Bad request',
                'message': e.__str__()
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
