from django.contrib import admin

from .models import Picture, Dropzone, EventType, Event, JumpType, VideoResource, Jump, ProductType, UserBookingEventProduct, UserProfile, UserBooking, UserJump
# Register your models here.
admin.site.register(Picture)
admin.site.register(Dropzone)
admin.site.register(EventType)
admin.site.register(Event)
admin.site.register(JumpType)
admin.site.register(VideoResource)
admin.site.register(Jump)
admin.site.register(ProductType)
admin.site.register(UserBookingEventProduct)
admin.site.register(UserProfile)
admin.site.register(UserBooking)
admin.site.register(UserJump)