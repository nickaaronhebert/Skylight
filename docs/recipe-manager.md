# Recipe Manager

This is the source of truth for all household recipes. Claude reads this file during weekly meal planning to select meals, check last usage dates, and enforce the 21-day rotation rule.

## Rules
- **21-day rotation:** Do not schedule a meal if its `lastUsageDate` is within the past 21 days.
- **Lunches = kids meals:** Lunch recipes must be kid-friendly and prep time must be under 10 minutes. Adults eat dinner leftovers for lunch.
- **Scaling:** All recipes are written for **10 servings**.
- **Last usage:** Update `lastUsageDate` each time a meal is posted to the calendar.

---

## Recipe Format

```
### [Meal Name]
**Description:** ...
**mealType:** Bowl | Sheet Pan | Pasta | Soup | Sandwich | Breakfast | Salad | Casserole
**appropriateMealTimes:** breakfast | lunch | dinner (can be multiple)
**kidFriendly:** yes | no
**prepTime:** X min (active prep only, not cook time)
**lastUsageDate:** null | YYYY-MM-DD
**url:** null | https://...

**Ingredients (10 servings)**
- ...

**Instructions**
1. ...
```

---

## Recipes

---

### Philly Cheesesteak Bowls
**Description:** Bone broth brown rice topped with sautéed flank steak strips, bell peppers, and melted provolone.
**mealType:** Bowl
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 20 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 3 cups brown rice
- 6 cups bone broth
- 2.5 lbs flank steak, cut into thin strips
- 4 large bell peppers (mixed colors), sliced
- 2 tbsp olive oil
- 1 tsp garlic powder
- 1 tsp onion powder
- Salt and pepper to taste
- 10 slices provolone cheese

**Instructions**
1. Cook brown rice in bone broth: bring to boil, reduce heat, cover and simmer 40–45 min.
2. Season flank steak strips with salt, pepper, garlic powder, and onion powder.
3. Heat olive oil in a large skillet over high heat. Sear steak in batches 2–3 min per side. Set aside.
4. In the same skillet, sauté bell peppers until slightly softened, about 5 min.
5. Return steak to pan with peppers. Toss to combine.
6. Serve steak and peppers over rice. Top each bowl with a slice of provolone (it will melt from the heat of the food).

---

### Steak Bowls
**Description:** Wild rice topped with flank steak strips, roasted butternut squash, and tahini drizzle.
**mealType:** Bowl
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 20 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 3 cups wild rice
- 6 cups water
- 2.5 lbs flank steak, cut into strips
- 2 medium butternut squash, peeled and cubed
- 3 tbsp olive oil, divided
- Salt, pepper, garlic powder to taste
- ½ cup tahini
- 3 tbsp lemon juice
- 2 tbsp water (to thin tahini)

**Instructions**
1. Cook wild rice in water: bring to boil, reduce to low simmer, cover and cook 45–55 min until tender. Do not rush.
2. Toss butternut squash cubes in 2 tbsp olive oil, salt, and pepper. Roast at 400°F for 25–30 min until caramelized.
3. Season steak strips with salt, pepper, and garlic powder. Heat remaining olive oil in skillet over high heat. Sear steak 2–3 min per side. Set aside.
4. Whisk tahini, lemon juice, and water together until smooth. Season with salt.
5. Assemble bowls: rice, steak, butternut squash, drizzle tahini.

---

### Greek Bowls
**Description:** Quinoa topped with Greek-seasoned ground turkey, feta, cucumber, tzatziki, and pickled red onions.
**mealType:** Bowl
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 15 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 3 cups dry quinoa
- 6 cups water or broth
- 2.5 lbs ground turkey
- 3 tbsp Greek seasoning (oregano, garlic, lemon pepper blend)
- 1.5 cups crumbled feta
- 2 large cucumbers, diced
- 1.5 cups tzatziki
- 1 cup pickled red onions (see note)
- Salt and pepper to taste

**Instructions**
1. Cook quinoa in water or broth: bring to boil, reduce heat, cover and simmer 15 min. Fluff with fork.
2. Brown ground turkey in a large skillet over medium-high heat. Season generously with Greek seasoning, salt, and pepper. Cook until no pink remains.
3. Assemble bowls: quinoa base, turkey, cucumber, feta, a spoonful of tzatziki, pickled red onions.
4. **Pickled red onions (quick):** Thinly slice 2 red onions. Combine ½ cup red wine vinegar, ½ cup water, 1 tsp sugar, 1 tsp salt in a jar. Add onions. Ready in 30 min, best after a few hours.

