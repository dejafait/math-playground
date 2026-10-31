# L522 — Individual prime Stieltjes dilation limits

## Hypotheses

Retain exactly L521's fixed conditional model: 0<a<A<infinity,
ell=2a>log(2), I=(0,ell), the smooth-core logarithmic part operator
G_I with multiplier Psi(xi)=(1/2)log(1+xi^2), and

    c=log(2pi), d_n=log(n), w_n=Lambda(n)/sqrt(n),
    mu=nu_rho+sum_(n>=2,d_n<=2A) w_n(delta_(d_n)+delta_(-d_n))
                          -2cosh(x/2)1_(|x|<=2A)dx,
    rho(x)=exp(-x/2)/(1-exp(-2x))-exp(-x)/(2x), x>0,
    A_I=G_I-cI-R_I K_mu E, Dom(A_I)=Dom(G_I).

Here nu_rho has the even density rho. Assume a real normalized
nullvector A_Iu=0, ||u||_2=1, nonzero left renewal trace and
log(2)!=ell-d_n for every w_n>0 with d_n<=2A. Retain these last
two hypotheses although this specialization does not use them.
The cutoff includes equality, both prime shifts and the signed pole.
Nullvector existence and the complete-Weil identification with its
imported manuscript qualification remain assumptions, as in L516
and L521; no actual-Xi realization is asserted.

Let f=Eu be L515's continuous compact zero extension. L521 gives
f in BV(R). Define v(x)=f(x+a), supported in [-a,a], and use L516's
centered dilation U_r v(x)=sqrt(r)v(rx) and translation T_t v(x)=v(x+t).
Let Df and Dv denote distributional derivatives, as finite signed
Borel measures with <Df,phi>=-integral f phi' on smooth compact tests.
Put B=||f||_infinity and V=|Df|(R)=|Dv|(R)<infinity.

The unchanged pre-existing SPECIALIZE gate is
`drafts/literature/2026-10-30-weil-individual-prime-stieltjes-specialization.md`.
This is a known-result specialization (REPRODUCTION), not a new BV
theorem or a creative signed-cancellation mechanism. The moving-test
and normalization application passes the separate conceptual audit
below under the unchanged hypotheses; imported source proofs remain
outside that audit.

## Conclusion

For every n>=2 with d=d_n<=2A, the individual prime-pair limit in
L516 (3) exists and is

    J_n=lim_(r->1+) (w_n/(r-1))
              <v,(T_(d/r)+T_(-d/r)-T_d-T_(-d))U_r v>
       =w_n d integral_R [f(y+d)-f(y-d)] Df(dy).             (1)

The integral is absolutely convergent against |Df|, with

    |J_n|<=2w_n d B V.                                    (2)

Each signed shift separately has limit

    lim_(r->1+) <v,(T_(t/r)-T_t)U_r v>/(r-1)
                  =t integral_R f(y+t) Df(dy), t=+/-d.     (3)

If d>=ell, both integrals on the right of (3) vanish. This includes
d=ell and the cutoff equality d=2A, since 2A>ell. The d=ell
finite-r contribution is retained; it need not vanish before the
limit. Atoms with d>ell have zero finite-r contribution for r
sufficiently close to 1. If w_n=0 the corresponding term is zero.

Consequently L516's aggregate limit is the finite, absolutely
convergent sum S(v)=sum_(n>=2,d_n<=2A) J_n, and its identity becomes

    a(tau_L^2+tau_R^2)=H(v)-P(v)
        +sum_(n>=2,d_n<=2A)
            w_n d_n integral [f(y+d_n)-f(y-d_n)] Df(dy).    (4)

H, P and the traces have precisely L516's definitions for v. No
term of nu_rho, scalar c or the signed pole is changed. The finite
bound (2) supplies no arithmetic sign, family-uniform bound or
saving proportional to an eigenvalue; L516 (6), full-Weil
identification, collar/branch estimates and Xi transfer remain open.

## Proof

### Imported derivative-measure convergence

Import Bruno Galerne, *Random fields of bounded variation and
computation of their variation intensity*, Adv. Appl. Probab. 48
(2016), 947–971, Section 2, Lemma 1 and Theorem 1, pp.951–953
([primary publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/83627D38EAB49283AE917366027E8BE7/S0001867816000604a.pdf/random_fields_of_bounded_variation_and_computation_of_their_variation_intensity.pdf)).
For g in BV(R) intersect L1(R), the signed finite measures

    q_h^g(dx)=[g(x+h)-g(x)]dx/h, h!=0,

have |q_h^g|(R)<=|Dg|(R) and converge weak-* to Dg as h->0,
tested against C_0(R). The parameter h may have either sign. This
is the whole-line one-dimensional case, with no eroded boundary.
Its sign convention agrees with the distributional derivative
above: for a smooth test, a change of variables yields the limit
-integral g phi'. We use the cited norm bound and convergence,
not an independent reproof or any stochastic assumption.

