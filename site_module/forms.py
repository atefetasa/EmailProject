from .models import SiteSettings
from django import forms
from .models import BackgroundColor, BackgroundImage
from django.utils.safestring import mark_safe


class CustomChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        if hasattr(obj, 'color_image'):
            return mark_safe("<img src='%s' alt='%s'/>" % (obj.color_image.url, obj.color_name))
        elif hasattr(obj, 'image'):
            return mark_safe("<img src='%s' alt='%s'/>" % (obj.image.url, obj.image_name))


class SiteSettingsForm(forms.Form):
    header_background_color = CustomChoiceField(queryset=BackgroundColor.objects.all(),
                                                widget=forms.RadioSelect,
                                                blank=False, )
    sidebar_background_color = CustomChoiceField(queryset=BackgroundColor.objects.all(),
                                                 widget=forms.RadioSelect,
                                                 blank=False,
                                                 )
    main_background_color = CustomChoiceField(queryset=BackgroundColor.objects.all(),
                                              widget=forms.RadioSelect,
                                              blank=False,
                                              label="Main section background color"
                                              )
    icons_color = forms.ChoiceField(choices=SiteSettings.icons_choices,
                                    widget=forms.RadioSelect)
    background_image = CustomChoiceField(queryset=BackgroundImage.objects.all(),
                                         widget=forms.RadioSelect,
                                         empty_label="No background image",
                                         blank=True,
                                         )
