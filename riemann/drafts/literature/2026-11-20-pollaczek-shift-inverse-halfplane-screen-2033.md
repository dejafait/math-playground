# Fixed Pollaczek inverse/half-plane screen — nomination2033

TARGET: Test C029n's full U_6 for the fixed identity U_6=(3/4-it/2)h(t+2i)+(3/4+it/2)h(t-2i), with real h of degree at most six, and certify whether h has at most one zero in Im(t)<-2 counted with algebraic multiplicity.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed imaginary-shift comparison2033 searches exact Pollaczek difference equations, inverse operators and exceptional-zero bounds, and checks the recorded finite stops; no inspected source supplies this actual inverse's half-plane count. drafts/literature/2026-11-20-pollaczek-imaginary-shift-discovery-2032.md
SOURCE_EVIDENCE: NIST DLMF18.22.16-18 https://dlmf.nist.gov/18.22#ii ; de Bruijn, Duke Math.J.17(3)(1950),197-226, Lemma2 and complete proof p215, https://repository.tudelft.nl/file/File_524a4d3c-0858-4c55-b425-8c8ce1fb89da ; standard Rouché theorem/proof, Berkeley Lecture23,22April2026, https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_23.html ; C029n's exact finite source formulas/enclosures reused.
COMPARISON: The operator is fixed by the source equation and supports an inverse coefficient screen; the general polynomial real-part zero bound is known. The actual inverse/half-plane count is not supplied by preservation or by the basis recurrence. This is known-method specialization, not a novelty claim.
GAP: Solve and verify the full identity, establish actual degree, and certify the multiplicity-counted half-plane threshold, including any boundary difficulty. A finite pass leaves the eventual uniform inverse-family condition entirely open.
REASON: One fixed-source inverse screen tests a weaker input-location condition than real-rootedness without reusing residue signs, boundary metrics, affine increments or the failed differential range. It is not another isolated root count of T_6.
SCOPE: Newly written ready nomination; separate approval must precede research. Only N=6, shifts +/-2i, coefficients 3/4-/+it/2 and C029n's unchanged U_6/enclosures. No parameter fit, auxiliary coefficient substitution, degree campaign or precision increase.

## Purpose and exact scope

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
C029m's sufficient eventual full-family index bound remains unproved.
The intermediate target is the displayed identity plus one specific
input-location count for its real polynomial preimage. No such identity
or count was verified in the literature-only nomination.

Use every odd and even coefficient of U_6=T_6/S from C029n, with
S=sin(pi/8)/sqrt(2)>0. The right-hand operator is fixed before any
root information. Use the DLMF equation with lambda=3/4, phi=pi/2,
x=t/2 to check the finite inverse coefficient calculation, including
signs, scaling and degree. Do not assign one eigenvalue to the
weighted sum. Any diagonal inversion must retain the actual distinct
basis eigenvalues and verify every coefficient of the final identity.

Use real h of degree at most six. Prove the actual degree and any
nonzero denominator used. A source formula may be imported with the
necessary applicability check; do not reprove a general difference
equation or preservation theorem. Preserve failed solves or any
unexpected cancellation as evidence, without changing the operator.

## Count and source application obligations

The threshold is at most one zero of h in the **open** half-plane
Im(t)<-2, with algebraic multiplicity. No numerical root list is a
certificate. Boundary roots do not belong to that open half-plane,
but a disk crossing the line cannot be assigned a count from its
center. Resolve such cases rigorously or report the test inconclusive.

For a subsequent source application, use de Bruijn Lemma2: if real
polynomials U,V give W=U+iV with n lower-half-plane zeros, U has
at most n conjugate nonreal pairs. Verify the choice
W(t)=(3/4+it/2)h(t-2i), its real part, every prefactor zero, and
the effect of the shift on the strict half-plane. Nonzero output,
real common factors, multiplicities and possible leading real-part
cancellation must be covered, as in the inspected source proof.
No exceptional-zero theorem for entire functions is being applied.

If useful, certify roots using the standard Rouché theorem cited
above and already covered in C029l: analytic functions on a
neighborhood of a bounded domain's closure with piecewise smooth
boundary have equal multiplicity-counted zeros when the perturbation
is strictly smaller on the boundary. Rational disks/contours with
complete inequalities and coverage of the proved degree are allowed.
Approximate roots may seed contours but do not verify them. A different
unassessed root-count theorem requires a separate source review.

Reuse C029n's exact Q(sqrt(2))[pi] coefficients and proved rational
pi/sqrt(2) enclosures of width 10^(-60). New derived coefficients
must remain exact until interval evaluation. Do not assume separately
evaluated repeated parameters are independent. If a script is useful
after approval, save complete coefficients, contours, zero counts,
bounds, failures and input hashes under scripts/pollaczek/; print
only the actual/required thresholds and certificate path. Inspect
complete load-bearing values, not bounded previews alone.

## Continue or stop

A pass requires the full exact identity and a proved half-plane count
at most one; also check the cited real-part application's hypotheses.
It validates this finite input condition only. A count greater than
one rejects this fixed finite inverse baseline; it does not disprove
an eventual-only law or RH. An unresolved enclosure is inconclusive,
not a negative root count. No degree/precision/shift campaign follows.

Plausible downstream use: a uniform version of this explicit inverse
condition for the **full** T_N family could supply the one-pair bound
needed by C029m. The required family structure is unpaid and must be
separately assessed; no source or finite test supplies it automatically.
This calculation is REPRODUCTION/calculation, not proof_attempt/creative.

Essential inputs: C029m, C029n and the cited DLMF/de Bruijn/Rouché
statements. C029s and the recorded metric/residue/affine stops are
contrasts, not mathematical inputs. Actual-degree/singular and
boundary cases across N, uniformity, initialization and qualified
weighted convergence/upstream[9] remain unresolved. Full matching
Mathlib coverage unchecked. No cross-notebook theorem input.
