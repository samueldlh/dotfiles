# Configuration for Qtile
# samueldlh

from typing import List

import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(), desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(), desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack"),
    # Launch terminal
    Key([mod], "Return", lazy.spawn(terminal)),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Close windows
    Key([mod, "shift"], "w", lazy.window.kill()),

    #Focus of monitors
    Key([mod], "comma", lazy.prev_screen()),
    # Window size
    Key([mod, "shift"], "u", lazy.layout.grow()),
    Key([mod, "shift"], "i", lazy.layout.shrink()),

    # Restart qtile
    Key([mod, "control"], "r", lazy.restart()),
    # Shutdown qtile 
    Key([mod, "control"], "q", lazy.shutdown()),

    #Apps
    Key([mod, "shift"], "m", lazy.spawn("rofi -show run")),
    #Browser
    Key([mod], "b", lazy.spawn("firefox-developer-edition")),

    #screenshot
    Key([mod, "shift"], "p", lazy.spawn("imlib2_grab screenshot.png")),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    # Brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

]

groups = [Group(i) for i in ["1","2", "3", "4", "5"]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layouts = [
    layout.MonadTall(border_focus="#000000", border_width=1, margin=3),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono NF", 
    fontsize=13,
    padding=5,
    background="#000000"
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(active='#ffffff',),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={'launch': ("#ff0000", "#ffffff"),},
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.CurrentLayout(),
                widget.Battery(format='{percent:2.0%} '),
                widget.Clock(format='%Y-%m-%d'),
                widget.QuickExit(default_text="",countdown_format='{}', countdown_start=3)
            ],
            19,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
