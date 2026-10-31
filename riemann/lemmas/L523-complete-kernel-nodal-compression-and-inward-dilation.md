# L523 — Complete-kernel nodal compression and inward dilation

## Hypotheses

Retain L516's complete conditional model on I_a=(-a,a), with
0<a<A<infinity, ell=2a>log(2), real functions and zero extensions.
The reference part form q_G has multiplier
Psi(xi)=(1/2)log(1+xi^2), Levy density n(t)=exp(-|t|)/(2|t|),
and the smooth-core domain Q_(I_a) specified in L515. Write

    c=log(2pi), k(t)=2cosh(t/2), d_n=log(n), w_n=Lambda(n)/sqrt(n),
    rho(t)=exp(-t/2)/(1-exp(-2t))-exp(-t)/(2t), t>0,
    mu_A=nu_rho+sum_(d_n<=2A)w_n(delta_(d_n)+delta_(-d_n))
                          -k(t)1_(|t|<=2A)dt,
    b(f,g)=q_G(f,g)-c<f,g>-<f,mu_A*g>,
    A_a=G_(I_a)-cI-R_(I_a)K_(mu_A)E_(I_a).

Here nu_rho has the even density rho. This is exactly L516's
signed form, including every prime power at the cutoff and both
shifts. Its complete-Weil identification and source-manuscript
qualification are retained; no actual-Xi realization is proved.

Assume b>=0 on Q_(I_a) at this one fixed interval and a real
normalized v in Dom(A_a) with A_a v=0. Retain L522's additional
hypotheses tau_L(v)!=0 and log(2)!=ell-d_n for every w_n>0 with
d_n<=2A. Nullvector existence and a first-zero realization remain
conditional. Neither simplicity nor either nodal part's nonvanishing
is assumed. L515 gives the bounded continuous zero extension; L522
supplies its BV property and signed prime limits, with the upstream
L521 qualifications unchanged. H, P, S and tau_L,tau_R have precisely
L516's normalization. The Fourier transform is integral f(x)e^(-i xi x) dx.
Its archimedean multiplier is m(xi)=Re psi(1/4+i xi/2)-log(pi),
where psi is the digamma function.

This is the bounded test under the pre-existing EXPLORE assessment
`drafts/literature/2026-10-30-weil-nodal-nullvector-compression-coverage.md`.
The domain and quadratic algebra are known inputs/specializations.
The attempted bridge from their exact arithmetic specialization to a
derivative sign fails the stated continuation test below. No novelty
claim is made. The separate conceptual application audit below passes
under the unchanged hypotheses and source qualifications.

## Conclusion

Put p=max(v,0), q=max(-v,0), and, for real s, define

    C_fg(s)=integral_R f(x)g(x+s)dx,
    X(s)=C_pq(s)+C_qp(s),
    kappa(s)=exp(-s/2)/(1-exp(-2s)), s>0.

Both p,q belong to Q_(I_a) and are continuous compact BV functions.
They need not belong to Dom(A_a). For one number beta>=0,

    b(p,p)=b(p,q)=b(q,q)=beta,                              (1)
    b(alpha p+gamma q,alpha p+gamma q)=beta(alpha+gamma)^2. (2)

Their exact complete-kernel cross interaction is

    beta=integral_0^ell [k(s)-kappa(s)]X(s)ds
                              -sum_(d_n<=2A)w_n X(d_n).   (3)

All integrals in (3) are absolutely convergent, X>=0, and
X(s)=0 for s>=ell. Thus the necessary nodal restriction is

    sum_(d_n<=2A)w_n X(d_n)
                   <=integral_0^ell [k(s)-kappa(s)]X(s)ds. (4)

The pole remains with its positive cross sign. The continuous kernel
k-kappa is negative near zero and positive at s=log(2)<ell;
no fixed off-diagonal sign is supplied. If either nodal part is
zero, (1)–(4) have beta=X=0 and add no constraint to the null equation.

