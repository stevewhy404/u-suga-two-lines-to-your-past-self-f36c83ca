import os

LINE_1 = "Don't send the text you typed at 2 a.m. on the kitchen floor telling Maya 'I think we should stop seeing each other'."
LINE_2 = "You will spend the next year learning the doubt was only exhaustion, and no apology ever unsends a sentence she believed."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE_1 + "\n" + LINE_2 + "\n")
