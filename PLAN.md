# VILLAGE CHRONICLES — Development Plan

## Game Overview
**Genre:** Adult Visual Novel + Dating Simulation
**Engine:** Ren'Py
**Setting:** Konoha village, slice-of-life civilian POV
**Player:** Male civilian shopkeeper, new to Konoha
**Art Style:** Anime (unholyDesireMixSinister V8.0 via zlkpro.tech)
**Image Pipeline:** generate → R2 bucket → imgproxy WebP
**Repo:** https://github.com/AyuTriphasari/VILLAGE-CHRONICLES

---

## PHASE 1 — Foundation ✅ COMPLETE
> Core project structure and visual theme

- [x] Clone base Ren'Py scaffold
- [x] Generate custom GUI assets (textbox, namebox, buttons, scrollbars, overlays)
- [x] Update gui.rpy theme colors (dark forest + sakura + gold palette)
- [x] Generate AI main menu background (Konoha at dusk, 1280x720)
- [x] Generate game_menu background (interior scene)
- [x] Create window_icon.png (sakura blossom icon)
- [x] Set up images/ folder structure (bg, sprites per character, cg)
- [x] Set up audio/ folder structure (bgm, sfx)

---

## PHASE 2 — Core Systems ✅ COMPLETE
> Game mechanics and variables

- [x] **Day/Time System** → `game/systems/day_time.rpy`
  - Variables: day_count, time_of_day (morning/afternoon/evening/night)
  - Day advance mechanic with daily reset
  - Time display in HUD

- [x] **Stats System** → `game/systems/variables.rpy`
  - Player stats: charm, wit, generosity
  - Per-character: affinity (0-100), trust (0-100), mood (daily)
  - Ryo (money) system + inventory

- [x] **HUD Screen** → `game/screens/hud.rpy`
  - Top bar: day, time, ryo
  - Side panel: character affinity bars (shown after meeting)
  - Theme-matched dark forest + gold styling

- [x] **Shop System** → `game/screens/shop.rpy`
  - Open/close shop mechanic with daily income
  - 3 upgrade tiers (₩80 / ₩150 / ₩260 per day)
  - Inventory items unlocked by shop level
  - Buy items function

- [x] **Main Script** → `game/script.rpy`
  - Day 1 intro + first Ino meeting
  - Daily loop (day_loop label)
  - Location visit labels (flower shop, explore)
  - Save/Load via Ren'Py default system

---

## PHASE 3 — World & Navigation
> Village map and location system

- [x] **Village Map Screen**
  - Clickable locations:
    - [x] Your Shop (home base)
    - [x] Market Street
    - [x] Ino's Flower Shop
    - [x] Training Ground
    - [x] Village Park
    - [x] Ramen Bar (Ichiraku)
  - [x] Time-of-day availability per location
  - [x] Character presence indicators

- [x] **Location Backgrounds** (AI generated, 1280x720)
  - [x] bg_shop_interior.png
  - [x] bg_market_day.png / bg_market_night.png
  - [x] bg_flower_shop.png
  - [x] bg_training_ground.png
  - [x] bg_park_day.png / bg_park_evening.png
  - [x] bg_ramen_bar.png

---

## PHASE 4 — Character: INO YAMANAKA
> First full playable character route

### 4a. Sprite Generation (all transparent WebP)
- [x] ino_normal.webp — default standing pose
- [x] ino_happy.webp — smiling wide
- [x] ino_shy.webp — blushing, looking away
- [x] ino_surprised.webp — shocked expression
- [x] ino_annoyed.webp — arms crossed, pouting
- [x] ino_blush.webp — deep blush, flustered
- [x] ino_seductive.webp — confident smile, flirty (affinity 50+)
- [x] ino_intimate1.webp — Act 2 scene sprite
- [x] ino_intimate2.webp — Act 3 scene sprite

**Prompt base:** `ino yamanaka, shiny skin, big breasts, mature, adult woman, blonde hair, very long high ponytail, blue eyes, slim curvy anime woman, standing front view, cowboy shot, full body centered, same outfit: sleeveless fitted purple crop top, matching purple skirt, white waist bandage belt, black arm warmers, black open toe shinobi sandals, {expression}, clean transparent background, consistent character design, consistent outfit, visual novel sprite, anime style, masterpiece, best quality, amazing quality, very aesthetic, absurdres`

