from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tips

class TipsListView(APIView):
    def get(self, request):
        status_counts = Tips.objects.values('status').annotate(count=Count('status'))
        response_data = {item['status']: item['count'] for item in status_counts}
        return Response(response_data)
