class MonkeyBananaProblem:
    def __init__(self):
        self.monkey_position = "floor"
        self.chair_position = "floor"
        self.stick_position = "floor"
        self.banana_position = "ceiling"

        self.monkey_on_chair = False
        self.monkey_has_stick = False

    def move_chair(self):
        if self.monkey_position == "floor" and self.chair_position == "floor":
            self.chair_position = "under_banana"
            print("Monkey moved the chair under the banana.")
        else:
            print("Monkey cannot move the chair.")

    def climb_chair(self):
        if self.chair_position == "under_banana" and self.monkey_position == "floor":
            self.monkey_position = "chair"
            self.monkey_on_chair = True
            print("Monkey climbed onto the chair.")
        else:
            print("Monkey cannot climb the chair.")

    def pick_stick(self):
        if self.monkey_on_chair and not self.monkey_has_stick:
            self.monkey_has_stick = True
            print("Monkey picked up the stick.")
        else:
            print("Monkey cannot pick the stick.")

    def knock_banana(self):
        if self.monkey_on_chair and self.monkey_has_stick:
            self.banana_position = "floor"
            print("Monkey knocked down the banana. Goal achieved!")
        else:
            print("Monkey cannot knock down the banana.")

    def show_state(self):
        print("\n--- Current State ---")
        print("Monkey position:", self.monkey_position)
        print("Chair position:", self.chair_position)
        print("Stick with monkey:", self.monkey_has_stick)
        print("Banana position:", self.banana_position)
        print("---------------------\n")

    def menu(self):
        while True:
            print("Choose an action:")
            print("1. Move chair")
            print("2. Climb chair")
            print("3. Pick stick")
            print("4. Knock banana")
            print("5. Show state")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.move_chair()
            elif choice == "2":
                self.climb_chair()
            elif choice == "3":
                self.pick_stick()
            elif choice == "4":
                self.knock_banana()
            elif choice == "5":
                self.show_state()
            elif choice == "6":
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")


# Run the program
problem = MonkeyBananaProblem()
problem.menu()
