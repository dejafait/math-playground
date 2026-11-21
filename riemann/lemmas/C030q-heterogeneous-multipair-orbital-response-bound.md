# Corollary C030q: a uniform heterogeneous multipair orbital response bound

## Hypotheses

Let m>=1 and n>=2m be finite integers. Let a_1,...,a_m,r,x>0 and
b_1,...,b_m be real, with x*sum_l |b_l|<=1/4. Put

    D_b=diag(a_1+i*b_1,a_1-i*b_1,...,a_m+i*b_m,a_m-i*b_m,r,...,r),
    D_0=diag(a_1,a_1,...,a_m,a_m,r,...,r),
    B=diag(b_1,-b_1,...,b_m,-b_m,0,...,0),
    A=sum_l |b_l|, M=sum_l b_l^2.

For j=0,...,n let P_j be any rank-j orthogonal projection on C^n.
All unitary integrals use probability Haar measure on U(n). Define

    Z_(j,b)(t)=integral exp(-t*tr(D_b*V*P_j*V*))dV,
    G_(j,b)(t)=-Z'_(j,b)(t)/Z_(j,b)(t),
    E_k(x)=(G_(k+1,b)(x)-G_(k,b)(x))
                   -(G_(k+1,0)(x)-G_(k,0)(x)), 0<=k<n.

All entries of D_b are fixed under differentiation. Each rank and
reference has its own normalizer. The case n=2m has no r entries.
Zero phases, coincident real parts, either sign of every real contrast,
repeated projection spectra, and adjacent endpoint ranks are included.

Use the full real tilted-array comparison established in C030l: weak
coordinatewise ordered real top rows, arbitrary fixed real fields on
proper nested-corner traces, continuous increasing tests, and separately
normalized laws. Its scalar rank-mean consequence alone is insufficient.
The precise source and specialization qualifications are given below.

## Conclusion

Every Z_(j,b)(x) is positive real on the entire closed phase window, and

    Z_(j,b)(x)/Z_(j,0)(x) >= 31/32,
    |G_(j,b)(x)-G_(j,0)(x)| <= (4224/961)*x*M.             (1)

In particular the approved target holds with an absolute constant:

    |E_k(x)| <= (8448/961)*x*sum_l b_l^2
              <= 9*x*sum_l b_l^2.                        (2)

The constants are independent of m,n and all real parts. At j=0,n the
individual response is zero; hence 4224/961 suffices in (2) at k=0,n-1.
No sharpness is asserted. C030o's smaller constant remains applicable
within its common-real-part scope; C030p is the two-pair comparison.
Neither is a mathematical input to this proof.

This is bounded attempt1222 under the prior EXPLORE assessment1220 and
source comparison1221, reusing1213/1217. Independent conceptual audit1224,
under assessment1222/review1223, passes the stated claim with unchanged
hypotheses and constants; its full checks appear below. The audit is
REPRODUCTION of this local proof. POTENTIALLY_NEW described only the
original source comparison, not certified originality. This finite
perturbation estimate is not a complete RH candidate. Actual-Xi phase
and degree/time budgets, finite-reference and signed-complement inputs,
all-degree positivity, theta signing and graph realization remain open.

## Proof

### Reality, the positive floor and the physical derivative

Fix j. Write Q=V*P_j*V*, L=tr(D_0*Q), and R=tr(B*Q). These are bounded
real observables for the fixed finite matrices, with 0<=Q<=I. Let E_t
denote expectation under the positive probability law proportional to
exp(-t*L)dV. The real reference normalizer is strictly positive for
every real t. The simultaneous swap of the two coordinates in every
pair preserves D_0 and changes B to -B. Haar invariance therefore gives

    F_j(t):=Z_(j,b)(t)/Z_(j,0)(t)=E_t cos(t*R).           (3)

Every Q_ii is in [0,1], so

    |R|=|sum_l b_l*(Q_(2l-1,2l-1)-Q_(2l,2l))|<=A.

