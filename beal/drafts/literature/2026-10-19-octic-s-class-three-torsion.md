# Octic S-class three-torsion — algorithm coverage, execution parked

TARGET: Compute the S-class three-torsion Cl(O_K[1/165])[3] for L098's degree-eight field with an unconditional certificate.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused 2026-10-16-localized-two-class-kernel-computation.md for the general certification/localization interface; searched the exact octic coefficient strings, S-class three-torsion, bnfcertify/bnfsunit and Magma proof modes; no inspected source supplies this field's unconditional localized class value.
SOURCE_EVIDENCE: PARI stable General number fields catalogue, named entries and sections below; PARI bnfunits.c implementation lines 130–165 and 203–222; Belabas 16 September 2011 primary clarification; Magma Ideal Class Groups handbook ClassGroup and MinkowskiBound entries; retrieved 19 October 2026.
COMPARISON: Known algorithms cover maximal-order certification, full ordinary class certification and localization for a general number field; they supply no octic output or bounded successful execution here. The existing degree-36 assessment's methods are reusable, but its field-specific data are not inputs for K.
GAP: No certified maximal basis, complete ordinary/localized class output, executable checked class backend or demonstrated resource bound is available for this octic; no three-torsion value has been computed.
REASON: Method coverage is ready for a future specialization, but the required executable bounded continuation test fails. Park execution until an actual backend and bounded certification plan, or independently checkable complete data, exist; move to an independent target.
SCOPE: Exactly TARGET for L098's maximal ring and every prime above 3,5,11; no class representatives, norm-fiber survival, fifth-power compatibility, integer elimination or other algebra factors are approved.
LITERATURE_REASON: The saved REVIEW_REQUIRED target lacks an assessed unconditional certification path; compare the exact guarantees and reuse the earlier general class-algorithm review before execution.

## Gap, intended use and decision test

The main gap remains integer elimination in both complete L095 systems,
and independently the other algebra factors and residual signatures.
Audited L097 and L098 fix the degree-eight field K=Q[X]/(H(X,1)),
theta its original generator and S all maximal-ring primes over 3,5,11.
L098's cited Cremona–Lingham Section 2 Kummer sequence explains the
intermediate target: zero localized three-torsion would justify S-unit
exhaustion; a nonzero group requires its nonunit contribution. Neither
outcome solves the simultaneous fifth-power conditions or integer lifting.
No new mathematical specialization or lemma is proved in this review.

Continue only with an executable bounded plan whose successful output
certifies the whole requested group unconditionally. A timeout or a
conditional class report is an incomplete computation, never torsion
vanishing. No such executable plan is available in this environment.
This is an execution park, not an inaccessible-source finding, theorem
against feasibility or ban on future class arithmetic.

## Primary guarantees and exact comparison

[PARI stable catalogue](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html),
accessed 2026-10-19, no fixed release identifier displayed. Inspected
“Class group, units, and the GRH” and the complete relevant entries:

- `nfinit`: nonmonic input triggers integral-model conversion and returns its generator change; retain it for theta.
- `nfcertify(nf)=[]`: certifies the maximal basis and field discriminant; a nonempty vector is insufficient.
- `bnfinit(P,1)`: keeps exact compact algebraic data, but does not remove GRH.
- `bnfcertify(bnf,0)=1`: certifies the full class/unit data; fundamental units are required. Flag one only certifies a quotient.
- `idealprimedec(nf,p)`: returns all primes; omit the residue-degree filter.
- `bnfisprincipal`: returns class coordinates and a principal factor, permitting exact ideal-identity replay.
- `bnfsunit(bnf,S)[5]`: contains S-class order, cyclic factors and ideal representatives.

Use these entries as software specifications, not a claim that a run
occurred. The exact input polynomial is the full L098 h, not its
nonintegral generator treated as a monic integral power-order model.

