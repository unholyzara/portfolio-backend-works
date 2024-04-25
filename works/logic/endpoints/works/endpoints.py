from datetime import datetime

from pydantic import BaseModel, ValidationError
from django.http.response import JsonResponse
from django.views.generic import ListView

from logic.models import Work, Company
from logic.serializers import WorkSerializer
from logic.utils import get_datetime_from_string


class WorkListEndpoint(ListView):
    model = Work
    http_method_names = ["get"]

    class GetParams(BaseModel):
        active: bool = True
        date_from: str | None = None
        date_to: str | None = None

        def get_date_from(self):
            if self.date_from is None:
                return None
            return get_datetime_from_string(string=self.date_from)

        def get_date_to(self):
            if self.date_to is None:
                return None
            return get_datetime_from_string(string=self.date_to)

    def get_request_params(self):
        return self.GetParams.model_validate(self.request.GET)

    def get_queryset(self, request_params: GetParams):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            active=request_params.active,
        )
        date_from = request_params.get_date_from()
        date_to = request_params.get_date_to()
        if date_from is not None:
            queryset = queryset.filter(date_from__gte=date_from.date())
        if date_to is not None:
            queryset = queryset.filter(date_to__lte=date_to.date())
        return queryset.distinct()

    def dispatch(self, request):
        company, _ = Company.objects.get_or_create(
            active=True, name="TEST", slug="test"
        )
        Work.objects.get_or_create(
            active=True,
            date_from=datetime(year=2023, month=9, day=23).date(),
            company=company,
            slug="test-work-1",
        )
        try:
            request_params = self.get_request_params()
        except ValidationError:
            error_response = {"error": "Request Params are not valid"}
            return JsonResponse(data=error_response, status=400)
        else:
            queryset = self.get_queryset(request_params=request_params)
            serializer = WorkSerializer(queryset, many=True)
            return JsonResponse(data=serializer.data, status=200, safe=False)
