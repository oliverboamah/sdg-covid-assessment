# django imports
from django.urls import path

# covid_app imports
from src.covid_project.covid_app.api.v1.views.estimator_api_json_view import EstimatorJSONAPIView

app_name = 'covid_app'
urlpatterns = [
    path(route='api/v1/on-covid-19', view=EstimatorJSONAPIView.as_view(), name='default_estimator'),
    path(route='api/v1/on-covid-19/json', view=EstimatorJSONAPIView.as_view(), name='estimator_json'),
]
