from wtforms import TextAreaField, SelectField, TextField, DateField
from wtforms.widgets import TextArea, Select, TextInput, HTMLString, html_params
 
class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        kwargs.setdefault('id', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)
 
 
class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()

