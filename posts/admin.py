from django.contrib import admin

from .models import Post, PostFile, Commet, Like

# Register your models here.



class PostFileInLineAdmin(admin.StackedInline):

    
    model = PostFile
    fields = ('file', )
    extra = 0 
    # can_delete = False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['title','user','is_active','created_time']
    inlines = [PostFileInLineAdmin]  
    # actions = None
    
    # def has_delete_permission(self):
        
    #     return False
    
    # def has_add_permission(self):
        
    #     return False                    



# @admin.register(PostFile)
# class PostFileAdmin(admin.ModelAdmin):
#     pass
 
 
@admin.register(Commet)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'is_approved')
    list_filter = ('is_approved',)
    date_hierarchy = 'created_time'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'is_liked')
    list_filter = ('is_liked',)
    date_hierarchy = 'created_time'