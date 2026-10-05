import html
import re
from pathlib import Path

import markdown

ROOT = Path("/home/milosz/priv/Mieszko_homework/computing/bash-course")
OUT = ROOT / "bash-course.html"

LESSONS = [
    ("01-meet-the-terminal", "echo · date · whoami · history"),
    ("02-finding-your-way", "pwd · ls · cd"),
    ("03-files-and-folders", "mkdir · cp · mv · rm"),
    ("04-reading-and-writing", "cat · less · head · nano"),
    ("05-getting-help", "man · --help · apropos"),
    ("06-searching", "grep · find"),
    ("07-pipes-and-redirection", "> · | · sort · uniq"),
    ("08-permissions-and-programs", "chmod · sudo · apt"),
    ("09-first-scripts", "#!/bin/bash · $var · read"),
    ("10-decisions-and-loops", "if · for · while"),
    ("11-final-project", "everything"),
]

SCRIPTS = {
    9: ["about_me", "age", "calc", "backup", "dice", "report"],
    10: ["password", "times", "fizzbuzz", "sort_files", "dice_game", "check", "guess"],
    11: ["diary"],
}

KEYS = {"Ctrl", "Alt", "Shift", "Tab", "Enter", "Space", "↑", "↓", "Page Up", "Page Down", "Tab Tab"}


def md(text):
    out = markdown.markdown(text, extensions=["fenced_code", "tables", "sane_lists"])
    return polish(out)


def polish(h):
    h = h.replace("\\|", "|")  # escaped pipes from markdown tables
    # key combinations: `Ctrl` + `C` -> <kbd>
    def combo(m):
        return re.sub(r"<code>([^<]{1,12})</code>", r"<kbd>\1</kbd>", m.group(0))
    h = re.sub(r"(?:<code>[^<]{1,12}</code>\s*\+\s*)+<code>[^<]{1,12}</code>", combo, h)
    for k in KEYS:
        h = h.replace(f"<code>{html.escape(k)}</code>", f"<kbd>{html.escape(k)}</kbd>")
    # code blocks: add a header bar with a label and copy button
    def block(m):
        lang = m.group(1) or ""
        label = "terminal" if lang == "bash" else "output"
        return (f'<div class="code"><div class="code-bar"><span>{label}</span>'
                f'<button type="button" class="copy">Copy</button></div><pre><code>')
    h = re.sub(r'<pre><code(?: class="language-(\w+)")?>', block, h)
    h = h.replace("</code></pre>", "</code></pre></div>")
    # tables scroll on their own on narrow screens
    h = h.replace("<table>", '<div class="table"><table>').replace("</table>", "</table></div>")
    # checklist items
    h = h.replace("<li>[ ] ", '<li class="task"><input type="checkbox" aria-label="done"> ')
    if "```" in h:
        raise SystemExit("unrendered fence left in output")
    return h


def split_solutions():
    parts = {}
    for f in sorted((ROOT / "solutions").glob("lessons-*.md")):
        text = f.read_text()
        for chunk in re.split(r"^## ", text, flags=re.M)[1:]:
            title, body = chunk.split("\n", 1)
            m = re.match(r"Lesson (\d+)", title)
            n = int(m.group(1)) if m else 11
            body = re.sub(r"\[([^\]]+)\]\((?:scripts/)?[^)]+\)", r"\1", body)
            body = body.replace("in the `scripts/` folder", "below")
            parts[n] = body
    return parts


def fix_list_fences(text):
    # python-markdown can't nest fenced code in list items; pull it out of the list
    return re.sub(r"\n(\d+)\. ```bash\n    (.*?)\n    ```\n",
                  lambda m: f"\n{m.group(1)}. Command:\n\n```bash\n{m.group(2)}\n```\n\n",
                  text, flags=re.S)


solutions = split_solutions()
sections = []
nav = []
for i, (slug, cmds) in enumerate(LESSONS, start=1):
    text = (ROOT / "lessons" / f"{slug}.md").read_text()
    first, body = text.split("\n", 1)
    title = re.sub(r"^# (Lesson \d+: )?", "", first).strip()
    is_project = i == 11
    sid = "project" if is_project else f"lesson-{i}"
    eyebrow = "Final project" if is_project else f"Lesson {i} of 10"
    content = md(body)
    answers = md(fix_list_fences(solutions.get(i, "")))
    for name in SCRIPTS.get(i, []):
        src = (ROOT / "solutions" / "scripts" / f"{name}.sh").read_text()
        answers += (f"<h4>{name}.sh</h4>" + md(f"```bash\n{src}```"))
    nav.append((sid, ("★" if is_project else f"{i:02d}"), title, cmds))
    sections.append(f"""
<section class="view" id="{sid}" data-title="{html.escape(title)}" hidden>
  <header class="lesson-head">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{html.escape(title)}</h1>
    <p class="prompt"><span class="ps1">learner@ubuntu:~/playground$</span> {html.escape(cmds)}</p>
  </header>
  <div class="prose">{content}</div>
  <details class="answers">
    <summary>Show the answers</summary>
    <div class="prose">{answers}</div>
  </details>
  <div class="lesson-foot">
    <label class="done"><input type="checkbox" class="done-box" id="done-{sid}" data-id="{sid}"> I finished this {'project' if is_project else 'lesson'}</label>
    <nav class="pager"></nav>
  </div>
</section>""")

cheat = (ROOT / "cheatsheet.md").read_text().split("\n", 1)[1]
setup_script = (ROOT / "practice" / "setup-playground.sh").read_text()

