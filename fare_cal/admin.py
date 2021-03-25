from django.contrib import admin
from .models import BoardingDetail, LineDetail


@admin.register(LineDetail)
class LineDetail_Admin(admin.ModelAdmin):
    list_display = ('line_color', 'line_charge', )


@admin.register(BoardingDetail)
class BoardingDetails_Admin(admin.ModelAdmin):
    list_display = ('boarding_name', 'boarding_id', 'is_terminal', 'is_interchange', 'is_bus',
                    'is_railway', 'is_shuttle', 'is_interchange_terminal')
