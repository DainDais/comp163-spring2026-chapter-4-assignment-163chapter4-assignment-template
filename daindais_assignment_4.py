"""
COMP 163 - Introduction to Programming
Assignment: Chapter 4 - College Life Adventure Game
Name: Dain Dais
GitHub Username: DainDais
Date: 02/13/2026
Description: A 5-day college prep game where you manage energy, stress, and knowledge to pass a final exam.
AI Usage: AI helped with balancing, debugging, and general cleanup. All decision logic/story choices written by me.
"""

student_name = input("What's Your Name? ")

# Required variables
current_gpa = 3.0
study_hours = 0
social_points = 0
stress_level = 25

# Game stats
knowledge = 10
energy = 70

day = 1
turn = 1
total_turn = 1

print("Professor: Congratulations on making it to the end of the semester!")
input("Press Enter to continue...")
print("But before I can let you enjoy your summer break you have to pass your final test.")
input("Press Enter to continue...")
print(f"{student_name}: A final test? No one told me about this!")
input("Press Enter to continue...")
print("Professor: If you came to class you'd know about it, and its 50 percent of your grade.")
input("Press Enter to continue...")
print(f"{student_name}: Oh no! I have to pass this test or say good bye to summer!!")

# ----------------------------
# Helper clamp (no loops)
# ----------------------------
def_clamp = None  # identity operator placeholder (keeps Chapter 4 legal usage simple)
if def_clamp is None:
    pass

# ========================================
# DAY 1
# ========================================
print("\n" + "." * 60)
print(f"Day {day} (Monday)")
print("\nSpecial Event: Campus Coffee Shop Encounter")
print("You run into your study buddy at the coffee shop.")
print("A) Ignore them and study alone (Knowledge +15, Stress +10)")
print("B) Study together for 2 hours (Knowledge +12, Social +10, Study Hours +2)")
print("C) Chat and relax (Stress -10, Social +15, Energy +5)")

# Special event choice with membership operator
event_choice = input("Your choice (A/B/C): ")
# Using membership operator to validate input
if event_choice in ["A", "B", "C"]:
    if event_choice == "A":
        knowledge += 15
        stress_level += 10
        print(f"{student_name}: I need to focus alone right now.")
    elif event_choice == "B":
        knowledge += 12
        social_points += 10
        study_hours += 2
        print(f"{student_name}: Let's study together! Two heads are better than one.")
    else:
        stress_level -= 10
        social_points += 15
        energy += 5
        print(f"{student_name}: I need a break. Let's just hang out!")
else:
    # Invalid choice penalty
    print("Invalid choice! You wasted time being confused.")
    stress_level += 5

turn = 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nWake Up Event: Your alarm goes off at 7 AM")
print("A) Hit snooze and sleep in (Energy +15, Study Hours -1, Stress -5)")
print("B) Wake up and go for a jog (Energy +10, Stress -10)")
print("C) Wake up immediately and review notes (Knowledge +8, Energy -5, Study Hours +1)")

wake_choice = input("Your choice (A/B/C): ")

# Nested conditionals based on current energy levels
if energy < 50:
    # Low energy affects choices differently
    if wake_choice == "A":
        energy += 20
        study_hours -= 1
        stress_level -= 5
        print("You really needed that sleep!")
    elif wake_choice == "B":
        energy += 5
        stress_level -= 5
        print("The jog was tough but you pushed through.")
    else:
        knowledge += 5
        energy -= 10
        study_hours += 1
        print("You struggle to focus while tired.")
else:
    # Normal energy choices
    if wake_choice == "A":
        energy += 15
        study_hours -= 1
        stress_level -= 5
        print("A little extra sleep never hurt anyone.")
    elif wake_choice == "B":
        energy += 10
        stress_level -= 10
        print("Great workout! You feel refreshed.")
    else:
        knowledge += 8
        energy -= 5
        study_hours += 1
        print("Early morning studying is productive!")

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nFree Time: Afternoon Activity")
print("A) Library study session (Knowledge +10, Study Hours +2, Stress +8)")
print("B) Gym workout (Energy +8, Stress -12)")
print("C) Nap in dorm (Energy +20, Stress -5)")
print("D) Join friends at student center (Social +12, Energy -5)")

choice = input("Your choice (A/B/C/D): ")

if choice == "A":
    knowledge += 10
    study_hours += 2
    stress_level += 8
    print("You make good progress but feel the pressure building.")
