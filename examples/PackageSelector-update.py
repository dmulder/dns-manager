# encoding: utf-8




from libyui import *
class PackageSelectorUpdateClient:
    def main(self):
      Pkg.TargetInit(
        "/", # installed system
        False
      ) # don't create a new RPM database
      UI.OpenDialog(
        Opt("defaultsize"),
        PackageSelector(Id("selector"), Opt("testMode", "updateMode"))
      )
      input = UI.RunPkgSelection(Id("selector"))
      UI.CloseDialog()

      ycpbuiltins.y2milestone("Input: %1", input)


PackageSelectorUpdateClient().main()

