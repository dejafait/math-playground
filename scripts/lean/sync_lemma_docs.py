"""Keep lemma documentation sections and embedded validated sources consistent.

Run from the repository root. This script never marks a proof as validated;
validation status must be set only after a successful Lake build and axiom audit.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SECTIONS = ["Hypotheses.", "Conclusion.", "Proof.", "Mathlib.",
            "Lean proof status.", "Lean proof command.", "Lean proof code."]


def normalize(path):
    text = path.read_text()
    for old in ["Hypotheses and construction.", "Hypotheses and definitions.",
                "Definitions and construction."]:
        text = text.replace(f"**{old}**", "**Hypotheses.**", 1)
    text = text.replace("**Proof/certificate.**", "**Proof.**", 1)
    if "**Proof.**" not in text:
        text, count = re.subn(r"^## (?:Proof[^\n]*|Uniform expansions and proof)\n",
                             "**Proof.**\n", text, count=1, flags=re.M)
        if count != 1:
            raise ValueError(f"Cannot locate proof: {path}")
    if path.name.startswith("C032a") and "**Hypotheses.**" not in text:
        text = text.replace("For the actual Ξ nodes β_j=α_j^{-2}, RH holds",
            "**Hypotheses.** The actual Ξ nodes β_j=α_j^{-2} and power sums S_k are as in Lemmas 24–25.\n\n"
            "**Conclusion.** RH holds", 1)
    if "**Hypotheses.**" not in text:
        text = text.replace("**Construction.**", "**Hypotheses.**", 1)
    # Preserve supplemental mathematical material as subsections.
    text = text.replace("**Construction.**", "### Construction\n")
    text = text.replace("**Unresolved requirement.**", "### Unresolved requirement\n")
    if "**Mathlib.**" not in text:
        text = text.rstrip() + "\n\n" + """**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
"""
    # A validated proof's documentation must embed its exact source file.
    ident = path.name.split("-", 1)[0]
    source = ROOT / "scripts" / "lean" / "Rh" / f"{ident}.lean"
    if "```lean\n" in text:
        if not source.exists():
            raise ValueError(f"Missing Lean source: {source}")
        before, code = text.split("```lean\n", 1)
        _, after = code.split("```", 1)
        text = before + "```lean\n" + source.read_text().rstrip() + "\n```" + after
    actual = [s for s in re.findall(r"^\*\*([^*]+)\*\*", text, re.M) if s in SECTIONS]
    if actual != SECTIONS:
        raise ValueError(f"Unexpected section order in {path}: {actual}")
    if text != path.read_text():
        path.write_text(text)


if __name__ == "__main__":
    paths = sorted((ROOT / "lemmas").glob("*.md"))
    for path in paths:
        normalize(path)
    print(f"Checked common section order and synchronized proof code in {len(paths)} files.")
