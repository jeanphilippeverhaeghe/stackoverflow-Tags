from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Index
    """
    return render(request, 'index.html')

from .forms import SaisieQuestionForm

def saisie_question(request):

    form = SaisieQuestionForm(request.POST or None)

    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        ma_question = form.cleaned_data['Ma_Question']
        nb_tags = form.cleaned_data['Nb_Tags']

        print ("ma_question: " , ma_question)

        from . import sof_tags_creator
        pred , comment_pred = sof_tags_creator.tagme(ma_question, nb_tags = nb_tags)

        form.fields['Prediction'].label="Proposition de tags: " + str(pred)
        form.fields['Comment_Prediction'].label="Commentaire sur la proposition de tags: " + comment_pred

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'saisie_question.html', locals())
