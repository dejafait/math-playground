# L515 — Signed-measure eigenfunction smoothing and trace application

## Hypotheses

Fix ell>0 and I=(0,ell). All spaces may be complex. Write E for
zero extension from I to R and R_I for restriction. The Fourier
convention is hat f(xi)=integral_R f(x)exp(-i xi x) dx. Set

    Psi(xi)=(1/2)log(1+xi^2),  n(t)=exp(-|t|)/(2|t|), t!=0.

G_I is the nonnegative self-adjoint part operator of the whole-line
regular symmetric Levy form with multiplier Psi: its form domain is
the closure of C_c^infinity(I) under the norm

    ||f||_2^2+(1/(2pi))integral_R Psi(xi)|hat(Ef)(xi)|^2 dxi.

Thus it is the process killed on exit from I, not subordination of an
already killed Brownian generator. Let c be real, and let mu be a
finite real even signed Borel measure on R. Atoms, including at zero,
are permitted. Put M=||mu||_TV and

    K_mu f=R_I(mu*Ef),  A_I=G_I-cI-K_mu,
    Dom(A_I)=Dom(G_I).

This is the preapproved SPECIALIZE target in
`drafts/literature/2026-10-30-weil-eigenfunction-boundedness-coverage.md`.
The bound is already asserted for the source's signed atomic measure
in bramble_trace, *Boundary traces and support variation for localized
Weil operators*, paper 67 v1, 27 October 2026,
[Section 3.2, (3.7)–(3.8)](https://rstation.ai/problems/riemann_hypothesis/papers/67).
This reproduction spells out the arbitrary finite-measure domination
and convergence topologies needed for that application. No new
smoothing mechanism or independent reproof of the cited semigroup
theorems is claimed.

## Conclusion

A_I is self-adjoint and bounded below by -c-M. Its time-one semigroup
and every eigenvector A_Iu=lambda u satisfy

    ||exp(-A_I)||_(L2(I)->Linfinity(I)) <= exp(c+M)/sqrt(2),       (1)
    ||u||_infinity <= exp(lambda+c+M)||u||_2/sqrt(2),              (2)
    ||G_Iu||_infinity <= (|lambda+c|+M)||u||_infinity.            (3)

These statements include every vector in every eigenspace, with no
positivity, simplicity, or sign restriction on lambda or u. For such
a vector, L514 supplies both interval-to-half-line operator-domain
splits, so the hypotheses of L513 hold with h=G_Iu. Consequently its
continuous representative and both signed, absolutely convergent
renewal trace formulas apply, with the full exterior forcing retained.

This application uses L513 and L514 as stated. The separate critical
assembly audit below checks L514's application and the bounded-data
premises; it does not independently audit the imported source proofs.
Identification of the actual localized Weil realization with A_I is
still an independent input of L512. No collar asymptotics, nonzero
trace, estimate of trace squared by an eigenvalue, or RH positivity
is proved. The constants here depend on the displayed fixed data;
no bound through an unbounded family of measures or supports is asserted.

## Proof

### Finite signed convolution, with atoms

For f in L2(R), translation y->f(.-y) is strongly continuous into L2.
The Bochner integral against the signed finite measure mu defines
mu*f, and Minkowski gives ||mu*f||_2<=M||f||_2. Its representative
satisfies |mu*f|<=|mu|*|f| almost everywhere. One may justify this
by Fubini on bounded x sets, followed by exhaustion, since the L2
bound implies local L1 integrability. For f in L-infinity, use a
bounded measurable representative; the same convolution has bound
M||f||_infinity and agrees with its L2 definition on the intersection.
Changing representatives does not change the convolution almost
everywhere: for a Lebesgue-null set N, Tonelli gives

    integral_R integral_R 1_N(x-y) d|mu|(y) dx=0.

This also handles atomic translations without assigning values on a
null set. Extension and restriction are contractions on both spaces.
For nonnegative F, convolution by nu=|mu| preserves order. Globally,

    |E K_mu f| <= nu*E|f|.                                    (4)

Outside I the left side is zero. Since mu is real and even, changing
variables x->x+y and then y->-y shows convolution is self-adjoint on
L2(R); the pairings are absolutely integrable by
M||f||_2||g||_2. Compression preserves that property. Thus K_mu is
bounded self-adjoint with norm <=M. The bounded self-adjoint
perturbation theorem gives the asserted domain, self-adjointness,
and lower bound, since G_I>=0.

### Whole-line and killed semigroup inputs

Let P_t be the whole-line convolution probability semigroup with
Fourier multiplier exp(-t Psi)=(1+xi^2)^(-t/2), and P_0=I.
Import Grzywny–Ryznar, *Potential theory of one-dimensional geometric
stable processes*, [arXiv:1107.0745v1, Section 2](https://arxiv.org/html/1107.0745v1):
the gamma-subordination density preceding (2.3), the Levy density
(2.4), and the killed transition identity and domination following it.
Their alpha=2 process has exponent log(1+xi^2) and density
exp(-|t|)/|t|, so use their process at half speed. It has exactly
Psi and n above, and its time-t density is their time-t/2 density.
The killed-process representation gives, for T_t=exp(-tG_I),

    |E T_t f| <= P_t E|f|,  t>=0.                             (5)

The part-form/part-process identification is the standard theorem of
Fukushima–Oshima–Takeda, *Dirichlet Forms and Symmetric Markov
Processes*, second revised and extended edition, Section 4.4,
Theorems 4.4.2–4.4.3, pp.173–175. The hypotheses are the regular
symmetric Levy form, Lebesgue reference measure, and open interval;
its smooth-core part realization is precisely the one stipulated here.
This is the same identification used in L513. In particular (5)
does not interchange killing and Brownian subordination. For complex
f, positivity of the killed kernel first gives |T_tf|<=T_t|f|.

Plancherel, with this Fourier normalization, gives at time one

    ||p_1||_2^2=(1/(2pi))integral_R (1+xi^2)^(-1) dxi=1/2.     (6)

The density supplied by subordination agrees with this L2 inverse
transform. No L2 kernel bound at every positive small time is used.

### Dyson domination in L2

Use Engel–Nagel, *One-Parameter Semigroups for Linear Evolution
Equations*, GTM 194, Springer, 2000,
[III.1.3 p.158 and III.1.9–1.10 pp.162–163](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf).
On the Banach space L2(I), -G_I generates the contraction C0-semigroup
T_t, and K_mu is bounded. Therefore exp(t(-G_I+K_mu)) has the series

    S(t)=sum_(j>=0) S_j(t),  S_0(t)=T_t,
    S_(j+1)(t)f=integral_0^t T_(t-s) K_mu S_j(s)f ds.           (7)

These are Bochner integrals for each L2 vector, and the series
converges in L2 operator norm uniformly on compact time intervals.
We import that theorem, rather than assuming convergence into
L-infinity. The scalar shift is exact: exp(-tA_I)=exp(ct)S(t).

For every t>=0, f in L2(I), and j>=0, we claim the L2 lattice inequality

    |E S_j(t)f| <= (t^j/j!) P_t(nu^{*j}*E|f|),                (8)

where nu^{*0} is unit mass at zero and t^0=1. Equation (5) proves
the j=0 case. In (7), (4), (5), and the induction hypothesis give

    |E T_(t-s) K_mu S_j(s)f|
      <= P_(t-s)(nu*E|S_j(s)f|)
      <= (s^j/j!) P_t(nu^{*(j+1)}*E|f|).                     (9)

The last equality uses only whole-line convolutions: P_(t-s)P_s=P_t
and finite-measure convolutions commute with P_s. It does not assert
that the compressed operators commute. All convolutions are bounded
on L2 and positive after domination, so associativity follows from
Tonelli for nonnegative data, and extension to L2.

The modulus inequality for the L2 Bochner integral now integrates
(9), giving (8) with j+1 since integral_0^t s^j/j! ds=t^(j+1)/(j+1)!.
This passage is valid in the Banach lattice L2: the integrands are
strongly measurable, have integrable L2 norms, and the positive cone
is closed. Alternatively pair with nonnegative L2 tests and use
Fubini. It requires no common pointwise exceptional set for uncountably
many times and no L-infinity Bochner integrability at small times.

### Stronger-norm convergence at time one

Let nu^{*j}(R)=M^j, with the j=0 mass interpreted as one even when
M=0. Minkowski and (6) give

    ||p_1*nu^{*j}||_2 <= M^j/sqrt(2).

Cauchy–Schwarz for convolution against E|f|, followed by (8), yields

    ||S_j(1)f||_infinity <= M^j||f||_2/(j! sqrt(2)).           (10)

Thus the series at time one converges in the Banach space of bounded
operators L2(I)->L-infinity(I). More explicitly its remainder after
degree N is bounded by

    (1/sqrt(2)) sum_(j>N) M^j/j!

in that operator norm; it tends to zero. Since ell is finite,
||g||_2<=sqrt(ell)||g||_infinity on I. Hence this stronger-norm sum
also converges in L2 and is the same S(1) as in (7), by uniqueness
of L2 limits. Multiplying by exp(c) and summing (10) proves (1).
This step supplies the missing convergence justification; bare L2
convergence of a bounded-perturbation series would not imply (1).

### Eigen-equation and exact trace application

Self-adjointness makes every eigenvalue lambda real. The spectral
theorem gives exp(-A_I)u=exp(-lambda)u, so (1) gives (2), also for
any vector in a multiple eigenspace. In L2 the eigen-equation reads

    h=G_Iu=(lambda+c)u+K_mu u.                               (11)

The right side is bounded by the L-infinity convolution estimate
already proved. It agrees with h as an L2 function, and proves (3).
This argument obtains boundedness before invoking boundary regularity;
there is no circular use of L513's bounded-data premise.

L514 applies to u in Dom(G_I) and to its reflection, giving the
zero-extended half-line operator-domain splits with interior h and
the exact exterior forcing

    g(y)=-integral_0^ell n(y-z)u(z) dz,  y>ell.

Together with (2)–(3), these are all the additional hypotheses of
L513. Its theorem therefore supplies the continuous representative,
the normalized left and right traces and absolute convergence of
their interior and exterior integrals. The exterior term is not
discarded or presumed bounded on the whole half-line. No parity or
sign assumption is needed for this application. Its imported renewal
and boundary theorems and L514's domain result retain their original
qualifications. L512 still needs its full realization and collar
inputs; neither (1) nor (3) gives a vanishing boundary flux as a full
operator eigenvalue tends to zero.

This completes the application as a known-result reproduction.

### Separate critical assembly audit, 2026-10-30

The independent review passes (1)–(3) and the application to L513 for
every fixed ell>0, real c and finite real even signed Borel mu in the
hypotheses. No extra regularity of mu or positivity of u is needed.
In the first step, the null-set Tonelli argument really concerns the
product of Lebesgue measure and |mu|. Hence atomic translations define
the same L2 and L-infinity equivalence classes; no value at an atom
has been assigned to an ill-defined pointwise representative. Evenness
and reality supply self-adjointness, while only total variation is
used for domination.

The killed-semigroup identification uses the same regular form and
open-part realization checked in L513, with the cited
Fukushima–Oshima–Takeda theorem and GR at half speed. In (9), the
first bound includes zero extension of the compressed convolution;
replacing it by the larger whole-line positive convolution is valid.
Only those whole-line operators are commuted. The integral inequality
is in the L2 lattice: strong measurability and the norm bounds give
Bochner integrability, and closedness of the positive cone allows
integration of the order bound. No uncountable intersection of
pointwise full-measure sets, or small-time L-infinity kernel estimate,
is required.

Equation (6) gives exactly ||p_1||_2=1/sqrt(2). Thus (10) bounds
each linear map S_j(1):L2(I)->L-infinity(I) by M^j/(j!sqrt(2)).
Completeness of that operator space gives a sum and the stated
factorial tail there. The finite-interval embedding into L2, with
norm sqrt(ell), identifies it with the independently imported L2
Dyson sum. This establishes the stronger-norm conclusion rather
than inferring it from L2 convergence. The case M=0 retains the
j=0 unit mass and zero higher terms, so the argument includes it.

Finally a model eigenvector lies in Dom(G_I) by the stipulated
operator domain. The spectral identity gives bounded u; (11) and
the already proved L-infinity convolution bound give bounded h.
L514 supplies the half-line domain identity for u and for its
reflection. Reflection commutes with G_I, so the reflected forcing
is h(ell-·), still bounded. It need not be treated as a positive,
real, simple or parity eigenvector. These are exactly L513's domain
and bounded-data hypotheses, with the same normalization of Psi and n.
Its full exterior forcing, signed integrability and representative
qualifications are retained. No trace theorem is used to obtain the
initial smoothing bound, and no global boundedness of the exterior
forcing is assumed.

No repair of the estimates or dependency graph was required. This
certifies the local specialization and its assembly, not a new result
beyond the inspected sources. The norm bound in (2) has a finite
nonzero limit as lambda tends to zero for fixed c and M; it supplies
no factor vanishing with lambda. Full-Weil identification, collar
control, and an arithmetic bound relating flux to a small eigenvalue
remain unproved here.

## Mathlib

Full matching coverage of signed-measure Dyson smoothing and this
trace application has not been checked. Supporting inputs are the
named Plancherel theorem, Minkowski and Cauchy–Schwarz inequalities,
bounded perturbation and spectral theorems, and the cited killed-process
and renewal results. No specific Mathlib declaration was inspected;
unknown coverage is not evidence of absence. No Lean verification is
claimed.
