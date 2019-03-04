from _pydecimal import Decimal

from django.db import models


class Competence(models.Model):
    class Meta:
        verbose_name = 'Компетенция'
        verbose_name_plural = 'Компетенции'

    name = models.CharField(max_length=300, unique=True, verbose_name="Название")
    code = models.CharField(max_length=10, unique=True, verbose_name="Шифр")
    type = models.CharField(max_length=50, verbose_name="Расшифровка")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return "%s %s" % (self.code, self.name)


class Module(models.Model):
    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    name = models.CharField(max_length=200, unique=True, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    competences = models.ManyToManyField(Competence, related_name="developed_competences", verbose_name="Компетенции",
                                         blank=True)
    child_modules = models.ManyToManyField("self", blank=True, verbose_name="Следующие модули")
    parent_modules = models.ManyToManyField("self", blank=True, verbose_name="Предыдущие модули")

    def __str__(self):
        return self.name


class Role(models.Model):
    class Meta:
        verbose_name = 'Роль/Позииция'
        verbose_name_plural = 'Роли'

    name = models.CharField(max_length=200, unique=True, verbose_name="Название роли")
    competences = models.ManyToManyField(Competence, related_name="competences", verbose_name="Компетенции", blank=True)

    def __str__(self):
        return self.name


class Interest(models.Model):
    class Meta:
        verbose_name = 'Интерес/Пожелание'
        verbose_name_plural = 'Интересы/Пожелания'

    name = models.CharField(max_length=300, unique=True, verbose_name="Название")

    def __str__(self):
        return self.name


class Student(models.Model):
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    name = models.CharField(max_length=150, unique=True, verbose_name="ФИО")
    current_module = models.ForeignKey(Module, related_name="current_modules", on_delete=models.SET_NULL,
                                       blank=True, null=True, verbose_name="Текущий модуль")
    role = models.OneToOneField(Role, related_name="current_role", on_delete=models.SET_NULL,
                                blank=True, null=True, verbose_name="Роль/Позиция")
    interests = models.ManyToManyField(Interest, related_name="interests", blank=True, verbose_name="Интересы")

    competences = models.ManyToManyField(Competence, through='StudentCompetence', verbose_name="Компетенции")

    def __str__(self):
        return self.name


class StudentCompetence(models.Model):
    class Meta:
        verbose_name = 'Студент-Компетенция'
        verbose_name_plural = 'Студент-Компетенция'

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    level = models.DecimalField(verbose_name="Уровень", max_digits=20, decimal_places=2)

    def __str__(self):
        return "%s - %s" % (self.student, self.competence)


class Content(models.Model):
    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'


class Evaluation(models.Model):
    class Meta:
        verbose_name = 'Оценивание'
        verbose_name_plural = 'Оценивания'

    name = models.CharField(max_length=200, unique=True, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    function = models.TextField(verbose_name="Функция")
    competence = models.ForeignKey(Competence, related_name="evaluated_competence", on_delete=models.CASCADE,
                                   blank=True, null=True, verbose_name="Оцениваемая компетенция")

    def __str__(self):
        return self.name
