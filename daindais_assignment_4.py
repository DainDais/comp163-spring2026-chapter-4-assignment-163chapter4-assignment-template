"""
COMP 163 - Introduction to Programming
Assignment: Chapter 4 - College Life Adventure Game
Name: Dain Dais
GitHub Username: DainDais
Date: 02/13/2026
Description: The goal of the game is to pass your test in 5 days.
            The game starts on monday and you'll have 4 turns per day
            To prepare for the test. But there will be other factors to consider
            that can determine how you perform in the end.
AI Usage: [Describe any AI assistance OR write "None"]
"""

student_name = input("What's Your Name? ")
current_gpa = 3.0
study_hours = 0
social_points = 0
stress_level = 25
knowledge = 10
energy = 70
day = 1
turn = 1
# Introduction
print("Professor: Congratulations on making it to the end of the semester!")
input("Press Enter to continue...")
print("But before I can let you enjoy your summer break you have to pass your final test.")
input(" ")
print(f"{student_name}: A final test? No one told me about this!")
input(" ")
print("Professor: If you came to class you'd know about it, and its 50 percent of your grade.")
input(" ")
print(f"{student_name}: Oh no! I have to pass this test or say good bye to summer!!")
print("..........................................................................................................")

print(f"Day {day}:")
print("Current Stats:")
print(f"    Energy: {energy}")
print(f"    Knowledge: {knowledge}")
print(f"    Social Points: {social_points}")
print(f"    Stress Level: {stress_level}")
print(f"    Study Hours: {study_hours}")
print(f"    GPA: {current_gpa}")

# ========================================
# Decision 1: Wake Up
# ========================================
if turn == 1:
    print("TURN 1/20")
    print("For some reason you feel the urge to sleep in.\n Doing so would cost you 1 turn, but increase energy and lower stress")
    print("Do you want to sleep in? (y/n)")
descision = input()

if descision == "y":
    energy += 20
    stress_level -= 10
    print("You decided to sleep in. Your energy has increased and your stress level has decreased.")
    print(f"+20 Energy: {energy}, -10 Stress: {stress_level}")
    # Sleeping in uses up time, so we skip a turn
    turn += 2

elif descision == "n":
    print("You decided to get up early.")
    turn += 1

else:
    print("Invalid input. Please enter 'y' or 'n'.")
    # Default behavior so the game can still run without crashing
    print("TURN 2/20")

# Keep stats in a sensible range (no loops, just simple bounds)
if energy > 100:
    energy = 100
if energy < 0:
    energy = 0
if stress_level > 100:
    stress_level = 100
if stress_level < 0:
    stress_level = 0

# ========================================
# Decision 2: Free Time Activity
# ========================================
if turn == 2:
    print("What will you do?\n 1. Study\n 2. Socialize\n 3. Relax")
    descision = input("Enter a Number: ")

# Study: strong gain, but costs energy and raises stress
if descision == "1" and energy >= 40 and stress_level <= 70:
    study_hours += 2
    knowledge += 7
    energy -= 12
    stress_level += 8
    print("You decided to study.")
    print(f"+2 Study Hours: {study_hours}, +7 Knowledge: {knowledge}, -12 Energy: {energy}, +8 Stress: {stress_level}")
    turn += 1

# Socialize: best when you're worn out (low energy) and stressed (high stress)
elif descision == "2" and energy < 50 and stress_level > 70:
    social_points += 10
    knowledge -= 3
    energy += 5
    stress_level -= 20
    print("You decided to socialize.")
    print(f"+10 Social Points: {social_points}, -3 Knowledge: {knowledge}, +5 Energy: {energy}, -20 Stress: {stress_level}")
    turn += 1

# Relax: safe recovery option
elif descision == "3":
    energy += 10
    stress_level -= 20
    print("You decided to relax.")
    print(f"+10 Energy: {energy}, -20 Stress: {stress_level}")
    turn += 1

else:
    print("That choice didn't work with your current stats (or was invalid). Nothing changes this turn.")


