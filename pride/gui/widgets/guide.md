settings slider
===============

           rect  rect  rect  rect
    [unit]|---------slider-------|[value]

- rect displays qualitative level (e.g. very low, low, medium, high, very high)
- slider displays quantitative level (x < y < z)
- Clicking on level button sets value and slider to appropriate value
- Dragging slider highlights a rect (level button)


Recursive Menu
==========

      [current_place]
        rect   rect
        rect   rect

Each rect displays an option from a menu e.g.:

    play   load
    create options

Selecting an option:
    - hides currently displayed choices
    - appends the selected option onto the current_place
    - Either:
        - The selected option opens a new menu
        - The selected option performs some function