The elementary inequality cos(v)>=1-v^2/2 now gives

    F_j(t)>=1-t^2*A^2/2>=31/32,  t>0, t*A<=1/4.         (4)

Thus Z_(j,b)(t)=Z_(j,0)(t)*F_j(t) is positive real in this window,
including its boundary. For fixed entries, the integrands and all their
derivatives are bounded on every compact real t interval. Differentiation
under the Haar integral and the quotient rule are justified by those
bounds. In particular F_j is real and smooth for all real t, and

    F_j'(t)=-E_t[R*sin(t*R)]-Cov_t(L,cos(t*R)).           (5)

Continuity and (4) give a neighborhood with F_j>0 at every point of the
closed window. At such a point the full physical response is

    G_(j,b)(t)-G_(j,0)(t)=-F_j'(t)/F_j(t).               (6)

We bound this full derivative, including the covariance in (5).

### Pair symmetry and the series to be differentiated

Put Y=t*Q and delta_l(Y)=Y_(2l-1,2l-1)-Y_(2l,2l). Each individual pair
swap preserves the real weight and changes only that delta_l's sign.
Average the integrand exp(-i*sum_l b_l*delta_l) over the finite group of
all 2^m pair swaps. Its average is product_l cos(b_l*delta_l). Thus

    F_j(t)=E_t product_l cos(b_l*delta_l(t*Q)).           (7)

This is a symmetry identity; the delta_l are not assumed independent.
For h=(h_1,...,h_m) in N_0^m, define s=|h|=sum_l h_l and

    c_h=product_l b_l^(2h_l)/(2h_l)!,
    M_h(t)=E_t product_(l:h_l>0) delta_l(t*Q)^(2h_l).

Use c_0=1, M_0=1, including the convention b_l^0=1 when b_l=0.
Expanding the cosines gives

    F_j(t)=sum_h (-1)^|h| c_h M_h(t).                   (8)

For 0<t<=T, |delta_l(t*Q)|<=T and 0<=M_h(t)<=T^(2s).
All c_h are nonnegative. The inequality (2h)!>=2^h*h!, valid also
at h=0, and the finite multinomial theorem imply

    sum_(|h|=s) c_h <= (M/2)^s/s!.                     (9)

Consequently the absolute sum of the integrands in (8), uniformly for
0<t<=T and all Q, is at most exp(T^2*M/2). This justifies expansion and
integration. Termwise differentiation will require the next estimate.

### A fixed-degree moment uses only finitely many initial rows

Take h with s>=1, and let p be the number of positive h_l, so 1<=p<=s
and p<=m. For this one scalar moment, simultaneously permute the involved
coordinate pairs to positions 1,...,2p, and relabel their positive
exponents h_1,...,h_p. Permute D_0 and Q in the same way. Haar invariance
identifies the resulting expectation with the original M_h(t). The
remaining real rates are retained, in any fixed order. This permutation
can differ for different h, but it is independent of t for each h.
We do not identify joint couplings for different h or different pair
orders.

Let q_1,...,q_n be the resulting real diagonal of D_0. For the scaled
orbit Y=t*Q, let z_i^(v), 1<=i<=v<=n, be the increasingly ordered
eigenvalues of its leading v-corner and let S_v=sum_i z_i^(v), S_0=0.
The weak top row is lambda_j(t)=(0^(n-j),t^j). Telescoping diagonals gives

    tr(D_0*Y)=q_n*S_n+sum_(v<n)(q_v-q_(v+1))*S_v.        (10)

The term q_n*S_n=q_n*t*j is constant on that orbit and cancels within
its own normalized real law. Hence its full array law nu_t is the law
in C030l with fixed real proper-row fields

    c_v=q_(v+1)-q_v, v<n.                              (11)

These fields are independent of t, with no restriction on their signs.
Every real rate, including those outside the selected pairs, is included
in (10). No real tilt is frozen during a physical derivative.

The active pair differences on this array are

    d_l(z)=2*S_(2l-1)-S_(2l-2)-S_(2l), 1<=l<=p.        (12)

