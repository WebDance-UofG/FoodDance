from django.contrib import admin

# Register your models here.
from .models import Recipe, Materials, RecipeStep


class materialsInline(admin.TabularInline):
    model = Materials
    fk_name = "recipe"

class recipeStepInline(admin.TabularInline):
    model = RecipeStep
    fk_name = "recipe"

class recipe(admin.ModelAdmin):
    list_display = ('title','image','author')
    readonly_fields = ('author','pub_date','slug','views','shares')
    inlines = [materialsInline, recipeStepInline]
    fieldsets = ((None,{'fields':('title','image','overview','duration','budget','difficulty')}),)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Recipe, recipe)