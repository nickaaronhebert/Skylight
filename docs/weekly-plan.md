# Weekly Planning Guide

This document defines the complete weekly planning session. Run this every week, in order. Each section has an approval checkpoint before anything is posted.

---

## Before You Start

Tell Claude:
- The week you are planning (e.g. "plan the week of May 18")
- Your bearer token
- Any constraints (travel, events, dietary preferences this week)

Claude will check the calendar before proposing anything.

---

## Section 1 — Weekly Events

**What Claude does:**
- Checks the family calendar for the target week
- Flags anything that affects other sections (e.g. a sports practice night = simple dinner, a school holiday = nanny not needed)

**Approval checkpoint:** Confirm the week's events are correct before proceeding.

---

## Section 2 — Meals

This section runs in two phases: new meal proposals first, then menu planning from the full repository.

### Phase 1 — New Meal Proposals

**What Claude does:**
- Proposes 10 new meals not currently in `docs/recipe-manager.md`
- Presents each with a name and one-line description
- Madison selects any number to approve (or none)

**What Claude does with approved meals:**
- Fully prepares each approved meal in recipe-manager.md format:
  - Name, description, mealType, appropriateMealTimes, kidFriendly, prepTime, lastUsageDate (null), URL (if available)
  - Full ingredients list scaled to 10 servings
  - Step-by-step instructions
- Writes all approved meals into `docs/recipe-manager.md` under the correct category

**Approval checkpoint:** Madison confirms which new meals to add before Claude writes them to the file.

### Phase 2 — Weekly Menu Planning

**What Claude does:**
- Reads `docs/recipe-manager.md` (now including any newly added meals)
- Checks what meals are already on the Skylight calendar for the target week
- Proposes a full week of lunches (kids) and dinners based on the rules below

**Rules:**
- Do not schedule any meal whose `lastUsageDate` is within the past 21 days
- Identify 1–2 protein anchors and build meals around them
- Intentionally reuse ingredients across meals to reduce waste
- Weekday dinners = assemble, not cook
- One or two fresh-cook nights (salmon, sheet pan) are fine
- Lunch slots = kids only; must be kid-friendly and prep < 10 min
- Adults eat dinner leftovers for lunch — do not plan adult lunches
- Saturday is flexible/leftover night unless specified

**Approval checkpoint:** Review and approve the full menu before posting.

**What Claude posts:** All meals to the Skylight calendar. Updates `lastUsageDate` for each posted meal in `docs/recipe-manager.md`.

---

## Section 3 — Evening Assistant Prep Tasks

**What Claude does:**
- Derives all prep tasks directly from the approved menu
- Groups tasks efficiently based on what can be batched together
- Sequences tasks so ingredients are ready before they are needed
- Assigns each task to the correct evening with an active time estimate

**Rules:**
- Separate prep tasks from assembly tasks
- Use Instant Pot over slow cooker
- Incremental nightly tasks should be 10–15 min max
- The primary batch night is determined by the menu, not fixed to a day

**Approval checkpoint:** Review prep schedule before posting.

**What Claude posts:** All prep tasks as chores assigned to Evening Assistant.

---

## Section 4 — Household Chores Review & Planning

This section replaces the old separate kids and nanny sections. All recurring tasks are already set up in Skylight — this section is for reviewing last week and confirming the upcoming week.

### Part A — Last Week's Report

**What Claude does:**
- Fetches chore completion data for the previous week from Skylight
- Reports completion rate per person with done/not-done breakdown
- Presents as a quick summary (e.g. "Eleanor: 8/10 ✓, Elizabeth: 4/5 ✓")

### Part B — Upcoming Week Chore List

**What Claude does:**
- Fetches the chore list from Skylight for each day of the target week
- Presents the full schedule sorted by person, then by day
- Flags anything that looks missing or unexpected based on `docs/recurring-tasks.md`

**Format:**
```
Monday May 19
  Eleanor: Clean bedroom, Unload dishwasher, Wipe bathroom counters
  Delaney: Clean bedroom, Wipe bathroom sink, Tidy playroom
  Marley: Clean bedroom, Pick up toys, Put shoes away
  Elizabeth: Fridges cleaned out, Put away grocery order, Marley & Adeline's Rooms

Tuesday May 20
  ...
```

**Approval checkpoint:** User confirms the schedule looks correct. User specifies any additions (one-off tasks, special requests) or removals.

**What Claude posts:** Any one-off tasks the user requests. Removes anything the user flags.

---

## Section 5 — Grocery List

**What Claude does:**
- Consolidates all ingredients from the approved meal plan
- Groups by category (proteins, produce, dairy, pantry, spices)
- Flags quantities based on 10-serving default
- Notes items likely already stocked (spices, pantry staples)

**No API posting — this is an output for shopping.**

---

## Complete Weekly Checklist

- [ ] Weekly events reviewed
- [ ] New meal proposals reviewed and repo updated
- [ ] Menu approved and posted, lastUsageDates updated
- [ ] Evening Assistant prep tasks approved and posted
- [ ] Last week's chore completion reviewed
- [ ] Upcoming week chore schedule confirmed
- [ ] Grocery list generated

**Estimated session time: 15–20 minutes**
