from django import forms


class TarefasForm(forms.Form):
    TarefaID = forms.IntegerField()
    #Nome = models.TextField(max_length=99)
    #horacomecada = models.DateField()
    #horafinalizada = models.DateField()
    #UserID = models.IntegerField(max_length=20)
    #ID_Projeto = models.IntegerField(max_length=20)
