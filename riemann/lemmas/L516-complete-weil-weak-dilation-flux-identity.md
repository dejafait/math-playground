# L516 — Complete Weil weak-dilation flux identity

## Hypotheses

Fix 0<a<A<infinity. Work with real functions, zero extension from
I_a=(-a,a), and Fourier transform hat f(xi)=integral f(x)e^(-i xi x) dx.
Write T_t f(x)=f(x+t), U_r f(x)=sqrt(r)f(rx), and

    m(xi)=Re psi(1/4+i xi/2)-log(pi),
    k(t)=2 cosh(t/2), ell_n=log(n), w_n=Lambda(n)/sqrt(n).

On functions supported in I_A, let b be the real symmetric bilinear
form obtained by polarizing the complete form recorded in L512:

    b(f,f)=(1/(2pi)) integral m(xi)|hat f(xi)|^2 dxi
           + integral integral k(x-y)f(x)f(y) dx dy
           - sum_(ell_n<=2A) w_n <f,(T_ell_n+T_(-ell_n))f>.    (1)

The pole integral is exactly 2 hat f(i/2)hat f(-i/2) for real f.
All prime powers in the displayed range are retained, including
equality at the cutoff; terms beyond it have no overlap.

Retain the complete-form identification from bramble_trace,
*Boundary traces and support variation for localized Weil operators*,
paper 67 v1, 27 October 2026,
[(2.1), (3.1)–(3.5)](https://rstation.ai/problems/riemann_hypothesis/papers/67).
In the notation of L513–L515 it is

    b(f,g)=q_G(f,g)-c<f,g>-<f,mu_A*g>, c=log(2pi),
    G=(1/2)log(1-D_x^2), n(t)=exp(-|t|)/(2|t|),
    mu_A=nu_rho+sum_(ell_n<=2A)w_n(delta_ell_n+delta_(-ell_n))
                       -k(t)1_(|t|<=2A)dt,                  (2)

where nu_rho has even density
rho(t)=exp(-t/2)/(1-exp(-2t))-exp(-t)/(2t), t>0, and is finite.
The form domain is the zero-extension smooth-core logarithmic
domain Q_(I_a); its realization is

    A_a=G_(I_a)-cI-R_(I_a)K_(mu_A)E_(I_a),
    Dom(A_a)=Dom(G_(I_a)).

As in L512, the full-Weil identification and its imported manuscript
proof are not independently audited here. L512's activation theorem
and the source's collar resolvents and support-derivative law are not
used. The conditional model (2) has the audited fixed-domain,
bounded-data and trace inputs L513–L515.

Let A_a u=lambda u, with u real and ||u||_2=1. Neither positivity of
lambda, simplicity, nor a spectral gap is needed for the identity.
By L515 and L513, use its continuous zero extension and traces

    tau_R=lim_(t->0+) sqrt(log(1/t))u(a-t),
    tau_L=lim_(t->0+) sqrt(log(1/t))u(-a+t).

The gate is the pre-existing EXPLORE assessment
`drafts/literature/2026-10-30-weil-finite-dilation-remainder-test.md`.
This is a local derivation under that gate. The separate conceptual
audit below passes the fixed-vector identity under the retained
realization. POTENTIALLY_NEW records only the absence of an adequate
match in the saved search; it does not certify originality.

## Conclusion

Put u_r=U_r u, v_r=U_(1/r)u, for 1<r<A/a, and define

    H(u)=(1/(2pi)) integral xi m'(xi)|hat u(xi)|^2 dxi,
    P(u)=integral integral [2cosh((x-y)/2)
                          +(x-y)sinh((x-y)/2)]u(x)u(y) dx dy,
    S_r(u)=sum_(ell_n<=2A) w_n/(r-1)
          *<u,(T_(ell_n/r)+T_(-ell_n/r)
                         -T_ell_n-T_(-ell_n))u_r>.           (3)

H and P are finite. The full signed sum S_r has a finite one-sided
limit S(u), and

    lim_(r->1+) [b(u,v_r)-b(u,u_r)]/(r-1)
                 =-a(tau_L^2+tau_R^2),                      (4)
    a(tau_L^2+tau_R^2)=H(u)-P(u)+S(u).                      (5)

No individual derivative of a prime autocorrelation, H1 regularity,
or differentiability of r->u_r in the form norm is asserted. The
combined weak difference (4), not the derivative of either pairing
separately, is what is proved. At an exact activation ell_n=2a,
that atom pair's contribution to S_r is O(1/log(1/(r-1))) and
tends to zero. All its finite-r terms remain in (3).

Here is the explicit remaining arithmetic criterion. On the
hypothetical family from the approved target, a_0<=a<A,
||u_a||_2=1, 0<lambda(a)<=lambda_0, it would suffice to prove
with one finite K>=0 independent of a and lambda(a) that

    limsup_(r->1+) S_r(u_a)
                <=P(u_a)-H(u_a)+K lambda(a).                (6)

Then (5) gives tau_L(u_a)^2+tau_R(u_a)^2
<= (K/a_0)lambda(a). Equivalently, the finite sum in the numerator
of (3) must be at most
(r-1)[P(u_a)-H(u_a)+K lambda(a)]+o_a(r-1).
The little-o need not be uniform for this pointwise implication;
the same K for the whole family is essential.

Inequality (6) is **not proved**. It states the signed cancellation
still needed and, through (5), is equivalent to the corresponding
a-weighted flux bound. It is not an independent positivity input.
There is no bound on its error proportional to lambda, no uniform
dilation-limit rate, no all-support positivity or Xi conclusion.
The source realization, multiple branches, and later support/Xi
transfer remain separate from this intermediate identity.

## Proof

### Admissible dilations and restrictions

Let Psi(xi)=(1/2)log(1+xi^2). For r>=1,

    Psi(r xi)<=Psi(xi)+log(r), Psi(xi/r)<=Psi(xi).

The Fourier change of variables therefore bounds U_r and U_(1/r)
on the whole logarithmic form domain, locally uniformly in r.
Dilate smooth-core approximations to u: U_r maps them into
C_c^infinity(I_a), while U_(1/r) maps them into
C_c^infinity(I_(ar)). The same inequalities pass their convergence
to the form norm. Thus u_r is an admissible weak eigen-equation test,
and v_r belongs to Q_(I_(ar)), embedded in Q_(I_A).
The dilation group is strongly continuous on L2: this follows first
for smooth compactly supported functions by dominated convergence
and then for arbitrary L2 functions by density and unitarity.
In particular u_r->u in L2, with no derivative assumption.

Restriction of v_r to I_a and to the two exterior collars is also
admissible in the respective part domains. Here are both auxiliary
half-line embeddings explicitly. Choose B>ar. Since v_r is in
Q_(I_(ar)), its same smooth-core approximants put its zero extension
in Q_(-B,infinity). Translate x to x+B and apply L514 (1) with
ell=B+a. The restrictions f=v_r 1_(-B,a) and g=v_r 1_(a,infinity)
belong to Q_(-B,a) and Q_(a,infinity), respectively.

Reflect f by x=a-z. This maps Q_(-B,a) to Q_(0,a+B), which embeds
in Q_(0,infinity) using the same smooth core. Apply L514 (1) again,
now with ell=2a. Its interval part, reflected back, is v_r 1_(-a,a)
in Q_(I_a); its half-line part is v_r 1_(-infinity,-a) in
Q_(-infinity,-a). Thus the weak interior test is admissible before
the eigen-equation is used. The exterior pieces have finite
whole-line logarithmic energy and are supported in [a,ar] and
[-ar,-a]. L514's bounded-interval core-density consequence, proved
there using (7)–(8), puts them in Q_(a,ar) and Q_(-ar,-a).
Those domains embed in Q_(I_A) by their smooth cores.

L514's cross-form identity, after the same translations and
reflections, gives the kernel -n(x-y) between the interior and
each collar. All these are identities for form limits, not just
smooth tests. The bounded perturbation in (2) changes none of
these domains.

L515 gives bounded u and bounded G_(I_a)u. L514 supplies the
half-line operator splits, and L513 then gives the stated traces.
In particular, for a fixed sufficiently small epsilon>0,

    |u(a-t)|+|u(-a+t)|<=C_u/sqrt(log(1/t)), 0<t<epsilon.      (7)

All constants in this proof may depend on this fixed a and u.

### Exact exterior pairing

For x outside I_a set

    F(x)=-integral_(I_a) n(x-y)u(y)dy-(mu_A*u)(x).            (8)

The first integral is absolutely defined at each point off the
closed interval. Its cross operator into either complementary
half-line is bounded on L2 by L514 (with reflection on the left).
For the continuous compactly supported representative of u, the
pointwise convolution in the second term is bounded everywhere by
||mu_A||_TV ||u||_infinity and agrees with its L2 definition. It is
continuous by dominated convergence against |mu_A|. Thus the collar
pairing agrees with the continuous cross form and is absolutely
integrable; the later rescaling uses this fixed representative.

Write v_r=v_in+v_out using the admissible restrictions above.
The weak equation applies to v_in. Formula (2) and the cross-form
identity give b(u,v_out)=integral F(x)v_out(x)dx; the scalar term
has disjoint supports. Since u vanishes on the collars,

    b(u,v_r)=lambda<u,v_r>+integral_(I_(ar) minus I_a) F v_r,
    b(u,u_r)=lambda<u,u_r>.

Real symmetry and unitarity give
<u,U_(1/r)u>=<U_r u,u>=<u,U_r u>. Consequently

    b(u,v_r)-b(u,u_r)
            =integral_(I_(ar) minus I_a) F(x)v_r(x)dx.       (9)

No equation is imposed in the collars, and no unsigned estimate
has replaced the complete perturbation in this exact identity.

### Exterior singularity from the actual traces

At the right endpoint, write y=a-t. We claim

    F(a+s)=-tau_R sqrt(log(1/s))+o(sqrt(log(1/s)))            (10)

as s decreases to zero, with the analogous left formula. This is
proved directly from the trace, not imported from a collar theorem.

Fix 0<epsilon<min(a,exp(-2)). The part with t>=epsilon in
integral_0^(2a) n(s+t)u(a-t)dt is bounded as s->0.
Replacing exp(-(s+t))/(2(s+t)) by 1/(2(s+t)) on t<epsilon
also has bounded error, since (1-exp(-z))/z<=1 and u is bounded.
The normalized scalar integral is

    J_epsilon(s)=(1/2)integral_0^epsilon
                         dt/[(s+t)sqrt(log(1/t))]
                ~sqrt(log(1/s)).                            (11)

Here is the leading-constant check. For s<epsilon^2, the part
0<t<s is at most 1/[2sqrt(log(1/s))]. On s<t<epsilon, replacing
1/(s+t) by 1/t has error at most
(1/2)integral_s^epsilon s/[t^2 sqrt(log(1/t))]dt.
Split at sqrt(s). The lower part is O(1/sqrt(log(1/s))) and the
upper part is O_epsilon(sqrt(s)). The integral with 1/t equals
sqrt(log(1/s))-sqrt(log(1/epsilon)), proving (11).

Now u(a-t)=[tau_R+e(t)]/sqrt(log(1/t)), with e(t)->0.
Given eta>0, choose a smaller cutoff where |e(t)|<=eta.
Equation (11) bounds the error below that cutoff by
eta sqrt(log(1/s))(1+o(1)); the remaining fixed t range gives a
bounded error. Let eta decrease to zero. The finite-measure term
in (8) is bounded, so it does not change the leading coefficient.
This proves (10), including tau_R=0, and also the bound
|F(a+s)|<=C sqrt(log(1/s)) near zero. Reflection proves both
statements with tau_L at -a-s.

Set delta=a(r-1), L=log(1/delta), and s=delta y. On the right collar,

    v_r(a+s)=r^(-1/2)u(a-(delta-s)/r), 0<s<delta.

For each 0<y<1, the product F(a+delta y)v_r(a+delta y)
tends to -tau_R^2. Indeed the ratio of its two logarithmic
normalizations is

    sqrt[(L+log(1/y))/(L+log(r)+log(1/(1-y)))]->1.

By (7) and (10), its absolute value is at most a fixed constant
times sqrt(1+log(1/y)) when L>=1. This is integrable on (0,1).
Dominated convergence therefore gives

    (1/delta)integral_a^(ar) F(x)v_r(x)dx ->-tau_R^2.

The same proof on the left gives -tau_L^2. Since delta/(r-1)=a,
(9) proves (4). This argument preserves the endpoint contribution
without a smooth approximation being asserted to preserve traces.

### Exact complete-form change of variables

Apply the same outward dilation U_(1/r) to both arguments of b.
Since u=U_(1/r)u_r and v_r=U_(1/r)u, its Fourier multiplier
becomes m(xi/r), its pole kernel becomes r k(r(x-y)), and each
translation T_ell becomes T_(ell/r). Change of variables first
establishes these identities on the smooth core. The logarithmic
form bounds above, bounded kernels on the compact support, and
bounded translations extend them to u_r,u. Symmetry of b yields

    b(u,v_r)-b(u,u_r)=M_r+P_r-(r-1)S_r(u),                  (12)
    M_r=(1/(2pi))integral [m(xi/r)-m(xi)]
                                  conjugate(hat u(xi))hat u_r(xi) dxi,
    P_r=integral integral [r k(r(x-y))-k(x-y)]u(x)u_r(y) dx dy.

The Fourier integral is real for real u,u_r. The pole kernel is
the full k, not a discarded or unsigned rank-two term. The fixed
finite prime set ell_n<=2A suffices: all original pairings have
supports in I_A, and no translation outside this set has overlap
in their scaled expression. This also follows directly from
ell_n<=a(1+r)<2A for a potentially overlapping scaled term.

### Smooth terms and existence of the signed aggregate limit

The function p(xi)=xi m'(xi) is real and bounded on R. For an exact
standard input use [NIST DLMF 5.15.8](https://dlmf.nist.gov/5.15.E8):
psi'(z)=1/z+O(|z|^(-2)) as |z|->infinity in any fixed sector
|arg z|<=pi-epsilon. Our line z=1/4+i xi/2 stays in such a
sector and has no pole. Analyticity on compact portions and
m'(xi)=Re[(i/2)psi'(1/4+i xi/2)] show p is bounded and tends
to 1 at both frequency infinities. At xi=0 it is zero.
These hypotheses justify this use of the cited asymptotic.

In particular

    [m(xi/r)-m(xi)]/(r-1)
           =-(1/(r-1))integral_1^r p(xi/t)dt/t

is bounded uniformly in xi and r near 1, and tends pointwise
to -p(xi). Dominated convergence gives strong convergence of
these multipliers on each fixed L2 vector. Combining this with
u_r->u in L2 and Plancherel proves

    M_r/(r-1)->-H(u).                                       (13)

Similarly [r k(rt)-k(t)]/(r-1) converges uniformly on compact
t sets to k(t)+t k'(t)=2cosh(t/2)+t sinh(t/2).
All spatial supports here lie in I_A, and L2 convergence of u_r
implies L1 convergence on this fixed finite interval. Boundedness
of the kernels and their uniform convergence prove

    P_r/(r-1)->P(u).                                        (14)

Equations (4), (12)–(14) prove convergence of the *entire signed*
S_r, and give -a(tau_L^2+tau_R^2)=-H+P-S. This is (5).
We have not differentiated a translation on a rough eigenfunction,
split the limit into individual primes, or assumed a common rate
as a or the eigenfunction varies.

### Exact activation and absent atoms

For this limiting calculation take r sufficiently close to 1, in
particular r<2. If ell=2a, the unscaled pairings <u,T_(+/-ell)u_r> vanish,
because the support widths sum to a+a/r<2a. For the plus scaled
shift the overlap is x=-a+t, 0<t<delta/r, and its integrand is

    u(-a+t)sqrt(r)u(a-(delta-r t)).

Both inward distances are at most delta. Bound each factor using
(7); the product is O(1/log(1/delta)), uniformly on this interval.
The overlap length is delta/r, so the pairing is
O(delta/log(1/delta)). The minus shift has the same bound.
After division by r-1 and multiplication by its fixed weight,
this proves the asserted O(1/log(1/(r-1))) contribution.
The argument permits zero traces and either sign of the product.
For ell>2a a fixed atom has no overlap in either scaled or
unscaled pairing once r is sufficiently close to 1. There are
only finitely many atoms in (3), so this covers them all without
discarding a newly activating term at finite r.

### The remaining estimate and the scalar-shift check

Under (6), use the proved limit in (5) at each fixed a. It gives
a(tau_L^2+tau_R^2)<=K lambda(a); divide by a>=a_0. This proves
only the stated conditional implication. Absolute bounds on H,
P, or S do not give the required cancellation to accuracy O(lambda).
In particular, convergence of S_r without a sign estimate does
not establish (6), even along a simple branch.

Adding a scalar dI to the operator adds d<f,g> to the form.
Its contribution to (9) is exactly zero because the two real
overlaps are equal. It leaves the eigenfunction, its traces, and
all terms in (5) unchanged (the derivative of m+d is m'), while
replacing lambda by lambda+d. Thus the identity itself cannot
supply a factor vanishing with the eigenvalue. This agrees with
the scalar-shift obstruction recorded in paper 67 Section 9.
No positivity of the complete form is an input to any step above.

The local result is the mixed weak difference and its explicit signed
prime remainder. The actual arithmetic estimate (6) is outstanding.
This is not a complete candidate proof of RH or a new verified
positivity range.

### Separate conceptual audit, 2026-10-30

The pre-existing EXPLORE assessment
`drafts/literature/2026-10-30-l516-weak-dilation-audit-scope.md`
covers this audit. Equations (4)–(5), signed aggregate convergence
and the exact-activation conclusion pass for every fixed eigenvector
in the stated model, with either eigenvalue sign and zero traces
allowed. The two auxiliary half-line embeddings are now explicit
above; this expands the domain justification without changing the
statement, normalization or mathematical inputs.

In detail, the dilations act boundedly on the Fourier form norm and
map the actual interval cores to the asserted cores. The first split
does not directly furnish the interior test: the reflected second
split at 2a is essential. Both uses of L514 have positive interval
length and a previously established half-line form-domain member.
Its bounded-interval density consequence is applied only after the
collar restrictions have finite energy. The exterior pairing is
absolutely integrable: L514's positive cross-kernel bound applies to
|u| and |v_out|, and finite-measure convolution is bounded because
L515 supplied bounded u before any trace application. Hence (9)
uses the weak equation only on Q_(I_a), never on an exterior test.

The coefficient in (11) is exactly one: the factor 1/2 from n
cancels the factor two in the primitive of 1/[t sqrt(log(1/t))].
For 0<s<epsilon^2 the two replacement-error bounds in (11) are
O(1/sqrt(log(1/s))) and O_epsilon(sqrt(s)); neither hides a leading
constant. With s=delta y, the complete collar product is bounded by
C sqrt((L+log(1/y))/L)<=C sqrt(1+log(1/y)) for L>=1.
The denominator's additional log(r)+log(1/(1-y)) is nonnegative,
so the same bound controls the y=1 end too. Its integral is finite
by y=exp(-z). The trace errors tend to zero for each 0<y<1 even
when a trace is zero. Thus dominated convergence gives -tau_R^2
and -tau_L^2 with delta/(r-1)=a; no parity assumption or
trace-preserving smooth approximation enters.

In the complete-form transformation, U_(1/r) changes m to m(./r),
k(t) to r k(rt), and T_ell to T_(ell/r). Symmetry of each plus/minus
translation pair gives exactly the sign -(r-1)S_r in (12).
A scaled prime term can overlap only if ell<=a(1+r)<2A;
an unscaled one requires ell<=a(1+1/r). Thus the fixed prime cutoff
is sufficient for every allowed r, including its equality atoms.
The cited trigamma sector contains both frequency tails. It makes
p=xi m' bounded, so the quotient multipliers converge strongly on
the fixed L2 vector while u_r converges in L2. The pole quotient
converges uniformly on the fixed compact difference interval.
These are separate justified limits; (12) then forces convergence
of the signed aggregate, without asserting convergence prime by prime.

At ell=2a the two scaled overlaps have length delta/r. Both inward
distances are <=delta, so their products are bounded by C/L, also
at either end of the overlap. Their quotient contributions are
O(1/L); unscaled overlaps are empty. Every ell>2a is eventually
absent, simultaneously because the retained prime set is finite.
These observations justify the limiting activation assertions without
deleting any finite-r term.

Finally (6) is equivalent, for this family, to the a-weighted flux
bound by (5). A single K is still required across the family; fixed-a
limits and bounded absolute terms supply none. The scalar-shift check
is valid because the two real overlaps cancel identically. This audit
certifies the conditional local identity, not its arithmetic sign,
source realization, source collar/support proofs, multiple-branch
continuation or Xi transfer. This validates the previously stated
local identity; it does not certify originality.

## Mathlib

Full matching coverage of this logarithmic weak-dilation identity
with signed translated atoms has not been checked. Supporting
inputs are Plancherel, strong continuity of unitary dilations,
dominated convergence, the cited trigamma asymptotic, and the
qualified domain and trace results in L513–L515. No Mathlib
declaration or Lean proof was inspected. Unknown coverage is not
evidence of absence. The local identity has the separate conceptual
audit above; the imported source manuscripts remain unaudited.
