from pawpal_system import Pet, Task, Scheduler


def test_mark_complete_changes_status():
    task = Task(description="Walk", time="08:00", frequency="once")

    task.mark_complete()

    assert task.completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Mochi", species="dog")
    pet.add_task(Task(description="Feed", time="07:00", frequency="once"))

    assert len(pet.tasks) == 1


def test_sort_tasks_by_time():
    scheduler = Scheduler()
    tasks = [
        Task(description="Dinner", time="19:00", frequency="once"),
        Task(description="Breakfast", time="07:00", frequency="once"),
        Task(description="Lunch", time="12:00", frequency="once"),
    ]

    sorted_tasks = scheduler.sort_by_time(tasks)

    assert [task.description for task in sorted_tasks] == ["Breakfast", "Lunch", "Dinner"]


def test_recurring_task_creates_next_occurrence():
    pet = Pet(name="Mochi", species="dog")
    task = Task(description="Water", time="09:00", frequency="daily")
    pet.add_task(task)

    task.mark_complete()

    assert len(pet.tasks) == 2
    assert pet.tasks[-1].frequency == "daily"


def test_conflict_detection_flags_duplicate_times():
    scheduler = Scheduler()
    pet = Pet(name="Mochi", species="dog")
    pet.add_task(Task(description="Walk", time="08:00", frequency="once"))
    pet.add_task(Task(description="Feed", time="08:00", frequency="once"))

    conflicts = scheduler.detect_conflicts([pet.tasks[0], pet.tasks[1]])

    assert conflicts == ["Walk and Feed are both scheduled for 08:00"]
