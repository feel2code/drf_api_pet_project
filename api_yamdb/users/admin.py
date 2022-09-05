from django.contrib import admin

from reviews.models import Categories, Genres, Review, Title
from users.models import User

admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Genres)
admin.site.register(Review)
admin.site.register(Title)
