from django.db import models
from QMS.models import Audittype


class WorkManual(models.Model):
	type = (
		('Project', 'Project'),
		('Tender', 'Tender')
	)
	audit_typ = models.ForeignKey(Audittype,related_name='audit_typ',on_delete=models.CASCADE)
	cls_ref_no = models.CharField(max_length=10)
	activity_title = models.CharField(max_length=100)
	ISO_certification_year = models.IntegerField()
	type_of_projectortender = models.CharField(max_length=10)
	explain_of_activity = models.TextField()

	class Meta:

		db_table = 'work_manual'


class ManualCheckList(models.Model):
	workmanual = models.ForeignKey(WorkManual, related_name='workmanual', on_delete=models.CASCADE)
	checklist = models.TextField()
	class Meta:

		db_table = 'work_manual_checklist'