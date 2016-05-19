from django.db import models
from django.db.models import Q
from django.db.utils import IntegrityError
# Create your models here.


class StaffManager(models.Manager):

    def all_working(self):
        qs = super(StaffManager, self).filter(~Q(employ_date=None), dismiss_date=None)
        return qs

    def all_new(self):
        qs = super(StaffManager, self).filter(employ_date=None, dismiss_date=None)
        return qs

    def all_dismissed(self):
        qs = super(StaffManager, self).filter(~Q(employ_date=None), ~Q(dismiss_date=None))
        return qs


class Staff(models.Model):

    first_name = models.CharField(u'Имя', max_length=255)
    middle_name = models.CharField(u'Отчество', max_length=255)
    last_name = models.CharField(u'Фамилия', max_length=255)
    birthday = models.DateField(u'Дата рождения', blank=True, null=True)
    employ_date = models.DateField(u'Дата приема', blank=True, null=True)
    dismiss_date = models.DateField(u'Дата увольнения', blank=True, null=True)
    post = models.ForeignKey('Post', verbose_name=u'Должность', )

    objects = StaffManager()

    class Meta:
        unique_together = ('first_name', 'middle_name', 'last_name')

    def __str__(self):
        return str(self.get_full_name())

    def get_full_name(self):
        full_name = u' '.join([self.first_name, self.middle_name, self.last_name])
        return full_name

    # @property
    # def is_working(self):
    #     if self.employ_date is not None and self.employ_date <= timezone.now().date() and self.dismiss_date is None:
    #         return True
    #     return False
    #
    # @property
    # def is_new(self):
    #     if self.employ_date is None  and self.dismiss_date is None:
    #         return True
    #     return False
    #
    # @property
    # def is_dismiss(self):
    #     if self.employ_date is not None and self.dismiss_date is not None:
    #         return True
    #     return False


class Document(models.Model):
    EMPLOYEMENT = 0
    DISMISSMENT = 1
    DOCUMENT_TYPE = (
        (EMPLOYEMENT, u'Прием на работу'),
        (DISMISSMENT, u'Увольнение')
    )

    staff = models.ForeignKey('Staff', verbose_name=u'Сотрудник',)
    document_type = models.IntegerField(u'Тип документа', choices=DOCUMENT_TYPE, null=True)
    date = models.DateTimeField(u'Дата', auto_now=True, auto_now_add=False)
    employ_date = models.DateField(u'Дата приема', blank=True, null=True)
    dismiss_date = models.DateField(u'Дата увольнения', blank=True, null=True)
    number = models.IntegerField(u'Номер', unique=True)

    class Meta:
        unique_together = ('date', 'number')

    def save(self, *args, **kwargs):
        if self.document_type == self.EMPLOYEMENT and self.employ_date is None:
            raise IntegrityError
        if self.document_type == self.DISMISSMENT and self.dismiss_date is None:
            raise IntegrityError
        if self.DOCUMENT_TYPE == self.DISMISSMENT and self.dismiss_date is not None and self.employ_date is None:
            raise IntegrityError
        super(Document, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.number)


class Post(models.Model):
    name = models.CharField(u'Должность', max_length=255)
    description = models.TextField(u'Описание (не обязательно)', blank=True, null=True)

    def __str__(self):
        return str(self.name)