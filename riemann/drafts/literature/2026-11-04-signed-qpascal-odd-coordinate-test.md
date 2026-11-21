# Actual signed q-Pascal comparison — odd-coordinate discriminator

TARGET: Test whether strict accretivity of A_r=J(J+F) is already obstructed by e_1^T(A_r+A_r^T)e_1/2 at k=r-1 for the actual Xi coefficients, using the cited q-Pascal factors and finite-value coefficient asymptotics.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step414's exact signed-matrix, accretive-determinant and local duplicate searches recorded in 2026-11-04-signed-qpascal-symmetric-part-review.md; no matching actual odd-coordinate estimate was found or novelty established.
SOURCE_EVIDENCE: Michałowski 2607.16795v1 Lemma4.1/proof, (6), Section6 and Lemma6.2/proof; O'Sullivan 2007.13582v2 Theorem1.4/(1.8), assessed Section7 proof cases; Zhang 2601.18977v1 Section4 Lemmas4.1/4.2 with full proofs. Direct URLs and exact qualifications are below and in step414's review.
COMPARISON: Known finite factorization and strict real accretivity give a possible determinant-sign interface; known actual coefficient asymptotics permit a bounded finite-value specialization. Neither source evaluates this coordinate at k=r-1. L765 excludes only the unsigned norm test on a different ray.
GAP: Verify boundary normalization and the actual low-coordinate expression, eventual 0<q<1 and all amplified integer errors, then decide its sign against zero. No value or sign has been derived; positivity of the remaining directions remains independent.
REASON: One signed necessary-condition test can reject this sufficient mechanism without a matrix scan or assumed minor signs. The calculation specializes known inputs; it is not a preapproved creative all-degree positivity proof.
SCOPE: Integer r tending to infinity, k=d=r-1, original log-quadratic q-Pascal model, one vector e_1 only; finite determinant-transfer verification is included. No changed model, optimized preconditioner, extensive scan, or full source/certificate audit. Newly written ready assessment awaits separate approval next turn.

Use actual L018/L019/L021 and audited L765's finite-normalization
argument; do not import L765's k=1024r asymptotic at the changed center.
L766 and L773 are route comparisons, not premises. No actual
real-rootedness, all-order Turan positivity or cross-notebook input.

Define a_n=M_(2n)/(8*4^n*(2n)!)>0 and f(n)=log(a_n), n>=0.
For k=d=r-1 and r>=2 put

    rho=a_(k+1)/a_k,
    q=a_(k-1)*a_(k+1)/a_k^2, tau=-log(q),
    h_s=f(k+s)-f(k)-s*(f(k+1)-f(k))+tau*s*(s-1)/2,
    V_ij=q^(i*j), L_ij=[i choose j]_q (i>=j), 0 otherwise,
    D_m=product_(h=0)^(m-1)(q^m-q^h), D_0=1,
    E_ij=V_ij*(exp(h_(d-i-j))-1),
    F=|D|^(-1/2)*L^(-1)*E*L^(-T)*|D|^(-1/2),
    J=diag((-1)^m), A_r=J*(J+F), H_r=(A_r+A_r^T)/2.

Indices i,j,m are zero-based, 0 through r-1; |D| is the diagonal
matrix of absolute pivots. All a-indices in E lie in [0,2r-2]. First
prove eventual 0<q<1 before using invertible whitening. Define
e_1=(0,1,0,...) in R^r and Q_r=e_1^T H_r e_1.
These are proposed test definitions, not evaluated identities or signs.

The full cited inputs are:

- [Michałowski v1](https://arxiv.org/html/2607.16795v1#S4), Lemma4.1:
  exact finite V=L D L^T for r>=2, 0<q<1. Its (6) and Section6
  specify the comparison. Verify its finite positive diagonal
  transformations at k=d, including the rho-direction correction
  already audited in L765. Do not use the tail theorem or its small
  r*tau bounds. Check the determinant/signature/column-reversal
  arithmetic when relating a hypothetical H_r>0 to D_(r,r-1)>0.
- [Zhang v1](https://arxiv.org/html/2601.18977v1#S4), Lemma4.2:
  H=(A+A^T)/2>0 for a real square A implies det A>0. Import this
  theorem; no reproof is needed. Semidefiniteness gives only det A>=0.
  No actual strict accretivity has been proved. No stronger inertia
  claim is an input.
- [O'Sullivan v2](https://arxiv.org/html/2007.13582v2#S1), (1.2),
  Theorem1.4/(1.8): arbitrary fixed-order integer-value coefficient
  expansion for gamma_n, with O_K(log(n)^K/n^K) remainder and
  w=W(2n/pi). Preserve a_n=gamma_n/(8*4^n*n!). Use a fixed K
  sufficient for every finite-difference multiplier; do not
  differentiate its remainder or assert an effective onset.

Extract just the rows needed for Q_r using lower triangularity, checking
which coefficient indices actually survive. Establish the error in
each combined adjacent-defect expression before exponentiating or
taking ratios; separately coarse endpoint errors may not suffice.
Use finite values, not a smooth interpolation of unknown errors.
If the necessary support reaches bounded indices, keep those exact
values and do not apply a large-n expansion there.

Decisive evidence is a rigorous eventual nonpositive Q_r, or one
rigorously certified nonpositive example. Either rejects strict H_r>0
for the proposed all-order mechanism. A rigorous positive asymptotic
is informative only for this coordinate; it does not establish H_r>0.
If the error cannot decide the sign, save its precise size and stop
this attempt without enlarging the vector family or scanning degrees.
Continue beyond this test only if it passes and an explicit remaining
signed estimate can be nominated and assessed. No result is anticipated.

Downstream use is a discriminator for a signed sufficient matrix route
to exceptional actual coefficient signs. Even full success on that
edge leaves other shifts, finite orders and the main mixed-positivity
assembly unresolved. A failed sufficient condition is not a negative
minor or a disproof of RH. Mathlib matching coverage is not checked.
