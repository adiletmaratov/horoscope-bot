from django.db import models


class NambaOneUser(models.Model):
    n1_user_id = models.IntegerField(verbose_name="ID пользователя в Namba One",
                                     unique=True)
    datetime_created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['datetime_created']

