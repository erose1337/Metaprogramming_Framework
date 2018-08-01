import datetime

import pride.gui.gui

MONTHS = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")
          
NUMBER_TO_MONTH = dict((index, month) for index, month in enumerate(MONTHS))
          
NUMBER_OF_DAYS = {"January" : 31, "February" : 28, "March" : 31,
                  "April" : 31, "May" : 30, "June" : 31, "July" : 31,
                  "August" : 31, "September" : 30, "October" : 30,
                  "November" : 30, "December" : 31}
                  
class Calendar(pride.gui.gui.Window):
    
    defaults = {"month" : '', "background_color" : (255, 255, 255, 155),
                "color" : (21, 21, 21, 255), "text_color" : (68, 68, 68, 255)}
    required_attributes = ("month", )
    post_initializer = "setup_calendar"
            
    def setup_calendar(self):        
        self.change_month(self.month)
        
    def change_month(self, month):
        for child in self.children:
            child.delete()
        
        year = datetime.datetime.now().year
        
        number_of_days = NUMBER_OF_DAYS[month]
        number_of_rows, extra = divmod(number_of_days, 7)
        if extra:
            number_of_rows += 1
            
        background_color = self.background_color
        outline_color = self.color
        text_color = self.text_color
        
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
        printed = False
        
        
        days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")        
        for index, day in enumerate(days):            
            button = day_bar.create("pride.gui.gui.Button", text=day, 
                                    pack_mode="left", text_color=text_color,
                                    background_color=background_color, color=outline_color)  
            
        for day_number in range(1, number_of_days + 1):
            row_number, column_number = divmod(day_number - 1, 7)
            day_button = grid[column_number][row_number]
            day_button.text = str(day_number)
            day_button.center_text = False
            day_button.text_color = text_color
            
            
class Previous_Month_Button(pride.gui.gui.Button): pass


class Next_Month_Button(pride.gui.gui.Button): pass


class Month_Display_Button(pride.gui.gui.Button): pass


class Week_Display_Button(pride.gui.gui.Button): pass


class Day_Display_Button(pride.gui.gui.Button): pass


            
        
        