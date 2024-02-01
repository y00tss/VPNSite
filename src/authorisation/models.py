from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom user model."""
    moderator = models.BooleanField(
        default=False
    )

    avatar = models.ImageField(
        'Images',
        default=None,
        upload_to='authorisation/images/profile_avatar',
        blank=True,
    )


# Override related_name for groups and user_permissions
CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'  # noqa
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'  # noqa


# class Statistic(models.Model):
#     """Model for statistic"""
#     user = models.ForeignKey(
#         CustomUser,
#         on_delete=models.CASCADE,
#     )
#
#     ip = models.GenericIPAddressField(
#         verbose_name='HomeIP',
#     )
#
#     def __str__(self):
#         return f'{self.user} {self.date} {self.time} {self.ip}'
#
#     class Meta:
#         verbose_name = 'Statistic'
#         verbose_name_plural = 'Statistics'
