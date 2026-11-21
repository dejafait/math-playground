# Corollary C030p: a uniform two-real-part orbital response bound

## Hypotheses

Let n>=4 be a finite integer, a_1,a_2,r,x>0, and b_1,b_2 real.
Assume x*(|b_1|+|b_2|)<=1/4. Set

    D_b=diag(a_1+i*b_1,a_1-i*b_1,a_2+i*b_2,a_2-i*b_2,r,...,r),
    D_0=diag(a_1,a_1,a_2,a_2,r,...,r),
    B=diag(b_1,-b_1,b_2,-b_2,0,...,0),
    A=|b_1|+|b_2|, M=b_1^2+b_2^2.

For each j=0,...,n, let P_j be a rank-j orthogonal projection on C^n.
All integrals use probability Haar measure on U(n). Define

    Z_(j,b)(t)=integral exp(-t*tr(D_b*V*P_j*V*))dV,
    G_(j,b)(t)=-Z'_(j,b)(t)/Z_(j,b)(t),
    E_k(x)=(G_(k+1,b)(x)-G_(k,b)(x))
                  -(G_(k+1,0)(x)-G_(k,0)(x)), 0<=k<n.

Every derivative fixes all entries of D_b. Every rank and reference
has its own normalizer. When n=4 there are no entries r. Coincident
real parts, either sign of every real contrast or phase, zero phases,
repeated projection spectra and adjacent endpoint ranks are included.

The mathematical input is the full real tilted-array comparison proved
in C030l: weak coordinatewise ordered top rows, arbitrary fixed real
fields on proper nested-corner traces, continuous increasing tests and
separate normalizers. Its scalar rank-mean bound alone would not suffice.
The source qualifications for that input appear below. No stochastic
order for a complex measure or independence of disjoint corners is used.

## Conclusion

On the entire stated closed phase window, each Z_(j,b)(x) is positive
real, and

    Z_(j,b)(x)/Z_(j,0)(x) >= 31/32,
    |G_(j,b)(x)-G_(j,0)(x)| <= (640/31)*x*M.          (1)

Consequently the approved target has the absolute constant

    |E_k(x)| <= (1280/31)*x*(b_1^2+b_2^2).           (2)

These constants are independent of n,a_1,a_2,r and all real contrasts.
At j=0,n the individual response in (1) is zero, so 640/31 suffices
in (2) for k=0,n-1. No sharpness is claimed. C030o retains its smaller
constant in its common-real-part scope; it is a comparison, not an input.

This is bounded attempt1218 under the prior EXPLORE assessment1216 and
source comparison1217. Independent conceptual audit1220, under the
separately approved assessment1218/review1219, passes the full stated
claim with unchanged hypotheses and constants. Audit1220 is REPRODUCTION
of this local proof, not a result beyond it. POTENTIALLY_NEW described
only the original search comparison, not certified originality.
This is not a complete RH candidate. The actual-Xi phase and degree/time
budgets, finite-reference and signed-complement hypotheses, all-degree
positivity, theta signing and graph realization remain unresolved.

## Proof

### Reality, positivity and the actual physical derivative

Fix j and write Q=V*P_j*V*, R=tr(B*Q), and L=tr(D_0*Q).
Thus Q is Hermitian, 0<=Q<=I, and tr(D_b*Q)=L+i*R. Both L and R
are bounded real functions of V. The permutation simultaneously swapping
coordinates 1,2 and 3,4 commutes with D_0 and conjugates B to -B.
Conjugating Q by it preserves the Haar orbital law and L, and changes
R to -R. This remains true when phases vanish or have either sign.

Since Z_(j,0)(t)>0 for real t, the ratio is, for all t>0,

    F_j(t):=Z_(j,b)(t)/Z_(j,0)(t)
          = integral exp(-t*L)*cos(t*R)dV
                          / integral exp(-t*L)dV.                 (3)

The sine integral vanishes by the preceding symmetry. Also

    R=b_1*(Q_11-Q_22)+b_2*(Q_33-Q_44),
    |R|<=A,                                                     (4)

