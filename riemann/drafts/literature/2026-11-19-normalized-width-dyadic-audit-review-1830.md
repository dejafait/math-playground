# Once-rounded normalized-width audit: source approval1831

TARGET: Audit C033z1830's once-rounded normalized-width constructor for error<=2^-60, cost<=322 including clamps, exact iterate denominators2^[34*(3^n-1)] and rescaled denominator<=2^223055, including endpoints, equality branches and1802 input perturbation.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused1828 discovery queries/comparison and1829 approval for the unchanged exact-Newton and comparison-halving ingredients. Scoped comparison read C033z hypotheses,1802(14)-(17),1810 conversion precedent,1825 initializer/source application and1830(39)-(42)/ledger/Mathlib; checked ATTEMPTS/2026-11-19-unrounded-gmp-execution-budget-1823.md. No repeated discovery search or novelty inference.
SOURCE_EVIDENCE: Reopened Brent-Zimmermann, Modern Computer Arithmetic v0.5.9,7 October2010, Lemma3.14,printed p112/PDF page128 https://members.loria.fr/PZimmermann/mca/mca-cup-0.5.9.pdf#page=128 and WPI MA3257 Spring2023 lecture23,pp1-2 https://users.wpi.edu/~bgu/sp23/ma3257/lecture_notes/MA3257_L23.pdf ; read the complete Newton statement/Taylor proof and bisection algorithm/theorem/halving proof. Reuse drafts/literature/2026-11-19-normalized-width-source-notes-1828.md for stronger fixed-point nonimports, GMP canonical-form coverage and access qualifications.
COMPARISON: These sources cover exact positive-input Newton error and strict-sign interval halving. Neither supplies1830's fixed64-slot equality convention, odd-grid numerator, exact denominator induction or full288-operation ledger. Those are finite local audit obligations under the previously assessed rational model; no missing general numerical theorem is essential. The construction certificate does not supply an independent audit.
GAP: No essential source gap remains for the exact saved audit. Independent scrutiny/replay of(39)-(42), positivity at every theorem application, conversion endpoints/equalities,1802 perturbation/clamps, every reduced denominator and full cost remain undone. No numerical contract, runtime, global ledger or actual-Xi claim is verified in this source turn.
REASON: Separate scope approval1831 compares the newly written constructor with the already inspected inputs; SPECIALIZE authorizes an application audit, not a reproof of general Newton theory or approval of its finite conclusions. This is source-gate completion without new mathematical evidence.
SCOPE: Supplied rational W in[1,2^30], unchanged rational operation model and true panel flag. One64-slot conversion on[1/4,1], eight exact Newton steps, no new global ledger or runtime/scalar claim.
LITERATURE_REASON: The1830 audit continuation was newly REVIEW_REQUIRED after construction; this turn supplies its separate scope approval using1828/1829 coverage, without reopening discovery for a ready numerical ingredient.

The mathematical audit target is exactly TARGET above. Its canonical proof
is C033z extension1830; exact finite evidence is
scripts/smoothed-law/width_dyadic_1830.json, produced by the corresponding
Python script. Relevant local imports remain C033z1802/1825/1827 and1810's
conversion precedent, C033y's panel map, and downstream C033w/u and
C032s/q/w/j. The prior gate already covered construction; this separate
source review does not perform the independent audit or repeat discovery.

## Primary hypotheses and specialization boundary

The MCA source assumes a,x>0, defines rho=a^(-1/2), and gives the
one-step error estimate for x'=x+(x/2)*(1-a*x^2), with the Taylor
intermediate point between x and rho. Its full proof on printed p112
uses Taylor's theorem for f(t)=a-t^(-2). No radix, rounding or initial
closeness hypothesis occurs in Lemma3.14. This does not grant positivity
of x' for arbitrary positive inputs:1830 must retain1825's invariant
before each subsequent application. Check the converted coefficient and
the initializer rather than transfer a sample result from unrounded W.
Import the general theorem by citation; do not reprove it during the audit.

The WPI theorem on p2 assumes continuity and strictly opposite endpoint
signs. Its first midpoint is p_1; the proof uses nested interval lengths
and half-length error. Its p1 algorithm stops at an exact midpoint root.
The1830 comparison algorithm instead deliberately runs all64 slots, even
at equality. Thus endpoint inputs and equality paths require its explicit
closed-containment argument; they cannot be covered by quoting the strict
sign theorem alone. The placement of the final midpoint, grid membership
and every paid comparison remain local implementation checks. This is an
identified specialization boundary, not a completed new proof here.

Ordinary mean-value error propagation is a standard named input; the audit
must verify its derivative bounds on the entire coefficient and width
segments. The three error contributions, rescaling and projection to the
panel clamp are separate obligations. C033z1830 expressly gives only an
unclamped guarantee for an arbitrary W unless the exact inverse root is in
the selected clamp interval. Do not infer this hypothesis from the flag
alone or preserve1825's stronger error allowance without checking1830.

No inspected theorem certifies the claimed exact powers of two in reduced
denominators or the operation count. Checking a finite specified rational
expression by parity induction and a charged expression ledger needs no
additional numerical source. This permission is limited to auditing the
written induction/ledger, not establishing an uncovered new algorithm.
The GMP canonical-form convention fixes the meaning of denominator only;
it supplies no cost bound. Integer Algorithm3.9/Lemma3.15 and the stronger
fixed-point Theorems4-5 in1828 remain nonimports, with their differing
domains, seeds, iteration rounding and primitives. No full matching
Mathlib theorem was checked; availability remains unknown.

## Audit test and retained failures

Continue with one independent application audit under SPECIALIZE. Require
all original thresholds together: error<=2^-60, cost<=322 including clamps,
the claimed exact iterate denominators and rescaled bound. Include endpoints,
all equality branches,1802 perturbation and every expression in the ledger.
Check complete load-bearing certificate evidence, not a preview or sample
alone; uniform claims require the written proofs. A failing check must
identify the unsupported claim and its consequence, preserving the
constructor and evidence without loosening the thresholds. Passing still
does not certify practical bit cost, runtime, a revised evaluator ledger
or any scalar value. No proof or certificate was replayed in this turn.

The1823 unrounded execution stop remains15/780 profiles,0/8 scalars and
six independently replayed1823b profiles. It concerns an operationally
different evaluator and is not a ban on this independent finite test.
The local1810 rounding precedent and1825/1827 audit are ingredients, not
duplicates proving the1830 changed-coefficient contract. Full-source
correctness and law/divisor/zero-data inputs remain unverified. Retain
divisor/conjugation/multiplicity, excluded ordinate0, strict strip/gamma>14,
counting/real-zero/reciprocal-square tail, heat positivity/separate errors,
both fixed-v1 qualifications, zero drift/killing and Gaussian half-variance.
Conditioning, weights, TV<=2, observations, signed-height cancellation and
actual-Xi realization remain independently open. This numerical scope
supplies no justified new central creative mechanism. No lemma, mathematical
script, PROOF or DAG changes are part of this literature-only approval.
