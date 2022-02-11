# encoding: utf-8

# Tree with icons


from libyui import *
class TreeCheckboxClient:
    def main(self):
      UI.OpenDialog(
        VBox(
          Heading("YaST2 Mini Control Center"),
          Tree(
            Id("mod"),
            Opt("multiSelection"),
            "Modules",
            [
              Item(
                Id("country"),
                Term("icon", "libyui-libyui-language.png"),
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
              Item(Id("xmas"), Term("icon", "libyui-software.png"), "Merry X-Mas"),
              Item(
                Id("newyear"),
                Term("icon", "libyui-software.png"),
                "Happy New Year"
              )
            ]
          ),
          PushButton(Id("ok"), Opt("default"), "&OK")
        )
      )

      UI.ChangeWidget("mod", "SelectedItems", [Id("xmas"), Id("newyear")])

      id = None
      while True:
        id = UI.TimeoutUserInput(300)
        selected_items = UI.QueryWidget(Id("mod"), "SelectedItems")

        ycpbuiltins.y2warning("Selected items: %1", selected_items)
        if id == "ok":
          break

      UI.CloseDialog()

TreeCheckboxClient().main()