**Pipeline:** generate at 720x1280 transparent WebP, then resize with Image Resizer skill to height 720 while preserving alpha. Heroine images must include `shiny skin`, `big breasts`, and `mature`. Use character LoRAs when available. Ino LoRA: `models/loras/ino_yamanaka_ixl_rc1-000006.safetensors` strength `0.75`, trigger `ino yamanaka`.

### 4b. Act 1 — Meet & Build Trust (Day 1–7, SFW)
- [x] Day 1: Ino visits shop, first meeting
- [x] Day 2: She returns, teases about shop decor
- [x] Day 3: Gift mechanic introduced (flowers)
- [x] Day 4: Afternoon free time event at flower shop
- [x] Day 5: Affinity check event (need affinity 15+)
- [x] Day 6: Evening walk encounter in park
- [x] Day 7: End of week — affinity summary, unlock Act 2 hint

### 4c. Act 2 — Deeper Bond (Day 8–14, first intimate scene at affinity 50)
- [ ] Day 8-10: Daily interactions, trust building
- [ ] Day 11: Personal story event (Ino's insecurity about being compared to Sakura)
- [ ] Day 12: Comfort scene, trust boost
- [ ] Day 13: First intimate scene (affinity 50 required)
- [ ] Day 14: Morning after, relationship status changes

### 4d. Act 3 — Route Endings (Day 15+)
- [ ] Ending A: Lovers (affinity 80+, trust 70+)
- [ ] Ending B: Friends with benefits (affinity 60+, trust 40+)
- [ ] Ending C: Heartbreak (low trust path)

---

## PHASE 5 — Character: SAKURA HARUNO
> Second character route

### 5a. Sprites
- [ ] sakura_normal, happy, shy, annoyed, blush, seductive, intimate1, intimate2

**Prompt base:** `sakura haruno, pink hair, short hair, red outfit, standing, front view, cowboy shot, {expression}, simple background, white background, masterpiece, best quality`

### 5b. Story
- [ ] Act 1: Medical supply customer, tsundere dynamic (Day 1–7)
- [ ] Act 2: Injury event, she treats you (Day 8–14)
- [ ] Act 3: Three endings (Day 15+)

---

## PHASE 6 — Character: HINATA HYUGA
> Third character route (slow burn)

### 6a. Sprites
- [ ] hinata_normal, happy, shy, surprised, blush, seductive, intimate1, intimate2

**Prompt base:** `hinata hyuga, dark blue hair, lavender eyes, white jacket, standing, front view, cowboy shot, {expression}, simple background`

### 6b. Story
- [ ] Act 1: Shy regular customer, barely speaks (Day 1–7)
- [ ] Act 2: Opens up slowly, stutter mechanic in dialogue (Day 8–21, slow burn)
- [ ] Act 3: Three endings

---

## PHASE 7 — Additional Characters (Post-core)
- [ ] **Temari** — limited-time route (visiting Suna ambassador), urgency mechanic
- [ ] **TenTen** — weapon repair client, tomboy route

---

## PHASE 8 — Special Events & Polish
- [ ] Rival system (e.g. Sasuke competing for attention)
- [ ] Group events (affinity with 2+ characters)
- [ ] Special CG scenes (full-screen illustration moments)
- [ ] BGM integration (looping ambient tracks per location/time)
- [ ] SFX (UI clicks, scene transitions)
- [ ] Achievement/gallery system (unlocked CGs)

---

## PHASE 9 — Build & Distribution
- [ ] Test full playthrough (Day 1–15 minimum)
- [ ] Package for Windows/Linux/Mac via Ren'Py builder
- [ ] itch.io release page setup

---

## Current Status

| Phase | Status |
|-------|--------|
| Phase 1 — Foundation | ✅ Complete |
| Phase 2 — Core Systems | ✅ Complete |
| Phase 3 — World & Map | ✅ Complete |
| Phase 4 — Ino Route | 🟡 Act 1 Complete |
| Phase 5 — Sakura Route | ⬜ Not Started |
| Phase 6 — Hinata Route | ⬜ Not Started |
| Phase 7 — Extra Characters | ⬜ Not Started |
| Phase 8 — Polish | ⬜ Not Started |
| Phase 9 — Distribution | ⬜ Not Started |

---

## Notes
- All sprites generated via `https://app.zlkpro.tech` using unholyDesireMixSinister V8.0
- Images served via `https://imgproxy.zlkpro.tech/insecure/q:90/plain/<r2_url>@webp`
- Always push to git after each change (auto, no confirmation needed)
- GitHub: AyuTriphasari/VILLAGE-CHRONICLES
