from django.db import models

class ClientType(models.Model):
    type_id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Client(models.Model):
    GENDER_CHOICES = [(1, "Male"), (2, "Female")]

    cid = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=150, null=False)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    type = models.ForeignKey(ClientType, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name

class Product(models.Model):
    pid = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Order(models.Model):
    oid = models.IntegerField(primary_key=True, default=0)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateField()
    shipping_date = models.DateField()