elif choice == "B":
    energy += 8
    stress_level -= 12
    print("Exercise clears your mind!")
elif choice == "C":
    energy += 20
    stress_level -= 5
    print("That nap hit different!")
elif choice == "D":
    social_points += 12
    energy -= 5
    print("You have a great time with friends!")
else:
    print("Invalid choice! You wander around aimlessly.")
    energy -= 5

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nFree Time: Evening Activity")
print("A) Attend study group (Knowledge +12, Social +8, Study Hours +2, Stress +5)")
print("B) Watch Netflix and chill (Energy +15, Stress -8)")
print("C) Review lecture notes alone (Knowledge +15, Study Hours +2, Stress +10)")
print("D) Call family back home (Stress -15, Social +5)")

choice = input("Your choice (A/B/C/D): ")

if choice == "A":
    knowledge += 12
    social_points += 8
    study_hours += 2
    stress_level += 5
    print("Productive study session with classmates!")
elif choice == "B":
    energy += 15
    stress_level -= 8
    print("You binge watch your favorite show. Time well spent?")
elif choice == "C":
    knowledge += 15
    study_hours += 2
    stress_level += 10
    print("Solo study grind! You're learning but feeling the pressure.")
elif choice == "D":
    stress_level -= 15
    social_points += 5
    print("Talking to family always helps you feel better.")
else:
    print("Invalid choice! You waste time scrolling social media.")
    stress_level += 5

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nFree Time: Late Night Decision")
print("A) Cram study until midnight (Knowledge +18, Study Hours +3, Energy -15, Stress +15)")
print("B) Get good sleep (Energy +25, Stress -10)")
print("C) Light review then sleep (Knowledge +8, Study Hours +1, Energy +10, Stress -5)")

choice = input("Your choice (A/B/C): ")

if choice == "A":
    knowledge += 18
    study_hours += 3
    energy -= 15
    stress_level += 15
    print("You study hard but you're exhausted and anxious.")
elif choice == "B":
    energy += 25
    stress_level -= 10
    print("You sleep like a baby. Tomorrow is a new day!")
elif choice == "C":
    knowledge += 8
    study_hours += 1
    energy += 10
    stress_level -= 5
    print("Balanced approach! You feel pretty good.")
else:
    print("Invalid choice! You stay up worrying about nothing.")
    energy -= 10
    stress_level += 10

total_turn += 1

# clamp
if energy > 100:
    energy = 100
if energy < 0:
    energy = 0
if stress_level > 100:
    stress_level = 100
if stress_level < 0:
    stress_level = 0
if knowledge > 100:
    knowledge = 100
if knowledge < 0:
    knowledge = 0

print("\nEnd of Day Stats:")
print(f"Energy: {energy} | Knowledge: {knowledge} | Social: {social_points} | Stress: {stress_level} | Study Hours: {study_hours}")

day += 1

# ========================================
# DAY 2
# ========================================
print("\n" + "." * 60)
print(f"Day {day} (Tuesday)")
print("\nSpecial Event: Pop Quiz Surprise!")
print("Your professor announces an unexpected quiz that could give bonus knowledge.")
print("A) Take the quiz confidently (Knowledge +10 if knowledge > 30, else +5)")
print("B) Skip class and study instead (Knowledge +8, Study Hours +2, Stress +5)")
print("C) Take quiz but you're nervous (Knowledge +3, Stress +15)")

event_choice = input("Your choice (A/B/C): ")

# Using comparison operators and nested conditionals
if event_choice == "A":
    if knowledge > 30:
        knowledge += 10
        print("You ace the quiz! Your studying is paying off!")
    else:
        knowledge += 5
        print("You struggle but learn from it.")
elif event_choice == "B":
    knowledge += 8
    study_hours += 2
    stress_level += 5
    print("You skip and study, but feel guilty about missing class.")
elif event_choice == "C":
    knowledge += 3
    stress_level += 15
    print("Anxiety got the best of you during the quiz.")
else:
    print("Invalid choice! You froze and missed the opportunity.")
    stress_level += 10

turn = 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nWake Up Event: Morning Routine")
print("A) Quick breakfast and review (Knowledge +5, Energy +10, Study Hours +1)")
print("B) Sleep through breakfast (Energy +15, Study Hours -1)")
print("C) Healthy breakfast and meditation (Energy +12, Stress -12)")

wake_choice = input("Your choice (A/B/C): ")

