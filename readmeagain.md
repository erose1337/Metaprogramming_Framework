pride: Python Runtime and Integrated Development Environment
----
pride offers simple reusable apis and design patterns for assembling programs from standard components, such as:
    - audio
        - provides simple access to audio ins/outs (i.e. microphones and speakers)
    - gui
        - provides support for graphical applications (based on pysdl2)
    - networking
        - sockets
            - RPC (remote procedure calls)
                - DTS (data transfer service)
                    - SDTS (secure data transfer service)
    - database
        - sqlite3 only
    - data serialization
        - pythons default serializer ("pickle") is insecure
    - security and cryptography
    - command line arguments, debugging, alerts, logging, and site configuration support

Programs written with pride tend to be succinct and robust while still sporting a complete set of features


pride allows you to write concurrent programs without coroutines or synchronization primitives such as locks.
Instead, a component that performs the desired functionality is designed and instantiated at application start-up, and it interacts with other components and services in the runtime when/as necessary via references. 
    - An arbitrary number of programs can execute in a single thread
    - Programs may be saved/loaded at arbitrary points in their execution
    - Programs can be updated from source at runtime without stopping the application

    
    
pride offers debugging assistance via built-in alerts and logging features
    - example: `--print_level 0+debug`
        - 0 will show all normal messages
        - debug will display all method calls with arguments as they are called
            - only applies to methods of Base objects
    - supports standard 'v', 'vv', 'vvv', ... flags, as well as custom flags
    
Every component in the environment can be customized via the site_config file:
    - simply define new defaults for the component in question
    - can change defaults for a single session without editing site_config.py via the `--site_config` flag
    
    