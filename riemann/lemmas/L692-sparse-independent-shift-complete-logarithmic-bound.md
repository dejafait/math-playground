# Lemma 692: a growing sparse independent support pays the complete logarithmic loss

## Hypotheses

Use L666's family: integers q>=1, n=12q+3, M=4q+1=n/3,
x=-d=-5/4, R=11/8, U=R^2, h=27/(10n), t_j=j/n for 0<=j<n.
For -2q<=m<2q choose real |e_m|<=1/8 and put

    a_m(e)=x+i*h*(m+1/2+e_m),
    Z_e={x} union {a_m(e): -2q<=m<2q},
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    c_k(e,u)=R^(-1) sum_(a in Z_e) W_a(u)*(a/R)^k,
    G_e(u,zeta)=sum_(0<=k<M) c_k(e,u)*zeta^k,
    m_e(u)=mean_(|zeta|=1) log|G_e(u,zeta)|,
    A_n(e)=mean_(|u|=1) m_e(u).

Both means are normalized. All original residues are one, the anchor
is fixed, all M spatial moments are retained, and one displacement
vector is used at every angle. The full j=0 product and denominator
angle 1/u are part of these definitions. Use L657's complete K,Q,m_0,
Z_n,P_n, with Z_n denoting its angular zero charge.

Assume n>=10^6 and, for an integer L with 1<=L<=n/40000,

    #{m: e_m!=0} <= 2L.                                  (1)

The changed indices may occur anywhere, need not be consecutive or
symmetric, and the shifts may vary independently. In particular this
covers at most 2*floor(n/40000) changed nodes.

## Conclusion

For every |u|=1, including angles with spatial-circle zeros,

    m_e(u) >= -log(2R)-4L*log(5*n^2/(2*L^2))
           >= -log(2R)-n/400.                            (2)

Consequently

    A_n(e) >= A_n(0)-n/400-1-log 2
           >= A_n(0)-n/100.                              (3)

Thus the approved n/100+C*log n loss is paid on this subfamily with
C=0 and the explicit onset 10^6. The same estimates hold simultaneously
along the entire straight homotopy e_m(t)=t*e_m, 0<=t<=1.

Let r_*=273/200 and rho=r_*/R=273/275, and set

    C_m=log[r_*^2/(d^2*(1-rho))], C_*=1+log 2+C_m.

The complete angular charge satisfies

    Z_n(e) >= Z_n(0)-n/400-C_*.                           (4)

This permits a number of independent shifts, and hence interfaces,
growing proportionally to n, but only a small fraction of the full
cube. The full cube has 4q~n/3 potentially changed nodes. Neither its
complete logarithmic bound nor H/support transfer, Xi realization or
mixed positivity follows. The result is a new local partial bound
within the assessed target, not certified originality or an RH candidate.
Section 7 records a separate finite audit accepting (2)–(4) under
exactly these hypotheses. This is local validation of the specialization,
not a new general coefficient theorem or a full-cube result.

## Proof

