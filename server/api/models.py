from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, RegexValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    title = models.CharField(max_length=64, unique=True)

    # Note that max_length for TextField is not enforced at database level,
    # it is just used to set form field length

    # blank=True and null=True are often seen together as blank sets whether a
    # value is required in a form, and null allows NULL on the database column
    description = models.TextField(max_length=256, blank=True, null=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    slug = models.SlugField(null=False, unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # We will use dynamic slugs when routing, so they are updateable
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Board(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    '''
        updated the title not to be unique
        '''
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('project', 'title')


class List(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    position = models.PositiveIntegerField()  # >= 0

    class Meta:
        unique_together = ('board', 'title')

    def __str__(self):
        return self.title


class Task(models.Model):
    # We will see what _() means later; do not worry if you used hardcoded
    # strings for now
    class Priority(models.TextChoices):
        HIGH = 'H', _('High')
        MEDIUM = 'M', _('Medium')
        LOW = 'L', _('Low')

    def validate_story_points(value):
        if value % 5 != 0 or value > 100:
            raise ValidationError(
                _('%(value)s is not a valid story point value'),
                params={'value': value})

    # Django automatically creates a primary key for you, but it is good to
    # know how to create your own
    task_no = models.AutoField(primary_key=True)

    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=512, blank=True, null=True)
    priority = models.CharField(max_length=1, choices=Priority)
    story_points = models.PositiveIntegerField(
        validators=[validate_story_points])

    # Lazy resolution uses strings for models that do not yet exist:
    labels = models.ManyToManyField('Label', blank=True)

    def __str__(self):
        return self.title


class Label(models.Model):
    title = models.CharField(max_length=32)
    colour = models.CharField(max_length=7, validators=[
                              RegexValidator('#[0-9A-F]{6}')])
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