The hypotheses hold for f by L515 and L521. Translation gives
them for v as well. For any continuous compact test psi,

    integral psi(x) Dv(dx)=integral psi(y-a) Df(dy).         (5)

For smooth tests this follows from x=y-a in the distributional
definition; density of smooth tests in C_0 and finite measure norms
extend it to the displayed tests. Thus variation is unchanged.

### Exact change of variables, including the dilation center

Fix one t=+/-d. Let 1<r<A/a and h=t(1-1/r), which has the sign
of t. All the following Lebesgue pairings are absolutely integrable:
v and U_r v are bounded with compact supports. In the first shifted
pairing set z=x+t/r, and in the second set z=x+t. Then set y=z-t.
This gives the exact identities

    <v,(T_(t/r)-T_t)U_r v>
       =integral [v(z-t/r)-v(z-t)] sqrt(r)v(rz) dz
       =integral [v(y+h)-v(y)] sqrt(r)v(r(y+t)) dy,
    <v,(T_(t/r)-T_t)U_r v>/(r-1)
       =(t/r) integral phi_(r,t)(y) q_h^v(dy),
    phi_(r,t)(y)=sqrt(r)v(r(y+t)).                         (6)

In particular h/(r-1)=t/r, with no missing minus sign or sqrt(r).
To express centered dilation in L521's interval coordinates, define

    W_r f(y)=sqrt(r) f(a+r(y-a)).

It is W_r, rather than dilation about the endpoint 0, that transports
U_r. With s=y+a in (6), its moving test is
sqrt(r)f(a+r(s-a+t))=W_r f(s+t). Both coordinate systems therefore
have the same step h and the same prefactor t/r.

### Moving continuous tests

Let omega(epsilon)=sup_(|x-z|<=epsilon)|v(x)-v(z)|. Compact
continuity gives omega(epsilon)->0 as epsilon->0. For r>=1,
phi_(r,t) and phi_t(y)=v(y+t) are continuous and vanish outside
the common compact interval [-a-t,a-t]. On this interval
|y+t|<=a. The elementary bound

    ||phi_(r,t)-phi_t||_infinity
        <=(sqrt(r)-1)B+omega(a(r-1)) ->0                 (7)

follows by adding and subtracting v(r(y+t)). Outside the interval
both functions are zero. Consequently

    |integral (phi_(r,t)-phi_t) q_h^v|
           <=V ||phi_(r,t)-phi_t||_infinity ->0.           (8)

Galerne's theorem applies to the fixed C_0 test phi_t, while (8)
justifies replacing it by the moving one. Thus (6), t/r->t and
(5) give (3). The argument includes negative h; it never tests a
measure using only L2 convergence or differentiates a trace error.
It also gives the finite-r bound

    |<v,(T_(t/r)-T_t)U_r v>/(r-1)|
                          <=|t| B V/sqrt(r).             (9)

Adding t=d and t=-d and multiplying by w_n>=0 proves (1)–(2).
Absolute integrability follows directly from boundedness of the
integrand and finiteness of |Df|, rather than a sign assumption.

### Equality atoms, finite sum and flux assembly

Since f vanishes off [0,ell], its distributional derivative is
supported there: testing in either complementary open half-line
gives zero. Continuity gives f(0)=f(ell)=0. Hence if d>=ell,
f(y+d)=f(y-d)=0 for every y in [0,ell], including both endpoints.
Both Stieltjes pairings therefore vanish. This argument does not
discard equality atoms or presume differentiability at an endpoint.

For comparison with the original finite-r terms, v has support
[-a,a] and U_r v support [-a/r,a/r]. A scaled translation t/r
can overlap only if |t|<=a(r+1); an unscaled one can overlap only
if |t|<=a+a/r. If d>ell=2a, choose r>1 sufficiently close to 1
that a(r+1)<d. Both pairings then vanish. In particular d=2A is
retained but inactive (already a(1+r)<a+A<2A for r<A/a).
At d=ell the scaled overlap can persist. Formula (3) proves its
zero limit; it agrees with L516's separately established
O(1/log(1/(r-1))) bound from the two endpoint traces. No claim of
finite-r vanishing at this activation is made.

There are only finitely many integers n with log(n)<=2A. Thus one
may pass to the limit term by term in L516 (3), with no infinite
interchange or uniform-in-n assertion. The total absolute bound is
2BV sum_(d_n<=2A) w_n d_n<infinity. This proves the asserted formula
for S(v). Translation of the operator preserves the even convolution,
logarithmic part realization, real normalization and traces, so v
satisfies L516 with lambda=0. Inserting the computed S(v) into its
audited identity (5) proves (4). The complete signed model, density,
scalar normalization and pole remain those used there.

The specialization exposes the individual terms but supplies no
inequality comparing their signed sum with P-H+K lambda. B and V
are fixed-vector constants. In particular (9) cannot be promoted
to a uniform family saving or an RH positivity statement.

