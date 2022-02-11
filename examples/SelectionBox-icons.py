# encoding: utf-8

# Selection box with icons


from libyui import *
class SelectionBoxIconsClient:
    def main(self):
      UI.OpenDialog(
        VBox(
          Heading("YaST2 Mini Control Center"),
          SelectionBox(
            Id("mod"),
            "Modules",
            [
              Item(Id("keyboard"), Term("icon", "libyui-keyboard.png"), "Keyboard"),
              Item(Id("mouse"), Term("icon", "libyui-mouse.png"), "Mouse"),
              Item(
                Id("timezone"),
                Term("icon", "libyui-timezone.png"),
                "Time zone"
              ),
              Item(Id("lan"), Term("icon", "libyui-lan.png"), "Network"),
              Item(
                Id("sw_single"),
                Term("icon", "libyui-software.png"),
                "Software"
              )
            ]
          ),
          PushButton("&OK")
        )
      )
      UI.UserInput()

      # Get the input from the selection box.
      #
      # Notice: The return value of UI::UserInput() does NOT return this value!
      # Rather, it returns the ID of the widget (normally the PushButton)
      # that caused UI::UserInput() to return.
      mod = UI.QueryWidget(Id("mod"), "CurrentItem")

      # Close the dialog.
      # Remember to read values from the dialog's widgets BEFORE closing it!
      UI.CloseDialog()


SelectionBoxIconsClient().main()

