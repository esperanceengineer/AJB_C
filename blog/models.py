from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Article(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Temoignage(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Partenaire(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Sujet(models.Model):
    title = models.CharField(max_length=100)
    activite = models.ForeignKey('users.TypeActivte', on_delete=models.SET_NULL, related_name='sujets',null = True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    STATUS_VISIBLE = 'visible'
    STATUS_HIDDEN = 'hidden'
    STATUS_MODERATED = 'moderated'

    STATUS_CHOICES = (
        (STATUS_VISIBLE,'Visible'),
        (STATUS_HIDDEN,'Hidden'),
        (STATUS_MODERATED,'Moderated'),
    )

    sujet = models.ForeignKey('blog.Sujet',on_delete=models.CASCADE,related_name='comments')
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    status = models.CharField(default=STATUS_VISIBLE,max_length=20,choices=STATUS_CHOICES)
    moderation_text= models.CharField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '{} {} (status={})'.format(self.author_name,self.text[:20],self.status)

class Image(models.Model):
    image = models.ImageField(upload_to=upload_to)
    sujet = models.ForeignKey('blog.Sujet', on_delete=models.CASCADE, related_name='images')