because every Q_ll lies in [0,1]. Applying cos(v)>=1-v^2/2 pointwise
in the positive real reference law gives

    F_j(t)>=1-t^2*A^2/2>=31/32  when t*A<=1/4.                    (5)

The bound includes the closed boundary. Multiplying by Z_(j,0)(t)>0
proves that the complex partition function itself is positive real there.

For fixed matrix entries, L and R are bounded and every derivative of
the integrands in (3) is bounded uniformly on compact t intervals.
Differentiation under Haar integration is therefore valid. The positive
reference denominator makes F_j real and smooth for all t>0. At every
point of the closed window, (5) and continuity provide a positive real
neighborhood, so the logarithmic responses are well defined. In
particular the exact identity to be bounded is

    G_(j,b)(x)-G_(j,0)(x)=-F_j'(x)/F_j(x).                        (6)

For clarity about this derivative, let E_t and Cov_t denote expectation
and covariance under density exp(-t*L)/Z_(j,0)(t). Directly differentiating
(3) gives

    F_j'(t)=-E_t[R*sin(t*R)]-Cov_t(L,cos(t*R)).                    (7)

The argument below bounds the full expression, including the covariance.
It does not freeze the real tilt or claim the covariance vanishes.

### Fixed real fields on one nested array

Use the scaled real orbit Y=t*Q. Let z_l^(s), 1<=l<=s<=n, be the
increasingly ordered eigenvalues of its leading s-by-s corner, and
S_s=sum_l z_l^(s). The top row is

    lambda_j(t)=(0^(n-j),t^j).

For n>4 the real exponent telescopes as

    tr(D_0*Y)=r*S_n+(a_1-a_2)*S_2+(a_2-r)*S_4.                   (8)

For n=4 it is instead

    tr(D_0*Y)=a_2*S_4+(a_1-a_2)*S_2.                            (9)

On each fixed orbit S_n=t*j is constant. Removing its exponential
factor within that orbit's own normalization, the array law nu_t is
precisely the fixed-field law in C030l with

    c_2=a_2-a_1, c_4=r-a_2, other c_s=0,       if n>4;
    c_2=a_2-a_1, other proper c_s=0,            if n=4.            (10)

These fields are independent of t. In particular no fictitious proper
row 4 is introduced when n=4, and no sign restriction on the fields is
needed. Equations (8)-(10) identify the entire real reference law, not
only a marginal or an untilted coupling.

Writing diagonal entries as Y_ss=S_s-S_(s-1) gives the full imaginary
phase as the following function of this same nested array:

    T(z)=tr(B*Y)=sum_(s=1)^4 d_s*S_s,
    (d_1,d_2,d_3,d_4)=(2*b_1,-b_1-b_2,2*b_2,-b_2).              (11)

Hence (3) is exactly F_j(t)=E_(nu_t) cos(T(z)). The fourth row in (11)
is the fixed top row when n=4. This uses the whole phase; no factorization
into disjoint-corner laws is asserted.

### The full-array order and its translation normalization

C030l states its comparison for continuous increasing tests of the
proper rows. It also permits a test Phi(z,lambda) increasing in the
proper rows z and the top row lambda. Indeed, for ordered boundaries
lambda<=mu, pointwise monotonicity and then C030l with the fixed test
Phi(.,mu) give

    E_(lambda,c) Phi(z,lambda)
       <= E_(lambda,c) Phi(z,mu)
       <= E_(mu,c) Phi(z,mu).                                  (12)

The tests below are defined continuously on the full coordinate space,
so the intermediate evaluation does not require (z,mu) to interlace.
Each relevant orbit is compact and the integrands are bounded on it.
Thus (12) includes tests of row 4 at n=4 without a new orbital theorem.

For eta>0, the top rows obey

    lambda_j(t)<=lambda_j(t+eta)<=lambda_j(t)+eta*(1,...,1).

