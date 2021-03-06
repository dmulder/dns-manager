# encoding: utf-8



from libyui import *
class LayoutWeights1Client:
    def main(self):
      # Layout example:
      #
      # Build a dialog with three widgets with different weights.
      #
      # Weights do not need to add up to 100 or any other special
      # number, but it helps the application programmer to keep track
      # of the percentage of each part of the layout.
      #
      # Notice how the second button commands the overall size of the
      # dialog since it has the largest "nice size" to "weight" ratio.
      #
      # Upon resize all widgets will resize to maintain their
      # respective weights at all times.
      #

      UI.OpenDialog(
        HBox(
          HWeight(25, PushButton(Opt("default"), "OK\n25%")),
          HWeight(25, PushButton("Cancel everything\n25%")),
          HWeight(50, PushButton("Help\n50%"))
        )
      )

      UI.UserInput()
      UI.CloseDialog()


LayoutWeights1Client().main()

