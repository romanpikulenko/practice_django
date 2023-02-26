# -*- coding: utf-8 -*-
import datetime

from django import forms


class ContactForm(forms.Form):
    date_creation = forms.DateField(
        initial=datetime.date.today(), help_text="Заполнить форму только в настоящий момент"
    )
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=500)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    # так как форма это класс - поддерживает методы.
    def clean_date_creation(self):
        data = self.cleaned_data["date_creation"]
        if data < datetime.date.today():
            raise forms.ValidationError(("Форма не действительна, перейдите на сайт прострочена дата"))

        return data
