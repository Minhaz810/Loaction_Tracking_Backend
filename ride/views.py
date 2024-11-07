from django.db.models import Count,Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from ride.models import Tips,AdminEarning
from ride.serializers import AdminEarningSerializer,TipsSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class TipsListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        status_counts = Tips.objects.values('status').annotate(count=Count('status'))
        response_data = {item['status']: item['count'] for item in status_counts}
        return Response(response_data)

class AdminEarningListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        admin_earnings = AdminEarning.objects.all()
        serializer = AdminEarningSerializer(admin_earnings, many=True)

        total_earning = admin_earnings.aggregate(total_earning=Sum('earning'))['total_earning'] or 0
        total_outstanding = admin_earnings.aggregate(total_outstanding=Sum('outstanding'))['total_outstanding'] or 0
        response_data = {
            "total_earning": total_earning,
            "total_outstanding": total_outstanding,
            "records": serializer.data
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
