## ============================================================
## VILLAGE CHRONICLES — Shop System
## ============================================================

## Income per open session based on shop level
define SHOP_INCOME = {1: 80, 2: 150, 3: 260}
define SHOP_UPGRADE_COST = {1: 500, 2: 1200}

## Items unlocked per shop level
define SHOP_ITEMS_BY_LEVEL = {
    1: ["herbs", "flowers"],
    2: ["herbs", "flowers", "kunai_parts", "sweets"],
    3: ["herbs", "flowers", "kunai_parts", "sweets", "medicine"],
}

define ITEM_NAMES = {
    "herbs":       "Medicinal Herbs",
    "flowers":     "Fresh Flowers",
    "kunai_parts": "Kunai Parts",
    "sweets":      "Konoha Sweets",
    "medicine":    "Healing Salve",
}

define ITEM_DESCS = {
    "herbs":       "Useful for healing and cooking. Popular with medic-nin.",
    "flowers":     "Bright and fragrant. A thoughtful gift.",
    "kunai_parts": "Spare parts for weapon maintenance.",
    "sweets":      "Local Konoha treats. Hard to resist.",
    "medicine":    "Premium healing salve. High demand.",
}

## ── Shop main screen ──────────────────────────────────────────
screen shop_screen():
    modal True
    zorder 200
    style_prefix "shop"

    add "#0a1610ee"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 720
        ysize 500
        background "#0d2218ee"
        xpadding 30
        ypadding 24

        vbox:
            xfill True
            spacing 16

            ## Header
            hbox:
                xfill True
                text "YOUR SHOP" size 22 color "#c8a550" bold True xalign 0.0
                text "Lv.[shop_level]" size 14 color "#8aaa84" xalign 1.0 yalign 1.0

            ## Divider
            frame:
                xfill True
                ysize 1
                background "#c8a55066"

            ## Stock list
            viewport:
                scrollbars "vertical"
                mousewheel True
                ysize 250
                xfill True

                vbox:
                    spacing 10
                    for item_key in SHOP_ITEMS_BY_LEVEL[shop_level]:
                        $ item_data = shop_stock.get(item_key, {"price": 0, "stock": 0})
                        frame:
                            background "#0a1e1200"
                            xfill True
                            ysize 56
                            xpadding 12
                            ypadding 8
                            hbox:
                                spacing 12
                                xfill True
                                vbox:
                                    xsize 500
                                    spacing 3
                                    text "[ITEM_NAMES[item_key]]" size 15 color "#f0ead8"
                                    text "[ITEM_DESCS[item_key]]" size 11 color "#8aaa84"
                                vbox:
                                    xfill True
                                    text "₩[item_data['price']]" size 13 color "#c8a550" xalign 1.0
                                    text "Stock: [item_data['stock']]" size 11 color "#8aaa84" xalign 1.0

            vbox:
                xfill True
                spacing 12

                if shop_level < 3:
                    $ upgrade_cost = SHOP_UPGRADE_COST[shop_level]
                    textbutton "Upgrade Shop (₩[upgrade_cost])":
                        action Function(upgrade_shop)
                        sensitive ryo >= upgrade_cost
                        style "shop_wide_button"
                else:
                    text "Shop fully upgraded." size 13 color "#c8a550" xalign 0.5

                ## Footer
                frame:
                    xfill True
                    ysize 1
                    background "#c8a55066"

                hbox:
                    spacing 14
                    xfill True

                    if not shop_open:
                        textbutton "Open Shop (earn ₩[SHOP_INCOME[shop_level]])":
                            action [
                                Function(open_shop),
                                Hide("shop_screen"),
                                Return("opened")
                            ]
                            style "shop_primary_button"
                    else:
                        text "Shop already opened today." size 13 color "#8aaa84" yalign 0.5 xsize 506

                    textbutton "Close":
                        action [Hide("shop_screen"), Return("close")]
                        style "shop_close_button"

style shop_wide_button is button:
    xsize 660
    ysize 38
    background Frame("gui/button/choice_idle_background.png", Borders(100, 5, 100, 5), tile=False)
    hover_background Frame("gui/button/choice_hover_background.png", Borders(100, 5, 100, 5), tile=False)
    insensitive_background Frame("gui/button/choice_idle_background.png", Borders(100, 5, 100, 5), tile=False)

style shop_wide_button_text is button_text:
    size 18
    xalign 0.5
    color "#a0b89a"
    hover_color "#ffffff"
    insensitive_color "#8888887f"

style shop_primary_button is shop_wide_button:
    xsize 506

style shop_close_button is shop_wide_button:
    xsize 140

## ── Python helpers ────────────────────────────────────────────
init python:
    def open_shop():
        global shop_open, ryo, daily_income
        if not shop_open:
            income = SHOP_INCOME[shop_level]
            shop_open = True
            ryo += income
            daily_income += income

    def upgrade_shop():
        global shop_level, ryo
        cost = SHOP_UPGRADE_COST.get(shop_level, 99999)
        if shop_level < 3 and ryo >= cost:
            ryo -= cost
            shop_level += 1
            renpy.notify("Shop upgraded to level %s." % shop_level)
            return True
        renpy.notify("Not enough ryo to upgrade.")
        return False

    def buy_item(item_key, qty=1):
        global ryo, inventory
        item = shop_stock.get(item_key)
        if not item:
            return False
        cost = item["price"] * qty
        if ryo >= cost and item["stock"] >= qty:
            ryo -= cost
            item["stock"] -= qty
            inventory[item_key] = inventory.get(item_key, 0) + qty
            return True
        return False

## ── Label to call shop from script ───────────────────────────
label visit_shop:
    call show_hud
    call screen shop_screen
    return
