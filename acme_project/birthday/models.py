from django.db import models


class Birthdey(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=20
    )
    last_name = models.CharField(
        'Фамилия',
        blank=True,
        help_text='Необязательное поле',
        max_length=20
    )
    birthdey = models.DateField('Дата рождения')
