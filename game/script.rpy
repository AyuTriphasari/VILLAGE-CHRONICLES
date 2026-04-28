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
image bg_park_evening = "images/bg/bg_park_evening.png"
image bg_training   = "images/bg/bg_training_ground.png"
image bg_ramen      = "images/bg/bg_ramen_bar.png"
image bg_market_night = "images/bg/bg_market_night.png"
image bg_village_map = "images/bg/bg_village_map.png"

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

    call open_village_map

    if time_of_day == "night":
        jump night_end

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


## ── VILLAGE MAP ROUTER ───────────────────────────────────────
label open_village_map:
    call screen village_map
    $ destination = _return

    if destination == "map_cancel":
        "You stay near the shop and let the village noise pass by."
        call advance_time
        return

    call expression destination
    call advance_time
    return

label map_visit_shop:
    scene bg_shop
    with dissolve

    if not shop_open:
        "Back at your shop, the shelves wait like they are judging your work ethic."
        call visit_shop
    else:
        "The shop is already handled for today."
        "You straighten a few displays and count the coins again, because apparently that is your personality now."
    return

label map_visit_market:
    if time_of_day == "evening":
        scene bg_market_night
    else:
        scene bg_street
    with dissolve

    "Market Street hums with merchants, shinobi, and civilians trading gossip like currency."

    menu:
        "Browse the stalls?"

        "Look for useful supplies.":
            if spend_ryo(50):
                $ inventory["herbs"] = inventory.get("herbs", 0) + 1
                "You buy a bundle of medicinal herbs. Practical. Almost suspiciously responsible."
            else:
                "You check your pouch and decide window-shopping is a valid lifestyle."

        "Listen for rumors.":
            $ player_wit += 1
            "You pick up enough gossip to sound informed at dinner. Your Wit increases."
    return

label map_visit_flower_shop:
    call visit_ino_shop
    return

label map_visit_training_ground:
    scene bg_training
    with dissolve

    "The training ground is scarred with kunai marks and old footprints."
    "A few shinobi drill nearby while you try very hard to look like you belong."

    menu:
        "How do you spend the visit?"

        "Practice basic movement.":
            $ player_charm += 1
            "You work up a sweat and only embarrass yourself twice. Charm increases."

        "Collect discarded parts.":
            $ inventory["kunai_parts"] = inventory.get("kunai_parts", 0) + 1
            "You find usable kunai parts near a target post. TenTen would probably call it trash. You call it inventory."
    return

label map_visit_park:
    if time_of_day == "evening":
        scene bg_park_evening
    else:
        scene bg_park
    with dissolve

    "The village park is quieter than the market, all rustling leaves and distant laughter."

    if ino_met and day_count == 6 and time_of_day == "evening" and not flag_ino_day6_done:
        call ino_act1_day6_park
        return
    elif ino_met and time_of_day == "evening":
        show ino_shy at center
        with dissolve
        "You spot Ino near the path, pretending she was not also enjoying the quiet."
        ino "What? People are allowed to walk."
        mc "Never accused you of anything."
        ino "Good. Keep being smart."
        $ ino_affinity += 4
        hide ino_shy
        with dissolve
    else:
        $ player_charm += 1
        "A slow walk clears your head. Charm increases."
    return

label map_visit_ramen:
    scene bg_ramen
    with dissolve

    "Ichiraku is warm, loud, and dangerously good at making you spend money."

    menu:
        "Order ramen?"

        "Buy a bowl. (₩60)":
            if spend_ryo(60):
                $ player_gen += 1
                "The broth hits like a small religious experience. Generosity increases."
            else:
                "You do the tragic math and skip dinner. Character building, probably."

        "Just enjoy the atmosphere.":
            "You sit for a while and listen to the village breathe."
    return

## ── LOCATION: EXPLORE MORNING ─────────────────────────────────
label explore_morning:
    "You walk through the quiet morning streets."
    "The village is just waking up. The smell of fresh rice and miso drifts from open doors."
    return

## ── LOCATION: INO'S FLOWER SHOP ───────────────────────────────
label visit_ino_shop:
    if day_count == 2 and not flag_ino_day2_done:
        call ino_act1_day2
    elif day_count == 3 and not flag_ino_day3_done:
        call ino_act1_day3
    elif day_count == 4 and not flag_ino_day4_done:
        call ino_act1_day4
    elif day_count == 5 and not flag_ino_day5_done:
        call ino_act1_day5
    elif day_count == 6 and not flag_ino_day6_done:
        call ino_act1_day6_flower_backup
    elif day_count >= 7 and not flag_ino_day7_done:
        call ino_act1_day7
    else:
        call ino_flower_shop_repeat
    return

