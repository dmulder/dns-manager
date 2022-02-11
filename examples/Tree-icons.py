# encoding: utf-8

# Tree with icons


from libyui import *
class TreeIconsClient:
    def main(self):
      UI.OpenDialog(
        VBox(
          Heading("YaST2 Mini Control Center"),
          Tree(
            Id("mod"),
            "Modules",
            [
              Item(
                Id("country"),
                Term("icon", "libyui-language.png"),
                "Localization",
                True,
                [
                  Item(
                    Id("keyboard"),
                    Term("icon", "libyui-keyboard.png"),
                    "Keyboard"
                  ),
                  Item(
                    Id("timezone"),
                    Term("icon", "libyui-timezone.png"),
                    "Time zone"
                  )
                ]
              ),
              Item(Id("mouse"), Term("icon", "libyui-mouse.png"), "Mouse"),
              Item(Id("lan"), Term("icon", "libyui-lan.png"), "Network"),
              Item(
                Id("sw_single"),
                Term("icon", "libyui-software.png"),
                "Software"
              )
            ]
          ),
          PushButton(Id("ok"), Opt("default"), "&OK")
        )
      )

      UI.UserInput()
      UI.CloseDialog()


TreeIconsClient().main()

