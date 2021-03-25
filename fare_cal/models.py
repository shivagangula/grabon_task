from django.db import models


class LineDetail(models.Model):
    line_color = models.CharField(max_length=10)
    line_charge = models.FloatField()

    def __str__(self):
        return self.line_color


class BoardingDetail(models.Model):
    boarding_name = models.CharField(max_length=20)
    line_details = models.ForeignKey("LineDetail", on_delete=models.CASCADE,)
    boarding_id = models.CharField(max_length=20)
    is_terminal = models.BooleanField(default=False)
    is_interchange = models.BooleanField(default=False)
    is_bus = models.BooleanField(default=False)
    is_railway = models.BooleanField(default=False)
    is_shuttle = models.BooleanField(default=False)
    is_interchange_terminal = models.BooleanField(default=False)

    def __str__(self):
        return self.boarding_name
