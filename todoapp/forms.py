from django import forms
from todoapp.models import ToDo


class TodoForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))

    class Meta:
        model = ToDo
        fields = ['content',]


class TodoUpdateForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))

    class Meta:
        model = ToDo
        fields = ['content',]

    def save(self, commit=True):
        todo_list = self.instance
        todo_list.content = self.cleaned_data['content']

        if commit:
            todo_list.save()
        return todo_list



