from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.

def upload_to(instance, filename):
    return 'courses/{filename}'.format(filename=filename)

#model for categories
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

#model for courses, where most of the information is stored
class Course(models.Model):
    USD = 'USD'
    GEL = 'GEL'
    EUR = 'EUR'
    CURRENCY_CHOICES = [
        (USD, 'USD'),
        (GEL, 'GEL'),
        (EUR, 'EUR'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='courses_created',
                              on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                                 related_name='courses',
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name='courses_joined',
                                      blank=True)
    price = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=3,
                                choices=CURRENCY_CHOICES,
                                default=USD,)
    image = models.ImageField(
        _("Image"), upload_to=upload_to, default='courses/default.jpg')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

#module for each course
class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.created}. {self.title}'

    class Meta:
        ordering = ['-created']

#model for course review
class Review(models.Model):
    #review model which has a foreignkey relationship with user and course
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='review', on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, blank=True)
    rating = models.IntegerField(default=1, choices=RATING)

    def __str__(self):
        return f'{self.user} {self.rating}'
