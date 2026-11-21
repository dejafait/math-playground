# Lemma 934: vanishing fixed-bump projection onto the joint two-shift span

## Hypotheses

Use L637's actual real Hardy function Z, with
Z(t)=exp(i theta(t)) zeta(1/2+it) on the real axis. Fix
w>=0 in C_c^infinity((0,1)), integral w=1, and u0 in (0,1)
with w(u0)>0. Fix precisely

    psi(x)=exp(-1/(1-4x^2)) for |x|<1/2, and zero otherwise.

For T tending to infinity set

    L=log T, N=floor(T^(1/5)), T<=X<=2T, a=X+u0*T,
    w_XT(t)=w((t-X)/T),
    <f,h>_T=integral w_XT(t) f(t) conjugate(h(t)) dt,
    g(t)=psi(L(t-a))/||psi(L(.-a))||_T,
    P_s(t)=sum_(n<=N)c_(s,n)n^(-it), s in {-1,+1},
    U_c(t)=sum_(s=+/-1)Z(t+s/L)P_s(t),
    S=sum_(s=+/-1)sum_(n<=N)|c_(s,n)|^2,
    V=span_C{Z(t+s/L)n^(-it):s=-1,+1, 1<=n<=N}.

The inner product is linear in its first slot. Let Pi be the orthogonal
projection onto V in L2(w_XT dt), interpreted as equivalence classes
where w vanishes. Both coefficient vectors may depend arbitrarily on
T and X. All constants and onsets below are independent of X and the
vectors, with dependence only on the fixed data and imported constants.

Use the stronger first inequality of audited L933(4): for this exact
joint dictionary, some fixed c0>0 and a uniform onset give

    ||U_c||_T^2 >= c0 T N^(-1/8) S.                       (1)

Only this actual norm conclusion is used, not an unproved normalized
cross-term contraction. Reuse L927 Section 3's local numerator method
and finite-dimensional Hilbert projection argument. Its single-span
projection conclusion is not used to bound the joint span.

