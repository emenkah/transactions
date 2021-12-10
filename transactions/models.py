from django.db import models

# Create your models here.


class Transactions(models.Model):
    name = models.CharField('Fullname', max_length=256)
    address = models.CharField('Fullname', max_length=256)
    checked = models.BooleanField('Checked', blank=True, null=True)
    description = models.CharField('Fullname', max_length=256)
    interest = models.CharField('Interest', max_length=256, blank=True, null=True)
    date_of_birth = models.DateTimeField("Date of Birth", blank=True, null=True)
    email = models.EmailField('Email address.', max_length=255, blank=True, null=True)
    account	= models.IntegerField('Account No', blank=True, null=True)
    credit_card = models.JSONField()
    position = models.IntegerField("Position", blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}-{}-{}'.format(self.name, self.email, self.account, self.date_of_birth)


# class Track(models.Model):
#     STATUS_CHOICE = (
#         ('complete', 'complete'),
#         ('started', 'started'),
#     )
#     created_datetime = models.DateTimeField(auto_now_add=True)
#     position = models.IntegerField("Position", blank=True, null=True)
#     status = models.CharField('Status', choices=STATUS_CHOICE, max_length=256, blank=True, null=True)
    
#     def __str__(self):
#         return '{}-{}'.format(self.position, self.created_datetime)

