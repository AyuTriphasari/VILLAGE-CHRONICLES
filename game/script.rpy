## ============================================================
## VILLAGE CHRONICLES — Main Script
## ============================================================

## ── Characters ───────────────────────────────────────────────
define narrator = Character(None)
define mc       = Character("[player_name]", color="#c8a550")
define ino      = Character("Ino", color="#dc82a0")
define sakura   = Character("Sakura", color="#ff6b8a")
define hinata   = Character("Hinata", color="#a0c4ff")
define temari   = Character("Temari", color="#d4c050")
define tenten   = Character("TenTen", color="#e09060")

## ── Images (placeholders until sprites are generated) ────────
## Backgrounds
image bg_room       = "images/bg/bg_shop_interior.png"
image bg_shop       = "images/bg/bg_shop_interior.png"
image bg_morning    = "images/bg/bg_shop_interior.png"
image bg_street     = "images/bg/bg_market_day.png"
image bg_flower     = "images/bg/bg_flower_shop.png"
image bg_park       = "images/bg/bg_park_day.png"

## Character sprites
image ino_normal    = "images/sprites/ino/ino_normal.webp"
image ino_happy     = "images/sprites/ino/ino_happy.webp"
image ino_shy       = "images/sprites/ino/ino_shy.webp"
image ino_surprised = "images/sprites/ino/ino_surprised.webp"
image ino_annoyed   = "images/sprites/ino/ino_annoyed.webp"
image ino_blush     = "images/sprites/ino/ino_blush.webp"
image ino_seductive = "images/sprites/ino/ino_seductive.webp"
image ino_intimate1 = "images/sprites/ino/ino_intimate1.webp"
image ino_intimate2 = "images/sprites/ino/ino_intimate2.webp"

## ── Start ────────────────────────────────────────────────────
label start:
    $ renpy.block_rollback()
    call show_hud

    scene bg_morning
    with dissolve

    ## ── DAY 1: MORNING — Arrival ──────────────────────────
    "The morning air carries the scent of pine and distant ramen."
    "You stand in front of a modest shop on a quiet street in Konoha."
    "The sign above the door reads: {b}Ryu's Supply Co.{/b}"
    "You moved here two weeks ago. Today is your first real day open for business."

    mc "Alright... let's make this work."

    "You push open the door. The wooden floor creaks. Shelves half-stocked, but it's yours."

    ## ── Shop tutorial ─────────────────────────────────────
    if not flag_shop_tutorial_done:
        "A note from the previous owner is pinned to the counter."
        "{i}\"Morning customers come early. Open the shop and stock up. The village runs on trust — and ryo.\"{/i}"
        $ flag_shop_tutorial_done = True

    menu:
        "What do you want to do first?"

        "Open the shop for business.":
            call visit_shop
            if shop_open:
                mc "Not bad for day one."
                $ renpy.notify("Shop opened! Earned ₩[SHOP_INCOME[shop_level]]")

        "Explore the street first.":
            call explore_morning

    call advance_time  # morning → afternoon
    jump day_1_afternoon

## ── DAY 1: AFTERNOON ──────────────────────────────────────────
label day_1_afternoon:
    scene bg_street
    with dissolve

    "The village market street is lively in the afternoon."
    "Shinobi and civilians weave between stalls selling food, tools, and supplies."
    "You step outside to get a feel for the neighborhood."

    "Just as you turn the corner — someone nearly walks straight into you."

    ## First Ino meeting
    $ ino_met = True
    $ ino_affinity += 5

    show ino_normal at center
    with dissolve

    ino "Whoa — watch where you're going!"
    mc "Sorry about that. I was just—"
    ino "Wait. You're the new person who took over old Tanaka's shop, aren't you?"

    mc "That's me. Name's [player_name]. Just opened today actually."

    ino "Hmm."
    "She looks you over with sharp blue eyes, arms crossed."
    ino "I'm Ino. My family's flower shop is right next to yours. So I guess we're neighbors."

    menu:
        "Nice to meet you, Ino.":
            mc "Nice to meet you, Ino. I'll try not to walk into you again."
            ino "Ha. See that you don't."
            $ ino_affinity += 5
            $ ino_mood = "happy"

        "Small world.":
            mc "Small world. Looks like we'll be seeing a lot of each other."
            ino "Don't push your luck."
            $ ino_affinity += 2

    hide ino_normal
    with dissolve

    "She walks off toward her shop, glancing back once."
    "Something tells you this village is going to be interesting."

    call advance_time  # afternoon → evening
    jump day_1_evening

