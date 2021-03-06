# encoding: utf-8



from libyui import *

class ComboBoxSetInputMaxLengthClient:
    def main(self):

      UI.OpenDialog(
        VBox(
          ComboBox(
            Id("input"),
            Opt("editable"),
            "Combo Box",
            ["pizza", "pasta", "pronta"]
          ),
          IntField(Id("field"), "Limit characters to...", -1, 100, -1),
          PushButton(Id("butt"), "limit input"),
          PushButton(Id("exitButton"), "Exit")
        )
      )

      ret = None
      ret = UI.UserInput()

      while (ret != "exitButton"):
        chars = UI.QueryWidget(Id("field"), "Value")
        UI.ChangeWidget("input", "InputMaxLength", chars)

        ret = UI.UserInput()

      UI.CloseDialog()

ComboBoxSetInputMaxLengthClient().main()
