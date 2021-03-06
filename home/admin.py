from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from home.models import BigSection, SubSection, Project, StepOneInterest
# Register your models here.
class BigSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    def description(self, obj):
        return obj.description
class SubSectionAdmin (admin.ModelAdmin):
    list_display = ('name', 'description')
    def description(self, obj):
        return obj.description
class ProjectAdmin (admin.ModelAdmin):
    list_display = ('name', 'description')
    def description(self, obj):
        return obj.description
class StepOneInterestAdmin(admin.ModelAdmin):
    list_display = ('user',)
  

    

admin.site.register(StepOneInterest, StepOneInterestAdmin,)
admin.site.register (BigSection, BigSectionAdmin)
admin.site.register (SubSection, SubSectionAdmin)
admin.site.register (Project, ProjectAdmin)