class Order(models.Model):
    client_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)

class Order(models.Model):
    client_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    repair_status = models.CharField(max_length=50, default="Принят")