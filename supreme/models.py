from django.db import models

# Home section
class Home(models.Model):
  name = models.CharField(max_length=20)
  greetings_1 = models.CharField(max_length=5)
  greetings_2 = models.CharField(max_length=5)
  picture = models.ImageField(upload_to='picture/')
  # save time when modified
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
  
# About Section
class About(models.Model):
  heading = models.CharField(max_length=50)
  career = models.CharField(max_length=20)
  description = models.TextField(blank=False)
  profile_img = models.ImageField(upload_to='profile/')
  # save time when modified
  updated = models.DateTimeField(auto_created=True)

  def __str__(self):
    return self.career
    

class Profile(models.Model):
  about = models.ForeignKey(About,
                            on_delete=models.CASCADE)
  social_name = models.CharField(max_length=10)
  link = models.URLField(max_length=200)



# Skills Section
class Category(models.Model):
  name = models.CharField(max_length=20)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'skill'
    verbose_name_plural = 'skills' 

  def __str__(self):
    return self.name
  
class Skills(models.Model):
  Category = models.ForeignKey(Category,
                               on_delete=models.CASCADE)
  skill_name = models.CharField(max_length=20)


# Portfolio Section
class Portfolio(models.Model):
  image = models.ImageField(upload_to='profile/')
  link = models.URLField(max_length=200)

  def __str__(self):
    return f'portfolio {self.id}'