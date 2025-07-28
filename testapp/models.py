from django.db import models


class BogieDetails(models.Model):
    bogie_no = models.CharField(max_length=50)
    maker_year_built = models.CharField(max_length=100)
    incoming_div_and_date = models.CharField(max_length=100)
    deficit_components = models.CharField(max_length=255)
    date_of_ioh = models.DateField()


class BogieChecksheet(models.Model):
    bogie_frame_condition = models.CharField(max_length=100)
    bolster = models.CharField(max_length=100)
    bolster_suspension_bracket = models.CharField(max_length=100)
    lower_spring_seat = models.CharField(max_length=100)
    axle_guide = models.CharField(max_length=100)


class BMBCChecksheet(models.Model):
    cylinder_body = models.CharField(max_length=100)
    piston_trunnion = models.CharField(max_length=100)
    adjusting_tube = models.CharField(max_length=100)
    plunger_spring = models.CharField(max_length=100)


class FormData(models.Model):
    form_number = models.CharField(max_length=50)
    inspection_by = models.CharField(max_length=100)
    inspection_date = models.DateField()

    bogie_details = models.OneToOneField(BogieDetails, on_delete=models.CASCADE)
    bogie_checksheet = models.OneToOneField(BogieChecksheet, on_delete=models.CASCADE)
    bmbc_checksheet = models.OneToOneField(BMBCChecksheet, on_delete=models.CASCADE)

    def __str__(self):
        return self.form_number

