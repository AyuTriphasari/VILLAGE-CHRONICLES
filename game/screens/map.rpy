## ============================================================
## VILLAGE CHRONICLES — Village Map Screen
## ============================================================

init python:
    MAP_LOCATION_DATA = {
        "shop": {
            "name": "Your Shop",
            "subtitle": "home base",
            "label": "map_visit_shop",
            "times": ["morning", "afternoon", "evening"],
            "pos": (208, 424),
        },
        "market": {
            "name": "Market Street",
            "subtitle": "supplies and rumors",
            "label": "map_visit_market",
            "times": ["morning", "afternoon"],
            "pos": (498, 348),
        },
        "flower_shop": {
            "name": "Ino's Flower Shop",
            "subtitle": "flowers and trouble",
            "label": "map_visit_flower_shop",
            "times": ["morning", "afternoon", "evening"],
            "pos": (696, 258),
        },
        "training_ground": {
            "name": "Training Ground",
            "subtitle": "shinobi practice",
            "label": "map_visit_training_ground",
            "times": ["morning", "afternoon"],
            "pos": (980, 238),
        },
        "park": {
            "name": "Village Park",
            "subtitle": "quiet walks",
            "label": "map_visit_park",
            "times": ["afternoon", "evening"],
            "pos": (832, 514),
        },
        "ramen": {
            "name": "Ramen Bar",
            "subtitle": "Ichiraku counter",
            "label": "map_visit_ramen",
            "times": ["afternoon", "evening"],
            "pos": (1080, 452),
        },
    }

    def map_location_available(location_key):
        return time_of_day in MAP_LOCATION_DATA[location_key]["times"]

    def map_location_subtitle(location_key):
        if location_key == "flower_shop" and ino_met:
            if time_of_day in ["morning", "afternoon"]:
                return "Ino is working"
            return "lights still on"
        if location_key == "park" and ino_met and time_of_day == "evening":
            return "Ino may pass by"
        return MAP_LOCATION_DATA[location_key]["subtitle"]

screen village_map():
    modal True
    zorder 100

    add "images/bg/bg_village_map.png"
    add "#06110aaa"

    frame:
        xalign 0.5
        yalign 0.05
        xsize 760
        background "#0a1610dd"
        xpadding 24
        ypadding 14

        hbox:
            spacing 26
            vbox:
                spacing 2
                text "KONOHA VILLAGE" size 28 color "#c8a550" bold True
                text "Day [day_count] • [TIME_LABELS[time_of_day]] • ₩[ryo]" size 15 color "#f0ead8"
            text "choose a destination" size 14 color "#8aaa84" yalign 0.72

    for location_key, location_data in MAP_LOCATION_DATA.items():
        $ available = map_location_available(location_key)
        $ px, py = location_data["pos"]
        fixed:
            xpos px
            ypos py
            xsize 214
            ysize 74
            anchor (0.5, 0.5)

            if available:
                textbutton location_data["name"]:
                    xfill True
                    yfill True
                    action Return(location_data["label"])
                    style "map_location_button"
            else:
                frame:
                    xfill True
                    yfill True
                    background "#07110dcc"
                    xpadding 12
                    ypadding 8
                    vbox:
                        spacing 2
                        text location_data["name"] size 15 color "#777c6c" bold True
                        text "closed now" size 11 color "#777c6c"

            vbox:
                xpos 14
                ypos 38
                xsize 186
                text map_location_subtitle(location_key) size 11 color ("#f0ead8" if available else "#777c6c")

            if location_key == "flower_shop" and ino_met and available:
                frame:
                    xalign 1.0
                    yalign 0.0
                    background "#dc82a0dd"
                    xpadding 7
                    ypadding 2
                    text "Ino" size 10 color "#160810" bold True

    frame:
        xalign 0.5
        yalign 0.94
        background "#0a1610dd"
        xpadding 18
        ypadding 10

        hbox:
            spacing 18
            text "unavailable locations reopen later" size 13 color "#8aaa84" yalign 0.5
            textbutton "Stay Here":
                action Return("map_cancel")
                style "map_footer_button"

style map_location_button is button:
    background "#0d2218dd"
    hover_background "#2d4129ee"
    selected_background "#2d4129ee"
    xpadding 12
    ypadding 8

style map_location_button_text is button_text:
    size 15
    color "#f0ead8"
    hover_color "#ffffff"
    bold True
    xalign 0.5
    yalign 0.28

style map_footer_button is button:
    xsize 150
    ysize 34
    background Frame("gui/button/choice_idle_background.png", Borders(100, 5, 100, 5), tile=False)
    hover_background Frame("gui/button/choice_hover_background.png", Borders(100, 5, 100, 5), tile=False)

style map_footer_button_text is button_text:
    size 14
    xalign 0.5
    yalign 0.5
    color "#f0ead8"
    hover_color "#ffffff"
