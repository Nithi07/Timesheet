from django import forms
from QMS.models import Audittype
from QMS.models import WorkManual
from QMS.models import ManualCheckList
from django.forms import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from QMS.custom_layout_object import Formset


class WorkManualform(forms.ModelForm):
    type = (
        ('Project','Project'),
        ('Tender','Tender')
        )
    audit_typ = forms.ModelChoiceField(queryset=Audittype.objects.all(),empty_label='Select')
    cls_ref_no = forms.CharField(max_length=10)
    activity_title = forms.CharField(max_length=100)
    ISO_certification_year = forms.IntegerField()
    type_of_projectortender = forms.CharField(max_length=10)

    def __init__(self, *args, **kwargs):
        super(WorkManualform, self).__init__(*args, **kwargs)
        self.fields['audit_typ'].label_from_instance = lambda obj: "%s" % obj.audittype
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        # self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Div(
                Field('audit_typ'),
                Field('cls_ref_no'),
                Field('activity_title'),
                Field('ISO_certification_year'),
                Field('type_of_projectortender'),
                # Fieldset('Add titles'),
                Field('checklist'),
                HTML("<br>"),
                Formset('activity'),
                ButtonHolder(Submit('submit', 'save')),
                )
            )

    class Meta:
        model = WorkManual
        fields = ['audit_typ','cls_ref_no','activity_title','ISO_certification_year','type_of_projectortender',
                  ]


class ManualCheckListForm(forms.ModelForm):

    class Meta:
        model = ManualCheckList
        widgets = {
            'checklist': forms.Textarea(attrs={'rows': 2, 'cols': 22}),
        }
        fields = ['checklist']


ManualCheckListFormSet = inlineformset_factory(WorkManual, ManualCheckList, form=ManualCheckListForm,extra=1, can_delete=True)

        





