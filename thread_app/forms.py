from django.forms import ModelForm

from thread_app.models import Topic, Comment


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


class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'user_name',
            'message',
        ]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs['value'] = '名無し（必ず入力してください）'

    def save_with_topic(self, topic_id, commit=True):
        comment = self.save(commit=False)
        comment.topic = Topic.objects.get(id=topic_id)
        comment.no = Comment.objects.filter(topic_id=topic_id).count() + 1
        if commit:
            comment.save()
        return comment
