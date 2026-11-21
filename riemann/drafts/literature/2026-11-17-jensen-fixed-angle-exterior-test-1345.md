# Actual Jensen circle: fixed-angle exterior test1345

TARGET: Test whether Ono2610.38870v1 Lemmas7-8/12-13 pay the fixed-angle exterior of the actual K=Q Jensen Cauchy circle: for q=q_e+x*d^(-2/3), 1<=x<=4, and each fixed 0<theta_0<=1/10, prove or refute sup_x |I_out(d,x;theta_0)|/M_d(x)=o(1), with M_d and both semicircle pieces defined in the assessment.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1345 inspected Ono's exact whole-circle bounds and CFU's exterior hypothesis; reuse that completed assessment and its unshifted/coalescing searches. This test applies the known bounds on a different cutoff; it does not claim a new contour theorem.
SOURCE_EVIDENCE: Ken Ono, arXiv2610.38870v1, (2.5)-(3.3), Lemma7/full proof pp6-7, Lemma8/full proof pp7-8, Lemma12/full proof p10 and Lemma13/whole-semicircle proof p11, exact (4.5)-(4.6), plus the angular Cauchy measure in Proposition15 p13: https://arxiv.org/pdf/2610.38870v1 . CFU1957 Section5 p607 identifies why an exterior estimate is required: https://doi.org/10.1017/S0305004100032655 .
COMPARISON: Known phase and amplitude estimates cover this exterior region before Gaussian asymptotics. The work is an ordinary specialization retaining a fixed cutoff, exact degree parameters, polynomial amplitude allowance, Cauchy prefactor and conjugate upper half. No Airy expansion is imported or needed for this isolated test.
GAP: Check eventual source parameter ranges, a positive phase separation on the retained exterior, boundary branches, amplitude nonvanishing and the ratio against the proposed d^(-1/3) scale. The ratio is a target, not a result. Local cubic/reference and sign gaps remain independent.
REASON: A narrowly paid exterior is a necessary possible input to the parked full edge comparison; unlike assuming CFU's outside-small hypothesis, this is independently checkable from inspected source estimates. No additional essential source coverage is missing for this test.
SCOPE: K=Q only, n=0, d integer tending to infinity, x in [1,4], each fixed theta_0 in (0,1/10]; constants/onset may depend on theta_0, never on x or d. No claim uniform as theta_0 tends to zero. Proposed REPRODUCTION; new ready continuation requires separate supervisor approval before invocation.

## Exact proposed test, not an established estimate

Use Ono's F, T, Lambda, B=T^2, kappa, A_d and h_q verbatim.
For q=q_e+x*d^(-2/3), let r,alpha,u_q=r^2 exp(-2i alpha)
be precisely its Lemma7 parameters. No new saddle approximation is
being defined. On the full circle let

I_out(d,x;theta_0) = d!/(2*pi*i*d^d) times
integral over {u=r^2 exp(i theta): theta_0<=|theta|<=pi}
of F(T^2*u) exp(-d*q*u) du/u^(d+1).

Each of the two arcs has counterclockwise orientation; this definition
includes the original Cauchy prefactor and both negative-axis boundary
values. It introduces no connector or contour deformation. On the lower
arc use the source's branches with -pi<=arg(u)<=0, and on the upper
arc use their conjugates. F itself and the integer power are single-
valued. Match the source's measure du/u before applying a modulus bound.

Use its lower amplitude a_q(theta) from (4.4) and define the positive
comparison scale

M_d(x) = (d!/d^d)*|a_q(-2*alpha)|*
         exp(d*Re(h_q(u_q)))*d^(-1/3).

This is a proposed normalization for an exterior-payment test, **not**
a proved Airy leading term, a value of A_d, or a signed lower bound.
Do not divide by an Airy function, or silently replace d^(-1/3) by a
Gaussian factor. Source amplitude nonvanishing and every parameter
restriction must be checked before division. No coefficient dictionary
to a different local P_d is needed: the observable is source A_d.

## Source inputs and remaining calculation

Import Ono's named estimates by citation; do not reprove its whole
root-count theorem. Check K=Q, the exact eventual q-range required by
Lemma13, and the uniform near-edge parameter information in Lemma7.
Lemma8's phase decrease holds on the entire lower semicircle;
Lemma13's whole-semicircle amplitude ratio allows polynomial growth.
The upper arc needs the conjugate bound with its correct orientation.
All constants and limiting statements must be uniform in x in [1,4].

The bounded discriminator is whether these inputs give a positive
fixed-cutoff phase gap and an exterior upper bound that is o(M_d).
Write the actual resulting upper bound, required o(1) threshold,
constant dependencies and any failed inequality. No numerical script
or finite sampling is needed. If the source envelope fails the test,
report only failure of that certificate, not a lower bound on I_out.
If it succeeds, it pays just the fixed-angle exterior. Neither outcome
permits substituting the estimate for an unresolved local integral.

The cutoff is fixed while d grows. Shrinking theta_0 with d, moving
connectors inside the omitted local arc, differentiating a remainder,
extracting a real cubic coefficient and asserting Airy signs are outside
this assessment. A later full cubic comparison requires its own paid
coordinate/amplitude/connector argument; the original sign-window
nomination remains parked until those are supplied.

Main goal relevance: actual all-degree positivity L030-L032/C032a is
still open. A successful exterior payment removes one explicit analytic
obligation for an alternative local unshifted-root estimate. It leaves
all-degree hyperbolicity, outer root losses, exceptional zeros, local
sign margins and finite initialization unproved. This is not a direct
Schur-residual payment. No cross-notebook input is used.

Existing failures: reuse review1345's exact comparison with the named
Laguerre average and unshifted bulk sources; neither is this full-circle
fixed-cutoff test. This refinement changes the cutoff mechanism rather
than repeating the stopped automatic Gaussian/Airy sign import. No
novelty or universal impossibility is inferred. Mathlib full matching
coverage unchecked. Routine source specialization is not creative work.
