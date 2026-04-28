## ============================================================
## VILLAGE CHRONICLES — HUD Screen
## ============================================================

## Colors (matching gui.rpy palette)
define HUD_GOLD       = "#c8a550"
define HUD_SAKURA     = "#dc82a0"
define HUD_DARK       = "#0a1610ee"
define HUD_TEXT       = "#f0ead8"
define HUD_MUTED      = "#8aaa84"

## Show HUD during gameplay
screen hud():
    zorder 10
    style_prefix "hud"

    ## ── Top bar ───────────────────────────────────────────
    frame:
        xalign 0.0
        yalign 0.0
        xoffset 12
        yoffset 12
        xsize 340
        ysize 64
        background Frame("gui/hud_bar.png", 8, 8) if renpy.loadable("gui/hud_bar.png") else "#0a1610dd"
        xpadding 14
        ypadding 8

        hbox:
            spacing 24
            vbox:
                spacing 2
                text "DAY [day_count]" size 11 color HUD_GOLD bold True
                text "[TIME_LABELS[time_of_day]]" size 13 color HUD_TEXT

            vbox:
                spacing 2
                text "RYO" size 11 color HUD_GOLD bold True
                text "₩[ryo]" size 13 color HUD_TEXT

    ## ── Affinity sidebar (right) ──────────────────────────
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -12
        yoffset 12
        xsize 160
        background "#0a1610cc"
        xpadding 12
        ypadding 10

        vbox:
            spacing 8

            if ino_met:
                $ _ino_pct = ino_affinity / 100.0
                vbox:
                    spacing 3
                    hbox:
                        text "Ino" size 11 color HUD_SAKURA
                        text " [ino_affinity]" size 11 color HUD_MUTED
                    bar:
                        value ino_affinity
                        range 100
                        xsize 130
                        ysize 6
                        left_bar "#dc82a0cc"
                        right_bar "#1e3e22"

            if sakura_met:
                vbox:
                    spacing 3
                    hbox:
                        text "Sakura" size 11 color HUD_SAKURA
                        text " [sakura_affinity]" size 11 color HUD_MUTED
                    bar:
                        value sakura_affinity
                        range 100
                        xsize 130
                        ysize 6
                        left_bar "#dc82a0cc"
                        right_bar "#1e3e22"

            if hinata_met:
                vbox:
                    spacing 3
                    hbox:
                        text "Hinata" size 11 color HUD_SAKURA
                        text " [hinata_affinity]" size 11 color HUD_MUTED
                    bar:
                        value hinata_affinity
                        range 100
                        xsize 130
                        ysize 6
                        left_bar "#dc82a0cc"
                        right_bar "#1e3e22"

## Show/hide HUD helpers
label show_hud:
    show screen hud
    return

label hide_hud:
    hide screen hud
    return