Indeed Y_ii=S_i-S_(i-1). Thus M_h(t)=E_(nu_t) product_l d_l^(2h_l).
When 2p=n, S_(2p) is the deterministic top trace, not a proper row.

### Full-array comparison and normalization under translation

C030l also controls continuous tests Phi(z,lambda) increasing in both
the proper rows and the top row, provided they are defined on the full
coordinate space. For ordered boundaries lambda<=mu, first use
Phi(z,lambda)<=Phi(z,mu) pointwise, then apply C030l with the fixed
proper-row test Phi(.,mu). This proves

    E_(lambda,c) Phi(z,lambda)<=E_(mu,c) Phi(z,mu).       (13)

The intermediate (z,mu) need not interlace, which is why global
definition of the test matters. Every relevant support is compact.

For eta>0, put U=t+eta. Coordinatewise,

    lambda_j(t)<=lambda_j(U)<=lambda_j(t)+eta*(1,...,1).

All three laws use the same fields (11). Translating the top row by eta
translates Y by eta*I and every corner eigenvalue by eta. The proper-row
weight is multiplied by exp(eta*sum_(v<n) v*c_v), a constant. Its own
normalizer is multiplied by the same constant, which cancels. It follows
from C030l and (13) that, for increasing full-array tests,

    nu_t <= nu_U <= translation_eta(nu_t).              (14)

This is an expectation comparison; it asserts no common ordered matrix
coupling. In particular, writing Delta for the difference of expectations
under nu_U and nu_t gives

    0<=Delta E z_i^(v)<=eta,
    0<=Delta E S_v<=v*eta, 1<=v<=n.                    (15)

The top-row case is included by (13), and the weak-boundary comparison
includes j=0,n. No ambient Lebesgue density is assigned to a collapsed
projection polytope.

### A globally increasing correction for each even monomial

For U>0 define clip_U(v)=max(-U,min(U,v)) and, on the full array space,

    g_h(z)=product_(l=1)^p clip_U(d_l(z))^(2h_l),
    H_h(z)=2*U^(2s-1)*sum_(l=1)^p h_l*
                    (2*S_(2l-1)+S_(2l-2)+S_(2l)).      (16)

As a function of its p scalar d arguments, g_h is separately Lipschitz
with constant 2*h_l*U^(2s-1) in argument l. This follows from the
1-Lipschitz clipping map, the power bound
|v^(2h_l)-w^(2h_l)|<=2*h_l*U^(2h_l-1)*|v-w| for v,w in [-U,U],
and the bound U^(2(s-h_l)) for the product of the other factors.
Changing several arguments and telescoping gives the sum of these
individual bounds; no differentiability at clipping endpoints is needed.

Increasing one corner eigenvalue by u>=0 changes each S_v in that
coordinate's row by u. Formula (12) and the preceding Lipschitz bounds
show that the change in either signed g_h is at least the negative of
the change in H_h. Thus both g_h+H_h and -g_h+H_h are continuous
coordinatewise increasing functions on the entire coordinate space.
The argument includes any top-row coordinate occurring in (16).

At times t and U the actual matrices satisfy 0<=Y<=U*I, so |d_l|<=U.
The clipping therefore disappears on both actual supports. Apply the
lower comparison in (14) to these two increasing tests. Then apply (15)
to H_h, whose row coefficients are nonnegative. This yields

    |M_h(U)-M_h(t)| <= Delta E H_h
      <= 2*U^(2s-1)*eta*sum_(l=1)^p h_l*(8l-4).        (17)

The factor 8l-4 is exactly 2*(2l-1)+(2l-2)+2l, the sum of row lengths
with their coefficients in (16). It does not count all m pairs.
Because h_l>=1 and sum h_l=s,

    sum_l l*h_l <= p*(p+1)/2+p*(s-p),
    sum_l h_l*(8l-4)
       <= 8*p*s-4*p*(p-1)-4*s
        =4*s^2-4*(s-p)*(s-p+1) <=4*s^2.               (18)

