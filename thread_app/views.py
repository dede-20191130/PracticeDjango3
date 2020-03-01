from django.core.mail import send_mail, EmailMessage
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, CreateView, ListView

from thread_app.forms import TopicCreateForm, CommentModelForm
from thread_app.models import Topic, Category, Comment


# class TopicDetailView(DetailView):
#     template_name = 'thread/detail_topic.html'
#     model = Topic
#     context_object_name = 'topic'


class TopicCreateView(CreateView):
    template_name = 'thread/create_topic.html'
    form_class = TopicCreateForm
    model = Topic
    success_url = reverse_lazy('base:top')

    def form_valid(self, form):
        ctx = {'form': form}
        if self.request.POST.get('next', '') == 'confirm':
            return render(self.request, 'thread/confirm_topic.html', ctx)
        if self.request.POST.get('next', '') == 'back':
            return render(self.request, 'thread/create_topic.html', ctx)
        if self.request.POST.get('next', '') == 'create':
            # メール送信処理
            template = get_template('thread/mail/topic_mail.html')
            mail_ctx = {
                'title': form.data['title'],
                'user_name': form.data['user_name'],
                'message': form.data['message'],
            }
            EmailMessage(
                subject='トピック作成: ' + form.data['title'],
                body=template.render(mail_ctx),
                from_email='hogehoge@example.com',
                to=['admin@example.com'],
                cc=['admin2@example.com'],
                bcc=['admin3@example.com'],
            ).send()

            # send_mail(
            #     subject='トピック作成: ' + form.data['title'],
            #     message=template.render(mail_ctx),
            #     from_email='hogehoge@example.com',
            #     recipient_list=[
            #         'admin@example.com',
            #     ]
            # )

            return super().form_valid(form)
        else:
            # 正常動作ではここは通らない。エラーページへの遷移でも良い
            return redirect(reverse_lazy('base:top'))


# class TopicFormView(FormView):
#     template_name = 'thread/create_topic.html'
#     form_class = TopicCreateForm
#     success_url = reverse_lazy('base:top')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# def topic_create(request):
#     template_name = 'thread/create_topic.html'
#     ctx = {}
#     if request.method == 'GET':
#         ctx['form'] = TopicCreateForm()
#         return render(request, template_name, ctx)
#
#     if request.method == 'POST':
#         topic_form = TopicCreateForm(request.POST)
#         if topic_form.is_valid():
#             topic_form.save()
#             return redirect(reverse_lazy('base:top'))
#         else:
#             ctx['form'] = topic_form
#             return render(request, template_name, ctx)


class CategoryView(ListView):
    template_name = 'thread/category.html'
    context_object_name = 'topic_list'
    paginate_by = 2
    page_kwarg = 'p'

    def get_queryset(self):
        return Topic.objects.filter(category__url_code=self.kwargs['url_code'])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category'] = get_object_or_404(Category, url_code=self.kwargs['url_code'])
        return ctx


class TopicAndCommentView(FormView):
    template_name = 'thread/detail_topic.html'
    form_class = CommentModelForm

    def form_valid(self, form):
        # comment = form.save(commit=False)  # 保存せずオブジェクト生成する
        # comment.topic = Topic.objects.get(id=self.kwargs['pk'])
        # comment.no = Comment.objects.filter(topic=self.kwargs['pk']).count() + 1
        # comment.save()
        form.save_with_topic(self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('thread:topic', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self):
        ctx = super().get_context_data()
        ctx['topic'] = Topic.objects.get(id=self.kwargs['pk'])
        ctx['comment_list'] = Comment.objects.filter(
            topic_id=self.kwargs['pk']).annotate(vote_count=Count('vote')).order_by('no')
        return ctx
