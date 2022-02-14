from django.contrib import admin
from . import models

# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_text', 'image_tag')
admin.site.register(models.Banners, BannerAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=('title', 'image_tag')
admin.site.register(models.Service, ServiceAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'detail')
admin.site.register(models.Page, PageAdmin)

class FaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'ans')
admin.site.register(models.Faq, FaqAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'detail', 'send_time')
admin.site.register(models.Enquiry, EnquiryAdmin)