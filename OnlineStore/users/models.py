from django.db import models


class Feedback(models.Model):
    feedback_name = models.CharField(max_length=50, verbose_name='Customer name',)
    feedback_email = models.EmailField(verbose_name='Customer email',)
    feedback_message = models.TextField(verbose_name='Message',)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation',)

    class Meta:
        verbose_name = 'Customer Feedback'
        verbose_name_plural = 'Customer Feedback'

    def __str__(self):
        return self.feedback_message[:30]