# Keep stats in a sensible range (again, no loops)
if energy > 100:
    energy = 100
if energy < 0:
    energy = 0
if stress_level > 100:
    stress_level = 100
if stress_level < 0:
    stress_level = 0
if knowledge < 0:
    knowledge = 0
if knowledge > 100:
    knowledge = 100
else: 
    pass

print("\nUpdated Stats:")
print(f"    Energy: {energy}")
print(f"    Knowledge: {knowledge}")
print(f"    Social Points: {social_points}")
print(f"    Stress Level: {stress_level}")
print(f"    Study Hours: {study_hours}")
print(f"    GPA: {current_gpa}")

# ========================================
# Decision 3: Free Time Activity
# ========================================
if turn == 3:
    print("TURN 3/20")
    print("What will you do?\n 1. Study\n 2. Socialize\n 3. Relax")
    descision = input("Enter a Number: ")

# Study: strong gain, but costs energy and raises stress
if descision == "1" and energy >= 40 and stress_level <= 70:
    study_hours += 2
    knowledge += 7
    energy -= 12
    stress_level += 8
    print("You decided to study.")
    print(f"+2 Study Hours: {study_hours}, +7 Knowledge: {knowledge}, -12 Energy: {energy}, +8 Stress: {stress_level}")

# Socialize: best when you're worn out (low energy) and stressed (high stress)
elif descision == "2" and energy < 50 and stress_level > 70:
    social_points += 10
    knowledge -= 3
    energy += 5 
    stress_level -= 20
    print("You decided to socialize.")
    print(f"+10 Social Points: {social_points}, +5 Energy: {energy}, -20 Stress: {stress_level}")

# Relax: safe recovery option
elif descision == "3":
    energy += 10
    stress_level -= 20
    print("You decided to relax.")
    print(f"+10 Energy: {energy}, -20 Stress: {stress_level}")

else:
    print("That choice didn't work with your current stats (or was invalid). Nothing changes this turn.")

# Keep stats in a sensible range (again, no loops)
if energy > 100:
    energy = 100
if energy < 0:
    energy = 0
if stress_level > 100:
    stress_level = 100
if stress_level < 0:
    stress_level = 0
if knowledge < 0:
    knowledge = 0
if knowledge > 100:
    knowledge = 100

# ========================================
# Decision 4: Free Time Activity
# ========================================
if turn == 4:
    print("TURN 4/20")
    print("What will you do?\n 1. Study\n 2. Socialize\n 3. Relax")
    descision = input("Enter a Number: ")

# Study: strong gain, but costs energy and raises stress
if descision == "1" and energy >= 40 and stress_level <= 70:
    study_hours += 2
    knowledge += 7
    energy -= 12
    stress_level += 8
    print("You decided to study.")
    print(f"+2 Study Hours: {study_hours}, +7 Knowledge: {knowledge}, -12 Energy: {energy}, +8 Stress: {stress_level}")

# Socialize: best when you're worn out (low energy) and stressed (high stress)
elif descision == "2" and energy < 50 and stress_level > 70:
    social_points += 10
    knowledge -= 3
    energy += 5
    stress_level -= 20
    print("You decided to socialize.")
    print(f"+10 Social Points: {social_points}, -3 Knowledge: {knowledge}, +5 Energy: {energy}, -20 Stress: {stress_level}")

# Relax: safe recovery option
elif descision == "3":
    energy += 10
    stress_level -= 20
    print("You decided to relax.")
    print(f"+10 Energy: {energy}, -20 Stress: {stress_level}")

else:
    print("That choice didn't work with your current stats (or was invalid). Nothing changes this turn.")


# Keep stats in a sensible range (again, no loops)
if energy > 100:
    energy = 100
if energy < 0:
    energy = 0
if stress_level > 100:
    stress_level = 100
if stress_level < 0:
    stress_level = 0
if knowledge < 0:
    knowledge = 0
if knowledge > 100:
    knowledge = 100
