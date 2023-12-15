
from django.contrib import admin
from .models import Location, University, Asset

class LocationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('بيانات الاساسية ', {
            'fields': ('location_number', 'location_name', 'location_type', 'address', 'owner', 'phone_number', 'site_status', 'area')
        }),
        ('University Information', {
            'fields': ('university_number', 'university_name')
        }),
        ('Asset Information', {
            'fields': ('asset_number', 'barcode')
        }),
    )

class UniversityAdmin(admin.ModelAdmin):
    fieldsets = (
        ('University Information', {
            'fields': ('university_number', 'university_name', 'specialization', 'student_count', 'faculty_count', 'maintenance_required')
        }),
    )

class AssetAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Asset Information', {
            'fields': ('asset_number', 'asset_name', 'asset_type', 'asset_status', 'asset_quantity', 'asset_value', 'date_added', 'department', 'asset_admin')
        }),
    )

admin.site.register(Location, LocationAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Asset, AssetAdmin)

