from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by"
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price"),},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
    )

    ordering = ("name", "price", "bedrooms")

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "house_rules",
        "facilities",
        "city",
        "country",
    )

    search_fields = ("city", "^host__username")

    filter_horizontal = ("amenities", "facilities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ """

    pass
