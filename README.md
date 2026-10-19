# python_study

My personal Python learning repo: a structured, self-paced curriculum plus my own solutions to every exercise I've completed.

## What's in here

- **`python-study-Neo_1/`** — the study program itself: 15 curriculum modules (hello world → variables, strings, collections, control flow, loops, functions, OOP, files and exceptions, testing, standard library, pip/venvs, APIs with requests, final project), 100 piscine-style practice questions, a quest system, `ROADMAP.md` and `PROGRESS.md` to track where I am, and curated resources. Sources: the Net Ninja Python playlist and Python Crash Course (3rd ed.).
- **`answers/`** — my worked solutions as I progress: exercise folders, a number-guessing game (loops + conditionals practice) and a to-do manager (first small CLI app), plus `answers.txt` notes.

## How it's used

Work module by module in `python-study-Neo_1/curriculum/`: read the exercise file, solve it, and store the solution in `answers/` with the exercise number. `PROGRESS.md` records completed modules; `ROADMAP.md` is the plan ahead.

Everything runs on the standard library only unless a module says otherwise — it's plain `python3 file.py`.

## Curriculum → answers map

| Curriculum module | Concepts | My answer |
|---|---|---|
| `03_strings` | string indexing and slicing | exercises 4-5 warm-ups in `answers/` |
| `04_lists_tuples` | `append`, `insert`, indexing | `answers/exercise4/answer.py` |
| `05_dictionaries_sets` | keys, values, lookups | `answers/exercise6/answer.py` |
| `07_loops` | `while` and `for` in practice | `answers/exercise7/answer.py` + `answers/guess-game.py` |
| `08_functions` | functions as verbs over list storage | `answers/to-do manager.py` |

Run any of them with the answers runner: `python answers/run_exercise.py <key>`
(`list` shows everything).
