import datetime

import pride.gui.gui

MONTHS = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")
          
NUMBER_TO_MONTH = dict((index + 1, month) for index, month in enumerate(MONTHS))
          
NUMBER_OF_DAYS = {"January" : 31, "February" : 28, "March" : 31,
                  "April" : 31, "May" : 30, "June" : 31, "July" : 31,
                  "August" : 31, "September" : 30, "October" : 30,
                  "November" : 30, "December" : 31}
                  
class Calendar(pride.gui.gui.Window):
    
    defaults = {"month" : '', "background_color" : (255, 255, 255, 80),
                "color" : (21, 21, 21, 255), "text_color" : (68, 68, 68, 255)}
    required_attributes = ("month", )
    post_initializer = "setup_calendar"
            
    def setup_calendar(self):        
        self.change_month(self.month)
        
    def change_month(self, month, year=None, day=None):                
        for child in self.children[:]:            
            child.delete()            
                        
        background_color = self.background_color
        outline_color = self.color
        text_color = self.text_color
        now = datetime.datetime.now()
        year = now.year if year is None else year  
        month_index = MONTHS.index(month) + 1  
        day = now.day if day is None else day       
        datetime_object = datetime.datetime(year, month_index, 1)
        first_weekday = (datetime_object.weekday() + 1) % 7 # because datetime starts with monday as day 0 instead of sunday    
        unused_days = first_weekday                
        
        number_of_days = NUMBER_OF_DAYS[month]
        number_of_rows, extra = divmod(number_of_days + unused_days, 7)
        if extra:
            number_of_rows += 1
            
        top_bar = self.create("pride.gui.gui.Container", pack_mode="top", h_range=(50, 50),
                              color=outline_color)
        day_bar = self.create("pride.gui.gui.Container", pack_mode="top", h_range=(30, 30),
                              color=outline_color)        
        grid = self.create("pride.gui.grid.Grid", columns=number_of_rows, rows=7,
                           square_colors=(background_color, background_color),
                           square_outline_colors=(outline_color, outline_color),
                           color=outline_color)
                           
        top_bar.create(Previous_Month_Button, pack_mode="left", text='<', 
                       w_range=(40, 40), background_color=background_color,
                       color=outline_color, text_color=text_color)
        top_bar.create(Next_Month_Button, pack_mode="left", text='>', 
                       w_range=(40, 40), background_color=background_color,
                       color=outline_color, text_color=text_color)
        top_bar.create("pride.gui.gui.Button", pack_mode="main", 
                       text="{} {}".format(month, year), background_color=background_color,
                       color=outline_color, text_color=text_color)
        top_bar.create(Month_Display_Button, pack_mode="right", w_range=(60, 60),
                       background_color=background_color, color=outline_color,
                       text="Month", text_color=text_color)
        top_bar.create(Week_Display_Button, pack_mode="right", w_range=(50, 50),
                       background_color=background_color, color=outline_color,
                       text="Week", text_color=text_color)
        top_bar.create(Day_Display_Button, pack_mode="right", w_range=(40, 40),
                       background_color=background_color, color=outline_color,
                       text="Day", text_color=text_color)
               
        days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")        
        for index, day in enumerate(days):            
            button = day_bar.create("pride.gui.gui.Button", text=day, 
                                    pack_mode="left", text_color=text_color,
                                    background_color=background_color, color=outline_color)  
                      
        prior_month = MONTHS[MONTHS.index(month) - 1]
        prior_month_days = NUMBER_OF_DAYS[prior_month]                
        prior_month_day = (prior_month_days - unused_days) + 1           
        for day_number in range(unused_days):
            day_button = grid[day_number][0]
            day_button.text = str(prior_month_day + day_number)
            day_button.center_text = False
            day_button.text_color = text_color                        
        try:
            offset = day_number + 1
        except NameError:
            offset = 0
        
        day_number = 1
        for remaining_day in range(7 - unused_days):            
            day_button = grid[offset + remaining_day][0]
            day_button.text = str(day_number)
            day_button.center_text = False
            day_button.text_color = text_color
            day_number += 1
            
        for day_number in range(day_number, number_of_days + 1):
            row_number, column_number = divmod((day_number + offset) - 1, 7)            
            day_button = grid[column_number][row_number]
            day_button.text = str(day_number)
            day_button.center_text = False
            day_button.text_color = text_color
            
            
class Previous_Month_Button(pride.gui.gui.Button): 

    def left_click(self, mouse):
        calendar = self.parent.parent
        previous_month = MONTHS[MONTHS.index(calendar.month) - 1]
        calendar.month = previous_month
        calendar.change_month(previous_month)
        calendar.pack()
        
    
class Next_Month_Button(pride.gui.gui.Button): 

    def left_click(self, mouse):
        calendar = self.parent.parent
        next_month = MONTHS[(MONTHS.index(calendar.month) + 1) % 12]
        calendar.month = next_month
        calendar.change_month(next_month)
        calendar.pack()
        
    
class Month_Display_Button(pride.gui.gui.Button): pass


class Week_Display_Button(pride.gui.gui.Button): pass


class Day_Display_Button(pride.gui.gui.Button): pass


            
        
        