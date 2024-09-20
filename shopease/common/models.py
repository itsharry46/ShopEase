from django.db import models

# Common Application Models
class Role(models.Model):
    
    class Meta:
        db_table = 'se_role'
        indexes = []

    ROLE_STATUS_CHOICES = [
        ('Y', 'Active'),
        ('N', 'Inactive')
    ]
    
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50, unique=True)
    role_status = models.CharField(max_length=1, choices=ROLE_STATUS_CHOICES, default='Y')
    updated_at = models.DateTimeField(auto_now=True)


class User(models.Model):

    class Meta:
        db_table = 'se_user'
        indexes = [
            models.Index(fields=['user_email']),
            models.Index(fields=['user_username']),
            models.Index(fields=['user_role']),
            models.Index(fields=['updated_at']),
        ]

    USER_STATUS_CHOICES = [
        ('Y', 'Active'),
        ('N', 'Inactive')
    ]

    user_id = models.AutoField(primary_key=True)
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=250, unique=True)
    user_username = models.CharField(max_length=100)
    user_password = models.CharField(max_length=128)
    user_role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True)
    user_status = models.CharField(max_length=1, choices=USER_STATUS_CHOICES, default='Y')
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)





# Consumer Applications Models





# Admin Applications Models