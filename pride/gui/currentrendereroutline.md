What major steps are involved in the process?
---------------------------------------------
- user input
    - act upon mouse clicks, key presses, etc
- predraw queue
    - used to perpetuate animation in cases where using postdraw_queue would lead to a "busy" icon by the mouse (for whatever reason)
- organize
    - space-filling rectangle packing algorithm
    - determines x, y, w, h of each gui object based on parent object size
- update draw instructions
    - drawing instructions are cached according to layer and updated when changes occur
- draw
    - drawing instructions are evaluated and presented to screen (a frame is drawn)
    - uses layer-cacheing strategy
        - each layer is saved and only layers that change are re-drawn
- postdraw
    - postdraw is used for things like perpetuating animation
        - used to set `texture_invalid` to True after drawing
            - drawing automatically clears the `texture_invalid` flag
    -? alternatively, could set animated objects to set `texture_invalid` to True when it is set to False while animating


What order and why?
-------------------

- clearly `update draw instructions` must come before `draw`
- `organize` should come before `update draw instructions`
    - organizing afterwards is too late
- `user input` should before organize
    - `left_click` could created/delete/hide/show/etc and could trigger organizer
- postdraw must come after draw
- predraw should come before organize/update/draw in case it makes any modifications that would trigger them
- user input could come before predraw, because user actions could manipulate predraw queue

user input -> predraw -> organize -> update -> draw -> postdraw
