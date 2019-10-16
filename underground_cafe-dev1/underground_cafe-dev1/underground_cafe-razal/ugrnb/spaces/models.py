from django.db import models

class Outlet(models.Model):
    name=models.CharField(max_length=255,unique=True)
    full_address=models.CharField(max_length=255)
    phone_no=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Zone(models.Model):
    name=models.CharField(max_length=255)
    outlet=models.ForeignKey(Outlet,on_delete=models.CASCADE)
    description=models.TextField()

    def __str__(self):
        return self.outlet.name+" , "+self.name
        
    class Meta:
        unique_together=('name','outlet')

class Table(models.Model):
    name=models.CharField(max_length=255)
    zone=models.ForeignKey(Zone,on_delete=models.CASCADE)

    def __str__(self):
        return self.zone.__str__()+" , "+self.name
    class Meta:
        unique_together=('name','zone')    

class Seat(models.Model):
    name=models.CharField(max_length=255)
    # zone=models.ForeignKey(Zone,on_delete=models.CASCADE)
    table=models.ForeignKey(Table,on_delete=models.CASCADE)

    def __str__(self):
        return self.table.__str__()+" , "+self.name
        
    class Meta:
        unique_together=('name','table')    
