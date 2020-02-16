from django.forms import ModelForm

from thread_app.models import Topic


class TopicCreateForm(ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title',
            'user_name',
            'category',
            'message',
        ]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '：')
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = '選択してください。'
        self.fields['user_name'].widget.attrs['value'] = '山田太郎'
