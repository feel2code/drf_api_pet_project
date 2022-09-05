from django.contrib import admin
from users.models import User
from reviews.models import Categories, Genres, Review, Title

admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Genres)
admin.site.register(Review)
admin.site.register(Title)