The autocorrelation C_v=C_vv is continuously differentiable and

    C_v'(d)=integral v(y-d) Dv(dy)
           =-integral v(y+d) Dv(dy),
    S(v)=-2 sum_(d_n<=2A)w_n d_n C_v'(d_n),
    C_v=C_pp+C_qq-X.                                     (5)

The C_fg entering X and the same-sign terms are also continuously
differentiable. For U_r v(x)=sqrt(r)v(rx) and 1<r<A/a,

    b(U_r v,U_r v)=b(U_r v-v,U_r v-v)>=0,
    lim_(r->1+) b(U_r v,U_r v)/(r-1)
                   =H(v)-P(v)+S(v)
                   =a(tau_L^2+tau_R^2)>0.                (6)

Consequently this admissible one-sided variation yields
S>=P-H, compatible with the assumed nonzero trace. It does not yield
the required reverse bound S<=P-H. Equations (3)–(4) constrain
overlap values and an integral, while (5) still requires their signed
slopes, including both same-sign terms. No estimate of those slopes
has been obtained from this compression.

This is a limitation of the tested static two-part implementation,
not a theorem of logical independence or a counterexample to the
actual arithmetic criterion. Further use of the full null equation
or new kernel estimates is not excluded. No trace vanishing, family
O(lambda) estimate, positivity range or RH conclusion follows.

## Proof

### Reference domain, weak tests and the compressed matrix

