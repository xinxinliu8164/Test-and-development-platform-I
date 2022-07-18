from django.db import models
from modules.models import ManageModule

# Create your models here.

class TestCase(models.Model):
    """用例"""

    module = models.ForeignKey(ManageModule, on_delete=models.CASCADE)
    name = models.CharField("用例名称", max_length=100, default='')

    url = models.TextField("url")
    req_method = models.CharField("请求方法", max_length=50, default='')
    header_editor = models.TextField("请求头", default='')
    par_type = models.CharField("参数类型", max_length=50, default='')
    parameters = models.TextField("请求参数", default='')
    rep_result = models.TextField("响应结果", default='')
    assert_type = models.TextField("断言类型", default='')
    assert_text = models.TextField("断言文本", default='')

    update_time = models.DateTimeField("更新时间", auto_now=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        # return u'{0}'.format(self.name)
        return self.name