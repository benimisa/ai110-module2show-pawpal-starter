from pawpal_system import Owner, Pet, Scheduler, Task


if __name__ == "__main__":
    owner = Owner(name="Jordan")
    pet_one = Pet(name="Mochi", species="dog")
    pet_two = Pet(name="Luna", species="cat")
    owner.add_pet(pet_one)
    owner.add_pet(pet_two)

    pet_one.add_task(Task(description="Morning walk", time="08:00", frequency="daily", priority="high"))
    pet_one.add_task(Task(description="Feed breakfast", time="07:30", frequency="daily", priority="high"))
    pet_two.add_task(Task(description="Play session", time="18:00", frequency="daily", priority="medium"))
    pet_two.add_task(Task(description="Grooming", time="18:00", frequency="once", priority="low"))

    scheduler = Scheduler()
    plan = scheduler.build_daily_plan(owner)

    print("Today's Schedule")
    print("----------------")
    for task in plan:
        print(f"- {task.time}: {task.description} ({task.priority})")

    conflicts = scheduler.detect_conflicts(owner.get_all_tasks())
    if conflicts:
        print("\nWarnings:")
        for warning in conflicts:
            print(f"- {warning}")
