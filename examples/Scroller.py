# encoding: utf-8

# Example that scrolls a lot


from libyui import *
class ScrollerClient:
    def main(self):
      UI.OpenDialog(
        VBox(
          LogView(
            Id("log"),
            "",
            10, # visible lines
            5000
          ), # lines to store
          PushButton(Id("cancel"), "&Close")
        )
      )

      count = 0
      button = None
      while True:
        count = count + 1
        message = ycpbuiltins.sformat("[%1] Log line #%2\n", count, count)
        UI.ChangeWidget("log", "LastLine", message)
        button = UI.TimeoutUserInput(200) # millisec
        if button == "cancel":
          break


      UI.CloseDialog()


ScrollerClient().main()

