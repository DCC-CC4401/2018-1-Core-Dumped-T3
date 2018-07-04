$(function () {
  $('#day').datetimepicker({
    format: 'L',
    minDate: moment().add(1, 'h'),
    date: moment("{{ form.day.value }}", "DD-MM-YYYY"),
    enabledHours: [9, 10, 11, 12, 13, 14, 15, 16, 17],
    daysOfWeekDisabled: [0, 6],
    locale: 'es'
  })
  $('#start_time').datetimepicker({
    format: 'LT',
    minDate: moment().add(1, 'h'),
    date: moment("{{ form.day.value }} {{ form.start_time.value }}", "DD-MM-YYYY HH-mm"),
    enabledHours: [9, 10, 11, 12, 13, 14, 15, 16, 17],
    daysOfWeekDisabled: [0, 6],
    locale: 'es'
  });
  $('#end_time').datetimepicker({
    format: 'LT',
    minDate: moment().add({'h': 1, 'm': 1}),
    date: moment("{{ form.day.value }} {{ form.end_time.value }}", "DD-MM-YYYY HH-mm"),
    enabledHours: [9, 10, 11, 12, 13, 14, 15, 16, 17],
    daysOfWeekDisabled: [0, 6],
    locale: 'es'
  });
  $('#day').on("change.datetimepicker", function (e) {
    let newDate = e.date;
    $('#start_time').datetimepicker(
      'date', 
      $("#start_time").datetimepicker('date').set({
        'year': newDate.year(),
        'month': newDate.month(),
        'date': newDate.date()
      })
    );
    $('#end_time').datetimepicker(
      'date',
      $('#end_time').datetimepicker('date').set({
        'year': newDate.year(),
        'month': newDate.month(),
        'date': newDate.date()
      })
    );
  });
  $('#start_time').on("change.datetimepicker", function(e) {
    $('#day').datetimepicker('date', e.date)
    if($("#end_time").datetimepicker('date') && $("#end_time").datetimepicker('date').isBefore(e.date.add(1, 'm'))) {
      $("#end_time").datetimepicker('date', e.date);
    }
  });
  $('#end_time').on("change.datetimepicker", function(e) {
    if($("#start_time").datetimepicker('date') && $("#start_time").datetimepicker('date').isAfter(e.date.subtract(1, 'm'))) {
      $("#start_time").datetimepicker('date', e.date);
    }
  });
});