label ino_flower_shop_repeat:
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
            ino "Neighbor thing. Sure. Very official."
            $ ino_affinity += 2

        "I wanted to buy some flowers.":
            if spend_ryo(80):
                mc "I'll take whatever looks freshest."
                ino "Good taste. Finally, a customer with survival instincts."
                $ inventory["flowers"] = inventory.get("flowers", 0) + 1
                $ ino_affinity += 4
                $ flag_gifted_ino_today = True
                "She wraps a small bouquet with practiced hands."
            else:
                mc "Actually... I might be short on ryo."
                ino "You came to buy flowers without money? Bold strategy."

        "Ask how business is going." if ino_mood != "annoyed":
            mc "Busy day?"
            ino "Busy enough. People suddenly remember flowers exist when they mess up."
            mc "Sounds profitable."
            ino "Emotionally exhausting, but yes."
            $ ino_trust += 2

    hide ino_normal
    with dissolve
    return

## ── INO ACT 1 EVENTS ─────────────────────────────────────────
label ino_act1_day2:
    scene bg_flower
    with dissolve

    show ino_annoyed at center
    with dissolve

    "You find Ino standing outside the flower shop with a watering can in one hand and a very judgmental look on her face."
    ino "So. New shop guy."
    mc "That sounds like a title I haven't earned yet."
    ino "You earned it when your front display started leaning into my flower buckets."

    mc "It is not leaning. It is... exploring the neighborhood."
    ino "Your shelf has more courage than common sense."

    menu:
        "Promise to fix it.":
            mc "I'll fix it before it starts a diplomatic incident."
            show ino_happy at center
            ino "Good. Konoha has survived wars. I'd hate to see it fall to bad carpentry."
            $ ino_affinity += 5
            $ ino_trust += 2

        "Tease her back.":
            mc "You came all the way over just to inspect my shelf? I'm honored."
            ino "Don't flatter yourself. I protect innocent flowers."
            mc "A noble calling."
            ino "Someone has to have standards around here."
            $ ino_affinity += 4
            $ player_wit += 1

    show ino_normal at center
    ino "Anyway... your shop is rough, but it has potential."
    mc "I'll take that as a compliment."
    ino "Take it as a warning. Potential means people expect you to improve."

    $ flag_ino_day2_done = True
    hide ino_normal
    with dissolve
    return

label ino_act1_day3:
    scene bg_flower
    with dissolve

    show ino_normal at center
    with dissolve

    "A small bell rings as you step into the Yamanaka flower shop."
    "Ino is behind the counter, trimming stems with quick, precise cuts."
    ino "If you're here to apologize to my flower buckets, they're listening."
    mc "I brought money. That usually works better."

    show ino_happy at center
    ino "Now you're learning."

    "She points at three small arrangements near the counter."
    ino "Beginner lesson. Flowers aren't just pretty. They say things when people are too awkward to use words."
    mc "That sounds dangerous in this village."
    ino "Extremely. That's why professionals exist."

    menu:
        "Buy a simple bouquet. (₩80)":
            if spend_ryo(80):
                $ inventory["flowers"] = inventory.get("flowers", 0) + 1
                $ flag_gifted_ino_today = True
                mc "I'll take this one."
                ino "Safe choice. Friendly, not desperate."
                mc "There are desperate flowers?"
                ino "There are desperate customers."
                $ ino_affinity += 6
                $ ino_trust += 3
            else:
                mc "I'll come back after my wallet recovers."
                show ino_annoyed at center
                ino "The tragic life of a business owner."
                $ ino_affinity += 1

        "Ask her to explain the meanings.":
            mc "Teach me before I accidentally declare war with a bouquet."
            show ino_happy at center
            ino "Smart. Yellow is friendship. White can be respect. Red is... don't start with red."
            mc "Noted. Avoid emotional explosives."
            ino "Exactly."
            $ ino_trust += 5
            $ ino_affinity += 3

    $ flag_ino_day3_done = True
    hide ino_happy
    hide ino_annoyed
    hide ino_normal
    with dissolve
    return

label ino_act1_day4:
    scene bg_flower
    with dissolve

    show ino_normal at center
    with dissolve

    "In the afternoon, the flower shop is quieter."
    "Ino is on a small stool, reaching for a box on the top shelf and pretending the height problem does not exist."
    mc "Need help?"
    show ino_annoyed at center
    ino "I need the shelf to be less smug."
    mc "That's not a no."

    menu:
        "Help her with the box.":
            "You step closer and lift the box down before it can commit violence."
            show ino_shy at center
            ino "...Thanks."
            mc "Anytime."
            ino "Don't make it weird. It was shelf logistics."
            $ ino_trust += 6
            $ ino_affinity += 5

        "Let her handle it.":
            mc "I'll stand here as emotional support."
            show ino_annoyed at center
            ino "Useless, but honest."
            "She manages to pull the box down, then nearly drops it into your arms anyway."
            mc "See? Teamwork."
            ino "Accidental teamwork."
            $ ino_affinity += 3

    show ino_normal at center
    "The box is full of old ribbons, price tags, and small glass vases."
    ino "Mom says the shop looks better when everything has a place."
    mc "She sounds strict."
    ino "She notices everything. It's a family curse."
    mc "You notice everything too."
    show ino_shy at center
    ino "Only obvious things."

    $ flag_ino_day4_done = True
    hide ino_shy
    hide ino_annoyed
    hide ino_normal
    with dissolve
    return

