# encoding: utf-8

# Example showing how to replace SelectionBox items


from libyui import *
class SelectionBoxReplaceItems1Client:
    def main(self):

      pizza_list = [
        "Pizza Napoli",
        "Pizza Funghi",
        "Pizza Salami",
        "Pizza Hawaii"
      ]

      pasta_list = ["Spaghetti", "Rigatoni", "Tortellini"]

      UI.OpenDialog(
        VBox(
          SelectionBox(Id("menu"), "Daily &Specials:", pizza_list),
          HBox(
            PushButton(Id("pizza"), "Pi&zza"),
            PushButton(Id("pasta"), "&Pasta"),
            PushButton(Id("diet"), "Strict &Diet")
          ),
          PushButton(Id("ok"), "&OK")
        )
      )

      button = None
      while True:
        button = UI.UserInput()

        if button == "pizza":
          UI.ChangeWidget("menu", "Items", pizza_list)
        if button == "pasta":
          UI.ChangeWidget("menu", "Items", pasta_list)
        if button == "diet":
          UI.ChangeWidget("menu", "Items", [])
        if button == "ok":
            break

      order = UI.QueryWidget("menu", "CurrentItem")
      UI.CloseDialog()


      #
      # Show the result
      #

      UI.OpenDialog(
        VBox(
          Label(ycpbuiltins.sformat("Your order: %1", order)),
          PushButton(Opt("default"), "&OK")
        )
      )
      UI.UserInput()
      UI.CloseDialog()


SelectionBoxReplaceItems1Client().main()