### 1. Scope, known results and comparison with existing stops

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-independent-shift-mahler-homotopy.md`.
It covers this exact cube/path and useful partial complete-charge
bounds, with all remaining losses explicit. L691 already controls two
independently moved halves by a single-interface analytic limit. That
compact limit is not assumed for growing interfaces here. L664's
two-offset family, L665's absolute-transfer failure and L666's signed
energy obstruction do not imply (2).

L686's spatial denominator clearing gives a small-circle norm bound
at one angle for sparse support. Its separation-product idea motivates
the test below; no conclusion or unaudited baseline from L686 is used.
Here exact annihilation in the available moments and the audited L690
uniform baseline give a bound for the complete spatial logarithmic
mean at every angle. The coefficient charge below is essential;
neither a large coefficient nor a norm alone equals that mean.

Import the complete polynomial root formula, including boundary roots,
from F. Brunault and W. Zudilin, *Many Variations of Mahler Measures*,
ISBN 9781108794459, [Propositions 1.4–1.5, pp.6–7, and Lemma 1.6, p.8](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
as inspected in the assessments. Proposition 1.4 includes boundary
roots, Proposition 1.5 gives the polynomial root formula, and Lemma 1.6
gives the coefficient bound used in (13). L657 supplies nonzero spatial
slices, absolute product-log integrability and the exact angular charge
identity. These general results are imported without reproof. The separate
audit scope is `drafts/literature/2026-11-03-sparse-complete-logarithmic-audit-scope.md`.
L690 (1)–(2), with common displacement zero, is the
quantitative baseline. No new source input, singular-log differentiation,
root separation from a circle, or continuity uniform in degree is used.

### 2. Exact annihilation and the baseline remainder

Since n>=10^6 and L<=n/40000, 8L<=n/5000<M-1. In particular
2L<=4q and N:=4L<=M-1. Choose a set S of exactly 2L indices containing
every changed index, padding with unchanged ones if necessary. Define
the monic polynomial in the normalized pole coordinate z

    p(z)=product_(m in S) (z-a_m(e)/R)*(z-a_m(0)/R)
        =sum_(k=0)^N p_k*z^k.                            (5)

Repeated factors from padding are retained. L666 gives |a_m(e)|<R
and the same for a_m(0), so

    sum_k |p_k| <= product_(all labelled roots b)(1+|b|)
                 <=2^N.                                 (6)

For each angular u all products W_a are finite. In

    T_e(u):=sum_(k=0)^N p_k*c_k(e,u)
           =R^(-1) sum_(a in Z_e) W_a(u)*p(a/R),          (7)

the terms indexed by S vanish. The same is true for e=0, with this
same polynomial p. All remaining nodes and W_a values agree exactly.
Therefore T_e(u)=sum_(k=0)^N p_k*c_k(0,u). This identity changes no
residue, uses no approximation and holds for every |u|=1.

L690 (1), with E_n=n^2*exp(22-n/500), gives uniformly on both circles

    |G_0(u,zeta)-R^(-1)T_M(x*zeta/R)|<=E_n.

Taking a Fourier coefficient in the spatial variable bounds each
coefficient difference by E_n: the coefficient equals the normalized
integral of this polynomial difference times zeta^(-k). Thus (6)–(7)
give

    |T_e(u)-R^(-1)*p(x/R)| <= E_n*2^N.                   (8)

All indices k<=N are available spatial moments; no coefficient of
degree >=M has been introduced.

### 3. The anchor separation and dominance over the baseline error

Order the 2L selected indices by increasing |m+1/2|. There are exactly
two indices at each magnitude k-1/2, 1<=k<=2q. Hence for the j-th
selected index, putting k=ceil(j/2), both its old and new ordinates
have absolute value at least

    h*(k-5/8) >= 3*h*k/8.

In (5) this yields, including every labelled factor,

    |p(x/R)| >= (3*h/(8R))^(4L)*(L!)^4
              >= (L/(5n))^(4L).                         (9)

For the last inequality use log(L!)>=L*log L-L (integrate log t
on [1,L], with L=1 included) and exp(1)<3. The resulting constant
3*h/(8R*exp(1)) exceeds 27/(80R*n)=27/(110n)>1/(5n).
The nonanchor ordinates never vanish; the anchor value in (9) is
strictly positive in modulus. There is no phase or sign assumption.

For 0<v<=n/40000 the function v*log(10n/v) is increasing, since its
derivative log(10n/v)-1 is positive. Thus

    N*log(10n/L) <= (n/10000)*log 400000 < 7n/5000.      (10)

The elementary bound log 400000<14 follows from
exp(1)>8/3 and (8/3)^14>400000. Therefore the ratio of twice the
error in (8) to R^(-1)*(L/(5n))^N is at most

    2R*n^2*exp(22-n/500+N*log(10n/L))
        <= 2R*n^2*exp(22-n/2000) < 1.                  (11)

Indeed 1/500-7/5000=3/5000>1/2000. The last expression is decreasing
for real n>=10^6. Its logarithm at 10^6 is less than
2+40+22-500=-436: use log(2R)<2, and log(10^6)<20 since
exp(1)>2 and 2^20>10^6. These are strict bounds, not floating-point
screens. Equations (8)–(11) prove, uniformly in angle,

    |T_e(u)| >= (1/(2R))*(L/(5n))^N > 0.               (12)

### 4. Paying the coefficient-to-complete-mean charge

For a nonzero polynomial P(zeta)=gamma*product_(j=1)^D(zeta-alpha_j),
the imported root formula gives

    exp(mean log|P|)=|gamma|*product_j max(1,|alpha_j|).

Apply the imported Lemma 1.6 at the actual degree D: for 0<=k<=D,
the k-th coefficient has modulus at most binom(D,k) times this
Mahler measure. This includes D=0; coefficients with k>D are zero.
For G_e(u,.) one has D<=M-1, and binom(D,k)<=binom(M-1,k)
when k<=D. Thus for 0<=k<=N

    |c_k(e,u)| <= binom(M-1,k)*exp(m_e(u)).              (13)

This statement includes circle roots, multiple roots and degree drops.
L657 ensures a nonzero polynomial at every angular u. Since
N<=(M-1)/2, the largest binomial coefficient in (13) for k<=N is
binom(M-1,N). Using N!>=(N/exp(1))^N and exp(1)<3 gives

    binom(M-1,N) <= (exp(1)*(M-1)/N)^N <= (n/N)^N.

Combine (6), (7) and (13):

    |T_e(u)| <= (2n/N)^N*exp(m_e(u))
              = (n/(2L))^N*exp(m_e(u)).                 (14)

Together (12) and (14) imply

    exp(m_e(u)) >= (1/(2R))*(2L^2/(5n^2))^(4L),

which is the first inequality in (2). The function
v*[log(5/2)+2log(n/v)] is increasing on 0<v<=n/40000.
Since log(5/2)<1 and log 40000<11,

    4L*log(5n^2/(2L^2))
        <= (n/10000)*(1+22) = 23n/10000 < n/400.        (15)

Here exp(1)>8/3>5/2 and (8/3)^11>40000 justify the logarithmic
comparisons. This proves all of (2), with every coefficient loss paid.

### 5. Complete angular integration, charges and the straight path

L657 supplies absolute product-log integrability, so integrate (2)
over u to bound A_n(e). L690 (2) gives
A_n(0)<=-log R+1 for every admissible n>=30000. Subtracting yields
the first inequality in (3). The second follows from

    (1/100-1/400)*n = 3n/400 > 1+log 2,

already at n>=10^6. No singular logarithm is differentiated and no
zeros of G_e on either circle are excluded.

For the charge statement use L657 exactly:

    A_n(e)=m_0(e)+Z_n(e)-P_n.

Its interior denominator roots are p_j=t_j*x/U and do not depend on
e. All remaining denominator roots a/t_j are exterior. L657's two
bounds for m_0, at the same M, imply m_0(e)-m_0(0)<=C_m. Subtracting
the complete identities and using (3) proves (4). Cancelled factors
remain in K and Q; multiplicities, actual degrees and the finite
exceptional center-zero spatial slices are treated exactly as in L657.
No subset of numerator roots replaces Z_n.

At every t in [0,1], |t*e_m|<=1/8 and its changed-index set is a
subset of the same S. All estimates are uniform over these shifts.
Thus the whole straight path is covered by the same constants and
onset, without a derivative of A_n.

### 6. Remaining obstruction and verification limits

This is a complete-mean bound with growing independent support, beyond
the fixed-interface subfamily, but is still a small-support result.
For generic shifts at s indices, their s old and s new normalized
positions are distinct; the disjoint cell intervals in L666 ensure
this. Any nonzero polynomial annihilating all those positions has
degree at least 2s. The present method has only M moments, permitting
degree <=M-1. At full support s=4q this requires degree 8q while
M-1=4q. Even before that degree obstruction, the baseline error and
coefficient costs in (10)–(15) require a small support fraction.
Neither obstruction is an upper bound on A_n or a counterexample
to the full-cube target. Extending this method requires new structure
that avoids exact old-and-new annihilation or pays its remaining cost.

The exact rational support checks are reproducible with
`python3 scripts/one-sided-hankel/sparse-complete-logarithmic-101.py`.
The full certificate is
`scripts/one-sided-hankel/sparse-complete-logarithmic-101.json`.
It checks arithmetic comparisons only, not the analytic baseline,
the proof above, a global optimization, or an independent audit.
No numerical evidence is a premise of the logarithmic or charge steps.

### 7. Separate finite proof audit — 3 November 2026, step 103

Under the pre-existing SPECIALIZE audit assessment, accept (2)–(4).
The proof uses L690's already audited (1)–(2); its contour backend and
source manuscripts are not independently replayed here. The coefficient
inequality is the known Lemma 1.6 just cited, not a local discovery.

**Finite family and functional.** L666's ordinate gaps are at least 3h/4
and its nonanchor ordinates have absolute values at least 3h/8. Moreover
|a|^2<353/200<(273/200)^2. Thus there are exactly M distinct unit-residue
nodes satisfying L657, with no coincidence with the anchor, along every
allowed straight path. Since 8L<=n/5000<M-1 for n>=10^6, S can be
padded to 2L indices and N=4L<=(M-1)/2. Repeated factors in p do not
change annihilation. Expanding p(a/R) gives exactly sum p_k*c_k,
without coefficient conjugation or an extra power of R. Outside S the
nodes and their individual W_a agree, since W_a depends only on a and
the fixed anchor/grid. Both selected old and new terms vanish. Fourier
coefficient extraction from L690's full uniform error then gives (8)
for every angular u, not only almost everywhere.

**Separation and error.** The j-th selected absolute half-index is at
least ceil(j/2)-1/2. Both labelled roots therefore have distance from
x/R at least 3h*ceil(j/2)/(8R). Their product is the factorial
in (9). The elementary series bounds 8/3<exp(1)<3 justify its constant
27/110>1/5 and the logarithmic comparisons in (10) and (15). With
v<=n/40000, v*log(10n/v) is increasing. The error ratio in (11) has
logarithm bounded by log(2R)+2log n+22-n/2000; its derivative
2/n-1/2000 is negative throughout n>=10^6, and its onset upper bound
is -436. The certified rate margin is 3/5000>1/2000. Thus (12) is
strict and uniform. The real-n comparisons apply in particular to
every admissible n=12q+3 above the onset; no congruent endpoint is lost.

**Coefficient cost and mean.** Use the actual spatial degree, treating
coefficients above it as zero before replacing its binomial by the
nominal one. This covers constant nonzero slices. The binomial sequence
is increasing through N, and exp(1)*(M-1)<n, giving (14). The function
v*[log(5/2)+2log(n/v)] is increasing on the support range. Hence the
total cost is at most 23n/10000<n/400, while the available final
rate slack at n=10^6 is 7500>1+log 2. These are lower bounds on the
complete spatial mean, including circle roots, rather than lower
bounds on a single coefficient incorrectly identified with that mean.

**Integration, charge and path.** L657's Vandermonde argument ensures
every spatial slice is nonzero. Its nonzero K and boundary-nonzero Q
give absolute product-log integrability, so the angular integration is
valid despite torus zeros. L690 gives A_n(0)<=-log R+1 at this onset.
For each e the only interior roots of Q are the same p_j, of the same
multiplicities; all roots a/t_j have modulus >d. L657's center value
has constant coefficient with positive real part, so its center-zero exceptional
spatial slices are finite. Its complete identity, including cancelled
factors and actual angular degrees, consequently applies. The two
m_0 bounds at the same M give m_0(e)-m_0(0)<=C_m. Subtracting the
complete identities proves precisely (4), with C_*=1+log 2+C_m.
Finally every t*e lies in the same cube and has support contained in S.
All constants and the onset are independent of t; no path differentiation
or uniform root separation from either circle is being asserted.

Replayed all thirteen exact comparisons in the existing script and
inspected every actual/required value in its certificate's complete
`/checks` field. All passed: mean-loss upper rate 23/10000, reported
rate 1/400, target rate 1/100; error-rate margin 3/5000, required
>1/2000. This repeats the existing rational backend, not an independent
analytic verification. The paper audit above supplies the finite
applicability checks. Full matching Mathlib coverage remains unchecked.
No full-cube extension, diagonal comparison theorem, H/support transfer
or Xi conclusion is accepted by this audit. Section 6's degree and
cost limitations remain intact.

## Mathlib

Reuse the supporting univariate coverage recorded in the assessment:
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
including `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure` and
`Polynomial.mahlerMeasure_mul`. These support full root means, not
this family-specific annihilation and uniform constants. Full matching
coverage for (2)–(4) and the coefficient estimate has not been checked.
No library absence claim or formal verification is made.
