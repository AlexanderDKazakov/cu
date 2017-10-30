# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class MessageForm(forms.Form):

    jmeno = forms.CharField()
    jmeno.label = 'Jmeno, prejmeni, titul'

    zakaz_chislo = forms.CharField()
    zakaz_chislo.label = 'Zakaz chislo'

    zakaz_chislo = forms.CharField()
    zakaz_chislo.label = 'Zakaz chislo'

    odmenyKc = forms.CharField()
    odmenyKc.label = 'Vyse odmeny v Kc'

    odmenySl = forms.CharField()
    odmenySl.label = 'Vyse odmeny slovne'

    total_work_time = forms.CharField()
    total_work_time.label = 'Total work time'

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'
    helper.layout = Layout(
        Field('jmeno', css_class='input-xlarge'),
        Field('zakaz_chislo', css_class='input-xlarge'),
        Field('odmenyKc', css_class='input-xlarge'),
        Field('odmenySl', css_class='input-xlarge'),
        Field('total_work_time', css_class='input-xlarge'),

        FormActions(
            Submit('save_changes', 'Get pdf', css_class="btn-primary"),
            # Submit('cancel', 'Cancel' ),
        )
    )