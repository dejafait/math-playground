# Rational periodic storage: bounded mathematical attempt

Approved target and scope are unchanged from
`literature/2026-10-31-rational-periodic-storage-test.md`: arbitrary
four-state homogeneous quadratic W plus c R(x_0,y_0),
R(x,y)=x^3 y/(x^2+y^2), extended by zero, both branches on R^6,
full trace, and the closed-I dual. No larger storage class is tested.

Main gap: actual-Xi all-degree signs at unbounded heights. The
intermediate target is a certified cost below 1/288 or an exact
whole-family obstruction. A successful upper certificate could exclude
the nominated periodic surrogate; Xi transfer remains independent.
Reuse the supplied SPECIALIZE assessment, L589's audited quadratic
cancellation, L473 Section 4, L586 definitions and L588 Section 1.
The quadratic stop and the prior rational source working record were
checked; no matching rational result was recorded there.

Partial reasoning saved before further calculation (not yet a result):
off the origin, with d=x^2+y^2,

    R_x=x^2 y(x^2+3y^2)/d^2,
    R_y=x^3(x^2-y^2)/d^2,
    D R=R_x y+R_y z.

The quadratic growth of R and linear growth of its gradient should
verify C1 and the periodic chain rule, including the origin. For
the original finite B, x=epsilon, y=v, z=k epsilon, so setting
q=v^2 gives

    D R=[q(1+3q)+k(1-q)]/(1+q)^2.

The original q in {0,1/6} appears to give E D R=29/1176>0.
This alone cannot stop c<0. A second candidate keeps epsilon and k,
replaces q by {0,2} with P(q=2)=1/24, and keeps independent symmetric
signs. It preserves E q=1/12 and the first covariance block, while
appearing to give E D R=-19/1296 and E Q=23/1728. The same Schur
extension should restore the full K. If all values and extension
hypotheses check, the two laws obstruct opposite signs of c and
therefore the entire approved family. This is a test of global
inequalities, not a stationary or periodic realization.

Still to check: exhaustive finite sums, exact gradient bounds/origin,
periodic flux at arbitrary P and lag one, complete K extension and
the full two-branch implication. No mathematical script or solver has
been run. Do not interpret this working checkpoint as a proof.

Refinement before verification: the opposite-sign idea can be encoded
in a single finite witness. Keep epsilon and k and choose q=y^2 in
{0,1,2} with probabilities (625,38,9)/672, using independent symmetric
signs for nonzero y. Then E q=1/12. The conditional derivative means
appear to be (-1/12,1,169/108), whose weighted mean is zero. This
would annihilate c D R exactly for every c, in addition to L589's
quadratic cancellation. The clipped mean would be 625/48384, above
1/288 by 457/48384. The same Schur extension applies if the complete
K_0 block checks. This refinement stays within the approved whole-family
obstruction test; it changes a witness, not the storage or state domain.
These values still require the complete finite verification below.

Completed outcome: the refined witness checks exactly. The full proof,
including C1/growth at the origin, periodic flux, the original-law
diagnostic, all six reduced atom cases, the Schur extension to K,
quadratic cancellation and the global-branch implication, is canonical
in L590 (`lemmas/L590-rational-periodic-storage-finite-law-obstruction.md`).
The original two-witness sketch above was superseded by this single
annihilating law; it is retained as reasoning history, not needed by
the final proof. No certificate optimization or broader storage was
attempted. The bound is 625/48384, exceeding the required 1/288 by
457/48384. This supplies an informative NEGATIVE for the approved
family; independent audit remains pending.

`scripts/rational-periodic/verify_finite_witness.py` passed with zero
failures and wrote `scripts/rational-periodic/finite-witness-certificate.json`.
The complete selected old/new-law values and failure array were read
with the shared JSON inspector. The code verifies finite arithmetic;
the analytic obligations remain in the canonical proof. Source
coverage was reused unchanged, no external browsing or cross-notebook
input was needed, and no existing unfinished work was discarded.
