from django.contrib import admin
from django.utils.safestring import mark_safe
from Sewing_site.models import Post, MasterClass
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


class PostAdminForm(forms.ModelForm):
    text_of_post = forms.CharField(label = "Текст поста", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class MasterClassForm(forms.ModelForm):
    text_of_master_class = forms.CharField(label = "Описание мастер-класса", widget=CKEditorUploadingWidget())

    class Meta:
        model = MasterClass
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    list_display = ("name_of_post", "date_of_post", "get_image",)
    list_filter = ("date_of_post",)
    search_fields = ("name_of_post", "date_of_post",)
    form = PostAdminForm
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src ={obj.photo_of_preview_post.url} width="100"  height = "120">')

    get_image.short_description = "Изображение"


class MasterClassAdmin(admin.ModelAdmin):
    list_display = ("title_of_master_class", "date_of_master_class", "get_image",)
    list_filter = ("date_of_master_class",)
    search_fields = ("title_of_master_class", "date_of_master_class",)
    form = MasterClassForm
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src ={obj.photo_of_preview_master_class.url} width="100"  height = "120">')

    get_image.short_description = "Изображение"


admin.site.register(Post, PostAdmin)
admin.site.register(MasterClass, MasterClassAdmin)


admin.site.site_title = "Клубок"
admin.site.site_header = "Клубок"
