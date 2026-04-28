## ============================================================
## VILLAGE CHRONICLES — Game Variables
## ============================================================

## ── PLAYER STATS ────────────────────────────────────────────
default player_name    = "Ryu"
default player_charm   = 5      # affects dialogue options
default player_wit     = 5      # affects clever choices
default player_gen     = 5      # generosity (gift impact)

## ── ECONOMY ─────────────────────────────────────────────────
default ryo            = 500    # starting money
default shop_level     = 1      # 1=basic, 2=upgraded, 3=premium
default shop_open      = False  # was shop opened today?
default daily_income   = 0      # income earned today

## ── TIME SYSTEM ─────────────────────────────────────────────
default day_count      = 1
# time_of_day: "morning" / "afternoon" / "evening" / "night"
default time_of_day    = "morning"

## ── CHARACTER: INO ──────────────────────────────────────────
default ino_affinity   = 0      # 0–100
default ino_trust      = 0      # 0–100
default ino_mood       = "normal"   # daily: happy / normal / annoyed
default ino_met        = False
default ino_act        = 1      # current act (1/2/3)
default ino_ending     = None   # None / "lovers" / "fwb" / "heartbreak"

## ── CHARACTER: SAKURA ───────────────────────────────────────
default sakura_affinity = 0
default sakura_trust    = 0
default sakura_mood     = "normal"
default sakura_met      = False
default sakura_act      = 1
default sakura_ending   = None

## ── CHARACTER: HINATA ───────────────────────────────────────
default hinata_affinity = 0
default hinata_trust    = 0
default hinata_mood     = "normal"
default hinata_met      = False
default hinata_act      = 1
default hinata_ending   = None

## ── CHARACTER: TEMARI ───────────────────────────────────────
default temari_affinity = 0
default temari_trust    = 0
default temari_met      = False
default temari_days_left = 7    # limited-time route

## ── CHARACTER: TENTEN ───────────────────────────────────────
default tenten_affinity = 0
default tenten_trust    = 0
default tenten_met      = False

## ── FLAGS ────────────────────────────────────────────────────
default flag_gifted_ino_today    = False
default flag_gifted_sakura_today = False
default flag_gifted_hinata_today = False
default flag_intro_done          = False
default flag_shop_tutorial_done  = False
default flag_day_2_intro_done    = False

default flag_ino_day2_done      = False
default flag_ino_day3_done      = False
default flag_ino_day4_done      = False
default flag_ino_day5_done      = False
default flag_ino_day6_done      = False
default flag_ino_day7_done      = False
default flag_ino_act2_hint      = False

default flag_ino_day8_done      = False
default flag_ino_day9_done      = False
default flag_ino_day10_done     = False
default flag_ino_day11_done     = False
default flag_ino_day12_done     = False
default flag_ino_day13_done     = False
default flag_ino_day14_done     = False
default flag_ino_first_intimate = False
default ino_relationship_status = "neighbor"

## ── INVENTORY ────────────────────────────────────────────────
default inventory = {
    "herbs":       3,
    "flowers":     0,
    "kunai_parts": 0,
    "sweets":      0,
    "medicine":    0,
}

## ── SHOP STOCK (by level) ────────────────────────────────────
## updated when shop upgrades
default shop_stock = {
    "herbs":       {"price": 50,  "stock": 10},
    "flowers":     {"price": 80,  "stock": 5},
    "kunai_parts": {"price": 120, "stock": 3},
    "sweets":      {"price": 90,  "stock": 6},
    "medicine":    {"price": 180, "stock": 2},
}
