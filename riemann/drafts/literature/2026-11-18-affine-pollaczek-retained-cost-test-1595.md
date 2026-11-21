# Affine Meixner-Pollaczek finite test1595

TARGET: Test whether degree-dependent affine Meixner-Pollaczek references with lambda_d>0, 0<phi_d<pi, real m_d and nonzero real sigma_d can match the first three subleading coefficients of unchanged P_d and make the fourth/fifth retained Schmeisser cost o(d^2).
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Source-review1595 searched exact-family prescribed/leading-coefficient, Schmeisser, Jensen-reference, coefficient-matching and varying-parameter terminology; compared the named local reference and flow stops. Full queries and evidence limits are in source-notes1595. No adequate exact-cost theorem was inspected; no novelty assertion.
SOURCE_EVIDENCE: DLMF v1.2.8 (18.19.6)-(18.19.9) https://dlmf.nist.gov/18.19 ; (18.20.10) https://dlmf.nist.gov/18.20#E10 ; (18.22.7)-(18.22.8) https://dlmf.nist.gov/18.22#E8 ; (18.23.7) https://dlmf.nist.gov/18.23#E7 ; (5.11.9) https://dlmf.nist.gov/5.11#E9 ; Koekoek-Swarttouw Section1.7(1.7.1)-(1.7.4),p37 https://tudelft.roelofkoekoek.nl/documents/as98.pdf ; reuse Schmeisser2002 Theorem1/Corollary1 pp205-207 and complete relevant proof coverage in C028a/source-notes1503. Source-notes1595 records inspected qualifications and non-input asymptotic leads.
COMPARISON: Positive-weight orthogonality, exact finite definition and monic recurrence cover the stipulated parameters degree by degree. Their actual-P_d matching and retained statistic are not source conclusions. C028j's Laguerre stop, C028c's terminal reference stop and L530/L955's flow stops do not state this test. No uniform varying-parameter asymptotic or real-root premise is needed.
GAP: Determine eventual feasibility and, if feasible along unbounded degrees, whether the specified nonnegative retained contribution can be o(d^2). Passing is only a necessary diagnostic for a full I(P_d)=o(d) bound.
REASON: Import known formulas without reproof; the justified work is their finite affine/norm and actual-coefficient specialization. This is a routine calculation/REPRODUCTION, not a creative central-gap mechanism or a certified new discovery.
SCOPE: Integers d>=5; unchanged C028a P_d,b_j and fixed v=S_2>0,tau=S_3>0. A common finite tuple lambda_d>0,0<phi_d<pi,m_d real,sigma_d real nonzero is used for every 0<=n<=d; arbitrary degree dependence, negative scale and boundary approaches are included. No RH, real roots, simplicity, compact-parameter or conditioning assumption.

This ready assessment was newly written in literature-only review1595.
It requires separate approval next turn. No calculation is executed or
accepted by this note; no further source search is needed for the unchanged
scope unless that approval identifies an essential omission.

## Fixed construction and bounded test

Distinguish the standard reference polynomial P_n^(lambda)(z;phi) from
the unchanged actual P_d(x). Define

    q_n(x)=sigma^n*n!/(2*sin(phi))^n
                            *P_n^(lambda)((x-m)/sigma;phi),
    w(z)=|Gamma(lambda+i*z)|^2*exp((2*phi-pi)*z).

The reference measure is the pushforward of w(z)dz divided by its
total mass, as supplied by DLMF (18.19.9). Let h_n be the q_n squared
norms in this measure and write P_d=sum_(n=0)^d a_n*q_n. Check all
normalizing factors under arbitrary signed sigma. The exact recurrence
and terminating (18.20.10) suffice to extract the finite coefficients;
do not substitute an asymptotic formula with fixed parameters.

The first stage is exactly a_(d-1)=a_(d-2)=a_(d-3)=0. Characterize
feasibility in the full admitted domain before computing higher costs.
Only when an unbounded feasible family survives consider

    B_d=(h_(d-4)*a_(d-4)^2+h_(d-5)*a_(d-5)^2)/h_(d-1).

At d=5 the second term uses a_0. The necessary threshold is B_d=o(d^2),
inherited from C028a's full real Schmeisser statistic. If higher actual
coefficients are used, obtain their exact identities from C028a/L025 and
preserve all sign/evaluator qualifications; do not fit them numerically.
No parameter sweep or new infinite-Xi expansion is proposed.

Stop on eventual infeasibility, including unbounded subsequences, or
a uniform positive lower limit of B_d/d^2 over all feasible choices.
A positive test requires an explicit unbounded admissible sequence with
the ratio tending to zero, not a finite numerical sample. An inconclusive
attempt is recorded honestly and does not authorize unlimited optimization.
Even a vanishing retained cost leaves every other residual unpaid.

C028a supplies the actual polynomial, cubic identities and source-height
interface. C028j and C028c are contrasts, not mathematical premises of a
new obstruction. L030-L032/C032a positivity, C028b's H_d=o(d), odd
cancellation and unsmoothed realization stay unresolved. No lower bound
on actual heights follows from a large upper-bound statistic. Full
matching Mathlib coverage is unchecked and unknown.
