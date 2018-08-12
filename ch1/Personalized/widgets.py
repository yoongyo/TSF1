from django import forms


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

class BookingDatePickerWidget(forms.DateInput):
    template_name = 'widgets/booking_date.html'

    class Media:
        css = {
            'all': [
                '//code.jquery.com/ui/1.12.1/themes/smoothness/jquery-ui.css',
            ],
        }
        js = [
            '//code.jquery.com/ui/1.12.1/jquery-ui.min.js',
        ]

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

class LocationWidget(forms.TextInput):
    template_name = 'widgets/location_widget.html'

    class Media:
        js = [
            '//maps.googleapis.com/maps/api/js', # FIXME: Google Maps JavaScript API 키 적용
        ]

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs['readonly'] = True
        attrs['style'] = 'background-color: #eee; border: 0;'
        return attrs


class AutoCompleteSelect(forms.Select):
    template_name = 'widgets/autocomplete_select.html'
    class Media:
        css = {
            'all': [
                '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/css/select2.min.css',
            ],
        }
        js = [
            '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/js/select2.min.js',
            ]

    def build_attrs(self, *args, **kwargs):
        context = super().build_attrs(*args, **kwargs);
        context['style'] = 'min-width: 200px;'
        return context

class CounterTextInput(forms.TextInput):
    template_name = 'widgets/counter_text.html'

class MultiDatePicker(forms.TextInput):
    template_name = 'widgets/MultiDatePicker.html'

    class Media:
        css = {
            'all': [
                '//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.4.1/css/bootstrap-datepicker3.css',
                '//formden.com/static/cdn/bootstrap-iso.css',
            ],

        }
        js = [
             '//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.4.1/js/bootstrap-datepicker.min.js'
        ]
