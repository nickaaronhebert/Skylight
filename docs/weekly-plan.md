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

**What Claude does:**
- Checks what meals are already on the calendar
- Proposes a full week of lunches and dinners based on household preferences
- Respects any constraints flagged in Section 1

**Rules:**
- Identify 1–2 protein anchors and build meals around them
- Intentionally reuse ingredients across meals
- Weekday dinners = assemble, not cook
- One or two fresh-cook nights (salmon, sheet pan) are fine
- Kid-friendly lunches only
- Saturday is flexible/leftover night unless specified

**Approval checkpoint:** Review and approve the full menu before posting.

**What Claude posts:** All meals to the Skylight calendar.

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

## Section 4 — Kids' Chores

**Standing infrastructure (recurring, set up once):**
- Bedroom cleaning — daily for Eleanor, Delaney, and Marley
- Rotating daily chores — 2 per child per day, weekly cycle
- Full schedule defined in `docs/recurring-tasks.md`

**What Claude does each week:**
- Reads `docs/recurring-tasks.md` to know what should exist
- Verifies recurring chores are showing up correctly for the week
- Creates any missing chores using the RRULE definitions in that document
- Adds any special one-off tasks for the week

**Approval checkpoint:** Confirm kids' chore state before any changes.

**What Claude posts:** Missing recurring chores (if any) + any special one-off tasks.

---

## Section 5 — Nanny Tasks (Elizabeth)

**Standing infrastructure (recurring, set up once):**
- 2 morning tasks + 2 afternoon tasks per weekday, weekly cycle
- Full schedule defined in `docs/recurring-tasks.md`

**What Claude does each week:**
- Reads `docs/recurring-tasks.md` to know what should exist
- Verifies Elizabeth's tasks are in place Mon–Fri for the target week
- Creates any missing tasks using the RRULE definitions in that document
- Adds any special tasks specific to the week (e.g. deep clean before guests, school forms)

**Approval checkpoint:** Confirm Elizabeth's task state before any changes.

**What Claude posts:** Missing recurring tasks (if any) + any special one-off tasks.

---

## Section 6 — Grocery List

**What Claude does:**
- Consolidates all ingredients from the approved meal plan
- Groups by category (proteins, produce, dairy, pantry, spices)
- Flags quantities based on 10-serving default
- Notes items likely already stocked (spices, pantry staples)

**No API posting — this is an output for shopping.**

---

## Complete Weekly Checklist

- [ ] Weekly events reviewed
- [ ] Menu approved and posted
- [ ] Evening Assistant prep tasks approved and posted
- [ ] Kids' recurring chores verified
- [ ] Elizabeth's recurring tasks verified
- [ ] Grocery list generated

**Estimated session time: 15–20 minutes**
