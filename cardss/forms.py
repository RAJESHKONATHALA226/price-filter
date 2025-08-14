from django import forms

RCHOICES = (
    ("low", "low"),
    ("high", "high"),

)
class choiceform(forms.Form):
    choicefile=forms.ChoiceField(choices=RCHOICES,
    widget=forms.Select(attrs={'onchange':'this.form.submit()'})
    )
