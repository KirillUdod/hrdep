from django.db import models

# Create your models here.


class Staff(models.Model):

    first_name = models.CharField(u'Имя', max_length=255)
    middle_name = models.CharField(u'Отчество', max_length=255)
    last_name = models.CharField(u'Фамилия', max_length=255)
    birthday = models.DateField(u'Дата рождения', blank=True, null=True)
    employ_date = models.DateField(u'Дата приема', blank=True, null=True)
    unemploy_date = models.DateField(u'Дата увольнения', blank=True, null=True)
    post = models.ForeignKey('Post', verbose_name=u'Должность', )

    def __str__(self):
        return str(self.get_full_name())

    def get_full_name(self):
        full_name = u'%s %s %s' % (self.first_name, self.middle_name, self.last_name)
        return full_name.strip()


class Document(models.Model):
    EMPLOYEMENT = 0
    UNEMPLOYEMENT = 1
    DOCUMENT_TYPE = (
        (EMPLOYEMENT, u'Прием на работу'),
        (UNEMPLOYEMENT, u'Увольнение')
    )

    staff = models.ForeignKey('Staff', verbose_name=u'Сотрудник',)
    document_type = models.IntegerField(u'Тип документа', choices=DOCUMENT_TYPE)
    date = models.DateTimeField(u'Дата', auto_now=True, auto_now_add=False)
    employ_date = models.DateTimeField(u'Дата приема', blank=True, null=True)
    unemploy_date = models.DateTimeField(u'Дата увольнения', blank=True, null=True)
    number = models.IntegerField(u'Номер', unique=True)


    def __str__(self):
        return str(self.number)


class Post(models.Model):
    name = models.CharField(u'Должность', max_length=255)
    description = models.TextField(u'Описание (не обязательно)', blank=True, null=True)

    def __str__(self):
        return str(self.name)
