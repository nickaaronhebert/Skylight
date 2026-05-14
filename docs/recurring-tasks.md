# Recurring Tasks & Chore Schedule

This document is the source of truth for all standing recurring tasks in the household. Claude should read this document to verify, create, or repair recurring chores. Do not rely on memory or prior context — always reference this file.

When verifying a week, check that every task defined here has a corresponding chore in Skylight for the target dates. If any are missing, create them using the `create_multiple` endpoint with the `recurrence_set` format defined below.

---

## API Format for Recurring Chores

```
POST /api/frames/5289925/chores/create_multiple
{
  "summary": "Task name",
  "description": "",
  "start": "YYYY-MM-DD",         ← first occurrence date
  "start_time": null,
  "recurring_until": null,
  "up_for_grabs": false,
  "routine": false,
  "recurrence_set": ["RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=MO"],
  "category_ids": ["CATEGORY_ID"]
}
```

**BYDAY values:** MO, TU, WE, TH, FR, SA, SU
**For daily recurrence:** `["RRULE:FREQ=DAILY;INTERVAL=1"]`

---

## Eleanor (age 8) — Category ID: `20235057`

### Bedroom Cleaning
| Task | Recurrence | RRULE |
|---|---|---|
| Clean bedroom | Daily | `RRULE:FREQ=DAILY;INTERVAL=1` |

### Rotating Morning Chores (2 per day)
| Day | Chore 1 | Chore 2 | RRULE |
|---|---|---|---|
| Monday | Unload the dishwasher | Wipe bathroom counters | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=MO` |
| Tuesday | Take out recycling | Sweep the entryway | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=TU` |
| Wednesday | Fold her laundry | Vacuum her room | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=WE` |
| Thursday | Wipe bathroom mirror | Tidy the mudroom | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=TH` |
| Friday | Take out trash | Sweep the kitchen floor | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=FR` |
| Saturday | Water the plants | Dust the shelves | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=SA` |
| Sunday | Tidy the living room | Wipe bathroom counters | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=SU` |

---

## Delaney (age 6) — Category ID: `20235070`

### Bedroom Cleaning
| Task | Recurrence | RRULE |
|---|---|---|
| Clean bedroom | Daily | `RRULE:FREQ=DAILY;INTERVAL=1` |

### Rotating Morning Chores (2 per day)
| Day | Chore 1 | Chore 2 | RRULE |
|---|---|---|---|
| Monday | Wipe the bathroom sink | Tidy the playroom | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=MO` |
| Tuesday | Sort the laundry | Water the plants | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=TU` |
| Wednesday | Tidy the playroom | Pick up shoes and backpacks | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=WE` |
| Thursday | Wipe the bathroom sink | Sort the laundry | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=TH` |
| Friday | Tidy the playroom | Dust a surface | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=FR` |
| Saturday | Water the plants | Tidy the toy bins | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=SA` |
| Sunday | Tidy her bookshelf | Pick up shoes | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=SU` |

---

## Marley (age 4) — Category ID: `20235082`

### Bedroom Cleaning
| Task | Recurrence | RRULE |
|---|---|---|
| Clean bedroom | Daily | `RRULE:FREQ=DAILY;INTERVAL=1` |

### Rotating Morning Chores (2 per day)
| Day | Chore 1 | Chore 2 | RRULE |
|---|---|---|---|
| Monday | Pick up toys | Put shoes away | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=MO` |
| Tuesday | Water one plant | Help sort socks | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=TU` |
| Wednesday | Pick up toys | Put books away | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=WE` |
| Thursday | Put shoes away | Help sort socks | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=TH` |
| Friday | Pick up toys | Wipe her table with a cloth | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=FR` |
| Saturday | Tidy toy bins | Pick up toys | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=SA` |
| Sunday | Put books away | Pick up toys | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=SU` |

---

## Elizabeth — Nanny — Category ID: `20235149`

Standing recurring tasks Mon–Fri. In addition to these, there are 3 daily tasks that recur every weekday: **Kids Ready**, **Enforce Morning Routine**, **Toddler Duty + Daily Task**.

| Day | Task 1 | Task 2 | RRULE |
|---|---|---|---|
| Monday | Fridges cleaned out | Put away grocery order | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=MO` |
| Tuesday | Monthly Item | Bonus Room | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=TU` |
| Wednesday | Piano Room | Quarterly Project | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=WE` |
| Thursday | Laundry Wash/Dry Day | 1 Monthly Item in Between Loads | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=TH` |
| Friday | Sort Laundry: Bigs will put away their own | Living Room: sweep/mop, wipe down couches, toy bucket clear | `RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=SU;BYDAY=FR` |

---

## Evening Assistant — Category ID: `20237876`

The Evening Assistant has **no standing recurring tasks.** All tasks are generated fresh each week from the meal plan and posted during the weekly planning session. See `docs/weekly-plan.md` Section 3.

---

## Verification Checklist

During weekly planning (Section 4 and 5 of `docs/weekly-plan.md`), Claude should verify:

**Kids (Eleanor, Delaney, Marley):**
- [ ] Bedroom cleaning appearing daily for the target week
- [ ] 2 rotating chores per day appearing for the target week
- [ ] No duplicate chores

**Elizabeth:**
- [ ] 5 tasks per weekday appearing Mon–Fri for the target week (2 day-specific + 3 daily standing)
- [ ] No duplicate tasks

If any tasks are missing, create them using the `create_multiple` endpoint with the correct `recurrence_set` and `category_ids` from this document.
