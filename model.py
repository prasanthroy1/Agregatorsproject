from django.db import models

class UploadedFile(models.Model):
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class CSVRow(models.Model):
    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    column1 = models.FloatField(null=True, blank=True)  # Adjust types based on expected data
    column2 = models.FloatField(null=True, blank=True)