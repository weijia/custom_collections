from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from models import CollectionItem


class CollectionItemAdmin(GuardedModelAdmin):
    pass

admin.site.register(CollectionItem, CollectionItemAdmin)