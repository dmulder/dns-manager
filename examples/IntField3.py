# encoding: utf-8



from libyui import *
class IntField3Client:
    def main(self):
      # `IntField in combination with `HWeight
      # (test case for ncurses bug #488757)
      UI.OpenDialog(
        HBox(
          HWeight(1, IntField("short", 0, 10000, 50)),
          HWeight(1, PushButton(Opt("default"), "long label"))
        )
      )
      UI.UserInput()
      UI.CloseDialog()


IntField3Client().main()

