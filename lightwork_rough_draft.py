#started work on 16th may 2025
#VERSION 1.0

LIGHTWORK_CONSTANTS = ("VAR", 'FUNC', 'OUTPUT', 'CHECK PARSING', 'VERSION')
LIGHTWORK_EXCEPTION_CONSTANTS = ('CHECK PARSING', 'VERSION')
VERSION = 1.0
command_tuple = ()
variable_dict = {} 

import scipy as s

def run_function(e):
    print(user_input.GetValue())

def help_function(e):
    print("You have been helped")

import wx as w


lightwork = w.App()

window = w.Frame(None, title = "Lightwork", size = (800, 500))

#making the toolbar
RUN_ID = w.NewIdRef()
command_ = window.CreateToolBar()

run_button = command_.AddTool(RUN_ID, "Run", w.ArtProvider.GetBitmap(w.ART_GO_FORWARD, w.ART_TOOLBAR), shortHelp = "Compute your calculations")
help_button = command_.AddTool(w.ID_HELP, "Help", w.ArtProvider.GetBitmap(w.ART_HELP, w.ART_TOOLBAR), shortHelp = "Help you to use Lightwork")

command_.AddSeparator()
command_.Realize()

window.Bind(w.EVT_TOOL, run_function, id = RUN_ID)
window.Bind(w.EVT_TOOL, help_function, id = w.ID_HELP)

layout_ = w.GridBagSizer(hgap = 1, vgap = 1)

master_panel = w.Panel(window) #houses the sizers

user_input = w.TextCtrl(master_panel, style = w.TE_MULTILINE)
display_section = w.StaticText(master_panel, label= "Work in progress")

layout_.Add(user_input, pos = (0, 0), flag = w.EXPAND)
layout_.Add(display_section, pos = (0, 1),flag = w.EXPAND)

layout_.AddGrowableCol(0)
layout_.AddGrowableCol(1)
layout_.AddGrowableRow(0, proportion=1)

master_panel.SetSizer(layout_)
window.Show()
lightwork.MainLoop()