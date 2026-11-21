# Actual-G collective saddle in a fixed sector collar

TARGET: Test whether, for every sufficiently large integer r with k=r-1, the full actual-G angular density has a nonzero stationary point with nonsingular logarithmic Hessian in the fixed collar max_j|Re(zeta_j)|<=1/2, max_j|Im(zeta_j)|<=1.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed joint-angular-contour source review searched actual-Xi/Toeplitz/collective-saddle/stationary-point and electrostatic-equilibrium terms and checked local contour failures. No inspected result settles this exact growing-r collar question. This is bounded coverage, not a novelty certificate; details and primary comparisons below.
SOURCE_EVIDENCE: Reuse Katkova math/0505174v1 Lemmas1–2/(10)–(13), pp7–8 and Lemma4(c)/proof, pp11–12, rechecked in the companion review; L775 supplies actual G, scalar R_k and its justified compact-sector specialization. Pemantle–Wilson0903.3585v1 Thm2.3/Section5 supplies conditional fixed-dimension context only. Bertola–Chavez-Heredia–Grava2206.06861v4 Section1/(1.3)–(1.16), Definition1.1 and complete Thm1.3 were inspected for rational-field scope, not imported.
COMPARISON: The full interacting saddle is different from the scalar coefficient saddle used in L775. Known fixed-order positivity does not locate this configuration; fixed-dimension saddle asymptotics assumes the needed geometry. The inspected Stieltjes correspondence concerns rational external derivatives and conditional/generic orthogonality, not the actual-G collar. No known contour, root geometry or minor sign is assumed.
GAP: Decide the quantified collar-existence statement, retaining the exact sine Vandermonde and actual G. No derivative equations, limiting configuration, existence, exclusion or Hessian bound has yet been derived. Even success leaves thimble participation, quantitative errors, summed phases and all mixed-sign transfer unresolved.
REASON: This independently testable geometric prerequisite can discriminate a collective saddle confined to a known analytic sector before another unpaid signed-remainder attempt. It is not a nearby-cutoff or absolute-complement test, and does not reinstate the rejected automatic contour import.
SCOPE: One future analytic proof attempt on the exact TARGET after separate approval. Work in the specified logarithmic angular coordinates; preserve both boundaries, all interaction factors and actual G. No finite minor/atomic scan, generic positive-weight replacement, assumed deformation, all-order sign theorem or RH claim.
COVERED_TARGET: Test whether, for every sufficiently large integer r with k=r-1, the full actual-G angular density has a nonzero stationary point with nonsingular logarithmic Hessian in the fixed collar max_j|Re(zeta_j)|<=1/2, max_j|Im(zeta_j)|<=1.

## Exact proposed object and decision rule

This is a prospective target, not a result established in the literature
turn. Use L775's G(z)=xi(1/2+sqrt(z)/2)/8, with its ordinary coefficients
a_n=M_(2n)/(8*4^n*(2n)!), and unique R_k>0 satisfying
R_k G'(R_k)/G(R_k)=k. L018/L021 underlie that existing interface.
Define the proposed complex angular density by the same expression
inside Katkova (13), before taking a real part:

    H_r(zeta)=product_j [exp(-i*k*zeta_j)*G(R_k*exp(i*zeta_j))/G(R_k)]
               * product_(i<j) 4*sin((zeta_i-zeta_j)/2)^2.

This specifies a function to investigate; it asserts no new contour
identity or critical-point formula. The new question is whether for
every sufficiently large integer r>=2 there exists a vector zeta in
the closed collar stated in TARGET for which

    H_r(zeta) != 0,
    partial_(zeta_j) H_r(zeta)=0 for every j,
    det(partial_(zeta_i) partial_(zeta_j) log H_r(zeta)) != 0.

