from django import forms
from .models import Visitor, Delivery, Child, StaffAttendance, SocietyNotice

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = "__all__"


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = "__all__"


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = "__all__"


class StaffAttendanceForm(forms.ModelForm):
    class Meta:
        model = StaffAttendance
        fields = "__all__"


class NoticeForm(forms.ModelForm):
    class Meta:
        model = SocietyNotice
        fields = "__all__"