if wake_choice == "A":
    knowledge += 5
    energy += 10
    study_hours += 1
    print("Productive morning!")
elif wake_choice == "B":
    energy += 15
    study_hours -= 1
    print("You wake up late but well-rested.")
else:
    energy += 12
    stress_level -= 12
    print("You feel centered and ready for the day!")

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nFree Time: Afternoon Activity")
print("A) Attend professor's office hours (Knowledge +15, Study Hours +2, Stress +5)")
print("B) Play video games (Energy +10, Stress -10)")
print("C) Form a new study group (Knowledge +12, Social +15, Study Hours +2)")
print("D) Take a power nap (Energy +18, Stress -8)")

choice = input("Your choice (A/B/C/D): ")

if choice == "A":
    knowledge += 15
    study_hours += 2
    stress_level += 5
    print("The professor explains concepts that really help!")
elif choice == "B":
    energy += 10
    stress_level -= 10
    print("Gaming session! You needed this break.")
elif choice == "C":
    knowledge += 12
    social_points += 15
    study_hours += 2
    print("Great connections and productive studying!")
elif choice == "D":
    energy += 18
    stress_level -= 8
    print("Power nap recharged your batteries!")
else:
    print("Invalid choice! You procrastinate.")
    energy -= 5

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nFree Time: Evening Activity")
print("A) Practice problems from textbook (Knowledge +15, Study Hours +3, Stress +12)")
print("B) Go to campus event (Social +20, Energy -8)")
print("C) Meal prep and relax (Energy +12, Stress -10)")
print("D) Tutorial videos online (Knowledge +10, Study Hours +1, Stress +3)")

choice = input("Your choice (A/B/C/D): ")

if choice == "A":
    knowledge += 15
    study_hours += 3
    stress_level += 12
    print("Intense practice session! You're getting better but tired.")
elif choice == "B":
    social_points += 20
    energy -= 8
    print("Amazing time at the event! Lots of new friends!")
elif choice == "C":
    energy += 12
    stress_level -= 10
    print("Self-care is important. You feel much better!")
elif choice == "D":
    knowledge += 10
    study_hours += 1
    stress_level += 3
    print("Videos are helpful! Learned some new tricks.")
else:
    print("Invalid choice! You doom-scroll on your phone.")
    stress_level += 8

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nFree Time: Late Night Decision")
print("A) All-nighter study session (Knowledge +20, Study Hours +4, Energy -25, Stress +20)")
print("B) Review then early sleep (Knowledge +10, Study Hours +2, Energy +15, Stress -8)")
print("C) Just sleep (Energy +30, Stress -15)")

choice = input("Your choice (A/B/C): ")

if choice == "A":
    knowledge += 20
    study_hours += 4
    energy -= 25
    stress_level += 20
    print("You pull an all-nighter! Learned a lot but at what cost?")
elif choice == "B":
    knowledge += 10
    study_hours += 2
    energy += 15
    stress_level -= 8
    print("Smart balance of study and rest!")
elif choice == "C":
    energy += 30
    stress_level -= 15
    print("You prioritize rest. Your body thanks you!")
else:
    print("Invalid choice! You stay up watching random videos.")
    energy -= 15
    stress_level += 5

total_turn += 1

# clamp
if energy > 100:
    energy = 100
if energy < 0:
    energy = 0
if stress_level > 100:
    stress_level = 100
if stress_level < 0:
    stress_level = 0
if knowledge > 100:
    knowledge = 100
if knowledge < 0:
    knowledge = 0

print("\nEnd of Day Stats:")
print(f"Energy: {energy} | Knowledge: {knowledge} | Social: {social_points} | Stress: {stress_level} | Study Hours: {study_hours}")

day += 1

# ========================================
# DAY 3
# ========================================
print("\n" + "." * 60)
print(f"Day {day} (Wednesday)")
print("\nSpecial Event: Midweek Crisis!")
print("You realize you're behind schedule. The test is in 2 days!")
print("A) Panic study mode (Knowledge +15, Study Hours +3, Stress +25)")
print("B) Make a strategic study plan (Knowledge +10, Study Hours +2, Stress -5)")
print("C) Take a mental health day (Energy +20, Stress -20, Study Hours -2)")

event_choice = input("Your choice (A/B/C): ")

# Using logical operators (and/or)
if event_choice == "A":
    knowledge += 15
    study_hours += 3
    stress_level += 25
    print("You panic but push through with intense studying!")
