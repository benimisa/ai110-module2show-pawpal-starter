import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")
st.caption("A simple pet-care planner that helps you organize tasks for every pet.")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")
if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

owner = st.session_state.owner
scheduler = st.session_state.scheduler

with st.expander("Owner and pets", expanded=True):
    owner_name = st.text_input("Owner name", value=owner.name)
    if st.button("Save owner"):
        owner.name = owner_name
        st.success(f"Owner updated to {owner.name}.")

    st.subheader("Add a pet")
    pet_name = st.text_input("Pet name", key="pet_name_input")
    species = st.selectbox("Species", ["dog", "cat", "other"], key="pet_species")
    if st.button("Add pet"):
        owner.add_pet(Pet(name=pet_name, species=species))
        st.success(f"Added {pet_name} the {species}.")

    if owner.pets:
        pet_names = [pet.name for pet in owner.pets]
        selected_pet_name = st.selectbox("Choose a pet", pet_names)
        selected_pet = next(pet for pet in owner.pets if pet.name == selected_pet_name)
    else:
        selected_pet = None

with st.expander("Tasks", expanded=True):
    st.subheader("Add a task")
    if selected_pet is None:
        st.info("Add a pet before scheduling tasks.")
    else:
        task_title = st.text_input("Task title", value="Morning walk", key="task_title")
        task_time = st.text_input("Time", value="08:00", key="task_time")
        frequency = st.selectbox("Frequency", ["once", "daily", "weekly"], key="task_frequency")
        priority = st.selectbox("Priority", ["low", "medium", "high"], key="task_priority")
        duration = st.number_input("Duration (minutes)", min_value=5, max_value=240, value=30, key="task_duration")

        if st.button("Add task"):
            selected_pet.add_task(
                Task(
                    description=task_title,
                    time=task_time,
                    frequency=frequency,
                    priority=priority,
                    duration_minutes=int(duration),
                )
            )
            st.success(f"Added {task_title} for {selected_pet.name}.")

    if owner.get_all_tasks():
        st.subheader("Current tasks")
        task_rows = []
        for task in owner.get_all_tasks():
            task_rows.append(
                {
                    "Pet": task.parent_pet.name if task.parent_pet else "—",
                    "Task": task.description,
                    "Time": task.time,
                    "Frequency": task.frequency,
                    "Priority": task.priority,
                }
            )
        st.table(task_rows)

st.divider()
st.subheader("Build schedule")
if st.button("Generate schedule"):
    plan = scheduler.build_daily_plan(owner)
    if plan:
        st.success("Today's plan is ready.")
        st.table(
            [
                {
                    "Time": task.time,
                    "Pet": task.parent_pet.name if task.parent_pet else "—",
                    "Task": task.description,
                    "Priority": task.priority,
                }
                for task in plan
            ]
        )
    else:
        st.info("No pending tasks to show yet.")

    conflicts = scheduler.detect_conflicts(owner.get_all_tasks())
    if conflicts:
        st.warning("Potential scheduling conflicts:")
        for warning in conflicts:
            st.write(f"- {warning}")
