__title__ = 'fobi_phonenumber.forms'
__author__ = 'James Fenwick <jfenwick@tecaz.com>'
__copyright__ = 'Copyright (c) 2016 Tecaz Ltd'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('PhoneNumberForm',)

from django import forms
from django.utils.translation import gettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme
from fobi.settings import DEFAULT_MAX_LENGTH

theme = get_theme(request=None, as_instance=True)

class PhoneNumberForm(forms.Form, BaseFormFieldPluginForm):
    """
    Form for ``PhoneNumberPlugin``.
    """
    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("help_text", ""),
        ("initial", ""),
        ("max_length", "255"),
        ("required", True),
        ("placeholder", ""),
    ]

    label = forms.CharField(
        label = _("Label"),
        required = True,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
        )
    name = forms.CharField(
        label = _("Name"),
        required = True,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
        )
    help_text = forms.CharField(
        label = _("Help text"),
        required = False,
        widget = forms.widgets.Textarea(attrs={'class': theme.form_element_html_class})
        )
    initial = forms.CharField(
        label = _("Initial"),
        required = False,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
        )
    max_length = forms.IntegerField(
        label = _("Max length"),
        required = True,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class}),
        initial = DEFAULT_MAX_LENGTH
        )
    required = forms.BooleanField(
        label = _("Required"),
        required = False,
        widget = forms.widgets.CheckboxInput(attrs={'class': theme.form_element_checkbox_html_class})
        )
    placeholder = forms.CharField(
        label = _("Placeholder"),
        required = False,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
        )
