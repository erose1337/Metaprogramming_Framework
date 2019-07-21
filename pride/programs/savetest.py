def main():
    import pride.gui
    window = objects[pride.gui.enable()]
    a = window.create("pride.gui.gui.Application")
    s = a.save()
    a.delete()
    a = a.load(s)

if __name__ == "__main__":
    main()
