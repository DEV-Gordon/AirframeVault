from django.contrib import admin
from django.utils.html import format_html
from .models import (
	ManuFacturer,
	Developer,
	Role,
	AircraftType,
	AircraftImage,
	AircraftVideo,
)


class AircraftImageInline(admin.TabularInline):
	"""
	Inline admin for displaying and editing AircraftImage objects within AircraftType admin.
	Shows image preview and allows ordering.
	"""
	model = AircraftImage
	extra = 1
	readonly_fields = ("preview",)
	fields = ("image", "caption", "order", "preview")

	def preview(self, obj):
		if obj and getattr(obj, "image", None):
			return format_html('<img src="{}" style="max-height:100px;" />', obj.image.url)
		return "-"
	preview.short_description = "Preview"


class AircraftVideoInline(admin.TabularInline):
	"""
	Inline admin for displaying and editing AircraftVideo objects within AircraftType admin.
	Shows clickable video links and allows ordering.
	"""
	model = AircraftVideo
	extra = 1
	readonly_fields = ("link",)
	fields = ("url", "title", "provider", "order", "link")

	def link(self, obj):
		if obj and obj.url:
			label = obj.title or obj.url
			return format_html('<a href="{}" target="_blank">{}</a>', obj.url, label)
		return "-"
	link.short_description = "Video"


@admin.register(AircraftType)
class AircraftTypeAdmin(admin.ModelAdmin):
	"""
	Admin configuration for AircraftType model.
	Includes inlines for images and videos, search, filters, and API view button.
	"""
	list_display = ("name", "manufacturer", "country", "era", "fidelity_level", "is_flayable", "first_image", "view_api")
	list_filter = ("manufacturer", "country", "era", "fidelity_level", "is_flayable")
	search_fields = ("name", "model_designation", "nickname")
	ordering = ("name",)
	inlines = [AircraftImageInline, AircraftVideoInline]

	def view_api(self, obj):
		"""Render a button that opens the API detail for this aircraft type."""
		# API endpoint: /api/aircraft-types/<pk>/
		url = f"/api/aircraft-types/{obj.pk}/"
		return format_html('<a class="button" href="{}" target="_blank">View API</a>', url)
	view_api.short_description = "API"
	view_api.allow_tags = True

	def first_image(self, obj):
		first = obj.images.first()
		if first and getattr(first, "image", None):
			return format_html('<img src="{}" style="max-height:60px;" />', first.image.url)
		return "-"
	first_image.short_description = "Image"


@admin.register(AircraftImage)
class AircraftImageAdmin(admin.ModelAdmin):
	"""
	Admin configuration for AircraftImage model.
	Shows thumbnails and allows inline editing of order and captions.
	"""
	list_display = ("aircraft", "caption", "order", "thumbnail")
	search_fields = ("aircraft__name", "caption")
	list_editable = ("order",)
	readonly_fields = ("thumbnail",)

	def thumbnail(self, obj):
		if obj and getattr(obj, "image", None):
			return format_html('<img src="{}" style="max-height:80px;" />', obj.image.url)
		return "-"
	thumbnail.short_description = "Thumbnail"


@admin.register(AircraftVideo)
class AircraftVideoAdmin(admin.ModelAdmin):
	"""
	Admin configuration for AircraftVideo model.
	Shows clickable video links and allows inline editing of order and titles.
	"""
	list_display = ("aircraft", "title", "provider", "order", "link")
	search_fields = ("aircraft__name", "title", "provider")
	list_editable = ("order",)
	readonly_fields = ("link",)

	def link(self, obj):
		if obj and obj.url:
			return format_html('<a href="{}" target="_blank">{}</a>', obj.url, obj.title or obj.url)
		return "-"
	link.short_description = "Video Link"


@admin.register(ManuFacturer)
class ManufacturerAdmin(admin.ModelAdmin):
	"""
	Admin configuration for ManuFacturer model.
	"""
	list_display = ("name", "website")
	search_fields = ("name",)


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
	"""
	Admin configuration for Developer model.
	"""
	list_display = ("name", "website")
	search_fields = ("name",)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	"""
	Admin configuration for Role model.
	"""
	list_display = ("code", "name")
	search_fields = ("code", "name")

