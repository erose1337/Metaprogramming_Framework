import pride.gui.widgets.form
field_info = pride.gui.widgets.form.field_info

class Clock(pride.gui.widgets.form.Form):

    defaults = {"fields" : [
                     [field_info("hour", editable=False, auto_create_id=False,
                                 minimum=0, maximum=24)],
                     [field_info("minute", editable=False, auto_create_id=False,
                                 minimum=0, maximum=60)],
                     [field_info("second", editable=False, auto_create_id=False,
                                 minimum=0, maximum=60)]]}

    def __init__(self, **kwargs):
        self._set_time(time.localtime())
        super(Clock, self).__init__(**kwargs)
        self.update_time()
        self.sdl_window.schedule_postdraw_operation(self.update_time, self)

    def _set_time(self, current_time):
        self.hour = current_time.tm_hour
        self.minute = current_time.tm_min
        self.second = current_time.tm_sec

    def update_time(self):
        before = self.second
        now = time.localtime()
        if now.tm_sec != before:
            self._set_time(now)
            self.synchronize_fields()
            for field in self.fields_list.values():
                try:
                    field.update_position_from_value()
                except AttributeError:
                    if hasattr(field, "update_position_from_value"):
                        raise

        self.sdl_window.schedule_postdraw_operation(self.update_time, self)

def test_Clock():
    import pride.gui.main
    pride.gui.main.run_programs([Clock])

if __name__ == "__main__":
    test_Clock()
