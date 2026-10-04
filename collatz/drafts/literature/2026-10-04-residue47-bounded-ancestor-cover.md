# Bounded residue-47 ancestor cover: sourced obstruction and covered continuation

TARGET: Test whether shortcut inverse words of length at most 12 cover all roots n=47+243k, k>=0, outside an explicit finite base set by positive residue-20 ancestors strictly below the original root, retaining every integer and parity guard.
CHECKED: 2026-10-04
DECISION: IMPORT
SEARCH_EVIDENCE: Eleven exact-statement, terminology, stronger-result and continuation queries were executed on 2026-10-04; the directly matching obstruction and relevant variable-duration continuation were read, with queries and reuse limits below.
SOURCE_EVIDENCE: Read Sodelin, Bounded_Ancestor_Depth_Obstruction.md, node B-S20-ANCESTOR-DEPTH-OBSTRUCTION-001, exact statement and proof, web lines 8–41 and scope lines 42–74, https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/Bounded_Ancestor_Depth_Obstruction.md; read the continuation statements and proofs in Finite_Growing_First_Return_Spells.md and Postspell_Guarded_Root_Descent.md, and the failed-guard comparison in Postspell_Odd_Run_Obstruction.md, with exact sections below.
COMPARISON: The inspected theorem directly refutes the requested bounded cover, including its finite-base allowance; no word enumeration or new obstruction proof is needed. A separate inspected guarded forward theorem permits unbounded phase lengths but does not cover its failed-halving complement.
GAP: Universal convergence on the surviving least-root domain remains missing; the bounded ancestor mechanism is stopped, while a conditional restriction from the guarded variable-duration forward theorem is ready for citation application.
REASON: Resolve the saved REVIEW_REQUIRED target without changing it during assessment, import the matching negative result, and select a materially different covered mechanism rather than increase a refuted fixed ancestor-time bound.
SCOPE: Positive shortcut roots n=47+243k, all admissible inverse words of actual time at most 12, ancestors in residue 20 modulo 27 and strict original-root order; the covered continuation uses actual forward words (OOEO)^J O^H and the source's sufficient final-even guard, with unbounded J,H and the same original root.
COVERED_TARGET: Apply by citation the guarded postspell descent theorem to a least nonconvergent residue-20 root with actual prefix (OOEO)^J O^H, J>=2 and H>=3, recording the necessary bound v_2(z)<e(J,H), where z is the prefix endpoint and e(J,H) is the least integer >=J+H congruent to 2 modulo 18, while retaining the final-even guard and original-root comparison.

## Hypotheses

The TARGET is the unchanged action saved by step 025. It addresses an
infinite cylinder surviving L014–L018. A successful cover could exclude
that cylinder from the least bad root after its finite exceptions were
proved convergent; other cylinders would still need separate work.
The length bound was a discovery budget just above the two imported
fixed certificates, rather than an asserted sufficient bound. Use the
shortcut map and fixed least residue-20 root conventions in foundations
and L014.

## Conclusion

This is new NEGATIVE route evidence, classified KNOWN_IMPORTED. The
matching source prevents the proposed cover. No local mathematical
result or nonconvergent positive orbit is derived. The listed
continuation is approved for a separate mathematical turn; its
least-root consequence is not derived here.

## Proof

This section records precise citations and scope comparisons only.

### Exact obstruction

