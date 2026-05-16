# Claude Context — Skylight Meal Planning

This repo is used to interact with the Skylight family calendar API for automated meal planning. Read this file before doing anything.

---

## Credentials

You will need a bearer token from the user to make API requests. Ask for it if not provided. Never commit tokens to the repo.

**Frame ID:** `5289925`
**API Base URL:** `https://app.ourskylight.com`
**Required header:** `skylight-api-version: 2026-04-15`

---

## Known IDs

### Chore Categories
| ID | Label |
|---|---|
| `20237876` | Evening Assistant |
| `20235057` | Eleanor |
| `20235070` | Delaney |
| `20235082` | Marley |
| `20235149` | Elizabeth |
| `20235749` | Family |

### Meal Categories
| ID | Label |
|---|---|
| `8837086` | Breakfast |
| `8837087` | Lunch |
| `8837088` | Dinner |
| `8837089` | Snack |

---

## API Patterns

### Important: Request Body Format
The Skylight API documentation suggests JSON:API format but the actual endpoints behave differently:

- **Chores POST/PATCH** — use a flat body, not JSON:API wrapper
- **Meals POST** — use a flat body

### Chores

**Create a one-off chore**
```
POST /api/frames/{frameId}/chores
Authorization: Bearer <token>
Content-Type: application/json

{
  "summary": "Task name",
  "status": "pending",
  "start": "2026-05-11",
  "category_id": "20237876",
  "recurring": false
}
```

**Create a recurring chore**
Use `create_multiple` — the standard POST endpoint ignores recurrence fields.
`recurrence_set` must be an array with the `RRULE:` prefix.
```
POST /api/frames/{frameId}/chores/create_multiple
Authorization: Bearer <token>
Content-Type: application/json
skylight-api-version: 2026-04-15

{
  "summary": "Task name",
  "description": "",
  "start": "2026-05-11",
  "start_time": null,
  "recurring_until": null,
  "up_for_grabs": false,
  "routine": false,
  "recurrence_set": ["RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=MO"],
  "category_ids": ["20237876"]
}
```

**Update a chore**
```
PATCH /api/frames/{frameId}/chores/{choreId}
```

**Get chores**
```
GET /api/frames/{frameId}/chores?after=2026-05-11&before=2026-05-11&include_late=true
```

### Meals

**Get meal sittings**
```
GET /api/frames/{frameId}/meals/sittings?date_min=2026-05-01&date_max=2026-06-01&include=meal_category,meal_recipe
```

**Create a one-off meal**
```
POST /api/frames/{frameId}/meals/sittings?date_min=...&date_max=...&include=meal_category,meal_recipe
Authorization: Bearer <token>
Content-Type: application/json
skylight-api-version: 2026-04-15

{
  "meal_recipe_id": null,
  "meal_category_id": "8837088",
  "add_to_grocery_list": false,
  "note": null,
  "rrule": null,
  "description": null,
  "date": "2026-05-12",
  "summary": "Meal name"
}
```

**Create a recurring meal**
Same as above but with an rrule:
```json
{
  "rrule": "FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=TU",
  "summary": "Toast Tuesday"
}
```

**Delete a meal instance**
```
DELETE /api/frames/{frameId}/meals/sittings/{sittingId}/instances/{date}?date_min=...&date_max=...&include=meal_category,meal_recipe
```

---

## Weekly Planning

When asked to "plan the week" or similar, follow the full guide in `docs/weekly-plan.md`. It covers all six sections in order: events, meals, evening assistant prep, kids' chores, nanny tasks, and grocery list. Do not skip sections or jump ahead without approval at each checkpoint.

For all recurring chore definitions, schedules, RRULE formats, and category IDs — read `docs/recurring-tasks.md`. Do not rely on memory for these. That document is the source of truth.

For meal planning — read `docs/recipe-manager.md` before proposing any meals. This is the source of truth for all recipes, meal types, and last usage dates. Rules:
- Do not schedule a meal whose `lastUsageDate` is within the past 21 days
- Lunch slots on the calendar are for kids only — must be kid-friendly and prep < 10 min
- Update `lastUsageDate` in recipe-manager.md after posting meals to the calendar
- After the weekly menu is posted, propose 10 new meals for Madison to consider adding

---

## Meal Planning Workflow

Run these steps in order. Do not skip ahead.

1. **Check the calendar** — GET meals/sittings for the target week to see what's already planned
2. **Generate the menu** — propose lunches and dinners for the week based on household preferences (see below)
3. **Get approval** — present the menu and wait for confirmation before posting anything
4. **Post meals** — POST each meal to the calendar
5. **Generate prep tasks** — identify what the Evening Assistant needs to do and when, grouped efficiently
6. **Post prep tasks** — POST each prep task as a chore assigned to Evening Assistant (`20237876`)
7. **Generate grocery list** — consolidate all ingredients grouped by category
8. **Generate daily assembly guide** — quick pull-and-assemble instructions per day

---

## Household Preferences

See full BRD: `docs/meal-planning-brd.md`
See operating model: `docs/meal-planning-operations.md`

**Quick reference:**
- Health-conscious, lower-carb leaning
- Chicken-forward — batch shredded chicken is the primary protein anchor most weeks
- Bowl-friendly meals, simple prep
- Cauliflower rice and other rice alternatives preferred over white rice
- Kid-friendly lunches (protein boxes, wraps, roll-ups, yogurt + fruit)
- 10 servings default
- Weekday dinners = assemble, not cook
- One or two fresh-cook nights per week (salmon, sheet pan) are fine

---

## Evening Assistant

- Works Monday–Friday, 7–10pm
- Handles meal prep alongside other household duties — keep tasks realistic
- Prep tasks should be grouped efficiently based on the menu (not always Monday)
- Always estimate active time per prep night
- Batch tasks that can share active time (e.g. chop veg while protein cooks)
- Separate prep tasks from assembly tasks
- Use Instant Pot over slow cooker — prep happens in the evening, not during the day

---

## Meal Planning Tips

- Identify 1–2 protein anchors per week and build meals around them
- Intentionally reuse ingredients across meals (shared veg, sauces, bases)
- Sequence prep so ingredients are ready the evening before they're needed
- Lunches are portioned nightly by the assistant for next-day grab-and-go
- Saturday is typically a flexible/leftover night — don't plan it unless asked
- When posting meals in parallel, use background curl processes with `&` and `wait`
