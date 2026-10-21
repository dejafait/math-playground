# Conductor-eleven quadratic enclosure — separate scope approval

TARGET: Produce a finite L027 quadratic-coefficient enclosure for E=[0,-1,1,-10,-20] at p=7 using audited L041 symbols and C=0, certifying ordinarity, Teichmuller residues and unit-root precision, testing n=2,3,4 with M=n+1 and stopping at the first strict bound min(n-1,M)>v_7(b).
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact queries and inspected coverage from the primitive-error, finite-error and conductor-389 coefficient assessments; searched named conductor-eleven assessments/history and ATTEMPTS/023--024; compared L027, L033, L039/L041 and the old coefficient/new calibration interfaces. No new-model coefficient certificate was found in these targeted records; no novelty claim.
SOURCE_EVIDENCE: Reopened Stein--Wuthrich, Math. Comp. 82 (2013), Section 3 pp.1762--1765, Propositions 3.1/3.5, Corollary 3.3 and essential proofs plus multiplier definition; reopened Conrad, Hensel's Lemma, Theorem 4.1 printed p.6, undated live PDF, on 2026-10-10. Reused earlier ordinary-case and normalization assessment; precise links and comparison below.
COMPARISON: The known ordinary finite-polynomial method and canonical L027 cover the unchanged enclosure without lower-coefficient vanishing. Audited L039/L040/L041 supply this model's lattice, exact total-period normalization and all-level C=0; old conductor-389 software constants and numeric evidence do not transfer.
GAP: Good ordinarity at seven, finite residues/root residuals, every coefficient-stage path and exact b with a strict bound remain uncomputed; no source guarantees success at n=2,3,4. Independent L026 premises and general BSD gaps remain missing.
REASON: Separate comparison now covers the changed model and general-adapter contract. SPECIALIZE permits one bounded known-method implementation with independent replay, not new theorem derivation or a rank-two inference.
LITERATURE_REASON: The proposed coefficient transfer changes the model, relative lattice ordering/dimension and normalization from the preapproved conductor-389 target; those finite implementation obligations required separate coverage approval.
SCOPE: Only the exact TARGET above, model [0,-1,1,-10,-20], level 11, p=7, primitive untwisted trivial branch, total minimal real Neron period, kappa(gamma)=8, audited L041 F=phi/5 and C=0; n=2,3,4 and M=n+1, with good ordinarity an initial required check and complete independent replay.

The original 2026-10-10 proposal was REVIEW_REQUIRED and supplied no
coefficient arithmetic. This separate literature step approves its exact
unchanged target; it neither performs nor approves previously uncovered
mathematical derivations in the same turn.

Main gap: arbitrary m(E)>=2 still lacks rank E(Q)=m(E). The intermediate
target tests finite coefficient production on a second actual
general-adapter instance. Its plausible use is a certified quadratic
input to the point/coefficient mechanism of L004, or to L026 only when
all additional hypotheses are separately available. Neither central
vanishing nor two points nor complex order two is supplied for this model.

## Primary theorem comparison

[Stein--Wuthrich, publisher offprint, Section 3, pp.1762--1765](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6)
uses non-CM curves, total real periods, odd primes, the untwisted measure
and the 1+p coordinate. Proposition 3.1 is coefficientwise convergence;
Corollary 3.3 gives the adjacent monic divisor; Proposition 3.5 bounds
adjacent coefficient errors using both polynomial denominator bounds.
The relevant proof cases and multiplier definition were inspected.
These statements have no conductor-389 restriction or lower-vanishing
premise. Retain the ordinary interpolation multiplier. Reuse L027's
all-level tail argument, not the source's concluding two-level constant
or Lemma 3.6 wording. No convergence theorem is reproved here.

[Conrad, Theorem 4.1, printed p.6](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6)
requires f in Z_p[X], x in Z_p and |f(x)|_p<|f'(x)|_p^2. It gives the
unique nearby root and exact distance |f(x)/f'(x)|_p. L027 already
specializes this to the unit-root and Teichmuller polynomials. The new
finite residual and derivative checks remain required; the theorem
alone validates no numerical approximation.

