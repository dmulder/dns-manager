# encoding: utf-8



from libyui import *

class CheckBox1Client:
    def main(self):
      UI.OpenDialog(CheckBox("A &checked check box\nwith multi-line", True))
      UI.UserInput()
      UI.CloseDialog()

CheckBox1Client().main()
