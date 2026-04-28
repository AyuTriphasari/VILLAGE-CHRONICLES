## ============================================================
## VILLAGE CHRONICLES — Day / Time System
## ============================================================

## Time order: morning → afternoon → evening → night → (next day morning)
define TIME_ORDER = ["morning", "afternoon", "evening", "night"]

define TIME_LABELS = {
    "morning":   "Morning",
    "afternoon": "Afternoon",
    "evening":   "Evening",
    "night":     "Night",
}

## Advance time by one slot. If night → advance day.
label advance_time:
    python:
        idx = TIME_ORDER.index(time_of_day)
        if idx < len(TIME_ORDER) - 1:
            time_of_day = TIME_ORDER[idx + 1]
        else:
            # New day
            time_of_day = "morning"
            day_count += 1
            daily_income = 0
            shop_open = False
            flag_gifted_ino_today    = False
            flag_gifted_sakura_today = False
            flag_gifted_hinata_today = False
            # Random daily mood for met characters
            import random
            moods = ["happy", "normal", "normal", "annoyed"]
            if ino_met:
                ino_mood = random.choice(moods)
            if sakura_met:
                sakura_mood = random.choice(moods)
            if hinata_met:
                hinata_mood = random.choice(moods)
            # Temari countdown
            if temari_met and temari_days_left > 0:
                temari_days_left -= 1
    return

## Shortcut: skip to next day immediately
label skip_to_next_day:
    $ time_of_day = "night"
    call advance_time
    return

## Helper: check if it's currently a given time
## Usage: if is_time("evening"):
init python:
    def is_time(t):
        return time_of_day == t

    def is_day_or_later(n):
        return day_count >= n

    def can_afford(amount):
        return ryo >= amount

    def spend_ryo(amount):
        global ryo
        if ryo >= amount:
            ryo -= amount
            return True
        return False

    def earn_ryo(amount):
        global ryo, daily_income
        ryo += amount
        daily_income += amount
