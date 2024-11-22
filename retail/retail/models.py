from django.db import models

class SQLUpload(models.Model):
    file = models.FileField(upload_to='sql_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
