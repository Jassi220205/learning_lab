# ---------------- FSM TRANSITION FUNCTION ----------------

def transition(state):
    position, room_a, room_b = state

    # Terminal state
    if room_a == "Clean" and room_b == "Clean":
        return state, "NoOp"

    # Vacuum at Room A
    if position == "A":
        if room_a == "Dirty":
            return ("A", "Clean", room_b), "Suck"
        else:
            return ("B", room_a, room_b), "Move Right"

    # Vacuum at Room B
    if position == "B":
        if room_b == "Dirty":
            return ("B", room_a, "Clean"), "Suck"
        else:
            return ("A", room_a, room_b), "Move Left"


# ---------------- FSM EXECUTION ENGINE ----------------

def run_fsm(initial_state):
    state = initial_state
    step = 0

    print("Vacuum Cleaner Status: IDLE")
    print(f"Initial State: {state}\n")

    while True:
        next_state, action = transition(state)
        print(f"Step {step}:")
        print(f"Current State : {state}")
        print(f"Action Taken  : {action}\n")

        if action == "NoOp":
            break

        state = next_state
        step += 1

    print("Final State Reached:", state)


# ---------------- USER TEST CASE SELECTION ----------------

print("Select Test Case:")
print("a. Both rooms are dirty")
print("b. Only Room A is dirty")
print("c. Only Room B is dirty")
print("d. Both rooms are clean")

choice = input("Enter your choice (a/b/c/d): ").lower()

# Initial state assumption: Vacuum starts in Room A
if choice == "a":
    initial_state = ("A", "Dirty", "Dirty")
elif choice == "b":
    initial_state = ("A", "Dirty", "Clean")
elif choice == "c":
    initial_state = ("A", "Clean", "Dirty")
elif choice == "d":
    initial_state = ("A", "Clean", "Clean")
else:
    print("Invalid choice")
    exit()

run_fsm(initial_state)
