# encoding: utf-8



from libyui import *
class Enabling3Client:
    def main(self):
      UI.OpenDialog(
        VBox(
          VBox(
            Id("box"),
            Opt("disabled"),
            InputField("TestEntry", ""),
            CheckBox("Looks fine")
          ),
          PushButton(Id("change"), "&Change"),
          PushButton(Id("cancel"), "&Quit")
        )
      )

      enabled = False

      while (UI.UserInput() != "cancel"):
        enabled = not enabled
        UI.ChangeWidget(Id("box"), "Enabled", enabled)

      UI.CloseDialog()


Enabling3Client().main()