Sodelin, *An unbounded-depth obstruction for residue-20 ancestor covers*,
node `B-S20-ANCESTOR-DEPTH-OBSTRUCTION-001`,
[exact statement and proof, web lines 8–41](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Bounded_Ancestor_Depth_Obstruction.md#exact-positive-integer-statement),
states that, for every L,t>=0, roots r=47+3^(L+3)t admit no positive
m<r in residue 20 modulo 27 with T^b(m)=r and b<=L. The proof checks
every inverse guard by transfer to anchor 47 and compares endpoint order.
The only smaller allowed anchor start, 20, has a forward orbit missing 47.

The source's L=12 case lies in the saved 47-modulo-243 cylinder and is
unbounded as t varies, defeating its finite-base allowance. This is
direct citation applicability, without rebuilding the proof or inverse
trees. The rest of the note was read for scope: unbounded time and
general coalescence remain possible. Its q5-specific statements and
periodic-orbit example are not needed for this rejection.

### Covered variable-duration continuation

Read Sodelin, *Exact termination of every consecutive OOEO first-return
spell*, node `AC-GROWING-FIRST-RETURN-SPELL-001`,
[section 1 with proof, web lines 14–67](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Finite_Growing_First_Return_Spells.md#1-uniform-exact-spell-theorem).
Its count is floor(v_2(11r+23)/4) and terminal q=v_2(r+5) lies in
{0,1,2,3}; the stated states still exceed the original root. Sections
2–6 were read for scope. Ending this spell alone is insufficient.

Read *Guarded root descent after independently unbounded return spells
and odd runs*, node `AC-POSTSPELL-GUARDED-ROOT-DESCENT-001`,
[sections 1–3, web lines 25–151](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md#1-uniform-original-root-margin),
including the margin proof, parity/CRT construction and target-membership
argument. For r>3 following the actual prefix (OOEO)^J O^H, J>=2,H>=3,
section 1 gives 0<z/2^e<r when e>=J+H and 2^e divides z. Section 3
gives target membership for e=2 modulo 18. The source chooses the least
such e; this threshold is sufficient, not asserted optimal.

The covered action uses that theorem with L014's existing minimality
argument. Positive residue-20 roots exceed 3; only actual prefixes are
admitted. Target membership is retained because an arbitrary smaller
integer need not be a smaller member of the induction set. Citation
application and convergence transfer through the shortcut cycle are
deferred to the next mathematical turn.

Read [section 4, web lines 152–179](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md#4-why-the-guard-remains-a-real-open-boundary)
and the supporting
[*Fixed-length return spells can be followed by arbitrarily long further growth*, full statement and proof](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Odd_Run_Obstruction.md#exact-all-parameter-family),
node `AC-POSTSPELL-ODD-RUN-OBSTRUCTION-001`. Fixed spell length and exit
depth do not bound subsequent growth, and infinitely many sources have
too few final halvings. Correct growing phases and endpoint residue
cannot replace the missing guard. Arbitrary-source coverage and later
recharge control remain open in the inspected notes.

### Relevance and discriminating test

The main gap is universal eventual descent or convergence, rather than
arrival at residue 20. The requested bound was a smaller allowed
ancestor within 12 actual steps for every sufficiently large member of
the cylinder. The inspected theorem rejects that threshold. Stop this
cover mechanism, including enlargement to another fixed bound; retain
the obstruction without treating it as a global research stop.

The new intermediate target isolates when a whole forward excursion
can contradict fixed-root minimality despite unbounded growing phases.
Its plausible later use is to focus further work on insufficient final
halvings and later recharge. Continue the citation application only
with actual-word, positive-integer, target-membership and strict
original-root guarantees. A mismatch would reject or narrow it.
The failed-guard complement and other exit classes remain later steps;
no all-root entry into the guarded domain is assumed.

Attempt 011 preserves this stop. Attempts 009 and 010 remain parked or
stopped. This literature step spends no mathematical exploration turn
and resets no historical counter. No lemma, mathematical program or
candidate argument was produced.

### Search, reuse and provenance

Queries executed:

- `Collatz "47" "243" ancestor`
- `Collatz "bounded" "ancestor cover"`
- `site:github.com/Sodelin/Collatz-Conjecture-Work "cover" "12"`
- `Collatz "finite spell" "ancestor"`
- `"Collatz" "47+243"`
- `"Collatz" "47 mod243"`
- `Collatz "bounded ancestor" obstruction ternary cylinder`
- `Collatz "smaller" "ancestor" "bounded" theorem residue`
- `Collatz "Postspell_Guarded_Root_Descent"`
- `Collatz "OOEO" "J+H" descent`
- `Collatz "bounded ancestor" "47"`

Direct links in Complementary_Ancestor_Cylinders.md led to the exact
obstruction; search snippets were not treated as coverage. Reuse the
adequate published inverse-word arithmetic and retained-branch coverage
in the [residual-selector assessment](2026-10-03-residue20-residual-ancestor-selector.md)
and [complementary assessment](2026-10-04-complementary-valuation-three-ancestors.md).
The general inverse-word note, sections 1–5, was inspected for guard and
forward-orientation consistency. It supplies supporting semantics,
rather than the full obstruction or guarded forward theorem.

A bilateral-reduction lead was previewed only at its introduction and
odd-only map conventions:
[KokunoYumeto/collatz-workbench note dated 2026-09-16](https://github.com/KokunoYumeto/collatz-workbench/blob/main/collatz_reconstruction/research_program/bilateral_root_bounds_20260916/note.md).
Its full theorem proofs were not assessed and no result is imported.
Other claimed general resolutions were discovery hits only. Source
overlap does not establish originality or an exhaustive literature census.

The Sodelin notes were read from live main on 2026-10-04; their node
identifiers above specify the inspected statements. The obstruction,
spell, guarded-descent and odd-run notes have 145, 153, 199 and 132 web
lines respectively. Immutable commit metadata was inaccessible through
the browser; no commit hash was obtained. The theorem bodies and
essential proofs are accessible, so there is no source blocker. Their
complete Lean formalizations are pending; no local Lean audit or
external checker run was performed.

The [primary target page](https://mathprize.net/posts/collatz-conjecture/),
dated 2021-07-07, was rechecked. Its all-positive-integer convergence
statement matches local GOAL.md; prize terms are not inputs.

## Mathlib

Full bounded-ancestor obstruction, guarded postspell descent theorem,
and supporting valuation/congruence/iteration coverage: **not checked**.
No matching declaration or library absence is asserted. External source
proofs and pending Lean work are not Mathlib coverage claims.
