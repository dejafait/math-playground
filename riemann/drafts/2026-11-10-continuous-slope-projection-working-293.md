# Continuous-slope projection attempt — step293

Gate: the unchanged EXPLORE assessment
`literature/2026-11-10-continuous-slope-phase-projection-review-291.md`.
Target: its exact fixed two-quartet test, with no tuning of chi,
the slopes, r=2 or the two hypothetical inputs.

Main gap: L030-L032/C032a actual-Xi positivity and L966/L968 signed
forcing. Intermediate use: decide whether this finite spectral
filter merits a later actual-complement question. Actual outputs,
infinite-zero/regulator control, L993 recovery and L984(H) remain open.

The continuation test is a nonzero algebraic selected response with
interfering response little-o. The approved stop test is an incompatible
selected scale, or selected root growth at most one with interfering
limsup root growth strictly greater than one. Failed estimates are
inconclusive. Known source tools and stops214/244/279/284/285 are reused;
inverse271 is untouched. No cross-notebook input is used.

## Saved before lengthy work

L994's exact K identity and real bound, and L995's full coefficient
and inverse proofs, have been read. L995 is fixed-slope evidence only;
any continuously varying inverse or integrated singularity must be
justified here. L996 is downstream context, not a mathematical input.

Two possible implementations of the same assay are under consideration:
uniform bulk asymptotics followed by an endpoint saddle, or a directly
integrated generating germ whose endpoint singularity certifies the
coefficient root growth. The latter could avoid promoting a pointwise
algebraic error to an exponentially accurate projected error.
Neither implementation has yet established a Pi_n conclusion.

In particular the complete quartet, both critical branches, all four
moving interval endpoints, and K_m's constant subtraction must survive
the final comparison. An isolated endpoint contribution is insufficient.

## Saved analytic mechanism

Put B=9/4 and Delta=eta_1-eta_0=1/8+i. The exact coefficient
bound gives limsup |Pi_n(eta_0)|^(1/n)<=1 and bounds the interfering
root growth above by exp(B/8). The proposed certificate for equality
is a singularity at s(B)=exp(-B*Delta) of the INTEGRATED degree germ.

The upper positive-ordinate critical image is exactly
s(c)=exp(-c*Delta), after the prescribed normalization. Near B,
the other three right-pair critical images are distinct, and lower
endpoints, reflected points and the constant subtraction are regular.
The selected inverse has U=w_c+v_c*sqrt(q)+O(q),
v_c=-w_c*(1-i)*sqrt(tan(theta_c/2)), q=1-z/s(c).
The r=2 endpoint amplitude contains
(exp(2*c*lambda)-1)/lambda with Re(lambda)=3/8, hence is nonzero.
These statements still require the complete uniform proof below the
canonical result before they can certify the assay.

The endpoint coordinate z=s(B)*exp(Delta*y), x=B-c, would reduce
the only singular part to
integral_0^epsilon chi(B-x)*sqrt(x-y)*H(x,y)dx,
with H analytic near (0,0), H(0,0)!=0. Across real y>0 its jump is
-2*i*integral_0^y chi(B-x)*sqrt(y-x)*H(x,y)dx. Positivity of chi
and the common phase of H near (0,0) make this jump nonzero even
though chi is flat. This supplies an exact projected-germ argument,
not a claim that a pointwise asymptotic remainder is exponentially small.

Outstanding while this checkpoint is written: justify joint local
branches, isolate every other contribution, fix the square-root
determination, and prove that the jump is a continuation of the
original integrated germ. If those pass, Cauchy-Hadamard gives
limsup |Pi_n(eta_1)|^(1/n)=exp(9/32)>1, the approved stop criterion.

## Completion

The full proof and qualifications are now canonical in
[L997](../lemmas/L997-continuous-slope-projection-endpoint-leakage.md).
It addresses the saved outstanding points by exact inversion and a
convergent local expansion, retaining every complementary term before
proving it regular. The jump, not a numerical preview or a truncated
saddle expansion, certifies the interfering radius exp(-9/32).
The fixed assay has an informative negative result; independent
conceptual audit remains required. The earlier saved paragraphs record
the work in progress and are not additional unproved premises.