home = f"""
<section class="view" id="home" data-title="Start here">
  <header class="hero">
    <p class="eyebrow">A course for complete beginners · Ubuntu Linux</p>
    <h1>Bash, one command at a time</h1>
    <p class="lede">Ten lessons and a final project that take you from never having opened a terminal
    to writing your own Bash scripts. Each lesson takes about 45–60 minutes.</p>
    <p class="hero-actions"><a class="btn" href="#lesson-1">Start lesson 1</a> <a class="btn ghost" href="#setup">Set up the practice folder</a></p>
  </header>
  <div class="prose">
    <h2>What you will be able to do</h2>
    <ul>
      <li>open a terminal and move around the file system without a mouse</li>
      <li>create, copy, move, rename and delete files and folders</li>
      <li>read and edit text files from the terminal</li>
      <li>find files and search for words inside them</li>
      <li>combine small commands into powerful ones with pipes</li>
      <li>install programs and understand file permissions</li>
      <li>write small Bash scripts with variables, questions, decisions and loops</li>
    </ul>
    <h2>The lessons</h2>
  </div>
  <ol class="toc">{''.join(f'<li><a href="#{sid}"><span class="num">{num}</span><span class="t">{html.escape(t)}</span><span class="c">{html.escape(c)}</span><span class="tick" data-id="{sid}" aria-hidden="true"></span></a></li>' for sid, num, t, c in nav)}</ol>
  <div class="prose">
    <h2>How each lesson works</h2>
    <div class="table"><table>
      <tr><th>Part</th><th>What happens</th></tr>
      <tr><td><strong>Goals</strong></td><td>What you will be able to do after the lesson</td></tr>
      <tr><td><strong>Learn</strong></td><td>Short explanations, each followed by commands to type</td></tr>
      <tr><td><strong>Try it</strong></td><td>Small tasks to do straight away</td></tr>
      <tr><td><strong>Exercises</strong></td><td>Practice tasks, with answers folded away at the end of the lesson</td></tr>
      <tr><td><strong>Quiz</strong></td><td>Quick questions to check understanding</td></tr>
      <tr><td><strong>Recap</strong></td><td>The lesson's commands in one table</td></tr>
    </table></div>
    <h2>Tips for the learner</h2>
    <ul>
      <li><strong>Type every command yourself.</strong> Don't copy and paste the lesson commands: typing is how your fingers and memory learn. (The copy buttons are for the teacher and for long scripts.)</li>
      <li><strong>You cannot break the computer</strong> by working inside <code>~/playground</code>. Experiment!</li>
      <li>When stuck, press <kbd>Ctrl</kbd> + <kbd>C</kbd>. It stops whatever is running.</li>
      <li>Error messages are not failures. Read them: they usually say exactly what is wrong.</li>
      <li>Use the <kbd>Tab</kbd> key. It finishes names for you.</li>
      <li>Uppercase and lowercase are different: <code>Story.txt</code> and <code>story.txt</code> are two different files.</li>
    </ul>
  </div>
</section>

<section class="view" id="setup" data-title="Setup" hidden>
  <header class="lesson-head">
    <p class="eyebrow">Before lesson 1 · for the teacher</p>
    <h1>Set up the practice folder</h1>
    <p class="prompt"><span class="ps1">teacher@ubuntu:~$</span> bash setup-playground.sh</p>
  </header>
  <div class="prose">
    <p>The exercises use a practice folder called <code>~/playground</code>, full of files made for the course:
    a treasure hunt, a messy folder to tidy, a story, a server log, lists and a scores table.
    The script below creates it and touches nothing else.</p>
    <ol>
      <li>Use a computer with Ubuntu (any recent desktop version).</li>
      <li>Open a terminal with <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd>.</li>
      <li>Open a new file in the nano editor:
      {md("```bash\nnano setup-playground.sh\n```")}</li>
      <li>Press <strong>Copy</strong> on the script below, then paste it into nano with <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>.</li>
      <li>Save with <kbd>Ctrl</kbd> + <kbd>O</kbd>, <kbd>Enter</kbd>, and exit with <kbd>Ctrl</kbd> + <kbd>X</kbd>.</li>
      <li>Run it:
      {md("```bash\nbash setup-playground.sh\n```")}</li>
    </ol>
    <p>If the playground gets messed up, get a fresh copy at any time with:</p>
    {md("```bash\nbash setup-playground.sh --reset\n```")}
    <p>Lesson 8 installs a few small programs with <code>sudo apt install</code>, so the learner needs
    the computer's password or a teacher sitting next to them for that lesson.</p>
    <h2>setup-playground.sh</h2>
    {md("```bash\n" + setup_script + "```")}
  </div>
</section>

<section class="view" id="cheatsheet" data-title="Cheat sheet" hidden>
  <header class="lesson-head">
    <p class="eyebrow">Every command from the course</p>
    <h1>Cheat sheet</h1>
    <p class="prompt"><span class="ps1">learner@ubuntu:~$</span> man bash</p>
  </header>
  <div class="prose cheat">{md(cheat)}</div>
</section>
"""

page = (Path(__file__).parent / "template.html").read_text()
page = page.replace("{{NAV}}", "".join(
    f'<li><a href="#{sid}" data-id="{sid}"><span class="num">{num}</span><span class="t">{html.escape(t)}</span><span class="tick" data-id="{sid}" aria-hidden="true"></span></a></li>'
    for sid, num, t, c in nav))
page = page.replace("{{SECTIONS}}", home + "".join(sections))
OUT.write_text(page)
print(OUT, len(page))