For each fixed h, M_h(t)=t^(2s) times a normalized Haar expectation of
a bounded polynomial in Q under exp(-t*L). The same compact-interval
domination as for (3) makes it smooth. Divide (17) by eta and let eta
decrease to zero, using (18). We obtain the full derivative bound

    |M_h'(t)|<=8*s^2*t^(2s-1), t>0.                   (19)

It is uniform in m,n,j and all real rates. The difference quotients
vary the whole normalized law nu_t; (19) includes its real-field
response. No phase restriction was needed in this argument.

### Differentiated series, absolute constant and degenerate cases

For any fixed T>0, (9) and (19) imply

    sum_(s>=1) sum_(|h|=s) c_h |M_h'(t)|
       <=sum_(s>=1) 8*s^2*T^(2s-1)*(M/2)^s/s!, 0<t<=T.

The series on the right is finite. Thus the derivative series converges
uniformly on every compact positive t interval. Together with the
uniform convergence already shown for (8), the elementary theorem on
differentiating a uniformly convergent derivative series permits
termwise differentiation. Each term uses its own valid permutation
argument from (10)-(19); the scalar bounds are uniform, so no limit of
permutations, dimension or real contrast is being interchanged.

Put z=t^2*M/2. Summing s^2*z^s/s!=(z+z^2)*exp(z) gives

    |F_j'(t)| <= (8/t)*(z+z^2)*exp(z)
               =4*t*M*(1+z)*exp(z).                  (20)

At the target t=x, M<=A^2 and x*A<=1/4 imply 0<=z<=1/32. For
0<=z<1, the power series comparison exp(z)<=sum_(v>=0)z^v=1/(1-z)
gives

    (1+z)*exp(z)<= (33/32)*(32/31)=33/31,
    |F_j'(x)|<=(132/31)*x*M.                          (21)

Combining (4), (6) and (21) gives (4224/961)*x*M per rank. The triangle
inequality for the two adjacent responses, each with its own normalizer,
gives 8448/961 in (2). Since 8448<9*961=8649, C=9 also suffices.

The derivative bound (20) was established for all t>0 without taking a
logarithm. Therefore the right differences at x*A=1/4 are legitimate
even if x+eta is outside the phase window; only (6) at x uses (4).
For M=0 all b_l vanish, (7) is identically 1 and the responses are zero.
No step divides by a phase, M or a real contrast. At j=0, Q=0; at j=n,
Q=I and every delta_l is zero. Hence F_0=F_n=1 and the endpoint claims
follow. When n=2m, (10) has only its proper fields v<n, and any active
row n in (12) or (16) was handled by (13). No background entry is needed.
Coincidences and either sign of all real contrasts remain allowed by
C030l, completing the proof within the stated family.

### Source, specialization and downstream qualifications

