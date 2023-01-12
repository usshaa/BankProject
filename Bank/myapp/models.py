from django.db import models


# Create your models here.
districts = (('CH','chennai'),('Ma','madurai'),('TR','trichy'),('SA','salem'))
branch = (('Ad','adayar'),('Na','navalur'),('Si','siruseri'))
accounts = (('CA','current'),('SA','savings'))
gender_choices =((0,'male'),(1,'female'),(2,'not specified'))


class UserApplication(models.Model):
    name = models.CharField(max_length=200,null=False)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.IntegerField(choices=gender_choices,default='female')
    phone_number = models.PositiveBigIntegerField(unique=True,null=False)
    mail_id = models.EmailField(max_length=200,unique=True,null=False)
    address = models.TextField(max_length=100,null=False)
    district = models.CharField(max_length=200,choices=districts,default='chennai')
    branch = models.CharField(max_length=200,choices=branch,default='adayar')
    account_type = models.CharField(max_length=200,choices=accounts,default='savings')
    credit_card = models.BooleanField()
    debit_card = models.BooleanField()
    cheque_book = models.BooleanField()

    def __str__(self):
        return self.name