[PARI primary implementation](https://pari.math.u-bordeaux.fr/lcov-report/basemath/bnfunits.c.gcov.html),
`bnfsunit_i`, source lines 130–165, and `bnfsunit`, lines 203–222:
the implementation forms a relation matrix from all S-prime class
coordinates together with the ordinary cyclic relations, takes HNF,
then obtains the quotient's invariant factors by SNF. This confirms
localization of the entire class group before taking three-torsion;
it is not substitution of ordinary three-torsion. The inspected live
coverage rendering has no pinned commit; a future run must retain its
actual version. No complete code audit is claimed.

[Karim Belabas, “Re: class group without units or grh”](https://pari.math.u-bordeaux.fr/archives/pari-users-1109/msg00003.html),
16 September 2011, complete substantive message read: successful full
initialization and certification give unconditional correctness, barring
implementation bugs; termination of these routines is not guaranteed.
This is a historical implementer clarification, consistent with the live
catalogue's failure warning, not a field-specific runtime prediction.

[Magma Ideal Class Groups handbook](https://docs.magma-maths.org/GlobalFields/NumberFieldsAndOrders/ideal-class-group.html),
`ClassGroup` and `MinkowskiBound`, retrieved 2026-10-19: the map supports
both ideal representatives and class coordinates. Default rigorous
verification checks primes through the Minkowski bound and may be
impractical. `Proof := "Full"` uses the current global bounds, so a prior
`SetClassGroupBounds("GRH")` makes even that call conditional.
`Proof := "GRH"`, `"Bound"` and `"Subgroup"` do not by themselves meet
this target. A future Magma certificate must record explicit unconditional
bound settings, a maximal order and the entire supported-prime list.
No Magma maximal-order algorithm or executable is imported by this review.

## Required future artifact; no certificate obtained

Preserve the input h, exact field-model maps both ways, maximal basis,
field discriminant and full certification result; preserve the complete
ordinary class presentation and full certification success, then all
S-prime ideals, their class coordinates and localized invariant factors.
Require exact ideal arithmetic for relation replay, complete prime
products and total local degrees eight at each of 3,5,11, and explicit
three-torsion generators or a documented complete zero result. Relations
within an uncertified class presentation do not establish completeness.
The polynomial discriminant of L098 is not a substitute for maximality.
No such output, resource estimate based on a certified model, or
independent completeness certificate was obtained here.

The notebook-local bounded availability check found no `gp`, `sage` or
`magma` on PATH, neither Python `cypari2` nor `sage`, and no GP/Sage
executable in /opt/homebrew/bin or /usr/local/bin. This repeats an
implementation prerequisite already recorded in ATTEMPTS/026 and 037;
it is not mathematical negative evidence or evidence of global software
absence. Do not repeat these probes as a research step. No software was
installed and no class arithmetic ran. Reopening needs an actual backend
plus a bounded unconditional plan, or complete externally supplied data.
ATTEMPTS/043–044 concern different mechanisms and remain unchanged.

Exact-coefficient searches used `"1215" "1782" "2970" "class group"`
and `"55+165" "594" "1100" octic`; terminology searches used
`"S-class group" "bnfcertify" three torsion` and official PARI/Magma
certification queries. No matching field result was inspected. Search
silence does not certify novelty, absence of a published computation or
class triviality. Generic cubic-Kummer class-rank leads do not provide
hypotheses for this degree-eight field and were not imported.

## Scope preserved and independent continuation

The ready decision records algorithm coverage, not authorization to
repeat a blocked execution. Both L095 systems remain unsolved; the
norm fibers [75] and [15], fifth powers, integer lifting and other factors
remain open. Mathlib coverage is not checked.

A materially different independently testable proposal is primitive
three-adic realization of both complete L095 systems, with C a unit
and the simultaneous fifth-power equations retained. This needs no class
backend and is distinct from the stopped eleven-adic exclusion or direct
rational factorization. L095 and L096 identify the equations and prior
local scope; no three-adic result is derived or approved now. Its separate
assessment is REVIEW_REQUIRED. Putz's coefficient-specific three-adic
tables are an unread applicability lead for that assessment, not an
import for coefficient one.

The primary target formulation was rechecked on 2026-10-19 at
[Mauldin's primary page](https://sites.math.unt.edu/~mauldin/beal.html):
positive integer bases and exponents greater than two, with a prime
common to all three bases. The nominated AMS page failed retrieval;
its current contents and prize rules are not claimed read. No target
or proof assembly changed.
