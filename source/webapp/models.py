from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    ACTIVE = 'ACTIVE', 'Активна'
    NOT_ACTIVE = 'NOT_ACTIVE', 'Неактивна'


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Заголовок')
    description = models.TextField(max_length=2000, blank=False, null=False, verbose_name='Описание')
    status = models.CharField(max_length=100, choices=StatusChoice.choices, verbose_name='Статус', default=StatusChoice.ACTIVE)
    created_at = models.DateTimeField(max_length=3000, verbose_name='Дата')
    is_deleted = models.BooleanField(verbose_name='Удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.title} - {self.description} - {self.status} - {self.created_at}'