elif event_choice == "B":
    knowledge += 10
    study_hours += 2
    stress_level -= 5
    print("Smart planning! You feel more in control.")
elif event_choice == "C":
    energy += 20
    stress_level -= 20
    study_hours -= 2
    print("Sometimes you need to step back to move forward.")
else:
    print("Invalid choice! You freeze up from the pressure.")
    stress_level += 15

turn = 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nWake Up Event: Hump Day Motivation")
print("A) Early library run (Knowledge +8, Study Hours +2, Energy -5)")
print("B) Breakfast with friends (Social +10, Energy +12, Stress -8)")
print("C) Sleep in and skip morning class (Energy +20, Knowledge -5)")

wake_choice = input("Your choice (A/B/C): ")

# Using 'not in' membership operator
if wake_choice not in ["A", "B", "C"]:
    print("Invalid choice! You overslept accidentally.")
    energy += 10
    stress_level += 10
elif wake_choice == "A":
    knowledge += 8
    study_hours += 2
    energy -= 5
    print("Library grind! Getting serious now.")
elif wake_choice == "B":
    social_points += 10
    energy += 12
    stress_level -= 8
    print("Friends give you the motivation you needed!")
else:
    energy += 20
    knowledge -= 5
    print("You slept through an important lecture. Oops!")

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nFree Time: Afternoon Activity")
print("A) Intense study session (Knowledge +18, Study Hours +3, Stress +15, Energy -10)")
print("B) Study with music breaks (Knowledge +12, Study Hours +2, Stress +5)")
print("C) Exercise to clear mind (Energy +15, Stress -15)")
print("D) Social media break (Stress +10, Energy -5)")

choice = input("Your choice (A/B/C/D): ")

if choice == "A":
    knowledge += 18
    study_hours += 3
    stress_level += 15
    energy -= 10
    print("Beast mode studying! You're exhausted but learning.")
elif choice == "B":
    knowledge += 12
    study_hours += 2
    stress_level += 5
    print("Music helps you focus and stay motivated!")
elif choice == "C":
    energy += 15
    stress_level -= 15
    print("Exercise was exactly what you needed!")
elif choice == "D":
    stress_level += 10
    energy -= 5
    print("You fell into a social media rabbit hole...")
else:
    print("Invalid choice! You stare at your books without focusing.")
    stress_level += 5

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nFree Time: Evening Activity")
print("A) Join intensive tutoring session (Knowledge +20, Study Hours +3, Stress +10, Energy -8)")
print("B) Self-paced online learning (Knowledge +12, Study Hours +2, Stress +5)")
print("C) Dinner and movie night (Social +15, Energy +10, Stress -12)")
print("D) Create study guides (Knowledge +15, Study Hours +2, Stress +8)")

choice = input("Your choice (A/B/C/D): ")

if choice == "A":
    knowledge += 20
    study_hours += 3
    stress_level += 10
    energy -= 8
    print("Tutor session was intense but super helpful!")
elif choice == "B":
    knowledge += 12
    study_hours += 2
    stress_level += 5
    print("Learning at your own pace works well!")
elif choice == "C":
    social_points += 15
    energy += 10
    stress_level -= 12
    print("Great night with friends! You needed this.")
elif choice == "D":
    knowledge += 15
    study_hours += 2
    stress_level += 8
    print("Making study guides helps you organize information!")
else:
    print("Invalid choice! You overthink your strategy.")
    stress_level += 10

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nFree Time: Late Night Decision")
print("A) Marathon study session (Knowledge +22, Study Hours +4, Energy -20, Stress +18)")
print("B) Moderate study and rest (Knowledge +12, Study Hours +2, Energy +10, Stress -5)")
print("C) Full rest for tomorrow (Energy +28, Stress -12)")

choice = input("Your choice (A/B/C): ")

if choice == "A":
    knowledge += 22
    study_hours += 4
    energy -= 20
    stress_level += 18
    print("You study until you can't keep your eyes open!")
elif choice == "B":
    knowledge += 12
    study_hours += 2
    energy += 10
    stress_level -= 5
    print("Balanced approach keeps you effective!")
elif choice == "C":
    energy += 28
    stress_level -= 12
    print("Rest up! Tomorrow is another day.")
else:
    print("Invalid choice! You toss and turn with anxiety.")
    energy -= 5
    stress_level += 15

total_turn += 1