---

### Salmon Bowls
**Description:** Coconut rice with baked salmon, roasted broccoli, mushrooms, and sweet potato, finished with coconut aminos.
**mealType:** Bowl
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 20 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 3 cups jasmine rice
- 2 cans (13.5 oz each) coconut milk
- Water to bring total liquid to 6 cups
- 2 tbsp coconut sugar
- Pinch of salt
- 3–3.5 lbs salmon fillets
- 2 heads broccoli, cut into florets
- 1 lb mushrooms, sliced
- 2 medium sweet potatoes, cubed
- 3 tbsp olive oil
- ¼ cup coconut aminos
- Salt and pepper to taste

**Instructions**
1. Combine coconut milk and water to make 6 cups total liquid. Cook rice with coconut sugar and pinch of salt: bring to boil, cover, simmer 15–18 min.
2. Toss broccoli, mushrooms, and sweet potato in olive oil, salt, and pepper. Roast at 400°F for 20–25 min.
3. Season salmon with salt and pepper. Bake alongside vegetables at 400°F for 12–15 min until flaky.
4. Assemble bowls: coconut rice, salmon (broken into chunks), roasted vegetables. Drizzle with coconut aminos.

---

### Burger Buddha Bowls
**Description:** Roasted sweet potatoes and ground beef cooked in tomato paste, topped with pickled onions, pickles, tomatoes, and cheese — deconstructed burger in a bowl.
**mealType:** Bowl
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 15 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 5 medium sweet potatoes, peeled and cubed
- 3 tbsp olive oil
- 2.5 lbs ground beef (80/20)
- 2 cans (6 oz each) tomato paste
- 1 tsp garlic powder
- 1 tsp onion powder
- Salt and pepper to taste
- 1 cup pickled red onions
- 1 cup dill pickle slices
- 3 large tomatoes, diced
- 2 cups shredded cheddar cheese

**Instructions**
1. Toss sweet potato cubes in olive oil, salt, and pepper. Roast at 425°F for 25–30 min, flipping halfway.
2. Brown ground beef in a large skillet. Drain excess fat. Add tomato paste, garlic powder, onion powder, salt, and pepper. Stir and cook 3–4 min until combined and fragrant.
3. Assemble bowls: sweet potatoes, beef mixture, pickled onions, pickles, diced tomatoes, shredded cheddar.

---

### Street Corn Bowls
**Description:** Bone broth rice topped with skillet-charred corn mixed in a creamy tajin-cotija sauce, ground beef or chicken nuggets, avocado, and red onion.
**mealType:** Bowl
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 20 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 3 cups brown rice
- 6 cups bone broth
- 3 cans (15 oz each) corn, drained OR 6 ears corn, kernels cut off
- 1 cup cottage cheese
- ½ cup mayonnaise
- 2 tbsp tajin
- 1 cup cotija cheese, crumbled
- Juice of 3 limes
- Salt to taste
- 2 lbs ground beef OR 2 lbs chicken nuggets (cooked per package)
- 3–4 avocados, sliced
- 1 large red onion, diced

**Instructions**
1. Cook brown rice in bone broth: bring to boil, reduce heat, cover and simmer 40–45 min.
2. Heat a dry skillet over high heat. Add corn and cook without stirring for 2–3 min until lightly charred. Stir and char another 1–2 min.
3. Remove corn from heat. Stir in cottage cheese, mayo, tajin, cotija, and lime juice. Season with salt.
4. If using ground beef, brown in skillet with salt and pepper.
5. Assemble bowls: rice, corn mixture, beef or nuggets, avocado slices, red onion.

---

### Sheet Pan (Shrimp & Chicken Sausage)
**Description:** Shrimp and chicken sausage roasted on sheet pans with a colorful mix of vegetables. Easy weeknight assembly.
**mealType:** Sheet Pan
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 15 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 2 lbs large shrimp, peeled and deveined
- 2 lbs chicken sausage, sliced into rounds
- 2 zucchini, sliced into half-moons
- 2 bell peppers, cut into chunks
- 2 cups broccoli florets
- 1 pint cherry tomatoes
- 4 tbsp olive oil
- 2 tsp garlic powder
- 2 tsp Italian seasoning
- Salt and pepper to taste

