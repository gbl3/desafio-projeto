#Arquivo models do app curso que eu criei
#rodar makemigrations
#depois, rodar o comando migrate
#python manage.py migrate/makemigrations
#add categoria e slug
#add curso

from django.db import models

class Category(models.Model):
    name = models.CharField('Name', max_length = 30)
    slug = models.SlugField('Slug', max_length = 40,unique = True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField('Name', max_length = 30)
    slug = models.SlugField('Slug', max_length = 40,unique = True)
    is_approved = models.BooleanField('Is Approved',default = False)
    category = models.ForeignKey('Category')
    date_start = models.DateField('Date', blank = True)
    description = models.CharField('Description',max_length = 100,blank = True)
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name
