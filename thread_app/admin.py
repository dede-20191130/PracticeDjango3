from django.contrib import admin

from thread_app import models


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