**Instructions**
1. Preheat oven to 425°F. Line 2–3 sheet pans with parchment.
2. Toss sausage and vegetables in olive oil, garlic powder, Italian seasoning, salt, and pepper. Spread in a single layer across pans.
3. Roast 15 min. Remove from oven, add shrimp to pans, toss lightly.
4. Return to oven and roast 8–10 min more until shrimp are pink and cooked through.
5. Serve directly from pan.

---

### Salmon Sheet Pan
**Description:** Lemon-topped salmon with baby potatoes and asparagus roasted together, finished with feta and Greek goddess dressing.
**mealType:** Sheet Pan
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 10 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 3.5 lbs salmon fillet (1 large or multiple pieces)
- 3 lemons, sliced into rounds
- 2.5 lbs baby potatoes, halved
- 2 bunches asparagus, trimmed
- 4 tbsp olive oil
- Salt, pepper, garlic powder to taste
- 1 cup crumbled feta
- 1 bottle Greek goddess dressing (for serving)

**Instructions**
1. Preheat oven to 400°F. Line 2 sheet pans with parchment.
2. Toss baby potatoes in 2 tbsp olive oil, salt, pepper. Spread on one pan. Roast 15 min.
3. Add asparagus to the potato pan and add salmon to the second pan. Drizzle salmon and asparagus with remaining olive oil, season. Lay lemon slices on top of salmon.
4. Roast everything together 12–15 min until salmon is flaky and asparagus is tender.
5. Plate and top salmon with crumbled feta. Serve with Greek goddess dressing on the side.

---

### Messy Lasagna
**Description:** Deconstructed lasagna with Banza pasta, ground beef, Rao sauce, and cottage cheese — zucchini mixed in or broccoli on the side.
**mealType:** Pasta
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 15 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 2 boxes (8 oz each) Banza pasta (penne or rigatoni)
- 2 lbs ground beef
- 2 jars (24 oz each) Rao tomato sauce
- 24 oz (3 cups) cottage cheese
- 2 medium zucchini, diced (optional mix-in)
- 2 heads broccoli, cut into florets (optional side, roasted or steamed)
- 2 cups shredded mozzarella
- Salt, pepper, garlic powder, Italian seasoning to taste

**Instructions**
1. Cook Banza pasta per package directions. Drain and set aside.
2. Brown ground beef in a large pot over medium-high heat. Season with salt, pepper, garlic powder, and Italian seasoning. Drain excess fat.
3. Add Rao sauce to beef. Stir and simmer 5 min.
4. If using zucchini, add to the sauce and cook 3–4 min until softened.
5. Fold in cooked pasta and cottage cheese. Stir to combine.
6. Serve as is, or transfer to baking dishes, top with mozzarella, and broil 3–4 min until bubbly.
7. If using broccoli, roast at 425°F with olive oil, salt, and pepper for 20 min and serve on the side.

---

### Easy Chicken Marinara
**Description:** Baked chicken nuggets smothered in Rao marinara and melted mozzarella. Vegetable on the side.
**mealType:** Pasta
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 5 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 3 lbs frozen chicken nuggets (~60 nuggets)
- 2 jars (24 oz each) Rao marinara sauce
- 3 cups shredded mozzarella
- 2 heads broccoli OR 2 lbs green beans (for side)
- Olive oil, salt, pepper for vegetables

**Instructions**
1. Bake chicken nuggets per package directions until crispy.
2. Meanwhile, roast or steam your vegetable of choice.
3. Transfer nuggets to a large baking dish. Pour Rao sauce over top. Cover with mozzarella.
4. Broil 3–4 min until cheese is bubbly and golden.
5. Serve with vegetable on the side.

---

### Kids Mac & Cheese
**Description:** Creamy stovetop mac and cheese using evaporated milk — no draining the pasta water, which makes it extra saucy. Salad on the side.
**mealType:** Pasta
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 5 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 24 oz (2 standard boxes) macaroni noodles
- Water to cook pasta (do not drain)
- 2 cans (12 oz each) evaporated milk
- 24 oz shredded cheddar cheese
- Salt to taste
- Side salad (bagged salad mix, dressing)

