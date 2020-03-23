from django import forms
from QMS.models import EmployeeDetails, EmployePosition, EmployeDepartment
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset



class EmployeeDetailsform(forms.ModelForm):
        emp_code = forms.CharField(max_length=3,label='Employee Code') 
        emp_name = forms.CharField(max_length=50, label='Employee Name') 
        emp_department = forms.ModelChoiceField(queryset=EmployeDepartment.objects.all(),empty_label='Select') 
        emp_position = forms.ModelChoiceField(queryset=EmployePosition.objects.all(),empty_label='Select')
        emp_reporting_to = forms.CharField(max_length=50, label='Employee Reporting to') 
        emp_approved_by = forms.CharField(max_length=50, label='Employee Approved by') 
        emp_status = forms.CharField(max_length=50, label='Emplee Status') 

        def __init__(self, *args, **kwargs):
            super(EmployeeDetailsform, self).__init__(*args, **kwargs)
            self.fields['emp_department'].label_from_instance = lambda obj: "%s" % obj.department_name
            self.fields['emp_position'].label_from_instance = lambda obj: "%s" % obj.emp_posn
            self.helper = FormHelper()
            #self.helper.form_method = 'post'
            #self.helper.form_action = reverse('audittype_view.html')
            self.helper.label_class = 'col-lg-5'
            self.helper.field_class = 'col-lg-3'
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
            self.helper.form_class = 'form-horizontal'
            self.helper.layout = Layout(
                'emp_code',
                'emp_name',
                'emp_department',
                'emp_position',
                'emp_reporting_to',
                'emp_approved_by',
                'emp_status'
                )


        class Meta:
            """Meta Attributes"""
            model = EmployeeDetails
            fields = ['emp_code','emp_name','emp_department','emp_position','emp_reporting_to','emp_approved_by','emp_status']

                
            