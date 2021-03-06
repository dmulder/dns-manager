# encoding: utf-8

# Simple example for help text


from libyui import *
class HelpTextClient:
    def main(self):
      UI.OpenDialog(
        VBox(
          Id("mainLayout"),
          Label("Hello, World!"),
          HBox(
            PushButton(Opt("helpButton"), "&Help"),
            PushButton(Opt("default"), "&OK")
          )
        )
      )
      UI.ChangeWidget(
        "mainLayout",
        "HelpText",
        "Oh, come on, do you really need help for this?"
      )

      UI.UserInput()
      UI.CloseDialog()


HelpTextClient().main()

