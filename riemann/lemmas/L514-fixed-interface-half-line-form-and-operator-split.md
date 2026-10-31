# L514 — Fixed-interface half-line form and operator split

## Hypotheses

Fix ell>0, I=(0,ell), J=(ell,infinity), and H=(0,infinity).
All L2 spaces are complex, with inner products conjugate linear in
the first argument. Use hat f(xi)=integral_R f(x)exp(-i xi x) dx.
Set

    n(t)=exp(-|t|)/(2|t|), t!=0,
    Psi(xi)=(1/2)log(1+xi^2),
    q(f,g)=(1/2) integral_R integral_R
        conjugate(f(x)-f(y))(g(x)-g(y)) n(x-y) dx dy.

The whole-line form domain Q consists of the L2 functions of finite
q(f,f), with norm squared ||f||_2^2+q(f,f). For an open D, E_D
denotes zero extension. Define Q_D to be the closure of C_c^infinity(D)
in this whole-line form norm, identified with a subspace of L2(D).
Let q_D(f,g)=q(E_D f,E_D g), and let G_D be its nonnegative
self-adjoint operator. Write Q_+=Q_H and G_+=G_H. These are the
zero-extension smooth-core part forms stipulated in L513, not
subordination of an already killed Brownian generator.

The gate is the previously saved SPECIALIZE assessment
`drafts/literature/2026-10-30-weil-half-line-domain-split-coverage.md`.
This reproduces/specializes the compressed bounded-interval argument in
bramble_trace, *Boundary traces and support variation for localized
Weil operators*, paper 67 v1, 27 October 2026,
[Section 3.1, paragraphs after (3.6), and Section 3.3's use](https://rstation.ai/problems/riemann_hypothesis/papers/67).
The proof below supplies the half-line closure and operator-domain
application; it does not assume the manuscript's asserted split.

## Conclusion

Under the unitary restriction L2(H)=L2(I) direct-sum L2(J),

    Q_+ = Q_I direct-sum Q_J.                                  (1)

This is equality of domains, not an orthogonal decomposition of the
form. Define B:L2(J)->L2(I) by

    (Bg)(x)=integral_ell^infinity n(y-x)g(y) dy,  0<x<ell.

Then ||B||<=pi/2, B* has kernel n(y-x) from I to J, and

    q_+((f,g),(a,b))=q_I(f,a)+q_J(g,b)
                       -<f,Bb>-<g,B*a>.                      (2)
    |q_+((f,g),(f,g))-q_I(f,f)-q_J(g,g)|
                         <= (pi/2)(||f||_2^2+||g||_2^2).       (3)
    Dom(G_+)=Dom(G_I) direct-sum Dom(G_J),
    G_+(f,g)=(G_I f-Bg, G_J g-B*f).                           (4)

In particular, for every u in Dom(G_I), without an L-infinity
assumption, its extension U=(u,0) belongs to Dom(G_+) and

    (G_+U)(y)=(G_I u)(y),                       0<y<ell,
    (G_+U)(y)=-integral_0^ell n(y-z)u(z) dz,    y>ell,          (5)
    ||(G_+U)|_J||_2 <= (pi/2)||u||_2.

All operator equalities are L2 equalities. The exterior integral is
absolutely defined at each y>ell for an L2 representative. Reflection
u(x)->u(ell-x) preserves Dom(G_I), so (5) also supplies the reflected
split assumed in L513. Thus both of that lemma's split premises are
available; its additional boundedness and renewal inputs are unchanged.
L513's signed trace theorem is not used to prove (1)–(5).

This supplies no sign for the full Weil form, no boundedness of its
eigenfunctions, and no collar asymptotics or uniform inverse-trace
estimate near a first zero eigenvalue. Those inputs in L512 remain
independent. No new result beyond the cited standard-source
specialization, and no RH conclusion, is claimed.

## Proof

### Normalization and the imported density theorem

The nonnegative jump energy has Fourier representation

    q(f,f)=(1/(2pi)) integral_R Psi(xi)|hat f(xi)|^2 dxi.        (6)

Indeed Tonelli and Plancherel give the multiplier
integral_R(1-cos(xi t))n(t)dt. It equals
integral_0^infinity exp(-t)(1-cos(xi t))/t dt. Differentiation
in xi is justified by the integrable bound exp(-t); the derivative
is xi/(1+xi^2). Its value at xi=0 is zero, giving Psi. The same
Tonelli argument applies to arbitrary L2 functions with possibly
infinite energy. In particular Q is complete by its weighted Fourier
norm. Each stipulated core closure Q_D is closed and densely defined
on L2(D). Polarization defines the displayed sesquilinear forms.

Use Chen–Weth, *The Dirichlet Problem for the Logarithmic Laplacian*,
[arXiv:1710.03416v6, Section 3, Theorem 3.1 and (3.2)](https://arxiv.org/html/1710.03416v6):
on a bounded Lipschitz domain, compactly supported smooth functions
are dense in the zero-exterior short-range energy space H(Omega);
its energy norm controls L2. Their kernel (2.9) is
k(t)=1_(0<|t|<1)/|t| in dimension one, since c_1=1.
Write E_k for the energy with kernel k and the same factor 1/2
as q. The theorem extends to complex data by real/imaginary parts.
We import this density theorem, not its boundary-cutoff proof.

Here is the necessary comparison with the present positive multiplier.
The kernel difference m=n-k/2 is integrable, with

    A=||m||_1=integral_0^1 (1-exp(-t))/t dt
                         +integral_1^infinity exp(-t)/t dt<infinity.

At |t|<1, n>=exp(-1)k/2. Also n<=k/2+n 1_(|t|>=1).
Consequently, first as inequalities of nonnegative integrals,

    E_k(f,f)<=2 exp(1) q(f,f),
    q(f,f)<=E_k(f,f)/2+2||n 1_(|t|>=1)||_1 ||f||_2^2.        (7)

For finite energy one can also subtract the kernels:

    |q(f,f)-E_k(f,f)/2|<=2 A ||f||_2^2.                       (8)

The bound follows from
integral_R |f(x)-f(x-t)|^2 dx<=4||f||_2^2 and the factor 1/2.
Thus these energy norms with L2 added are equivalent. In particular,
if a zero-extended L2 function supported in a bounded interval has
finite q energy, the imported density theorem approximates it in
q+L2 by smooth tests in that interval. No comparison with the
indefinite multiplier log|xi|, and no unbounded-domain density theorem,
is being assumed.

### The actual bounded cross operator

Import the Carleman norm from Yafaev, *Spectral and scattering theory
for perturbations of the Carleman operator*,
[arXiv:1210.5709v2, (1.2)–(1.4) and Section 2.1, (2.1)–(2.3)](https://arxiv.org/html/1210.5709v2).
The operator C on L2(0,infinity) with kernel 1/(r+s) is unitarily
equivalent under the Mellin transform to multiplication by
pi/cosh(pi k); hence ||C||=pi. This theorem is imported without
reproving Mellin diagonalization.

Put r=ell-x in I and s=y-ell in J. Reflection and translation
are unitary in these coordinates. The transformed cross kernel is

    exp(-(r+s))/(2(r+s)),  0<r<ell, s>0.

It is one half of M C M followed by restriction to (0,ell), where
M multiplies by exp(-r). Each multiplication and restriction is a
contraction. Thus ||B||<=pi/2. The adjoint uses zero extension of
the reflected I function before M C M; hence it has exactly the
claimed kernel. The formula is first obtained on compact tests and
extends to L2. For fixed interior x (respectively y), the kernel
as a function on J (respectively I) is in L2, so Cauchy–Schwarz
also defines its absolutely convergent pointwise integral. Testing
on compact subsets identifies that formula with the L2 extension.

Applying the same positive kernel to |f|, |g| proves

    integral_I integral_J |f(x)||g(y)|n(y-x) dy dx
                       <=(pi/2)||f||_2||g||_2.                 (9)

All cross integrals below are therefore absolutely convergent. The
bound is uniform in ell; no sharpness claim is made for the damped,
restricted kernel.

### The first form-domain inclusion and the cross identity

Let f in Q_I and g in Q_J. Choose their stipulated smooth-core
approximations f_j,g_j. Their zero-extended sums are in
C_c^infinity(H), including across ell since each approximant
vanishes in a neighborhood of that interface. They converge to
E_I f+E_J g in the whole-line q+L2 norm, by the triangle inequality.
Thus the split domain is contained in Q_+.

For disjoint zero extensions, the only contributions to
q(E_I f,E_J b) come from I times J and J times I. Each contributes
one half of -integral_I integral_J conjugate(f(x))b(y)n(y-x).
Absolute convergence follows from (9). Their sum is -<f,Bb>.
The other cross term is -<g,B*a>. This gives (2) on the split
domain, either directly or by core approximation. Taking equal
arguments gives the difference -2 Re<f,Bg>, of absolute value
at most pi||f||_2||g||_2, and hence (3).

### Restricted tests and the reverse form-domain inclusion

Let phi in C_c^infinity(H), extended smoothly by zero to R.
For any bounded interval K=(a,b), its restriction phi 1_K has
finite energy. In fact its regional energy is at most q(phi,phi),
and its exterior killing term is at most

    ||phi||_infinity^2 integral_K integral_(R\K) n(x-y) dy dx.

Writing d=b-a and using Tonelli, this last double integral is

    2 integral_0^d integral_r^infinity exp(-t)/(2t) dt dr
       =integral_0^infinity min(t,d)exp(-t)/t dt <=1.           (10)

Thus jumps at the interval endpoints cause finite energy. This
calculation uses smoothness only to know the regional energy and
boundedness; it asserts no endpoint value or Sobolev trace theorem.

Apply (7) and Chen–Weth's bounded-interval density first with K=I.
It follows that phi|_I belongs to Q_I. Choose finite R>ell beyond
the support of phi and apply the same argument with K=(ell,R).
The zero extension of phi|_J is precisely phi 1_K. Smooth
approximants in K are also compact smooth tests in J, so phi|_J
belongs to Q_J. Density on an unbounded domain has not been used.

Now let U in Q_+, and choose phi_j in C_c^infinity(H) converging
to U in its form norm. Put f_j=phi_j|_I, g_j=phi_j|_J. Each is
in its part domain by the preceding argument. Applying (3) to
their differences yields

    q_I(f_j-f_k,f_j-f_k)+q_J(g_j-g_k,g_j-g_k)
       <=q_+(phi_j-phi_k,phi_j-phi_k)
                           +(pi/2)||phi_j-phi_k||_2^2.        (11)

Their L2 differences also tend to zero. Completeness of Q_I and
Q_J gives limits in those domains; L2 convergence identifies the
limits with U|_I,U|_J. This proves the reverse inclusion in (1).
Equation (2) now holds throughout Q_+. The comparison (3) in
both directions gives equivalence of the sum and unsplit form
norms with L2 added. No cancellation of infinite energies occurred.

### Representation and the product operator domain

Use Kato, *Perturbation Theory for Linear Operators*, corrected
second edition, reprint of the 1980 edition,
[VI.1.33, pp. 320–321, and VI.2.1, p. 322](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/kato1.pdf).
The former preserves closedness under an L2-bounded symmetric form
perturbation (relative form bound zero); the latter characterizes
the associated operator by its Hilbert-space-valued form functional.
These results apply to densely defined closed nonnegative forms,
or to their lower-bounded perturbations after a scalar shift.

On L2(I) direct-sum L2(J) let q_0=q_I direct-sum q_J, whose
associated operator T_0=G_I direct-sum G_J has the product domain.
Define the bounded self-adjoint operator

    K(f,g)=(-Bg,-B*f),     ||K||<=pi/2.

The norm estimate follows by squaring the two component estimates.
By (1) and (2), q_+=q_0+<K ., .> on their common domain. This
perturbation is closed by the cited theorem (also by (3)). It is
the already nonnegative q_+, not merely a formal block form.

To see the exact operator-domain conclusion in both directions,
if U in Dom(T_0), then for every V in Q_+,
q_+(U,V)=<T_0 U+KU,V>, so representation gives U in Dom(G_+)
and G_+U=T_0 U+KU. Conversely, if U in Dom(G_+), then
q_0(U,V)=<G_+U-KU,V> for every V in the product form domain.
Testing separately in Q_I and Q_J and using representation gives
U in Dom(T_0). This proves (4). It uses the actual bounded L2
operator K, not just a relatively bounded form.

Set g=0 to obtain (5); zero belongs to Dom(G_J). Translation and
reflection preserve the whole-line kernel n(x-y), the L2 norm
and the interval smooth core. Reflection about ell/2 therefore
commutes with the interval form and its operator, by the same
representation characterization. Apply (5) to that reflected u
to obtain the second split premise of L513. No distribution at ell
is omitted: membership and equality have been established against
the complete form domain before any exterior pointwise evaluation.

### Scope of the completed application

The cross bound, both core-closure inclusions and the operator-domain
characterization pass this specialization check for every fixed
ell>0 and arbitrary complex L2 operator-domain data. L513 retains
its original conditional statement as a record; (5) now supplies
its split premise without using that trace theorem in this proof.
The full exterior term is retained. For bounded u and G_I u, its
stronger integrability and the trace formula remain as proved in
L513. The primary theorems are cited imports, not independently
reproved or formally verified manuscripts.

### Separate critical audit, 2026-10-30

The assembly audit passes (1)–(5) with the stated smooth-core
definitions and no additional boundedness assumption. Its decisive
checks are as follows. For a restricted compact test, (10) bounds
the killing energy of both endpoints, while its regional energy is
finite before density is invoked. The comparison (7) therefore puts
the restriction in Chen–Weth's full zero-exterior space on a bounded
interval. Applying that theorem to I and to (ell,R), with R beyond
the test's support, is legitimate; its statement is not extended to
an unbounded domain. The subsequent Cauchy argument (11) is applied
only after both restricted tests are in their part domains. It proves
the reverse inclusion for every element of Q_+, not just for tests.

The reflected Carleman factorization bounds an actual operator B and
the absolute cross integral (9). Thus polarization and passage to
the core limits use finite integrals. The block K is self-adjoint on
the entire L2 direct sum; its norm is at most pi/2, as required.
The two representation arguments test against the full common form
domain established in (1). They prove both operator-domain inclusions,
so (5) cannot be hiding an interface distribution. Finally interval
reflection preserves the core and form, giving the reflected domain
statement without assuming parity of u. These checks require no
change to the proof or to its direct mathematical inputs.

This is an audit of a known-result specialization, not a new split
theorem or an independent audit of the imported source proofs.
The later application to bounded eigenvector data is in L515;
full-Weil realization, collars and near-null flux remain separate.

## Mathlib

Full matching coverage of this zero-extension logarithmic form split
has not been checked. The Carleman, density and representation inputs
are the precise cited standard results above. No absence claim about
Mathlib, and no Lean verification, is made.
