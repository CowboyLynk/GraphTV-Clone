from django.contrib import admin

# imports the models
from .models import Show, Season, Episode

"""
class WishListAdmin(admin.ModelAdmin):
	list_display = ['subject', 'course_id']

admin.site.register(Section, SectionAdmin)
admin.site.register(WishList, WishListAdmin)
"""

admin.site.register(Show)
admin.site.register(Season)
admin.site.register(Episode)
