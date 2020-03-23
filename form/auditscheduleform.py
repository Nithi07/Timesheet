from django import forms
from QMS.models import Auditschedule
from QMS.models import ListAuditors
from QMS.models import Audittype
from QMS.models import EmployeeDetails 
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset


   
class Auditscheduleform(forms.ModelForm):
    schedule_auditype = forms.ModelChoiceField(queryset=Audittype.objects.all(),empty_label='Select')
    schedule_auditor_list = forms.ModelMultipleChoiceField(queryset=ListAuditors.objects.all())
    schedule_auditee_list = forms.ModelMultipleChoiceField(queryset=EmployeeDetails.objects.all())
    schedule_job_code = forms.CharField(max_length=15)
    schedule_sub_job_code = forms.CharField(max_length=15)
    schedule_audit_date = forms.DateField()
    schedule_audit_time = forms.TimeField()
    schedule_iso_year = forms.IntegerField()
    schedule_final_auditor_list  = forms.ModelMultipleChoiceField(queryset=ListAuditors.objects.all())

   

    
    def __init__(self, *args, **kwargs):
        super(Auditscheduleform, self).__init__(*args, **kwargs)
        self.fields['schedule_auditype'].label_from_instance = lambda obj: "%s" % obj.audittype
        self.fields['schedule_auditor_list'].label_from_instance = lambda obj: "%s" % obj.auditors.emp_name
        self.fields['schedule_auditee_list'].label_from_instance = lambda obj: "%s" % obj.emp_name
        self.fields['schedule_final_auditor_list'].label_from_instance = lambda obj: "%s" % obj.auditors.emp_name
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        #self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            ('schedule_auditype'),
            ('schedule_job_code'),
            ('schedule_sub_job_code'),
            ('schedule_audit_date'),
            ('schedule_audit_time'),
            ('schedule_auditee_list'),
            ('schedule_auditor_list'),
            ('schedule_iso_year'),
            ('schedule_final_auditor_list'),
            )

    class Meta:
        model = Auditschedule
        fields = ['schedule_auditype','schedule_job_code','schedule_sub_job_code','schedule_audit_date','schedule_audit_time',
                  'schedule_auditee_list','schedule_auditor_list','schedule_iso_year','schedule_final_auditor_list']
        





