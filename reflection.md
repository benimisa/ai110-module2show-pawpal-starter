# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- I used four main classes: Owner, Pet, Task, and Scheduler.
- Owner manages one or more pets. Pet stores its tasks and basic details. Task holds scheduling information and completion state. Scheduler sorts, filters, detects conflicts, and builds a daily plan.

**b. Design changes**

- I added a parent-pet link on each Task so the scheduler can filter tasks by pet more naturally.
- I also made recurring tasks create a new task when completed instead of mutating the old task in place, which keeps the history clearer.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- The scheduler considers time, completion state, and pet membership.
- I prioritized time and whether a task was already completed because those are the most direct signals for a daily plan.

**b. Tradeoffs**

- The conflict detector only checks for exact duplicate times, not overlapping durations.
- That tradeoff is reasonable for this starter app because it keeps the logic simple, readable, and easy to verify.

---

## 3. AI Collaboration

**a. How you used AI**

- I used AI to brainstorm the class structure, draft the initial Python skeleton, and refine the scheduler methods.
- The most helpful prompts were requests for class design, clear terminal output formatting, and test cases for recurring behavior.

**b. Judgment and verification**

- I did not accept every AI suggestion blindly. For example, I simplified a more complex recurring-task design so the model would not add unnecessary state.
- I verified the implementation by running the CLI demo and the pytest suite instead of trusting the suggestion on its own.

---

## 4. Testing and Verification

**a. What you tested**

- I tested task completion, task addition, time-based sorting, recurring-task creation, and conflict detection.
- These behaviors matter because they are the core of the scheduling experience and directly affect a pet owner's trust in the app.

**b. Confidence**

- I am moderately confident that the core scheduler works correctly for the current scope.
- If I had more time, I would test edge cases such as empty pet lists, invalid time strings, and overlapping durations rather than exact duplicate times.

---

## 5. Reflection

**a. What went well**

- The class design stayed clear, and the scheduler methods were easy to test from the command line.

**b. What you would improve**

- I would add richer scheduling rules such as task duration and priority weighting if I had another iteration.

**c. Key takeaway**

- A strong human architect is still essential when using AI: the model can generate code quickly, but the developer must guide structure, constraints, and verification.
