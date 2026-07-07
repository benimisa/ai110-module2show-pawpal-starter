# PawPal+ (Module 2 Project)

PawPal+ is a lightweight pet-care planner built with Python and Streamlit. It helps an owner track pets, create care tasks, and view a sorted daily schedule with simple conflict detection and recurring-task support.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks such as walks, feeding, grooming, and play
- Keep tasks organized by time and priority
- Surface basic scheduling conflicts before they become a problem
- Repeat daily or weekly tasks automatically after they are completed

## What the app does

- Lets a user enter owner and pet information
- Lets a user add tasks with a time, frequency, priority, and duration
- Builds a simple daily schedule from the owner's pets
- Displays warnings when two tasks share the same time
- Supports recurring tasks for daily or weekly routines

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Run the CLI demo

```bash
python main.py
```

### Run the tests

```bash
python -m pytest
```

## 🖥️ Sample Output

```text
Today's Schedule
----------------
- 07:30: Feed breakfast (high)
- 08:00: Morning walk (high)
- 18:00: Play session (medium)

Warnings:
- Play session and Grooming are both scheduled for 18:00
```

## 🧪 Testing PawPal+

Run the test suite with:

```bash
python -m pytest
```

Example result:

```text
======================== test session starts ========================
5 passed in 0.09s
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | Scheduler.sort_by_time() | Tasks are ordered by chronological time |
| Filtering | Scheduler.filter_tasks() | Filters by pet name or completion state |
| Conflict handling | Scheduler.detect_conflicts() | Warns when two tasks share the same time |
| Recurring tasks | Task.mark_complete() | Daily and weekly tasks create a new follow-up task |

## 📸 Demo Walkthrough

1. Open the Streamlit app and enter an owner name.
2. Add one or more pets to the owner's profile.
3. Create tasks for each pet with a time, priority, and frequency.
4. Click Generate schedule to view the sorted plan.
5. Review any conflict warnings before finalizing the day.

**Screenshot or video** *(optional)*: Add your own screenshot here if you want to share a visual demo.
