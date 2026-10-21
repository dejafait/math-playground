# Bounded Sunley error comparison — completed attempt

Approved target: test whether the Sunley counting interval can have
positive endpoints of ratio below two at any 0<X<=10^6 for L96.
Coverage: `literature/2026-10-11-ninety-six-ideal-counting-error-feasibility.md`.
Essential mathematical inputs are L051-L052 and the cited counting and
residue-upper-bound theorems. Prior enumeration and auxiliary-relation
stops are contrasts, not premises. Existing unfinished work is preserved.

The saved reasoning was completed in
[L057](../lemmas/L057-ninety-six-sunley-interval-obstruction.md), which
contains the full proof, citations and qualifications. Its certificate
is `../scripts/ninety-six-analytic-error/counting-error-certificate.json`.
The integer premises have zero failures. Uniformly E/U>10^506 versus
the necessary E/U<1/2. This informative NEGATIVE parks the raw Sunley
interval implementation at X<=10^6, without measuring actual error or
taking an ideal count. It specializes known bounds without claiming
originality. All class/unit completeness and disk emptiness obligations
remain unresolved. Separate audit coverage is proposed, not approved.
