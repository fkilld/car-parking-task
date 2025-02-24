from rest_framework import viewsets, status, serializers
from .models import CarParkingDetails
from .serializers import CarParkingDetailsSerializer

class CarParkingDetailsViewSet(viewsets.ModelViewSet):
    queryset = CarParkingDetails.objects.all()
    serializer_class = CarParkingDetailsSerializer

    def perform_update(self, serializer):

        instance = self.get_object()
        new_out_time = serializer.validated_data.get('outTime', instance.outTime)


        if new_out_time and new_out_time < instance.inTime:
            raise serializers.ValidationError({"error": "outTime cannot be earlier than inTime"})


        updated_instance = serializer.save()

        if updated_instance.outTime:
            updated_instance.totalSpendTime = (
                updated_instance.outTime - updated_instance.inTime
            ).total_seconds() / 60 
            

            updated_instance.save(update_fields=['totalSpendTime'])
