from django.contrib import admin
from cms.models import Book, Impression

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'price',)
    list_display_links = ('id', 'name',)  #상세보기로 넘어갈 것인지 말것인지

class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)  #상세보기로 넘어갈 것인지 말것인지
    raw_id_fields = ('book',)

admin.site.register(Book, BookAdmin)
admin.site.register(Impression, ImpressionAdmin)
