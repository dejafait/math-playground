# Certified maximal-order ideal-lattice witness: narrow park

2026-10-11. The [source review](../drafts/literature/2026-10-11-global-eleven-ideal-lattice-witness.md)
inspected exact ideal interfaces and proposed diagnostic bound B=100.
PARI's qfminim documentation disclaims rigorous error tracking even for
flag 2; the primary Fincke–Pohst paper remained inaccessible. No certified
maximal-order/P1/Q5 data or working exact ideal backend were obtained.
No arithmetic or witness search ran.

WHY IT FAILS: Certified enumeration cannot be justified by qfminim output
alone, and exact ideal verification currently lacks its backend and data.
Candidate generation followed by exact verification could still prove a
positive result; this is not an impossibility theorem. Preserve
[L045](../lemmas/L045-global-eleven-projection-ideal-criterion.md) and
ATTEMPTS/013: finite failure cannot prove class nonvanishing. Reopening
this implementation requires actual certified inputs and rigorous
enumeration coverage or independently checkable positive witnesses.
Do not repeatedly seek the same unavailable computation. The different
power-order certificate interface has a separate REVIEW_REQUIRED
assessment; its algebra and witnesses are unproved.
