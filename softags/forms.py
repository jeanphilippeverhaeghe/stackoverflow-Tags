from django import forms

class SaisieQuestionForm(forms.Form):
    Ma_Question = forms.CharField(label = "Question Stackoverflow", widget = forms.Textarea)
    Nb_Tags = forms.IntegerField(label = "Nombre de Tags souhaités", initial = 10, min_value=1, max_value=30)

    Prediction = forms.BooleanField(label = "Proposition de tags ", required = False, disabled= True)
    Comment_Prediction = forms.BooleanField(label = "Commentaire sur la proposition de tags ", required = False, disabled= True)
    def __str__(self):
        return self.titre