The fields (10) are identical in all three comparisons. The tilted
law for the third boundary is the translation of nu_t by eta in
every corner eigenvalue. To see the normalization explicitly, adding
eta*I to Y adds s*eta to S_s, so its proper-row weight is multiplied
by the constant exp(eta*sum_(s<n) s*c_s). That same constant multiplies
its own normalizer and cancels. Haar orbit translation gives the claimed
translated probability law. Different t or rank normalizers were not
equated. C030l and (12) therefore give, for increasing full-array tests,

    nu_t <= nu_(t+eta) <= translation_eta(nu_t).                 (13)

The notation means expectation inequalities, with no simultaneous
matrix coupling assumed. Apply (13) to individual coordinates in
rows 1,...,4, including the deterministic top row if n=4. If Delta
denotes expectation at t+eta minus expectation at t, then

    0<=Delta E z_l^(s)<=eta,
    0<=Delta E S_s<=s*eta,  s=1,...,4.                          (14)

This remains valid for j=0,n and for weak/repeated top rows, which are
within C030l's proved scope.

### A monotone correction for the whole phase

Put

    K=sum_(s=1)^4 s*|d_s|,
    H(z)=sum_(s=1)^4 |d_s|*S_s,
    U=t+eta, tau=U*A.

Let clip_tau(v)=max(-tau,min(tau,v)) and h_U(v)=cos(clip_tau(v)).
On [-tau,tau], |(cos v)'|=|sin v|<=tau. Since clipping is
1-Lipschitz and takes values in this interval, h_U is globally
tau-Lipschitz, also when tau=0. Define on the full array space

    Psi_+(z)= h_U(T(z))+tau*H(z),
    Psi_-(z)=-h_U(T(z))+tau*H(z).                               (15)

Both tests are continuous and coordinatewise increasing. In fact,
increasing z_l^(s) by h>=0 changes T by d_s*h and H by |d_s|*h.
The change in either signed h_U term is at least -tau*|d_s|*h,
which the change in tau*H cancels. Coordinates outside rows 1,...,4
do not occur. This proof works at clipping boundaries and requires
neither differentiable eigenvalue paths nor monotonicity of cosine.

Every Y in the actual supports at times t and U satisfies 0<=Y<=U*I.
The diagonal-entry estimate (4), now for Y, gives |T(z)|<=U*A=tau.
Consequently h_U(T(z))=cos(T(z)) on both supports. Apply the lower
comparison in (13) to both tests (15). Using (14) and nonnegative
coefficients in H, one obtains

    |F_j(t+eta)-F_j(t)|
        <=tau*Delta E H
        <=U*A*K*eta.                                           (16)

The full physical dependence of the law nu_t is present in (16).
Smoothness was already justified using the original fixed-Haar
quotient (3). Divide (16) by eta and let eta decrease to zero:

    |F_j'(t)|<=t*A*K,  t>0.                                    (17)

No phase-window condition was used in (16)-(17). Thus the right
difference quotients are legitimate at the closed phase-window
endpoint; positivity outside that window was not assumed.

### Absolute constant and all exceptional cases

Write u=|b_1|, v=|b_2|. Formula (11) gives

    K=2*u+2*|b_1+b_2|+10*v<=4*u+12*v,
    A*K<=(u+v)*(4*u+12*v)
        =4*u^2+16*u*v+12*v^2
        <=12*u^2+20*v^2<=20*(u^2+v^2)=20*M.                    (18)

The penultimate inequality is 16*u*v<=8*(u^2+v^2). Combining
(5)-(6), (17) and (18) proves the per-rank bound in (1):

    |G_(j,b)(x)-G_(j,0)(x)|
       <=(32/31)*x*A*K<=(640/31)*x*M.

The triangle inequality for the two separately normalized ranks gives
(2). At rank zero Q=0. At rank n Q=I and tr(B)=0, so F_0=F_n=1
and both responses vanish exactly. If b_1=b_2=0 then A=K=0 and
F_j=1 at every rank. No division by A, K, M, either phase or any real
contrast was made. The n=4 case was treated with only proper field c_2
and with the top-row test extension (12). All signs and coincidences
of a_1,a_2,r remain allowed by the real comparison. This completes
the stated bound. The independent audit below retains all these cases.