The sole direct local mathematical input is C030l's full weak-row
comparison. Its orbital-law input is G. Olshanski, *Projections of
Orbital Measures, Gelfand-Tsetlin Polytopes, and Splines*, J. Lie Theory
23 (2013), 1011-1022, [Corollary 3.2, p1017, with Proposition 3.1/(10),
pp1015-16](https://www.heldermann-verlag.de/jlt/jlt23/olshla2e.pdf).
The source identifies the full corner-array law for a strict real
top row. C030l supplies the separately normalized comparison and the
continuity extension to weak rows. Its real-comparison source is
S. Sra, *On some positivity properties of the Riemann Xi function*,
[author v3, 2 November 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
Lemma C.7 and Theorem C.8, printed pp25-27, (C.14)-(C.16).
Those general results are imported with the existing scope assessments,
not reproved or independently source-audited in this attempt.

The new work for the approved target is the even-moment expansion,
the per-monomial permutation and clipped correction, and their uniform
sum controlling the physical derivative. The normalization and top-row
checks are included because the scalar rank comparison would not justify
them. Weingarten integration, complex HCIZ expansion, Bingham formulas,
independence of disjoint corners and stochastic order of complex laws
are not inputs. The finite pair-swap average in (7) is proved directly.
No theorem outside the saved coverage is invoked.

The result only pays a finite heterogeneous phase-perturbation cost.
It does not provide the actual-Xi family within the phase window, a
finite-reference or signed-complement bound, all-degree signs, theta
signing or a graph realization. The earlier scope stops retain their
recorded evidence. The construction checks in attempt1222 did not
constitute an independent audit; audit1224 is recorded separately below.
No novelty certification or RH resolution follows from this result.

### Independent conceptual audit1224

17 November 2026. The exact finite-family claim (1)-(2) passes the
separately approved conceptual audit, relative to C030l's full weak-row
comparison and its cited orbital-law input. This is a reproduction of
the local argument, not a strengthened bound or an independent audit of
the external source proofs. The only textual correction is to specify
t>0 at (4): the originally unqualified condition t*A<=1/4 alone would
also admit arbitrarily negative t. The stated theorem already assumes
x>0, so no hypothesis, conclusion or constant changes.

**Symmetry, normalization and the physical derivative.** For each
fixed j, conjugation of Q by a single pair-swap unitary preserves Haar
measure and tr(D_0 Q), reverses that pair's diagonal difference and
leaves all other differences unchanged. Averaging successively over
these commuting swaps gives (7) exactly, without independence. The
simultaneous swap separately proves that the partition ratio is the
real expectation of cos(t R). Since |R|<=A, its floor is 31/32 on
the specified window. Differentiating the separately normalized
expectation gives (5), including its covariance term. Positivity of
Z_(j,0) and F_j implies (6); a complex logarithm is not required.

**The moment-specific fields.** For each h, its p nonzero exponents
satisfy p<=s. A fixed coordinate permutation moves exactly those pairs
first; it also permutes every real rate. This is a Haar change of
variables for that one scalar moment. With Y=tQ, its law is the scaled
orbit with top row lambda_j(t). Equation (10) is the telescoping identity
sum_i q_i(S_i-S_(i-1)); hence all proper-row fields are precisely
q_(v+1)-q_v, fixed as t varies. The discarded factor exp(-q_n t j)
cancels only against this law's own normalizer. No real rate, including
one outside the active pairs, has been dropped. No coupling between
the different permutations is used anywhere in the sum.

**Global tests and boundary translation.** If Phi is increasing in
proper and top coordinates on the full coordinate space, the two
inequalities

    E_(lambda,c) Phi(z,lambda)
      <= E_(lambda,c) Phi(z,mu)
      <= E_(mu,c) Phi(z,mu)

hold for lambda<=mu. The second is C030l applied to the fixed test
Phi(.,mu). The first may evaluate a noninterlacing (z,mu), which explains
why a merely support-defined test would be insufficient. All tests used
here are global and continuous, and each relevant support is compact.
Adding eta to every top coordinate adds eta I to Y and v eta to S_v.
Thus the proper-row exponential weight and its normalizer both acquire
the constant exp(eta sum_(v<n) v c_v). The normalized law is exactly the
translated law. Applying the comparison to the two ordered boundaries
lambda_j(t)<=lambda_j(t+eta)<=lambda_j(t)+eta*1 gives (15) including
the top row. Separate normalizers and arbitrary real field signs are
therefore accounted for.

**Coordinate check on the correction.** Write alpha_(lv) for the
coefficient of S_v in d_l. Its nonzero values are 2 at v=2l-1 and -1
at v=2l-2,2l; the v=0 term is identically zero. Increasing one coordinate
of row v by u>=0 changes d_l by alpha_(lv) u. Telescoping over the
scalar d arguments and using clipping gives the global inequality

    |g_h(z+u e_(v,i))-g_h(z)|
      <= 2 U^(2s-1) u sum_l h_l |alpha_(lv)|.

The right side equals H_h(z+u e_(v,i))-H_h(z). Consequently both
H_h+g_h and H_h-g_h are coordinatewise increasing, even at clipping
corners and on noninterlacing arrays. This calculation includes v=n
when 2p=n. On both actual supports, 0<=Y<=U I implies |d_l|<=U,
so g_h equals the desired even monomial. Applying the lower comparison
to the two corrected tests bounds the absolute moment difference by
Delta E H_h. Its nonnegative trace coefficients and (15) give precisely
the row cost 2 U^(2s-1) eta sum_l h_l(8l-4) in (17).

To check the discrete maximization, put h_l=1+e_l with e_l>=0 and
sum_l e_l=s-p. Then sum_l l h_l<=p(p+1)/2+p(s-p), because each l<=p.
The row-cost upper bound becomes

    sum_l h_l(8l-4)
      <= 8ps-4p(p-1)-4s
       = 4s^2-4(s-p)(s-p+1) <= 4s^2.

In the original fixed coordinates let T_h(Q) be the product of the
unscaled even diagonal differences. Direct differentiation also gives

    M_h'(t)=2s t^(2s-1) E_t T_h
                     -t^(2s) Cov_t(L,T_h).

All integrands here are bounded on compact t intervals for the fixed
finite family. This proves smoothness and confirms that the right
difference quotient used in (17) varies the full law. Dividing by eta
and taking eta down to zero therefore bounds this entire derivative
by 8s^2 t^(2s-1), including the covariance. Its constant is uniform
although the elementary domination used to establish smoothness may
depend on the fixed real rates.

**Infinite sum and constants.** For fixed finite m, the coefficient
bound (9) follows from (2h_l)!>=2^h_l h_l! and the exact multinomial
identity at each s. It controls the undifferentiated integrand series
uniformly by exp(T^2 M/2). The derivative majorant at T is

    (8/T) sum_(s>=1) s^2 (T^2 M/2)^s/s! < infinity.

Thus both series have the required uniform convergence on every closed
subinterval of (0,infinity); each term is continuously differentiable.
The usual termwise differentiation theorem applies. In particular, the
coefficient bound is summed over all moments after their separate scalar
derivative estimates; it never requires a common permutation or a
dimension limit. The identity sum s^2 z^s/s!=(z+z^2)exp(z) follows by
splitting s^2=s(s-1)+s. With z=x^2 M/2<=1/32 this gives

    |F_j'(x)| <= 4xM (33/32)(32/31) = (132/31)xM,
    |F_j'(x)/F_j(x)| <= (132/31)(32/31)xM
                       = (4224/961)xM.

Adding the two separately normalized rank responses gives 8448/961;
9*961-8448=201>0. No numerical sampling is involved.

**Endpoints and verdict.** At j=0,n, Q is respectively 0,I, every pair
difference vanishes and F_j=1; the claimed improved adjacent-endpoint
constant follows. Zero phases cause no division and M=0 gives F_j=1
at every t. Repeated real parts and either sign of their contrasts are
allowed by the fixed-real-field comparison. If n=2m, any deterministic
top trace in the correction was already included in the global test;
there is no missing background field. Weak projection spectra use the
C030l continuity extension, not an ambient density on a collapsed
polytope. Finally, the derivative estimate is valid for all positive t,
independently of the phase window. At xA=1/4, continuity and the strict
floor give a positive neighborhood of F_j, so the logarithmic response
at x and the right difference quotients remain legitimate.

This validates the previously pending finite heterogeneous response
bound. It leaves the actual-Xi finite-reference, phase/degree/time and
signed-complement hypotheses, all-degree positivity, theta signing and
realization unresolved. It is not a complete RH candidate.

## Mathlib

Full matching coverage of (1)-(2), the tilted orbital comparison and its
orbital-law input is unchecked; no absence claim is made. Haar invariance,
bounded differentiation under an integral, finite multinomial sums,
clipping/Lipschitz estimates and uniform derivative-series convergence
are supporting mathematics. Matching formal theorem names were not
checked and no formalization is claimed.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
