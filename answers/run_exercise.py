"""Run any solved exercise or game from the answers folder.

Usage:
    python answers/run_exercise.py list      # show what's runnable
    python answers/run_exercise.py 4        # run exercise 4's answer
    python answers/run_exercise.py guess     # run the number guessing game
    python answers/run_exercise.py todo      # run the to-do manager
"""
import runpy
import sys
from pathlib import Path

ANSWERS = Path(__file__).parent

RUNNABLE = {
    "4": "exercise4/answer.py",
    "5": "exercise5/answer.py",
    "6": "exercise6/answer.py",
    "7": "exercise7/answer.py",
    "guess": "guess-game.py",
    "todo": "to-do manager.py",
}


def main():
    choice = sys.argv[1] if len(sys.argv) > 1 else ""

    if choice in ("", "list"):
        print("Runnable answers:")
        for key, path in RUNNABLE.items():
            marker = "x" if (ANSWERS / path).exists() else " "
            print(f"  [{marker}] {key:>5}  ->  answers/{path}")
        return

    if choice not in RUNNABLE:
        print(f"Unknown exercise: {choice!r}")
        print("Run with 'list' to see what's available.")
        return

    path = ANSWERS / RUNNABLE[choice]
    if not path.exists():
        print(f"answers/{RUNNABLE[choice]} does not exist yet")
        return

    runpy.run_path(str(path), run_name="__main__")


if __name__ == "__main__":
    main()
