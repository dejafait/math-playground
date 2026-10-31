# L518 — Full arithmetic residual of the raw renewal-adjoint cutoffs

## Hypotheses

Fix ell=2a>0 and A>a. Translate L516's retained complete model to
I=(0,ell), using zero extension E_I and the Fourier convention
hat f(xi)=integral_R f(x)exp(-i xi x) dx. Set

    Psi(xi)=(1/2)log(1+xi^2), n(t)=exp(-|t|)/(2|t|),
    c=log(2pi), k(t)=2cosh(t/2),
    d_n=log(n), w_n=Lambda(n)/sqrt(n),
    mu_A=nu_rho+sum_(n>=2,d_n<=2A) w_n(delta_(d_n)+delta_(-d_n))
                       -k(t)1_(|t|<=2A)dt,
    rho(t)=exp(-t/2)/(1-exp(-2t))-exp(-t)/(2t), t>0.

Here nu_rho has the even density rho; terms with w_n=0 contribute
zero. The finite real even signed measure and the full realization
are precisely those retained in L516:

    Bf=c f+R_I(mu_A*E_I f),
    A_I=G_I-B, Dom(A_I)=Dom(G_I).

G_I is the smooth-core part operator of the Levy form with multiplier
Psi from L513–L515. The complete-Weil identification and the original
manuscript proof remain unaudited inputs. No collar law, support
derivative, positivity or spectral gap is assumed.

Use the renewal function V and density v with the exact normalization
of L513 (3). Define the zero-extended, integrable weights

    f_L(x)=v(x)1_(0,ell)(x), f_R(x)=f_L(ell-x),
    E_L(x)=integral_ell^infinity v(y)n(y-x)dy, 0<x<ell.

Let chi be a smooth real function with 0<=chi<=1, chi(t)=0 for t<=1
and chi(t)=1 for t>=2. For 0<epsilon<ell/4 put

    phi_epsilon(x)=chi(x/epsilon)chi((ell-x)/epsilon)v(x), x in I,

and extend it by zero. These are the raw density cutoffs proposed in
the unchanged EXPLORE gate
`drafts/literature/2026-10-30-weil-nullspace-renewal-adjoint-coverage.md`.
No bounded correction or new adjoint construction is included.

Only for the pairing conclusions, assume a real u in Dom(A_I) with
A_Iu=0 and ||u||_2=1. In particular this includes the proposed simple
nullvector at a finite first-zero radius if it exists. Simplicity and
the first-zero property are not needed for the calculation. They are
not proved, and no existence of such a vector is asserted.

## Conclusion

The raw weights are in L1(I) but not in L2(I), hence not in the form
or operator domain. The full distributional residual of the left
weight on the open interval is the following L1 function:

    R_L(x)=E_L(x)-c v(x)-integral_0^ell rho(x-y)v(y)dy
       -sum_(n>=2,d_n<=2A) w_n[f_L(x-d_n)+f_L(x+d_n)]
       +integral_0^ell k(x-y)v(y)dy.                         (1)

Values at the finitely many atomic displacement points are immaterial.
In distributions on I,

    A_I phi_epsilon -> R_L.                                 (2)

The notation in (2) applies the closed operator only to the smooth
cutoffs. It does not put f_L in its domain. The limiting distribution
can equivalently be denoted (G f_L-c f_L-mu_A*f_L)|_I, where G is the
whole-line Fourier multiplier acting on distributions.

There is no coefficientwise cancellation of this residual:

    R_L(x)=-c v(x)+O(1)                         as x->0+;    (3)
    R_L(d_n+s)=-w_n v(s)+O(1)                   as s->0+    (4)

for each prime power with 0<d_n<ell. The constants may depend on the
fixed interval, A and the selected n. An atom with d_n=ell, as well
as one with d_n>ell, acts as zero on every interior cutoff and on f_L
after compression; it has not been dropped from (1).

Reflection gives R_R(x)=R_L(ell-x). No nonzero real linear combination
alpha R_L+beta R_R is the zero distribution on I. Thus neither raw
weight, nor a nonzero linear combination of the pair, is an interior
distributional null-solution for the full operator.

For the assumed nullvector, L515 and L513 give bounded u, bounded
h=G_Iu=Bu, and both normalized endpoint traces. All integrals below
are absolutely convergent, and the actual weak cutoff equation has
the limit

    0=lim_(epsilon->0) <u,A_I phi_epsilon>
      =tau_L(u)+integral_0^ell u(x)R_L(x)dx.                 (5)

More precisely,

    lim_(epsilon->0) integral_I u(x)[G_I phi_epsilon(x)-E_L(x)]dx
       =tau_L(u).                                          (6)

