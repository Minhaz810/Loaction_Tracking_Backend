from ride.models import Tips
import random

statuses = ['completed', 'in_process', 'cancelled']

def create_tips():
    for i in range(10):
        Tips.objects.create(
            driver_id=random.choice([1, 2, 3, 4]),
            status=random.choice(statuses)
        )