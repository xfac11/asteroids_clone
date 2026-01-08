from scoresystem import ScoreSystem
from scoreui import ScoreUI
def make_text_red(text):
    return f"\033[91m{text}\033[0m"

def make_text_green(text):
    return f"\033[92m{text}\033[0m"

def main():
    score_system = ScoreSystem()
    score_ui = ScoreUI(score_system)

    score_system.add(5)
    score_system.add(10)
    if score_system.get_score() != 15:
        print(make_text_red(f"Expected score to be 15 but was: {score_system.get_score()}"))
        print(make_text_red("Test Failed"))
    else:
        print("\033[92mTest Pass!")

    try:
        score_system.add("5")
    except TypeError:
        print(make_text_green(f"Tried to add the string 5 but failed with TypeError as expected"))
        print(make_text_green("Test Pass!"))
    except ValueError:
        print(f"Tried to add the string 5 but failed with ValueError as not expected")
        print("Test Failed")
    except Exception as e:
        print(f"Tried to add the string 5 but failed with some other error.")
        print(f"Test Failed")

    try:
        score_system.remove(-5)
    except ValueError:
        print("Tried to remove -5 and failed with ValueError as expected.")
        print("Test Pass!")
    except Exception as e:
        print(f"Tried to remove -5 and failed with: {e}")
        print("Test Failed")



main()
