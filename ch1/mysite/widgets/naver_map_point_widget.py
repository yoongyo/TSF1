import re
from django import forms
from django.conf import settings
from django.template.loader import render_to_string



class NaverMapPointWidget(forms.TextInput):
    def rnder(self, name, value, attrs):
        html = """
            <div style="width : 100px; height: 100px; background-color: red;">
                네이버 지도를 그려봅시다.
            </div>
        """

        parent_html = super().render(name, value, attrs)

        return parent_html + html