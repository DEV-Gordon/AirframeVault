
# Models for the core app: aircraft, manufacturers, developers, roles, images, and videos.
from django.db import models
from django.utils.translation import gettext_lazy as _

class ManuFacturer(models.Model):
    """
    Represents an aircraft manufacturer.
    """
    name = models.CharField(max_length=255, unique=True, verbose_name="Name")
    website = models.URLField(blank=True, verbose_name="Official Website")

    class Meta:
        verbose_name = _("Manufacturer")
        verbose_name_plural = _("Manufacturers")

    def __str__(self):
        return self.name


class AircraftImage(models.Model):
    """
    Stores an image related to a specific aircraft type.
    """
    aircraft = models.ForeignKey('AircraftType', related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="aircraft/images/", verbose_name="Image")
    caption = models.CharField(max_length=140, blank=True, verbose_name="Caption")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Order")

    class Meta:
        verbose_name = _("Aircraft Image")
        verbose_name_plural = _("Aircraft Images")
        ordering = ["order"]

    def __str__(self):
        return f"{self.aircraft.name} - {self.caption or 'Image'}"


class AircraftVideo(models.Model):
    """
    Stores a video URL related to a specific aircraft type.
    """
    aircraft = models.ForeignKey('AircraftType', related_name="videos", on_delete=models.CASCADE)
    url = models.URLField(verbose_name="Video URL")
    title = models.CharField(max_length=140, blank=True, verbose_name="Title")
    provider = models.CharField(max_length=50, blank=True, verbose_name="Provider")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Order")

    class Meta:
        verbose_name = _("Aircraft Video")
        verbose_name_plural = _("Aircraft Videos")
        ordering = ["order"]

    def __str__(self):
        return f"{self.aircraft.name} - {self.title or self.url}"
    
class Developer(models.Model):
    """
    Represents a developer or publisher of a DCS module.
    """
    name = models.CharField(max_length=255, unique=True, verbose_name="Name")
    website = models.URLField(blank=True, verbose_name="Official Website")

    class Meta:
        verbose_name = _("Developer")
        verbose_name_plural = _("Developers")

    def __str__(self):
        return self.name

class Role(models.Model):
    """
    Represents a combat or operational role for an aircraft (e.g., Fighter, Trainer).
    """
    code = models.CharField(max_length=5, unique=True, verbose_name="Code", help_text="E.g. FI, AT, MR, HE, TR, SP")
    name = models.CharField(max_length=50, unique=True, verbose_name="Name")

    class Meta:
        verbose_name = _("Role")
        verbose_name_plural = _("Roles")
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"

