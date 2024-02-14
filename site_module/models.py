from django.db import models
from account_module.models import User


class SiteSettings(models.Model):
    background_color_choices = [
        ("#ffffcc", "light lime"),
        ("#ddccff", "light purple"),
        ("#cce0ff", "light ocean blue"),
        ("#ccf5ff", "light sky blue"),
        ("#ffcccc", "light red"),
        ("white", "white"),
        ("#f3ccff", "pink purple")
    ]
    icons_choices = [
        ("c", "colored"),
        ("bw", "black and white")
    ]
    background_image_choices = [
        ("images/background_pictures/bg_no1.jpg", "background 1"),
        ("images/background_pictures/bg_no2.jpg", "background 2"),
        ("images/background_pictures/bg_no3.jpg", "background 3"),
        ("images/background_pictures/bg_no4.jpg", "background 4"),
        ("images/background_pictures/bg_no5.jpg", "background 5"),
        ("images/background_pictures/bg_no6.jpg", "background 6"),
        ("images/background_pictures/bg_no7.jpg", "background 7")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='siteSettings')
    header_background_color = models.CharField(max_length=7,
                                               choices=background_color_choices,
                                               default="#f3ccff",
                                               blank=True
                                               )
    sidebar_background_color = models.CharField(max_length=7,
                                                choices=background_color_choices,
                                                default="white",
                                                blank=True
                                                )
    main_background_color = models.CharField(max_length=7,
                                             choices=background_color_choices,
                                             default="white",
                                             blank=True
                                             )
    icons_color = models.CharField(max_length=2, choices=icons_choices, default="c", blank=True)
    background_image = models.CharField(max_length=40,
                                        choices=background_image_choices,
                                        null=True,
                                        blank=True,
                                        default=None
                                        )

    def __str__(self):
        return self

    