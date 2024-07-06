from django.db import models 
from phonenumber_field.modelfields import PhoneNumberField

class Donor(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=40)
    address = models.TextField(blank=True)
    state = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    med_history = models.CharField(max_length=100,blank=True)
    blood = models.CharField(max_length=40,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Organ(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=40)
    address = models.TextField(blank=True)
    state = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    donate = models.CharField(max_length=20,null=True, blank=True)
    other=models.CharField(max_length=100,null=True)
    donate_tissue = models.CharField(max_length=20,null=True, blank=True)
    proof = models.FileField(upload_to="organ_proofs/%Y/%m")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Looking(models.Model):
    name = models.CharField(max_length=40)
    patient = models.CharField(max_length=40)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False)
    dob = models.DateField(null=True)
    address = models.TextField(blank=True)
    state = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    units = models.IntegerField(blank=True)
    blood = models.CharField(max_length=40,blank=True)
    require = models.CharField(max_length=80, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient

class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

