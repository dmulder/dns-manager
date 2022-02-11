# encoding: utf-8



from libyui import *
class HCenter3Client:
    def main(self):
      UI.OpenDialog(
        Opt("defaultsize"),
        VBox(
          VCenter(PushButton(Opt("vstretch"), "Button 1")),
          VCenter(PushButton(Opt("vstretch"), "Button 2")),
          VCenter(PushButton(Opt("vstretch"), "Button 3"))
        )
      )
      UI.UserInput()
      UI.CloseDialog()


HCenter3Client().main()

