
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.conf.global_settings import LANGUAGES


class IconTypeChoices(models.TextChoices):
    JPEG = "image/jpeg", _("JPEG/JPG")
    PNG = "image/png", _("PNG")
    SVG = "image/svg+xml", _("SVG")
    WEBP = "image/webp", _("WEBP")
    AVIF = "image/avif", _("AVIF")
    ICO = "image/vnd.microsoft.icon", _("ICO")


class IconColorSchemeChoices(models.TextChoices):
    LIGHT = "Light", _("Light Mode")
    DARK = "Dark", _("Dark Mode")


class IconPurposeChoices(models.TextChoices):
    MONOCHROME = "monochrome", _("monochrome")
    MASKABLE = "maskable", _("maskable")
    ANY = "any", _("any")


class Icons(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    icon = models.FileField(verbose_name=_("Icon"), upload_to="pwa/icons/")
    icon_type = models.CharField(
        max_length=25,  choices=IconTypeChoices.choices, verbose_name=_("Icon Type"))
    color_scheme = models.CharField(
        max_length=5, choices=IconColorSchemeChoices.choices, default="Light",
        verbose_name=_("Color Scheme"))
    sizes = models.CharField(
        max_length=250, default="any", verbose_name=_("Sizes"))
    purpose = models.CharField(
        max_length=10, choices=IconPurposeChoices.choices, default="any", verbose_name=_("Purpose"))

    class Meta:
        verbose_name = _("Icon")
        verbose_name_plural = _("Icons")

    def __str__(self) -> str:
        return f"{self.name} - {self.sizes}"


class DisplayChoices(models.TextChoices):
    FULLSCREEN = "fullscreen", _("fullscreen")
    STANDALONE = "standalone", _("standalone")
    MINIMAL_UI = "minimal-ui", _("minimal-ui")
    BROWSER = "browser", _("browser")


class OrientationChoices(models.TextChoices):
    ANY = "any", _("any")
    MATURAL = "natural", _("natural")
    LANDSCAPE = "landscape", _("landscape")
    LANDSCAPE_PRIMARY = "landscape-primary", _("landscape-primary")
    LANDSCAPE_SECONDARY = "landscape-secondary", _("landscape-secondary")
    PORTRAIT = "portrait", _("portrait")
    PORTRAIT_PRIMARY = "portrait-primary", _("portrait-primary")
    PORTRAIT_SECONDARY = "portrait-secondary", _("portrait-secondary")


class DirectionChoices(models.TextChoices):
    RTL = "rtl", _("Right to Left")
    LTR = "ltr", _("Left to Right")


class ManifestVersion(models.IntegerChoices):
    V1 = 1, _("Vertion 1")
    V2 = 2, _("Vertion 2")
    V3 = 3, _("Vertion 3")


class Permissions(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    permistion = models.CharField(
        max_length=150, verbose_name=_("Permistion Code"))

    class Meta:
        verbose_name = _("Permission")
        verbose_name_plural = _("Permissions")

    def __str__(self) -> str:
        return f"{self.name}"


class ProgressiveWebApplication(models.Model):
    site = models.OneToOneField(
        Site, on_delete=models.CASCADE, verbose_name=_("Site"), related_name="pwa_site")
    name = models.CharField(max_length=46, verbose_name=_("Name"))
    short_name = models.CharField(max_length=13, verbose_name=_("Short Name"))
    theme_color = models.CharField(max_length=9, verbose_name=_("Theme Color"))
    background_color = models.CharField(
        max_length=9, verbose_name=_("Background Color"))
    display = models.CharField(
        max_length=10, choices=DisplayChoices.choices, verbose_name=_("Display"))
    orientation = models.CharField(
        max_length=19, choices=OrientationChoices.choices, verbose_name=_("Orientation"))
    scope = models.SlugField(max_length=100, verbose_name=_("Scop"))
    start_url = models.SlugField(max_length=450, verbose_name=_("Start URL"))
    icons = models.ManyToManyField(
        Icons, verbose_name=_("Icons"), related_name="pwa_icons")
    direction = models.CharField(
        max_length=3, choices=DirectionChoices.choices, verbose_name=_("Direction"))
    lang = models.CharField(
        max_length=50, choices=LANGUAGES, verbose_name=_("Language"))
    description = models.TextField(verbose_name=_("Description"))
    version = models.CharField(
        max_length=15, default="1.0.0", verbose_name=_("Version"))
    manifest_version = models.PositiveSmallIntegerField(
        default=3, choices=ManifestVersion.choices, verbose_name=_("Manifest Version"))
    permissions = models.ManyToManyField(
        Permissions, verbose_name=_("Permissions"), related_name="pwa_permissions")
    author = models.CharField(max_length=150, verbose_name=_("Author"))

    on_site = CurrentSiteManager()

    class Meta:
        verbose_name = _("PWA")
        verbose_name_plural = _("PWAs")
        constraints = [
            models.UniqueConstraint(
                fields=['site', ], name="%(app_label)s_%(class)s_unique")
        ]

    def __str__(self) -> str:
        return f"{self.name} - {self.site.name}"
