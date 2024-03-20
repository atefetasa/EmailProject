from django.db import models
from account_module.models import User

# first you should add background images and background colors to the database
# you should log in as superuser
# background images and background colors icons that I had added to the database are in the uploads folder in the root directory
# you can add background images in the predefined background images table in database.
# the values you can use as color_name attribute in BackgroundColor table are:
#ffccee
#ffcccc
#ddccff
#ccd9ff
#ffff80
#99ff99


class BackgroundColor(models.Model):
    color_name = models.CharField(max_length=7, null=False, blank=False, unique=True)
    color_image = models.ImageField(upload_to='background_colors_images', verbose_name='Background Color Images',
                                    null=False, blank=False, unique=True, db_index=True)

    def __str__(self):
        return self.color_name


class BackgroundImage(models.Model):
    image_name = models.CharField(max_length=30, null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='background_images', verbose_name='background image', null=True, blank=True)

    class Meta:
        verbose_name = 'Predefined Background Image'
        verbose_name_plural = 'Predefined Background Images'

    def __str__(self):
        return self.image_name


class SiteSettings(models.Model):
    icons_choices = [
        ("c", "colored"),
        ("bw", "black and white")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='siteSettings')
    header_background_color = models.ForeignKey(BackgroundColor, on_delete=models.SET_NULL, null=True, blank=True,
                                                default=None, related_name="header_background_color_settings")
    sidebar_background_color = models.ForeignKey(BackgroundColor, on_delete=models.SET_NULL, null=True, blank=True,
                                                 default=None, related_name="sidebar_background_color_settings")
    main_background_color = models.ForeignKey(BackgroundColor, on_delete=models.SET_NULL, null=True, blank=True,
                                              default=None, related_name="main_background_color_settings")
    icons_color = models.CharField(max_length=2, choices=icons_choices, default="c")
    background_image = models.ForeignKey(BackgroundImage, on_delete=models.SET_NULL,
                                         null=True, blank=True, default=None)

    def __str__(self):
        return self.user.username

    