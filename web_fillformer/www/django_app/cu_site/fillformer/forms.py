# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class MessageForm(forms.Form):

    # jmeno = forms.CharField(initial='Alexander Kazakov')
    jmeno = forms.CharField()
    jmeno.label = 'Jméno, příjmení, titul:'

    # zakaz_chislo1 = forms.CharField(initial='1234')
    zakaz_chislo1 = forms.CharField()
    zakaz_chislo1.label = 'Zakázka číslo:'

    # zakaz_chislo2 = forms.CharField(initial='123')
    zakaz_chislo2 = forms.CharField()
    zakaz_chislo2.label = '&zwnj;'

    # zakaz_chislo3 = forms.CharField(initial='123456')
    zakaz_chislo3 = forms.CharField()
    zakaz_chislo3.label = '&zwnj;'

    # odmenyKc = forms.CharField(initial='1 000')
    odmenyKc = forms.CharField()
    odmenyKc.label = 'Výše odměny v Kč:'

    # odmenySl = forms.CharField(initial='a lot of money')
    odmenySl = forms.CharField()
    odmenySl.label = 'Výše odměny slovně:'

    actions = forms.CharField(
        widget=forms.Textarea(),
        initial='preparing simulation script, simulation and getting result, '
                'review scripts and result, analyse result and factors, redo functions and scripts, '
                'analyse result, drinking a coffee, writing new scripts, eating, googling, reading',
    )
    actions.label = 'Action that you did'

    # date_field = forms.DateField(
    #     widget=forms.TextInput(
    #         attrs={'type': 'date'}
    #     )
    # )
    # date_field = forms.CharField(initial='02, 2017')
    date_field = forms.CharField()
    date_field.label = 'Month and year of date'

    # date_field_except = forms.CharField(initial='1, 2, 3, 4, 5')
    date_field_except = forms.CharField()
    date_field_except.label = 'Number of excepted days'

    # total_work_time = forms.CharField(initial='32')
    total_work_time = forms.CharField()
    total_work_time.label = 'Total work time'

    decision = forms.CharField(initial='No')
    # total_work_time = forms.CharField()
    decision.label = 'Need to sign a Head of department?'

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Field('date_field', css_class='input-xlarge', placeholder='MM, YYYY'),
        Field('date_field_except', css_class='input-xlarge', placeholder='1, 2, 3, 4'),
        Field('jmeno', css_class='input-xlarge', placeholder='Name and surname'),
        Div(
            Div(
                Field('zakaz_chislo1', placeholder='XXXX'),
                css_class='large-4 medium-4 cell'
            ),
            Div(
                Field('zakaz_chislo2', placeholder='XXX'),
                css_class='large-4 medium-4 cell'
            ),
            Div(
                Field('zakaz_chislo3', placeholder='XXXXXX'),
                css_class='large-4 medium-4 cell'
            ),
            css_class='grid-x grid-padding-x'
        ),
        Field('odmenyKc', css_class='input-xlarge', placeholder='1 000'),
        Field('odmenySl', css_class='input-xlarge', placeholder='one thousand'),
        Field('actions', rows="8", css_class='input-xlarge'),
        Field('decision', css_class='input-xlarge', placeholder='Yes/No'),
        Field('total_work_time', css_class='input-xlarge', placeholder='5'),

        FormActions(
            Submit('save_changes', 'Get pdf', css_class="btn-primary"),
        )
    )
