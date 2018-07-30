(function ($) {
	var methods = {
		init: function (data) {
			var current = new Date();
			var options = {
				current: current,
				months: ['January','February','March','April','May','June','July','August','September','October','November','December'],
				week: ['Su','Mo','Tu','We','Th','Fr','Sa'],
				year: current.getFullYear(),
				day: current.getDate(),
				month: current.getMonth(),
				template: '',
				drawDay: methods.generateDay,
				element: $(this),
				custom_data:'',
				customEvents: function () {},
				beforeLoad: function () {},
				goBack: function () {},
				goForward: function () {},
				openMonth: methods.openMonth
			};

			$.extend(options, data);

			return this.each(function () {
				var _this = $(this);

				options.beforeLoad();
				_this.data('calendar-options', options);
				methods.drawCalendar.apply(_this);
				methods.initEvents.apply(_this);

			});

		},
		initEvents: function () {
			var _this = $(this);
			var options = _this.data('calendar-options');
			$('body').on('click', '#calendar-back', function () {
				options.month--;
				if (options.month < 0) {
					options.month = 11;
					options.year--;
				}
				options.goBack();
				_this.data('calendar-options', options);
				methods.drawCalendar.apply(_this)
			}).on('click', '#calendar-forward', function () {
				options.month++;
				if (options.month > 11) {
					options.month = 0;
					options.year++;
				}
				options.goForward();
				_this.data('calendar-options', options);
				methods.drawCalendar.apply(_this)
			});
			options.customEvents()
		},
		openMonth: function (date) {
			var _this = $(this)[0].element;
			var options = _this.data('calendar-options');
			if (!(date instanceof Date)) {
				date = new Date();
			}
			options.year = date.getFullYear();
			options.month = date.getMonth();
			_this.data('calendar-options', options);

			methods.drawCalendar.apply(_this);
		},

		drawCalendar: function () {
			var _this = $(this);
			var options = _this.data('calendar-options');
			methods.generateHead.apply(_this);
			methods.generateBody.apply(_this);
			_this.html(options.template)
		},
		generateHead: function () {
			var _this = $(this);
			var options = _this.data('calendar-options');

			var week = [];
			for(var i =0; i < 7; i++) {
				week.push($('<th/>').text(options.week[i]))
			}

			options.template = $('<table/>').append(
				$('<thead/>').append(
					$('<tr/>').append(
						$('<th/>').attr('id', 'calendar-back').html("&laquo;")
					).append(
						$('<th/>').attr('colspan', 5).text(options.months[options.month] + ' ' + options.year)
					).append(
						$('<th/>').attr('id', 'calendar-forward').html("&raquo;")
					).addClass('cal-head')
				).append(
					$('<tr/>').append(week).addClass('cal-head')
				)
			).append(
				$('<tbody/>')
			);

			_this.data('calendar-options', options);
		},
		generateBody: function () {
			var _this = $(this);
			var options = _this.data('calendar-options');

			var this_month = new Date(options.year, options.month, 1);
			var next_month = new Date(options.year, options.month + 1, 1);

			// Find out when this month starts and ends.
			var week_day = this_month.getDay();
			var days_in_this_month = Math.round((next_month.getTime() - this_month.getTime()) / (1000 * 60 * 60 * 24));


			var emptyDays = [];
			for(var i = 0; i < week_day; i++) {
				emptyDays.push($('<td/>'));
			}

			var daysInWeek = [];
			for(var day_counter = 1; day_counter <= days_in_this_month; day_counter++) {
				week_day %= 7;
				daysInWeek.push($('<td/>').addClass('cal-dates').append(options.drawDay(day_counter, options)))
				if (week_day === 6) {
					options.template.find('tbody').append(
						$('<tr/>').append(emptyDays).append(daysInWeek)
					);
					emptyDays = daysInWeek = [];
				}
				week_day++;
			}
			if (daysInWeek.length) {
				options.template.find('tbody').append(
					$('<tr/>').append(emptyDays).append(daysInWeek)
				);
			}
			_this.data('calendar-options', options);
		},
		generateDay: function (day, options) {
			var elem = $('<span/>');
			if (options.day == day && (new Date()).getFullYear() == options.year && (new Date()).getMonth() == options.month) {
				elem.append($('<strong/>').text(day))
			} else {
				elem.text(day)
			}
			return elem;
		}

	};
	$.fn.calendar = function (method) {
		if (methods[method]) {
			return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
		} else if (typeof method === 'object' || !method) {
			return methods.init.apply(this, arguments);
		} else {
			alert('Method ' + method + ' does not exist on jQuery.calendar');
		}
	};

})(jQuery);