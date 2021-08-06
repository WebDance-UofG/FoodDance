from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.template.defaultfilters import slugify


# Create your models here.


class Recipe(models.Model):
    """
    The main content of recipes.
    """
    TITLE_MAX_LENGTH = 50
    OVERVIEW_MAX_LENGTH = 500

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    image = models.ImageField(upload_to='recipes')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    overview = models.CharField(max_length=OVERVIEW_MAX_LENGTH)
    duration = models.IntegerField()
    budget = models.IntegerField()
    # difficulty is  0-5
    difficulty = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    pub_date = models.DateField()
    slug = models.SlugField(unique=True)

    views = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        import datetime
        self.pub_date = datetime.date.today()
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug


class Materials(models.Model):
    """
    The materials(ingredients) of recipes.
    """
    INGREDIENT_MAX_LENGTH = 128
    WEIGHT_MAX_LENGTH = 128

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=INGREDIENT_MAX_LENGTH)
    weight = models.CharField(max_length=WEIGHT_MAX_LENGTH)

    def __str__(self):
        return self.ingredient


class RecipeStep(models.Model):
    """
    The cool steps of recipes.
    """
    CONTENT_MAX_LENGTH = 2000

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    index = models.IntegerField()
    image = models.ImageField(upload_to='recipes', blank=True)
    content = models.CharField(max_length=CONTENT_MAX_LENGTH)

    def save(self, *args, **kwargs):
        if not self.index or self.index == 0:
            self.index = RecipeStep.objects.filter(recipe=self.recipe).count() + 1
        super(RecipeStep, self).save(*args, **kwargs)

    def __str__(self):
        return self.recipe.slug + "-" + str(self.index)


class Comment(models.Model):
    """
    Comments of recipes
    """
    COMMENT_MAX_LENGTH = 500
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    content = models.CharField(max_length=COMMENT_MAX_LENGTH, default="")
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + " - rating:" + str(self.rating)


class UserProfile(models.Model):
    """
    The profile of a user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', blank=True)
    introduction = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)

    collections = models.ManyToManyField(Recipe, related_name="user_collections")

    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class ConfirmString(models.Model):
    """
    The confirmation code of a unconfirmed user
    """
    code = models.CharField(max_length=256)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    creat_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user.username + ":   " + self.code

    class Meta:
        ordering = ["-creat_time"]
        verbose_name = "Confirm code"



