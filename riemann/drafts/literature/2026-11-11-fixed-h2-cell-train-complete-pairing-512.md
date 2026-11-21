# Fixed-H2 neutral cell trains: complete-pairing attempt

TARGET: Test the fixed-H2 neutral single-profile cell-train detector against the complete zeta-zero pairing, proving exact admission and either full-zero negative separation from a hypothetical off-line zero or identifying a precise alias, tail or realization obstruction.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed step512 exact detector comparison and step511/279/283 searches, with queries and primary proof locators in 2026-11-11-fixed-h2-cell-train-detection-511.md. No matching constrained detector theorem was found in that bounded search; this is not evidence of novelty. This is a continuation nomination, with no mathematical attempt performed here.
SOURCE_EVIDENCE: Ready compact-test inputs are Suzuki2206.03682v4 https://arxiv.org/pdf/2206.03682v4 Section2.2, Sections3.1-3.5, (3.3), (3.5), Proposition3.1, and Suzuki2606.09096v3 https://arxiv.org/html/2606.09096v3 Section3.1(3.1), whose statements and relevant proof cases were inspected in step279/283. L742(8)-(12) supplies the local smooth-energy identification; L744(1),(6) and C744q fix the actual norm, moments, energy and downstream scale. The newly inspected detector lead is assessed in step512; none of its stronger detection assertions is an imported input.
COMPARISON: The known formula retains all complex ordinates with conjugate pairing and multiplicity. It does not supply negative separation or realize arbitrary compact-test witnesses as one-profile trains with a prescribed H2 cap. L742's positive spectral measure is RH-conditional; L743's unbounded modulation does not retain that cap. The exact difference is the constrained full-zero separation, not a reproof of the formula.
GAP: Exact train admission, nonvanishing of a suitable admissible profile at the relevant spectral data, complete-zero/alias separation and eventual-scale transfer are unproved. No rightmost zero, finite off-line set, spectral isolation, positive nonreal measure or favorable removed-zero remainder may be assumed. The implication being tested is not established.
REASON: A single complete-pairing test can determine whether imposing fixed Sobolev regularity actually removes off-line witnesses, a central obstruction to an independent low-energy floor. Essential formula coverage is ready and the new source lead has been compared; no further optional access retry is needed. The new ready continuation receives separate supervisor approval next turn.
SCOPE: ell=log(3)/2; fixed prescribed M0 for which there exists a nonzero locally neutral C_c^infinity(0,ell) profile with normalized H2 norm strictly less than M0; finite complex coefficient trains with one profile fixed as K varies; original complete E_(K ell), both local moments, unit unweighted L2 normalization and the actual smooth generator domain. No mathematical conclusion is asserted by this scope.

The main gap remains L030-L032/C032a actual-Xi positivity. This is a
diagnostic of the proposed low class, not a positive-margin theorem.
C744q's sufficient threshold remains

    E_(L_R)(u) >= 32 C^2 log(R)/R^4,
    K_R=floor(log log R/ell), L_R=K_R ell.

Even a detector would leave this independent sign, non-neutral coverage
and all-window assembly unresolved. No actual off-line zero is supplied.

## One bounded conceptual attempt

For nonzero f in C_c^infinity(0,ell), with

    integral exp(s/2) f(s) ds = integral exp(-s/2) f(s) ds = 0,
    ||f||_H2/||f||_2 <= M0,
    ||f||_H2^2 = ||f||_2^2+||f'||_2^2+||f''||_2^2,

consider, for a nonzero finite coefficient vector c,

    U_(K,c,f)(x)=sum_(j=0)^(K-1) c_j f(x-j ell),
    u_(K,c,f)=U_(K,c,f)/||U_(K,c,f)||_2.

First verify exact admission to L744's smooth family with both moments
and the actual generator domain. The denominator and budget must be
proved, not assumed from the notation. A prescribed M0 must satisfy the
stated strict-slack hypothesis; no assertion is made for every M0>=1.
The same f may depend on the hypothetical zero but must remain fixed as
K varies. Arbitrarily growing carrier frequency is not a substitute.

Then import the ready compact-smooth Weil identity by precise citation
and justify its Fourier convention for this finite train. Retain the
full conjugate-ordinate sum, every multiplicity, all translation aliases
and the finite-train convergence justification before any separation.
The desired conditional conclusion is existence of some f,K,c with
E_(K ell)(u_(K,c,f))<0 whenever an off-line nontrivial zero exists.
This paragraph sets a target and supplies no formula derivation or proof.

Continue only if the signed complete-zero argument controls the
complement without a rightmost-zero assumption or an unproved isolation
condition. A negative quartet, a finite-list eigenvalue, an unrestricted
interpolation assertion or an enlarged budget is not success. Stop after
one coherent attempt if a precise alias, tail or realization obstruction
remains; retain the exact unpaid claim and partial reasoning. An unclosed
estimate is not a counterexample to the detector and does not prove a
positive low floor. Repetition requires materially new input or a refined
mechanism with a discriminating test.

A witness at a single finite K does not itself establish the conclusion
on every eventual K_R scale. Record that transfer as an independent
obligation unless justified in the attempt. No finite sign calculation
or hypothetical zero supplies an RH proof or disproof.

## Reuse, failures and routing

The detailed source comparison, version qualifications and inspected
proof cases remain in [step512](2026-11-11-fixed-h2-cell-train-detection-511.md).
Reuse step279/283's ready compact-test assessment; do not browse again
merely because the constrained conclusion is unproved. Known results are
imports; the new work is only the uncovered constrained difference.

Essential local IDs are L742, L743, L744 and C744q. The unconditional
smooth identity L742(8)-(12) is usable; its RH-positive measure (4)-(7)
is not. Keep the signed neutral-tail Gram-dual and screw-remainder source
stops as contrasts, with no use of their unpaid estimates. L749/L750's
specific allocation/localization stops are also preserved; a historical
stop is not a general ban on distinct train separation. The October
baseline/register do not remove possible residual off-line zeros.
No cross-notebook input. Full matching Mathlib coverage is unchecked.

After separate approval, route proof_attempt/creative,
deep_research/max. The precise obstruction is survival of off-line
detectors under one fixed Sobolev budget; its relevance is whether the
low-margin strategy conceals an RH-strength obstruction. The bounded
test is exact admission followed by one complete-zero separation attempt.
Decisive evidence is a justified negative full energy at that budget or
a rigorously qualified alias/tail/realization obstruction. This mechanism
does not reproduce the high-modulation Rayleigh diagnostic.