### Separate conceptual application audit, 2026-10-30

The pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-30-l522-stieltjes-application-audit-coverage.md`
covers this audit. Equations (1)–(9), the equality cases and the
assembly with L516 pass. This verifies the known-result specialization;
it does not strengthen its conclusion or independently audit Galerne,
the imported renewal/domain sources or the complete-Weil identification.

**Input and domain transport.** L515 supplies a bounded continuous
representative with zero endpoint limits, and audited L521 supplies
finite variation of its zero extension. Thus the source theorem is
applied to an L1 BV function on the whole line. No H1 premise is added.
For the operator transport, let C_a f(x)=f(x+a). This is unitary on
L2, maps C_c^infinity((0,2a)) onto C_c^infinity((-a,a)), and multiplies
the Fourier transform by exp(i a xi). It therefore preserves the
logarithmic form norm and maps the completed part-form domains onto
each other. The weak form characterization of the associated operator
then transports its operator domain and G_I itself, not just its
formal multiplier. Convolution by the same finite measure commutes
with C_a; zero extension and restriction commute with the corresponding
interval translation. The scalar c is unchanged. Hence the full
translated vector is a real normalized nullvector of L516's A_a.
Its left and right inward-distance traces are exactly the old traces.
The pole and atomic kernels depend on differences, so translation
changes none of their signs, weights or cutoffs. Finally
C_a^(-1) U_r C_a f(y)=sqrt(r)f(a+r(y-a)), verifying W_r on the
actual coordinates. Dilation about the left endpoint would not be
this conjugate.

**Signed measures and the exact quotient.** For t of either sign,
moving the translation from the second factor gives the difference
v(z-t/r)-v(z-t). With y=z-t this is v(y+h)-v(y), where
h=t(1-1/r). Thus h/(r-1)=t/r, including t<0; no sign is absorbed
into the measure. The other factor remains sqrt(r)v(r(y+t)).
The cited measure convergence is to Dv with the convention
<Dv,psi>=-integral v psi', and its norm is at most V for both
signs of h. Translating this derivative measure gives (5), with
no reflection or extra sign. For comparison, on a smooth compact
test vector direct differentiation of the original pairing gives
-t integral v(x)v'(x+t)dx, which integration by parts identifies
with t integral v(x+t)v'(x)dx, the same sign as (3). This sign
check is not used to impose smoothness on the actual vector.

**Moving tests and the bound.** The supports of both phi_(r,t)
and phi_t lie in [-a-t,a-t] for r>=1. There |y+t|<=a, so adding
and subtracting v(r(y+t)) gives precisely (7). The square-root
error costs (sqrt(r)-1)B and the argument change costs
omega(a(r-1)). The uniform measure norm V makes (8) tend to zero;
the remaining fixed test belongs to C_0(R), as required by the
imported theorem. Also ||phi_(r,t)||_infinity<=sqrt(r)B, which
combined with |t|/r proves the stated finite-r bound (9).
Adding the two limits gives d[f(y+d)-f(y-d)] against Df, not
their sum. The limiting pair bound is exactly 2w_n d B V.
These steps justify the measure pairings without differentiating
u or a renewal-trace error and without an L2-to-measure inference.

**Equality atoms and assembly.** Df is supported in [0,ell]. For
d>=ell the shifted continuous test values vanish on this entire
closed interval, including the endpoints since f(0)=f(ell)=0.
This proves the zero limits without needing any assertion about
atoms of Df. The two finite-r overlap thresholds are respectively
d<=a(r+1) and d<=a+a/r. Thus d>ell is eventually inactive,
whereas d=ell may have a scaled overlap. The preceding measure
limit covers that overlap and agrees with L516's trace estimate.
At d=2A, a(r+1)<a+A<2A for every allowed r<A/a, so that retained
cutoff term is already inactive. The set of n is finite with A
fixed, and (9) bounds every one of its terms; termwise passage
requires no uniformity over growing supports. The resulting sum
is exactly S in L516 (3), with its positive coefficient in (5).
This proves (4) under the unchanged imported identification.

The nonzero left trace, ell>log(2) and excluded direct reflected
collision remain hypotheses even though this audit does not use
them to evaluate the correlations. In particular the identity
does not refute existence of such a nullvector. Fixed B and V
give neither a sign for S nor a uniform eigenvalue-relative error.
Trace vanishing, family estimates, branch/collar continuation and
actual-Xi transfer remain unresolved. No new mathematical input
or DAG edge is required by this audit.

## Mathlib

Full matching coverage of this BV moving-test prime specialization
has not been checked; no absence claim is made. The imported
result is Galerne's specific finite-measure convergence theorem.
Supporting facts are translation change of variables, uniform
continuity of compact continuous functions, the finite-measure
supremum-norm pairing bound and finite-sum limit passage. L515,
L516 and L521 retain their source and Mathlib qualifications.
No Lean verification or independent source-manuscript audit is claimed.
