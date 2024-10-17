from django.db import models


# Common Application Models
class Artifact(models.Model):
    
    class Meta:
        db_table = 'se_artifact'
        unique_together = (
            ('artifact_role_id', 'artifact_module_id')
        )
        indexes = [
            models.Index(fields=['artifact_role_id']),
            models.Index(fields=['artifact_module_id']),
            models.Index(fields=['artifact_create_status']),
            models.Index(fields=['artifact_read_status']),
            models.Index(fields=['artifact_update_status']),
            models.Index(fields=['artifact_delete_status'])
        ]
    
    ARTIFACT_CREATE_STATUS_CHOICES = [
        ('Y', 'Active'),
        ('N', 'Inactive')
    ]

    ARTIFACT_READ_STATUS_CHOICES = [
        ('Y', 'Active'),
        ('N', 'Inactive')
    ]

    ARTIFACT_UPDATE_STATUS_CHOICES = [
        ('Y', 'Active'),
        ('N', 'Inactive')
    ]

    ARTIFACT_DELETE_STATUS_CHOICES = [
        ('Y', 'Active'),
        ('N', 'Inactive')
    ]

    artifact_id = models.AutoField(primary_key=True)
    artifact_order_id = models.IntegerField(unique=True)
    artifact_role_id = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, db_column='artifact_role_id')
    artifact_module_id = models.ForeignKey('Module', on_delete=models.SET_NULL, null=True, db_column='artifact_module_id')
    artifact_create_status = models.CharField(max_length=1, choices=ARTIFACT_CREATE_STATUS_CHOICES, default='N')
    artifact_read_status = models.CharField(max_length=1, choices=ARTIFACT_READ_STATUS_CHOICES, default='N')
    artifact_update_status = models.CharField(max_length=1, choices=ARTIFACT_UPDATE_STATUS_CHOICES, default='N')
    artifact_delete_status = models.CharField(max_length=1, choices=ARTIFACT_DELETE_STATUS_CHOICES, default='N')
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)


class Module(models.Model):
    
    class Meta:
        db_table = 'se_module'
        indexes = [
            models.Index(fields=['module_status']),
            models.Index(fields=['module_icon']),
            models.Index(fields=['module_link'])
        ]

    MODULE_STATUS_CHOICES = [
        ('Y', 'Active'),
        ('N', 'Inactive')
    ]

    module_id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=100, unique=True)
    module_icon = models.CharField(max_length=250)
    module_link = models.CharField(max_length=250, null=True)
    module_status = models.CharField(max_length=1, choices=MODULE_STATUS_CHOICES, default='Y')
    updated_at = models.DateTimeField(auto_now=True)


class Role(models.Model):
    
    class Meta:
        db_table = 'se_role'
        indexes = [
            models.Index(fields=['role_status']),
            models.Index(fields=['is_deleted'])
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


class User(models.Model):

    class Meta:
        db_table = 'se_user'
        indexes = [
            models.Index(fields=['user_email']),
            models.Index(fields=['user_username']),
            models.Index(fields=['user_password']),
            models.Index(fields=['user_role_id']),
            models.Index(fields=['user_status']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['updated_at'])
        ]

    USER_STATUS_CHOICES = [
        ('Y', 'Active'),
        ('N', 'Inactive')
    ]
    
    user_id = models.AutoField(primary_key=True)
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=250)
    user_username = models.CharField(max_length=100)
    user_password = models.CharField(max_length=128)
    user_role_id = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, db_column='user_role_id')
    user_status = models.CharField(max_length=1, choices=USER_STATUS_CHOICES, default='Y')
    is_deleted = models.BooleanField(default=False)
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)


# Inventory Application Models


# Consumer Application Models