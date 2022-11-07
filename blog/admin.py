from django.contrib import admin
from blog.models import Sujet,Comment,Image, Article, Partenaire, Temoignage

#manage override of textfield
from django.db import models
from django.forms import Textarea


@admin.register(Sujet)
class SujetAdmin(admin.ModelAdmin):
    list_display = ('title','activite','published','created_at','comments_count','image')
    list_filter = ('activite__name','published',)

    def comments_count(self,obj):
        return Comment.objects.filter(sujet=obj).count()
    comments_count.short_description = 'Comments'

    #autocomplete_fields = ['activite']
    formfield_overrides = {
        models.TextField: {'widget':Textarea(attrs={'rows':20,'colrs':90})}
    }

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('sujet','author_name','status','text','moderation_text','created_at',)
    list_filter = ('status',)
    search_fields = ['author_name','sujet__title']
    list_editable = ('status','moderation_text',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'sujet')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'active','description','image')

@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('id','author', 'active','description','photo')

@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'active','image')