
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices

from accounts.managers import UserManager


class GenderChoices(TextChoices):
    MALE = 'MALE', 'Man'
    FEMALE = 'FEMALE', 'Women'


class Account(AbstractUser):
    username = models.CharField(
        unique=True,
        verbose_name='User name',
        max_length=100,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        blank=True,
        max_length=25
    )
    avatar = models.ImageField(
        null=True,
        blank=False,
        upload_to='avatars',
        verbose_name='Avatar',
    )
    liked_posts = models.ManyToManyField(
        verbose_name='Liked posts',
        to='posts.Post',
        related_name='user_likes'
    )
    subscriptions = models.ManyToManyField(
        verbose_name='Subscriptions',
        to='accounts.Account',
        related_name='subscribers'
    )
    commented_posts = models.ManyToManyField(
        verbose_name='Commented posts',
        to='posts.Post',
        related_name='user_comments'
    )
    description = models.TextField(
        verbose_name='Description',
        null=True,
        blank=True,
        max_length=150
    )
    phone = models.CharField(
        verbose_name='Phone',
        null=True,
        blank=True,
        max_length=15
    )
    gender = models.CharField(
        verbose_name='Gender',
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
        max_length=10
    )
    created_at = models.DateTimeField(
        verbose_name='Date of creation',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Date of change',
        auto_now=True
    )
    count_subscriptions = models.IntegerField(
        verbose_name='Count subscriptions',
        default=0
    )
    count_subscribers = models.IntegerField(
        verbose_name='Count subscribers',
        default=0
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.username}'
