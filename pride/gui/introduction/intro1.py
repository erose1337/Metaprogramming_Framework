""" This example shows how to create a window.
    A login prompt will be displayed.
    The login prompt can be avoided by setting the Gui user to the built-in User that represents the device.
    Depending on the nature of the application, one behavior may be preferable to the other.
    Run this file using `python -m pride.main yourpathhere/intro1.py`"""

def main():
    import pride
    import pride.gui
    import pride.gui.main
    window = pride.objects[pride.gui.enable()]
    window.create(pride.gui.main.Gui,
                 # user=pride.objects["/User"] # uncomment to skip login screen
                  )

if __name__ == "__main__":
    main()
