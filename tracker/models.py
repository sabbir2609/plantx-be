from django.db import models


class TrackLinks(models.Model):
    link = models.URLField(max_length=200)
    visit_time = models.DateTimeField(auto_now_add=True)
    referrer = models.CharField(max_length=200, null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name_plural = "Track Links"
        verbose_name = "Track Link"
