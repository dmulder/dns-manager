# encoding: utf-8

# Advanced example of using the Wizard widget.
#
# Note: YCP applications are discouraged from using the Wizard widget directly.
# Use the Wizard module instead.


from libyui import *
class Wizard3Client:
    def main(self):

      base_installation_steps = [
        { "id" : "language", "label" : "Language" },
        { "id" : "proposal", "label" : "Installation Settings" },
        { "id" : "do_resize", "label" : "Perform Installation" },
        { "id" : "prepdisk", "label" : "Perform Installation" },
        { "id" : "kickoff", "label" : "Perform Installation" },
        { "id" : "rpmcopy", "label" : "Perform Installation" },
        { "id" : "finish", "label" : "Perform Installation" }
      ]

      config_steps = [
        { "id" : "root", "label" : "Root Password" },
        { "id" : "proposal_net", "label" : "Network" },
        { "id" : "ask_net_test", "label" : "Network" },
        { "id" : "do_net_test", "label" : "Network" },
        { "id" : "you", "label" : "Online Update" },
        { "id" : "auth", "label" : "Users" },
        { "id" : "user", "label" : "Users" },
        { "id" : "suseconfig", "label" : "Clean Up" },
        { "id" : "release_notes", "label" : "Release Notes" },
        { "id" : "proposal_hw", "label" : "Device Configuration" }
      ]

      self.steps = ycpbuiltins.flatten([base_installation_steps, config_steps])

      if not UI.HasSpecialWidget("Wizard"):
        ycpbuiltins.y2error(
          "This works only with UIs that provide the wizard widget!"
        )
        return

      help_text = "<p>This is a help text.</p>" + "<p>It should be helpful.</p>" + "<p>If it isn't helpful, it should rather not be called a <i>help text</i>.</p>"

      UI.OpenDialog(
        Opt("defaultsize"),
        Wizard(
          Opt("stepsEnabled"),
          Symbol("back"),
          "&Back",
          Symbol("abort"),
          "Ab&ort",
          Symbol("next"),
          "&Next"
        )
      )

      # UI::DumpWidgetTree();

      UI.WizardCommand(
        Term(
          "SetDialogIcon",
          "/usr/share/YaST2/theme/current/icons/22x22/apps/YaST.png"
        )
      )
      UI.WizardCommand(
        Term("SetDialogHeading", "Welcome to the YaST2 installation")
      )
      UI.WizardCommand(Term("SetHelpText", help_text))
      UI.WizardCommand(
        Term("ShowReleaseNotesButton", "&Release Notes", "release_notes")
      )

      UI.WizardCommand(Term("AddStepHeading", "Base Installation"))

      for step in ycpbuiltins.foreach(base_installation_steps):
        UI.WizardCommand(
          Term(
            "AddStep",
            step["label"]),
            step["id"])

      UI.WizardCommand(Term("AddStepHeading", "Configuration"))

      for step in ycpbuiltins.foreach(config_steps):
        UI.WizardCommand(
          Term(
            "AddStep",
            step["label"],
            step["id"]
          )
        )


      current_step = 0
      self.show_step(0)

      while True:
        button =UI.UserInput()

        if button == "abort" or button == "cancel":
          break

        if button == "next" or button == "back":
          if button == "next" and (current_step + 1) < ycpbuiltins.size(self.steps):
            current_step = current_step + 1

            if current_step > 2:
              UI.WizardCommand(Term("HideReleaseNotesButton"))

          if button == "back" and current_step > 0:
            current_step = current_step - 1

          self.show_step(current_step)

      UI.CloseDialog()


    def show_step(self, no):
      current_id = self.steps[no]["id"]

      UI.ReplaceWidget(
        Id("contents"),
        VBox(
          Heading("Current workflow step:"),
          VSpacing(0.5),
          Label(current_id)
        )
      )

      UI.WizardCommand(Term("SetCurrentStep", current_id))


Wizard3Client().main()

