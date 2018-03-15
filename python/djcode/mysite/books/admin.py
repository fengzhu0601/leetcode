from django.contrib import admin
from books.models import Publisher, Author, Book

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)     ## 过滤器
    date_hierarchy = 'publication_date'     ## 筛选日期
    ordering = ('-publication_date',)       ## -降序排列
    # fields = ('title', 'authors', 'publisher')
    filter_horizontal = ('authors', )
    raw_id_fields = ('publisher',)


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