**Instructions**
1. Cook macaroni in a large pot of salted water until just al dente. Do not drain — leave about ½ cup of pasta water in the pot.
2. Reduce heat to low. Add evaporated milk and stir to combine.
3. Add shredded cheddar in handfuls, stirring constantly until fully melted and sauce is smooth.
4. Season with salt. Serve immediately with salad on the side.

---

### Butternut Squash Mac & Cheese
**Description:** Roasted butternut squash blended into a creamy, naturally cheesy sauce with nutritional yeast, tossed with pasta and broccoli, topped with cheddar and baked. Rotisserie chicken optional.
**mealType:** Casserole
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 15 min (plus 1 hr roasting)
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 2 medium butternut squash, halved lengthwise
- 1 cup chicken broth
- ½ cup nutritional yeast
- Salt to taste
- 24 oz pasta (penne or rotini)
- 2 heads broccoli, cut into florets
- 2 cups shredded cheddar
- 1 rotisserie chicken, shredded (optional)

**Instructions**
1. Roast butternut squash cut-side down on a sheet pan at 400°F for 60 min until very tender.
2. Scoop flesh into blender. Add chicken broth, nutritional yeast, and salt. Blend until completely smooth. Taste and adjust nutritional yeast for cheesiness.
3. Cook pasta per package directions. Steam or roast broccoli.
4. Toss pasta, broccoli, and shredded chicken (if using) with butternut squash sauce.
5. Transfer to a large casserole dish. Top with shredded cheddar.
6. Bake at 375°F for 20 min until bubbly. Broil 2–3 min to brown the top.

---

### Taco Soup
**Description:** Quick rotisserie chicken soup with corn, beans, and canned chilis. Topped with chips, cheese, Greek yogurt, and lime.
**mealType:** Soup
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 10 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 2 rotisserie chickens, shredded
- 2 cans (15 oz each) corn, drained
- 2 cans (15 oz each) black beans or kidney beans, drained and rinsed
- 2 cans (4 oz each) diced green chilis
- 1 can (14.5 oz) diced tomatoes
- 4 cups chicken broth
- 2 tbsp taco seasoning
- Salt to taste
- **Toppings:** tortilla chips, shredded cheddar, plain Greek yogurt, lime wedges

**Instructions**
1. Combine shredded chicken, corn, beans, green chilis, diced tomatoes, broth, and taco seasoning in a large pot.
2. Bring to a boil, reduce heat, and simmer 15–20 min.
3. Taste and adjust seasoning with salt and taco seasoning.
4. Serve topped with crushed tortilla chips, shredded cheddar, a dollop of Greek yogurt (in place of sour cream), and a squeeze of lime.

---

### Coconut Curry
**Description:** Chicken marinated in yogurt and curry powder, slow-simmered with onion, carrot, sweet potato, and coconut milk. Served with naan.
**mealType:** Soup
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 20 min (plus marinating time)
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 3 lbs boneless chicken thighs or breasts, cut into chunks
- 1 cup plain Greek yogurt
- 3 tbsp curry powder, divided
- 2 large onions, diced
- 4 large carrots, sliced
- 2 medium sweet potatoes, peeled and cubed
- 2 cans (13.5 oz each) coconut milk
- 2 tsp turmeric
- 1 tsp garlic powder
- Salt and pepper to taste
- 1–2 cans (15 oz) chickpeas, drained (optional)
- 2 bell peppers, diced (optional)
- 5 pieces naan bread, halved (to serve)

**Instructions**
1. Marinate chicken in Greek yogurt, 2 tbsp curry powder, salt, and pepper for at least 30 min (or overnight).
2. Heat oil in a large pot over medium heat. Sauté onions until softened, about 5 min.
3. Add marinated chicken. Cook 5–7 min, stirring occasionally.
4. Add carrots, sweet potato, remaining curry powder, turmeric, garlic powder. Stir to coat.
5. Pour in coconut milk. Bring to a boil, then reduce heat and simmer 20–25 min until vegetables are tender.
6. Add chickpeas and bell peppers (if using) in the last 10 min.
7. Serve with warmed naan.

---

### BLTAs
**Description:** Bacon, lettuce, tomato, avocado sandwiches with mayo. Fruit on the side.
**mealType:** Sandwich
**appropriateMealTimes:** lunch, dinner
**kidFriendly:** yes
**prepTime:** 10 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 2 lbs bacon (about 30–40 slices)
- 2 heads romaine or butter lettuce, leaves separated
- 4 large tomatoes, sliced
- 5 ripe avocados, sliced
- ½ cup mayonnaise
- 1.5 loaves sandwich bread (20 slices)
- 2 lbs fruit (melon, grapes, strawberries)

