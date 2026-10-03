# 2026-10-03 — Quantitative modulo-27 stopping calculation

The ready SPECIALIZE assessment is
[the saved exact-target review](literature/2026-10-03-mod27-effective-hitting.md).
This is one mathematical attempt on that target. The main gap remains
universal eventual descent. A logarithmic bound for reaching residue 20
or {1,2} could control excursions before a later induced-return analysis;
termination after repeated target visits is an independent missing step.

Reused the previously inspected public certificate, without another
literature search: [Sodelin, section 2](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/sources/Sufficiency_Rank_Audit_2026-09-05.md)
and [its residue checker](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/verification/mod27_rank_check.py).
The modular table and rank are reproduction. Quantitative constants are
the assessed specialization, with no originality claim. The live source
provenance qualifications in the prior assessment remain in force.

## Working checkpoint before exact verification

Stop at S={n>0:n=20 modulo 27} union {1,2}. The fifteen core residues
have h-values 0,1,2 and weights 16,28,49. Each internal core step is
expected to satisfy Q(T(n)) <= (20/21)Q(n) for n>=3, keeping +1.
Every positive nonterminal core integer is at least 4, so Q>=64.

For a start n>=3, the initial divisible-by-3 phase takes at most
log(n)/log(2)+1 steps and leaves at height m<=5n/3. Thus initial core
weight is at most 245n/3. If r internal core edges precede the exit,
r <= log((245/192)n)/log(21/20); the exit costs one further step.
The core exit height should be at most 1225n/144<9n. Direct entry
to residue 13 or 26 also has height at most 9n.

At residue 26, e=v_2(y+1) odd self-loops are followed by an even step
to residue 13 and one further step to residue 20. The tail costs e+2,
at most log(10n)/log(2)+2. This gives a provisional bound

    (2/log(2)+1/log(21/20))*log(n)
    + 4+log(245/192)/log(21/20)+log(10)/log(2).

The proposed simpler constants are A=24, B=14, M=2. Verification must
check every residue/parity edge, positive phase guards, all +1 terms,
exit lengths, and ceiling/off-by-one issues. No finite regression can
replace the all-integer inequalities. Continue only if these checks
validate the target; retain an exact failure if they do not.

Attempts 001/003 prohibit a bound independent of n, not this target.
The paired batch remains parked. No complete Collatz candidate exists.

## Completed result and decision

The provisional calculation survived the exact checks. The full informal
proof is [L013](../lemmas/L013-explicit-mod27-hitting-time.md), establishing
the exact assessed hitting-time target with A=24, B=14, M=2. Core
termination is proved by its contracting positive weight, not by assuming
Collatz. Residue-26 exit takes exactly v_2(y+1)+2 steps. Both phase-entry
heights and both arithmetic exit steps are included. Natural logarithms
and shortcut time are retained throughout.

`python3 scripts/mod27-hitting/check_hitting.py` passed: 15 core residues,
25 internal edges, five exits, all-integer coefficient inequalities with
+1, 20,000 first-hit regressions, and prescribed arithmetic loops through
1024 odd steps. The saved
[result](../scripts/mod27-hitting/result.json) is corroboration, not an
infinite-range inference. The required constants were obtained; no
weaker density or fixed-depth statement is substituted for them.

Outcome: ADVANCE toward a quantitative normalization input, classified
POTENTIALLY_NEW only because the exact time bound is outside the inspected
statements. The table and stopped rank are reproduced from the cited
source; the effective constants are an elementary specialization. This
classification does not certify originality. Full Mathlib coverage and
supporting library coverage are not checked.

The main gap is still a terminating mechanism for repeated target visits.
The rank is zero at a target visit and cannot be restarted as a decreasing
global rank. Checking strict decrease at the first subsequent hit is a
concrete test of the most direct possible bridge; it is outside the
previous review's scope and needs its own assessment. No return word has
been computed in this step. No Collatz candidate or counterexample has
appeared. Exhausted routes and existing unfinished work are preserved.
