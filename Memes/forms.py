from django.forms import ModelForm
from .models import Comment, Vote


# Vote Form
class VoteForm(ModelForm):
    '''
    Vote form. \n
    model = Model name \n
    fields = ['field_name'] or '__all__' if we want to get all fields. \n
    labels = {'field_name' : 'custom label'} -> if want to use custom label. \n

    We can style our form with CSS classes in for loop.
    '''
    class Meta:
        model = Vote
        fields = ['vote']

    # if we want to change the labels we can use this
    labels = {
        'vote' : 'Place your vote'
    }

    def __init__(self, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class' : 'CLASS_NAME'})



# Comment Form
class CommentForm(ModelForm):
    '''
    Comment form.
    model = Model name \n
    fields = ['field_name'] or '__all__' if we want to get all fields. \n
    labels = {'field_name' : 'custom label'} -> if want to use custom label. \n

    We can style our form with CSS classes in for loop.
    '''
    class Meta:
        model = Comment
        fields = ['body']

    labels = {
        'body' : 'Write your comment...'
    }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class' : 'CLASS_NAME'})