Import Fukushima, Oshima and Takeda, *Dirichlet Forms and Symmetric
Markov Processes*, second revised and extended edition, 2011,
[Theorems 1.4.1 and 1.4.2(i), pp.25–28](https://api.pageplace.de/preview/DT0400.9783110218091_A15362972/preview-9783110218091_A15362972.pdf).
Normal contractions and positive/negative parts preserve the domain
of a Dirichlet form. Apply this to L515's stipulated reference
part Dirichlet form on the open interval with Lebesgue measure.
The bounded perturbation in L516 has this same form domain. Hence
p,q are legitimate weak tests for the complete equation. No
contraction inequality for b, or operator-domain membership of
p,q, is inferred from this citation. There is no need to reprove
the standard domain theorem.

Clipping preserves continuity, support and boundedness. For any
finite ordered partition, the sum of the absolute increments of p
or q is at most that of v, since each clipping map is 1-Lipschitz.
Thus their total variations are finite. In particular all their
distributional derivatives are finite signed measures.

The weak null equation is b(v,h)=0 for every h in Q_(I_a).
Testing with p,q and using v=p-q gives
b(p,p)=b(p,q)=b(q,q). Their common value beta is nonnegative by
the assumed nonnegativity of b. Bilinearity proves (2). This also
gives b(|v|,|v|)=4beta; the unavailable full-form modulus contraction
cannot be used to set beta to zero. No division by a nodal norm
has occurred, so the argument includes a zero nodal part.

### Exact signed cross kernel and convergence

The Levy form stipulated in L515, polarized on its whole-line
zero extensions, is

    q_G(p,q)=(1/2) integral integral
        [p(x)-p(y)][q(x)-q(y)]n(x-y)dx dy.

This is the reference Levy-form representation, not a formula for
the full signed form. Its mixed integrand is absolutely integrable
by Cauchy–Schwarz applied to the two finite reference energies.
Since p(x)q(x)=0 at every point, its product of differences equals
-p(x)q(y)-p(y)q(x). These two nonnegative absolute terms have finite
integrals, and evenness of n therefore gives

    q_G(p,q)=-integral integral n(x-y)p(x)q(y)dx dy.        (7)

The scalar term is zero. The rho cross term is absolutely integrable
by the finite convolution-measure bound on L2, and the pole term is
absolutely integrable because k is bounded on the compact difference
interval and p,q are L1. Every translation pairing is bounded by
||p||_2||q||_2. Since n+rho=kappa away from zero, the exact complete
cross term is

    b(p,q)=integral integral [k(x-y)-kappa(|x-y|)]p(x)q(y)dx dy
                     -sum_(d_n<=2A)w_n[C_pq(d_n)+C_pq(-d_n)]. (8)

In particular, integral integral kappa(|x-y|)p(x)q(y) is finite:
use (7) and the absolute rho bound. The diagonal is a null set and
p(x)q(x)=0, so no singular diagonal value is assigned.

Set s=y-x in the absolutely integrable terms, and use
C_pq(-s)=C_qp(s). This yields (3). Nonnegativity of the functions
gives X>=0. Their supports lie in [-a,a], with zero values at the
endpoints, so X(s)=0 for s>=ell. Thus cutoff-equality and support-
equality atoms remain in (3); their zero values are justified,
not omitted as a convention. Formula (4) follows from beta>=0.

As s decreases to zero, kappa(s)~1/(2s) whereas k(s)->2.
At s=log(2), k=3/sqrt(2) and kappa=4/(3sqrt(2)), giving
k-kappa=5/(3sqrt(2))>0. Both signs occur within the allowed
difference interval. This is only a coefficient check; it neither
assumes that p,q see both regions nor asserts a full-form
positivity-preservation result. If p or q is zero, (8) and the
matrix equations give beta=X=0 directly.

### The slope observable, with BV justification

Use the signed difference-quotient convergence already imported in
L522 from Bruno Galerne, *Random fields of bounded variation and
computation of their variation intensity*, Adv. Appl. Probab. 48
(2016), 947–971, Section 2, Lemma 1 and Theorem 1, pp.951–953
([primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/83627D38EAB49283AE917366027E8BE7/S0001867816000604a.pdf/random_fields_of_bounded_variation_and_computation_of_their_variation_intensity.pdf)).
For g in BV(R) intersect L1(R), the measures
[g(y+h)-g(y)]dy/h converge weak-* to Dg, for either sign of h,
against continuous compact tests, with norm at most |Dg|(R).
We specialize that theorem, without reproving it or assuming H1.

For continuous compact BV functions f,g, a change of variables gives

    [C_fg(d+h)-C_fg(d)]/h
       =integral f(y-d)[g(y+h)-g(y)]dy/h.

The source theorem makes its limit integral f(y-d) Dg(dy).
Moving the change of displacement to the first factor instead gives
-integral g(y+d) Df(dy), using the quotient with step -h.
Both tests are continuous and compact. Uniform continuity of f or g
and the finite derivative-measure norm show that these limits depend
continuously on d. This proves the asserted C1 property and (5)'s
first equality. L522's exact signed limits then give its formula
for S, with no infinite sum or moving-support interchange. Expanding
v=p-q gives the last equality in (5).

For clarity, those same formulas express the unresolved quantity as

    S=-2 sum_(d_n<=2A)w_n d_n
                       [C_pp'(d_n)+C_qq'(d_n)-X'(d_n)].    (9)

Nothing in (3) or (4) is a bound on these derivatives. A single
overlap inequality at the fixed nullvector cannot be differentiated
in displacement: it has not been proved for a family with that
displacement varied. We do not assert that the complete eigen-equation
could never supply the missing information.

### What the admissible inward variation actually supplies

L516's form-domain dilation argument applies to v: U_r v belongs
to Q_(I_a) for r>1. Change variables in the complete form to obtain

    E(r):=b(U_r v,U_r v)
      =(1/(2pi))integral m(r xi)|hat v(xi)|^2 dxi
        +(1/r)integral integral k((x-y)/r)v(x)v(y)dx dy
        -2 sum_(d_n<=2A)w_n C_v(r d_n).                    (10)

This identity follows on the smooth core and extends by the domain
bounds from L516 and the bounded perturbations. The same finite
cutoff suffices; no atom has been removed. L516 proves that xi m'(xi)
is bounded. Thus the multiplier difference quotients in (10) are
uniformly bounded and converge to xi m'(xi), so their integrals
converge by dominated convergence against |hat v|^2. The pole
difference quotient converges uniformly on the compact difference
interval to -k(s)-s k'(s); its contribution is -P(v).
The C1 result just proved handles each of the finitely many prime
terms, giving S(v). For d_n>=ell, C_v is zero to the right and C1,
so C_v'(d_n)=0, also at equality. This checks every equality case
in (10)'s inward limit without dropping the atoms in advance.

We have proved E'(1+)=H-P+S without differentiating r->U_r v in
the form norm. Now h_r=U_r v-v belongs to Q_(I_a); the null equation
gives b(v,h_r)=0 and b(v,v)=0. Consequently E(r)=b(h_r,h_r)>=0.
Its right derivative at E(1)=0 is nonnegative. L516's audited flux
identity identifies that derivative with a(tau_L^2+tau_R^2),
strictly positive under the retained tau_L!=0 hypothesis. There is
no contradiction with fixed-interval semidefiniteness. An outward
dilation reaches outside I_a and is not a permissible nonnegativity
test for the assumed operator on this interval.

The achieved threshold is therefore the lower bound S>=P-H. The
sought upper bound would force zero flux (and contradict the retained
nonzero trace), but has not been established. The exact nodal matrix
and its finite signed kernels supply only (3)–(4); the admissible
dilation supplies the compatible lower bound (6). This fails the
approved continuation test for this implementation. It is stronger
evidence than a generic shifted-matrix example because the calculation
retains the actual c, nu_rho, pole, prime weights and equality atoms;
it is still not a counterexample to their possible arithmetic sign
criterion or to RH. Other independent gaps remain unchanged.

### Separate conceptual application audit, 2026-10-30

The pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-30-l523-first-critical-audit-scope.md`
covers this first audit. Equations (1)–(10) pass with all the stated
hypotheses retained. This verifies a conditional specialization and
its limited sign conclusion, without improving the estimate or
independently auditing the source manuscripts.

**Domains and weak tests.** The reference part form in L515 is a
Dirichlet form; its open interval and Lebesgue reference measure match
the cited FOT domain theorem. The complete signed perturbation is
bounded, so it changes neither this form domain nor the weak testing
class. Clipping v therefore gives p,q in Q_(I_a). The Lipschitz
partition bound gives their BV property, and L515's continuous zero
extension gives continuity and zero endpoint values. Since v is in
the associated operator domain, b(v,h)=<A_a v,h>=0 for every form
test h. In particular the tests p,q give both diagonal entries equal
to the off-diagonal entry beta; semidefiniteness gives beta>=0.
The cross term in the quadratic expansion is 2alpha gamma beta,
so the square in (2) and the factor 4 for |v| are correct. A zero
part forces beta=0. No contraction of b or division by p,q is used.

**Absolute convergence and the signed kernel.** With reference
energy q_G(f,f)=(1/2)integral integral (f(x)-f(y))^2 n(x-y),
Cauchy--Schwarz bounds the absolute mixed difference integral by
2 sqrt(q_G(p,p)q_G(q,q)). Disjointness p q=0 makes its negative
integrand the sum p(x)q(y)+p(y)q(x); each summand is nonnegative.
Tonelli and evenness consequently give (7), with no extra factor 2.
For the rho term the absolute integral is at most
||nu_rho||_TV ||p||_2 ||q||_2; the pole costs at most
sup_(|t|<=ell)|k(t)| ||p||_1 ||q||_1. Thus combining n and rho
and changing displacement are justified before any cancellation.
For either prime shift, Cauchy--Schwarz bounds the pairing, and
there are only finitely many retained n. Splitting positive and
negative displacements gives X(s), with the single integral in (3),
not twice that integral. The signed measure's negative pole becomes
+k in b(p,q), and its positive prime atoms become -w_n X(d_n).
The scalar term vanishes because p q=0. The checks
k(log(2))=3/sqrt(2), kappa(log(2))=4/(3sqrt(2)) and
kappa(s)~1/(2s) confirm the claimed change of coefficient sign.
They do not imply any sign for an untested overlap distribution.

**Correlation derivatives.** For fixed d the first difference
quotient tests Galerne's signed measure quotient for g against
f(.-d); the other tests the quotient for f with increment -h
against g(.+d), and hence has a minus sign. These are continuous
compact tests for either sign of h. The modulus of continuity gives

    |integral [f(y-d_1)-f(y-d_2)] Dg(dy)|
       <=omega_f(|d_1-d_2|)|Dg|(R).

It proves continuity of the derivative in d and hence the asserted
C1 property, including at the support boundary. For f=g=v, the
integral with v(y-d) is C_v'(d), and that with v(y+d) is -C_v'(d).
Thus L522's signed prime-pair formula is exactly -2w_n d_n C_v'(d_n).
Expanding v=p-q gives C_v=C_pp+C_qq-X without omitting either
same-sign term. No derivative of v as a function is assumed.

**Complete inward rescaling and limits.** The exact Fourier
identity is hat(U_r v)(xi)=r^(-1/2)hat v(xi/r); it changes the
multiplier to m(r xi). Two spatial changes of variables give
r^(-1)k((x-y)/r) for the pole and C_v(r d) for the plus shift.
The minus shift equals it because real autocorrelations are even.
These verify every factor and sign in (10). The fixed scalar
component of m has zero derivative since U_r is unitary. The
rho contribution remains included in the complete m; it has not
been discarded. The reference-domain dilation bounds in L516
extend this identity from the smooth core to the actual v.

Writing p_m(xi)=xi m'(xi), L516's bounded multiplier gives

    [m(r xi)-m(xi)]/(r-1)
      =(1/(r-1))integral_1^r p_m(t xi)dt/t.

Its absolute value is at most ||p_m||_infinity for r>1 and its
pointwise limit is p_m(xi). Plancherel and dominated convergence
give H. The pole quotient converges uniformly for |x-y|<=ell
to -k(x-y)-(x-y)k'(x-y), giving -P. The finite C1 prime sum
gives S. For d>=ell, C_v(d)=0 and C_v'(d)=0, also at equality
by C1 continuity. In the inward energy, r d>ell already makes
such an atom's correlation zero for r>1; this is consistent with
the possibly nonzero finite-r equality term in L522's different,
mixed pairing. Cutoff equality d=2A>ell is inactive and retained;
w_n=0 contributes zero. No growing-cutoff interchange is involved.

Finally U_r v-v is a permissible form test, so its mixed term
with v vanishes exactly. This proves E(r)=b(U_r v-v,U_r v-v)>=0
and E(1)=0. The right derivative is therefore nonnegative. L516's
audited flux identity identifies it with a(tau_L^2+tau_R^2),
strictly positive by the retained left trace assumption. It yields
S>=P-H, not the upper bound needed for vanishing flux. The possible
linear energy growth does not assert form differentiability of the
vector-valued dilation curve. Outward vectors have larger support
and cannot be tested against the assumed fixed-interval positivity.

The audit adds no mathematical input or DAG edge. Nonresonance,
ell>log(2), the nonzero trace and all upstream BV/source conditions
remain hypotheses even where individual calculations need less.
Nullvector existence, the arithmetic upper bound, uniform positive-
eigenvalue family control and actual-Xi realization remain unresolved.
The static-compression stop is verified only at its stated scope;
no impossibility result for the full null equation or RH follows.

## Mathlib

Full matching coverage of this conditional signed-kernel compression
and BV dilation specialization is not checked. The source inputs are
the precisely cited Dirichlet-form lattice theorem and BV measure
convergence; supporting steps are bilinear algebra, Cauchy–Schwarz,
finite signed convolution, changes of variables and dominated
convergence. No Mathlib declaration or Lean proof was inspected, and
unknown coverage is not an absence claim. The local specialization
passes the separate application audit above; L515, L516 and L522 keep
their existing source and audit qualifications.
