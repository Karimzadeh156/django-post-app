from django.db import models
from jalali_date import *

class article(models.Model):
    title = models.CharField('عنوان', max_length=100)
    create_date = models.DateTimeField('تاریخ')
#    create_date = models.DateTimeField('تاریخ',auto_now_add=True)
    body = models.TextField('متن')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=True, )

    def __str__(self):
        return self.title

    def continu(self):
        k = -1
        for space in self.body[200:222]:
            k += 1
            if space == " ":
                break
        return self.body[:200+k] + '...'

    def shamsidate(self):
        shamsi = datetime2jalali(self.create_date)
        return shamsi.strftime('%a %d %b %Y -' 'ساعت ' '%H:%M ')
