from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from QMS.models import Auditschedule
from QMS.models import Audittype
from QMS.form.auditscheduleform import Auditscheduleform
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy  


# Auditschedule ListView
class AuditscheduleListview(ListView):
    model = Auditschedule
    template_name = 'superadmin/auditshedule_view.html'

    def get_context_data(self, **kwargs):
        auditschedule = self.model.objects.all().order_by('pk')
        obj = {'auditschedule':auditschedule}
        return obj


class AuditscheduleConfirmListview(UpdateView):
    model = Auditschedule

    template_name = 'superadmin/auditschedule_confirm.html'
    success_url = 'auditscheduleview'

    def get_context_data(self):

        auditschedule = self.model.objects.get(pk=self.kwargs['pk'])
        auditype = Audittype.objects.all()
        obj = {'auditschedule':auditschedule,'auditype':auditype}
        return obj


class AuditscheduleConfirmUpdate(UpdateView):
    model = Auditschedule
    form_class = Auditscheduleform
    success_url = 'QMS:auditscheduleview'
    template_name = 'superadmin/auditshedule_form.html'

    def get_success_url(self):
        return reverse_lazy(self.success_url)

    def form_valid(self, form):
        form = self.get_form()
        auditschedule = self.model.objects.get(pk=self.kwargs['pk'])
        Q1 = ['01','02','03']
        Q2 = ['04','05','06']
        Q3 = ['07','08','09']
        Q4 = ['10','11','12']
        ac = []
        # auditees = auditschedule.schedule_auditee_list.emp_name
        auditype = auditschedule.schedule_auditype.auditcode
        ad = auditschedule.schedule_audit_date
        auditdate = str(ad).split('-')
        ac.append(auditype)

        if auditdate[1] in Q1:
            ac.append('Q1')
        elif auditdate[1] in Q2:
            ac.append('Q2')
        elif auditdate[1] in Q3:
            ac.append('Q3')
        elif auditdate[1] in Q4:
            ac.append('Q4')
        ac.append(auditdate[0])

        ac.append(str(auditschedule.id))

        auditcode = '/'.join(ac)
        self.object.schedule_audit_code = auditcode
        self.object.save()
        form.save()
        return HttpResponseRedirect(self.get_success_url())


# Auditschedule CreateView
class AuditscheduleCreate(CreateView):

    model = Auditschedule
    form_class = Auditscheduleform
    success_url = reverse_lazy('QMS:auditscheduleview')
    template_name = 'superadmin/auditshedule_form.html'

    def get_success_url(self):
        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return str(self.success_url)  # success_url may be lazy

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        #import pdb
        #pdb.set_trace()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())
    

class AuditscheduleUpdate(UpdateView):
     model = Auditschedule
     form_class = Auditscheduleform
     success_url = 'QMS:auditscheduleview'
     template_name = 'superadmin/auditshedule_form.html'

     def get_success_url(self):
        return reverse_lazy(self.success_url)

     def form_valid(self, form):
        form = self.get_form()
        form.save()
        return HttpResponseRedirect(self.get_success_url())


#Auditschedule DeleteView
class AuditscheduleDelete(DeleteView):
    model = Auditschedule
    success_url = 'QMS:auditscheduleview'
    template_name = 'superadmin/auditschedule_confirm_delete.html'

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(AuditscheduleDelete, self).get_object()
        return obj

    def get_success_url(self):
        return reverse_lazy(self.success_url)