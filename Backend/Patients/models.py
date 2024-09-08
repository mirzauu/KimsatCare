from django.db import models
from User.models import CustomUser
import uuid
# Create your models here.

class visitor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)  # Optional for patients
    phone_number = models.CharField(max_length=15, unique=True)
    # address = models.TextField(blank=True, null=True)
    # date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Patient {self.phone_number}"



class PatientProfile(models.Model):
    user = models.OneToOneField('visitor', on_delete=models.CASCADE, blank=True, null=True)  # Assuming 'visitor' is another model.
    MRD_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    # One-to-many relationship with LabReport
   
    def __str__(self):
        return f"Patient {self.MRD_number}"



class LabReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey('PatientProfile', on_delete=models.CASCADE, related_name='lab_reports')  # One-to-many relation
    report_file = models.FileField(upload_to='lab_reports/') 
    created_at = models.DateField(auto_now_add=True)  # Automatically set date when created

    def __str__(self):
        return f"Lab Report {self.id} for Patient {self.patient.MRD_number}"
    

    
    