# clamp
if energy > 100:
    energy = 100
if energy < 0:
    energy = 0
if stress_level > 100:
    stress_level = 100
if stress_level < 0:
    stress_level = 0
if knowledge > 100:
    knowledge = 100
if knowledge < 0:
    knowledge = 0

print("\nEnd of Day Stats:")
print(f"Energy: {energy} | Knowledge: {knowledge} | Social: {social_points} | Stress: {stress_level} | Study Hours: {study_hours}")

day += 1

# ========================================
# DAY 4
# ========================================
print("\n" + "." * 60)
print(f"Day {day} (Thursday)")
print("\nSpecial Event: Crunch Time!")
print("It's the day before the test. You can feel the pressure mounting.")
print("A) Emergency cramming (Knowledge +18, Study Hours +4, Stress +30, Energy -15)")
print("B) Focused review of weak areas (Knowledge +15, Study Hours +3, Stress +10)")
print("C) Trust your prep and relax (Stress -25, Energy +15)")

event_choice = input("Your choice (A/B/C): ")

# Using comparison and logical operators together
if event_choice == "A" and energy > 40:
    knowledge += 18
    study_hours += 4
    stress_level += 30
    energy -= 15
    print("You cram hard! High stress but learning a lot.")
elif event_choice == "A" and energy <= 40:
    knowledge += 10
    study_hours += 2
    stress_level += 35
    energy -= 20
    print("You try to cram but you're too tired to focus well!")
elif event_choice == "B":
    knowledge += 15
    study_hours += 3
    stress_level += 10
    print("Smart strategy! Targeting your weaknesses.")
elif event_choice == "C":
    stress_level -= 25
    energy += 15
    print("You trust your preparation. Confidence is key!")
else:
    print("Invalid choice! You spiral into stress.")
    stress_level += 20

turn = 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nWake Up Event: Final Prep Day")
print("A) Review flashcards over breakfast (Knowledge +10, Study Hours +1, Energy +8)")
print("B) Light exercise and positive thoughts (Energy +15, Stress -15)")
print("C) Sleep in to conserve energy (Energy +25, Study Hours -1)")

wake_choice = input("Your choice (A/B/C): ")

if wake_choice == "A":
    knowledge += 10
    study_hours += 1
    energy += 8
    print("Flashcards are helping concepts stick!")
elif wake_choice == "B":
    energy += 15
    stress_level -= 15
    print("You feel positive and energized!")
else:
    energy += 25
    study_hours -= 1
    print("Extra sleep helps you feel refreshed.")

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nFree Time: Afternoon Activity")
print("A) Final comprehensive review (Knowledge +16, Study Hours +3, Stress +12, Energy -12)")
print("B) Practice test simulation (Knowledge +18, Study Hours +2, Stress +15, Energy -8)")
print("C) Light review and breaks (Knowledge +10, Study Hours +1, Stress +3)")
print("D) Complete rest (Energy +20, Stress -18)")

choice = input("Your choice (A/B/C/D): ")

if choice == "A":
    knowledge += 16
    study_hours += 3
    stress_level += 12
    energy -= 12
    print("Comprehensive review! Covering all bases.")
elif choice == "B":
    knowledge += 18
    study_hours += 2
    stress_level += 15
    energy -= 8
    print("Practice test shows what you know and don't know!")
elif choice == "C":
    knowledge += 10
    study_hours += 1
    stress_level += 3
    print("Light touch keeps you sharp without burnout.")
elif choice == "D":
    energy += 20
    stress_level -= 18
    print("Sometimes rest is the best preparation!")
else:
    print("Invalid choice! You pace nervously.")
    stress_level += 12

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nFree Time: Evening Activity")
print("A) Last minute cramming (Knowledge +12, Study Hours +2, Stress +20, Energy -15)")
print("B) Group review session (Knowledge +14, Social +10, Study Hours +2, Stress +8)")
print("C) Relaxing dinner and early night (Energy +18, Stress -15)")
print("D) Organize notes and materials (Knowledge +8, Study Hours +1, Stress -5)")

choice = input("Your choice (A/B/C/D): ")

# Using identity operator
last_minute_cramming = "A"
if choice is last_minute_cramming:
    knowledge += 12
    study_hours += 2
    stress_level += 20
    energy -= 15
    print("Last minute panic studying! Is it helping or hurting?")
elif choice == "B":
    knowledge += 14
    social_points += 10
    study_hours += 2
    stress_level += 8
    print("Group session helps clarify final concepts!")
