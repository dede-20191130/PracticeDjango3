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