The analytic import for the numerator is the undifferentiated
real-axis Riemann--Siegel formula: E. C. Titchmarsh, revised by
D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, second
edition (1986), Section 4.17, (4.17.4), p.89; also
[C. Hughes, July 2017 LMS notes, Theorem 2.2, printed pp.18--19](https://personal.maths.manchester.ac.uk/jm/wiki/uploads/LMS/Hughes-lectures.pdf#page=20).
In L637's normalization it states, for all sufficiently large real v,

    Z(v)=2 sum_(j<=floor(sqrt(v/(2*pi)))) j^(-1/2)
             cos(theta(v)-v log j)+O(v^(-1/4)).           (2)

The uniform real-height remainder includes cutoff crossings. The
theorem is imported; its heuristic lecture explanation is not a proof
input. No differentiated remainder or complex-height extension is used.
The invocation-start SPECIALIZE assessment is
drafts/literature/2026-11-09-joint-fixed-bump-projection-26.md,
separately approved in step27. No new source retrieval is needed.

## Conclusion

At one sufficiently-large-T onset, uniformly in T<=X<=2T,

    ||Pi g||_T^2 <= C N^(9/8)/(sqrt(T) L)
                 <= C T^(-11/40)/log T = o(1).            (3)

In particular,

    inf_(U in V)||g-U||_T^2
        =1-||Pi g||_T^2 =1-O(T^(-11/40)/log T).          (4)

For every fixed 0<=r<1, eventually no U in V approximates g with
||g-U||_T<=r, simultaneously for all X in [T,2T]. This is an
obstruction for precisely the stated fixed bump and dictionary.
Other lengths, shift sets, bumps, signed weighted approximation,
signed transfer and actual-Xi all-degree mixed positivity remain open.

This is a source-covered specialization, classified REPRODUCTION.
It combines an audited local denominator with the already assessed
elementary numerator/projection method; it is not a new moment theorem
or certified advance beyond all literature. Written 9 November 2026,
step28. The separate application audit below passed on 9 November 2026,
step30, under the stated imports, without changing the bound. It is not
an RH candidate.

## Proof

### 1. Normalization and the two translated heights

Continuity and w(u0)>0 give delta>0 for which
w(u)>=w(u0)/2 whenever |u-u0|<=delta. For T sufficiently large,
1/(2TL)<=delta. Thus w_XT is positive throughout the interior of

    I=[a-1/(2L),a+1/(2L)],

where psi(L(t-a)) is positive. The bump has strictly positive norm
and ||g||_T=1. Weighted Cauchy--Schwarz on its support gives

    integral w_XT(t)|g(t)| dt
       <= (integral_I w_XT(t) dt)^(1/2)
       <= sqrt(||w||_infinity/L).                        (5)

For t in I and s=-1,+1, the translated height v=t+s/L differs
from a by at most 3/(2L). Since T<=a<=3T, both heights lie in
[T/2,4T] eventually, uniformly in X. Formula (2) applies at every
such height. The elementary integral comparison

    sum_(j<=M) j^(-1/2) <= 2 sqrt(M)  (M>=1)

and |cos|<=1 give

    sup_(t in I, s=-1,+1)|Z(t+s/L)| <= C1 T^(1/4).      (6)

The O(T^(-1/4)) remainder is absorbed in this bound. The floor cutoff
is retained, so this argument holds at its crossings and at zeros.
Neither Z, the weight nor g is translated elsewhere in the proof.

### 2. Full two-channel correlation estimate

For every t, finite Cauchy--Schwarz over all 2N coefficients gives

    |U_c(t)|
       <= sqrt(S) [sum_(s=+/-1)sum_(n<=N)|Z(t+s/L)|^2]^(1/2).

In particular (6) bounds this by C1 sqrt(2N) T^(1/4) sqrt(S)
on I. Since g vanishes outside I, (5) therefore proves

    |<g,U_c>_T|^2 <= C2 N T^(1/2) S/L.                  (7)

This charges both channels before taking any supremum. It does not
add separate projection estimates or assume a bound on either vector.
All constants in (7) are uniform for arbitrary moving complex pairs.

### 3. The entire projection supremum and a common onset

Take the maximum of the finitely many onsets for the imported bound
(1), bump positivity, the comparable-height inclusion, (2), and N>=1.
This maximum depends only on the fixed data and imported constants.
For S>0, (1) shows ||U_c||_T>0. For S=0, U_c=0 and (7) is
immediate. Thus every nonzero coefficient vector represents a
nonzero element of V at this common onset.

The finite span V is closed. Orthogonality and Cauchy--Schwarz give
the standard variational identity, as in L927 Section 3,

    ||Pi g||_T^2
       =sup_(0!=U in V)|<g,U>_T|^2/||U||_T^2.           (8)

Indeed <g,U>_T=<Pi g,U>_T for U in V. If Pi g=0, all
pairings vanish; otherwise U=Pi g attains the upper bound supplied
by Cauchy--Schwarz. Each U is represented by a coefficient pair.
Divide the coefficient-uniform (7) by (1), for every S>0, to obtain

    |<g,U_c>_T|^2/||U_c||_T^2
       <= (C2/c0) N^(9/8) T^(-1/2) L^(-1).              (9)

Taking the full supremum in (8) is legitimate because (9) already
holds uniformly for every vector and X. Since N<=T^(1/5),

    (1/5)(9/8)-1/2=9/40-20/40=-11/40.

This proves (3), which tends to zero uniformly. Pythagoras gives
the exact identity in (4). For fixed r<1, increase the onset until
C T^(-11/40)/log T<1-r^2; the minimum squared error then exceeds
r^2 for every X, proving the stated exclusion.

No infinite-span limit, unproved Gram inverse or nonuniform interchange
is used. The stronger first bound of L933(4), rather than its weaker
T L N^(-1/4) version, explains the power and single logarithm in (3).
Neither (3) nor (4) asserts anything about a signed |W|-weighted error
or the sign of a Xi observer. Those are separate unresolved gaps.

### Separate application audit — 9 November 2026, step30

This is the first independent application audit of Sections 1--3,
under the invocation-start SPECIALIZE assessment
drafts/literature/2026-11-09-l934-joint-projection-audit-28.md.
It passes. The exact fixed parameters and both independently moving
complex vectors agree with audited L933(4). Only its first inequality
is imported; its arithmetic proof and the primary manuscripts are not
reaudited here. L927 Section 3 supplies the elementary projection
framework, not an upper bound for a sum of subspaces.

**Weighted space and source domain.** Extend w by zero to the real
line. Continuity at u0 gives a fixed delta>0, chosen smaller than
min(u0,1-u0), on which w>=w(u0)/2. For 1/(2TL)<=delta the
nonzero bump has positive weighted norm. Hence ||g||_T=1 exactly,
and weighted Cauchy--Schwarz gives

    (integral w_XT |g|)^2 <= integral_I w_XT
                            <= ||w||_infinity/L.

The center lies between T and 3T and |t+s/L-a|<=3/(2L) on I
for each s=-1,+1. For large T, 3/(2L)<=T/2, so the lower
height is at least T/2 and the upper at most 7T/2<4T.
Both heights exceed the same real-axis source onset once T/2 does.
In (2), the cutoff M is O(sqrt(T)); the complete absolute sum
2 sum_(j<=M) j^(-1/2)<=4 sqrt(M), together with the uniform
O(T^(-1/4)) remainder, proves (6). No separation from zeros or
cutoff crossings, differentiated remainder or shifted weight is used.
All dictionary functions belong to this weighted L2 space since they
are continuous on its compact support.

**Simultaneous correlation and division.** On I the squared Euclidean
norm of the complete 2N-entry dictionary row is at most
2 C1^2 N T^(1/2), since |n^(-it)|=1 for real t. Thus finite
Cauchy--Schwarz, followed by the preceding weighted support bound,
gives, for every coefficient pair before any supremum,

    |<g,U_c>_T|^2 <= 2 C1^2 ||w||_infinity
                         N T^(1/2) S/L.

This estimate includes complex conjugation in the linear-first-slot
inner product through absolute values. Dividing by
c0 T N^(-1/8) S for S>0 gives exactly
C N^(9/8)/(sqrt(T)L), with no further logarithmic loss. For S=0
the represented vector and pairing vanish. For S>0 the imported lower
bound excludes a zero equivalence class, even if w vanishes elsewhere.

**Full supremum, exponent and onset.** The finite span is closed in
L2(w_XT dt). Orthogonality gives <g,U>=<Pi g,U> for U in V;
Cauchy--Schwarz bounds its variational quotient by ||Pi g||^2,
with equality at U=Pi g when nonzero. If Pi g=0 every quotient
vanishes. Each U has a coefficient representation, so the simultaneous
bound above controls the entire supremum, including pairs selected
after T and X. There is no addition of separate projection bounds.
The floor satisfies N<=T^(1/5), and
9/40-1/2=-11/40. Thus (3) follows with precisely the single factor
1/log T. Take the maximum of the fixed-data onsets for the imported
denominator, bump positivity, height inclusion, real-axis source and
N>=1. Each is independent of X and coefficients, so the maximum is
also uniform. For each fixed r<1, the further requirement
C T^(-11/40)/log T<1-r^2 has its own uniform eventual onset.
Pythagoras then proves (4) and the strict exclusion at tolerance r.

No load-bearing error was found, and no effective numerical onset or
stronger scope was obtained. Retain the exact unsigned realization
stop. Signed weighted transfer, other dictionaries and actual-Xi
all-degree mixed positivity remain unpaid; this audit supplies no
progress beyond the asserted source-covered specialization.

## Mathlib

Full matching coverage for this joint projection theorem and the
Riemann--Siegel/coercivity inputs has not been checked and remains
unknown. Finite Cauchy--Schwarz, Hilbert orthogonal projection and
Pythagoras are supporting mathematics, not a checked matching theorem
for this full specialization. No absence or formal-verification claim
is made.