elif choice == "C":
    energy += 18
    stress_level -= 15
    print("Smart! Rest before the big day.")
elif choice == "D":
    knowledge += 8
    study_hours += 1
    stress_level -= 5
    print("Organization helps you feel prepared!")
else:
    print("Invalid choice! You worry excessively.")
    stress_level += 15

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nFree Time: Night Before Test")
print("A) Study until you drop (Knowledge +15, Study Hours +3, Energy -25, Stress +25)")
print("B) Quick review and good sleep (Knowledge +8, Study Hours +1, Energy +20, Stress -10)")
print("C) Just sleep - you've done enough (Energy +30, Stress -20)")

choice = input("Your choice (A/B/C): ")

# Using 'not' logical operator
if not (choice == "A" or choice == "B" or choice == "C"):
    print("Invalid choice! You have nightmares about the test.")
    energy -= 10
    stress_level += 20
elif choice == "A":
    knowledge += 15
    study_hours += 3
    energy -= 25
    stress_level += 25
    print("You study until exhaustion. Will you regret this tomorrow?")
elif choice == "B":
    knowledge += 8
    study_hours += 1
    energy += 20
    stress_level -= 10
    print("Perfect balance! Quick review then rest.")
else:
    energy += 30
    stress_level -= 20
    print("You sleep peacefully knowing you're as ready as you'll be.")

total_turn += 1

# clamp
if energy > 100:
    energy = 100
if energy < 0:
    energy = 0
if stress_level > 100:
    stress_level = 100
if stress_level < 0:
    stress_level = 0
if knowledge > 100:
    knowledge = 100
if knowledge < 0:
    knowledge = 0

print("\nEnd of Day Stats:")
print(f"Energy: {energy} | Knowledge: {knowledge} | Social: {social_points} | Stress: {stress_level} | Study Hours: {study_hours}")

day += 1

# ========================================
# DAY 5
# ========================================
print("\n" + "." * 60)
print(f"Day {day} (Friday - TEST DAY)")
print("\nSpecial Event: Morning of the Final Exam")
print("You wake up and the test is in a few hours!")
print("A) Quick panic review (Knowledge +5, Stress +20, Energy -10)")
print("B) Meditate and visualize success (Stress -20, Energy +10)")
print("C) Healthy breakfast and calm preparation (Energy +15, Stress -10, Knowledge +5)")

event_choice = input("Your choice (A/B/C): ")

if event_choice == "A":
    knowledge += 5
    stress_level += 20
    energy -= 10
    print("Last second cramming! Your mind is racing!")
elif event_choice == "B":
    stress_level -= 20
    energy += 10
    print("You center yourself. Calm mind, clear thoughts.")
elif event_choice == "C":
    energy += 15
    stress_level -= 10
    knowledge += 5
    print("Perfect test day preparation!")
else:
    print("Invalid choice! You panic and forget to eat.")
    stress_level += 15
    energy -= 5

turn = 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nBefore Test: Final Moments")
print("A) Frantically review notes (Knowledge +3, Stress +15)")
print("B) Take deep breaths and relax (Stress -15, Energy +5)")
print("C) Chat with confident classmates (Stress +5, Knowledge +5, Social +5)")

wake_choice = input("Your choice (A/B/C): ")

if wake_choice == "A":
    knowledge += 3
    stress_level += 15
    print("You're frantically flipping through pages!")
elif wake_choice == "B":
    stress_level -= 15
    energy += 5
    print("Breathing exercises calm your nerves.")
else:
    stress_level += 5
    knowledge += 5
    social_points += 5
    print("Their confidence is somewhat contagious!")

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nDuring Test: Question Strategy")
print("A) Answer questions in order (Knowledge stays same)")
print("B) Skip hard questions, come back (Stress -8, Knowledge +3)")
print("C) Rush through to finish early (Stress +10, Knowledge -5)")

choice = input("Your choice (A/B/C): ")

if choice == "A":
    print("You methodically work through each question.")
elif choice == "B":
    stress_level -= 8
    knowledge += 3
    print("Smart strategy! Answer what you know first.")
elif choice == "C":
    stress_level += 10
    knowledge -= 5
    print("You rush and make careless mistakes!")
