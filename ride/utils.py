import random
from ride.models import Tips,AdminEarning
from django.utils import timezone

statuses = ['completed', 'in_process', 'cancelled']

def create_tips():
    for i in range(10):
        Tips.objects.create(
            driver_id=random.choice([1, 2, 3, 4]),
            status=random.choice(statuses)
        )
    
def create_random_admin_earnings():
    for _ in range(20):
        earning = round(random.uniform(0, 999.99), 2)
        outstanding = round(random.uniform(0, 999.99), 2)
        
        AdminEarning.objects.create(
            date=timezone.now(),
            earning=earning,
            outstanding=outstanding
        )