## ── DAY 1: EVENING ────────────────────────────────────────────
label day_1_evening:
    scene bg_shop
    with dissolve

    "You close up the shop as the sun dips behind the Hokage monument."
    "Not a bad first day."

    "You count the ryo earned: {b}₩[daily_income]{/b}"

    if daily_income > 0:
        "The shop is starting to feel real."
    else:
        "You remind yourself to open the shop earlier tomorrow."

    menu:
        "Rest up. Tomorrow's another day.":
            call advance_time   # evening → night
            call advance_time   # night → day 2
            jump day_loop

        "Stay up and organize the shop.":
            $ player_gen += 1
            "You spend the evening arranging shelves and planning inventory."
            "It feels satisfying. Your {b}Generosity{/b} increased."
            call advance_time
            call advance_time
            jump day_loop

## ── DAILY LOOP (Day 2+) ───────────────────────────────────────
label day_loop:
    call show_hud

    if time_of_day == "night":
        jump night_end

    scene bg_morning
    with dissolve

    "— Day [day_count] —"
    if time_of_day == "morning":
        "The morning light filters through the shop window."
    elif time_of_day == "afternoon":
        "The village outside is bright and loud with afternoon traffic."
    else:
        "Evening settles over Konoha, turning the shop windows gold."

    menu:
        "Day [day_count] — [TIME_LABELS[time_of_day]] — What will you do?"

        "Open the shop." if time_of_day == "morning" and not shop_open:
            call visit_shop
            call advance_time

        "Walk around the village." if time_of_day != "evening":
            call explore_morning
            call advance_time

        "Visit Ino's flower shop." if ino_met:
            call visit_ino_shop
            call advance_time

        "Wait a while.":
            call advance_time

    jump day_loop

label night_end:
    scene bg_shop
    with dissolve

    "The shop is quiet. Another day is done."

    if daily_income > 0:
        "Today's earnings: {b}₩[daily_income]{/b}."
    else:
        "No sales today. Even legends have slow Tuesdays."

    menu:
        "End the day?"

        "Sleep until morning.":
            call advance_time
            jump day_loop

## ── LOCATION: EXPLORE MORNING ─────────────────────────────────
label explore_morning:
    "You walk through the quiet morning streets."
    "The village is just waking up. The smell of fresh rice and miso drifts from open doors."
    return

## ── LOCATION: INO'S FLOWER SHOP ───────────────────────────────
label visit_ino_shop:
    scene bg_flower
    with dissolve

    show ino_normal at center
    with dissolve

    "The flower shop next door is small but bursting with color."
    "Ino is arranging a display when you walk in."

    python:
        if ino_mood == "happy":
            greeting = "Oh, it's you. Good timing actually."
        elif ino_mood == "annoyed":
            greeting = "What do you want? I'm busy."
        else:
            greeting = "Hey. Need something?"

    ino "[greeting]"

    menu:
        "Just saying hi.":
            mc "Just dropping by. Neighbor thing."
            ino "...Fine. Don't break anything."
            $ ino_affinity += 3

        "I wanted to buy some flowers.":
            if spend_ryo(80):
                mc "I'll take whatever looks freshest."
                ino "Good taste."
                $ inventory["flowers"] = inventory.get("flowers", 0) + 1
                $ ino_affinity += 8
                $ flag_gifted_ino_today = True
                "She wraps a small bouquet with practiced hands."
            else:
                mc "Actually... I might be short on ryo."
                ino "You came to buy flowers without money? Bold strategy."

        "Just passing by." if ino_mood != "annoyed":
            mc "Nothing, just passing by."
            ino "Then pass by faster."

    hide ino_normal
    with dissolve
    return
