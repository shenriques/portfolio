from django.db import models

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

''' ATTRIBUTES '''

class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]
	
    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    # true = key skills, false = coding skill
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name_plural = 'Tags'
        verbose_name = 'Tag'
    
    # provides another way to search uni notes
    name = models.CharField(max_length=200, blank=True, null=True) # e.g. 'php', 'class diagrams', 'web servers' etc 

    def __str__(self):
        return self.name

class Testimonial(models.Model):

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["name"]

    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    issued_by = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


''' USERS '''

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    # extends built in user model, hence OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # creates and stores avatars to folder named avatar in media files
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class ContactProfile(models.Model):
    
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]
    
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'

''' CONTENT '''

class UniNote(models.Model):

    class Meta:
        verbose_name_plural = 'Uni Notes'
        verbose_name = 'Uni Note'
        ordering = ["date"]

    date = models.DateTimeField(blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    year_of_study = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=500, blank=True, null=True)
    lecture_number = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(null=True, blank=True)

    # check if it has a slug before saving, if not
    def save(self, *args, **kwargs):
        if not self.id: # 1) 'if its a new object'
            self.slug = slugify(self.title) # 2) use lowercase / underscored title to create slug
        super(UniNote, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/uninote/{self.slug}"

class BlogPost(models.Model):

    class Meta:
        verbose_name_plural = 'Blog Posts'
        verbose_name = 'Blog Post'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    # lets you style the content how you want
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    # choose whether its visible on the page
    is_active = models.BooleanField(default=True)

    # check if it has a slug before saving, if not
    def save(self, *args, **kwargs):
        if not self.id: # 1) 'if its a new object'
            self.slug = slugify(self.title) # 2) use lowercase / underscored title to create slug
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

class PortfolioEntry(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Entries'
        verbose_name = 'Portfolio Entry'
        ordering = ["title"]
    date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(PortfolioEntry, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"