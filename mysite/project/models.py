from django.db import models

# Create your models here.
class Picture(models.Model):
	URL = models.CharField(max_length=1000)
	Verified = models.BooleanField()

class Dropzone(models.Model):
	DropzoneName = models.CharField(max_length=50)
	TheDescription = models.CharField(max_length=1000)
	pictureID = models.ForeignKey(Picture, blank=True, null=True)

class EventType(models.Model):
	EventTypeName = models.CharField(max_length=50)
	pictureID = models.ForeignKey(Picture, blank=True, null=True)

class Event(models.Model):
	EventTypeID = models.ForeignKey(EventType)
	DropzoneID = models.ForeignKey(Dropzone)
	EventName = models.CharField(max_length=50)
	TheDescription = models.CharField(max_length=1000)
	StartDate = models.DateTimeField('start date')
	EndDate = models.DateTimeField('end date')
	Spaces = models.IntegerField(default=0)

class JumpType(models.Model):
	JumpTypeName = models.CharField(max_length=50)
	pictureID = models.ForeignKey(Picture, blank=True, null=True)

class VideoResource(models.Model):
	URL = models.CharField(max_length=1000)
	Verified = models.BooleanField()

class Jump(models.Model):
	JumpTypeID = models.ForeignKey(JumpType)
	VideoResourceID = models.ForeignKey(VideoResource, blank=True, null=True)
	ShortDescription = models.CharField(max_length=100)
	TheDescription = models.CharField(max_length=1000)
	Notes = models.CharField(max_length=1000)
	JumpDate = models.DateTimeField('jump date')

class ProductType(models.Model):
	ProductName = models.CharField(max_length=50)
	TheDescription = models.CharField(max_length=1000)
	PictureID = models.ForeignKey(Picture, blank=True, null=True)

class Product(models.Model):
	ProductName = models.CharField(max_length=50)
	ProductTypeID = models.ForeignKey(ProductType)

class UserBookingEventProduct(models.Model):
	EventID = models.ForeignKey(Event)
	ProductID = models.ForeignKey(Product)

class UserProfile(models.Model):
	FirstName = models.CharField(max_length=50)
	LastName = models.CharField(max_length=50)

class UserBooking(models.Model):
	EventProductID = models.ForeignKey(UserBookingEventProduct)
	UserProfileID = models.ForeignKey(UserProfile)
	BookingDate = models.DateTimeField('booking date')

class UserJump(models.Model):
	UserProfileID = models.ForeignKey(UserProfile)
	JumpID = models.ForeignKey(Jump)
	JumpNumber = models.IntegerField()
	isOwner = models.BooleanField()