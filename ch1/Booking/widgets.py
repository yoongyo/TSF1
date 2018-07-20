from django import forms

class CounterTextInput(forms.TextInput):
    template_name = 'widgets/counter_text.html'

class DatePickerWidget(forms.DateInput):

    template_name = 'widgets/picker_date.html'

    class Media:
        css = {
            'all': [
                '//code.jquery.com/ui/1.12.1/themes/smoothness/jquery-ui.css',
            ],
        }
        js = [
            '//code.jquery.com/ui/1.12.1/jquery-ui.min.js',
            ]