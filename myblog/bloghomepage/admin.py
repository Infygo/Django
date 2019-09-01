from django.contrib import admin
from .models import Content, Cities, MoviesSeries, Sports, Thoughts

# Register your models here.

admin.site.register(Content)
admin.site.register(Cities)
admin.site.register(MoviesSeries)
admin.site.register(Sports)
admin.site.register(Thoughts)

