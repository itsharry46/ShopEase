from django.db import models

# Common Application Models
class Module(models.Model):

    class Meta:
        db_table = 'se_module'
        indexes = [
            models.Index(fields=['is_active']),
        ]
    
    MODULE_STATUS_CHOCIES = [
        ('Y', 'Active'),
        ('N', 'Inactive')
    ]

    module_id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=100, unique=True)
    module_status = models.CharField(max_length=1, choices=MODULE_STATUS_CHOCIES, default='Y')
    updated_at = models.DateTimeField(auto_now=True)


class Role(models.Model):
    
    class Meta:
        db_table = 'se_role'
        indexes = [
            models.Index(fields=['role_status']),
            models.Index(fields=['is_deleted']),
        ]

    ROLE_STATUS_CHOICES = [
        ('Y', 'Active'),
        ('N', 'Inactive')
    ]
    
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50, unique=True)
    role_status = models.CharField(max_length=1, choices=ROLE_STATUS_CHOICES, default='Y')
    is_deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)


class SubModule(models.Model):
    
    class Meta:
        db_table = 'se_sub_module'
        indexes = [
            models.Index(fields=['sub_module_module_id']),
            models.Index(fields=['sub_module_status'])
        ]
    
    SUB_MODULE_STATUS_CHOICES = [
        ('Y', 'Active'),
        ('N', 'Inactive')
    ]

    sub_module_id = models.AutoField(primary_key=True)
    sub_module_name = models.CharField(max_length=100, unique=True)
    sub_module_module_id = models.ForeignKey('Module', on_delete=models.SET_NULL, null=True, db_column='sub_module_module_id')
    sub_module_status = models.CharField(max_length=1, choices=SUB_MODULE_STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)


class User(models.Model):

    class Meta:
        db_table = 'se_user'
        indexes = [
            models.Index(fields=['user_email']),
            models.Index(fields=['user_username']),
            models.Index(fields=['user_password']),
            models.Index(fields=['user_status']),
            models.Index(fields=['is_deleted']),
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
    user_role_id = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, db_column='user_role_id')
    user_status = models.CharField(max_length=1, choices=USER_STATUS_CHOICES, default='Y')
    is_deleted = models.BooleanField(default=False)
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)





# Consumer Applications Models





# Admin Applications Models