## Changed instance and implementation obligations

Essential local inputs are L027, L028, audited L039/L040/L041 and their
complete structural, dual, ratio and calibration evidence and audits.
L039 supplies minimality, Delta=-11^5, conductor 11 and non-CM for the
exact original equation, independently of the adapter's retained
SUPPLIED_CONDITIONAL provenance. L040 retains its published optimality
and external-source qualifications. L041 identifies the full normalized
functional, including all integral generators, and denominator ten.
Its exclusion p!=5 applies at seven, conditional on good ordinarity.
These are prior results imported with their qualifications, not new
source conclusions or finite arithmetic established in this review.

The old scripts/quadratic-seven/build_certificate.py lines 55--121 and
verify_certificate.py lines 114--176 contain conductor-389 constants:
390 generators, dimension 65, its fixed lifts/coset lookup, scale -1,
denominator two and old model point count. They are methodology only.
The conductor-eleven calibration builder lines 38--125 instead reads
presentation.generator_coordinates, cosets.lifts/representatives and
the dual line from the L038-relative-v1 evidence; its sizes are twelve
and three, scale 1/5 and denominator ten. This is an interface comparison,
not an execution or universal correctness assertion. The next implementation
must bind the existing complete inputs and use their actual ordering,
all twelve values and full quotient coordinates. Preserve all prior bytes.

First certify the original curve's reduction and complete point count at
seven including infinity, with a distinct exhaustive replay; report t
and check t is a seven-adic unit before invoking the ordinary formula.
Stop this chosen-prime target if good ordinarity fails. No twist trace
or old coefficient-stage trace may be substituted.

At each scheduled n preserve all six exact Teichmuller residues in the
L027 interval, residue and sixth-power checks and unit derivatives; save
u as an exact rational unit, u=t modulo seven, residual valuation at least
M=n+1 and its derivative check. Use L027 (1)--(2) without rescaling:
least-positive r modulo 7^n for w*8^j, both rational argument families,
every j from zero to 7^(n-1)-1 and every binomial(j,2). Root approximation
must not choose approximate rational symbol arguments. No factors are
removed, and no lower coefficient is assumed zero.

Save every oriented path with ordered endpoints, determinant-one lifts,
Gamma_0(11) membership, raw generator vector, full-relative coordinates
and evaluation by L041. The independent replay must reconstruct all
cosets/paths, compare raw and quotient evaluations, check all finite root
and residue data and recompute the whole rational sum independently of
saved aggregates. Reuse the complete audited input evidence rather than
success flags or hashes as mathematical justification. Report the actual
and required bounds, failed checks and certificate paths. No such
coefficient evidence is produced by this literature step.

## Duplicates, failures and decision test

L033 is an already known-method coefficient certificate for a different
model; its number cannot certify this one. The named conductor-eleven
records stop at calibration. ATTEMPTS/023--024 stop conditional-audit
repetition as input production and preserve the parked uniform-twist
source blocker. Actual audited L039--L041 input data make this finite
transfer a different, independently testable task. Historical stops
remain preserved, and this review does not restart the uniform route.
No failed search is evidence of novelty.

After this separate approval, stop at the first complete strict
N=min(n-1,M)>v_7(b), using v_7(0)=infinity and the existing L027 limiting
error. If ordinarity or an essential path/normalization check fails,
retain the failure and stop the inference. If n=2,3,4 all fail the
strict comparison, retain every failed bound and reassess before extending
the schedule. A finite P_n coefficient alone is no limiting certificate;
an enclosure containing zero proves neither vanishing nor nonvanishing.

Uniform coefficient production, rational membership, Sha defects and
arbitrary complex-order comparison remain separate gaps. Full matching
Mathlib coverage remains not checked; unknown is not absence. No
cross-notebook theorem input, new lemma or mathematical script is used.
The approved next task is REPRODUCTION, and no BSD candidate exists.