else:
    print("Invalid choice! You waste time being indecisive.")
    stress_level += 10

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nDuring Test: Difficult Question")
print("A) Take your time and think it through (Knowledge +5, Stress +5)")
print("B) Make your best guess and move on (Stress -5)")
print("C) Panic and leave it blank (Stress +15, Knowledge -3)")

choice = input("Your choice (A/B/C): ")

if choice == "A":
    knowledge += 5
    stress_level += 5
    print("You work through the logic carefully.")
elif choice == "B":
    stress_level -= 5
    print("You make an educated guess and continue.")
elif choice == "C":
    stress_level += 15
    knowledge -= 3
    print("Panic takes over! You can't think straight.")
else:
    print("Invalid choice! You second-guess everything.")
    stress_level += 8

total_turn += 1
turn += 1

print(f"\nTURN {total_turn}/20 (Turn {turn}/4)")
print("\nFinal Minutes: Last Check")
print("A) Review all answers carefully (Knowledge +8, Stress +10)")
print("B) Submit and leave (Stress -10)")
print("C) Change answers based on gut feeling (Knowledge -5, Stress +5)")

choice = input("Your choice (A/B/C): ")

if choice == "A":
    knowledge += 8
    stress_level += 10
    print("You catch a few mistakes in your review!")
elif choice == "B":
    stress_level -= 10
    print("You're done! Time to relax.")
elif choice == "C":
    knowledge -= 5
    stress_level += 5
    print("Second-guessing might have hurt you...")
else:
    print("Invalid choice! You turn it in with uncertainty.")
    stress_level += 5

total_turn += 1

# clamp
if energy > 100:
    energy = 100
if energy < 0:
    energy = 0
if stress_level > 100:
    stress_level = 100
if stress_level < 0:
    stress_level = 0
if knowledge > 100:
    knowledge = 100
if knowledge < 0:
    knowledge = 0

print("\nEnd of Day Stats:")
print(f"Energy: {energy} | Knowledge: {knowledge} | Social: {social_points} | Stress: {stress_level} | Study Hours: {study_hours}")

# ========================================
# FINAL ENDINGS (3 endings)
# ========================================
print("\n" + "." * 60)
print("Final Test Results:")
print("You anxiously wait for your grade...")
input("Press Enter to see your result...")

# Worst ending: too much stress -> mental breakdown
if stress_level >= 85:
    print("\n" + "=" * 60)
    print("WORST ENDING: STRESS BREAKDOWN")
    print("=" * 60)
    print(f"\n{student_name}, you were so overwhelmed by stress that you couldn't")
    print("think clearly during the test. You had a panic attack and had to")
    print("leave the exam room early. The professor offers you a medical")
    print("withdrawal, but you'll have to retake the class next semester.")
    print("\nYour final stats:")
    print(f"Knowledge: {knowledge} | Stress: {stress_level} | Study Hours: {study_hours}")
    print("\nLesson learned: Mental health matters! Balance is everything.")
# Good ending: enough knowledge and managed stress
elif knowledge >= 65 and stress_level < 85:
    print("\n" + "=" * 60)
    print("GOOD ENDING: SUCCESS!")
    print("=" * 60)
    print(f"\nCongratulations {student_name}! You passed the final with flying colors!")
    print("Your balanced approach of studying hard while managing your stress")
    print("paid off. You not only passed but learned valuable life skills about")
    print("time management and self-care. Enjoy your summer break - you earned it!")
    print("\nYour final stats:")
    print(f"Knowledge: {knowledge} | Stress: {stress_level} | Study Hours: {study_hours}")
    
    # Bonus message for exceptional performance
    if knowledge >= 85 and stress_level < 50:
        print("\n*** EXCEPTIONAL PERFORMANCE ***")
        print("Your professor was so impressed that they want you to be a tutor next semester!")
# Bad ending: not enough knowledge
else:
    print("\n" + "=" * 60)
    print("BAD ENDING: DIDN'T PASS")
    print("=" * 60)
    print(f"\nSorry {student_name}, you didn't pass the final exam.")
    print("You didn't prepare enough and it showed on the test.")
    print("You'll need to retake this class, which means no summer break.")
    print("But hey, at least you learned that cramming doesn't work!")
    print("\nYour final stats:")
    print(f"Knowledge: {knowledge} | Stress: {stress_level} | Study Hours: {study_hours}")
    print("\nLesson learned: Consistent effort beats last-minute cramming!")

print("\n" + "=" * 60)
print("Thanks for playing College Life Adventure Game!")
print("=" * 60)