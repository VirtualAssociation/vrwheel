from django import forms

xp_types = (
    ('VR', 'VR'),
    ('AR', 'AR'),
    ('Other', 'Other')
)

stuffs = (
    ('Oculus Rift DK1', 'Oculus Rift DK1'),
    ('Oculus Rift DK2', 'Oculus Rift DK2'),
    ('HTC Vive', 'HTC Vive'),
    ('Gear VR', 'Gear VR'),
    ('Razer Hydra', 'Razer Hydra'),
    ('STEM', 'STEM')
)

class ProjectSubmitForm(forms.Form):
    name = forms.CharField(label='Project Name', max_length=200, required=True)
    url = forms.URLField(label='Project URL', initial='http://')
    xp_type = forms.ChoiceField(label='Experience Type', choices=xp_types)
    desc = forms.CharField(label='Project Description', widget=forms.Textarea, max_length=500, required=True)
    creator = forms.CharField(label='Creator', max_length=200, required=True)
    creator_url = forms.URLField(label='Creator URL', initial='http://')
    creation_date = forms.DateField(label='Created on')
    stuff = forms.MultipleChoiceField(label='Stuff needed', choices=stuffs)
    # image = forms.ImageField(label='Image')