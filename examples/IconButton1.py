# encoding: utf-8

# PushButton with icons (relative path)


from libyui import *
class IconButton1Client:
    def main(self):
      UI.OpenDialog(
        VBox(
          Heading("YaST2 Mini Control Center"),
          IconButton(Id("keyboard "), "libyui-keyboard.png", "Keyboard"),
          IconButton(Id("mouse"), "libyui-mouse.png", "Mouse"),
          IconButton(Id("timezone"), "libyui-timezone.png", "Time zone"),
          IconButton(Id("lan"), "libyui-lan.png", "Network"),
          IconButton(Id("sw_single"), "libyui-software.png", "Software")
        )
      )

      ret = None
      while True:
        ret = UI.UserInput()

        if ret != "cancel":
          UI.OpenDialog(
            Label("Running " + ret + "...")
          )
          ycpbuiltins.sleep(4000)
          UI.CloseDialog()
        if ret == "cancel":
          break

      UI.CloseDialog()


IconButton1Client().main()

