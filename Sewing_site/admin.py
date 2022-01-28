from django.contrib import admin
from django.utils.safestring import mark_safe
from Sewing_site.models import Post, PostImage
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


class PostAdminForm(forms.ModelForm):
    text_of_post = forms.CharField(label = "Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'




class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src ={obj.image_for_post.url} width="100"  height = "120">')

    get_image.short_description = "Изображение"

class PostAdmin(admin.ModelAdmin):
    list_display = ("name_of_post", "date_of_post", "get_image")
    list_display_list = ("name_of_post")
    list_filter_list = ("date_of_post")
    search_fields = ("name_of_post", "date_of_post")
    inlines = [PostImageInline]
    form = PostAdminForm
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src ={obj.photo_of_preview_post.url} width="100"  height = "120">')

    get_image.short_description = "Изображение"


class PostImageAdmin(admin.ModelAdmin):
    list_display = ("post", "title", "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src ={obj.image_for_post.url} width="100"  height = "120">')

    get_image.short_description = "Изображение"


admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)


admin.site.site_title = "Клубок"
admin.site.site_header = "Клубок"