**Instructions**
1. Cook bacon in batches in a skillet or oven (400°F for 15–18 min on a rack) until crispy. Drain on paper towels.
2. Toast bread if desired.
3. Spread mayo on bread slices.
4. Build each sandwich: lettuce, tomato, bacon, avocado. Season avocado with salt.
5. Serve with fruit on the side.

---

### Chicken Salad
**Description:** Classic rotisserie chicken salad with mayo, celery, and grapes. Served with fruit. Quick to assemble — kids' lunch staple.
**mealType:** Salad
**appropriateMealTimes:** lunch
**kidFriendly:** yes
**prepTime:** 8 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 2 rotisserie chickens, shredded (~4 lbs meat)
- 1 cup mayonnaise
- 4 stalks celery, diced small
- 2 cups grapes, halved
- Salt and pepper to taste
- 2 lbs fruit for side (watermelon, pineapple, etc.)

**Instructions**
1. Shred rotisserie chicken into a large bowl.
2. Add mayo, celery, and grapes. Stir to combine.
3. Season with salt and pepper. Taste and adjust mayo as needed.
4. Serve as a wrap, in a pita, on crackers, or in a cup.
5. Portion fruit on the side.
**Note:** Can be prepped and refrigerated up to 3 days ahead.

---

### Kodiak Pancakes
**Description:** High-protein Kodiak pancakes blended with cottage cheese for extra creaminess. Served with breakfast sausage and fruit.
**mealType:** Breakfast
**appropriateMealTimes:** breakfast, dinner
**kidFriendly:** yes
**prepTime:** 10 min
**lastUsageDate:** null
**url:** https://kodiakcakes.com/blogs/recipes

**Ingredients (10 servings)**
- 3 cups Kodiak Cakes Power Cakes mix
- 1 cup cottage cheese (blended smooth)
- 3 eggs
- Milk or water as needed per box directions (reduce by ½ cup since cottage cheese adds moisture)
- 2 lbs breakfast sausage links or patties
- 2 lbs fresh fruit (berries, banana slices, melon)
- Butter or cooking spray for griddle
- Maple syrup to serve

**Instructions**
1. Blend cottage cheese until smooth (30 seconds in blender).
2. Whisk together Kodiak mix, blended cottage cheese, eggs, and liquid per box directions (reduce liquid slightly).
3. Heat griddle or skillet over medium heat. Grease lightly.
4. Pour ¼ cup batter per pancake. Cook until bubbles form and edges set, about 2–3 min. Flip and cook 1–2 min more.
5. Cook breakfast sausage in a separate skillet per package directions.
6. Serve pancakes with sausage and fresh fruit.

---

### Sweet Potato Nachos
**Description:** Sheet pan nachos with roasted sweet potatoes, black beans, chicken or steak, and cheddar — topped with tomatoes, tortilla chips, Greek yogurt, and avocado.
**mealType:** Sheet Pan
**appropriateMealTimes:** dinner
**kidFriendly:** yes
**prepTime:** 15 min
**lastUsageDate:** null
**url:** null

**Ingredients (10 servings)**
- 5 medium sweet potatoes, peeled and sliced into thin rounds or cubed
- 2 cans (15 oz each) black beans, drained and rinsed
- 2 lbs rotisserie chicken (shredded) OR steak bites
- 2 cans (15 oz each) corn, drained
- 3 cups shredded cheddar cheese
- 3 tbsp olive oil
- 1 tbsp cumin, 1 tsp chili powder, salt and pepper
- **Toppings:** 3 diced tomatoes, 1 bag tortilla chips, 2 cups plain Greek yogurt, 3–4 avocados (sliced or mashed)

**Instructions**
1. Toss sweet potato in olive oil, cumin, chili powder, salt, and pepper. Roast at 425°F for 20–25 min until tender.
2. Spread sweet potatoes across 2 sheet pans. Top with black beans, corn, and chicken or steak.
3. Cover generously with shredded cheddar.
4. Bake at 375°F for 10 min until cheese melts.
5. Remove from oven. Top with diced tomatoes, avocado, and dollops of Greek yogurt. Add tortilla chips around the edges or on the side.