label ino_act1_day5:
    scene bg_flower
    with dissolve

    show ino_normal at center
    with dissolve

    "You stop by near closing time and find Ino sorting receipts with the grim focus of someone fighting paperwork."
    ino "If you're here to buy something, excellent. If you're here to talk, bring snacks."

    if ino_affinity >= 15:
        mc "You look like the receipts are winning."
        show ino_happy at center
        ino "They are organized chaos. Very different."
        mc "Need a second pair of eyes?"
        ino "From you?"
        mc "I can count to at least twenty."
        ino "Ambitious."

        "She lets you help sort the slips by supplier."
        "It is not glamorous, but the quiet rhythm feels comfortable."

        ino "You're less annoying when you're useful."
        mc "I'll put that on my shop sign."
        show ino_shy at center
        ino "Don't. I might have to deny saying it."
        $ ino_trust += 8
        $ ino_affinity += 6
    else:
        show ino_annoyed at center
        ino "You know, neighbors usually visit before asking for favors."
        mc "Fair. I have been buried under shop work."
        ino "Then unbury yourself properly next time."
        "The conversation stays polite, but the door does not open much further today."
        $ ino_affinity += 1

    $ flag_ino_day5_done = True
    hide ino_shy
    hide ino_happy
    hide ino_annoyed
    hide ino_normal
    with dissolve
    return

label ino_act1_day6_flower_backup:
    scene bg_flower
    with dissolve

    show ino_normal at center
    with dissolve

    "Ino is busy with customers, so your visit turns into a quick exchange across the counter."
    ino "Rain check. Unless you can clone yourself and handle three customers."
    mc "One of me already feels legally complicated."
    show ino_happy at center
    ino "Good answer."
    $ ino_affinity += 2
    $ flag_ino_day6_done = True
    hide ino_happy
    hide ino_normal
    with dissolve
    return

label ino_act1_day6_park:
    scene bg_park_evening
    with dissolve

    show ino_shy at center
    with dissolve

    "The park is quiet in the evening, washed in soft orange light."
    "You find Ino near the path, holding a paper bag from the market."
    ino "Before you say anything, no, I'm not following you."
    mc "I was going to say hello."
    ino "Good. Keep it normal."

    "For a while, you walk the same path without making a big deal out of it."
    "Ino talks about difficult customers. You talk about the shop refusing to feel like home yet."

    show ino_normal at center
    ino "It takes time."
    mc "The shop?"
    ino "Places. People. All of it."

    menu:
        "Admit you're still adjusting.":
            mc "Some mornings I still feel like I walked into someone else's life."
            show ino_shy at center
            ino "Yeah. I know that feeling."
            "She does not explain, and you do not push."
            $ ino_trust += 8
            $ ino_affinity += 4

        "Keep the mood light.":
            mc "At least the village has good ramen and hostile flower girls."
            show ino_annoyed at center
            ino "Hostile?"
            mc "Professionally intimidating."
            show ino_happy at center
            ino "Better."
            $ ino_affinity += 6

    $ flag_ino_day6_done = True
    hide ino_happy
    hide ino_annoyed
    hide ino_shy
    hide ino_normal
    with dissolve
    return

label ino_act1_day7:
    scene bg_flower
    with dissolve

    show ino_normal at center
    with dissolve

    "At the end of the week, Ino stops you before you can even reach the counter."
    ino "Come here. I need an opinion from someone who doesn't work here."
    mc "Dangerous choice."
    ino "Low stakes. Ribbon colors."

    "She lays three ribbons across a bouquet: pale yellow, deep purple, and soft white."
    "You give an honest answer. She changes two things anyway."

    show ino_happy at center
    ino "Not terrible."
    mc "From you, that sounds like applause."
    ino "Don't get greedy."

    if ino_trust >= 15:
        show ino_shy at center
        ino "Still... you're easier to talk to than I expected."
        mc "I had a worse reputation in your head?"
        ino "You were a mystery neighbor with suspicious shelves. Of course."
        mc "And now?"
        ino "Now you're... less suspicious."
        "It is a small thing, but the way she says it makes the shop feel warmer."
        $ flag_ino_act2_hint = True
        $ ino_affinity += 6
        $ ino_trust += 5
    else:
        ino "You survived your first week. That's something."
        mc "Barely."
        ino "Barely counts. For now."
        $ ino_affinity += 3

    $ flag_ino_day7_done = True
    hide ino_shy
    hide ino_happy
    hide ino_normal
    with dissolve
    return