The logarithm in the last condition is local at that nonzero point;
do not assume a global branch. A point on either collar boundary
counts. A failed search or exclusion on a smaller open collar does
not disprove this assertion. Verify the relation to any alternative
z=R_k exp(i*zeta) coordinates; a saddle of a density depends on its
coordinate measure. No claim of coordinate-invariant nonexistence is
permitted. Zeros or collisions cannot count as the required nonzero
stationary point, even when derivatives of H_r vanish there.

One bounded attempt should derive the exact coupled equations from
this specified object, then seek an analytic construction or a
necessary-condition obstruction uniform in r on this one collar.
No equation is supplied or derived in this assessment. Scalar saddles
or a saddle of a modulus on a real constrained domain do not answer
the holomorphic full-density question. Justify all complex derivative
estimates; do not differentiate the O-term of a real-axis asymptotic.

Continue only on a proved eventual family with the required nonzero
value/Hessian, or a quantitative partial condition that materially
narrows the missing geometry. An eventual exclusion, or rigorously
excluded unbounded sequence of orders, refutes this particular
eventual-existence assertion. Such an exclusion stops this collar
mechanism only. If neither is proved, save the exact equations and
unpaid inequality as inconclusive; do not repeat without new input.
Finite numerical samples are neither uniform existence nor exclusion.

## Source comparison and remaining obligations

[Katkova, math/0505174v1](https://arxiv.org/pdf/math/0505174v1#page=7)
supplies the coefficient identity, not this stationary configuration.
Its Lemma4(c) proof, pp11–12, uses the Euler product and sectorial
Stirling. Reuse L775's qualified specialization; do not import the
source's flagged auxiliary generic-C derivative estimates. The proposed
collar has a fixed angular width and bounded logarithmic radial width.
Its analytic estimates, boundary cases and any uniform derivative
bounds remain application work, not an assumed conclusion.

The companion joint-angular-contour assessment records the exact
[Pemantle–Wilson](https://arxiv.org/pdf/0903.3585v1#page=4)
hypotheses and the
[Lawrence–Yamauchi](https://journals.aps.org/prd/pdf/10.1103/PhysRevD.110.014508#page=2)
phase/Jacobian warnings. Neither is an existence theorem for this
configuration. No error bound or perfect-contour assertion is imported.

Marco Bertola, Eduardo Chavez-Heredia and Tamara Grava,
[*The Stieltjes–Fekete problem and degenerate orthogonal polynomials*,
2206.06861v4, 19 August2023, Section1, Definition1.1/Theorem1.3,
(1.3)–(1.16)](https://arxiv.org/html/2206.06861v4#S1),
was inspected to check the electrostatic terminology and stronger
known correspondence. Its field derivative is A/(2B) for relatively
prime polynomials; its conclusion relates equilibria and maximally
degenerate semiclassical orthogonality, with genericity, shared-root
qualifications and the printed extra degree/residue condition in the
converse. No rational-field identification, orthogonality or existence
in our prescribed collar has been supplied for G. Thus it is not an
automatic application. The proof in Section3 and the differing degree
inequality printed between Theorem1.3 and Theorems3.5/3.7 were not
audited; none of these results is a premise of the proposed attempt.
No semiclassical replacement or rational truncation of G is authorized.

Plausible downstream use is a sector-confined starting configuration
for a genuinely collective asymptotic treatment of D_(r,r-1), or an
obstruction forcing that treatment outside this collar. Even a
nondegenerate saddle does not establish its contribution to the
original torus, the sign of the summed leading terms, or an error
smaller than a positive main term. Those are independent gaps;
other coefficient shifts and L030–L032/C032a remain unresolved.

L775 is the relevant actual-G input; L843 is retired context only.
The scoped local search found no exact duplicate of this collar test.
Existing scalar-core, real-moment and automatic varying-symbol stops
remain in force at their stated scope. No cross-notebook input is used.
Mathlib full matching coverage is unchecked. No reproof of a known
general theorem is proposed. This new EXPLORE continuation requires a
separate approval next turn; this assessment is not its execution.