Reflection gives the same identities for tau_R and R_R. Distributional
convergence against interior smooth tests therefore does not justify
discarding the trace term in the pairing with this boundary-reaching u.

This is a negative result for the proposed raw-weight cancellation
implementation. Equations (3)–(4) expose a nonzero full arithmetic
residual; (5) still allows its pairing with a particular nullvector
to vanish. Neither tau_L=0, tau_R=0 nor their nonvanishing has been
proved. The endpoint question, the O(lambda) branch rate, trace-topology
convergence, multiple branches, collars, actual-Xi transfer and all-degree
positivity remain open. The separate conceptual audit below passes this
fixed-model result; the imported manuscript proofs remain unaudited.
POTENTIALLY_NEW means only that the saved bounded search
did not supply a matching full-arithmetic result, not certified novelty.

## Proof

### Reused renewal facts and the missing domain

The primary input already assessed for this target is Grzywny–Ryznar,
*Potential theory of one-dimensional geometric stable processes*,
[arXiv:1107.0745v1](https://arxiv.org/html/1107.0745v1), Proposition 3.2
and Lemma 4.1, including parameter two and its separate b=1 case.
Proposition 3.2 makes v completely monotone on (0,infinity); in
particular it is smooth, positive and decreasing there. Lemma 4.1
gives, for all sufficiently small positive x, constants c_1,c_2>0 with

    c_1/[x(log(1/x))^(3/2)] <= v(x)
                           <= c_2/[x(log(1/x))^(3/2)].       (7)

L513's time normalization is v=sqrt(2)v_GR. This changes the two
comparison constants but not (7). Its V(0)=0 and V'=v give
integral_0^ell v=V(ell)<infinity. The nonzero constant component
of v at infinity is retained; no decay of v there is assumed.
These are imported facts, not new renewal estimates or an extension
of the inapplicable positive-power-scaling weak-dual theorem.

The square of the lower bound in (7) is not integrable at zero:
after t=log(1/x), its integral is bounded below by a positive multiple
of integral^infinity exp(t)t^(-3)dt=infinity. Thus f_L is in L1 but
not L2. Reflection proves the same for f_R. Since both part-form and
operator domains are subspaces of L2, neither uncut weight is a weak
test. Smoothness of v makes every phi_epsilon a member of C_c^infinity(I).
Moreover 0<=phi_epsilon<=f_L and phi_epsilon->f_L pointwise on I, so

    ||phi_epsilon-f_L||_L1(R) -> 0.                          (8)

### The reference operator's complete interior distribution

For psi in C_c^infinity(I), its whole-line G image is bounded. Indeed
the absolutely convergent kernel formula has integrand
[psi(x)-psi(x-t)]n(t); a uniform Lipschitz bound controls |t|<1,
and boundedness of psi controls the integrable tail. Its Fourier
image Psi hat psi is in L2, so the part-form representation also
puts psi in Dom(G_I), with G_I psi=(G psi)|_I. L514 supplies its
half-line operator-domain split. These facts verify every additional
premise needed to apply L513 to psi, including bounded h.

The trace of this compactly supported psi is zero. L513 (T) consequently
gives the exact identity

    integral_I v(x)(G_I psi)(x)dx
       =integral_I psi(x)E_L(x)dx.                           (9)

All terms are absolute integrals by L513. In particular, because
v(y)<=v(ell) for y>=ell, L513 (9)'s cross integral yields

    integral_I E_L(x)dx <= v(ell)/2.                         (10)

Thus the distribution G f_L, tested against compact interior psi,
is exactly E_L. This uses the already proved signed trace for smooth
data, not an unproved assertion that v is an admissible harmonic test.
It also keeps the whole exterior tail y>ell.

For each epsilon, symmetry of G on smooth functions gives
<G phi_epsilon,psi>=<phi_epsilon,G psi>. By (8) and boundedness of
G psi on I, this tends to <f_L,G psi>=<E_L,psi>. Hence
G_I phi_epsilon->E_L in distributions on I. Finite signed convolution
has the whole-line L1 bound

    ||mu_A*(phi_epsilon-f_L)||_1
                    <=||mu_A||_TV ||phi_epsilon-f_L||_1 ->0. (11)

The scalar term has the same convergence. This proves (2), with
residual E_L-Bf_L. Expanding the exact measure gives (1): because
|x-y|<ell<2A on I times I, the pole cutoff is identically one in
its integral. All atomic terms and the nu_rho term are retained.
Equations (10)–(11) also show R_L is in L1(I).

### Noncancellation of the actual coefficients

The density rho has a removable singularity at zero, with
rho(0)=3/4. In fact the first term in its definition equals
1/(2t)+1/4+O(t), while exp(-t)/(2t)=1/(2t)-1/2+O(t).
It is therefore bounded on every fixed compact interval after even
extension. The continuous convolution in (1) is bounded by
sup_(|t|<=ell)|rho(t)| V(ell). The pole convolution is bounded by
2cosh(ell/2)V(ell). Both bounds hold throughout I.

For 0<x<ell/2, E_L(x) is bounded uniformly by

    v(ell) integral_ell^infinity n(y-ell/2)dy < infinity.     (12)

There are only finitely many atomic displacements in mu_A, all at
least log(2). For x sufficiently close to zero, f_L(x-d_n)=0;
each f_L(x+d_n) is either zero or bounded by v(d_n). In particular
d_n=ell gives zero, rather than an endpoint point mass. These facts
leave only -c v(x) unbounded in (1), proving (3). Since c>0 and
v(x)->infinity, R_L is strictly negative for all sufficiently small
positive x. It is not the zero distribution.

Fix a prime power with d=d_n in (0,ell). The selected term
-w_n f_L(x-d) equals -w_n v(s) at x=d+s. Every other displacement
is distinct. On a sufficiently small right neighborhood of d, its
argument either stays away from zero inside I or is outside I;
crossing ell produces at most a bounded jump. The scalar term is
bounded there, the continuous and pole terms were already bounded,
and E_L is bounded away from ell by the same argument as (12).
This proves (4). For d_n>=ell both x-d_n and x+d_n lie outside I
for almost every x in I, proving the equality-cutoff qualification
for f_L and all phi_epsilon.

To check combinations of the left and right weights, also bound (1)
near the opposite endpoint. Writing x=ell-s and y=ell+r gives

    E_L(ell-s)=integral_0^infinity
                v(ell+r)exp(-(r+s))/(2(r+s))dr
              =O(1+log(1/s)), s->0+.                        (13)

Split the integral at r=1 and use v(ell+r)<=v(ell) to justify this
bound. All other terms in (1) are bounded for sufficiently small s:
there are finitely many displacements d_n<ell, each then separated
from ell, while equality and larger displacements are zero. Thus
R_L(ell-s)=O(1+log(1/s)). The even kernels and symmetric atomic
measure commute with reflection, giving R_R(x)=R_L(ell-x).

From (7), (1+log(1/x))/v(x)->0. Dividing a putative equality
alpha R_L+beta R_R=0 almost everywhere by v(x) as x->0+ therefore
gives -alpha c=0. The displayed bounds make this implication uniform
on a sufficiently small endpoint interval, so an almost-everywhere
identity suffices. Reflection gives -beta c=0 as x->ell-. Hence
alpha=beta=0. This excludes coefficient cancellation for the whole
raw pair without assuming anything about the signs of eigenvectors.

### The admissible cutoff equation and its remaining trace term

Now assume the nullvector in the hypotheses. L515 gives bounded u
and h=G_Iu=Bu; L514 supplies the splits used by L513, and L513 gives
the continuous representative and finite traces. The weak equation
with the admissible phi_epsilon is

    <u,G_I phi_epsilon>=<h,phi_epsilon>,
    <u,A_I phi_epsilon>=0.                                  (14)

Dominated convergence against bounded h and (8) give
lim <u,G_I phi_epsilon>=integral_I h v. By (10) the pairing with
E_L is absolutely convergent. L513 (T), with its full exterior
term, now gives

    integral_I h v-integral_I u E_L=tau_L(u),                (15)

which proves (6). No passage from distributional convergence to a
pairing with u was used; (14) and the signed trace justify that
pairing limit independently.

Equation (11), boundedness of u and the scalar L1 convergence give
lim <u,B phi_epsilon>=integral_I u Bf_L. The equality
integral_I u Bf_L=integral_I f_L Bu is legitimate: the scalar part
is integrable, and for the measure part Tonelli's absolute bound is
at most ||u||_infinity ||mu_A||_TV V(ell); evenness supplies the
transpose. In particular all prime-power translations are included
in this interchange. Subtracting the two limits in (14), and using
R_L=E_L-Bf_L, proves (5). Reflection proves the right version.

Identity (15) alone would merely reproduce (T). The additional test
result is the explicitly nonzero full residual (1), its unavoidable
scalar and prime-power singularities (3)–(4), and the absence of any
nonzero cancelling raw pair. The cutoff identity yields
tau_L=-integral u R_L and tau_R=-integral u R_R, not annihilation
of those traces. The surviving remainder can still be orthogonal
to an unknown special eigenvector. No conclusion about that pairing
follows from a nonzero distribution alone. A repaired method would
need a new eigen-equation-specific input or a justified corrected
adjoint weight; neither has been constructed in this attempt.

### Separate conceptual audit, 2026-10-30

The pre-existing EXPLORE assessment
`drafts/literature/2026-10-30-weil-raw-renewal-residual-audit-coverage.md`
covers this review. Equations (1)–(6), the non-L2 exclusion and the
reflected noncancellation pass under the stated fixed-model hypotheses.
No statement, constant, sign or mathematical input needed repair.
This checks the local derivation, not the imported manuscript proofs
or any proposed zero-eigenvalue existence theorem.

First, L513 (3) uses precisely Psi=Psi_GR/2. Its reciprocal ladder
exponent, V and v are multiplied by sqrt(2), and the trace normalization
in (T) is one. The use of GR Proposition 3.2/Lemma 4.1 here needs only
complete monotonicity and (7), not a nonexistent decay of v at infinity.
The lower bound in (7) proves the asserted L2 divergence. Integrability
and (8) follow from V(0)=0 and the two cutoff factors, including the
one at ell. Every positive-epsilon cutoff is an admissible smooth test.

For clarity, the operator-domain step behind (9) also holds against
the full form domain. For compact smooth psi, the Fourier identity
q(psi,eta)=<G psi,eta> holds first for smooth eta and extends by
form-core approximation: q is continuous in form norm and G psi is
in L2. Thus psi belongs to Dom(G_I) with the asserted restriction.
The uniform Lipschitz and tail bounds make G psi bounded. L514 then
supplies the operator split, so every premise of L513 is satisfied.
The compact support gives zero trace. Consequently (9) identifies
the distribution without testing the weak equation with f_L itself.
The bound (10) follows by Tonelli from L513 (9) and monotonicity of v;
it retains the entire y>ell exterior tail, including its constant
renewal-density component.

The exact signs in (1) agree with L516 (2): the scalar, nu_rho and
positive atomic measure are subtracted, while the negative pole
measure gives the positive k convolution. Since ell<2A, the pole
cutoff is one on the whole difference interval, and nu_rho is never
truncated. Finite total variation and (8) justify (11) with no
pointwise convergence assertion at atoms. The shifts d_n=ell and
d_n>ell are zero almost everywhere after compression for each cutoff
and for f_L. No boundary delta mass is created by those translations.

The expansion rho(0)=3/4, the bounded compact pole kernel and V(ell)
bound both continuous convolutions. Near zero all active positive
shifts stay away from zero and all negative shifts vanish, so (12)
leaves exactly the singular term -c v(x). Near an interior d_n,
distinctness of the finite displacements isolates -w_n v(x-d_n);
possible crossings of ell only give bounded jumps. At the opposite
endpoint, (13) is at most logarithmic and every remaining term is
bounded on a sufficiently small fixed endpoint interval. Even at
ell=d_n that atom is identically absent after compression. Therefore
R_R(x)/v(x) tends to zero as x tends to zero, while R_L(x)/v(x)
tends to -c. These bounds hold off a null set uniformly near the
endpoint; they justify the linear-independence conclusion for
distributions represented by L1 functions, without evaluating at
their singular points. No estimate uniform in changing ell is claimed.

Finally L515 gives bounded u and h for an assumed nullvector of this
exact finite signed-measure model; L514 gives both domain splits.
For each epsilon, self-adjointness permits (14). Its limit follows
from ||phi_epsilon-f_L||_1 and bounded h, whereas the perturbation
limit follows from (11) and bounded u. The exterior pairing is bounded
by ||u||_infinity v(ell)/2. Transposition of the measure convolution
has absolute bound ||u||_infinity ||mu_A||_TV V(ell); evenness then
gives the stated equality, including every atomic translation.
L513 (T) supplies (15) with coefficient +1 for tau_L. Subtracting
the perturbation limit gives exactly 0=tau_L+integral u R_L, with
no missing boundary term. Reflection supplies the right identity.
Distributional convergence alone was not used for this limit.

The audit confirms only the raw implementation stop. It neither
proves nor disproves orthogonality of R_L or R_R to a particular
nullvector. Endpoint existence, trace convergence on moving intervals,
the O(lambda) rate and the full-Weil/collar/Xi qualifications remain
as stated. No new obstruction, positivity estimate or result beyond
the already recorded local calculation is claimed by this review.

## Mathlib

Full matching coverage of this singular-cutoff residual and boundary
pairing calculation has not been checked. The renewal inputs are
the cited GR Proposition 3.2/Lemma 4.1 with L513's normalization;
the local trace/domain/smoothing inputs retain their canonical source
qualifications. Supporting elementary tools are dominated convergence,
finite-measure convolution bounds, Fourier duality and reflection.
No Mathlib declaration or Lean verification is claimed. Unknown
coverage is not evidence of absence.
