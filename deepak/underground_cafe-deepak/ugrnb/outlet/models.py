from django.db import models

class Outlet(models.Model):
    # name=models.CharField(max_length=255, primary_key=True)
    name=models.CharField(max_length=255, unique=True)
    location=models.CharField(max_length=255)
    phone_no=models.CharField(max_length=255)
    email=models.EmailField(null=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "outlet"

class Zone(models.Model):
    name = models.CharField(max_length=100)
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.outlet.name, self.name)
    class Meta:
        db_table = "zone"

class Table(models.Model):
    name = models.CharField(max_length=100)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.zone.name, self.name)
    class Meta:
        db_table = "table"

class Seat(models.Model):
    number = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.table.name, self.number)
    class Meta:
        db_table = "seat"