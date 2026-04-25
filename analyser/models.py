from django.db import models
from django.contrib.auth.models import User


class ResumeResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255, default='Resume')
    overall_score = models.IntegerField()
    ats_score = models.IntegerField()
    experience_level = models.CharField(max_length=50)
    result_json = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.filename