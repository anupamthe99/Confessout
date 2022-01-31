from django.contrib import admin

from Confession.views import Contact
from .models import Confession
from .models import Contact
# Register your models here.
admin.site.register(Confession)
admin.site.register(Contact)