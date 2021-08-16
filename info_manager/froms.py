from django import forms
from .models import InfoPost_7,InfoPost_8,InfoPost_9
class UploadFileForm(forms.Form):
    upload_file = forms.FileField(label='文件上传')
    title = forms.CharField(max_length=200)

class InfoPostForm_7(forms.Form):
    class Meta:
        # 指明数据模型来源
        model = InfoPost_7()
        # 定义表单包含的字段
        fields = ('title', 'question', 'option_a','option_b','option_c','option_d','answer','question_id','quesiton_info')

class InfoPostForm_8(forms.Form):
    class Meta:
        # 指明数据模型来源
        model = InfoPost_8()
        # 定义表单包含的字段
        fields = ('title', 'question', 'option_a','option_b','option_c','option_d','answer','question_id','quesiton_info')

class InfoPostForm_9(forms.Form):
    class Meta:
        # 指明数据模型来源
        model = InfoPost_9()
        # 定义表单包含的字段
        fields = ('title', 'question', 'option_a','option_b','option_c','option_d','answer','question_id','quesiton_info')