class AircraftType(models.Model):
    """
    Main model for aircraft types in DCS World, including technical, operational, and developer info.
    """
    class OriginCountry(models.TextChoices):
        USA = 'US', _('United States')
        RUSSIA = 'RU', _('Russia / USSR')
        UK = 'UK', _('United Kingdom')
        FRANCE = 'FR', _('France')
        GERMANY = 'DE', _('Germany')
        ITALY = 'IT', _('Italy')
        SWEDEN = 'SE', _('Sweden')
        CHINA = 'CN', _('China')
        JAPAN = 'JP', _('Japan')
        SPAIN = 'ES', _('Spain')
        BRAZIL = 'BR', _('Brazil')
        INDIA = 'IN', _('India')
        CANADA = 'CA', _('Canada')
        ISRAEL = 'IL', _('Israel')
        TURKEY = 'TR', _('Turkey')
        MULTINATIONAL = 'MN', _('Multinational')

    class Era(models.TextChoices):
        WW2 = 'WW2', _('World War II')
        COLD_WAR = 'CW', _('Cold War')
        MODERN = 'MO', _('Modern')

    class FidelityLevel(models.TextChoices):
        FULL = 'FF', _('Full Fidelity (Clickable)')
        FC3 = 'FC', _('Flaming Cliffs (Simplified)')
        MOD = 'MD', _('Community Mod')

    # AircraftInfo fields
    # General aircraft identification and classification
    name = models.CharField(max_length=32, unique=True, verbose_name="Name")
    model_designation = models.CharField(max_length=32, blank=True, verbose_name="Model Designation", help_text="E.g. F-16C Block 50, MiG-29A, etc.")
    nickname = models.CharField(max_length=32, blank=True, verbose_name="Nickname", help_text="E.g. 'Viper' for F-16, 'Fulcrum' for MiG-29, etc.")
    country = models.CharField(max_length=2, choices=OriginCountry.choices, verbose_name="Country of Origin")
    era = models.CharField(max_length=3, choices=Era.choices, verbose_name="Era")
    roles = models.ManyToManyField(Role, related_name="aircraft_types", verbose_name="Roles", help_text="E.g. FI, AT, MR, HE, TR, SP")
    manufacturer = models.ForeignKey(ManuFacturer, on_delete=models.PROTECT, related_name="aircraft_types", verbose_name="Manufacturer")
    
    # DcsModuleInfo fields
    # Information about the DCS module implementation
    module_developers = models.ManyToManyField(Developer, related_name="aircraft_types", verbose_name="Developers")
    fidelity_level = models.CharField(max_length=2, choices=FidelityLevel.choices, verbose_name="Fidelity Level")
    flight_model = models.CharField(max_length=32, blank=True, verbose_name="Flight Model", help_text="E.g. 'Standard', 'Advanced', 'Realistic', etc.")
    is_flayable = models.BooleanField(default=True, verbose_name="Is Flyable", help_text="Indicates if the aircraft is currently flyable in DCS World.")
    carrier_capable = models.BooleanField(default=False, verbose_name="Carrier Capable", help_text="Indicates if the aircraft can operate from aircraft carriers.")
    
    # Technical specifications (optional, can be expanded later)
    crew = models.IntegerField(blank=True, null=True, verbose_name="Crew", help_text="Number of crew members (e.g. 1 for single-seat, 2 for tandem, etc.)")
    max_speed = models.CharField(max_length=32, blank=True, verbose_name="Max Speed", help_text="E.g. 'Mach 2.0', '1500 km/h', etc.")
    service_ceiling = models.CharField(max_length=32, blank=True, verbose_name="Service Ceiling", help_text="E.g. '50,000 ft', '15,000 m', etc.")
    range = models.CharField(max_length=32, blank=True, verbose_name="Range", help_text="E.g. '1,500 km', '800 nmi', etc.")
    climb_rate = models.CharField(max_length=32, blank=True, verbose_name="Climb Rate", help_text="E.g. '50,000 ft/min', '250 m/s', etc.")
    thrust_to_weight = models.CharField(max_length=32, blank=True, verbose_name="Thrust-to-Weight Ratio", help_text="E.g. '1.2', '0.9', etc.")
    empty_weight = models.CharField(max_length=32, blank=True, verbose_name="Empty Weight", help_text="E.g. '10,000 kg', '22,000 lbs', etc.")
    max_takeoff_weight = models.CharField(max_length=32, blank=True, verbose_name="Max Takeoff Weight", help_text="E.g. '20,000 kg', '44,000 lbs', etc.")
    engine = models.CharField(max_length=64, blank=True, verbose_name="Engine Type", help_text="E.g. 'Pratt & Whitney F100-PW-229', 'Saturn AL-31F', etc.")
    engine_count = models.IntegerField(blank=True, null=True, verbose_name="Engine Count", help_text="Number of engines (e.g. 1, 2, etc.)")
    
    # Avionics and systems (optional, can be expanded later)
    has_ejector_seat = models.BooleanField(default=False, verbose_name="Has Ejector Seat", help_text="Indicates if the aircraft is equipped with an ejector seat.")
    has_radar = models.BooleanField(default=False, verbose_name="Has Radar", help_text="Indicates if the aircraft is equipped with a radar system.")
    radar = models.CharField(max_length=64, blank=True, verbose_name="Radar System", help_text="E.g. 'AN/APG-68', 'N001 VEP', etc.")
    has_rwr = models.BooleanField(default=False, verbose_name="Has RWR", help_text="Indicates if the aircraft is equipped with a Radar Warning Receiver.")
    rwr = models.CharField(max_length=64, blank=True, verbose_name="RWR System", help_text="E.g. 'AN/ALR-56M', 'SPO-15', etc.")
    has_ecm = models.BooleanField(default=False, verbose_name="Has ECM", help_text="Indicates if the aircraft is equipped with Electronic Countermeasures.")
    ecm = models.CharField(max_length=64, blank=True, verbose_name="ECM System", help_text="E.g. 'AN/ALQ-131', 'Khibiny', etc.")
    has_datalink = models.BooleanField(default=False, verbose_name="Has Datalink", help_text="Indicates if the aircraft is equipped with a datalink system.")
    
    # Capabilities (optional, can be expanded later)
    air_to_air = models.BooleanField(default=False, verbose_name="Air-to-Air Capability", help_text="Indicates if the aircraft is capable of engaging in air-to-air combat.")
    air_to_ground = models.BooleanField(default=False, verbose_name="Air-to-Ground Capability", help_text="Indicates if the aircraft is capable of engaging in air-to-ground combat.")
    air_to_sea = models.BooleanField(default=False, verbose_name="Air-to-Sea Capability", help_text="Indicates if the aircraft is capable of engaging in air-to-sea combat.")
    reconnaissance = models.BooleanField(default=False, verbose_name="Reconnaissance Capability", help_text="Indicates if the aircraft is capable of performing reconnaissance missions.") 
    internal_canon = models.BooleanField(default=False, verbose_name="Internal Cannon", help_text="Indicates if the aircraft is equipped with an internal cannon.")
    hardpoint_count = models.IntegerField(blank=True, null=True, verbose_name="Hardpoint Count", help_text="Number of hardpoints available for weapons and equipment.")
    
    # Resources and media (optional, can be expanded later)
    image_url = models.URLField(blank=True, verbose_name="Image URL", help_text="URL to an image of the aircraft.")
    dcs_wiki_url = models.URLField(blank=True, verbose_name="DCS Wiki URL", help_text="URL to the aircraft's page on the hoggit Wiki.")
    chucks_guide_url = models.URLField(blank=True, verbose_name="Chuck's Guide URL", help_text="URL to the aircraft's page on Chuck's Guide.")
    offcial_manual_url = models.URLField(blank=True, verbose_name="Official Manual URL", help_text="URL to the official manual or documentation for the aircraft.")
    tutorial_video_url = models.URLField(blank=True, verbose_name="Tutorial Video URL", help_text="URL to a tutorial video for the aircraft.")

    class Meta:
        verbose_name = _("Aircraft Type")
        verbose_name_plural = _("Aircraft Types")

    def __str__(self):
        return self.name
