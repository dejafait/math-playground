# L095 eleven-adic solvability — source comparison complete

TARGET: Assess 11-adic solvability of both L095 power systems, retaining nonzero coordinates, m a unit and primitive reconstructed bases.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the rational-factor and independent-audit assessments, L095/L093 and history 317/319; searched exact signature/local/Hensel, rational-factor and H-coefficient phrases; no matching theorem deciding these two systems was located in the bounded search.
SOURCE_EVIDENCE: Zábrádi, Notes for the course p-adic methods in arithmetic (29 June 2022), Lemma 2.3, Theorem 2.4 and Corollary 2.5, printed p.4, inspected with their proofs; prior Putz and Pacetti–Villagra Torcomian comparisons reused unchanged; foundations/17-local-power-hensel-inputs.md already records supporting inputs.
COMPARISON: Known Hensel lifting supplies a method, not a solvability verdict for L095; Putz's special-coefficient exclusions and the modular theorem's p=11 exception still prevent importing a global exclusion. L001 concerns the unrestricted equation and does not certify either rational-factor system.
GAP: Need exact nonzero primitive lifts for both systems or a complete obstruction for a system, with all coordinate-valuation cases retained when asserting nonexistence; finite residue survivors do not decide this.
REASON: Essential method coverage is adequate for one bounded local test; no matching system-specific result was found and no novelty is inferred. No essential source is blocked for this scope.
LITERATURE_REASON: The new target is local solvability of the audited systems, beyond the prior rational-root reduction and audit; this review supplies the missing local-method comparison.
SCOPE: Exactly TARGET over Z_11 using audited L095 and the cover definition L093; elementary valuation/residue tests and cited Hensel lifting only, with no global field enumeration or local-to-global inference.

## Gap, target and use

The main gap remains global elimination and integer lifting for ordered
(3,5,11), within the unresolved Beal target. This intermediate target
asks whether eleven alone excludes either rational-factor system.
An obstruction would remove that integer system; exact local witnesses
for both would retire standalone eleven-adic nonexistence. Other
algebra factors, simultaneous global constraints and integer lifting
remain independent gaps. No such local result is established here.

## Sources and theorem comparison

Gergely Zábrádi, *Notes for the course p-adic methods in arithmetic*,
ELTE summer school, 29 June 2022,
[author PDF](https://zabradi.web.elte.hu/Jegyzetek/p-adic-meth-arith.pdf),
printed p.4 (PDF index 3), retrieved 2026-10-18. Lemma 2.3 and
Theorem 2.4 require an integral polynomial and approximate integral
root modulo p^n with one partial derivative of valuation k and
0 <= 2k < n. The latter gives an exact root congruent modulo p^(n-k),
fixing the other coordinates. Its proof iterates the former's Taylor
correction in one variable. Corollary 2.5 decomposes Z_p^* as
mu_(p-1) times (1+p Z_p), by lifting distinct residue roots. These
are method inputs only; their hypotheses must be checked on L095's
actual equations. No reproof is needed.

The already inspected Newton version and unit inputs are canonical in
foundations/17-local-power-hensel-inputs.md. No changed hypothesis
requires rereading Clark. No application, power-surjectivity claim or
new system-specific calculation is made this turn.

Reuse drafts/literature/2026-10-18-ordered-three-five-eleven-rational-factor.md
and its audit assessment for Putz's 2024 thesis, Section 5.2 and
Propositions 5.24–5.27 pp.170–173, and Pacetti–Villagra Torcomian's
Theorems A–C pp.4–5. Their inspected hypotheses remain unchanged:
Putz's terminal exclusions use special coefficients, and the modular
statements except eleven. The local-family code is no global
rational-root solver. No new theorem from those sources is imported.
The unread Dahmen provenance lead remains nonessential to this test.

L095's entire proof and independent audit were read: both H equations,
all denominator cases, and the converses are available. L093's full
cover interface was checked. The two systems have not previously been
decided locally in histories 317/319. L001's proof was inspected as a
mechanism limitation: its unrestricted local witnesses do not impose a
rational factor or these simultaneous powers. Older local-image and
norm-envelope stops concern different algebras; they neither approve
nor ban this test. The new review supplies no duplicate local theorem.

## Bounded discovery and limits

Queries: `"3,5,11" "local" Fermat rational`,
`"55" "165" "594" "1215" cube Fermat`,
`"3t^2+t+1" Fermat 11 rational`, `"11-adic" "3,5,11"`,
`"generalized Fermat" "rational factor" "local"`,
`"3, 5, 11" "Hensel"`, and `"3,5,11" "rational points"`.
Relevant hits returned the already assessed Putz thesis/package;
unrelated hits and snippets supply no theorem evidence. This is a
bounded search, not an exhaustive literature claim. Mathlib coverage
of the exact local systems and supporting declarations is not checked.

## One approved test, not performed

Retain L095's exact Q,H and both substitutions:
I has C=5m+u^5 and H(m,C)=a^3;
II has C=m+5^10 u^5 and H(m,5C)=5^11 a^3.
In each A=ma and B=Q(m,dC)u, with d=1 or 5 respectively.
All variables lie in Z_11, m is a unit, m,u,a,A,B,C are nonzero,
and min(v_11(A),v_11(B),v_11(C))=0. Do not impose unit conditions
at eleven merely from integer restrictions at three or five.

Make one bounded residue/valuation test, then certify any proposed
witness using the cited theorem and the same tuple throughout. Fixing
m,u while lifting a is allowed only after its actual derivative and
error satisfy the theorem. Nonzero coordinates and local primitivity
must be proved for the exact lift, not inferred from an approximate
solution that permits zero. A single exact witness suffices to refute
local emptiness of its system; it need not classify other valuations.
A nonexistence claim must instead cover v_11(C)>0, v_11(u)>0 and
all other feasible valuations without a finite cutoff assumption.

Continue the exclusion route only with an exhaustive obstruction;
retire it for each system with an exact admissible lift. If the bounded
test yields only singular residue survivors, record that limitation
and reassess rather than escalating precision without a lifting test.
No search, residue calculation, witness, lemma or script on this new
mathematical target has been produced in this literature-only step.
