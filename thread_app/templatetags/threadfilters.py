from django.template import Library

register = Library()


@register.filter
def comment_filter(text):
    return '<br>'.join(list(map(convert_url, text.split('\n'))))


def convert_url(text_line):
    """
    URLリンク行をaタグ付きの行に変換
    """
    if 'https://' in text_line or 'http://' in text_line:
        return '<a href="' + text_line + '" target="_blank" rel="noopener noreferrer">' + text_line + '</a>'
    else:
        return text_line