### Source and downstream qualifications

C030l proves the weak-row fixed-field comparison used here. Its named
orbital-law input is G. Olshanski, *Projections of Orbital Measures,
Gelfand-Tsetlin Polytopes, and Splines*, J. Lie Theory 23 (2013),
1011-1022, [Corollary 3.2, p1017, with Proposition 3.1/(10), pp1015-16](https://www.heldermann-verlag.de/jlt/jlt23/olshla2e.pdf).
That source identifies the uniform interlacing-array law for a strict
real top row; C030l supplies the separately normalized comparison and
the repeated-boundary extension. Its cited real comparison source is
S. Sra, *On some positivity properties of the Riemann Xi function*,
[author v3, 2 November 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
Lemma C.7 and Theorem C.8, printed pp25-27, equations (C.14)-(C.16).
The inspected source and scope records1213/1217 are reused. No general
orbital theorem is reproved or claimed independently reaudited here.

The new work needed for this exact target is the phase representation
(11), the full-array test qualification (12), and the monotone clipped
phase estimate (15)-(18). The Haar moment formula, conditional
independence, a complex-law order and a common normalizer are not inputs.
C030n/o remain scope/constant comparisons only. The proof asserts only
the displayed two-pair/common-background target; no further extension
or actual-Xi realization is being certified by this step. The finite
reference and signed remainder conditions, actual degree/time budgets,
L030-L032/C032a all-degree signs and graph realization remain unpaid.

### Independent conceptual audit1220

17 November 2026. The approved audit checks the entire finite-family
claim, relative to C030l's full real comparison and its cited orbital
law. It neither independently reproves Olshanski's theorem nor replaces
the weak-row comparison by its scalar rank consequence. The strict-row
source and C030l's local singular-boundary extension remain distinct.
No new external input, numerical certificate or extra local lemma is
needed. The following checks retain (1)-(2) without repair.

**Real law, phase and differentiation.** For each fixed rank, simultaneous
pair swaps preserve D_0 and send B to -B, including when one phase is
zero or the phases have opposite signs. Consequently the sine integral
is zero for every real t, not only in the window. Each Q_ll belongs
to [0,1], so |R|<=A; the lower bound 1-(t*A)^2/2 is pointwise under
the positive real law. At t*A=1/4 it is exactly 31/32. The real reference
partition function is strictly positive, and continuity gives a real
open neighborhood with F_j>0 at each point of the closed window.

For fixed entries and finite n, |L| and |R| are finite; their sizes may
depend on the real contrasts. This is sufficient for compact-interval
domination when differentiating the fixed-Haar quotient. It does not
assert a contrast-uniform bound at this stage. The quotient rule gives
exactly -E_t[R*sin(t*R)]-E_t[L*cos(t*R)]+E_t[L]*E_t[cos(t*R)],
which is (7). Likewise differentiating Z_b=F_j*Z_0 gives (6). Thus a
bound for the derivative of this quotient controls the full physical
response; there is no missing derivative of the reference tilt.

The diagonal identity Y_ss=S_s-S_(s-1) verifies (8)-(11) term by term.
For n>4, the coefficient of S_2 in -tr(D_0*Y) is a_2-a_1 and that of
S_4 is r-a_2. For n=4 only S_2 is a proper field; -a_2*S_4 is constant
on the orbit. These constants cancel within each probability law and
are never identified between times or ranks. The four phase coefficients
are respectively b_1-(-b_1), -b_1-b_2, b_2-(-b_2), and -b_2.
This identifies the full phase without a conditional-independence claim.

**Full-array order, deterministic top row and translation.** In (12),
Phi(z,lambda)<=Phi(z,mu) is valid even if (z,mu) is not an interlacing
array, because Phi is defined and increasing on the full product
coordinate space. For fixed mu the function Phi(.,mu) is an admissible
continuous increasing test for C030l. The supports are compact; bounded
test expectations suffice, so global unboundedness of the added linear
term causes no integration difficulty. This also verifies row4 when
n=4: it is a deterministic boundary variable in the first inequality,
not a fictitious proper corner in the second.

For every j, the ordered top-row inequalities in (13) hold coordinate
by coordinate, including j=0,n. Under addition of eta*I, every corner
eigenvalue increases by eta and S_s increases by s*eta. The proper-field
weight therefore acquires exp(eta*sum_(s<n)s*c_s). The translated law's
own normalizing integral acquires the identical factor. This proves the
upper comparison with a translated normalized law, for all signs of c_s;
no equality between the original and changed normalizers is needed.
Applying the two comparisons to each coordinate gives (14), including
the top-row coordinates. Weak projection spectra are explicitly within
C030l's continuity extension, not within a claimed full-dimensional
Lebesgue density for a collapsed polytope.

**Clipping and the full difference quotient.** The clipped cosine is
globally tau-Lipschitz since its unclipped derivative on [-tau,tau]
has modulus at most tau and clipping is 1-Lipschitz. This remains true
at tau=0. A change h>=0 in any coordinate from row s<=4 changes T by
d_s*h and H by |d_s|*h. Hence either signed clipped cosine plus tau*H
changes by at least zero. The tests are continuous and increasing on
the full coordinate space, not merely along admissible array paths.

At the physical times t and U=t+eta, the supports satisfy 0<=Y<=U*I,
so |T|<=U*A and the clipped test equals the actual cosine there. Write
Delta F=F_j(U)-F_j(t) and Delta H=E_(nu_U)H-E_(nu_t)H.
The lower comparison gives both
Delta F+tau*Delta H>=0 and -Delta F+tau*Delta H>=0.
The upper comparison and the nonnegative coefficients of H give
0<=Delta H<=K*eta. Thus |F_j(U)-F_j(t)|<=U*A*K*eta, exactly (16).
Removing clipping on the translated support is not required: the upper
comparison is used for linear coordinates/H. No simultaneous coupling
or differentiation of an eigenvalue path is used.

For every t>0, division by eta and eta decreasing to zero now gives
|F_j'(t)|<=t*A*K, because the full fixed-Haar quotient was already shown
smooth. In particular this argument remains valid at t*A=1/4: it does
not need a logarithm or positivity at t+eta outside the specified window.
Only (6) at the target t uses the positive denominator.

**Constant and degeneracies.** Direct evaluation gives
K=2*u+2*|b_1+b_2|+10*v<=4*u+12*v. The elementary inequality
16*u*v<=8*u^2+8*v^2 yields A*K<=12*u^2+20*v^2<=20*M.
Multiplication by 32/31 gives 640/31 per rank, and the triangle
inequality gives 1280/31 for two adjacent ranks with their own
normalizers. At rank0, Q=0; at rank n, Q=I and tr(B)=0. Thus both
endpoint responses vanish identically, proving the stated improvement
at k=0,n-1. When both phases vanish all responses vanish; with exactly
one zero phase no formula divides by that phase. No step divides by a
real contrast, so coincident real parts and every contrast sign are
included. The preceding top-row check covers n=4 at all ranks.

Audit verdict: the full stated bound and positive-real floor pass.
This validates one previously pending finite perturbation input. It
does not improve the constant, establish originality, extend the pair
count or background family, or pay actual-Xi reference, signed-complement,
degree/time, all-degree positivity, theta-signing or realization gaps.
The sole direct mathematical input remains C030l; C030n/o remain
comparisons. No dependency change is made.

## Mathlib

Full matching coverage of (1)-(2), the tilted orbital comparison and
its orbital-law input is unchecked; no absence claim is made. Haar
invariance, bounded differentiation, clipping/Lipschitz estimates and
finite coordinate monotonicity are supporting mathematics. Matching
formal theorem names for those ingredients were not checked, and no
formalization is claimed.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
