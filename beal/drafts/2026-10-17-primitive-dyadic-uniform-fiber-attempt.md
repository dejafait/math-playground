# Primitive dyadic uniform-fiber attempt — 2026-10-17

Approved target: determine the two-descent Kummer-class set of primitive
whole-fiber-compatible 54a1 dyadic points. Reuse the prior SPECIALIZE
assessment in `drafts/literature/2026-10-16-primitive-dyadic-two-descent-image.md`.

Main gap: primitive integer emptiness; no new global rank or class input
is available. Intermediate target for this bounded attempt: prove the
exact primitive scalar domain and uniform complete-fiber realization,
including every identification into the fixed rational/ramified algebra.
This would remove an essential prerequisite for a correlated Kummer
image calculation. Continue on a certified uniform milestone; do not
enumerate or claim an image unless class constancy and realizations are
proved. The independent class-kernel and integer-lifting gaps remain.

Saved reasoning before completion: with n=v2(c)>=1, the necessary
scalar valuation is 6-11n. Conversely set b=1, take the eleventh root
c of 1728/(1728-s), and the cube root a of s/(1728-s). Both root
equations reduce to odd unit equations after extracting valuations;
the same c works and a=7 mod 8. Put m=11n-6. L034's shifted polynomial
has C0 of valuation -m, C11 of valuation -2m, C12=1 and all other
coefficients of valuation at least -m. L046's two lifts should extend
using z=(2^(2m)u)^(-1) and z=pi^m u, pi^11=2. Since gcd(m,11)=1,
the second root generates all H. Reconstruction and identification
uniqueness still need to be written and checked before using this as
a completed result. No Kummer-class value is claimed by this draft.

Relevant duplicate/failure checks: L046 and its original attempt prove
only one realized scalar and the different five-isogeny image equality;
ATTEMPTS/014 therefore does not settle this two-descent target.
ATTEMPTS/037 parks a class-group backend required by a different route.
History 261 confirms the unrestricted ramified arithmetic audit, whose
2048-class list does not answer this correlated restriction. All prior
work is preserved. No cross-notebook input or new literature is used.

Further reasoning saved: put kappa=64-theta, a square since it is the
Kummer value at the order-five point 3T. The ramified point has
x=16+z, v_J(z)=3m, so v_J(4z/kappa)=22+3m. For n>=2 this is
at least 70>66, giving identity. For n=1 it is 37, odd and below
66, giving a nonsquare by L078. Writing beta=2^m s, the normalized
Hensel polynomial is

    Q_beta(W)=[2^m A(pi^m W)+beta Jbar(pi^m W)-beta^2 W^11]
              /[2^m A(0)+beta Jbar(0)],

where A(z)=h(16+z)^3. Coefficient differences for two odd betas
are divisible by 2; unit derivatives force root differences in
pi^11 O_H, hence z differences in pi^(m+11). At m=5 this gives
relative square precision 70>66, so all unit parts give one class.
For beta=1, its root is 1+pi^5 modulo pi^10: Jbar's constant and
linear coefficients are odd. Therefore an explicit representative is
64+4pi^5+4pi^10-theta, with relative precision 67>66.
The rational component has infinity parameter valuation m>=5;
L081's implicit identity gives a square-neighborhood bound 6m-2>=28
in the rational cubic, exceeding its threshold 6. Both valuations
n=1,2 have actual nonzero scalar and primitive whole-fiber witnesses.
These claims will be checked and written fully in the canonical proof;
no enumeration or global conclusion is needed.

## Completed bounded attempt

The full proof is now canonical in
[L082](../lemmas/L082-primitive-dyadic-two-descent-image.md). The uniform
fiber milestone extended to the exact two-element correlated set;
the explicit second class needs no numerical root or 34-bit label to
specify it. All square precision bounds and both finite-scalar
realizations are proved there. No mathematical script was run. The
result is REPRODUCTION/ADVANCE within the prior SPECIALIZE scope,
with separate critical audit still required. Global filtering and
integer lifting remain outside this completed attempt.
