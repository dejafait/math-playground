# L546 — Conditional reflection phase and coefficient separation

## Hypotheses

Work in O=Z[omega], omega=exp(2pi i/3), lambda=1+2omega. Fix the
source datum, S containing the primes over 6, and one nonzero L with
support S and (18)|(L). Put M_ref=lambda^12 L^4. Good primes are
outside S and have their primary generators p=1 modulo 3. For such p,
q_p=N(p), and chi_p is the sixth root of unity reducing to
a^((q_p-1)/6) modulo p on units. Every integer power, including zero
and negative powers, is defined to be zero on nonunits. For squarefree
A use the product over its primes; chi_1 is identically one.

Fix h_0 modulo L, including nonunit classes. Use the canonical cusp
construction of L547 and the finite-field inputs specified below:

1. The active radical r is a product of distinct good primes,
   c=c_F r, and c_F is fixed by h_0 and supported on S (with its
   normalizing unit). The chosen cusp function d, additive character
   vartheta and multiplier kappa_F depend only on h_0 and r modulo
   M_ref^2. L547 supplies the reflection multiplier/additive identities
   and simultaneous absent/inactive-prime conventions from the raw
   cusp expansions, including nonunit h_0. Its finite construction has
   passed independent critical review under the cited raw imports.
2. Use L558 for `eq:reflection-local-fourier` for all six exponents,
   including its zero-frequency values and zero-at-zero principal
   convention. Define tau_(p,m)^+/-=q_p^(-1/2)
   sum_y chi_p(y)^m e(+/-y/p) for nonzero m modulo 6.
   Their unit moduli follow from the Conrad norm/transport argument
   recorded in L557; its mixed-Jacobi product identity is not needed.
   The following one-prime scalar formulas are proved below, rather
   than retained as an additional finite premise:

   \[
   \begin{split}
   \sigma_p&=\lambda^2c/p,&
   \epsilon_p&=-((\lambda^3c/p)\sigma_p)^{-1}\pmod p,\\
   \omega_{p,j}&=
   \begin{cases}
   \tau_{p,j}^-\tau_{p,j+2}^+\chi_p(\epsilon_p)^{-j-2},&j=1,2,3,5,\\
   \tau_{p,4}^-,&j=4,\\
   -\tau_{p,2}^+\chi_p(\epsilon_p)^{-2},&j=0.
   \end{cases}
   \end{split}                                                    \tag{1}
   \]

   The finite part of the branch scalar is the product of
   chi_p(sigma_p)^(-2) omega_(p,j), times the inactive local factors;
   this is also proved below. The global prefactor
   -(i/81) bar(alpha(c))^2 hat(phi)(h_0) bar(kappa_F) belongs to the
   separate Mellin normalization, not to this finite discharge.
   Here alpha(z)=z/|z| and hat(phi) is the
   normalized finite Fourier transform of the fixed source phi,
   with |phi|<=1, hence |hat(phi)|<=1. No value of an
   individual Gauss root is assumed beyond these inputs.
3. Retain the finite marked expansion `cor:marked-reflection`, its
   source support and branch conventions. A mark is on the whole
   primal index n_0 b_0^3; disjoint prime lists have product-form
   coefficients independent of the row and dual index. In a fixed
   branch an inactive mark has coefficient q_p^(-1) and is absent
   from r; an active mark has j=0, scalar -omega_(p,0), and column
   q_p^(-1/2) chi_p(x)^(-2). Inactive marked choices are fixed before
   the remaining inner row/active-slot norm. All nonresidual active
   primes, especially j=4, are frozen there. These assumptions do not
   include either of the two phase identities in the Conclusion.
4. For coefficient separation retain the source coefficient/support
   input: mu=u lambda^h n_0 b_0^3, h>=-4, n_0 squarefree primary and
   b_0 primary, with their full allowed support and all shared primes;
   |d(mu)|<=27*3^(h/6)|b_0|. Fix u,h and a frozen extraction
   n_0=N_F n, b_0=B_F b as in the source's `def:unmarked-reflected-block`.
   Fix one summand of every frozen j=4 Ramanujan factor. Let F_sm
   be the product of its small-summand primes and frozen active j=0
   primes. At each chosen j=4 divisibility term, assign the prime
   either to N_F, or to B_F with p not dividing n_0; these products
   are disjoint. Retain every resulting restriction. R and the
   active-slot product P have independent
   fixed support restrictions apart from their explicit collision
   mask. Common smooth profile separation is retained; no new
   Fourier or norm assertion is a premise or conclusion here.

The two source identities to be checked are not hypotheses. Ordinary
cubic reciprocity on distinct primary primes is an imported standard
theorem, with normalization and precise citation given in the Proof.

## Conclusion

For every active p and j=0,...,5 there is a unit scalar xi_(p,j),
depending only on p,j and the fixed conventions, such that

\[
 \chi_p(\sigma_p)^{-2}\omega_{p,j}
       =\xi_{p,j}\chi_p(c/p)^{2j+2}.                         \tag{2}
\]

For distinct active primary primes p,q,

\[
 \chi_p(q)^{2j_p+2}\chi_q(p)^{2j_q+2}
       =(q/p)_3^{j_p+j_q+2}.                                \tag{3}
\]

Replacing the j=0 factor by an active mark changes xi_(p,0) to its
negative and changes no pair exponent. These identities reproduce
`eq:reflection-cross-prime-phase` and `eq:reflection-pair-phase`.

Let R contain exactly the moving residual j=1 primes and P the moving
active marks, with frozen active product F_act, so r=F_act R P.
In separate fixed classes of R and P modulo the full M_ref^2, the
arithmetic coefficients separate into row-only, tuple-only and
dual-only factors, apart from exactly

\[
 1_{(P,R)=1}\chi_R(nb)^3\chi_P(n)^{-2}1_{(P,b)=1}.            \tag{4}
\]

This includes empty lists, all collision zeros and the retained full
dual support. Bounded coefficient factors can be normalized as in
L541 after extracting its displayed magnitude factors. The result
removes only the retained phase/separation premise there. It proves
no coefficient bound, hybrid norm or Xi sign. The canonical cusp
construction is the external-to-this-proof input supplied by L547.

## Proof

The primary source is OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, 30 September 2026, commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a,
[pinned TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Stable locators are the two phase labels above,
`eq:reflection-local-fourier`, `eq:reflection-row-phase`,
`eq:reflection-multiplier`, `eq:reflection-additive-phase`,
`eq:marked-reflection-phase`, and `eq:unmarked-structural-block`.
Inspected ranges at that commit are 519–588, 1551–1725, 1881–1914,
2047–2138, 2714–2777, 2823–2866 and 6859–7030. The source already
claims the conclusions. Reproduction is needed to discharge a retained
finite implication of L541; importing the whole reflection conclusion
would not check that implication. L547 now supplies the finite canonical
cusp construction. L558 and L557 now discharge the finite Fourier,
Gauss norm and branch-scalar interface below. The marked,
coefficient/support and analytic inputs remain explicit assumptions;
the raw theta imports retain L547's qualifications.

### Independent discharge of the finite branch-scalar premise, 2026-10-31

This checks (1) without assuming (1), the phase conclusion (2), or
the dependent Mellin reflection. Fix an active p, put P=q_p,
H=chi_p and psi(y)=e(y/p), and let x=lambda^4 mu be any integral
dual residue, including zero. L547's reduced numerator satisfies
a=sigma_p h modulo p. Its cusp multiplier is conjugated, as checked
in L547's cusp identification. Thus its p-factor is
H(sigma_p)^(-2) H(h)^(-2), not H(h)^2. L547 (2) supplies
psi(epsilon_p x h^(-1)). After extracting the first constant, the
entire local finite sum is therefore

\[
 T_j(x)=\sum_{h\in k^*}C_{p,j}(h)H(h)^{-2}
                    \psi(\epsilon_p xh^{-1}).                 \tag{7}
\]

The cusp coefficient, fixed additive factor and kappa_F are independent
of these active frequencies by L547, so no frequency-dependent factor
has been omitted from (7). Both sigma_p and epsilon_p are units:
c/p=c_F(r/p) is prime to p. All inverse substitutions below are on k^*.

For j=1,2,3,5, L558 (1) and y=h^(-1) give

\[
 T_j(x)=P^{-1/2}\tau_{p,j}^-
           \sum_{y\in k^*}H(y)^{j+2}\psi(\epsilon_p xy).
\]

Here j+2 modulo six is respectively 3,4,5,1, hence nonprincipal.
If x is nonzero, substitute z=epsilon_p xy in this last sum; it is
sqrt(P) tau_(p,j+2)^+ H(epsilon_p)^(-j-2) H(x)^(-j-2).
If x=0, multiplicative orthogonality makes it zero. The zero extension
of H(x)^(-j-2) makes the same formula valid there. Consequently
T_j(x)=omega_(p,j) H(x)^(-j-2), with exactly the first case of (1).
The factors P^(-1/2) and sqrt(P) cancel. The exponents -j-2 modulo
six are respectively 3,2,1,5, exactly the four columns below.

For j=4, L558 again supplies P^(-1/2) tau_(p,4)^- H(h)^(-4).
The multiplier H(h)^(-2) makes their product principal on k^*.
After the same inverse substitution,

\[
 T_4(x)=P^{-1/2}\tau_{p,4}^-
                \sum_{y\in k^*}\psi(\epsilon_p xy)
       =\tau_{p,4}^-P^{-1/2}(P1_{x=0}-1).                  \tag{8}
\]

Additive orthogonality gives -1 for x nonzero and P-1 for x=0.
No nonprincipal Gauss formula is applied to exponent six.

For active j=0, L558 gives C_(p,0)(h)=-P^(-1). Therefore

\[
 T_0(x)=-P^{-1}\sum_{y\in k^*}H(y)^2\psi(\epsilon_p xy)
 =-\tau_{p,2}^+H(\epsilon_p)^{-2}
                       P^{-1/2}H(x)^{-2}.                \tag{9}
\]

The last equality uses unit scaling for x nonzero and nonprincipal
orthogonality for x=0. Thus its scalar has the minus sign in (1),
and its column retains P^(-1/2). Equations (7)–(9) prove every
active scalar and column, including their values at zero, directly
from L547 and L558.

For inactive frequencies L558 gives zero if j is nonzero and
1-P^(-1) if j=0. L547's simultaneous construction gives the latter
its own conductor omitting p. It is not evaluated using the active
sigma_p, epsilon_p or kernel scale. Products over distinct active
primes factor because these are finite independent frequency sums
and L547 fixes their common cusp data. For an empty active set the
product is one. This proves the finite branch-scalar assertion only;
the global -i/81 factor is outside this calculation.

For completeness the unit-modulus assertion uses Keith Conrad,
*Gauss and Jacobi sums on finite fields and Z/mZ*,
[Theorem 2.2(2), pp. 1–2](https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf),
with precisely L557's additive transport argument. Every Gauss index
used above is in {1,2,3,4,5}, hence its multiplicative character is
nonprincipal by L558. L556's normalization, used through L557/L558,
makes psi nontrivial for P=ell and P=ell^2. Writing psi as the finite
field trace character with nonzero parameter b, the plus and minus
sums acquire respectively H(b)^(-m) and H(-b)^(-m), both of modulus
one. The norm theorem thus gives |tau_(p,m)^+/-|=1. This uses no
individual Gauss phase evaluation or mixed-Jacobi identity, and all
sqrt(P) normalizations remain sqrt(P), equal to ell in residue degree
two. The epsilon and sigma character values also have modulus one.
Hence every omega in (1) is a unit scalar.

This is a reproduction of the primary branch calculation, now checked
against the independent finite-field inputs. It removes the remaining
finite scalar premise under L547's raw cusp imports. It proves no new
theta theorem, global Mellin constant, marked transform, uniform
estimate or signed-Xi identity.

### All six local exponents

Put t=c/p. The radical is squarefree and p is outside the support of
c_F lambda. Thus t, sigma_p and epsilon_p are units modulo p; division
below takes place only on this unit support. Equation (1) gives

\[
 \sigma_p=\lambda^2t,\qquad
 \epsilon_p=a t^{-2},\qquad a=-\lambda^{-5}\pmod p.
\]

Here a denotes the unit residue of this fraction modulo p; its
denominator is invertible. Evaluating chi_p(a) requires no symbol at
a nonunit and no global extension to a denominator divisible by p.

For j=1,2,3,5, multiplicativity gives (2) with

\[
 \xi_{p,j}=\tau_{p,j}^-\tau_{p,j+2}^+
            \chi_p(\lambda)^{-4}\chi_p(a)^{-j-2},
\]

because the t exponent is -2+2(j+2)=2j+2. None of these two Gauss
indices is zero modulo six. For j=0 the same computation gives

\[
 \xi_{p,0}=-\tau_{p,2}^+\chi_p(\lambda)^{-4}\chi_p(a)^{-2}.
\]

For j=4 no epsilon factor occurs, and
xi_(p,4)=tau_(p,4)^- chi_p(lambda)^(-4); its t exponent -2 equals
10 modulo six. Every xi has modulus one and contains no other prime.
For clarity the complete exponent/column check is

| j | t exponent mod 6 | local column B_p(x) |
|---|---|---|
| 0, active | 2 | q_p^(-1/2) chi_p(x)^(-2) |
| 1 | 4 | chi_p(x)^3 |
| 2 | 0 | chi_p(x)^2 |
| 3 | 2 | chi_p(x) |
| 4 | 4 | q_p^(-1/2)(-1+q_p 1_(p divides x)) |
| 5 | 0 | chi_p(x)^5 |

The local columns were derived independently in (7)–(9):
put y=h_p^(-1) in the active local sum. For j=1,2,3,5 it becomes
the exponent-(j+2) Gauss sum with argument epsilon_p x; at p|x its
value is zero by nontrivial character orthogonality. For j=4 it is
the trivial-character sum over nonzero y: -1 on a unit x, q_p-1 on
a nonunit x. For active j=0 the Fourier coefficient is -q_p^(-1),
giving the displayed q_p^(-1/2) column and the minus sign in (1).
The zero-frequency j=0 value is 1-q_p^(-1), with p inactive; for
j nonzero the zero-frequency value is zero. Thus no missing branch
or zero case is filled by a Gauss formula for exponent zero.

For a marked prime, the compatible absent and inactive branches have
the same conductor and canonical data. Their difference is
1-(1-q_p^(-1))=q_p^(-1). The active contribution is subtracted, so
its one-prime scalar is -xi_(p,0). This checks the active sign, not
a new derivation of the full marked transform. Its active conductor
contains p; its inactive conductor omits p. Changing branches changes
c, every relevant t and the kernel scale. The argument is branchwise
and never carries the active conductor into an inactive branch.

### Reciprocity and every pair type

Import Dunn–Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*,
Annals of Mathematics 200 (2024), no. 3, 967–1057,
[arXiv:2109.07463v3, Section 1.2, (1.4)](https://arxiv.org/html/2109.07463v3#S1.SS2).
It states cubic reciprocity for primary inputs a,b=1 modulo 3.
Apply it only to distinct primary p,q, hence coprime. Squaring the
defining sixth-power residue character reduces to the exponent
(q_p-1)/3; injectivity of reduction on the third roots of unity
identifies chi_p(q)^2 with (q/p)_3 in precisely that convention.
No conjugate character is substituted, and no GRH prime asymptotic
from that paper is used. Consequently the left side of (3) is
(q/p)_3^(j_p+1)(p/q)_3^(j_q+1), proving (3).

Here is j_p+j_q+2 modulo 3 for all 36 cases; an entry zero means
one, since both primes are distinct and the cubic symbol is a unit.

| j_p \\ j_q | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | 2 | 0 | 1 | 2 | 0 | 1 |
| 1 | 0 | 1 | 2 | 0 | 1 | 2 |
| 2 | 1 | 2 | 0 | 1 | 2 | 0 |
| 3 | 2 | 0 | 1 | 2 | 0 | 1 |
| 4 | 0 | 1 | 2 | 0 | 1 | 2 |
| 5 | 1 | 2 | 0 | 1 | 2 | 0 |

In particular row/mark has exponent 1+0+2=3. Row/j=4 instead has
exponent 7=1 modulo 3, which need not vanish. Freezing every such
nonresidual prime is essential to the conclusion's scope.

The pair identity is not asserted at p=q. A mark colliding with a
base prime forces that prime to divide the primal whole index, where
the base character power is zero, including exponent zero. The entire
primal summand is therefore zero before reflection. This remains so
if both primal factors share the prime. Distinct disjoint marked
lists give no repeated mark. Thus row/slot collisions are represented
by 1_(P,R)=1, and collisions with a frozen base prime are fixed slot
restrictions. No division by a zero symbol or cancellation at p=q
has occurred.

### Separate sectors and coefficient dependence

Expand chi_p(c/p)^(2j_p+2) into its c_F factor and the factors of the
other active primes. Each c_F interaction is one-prime-only. Group
the others by unordered pairs and use (3). Pairs within R depend
only on R; pairs within the active marked tuple depend only on that
tuple; pairs wholly in F_act are constant. Interactions with F_act
depend only on R or only on the tuple. All R/P pairs equal one.
The active mark's changed sign is also tuple-only. This explicitly
factors the finite moving-prime phase without a norm-invariance
claim about an arbitrary phase.

Fixing R and P separately modulo M_ref^2 fixes F_act R P modulo that
full modulus. Hence the canonical dependence from L547 fixes d,
vartheta and kappa_F, for this h_0. Each class restriction is on one
variable alone; it creates no coupled row/slot constraint. A fixed
product class alone would generally impose such a constraint, and
smaller reciprocity classes do not by themselves fix the cusp data.
Nonunit h_0 causes no change: c_F may differ, but is fixed, supported
on S and prime to every good moving prime. Canonical dependence in
that case is supplied by L547, not inferred from a unit-Fourier theorem.

Finally alpha(c)=alpha(c_F F_act) alpha(R) alpha(P), so its conjugate
square separates. Units and ramified factors of the conductor are
fixed; their interactions with moving primes are one-prime scalars.
Inactive base factors are frozen. An inactive marked choice has
already been fixed before this inner norm, with its own conductor;
its primal exclusions are fixed row/slot restrictions. No sum over
inactive choices or its quantitative cost is proved here.

Set x_F=u lambda^(h+4) N_F B_F^3, which is integral since h>=-4.
For each good moving prime the following equalities include all zeros:

\[
 \begin{split}
 \chi_R(x_Fnb^3)^3
     &=\chi_R(x_F)^3\chi_R(nb)^3,\\
 \chi_P(x_Fnb^3)^{-2}
     &=\chi_P(x_F)^{-2}\chi_P(n)^{-2}1_{(P,b)=1}.
 \end{split}                                                    \tag{5}
\]

To check them, first suppose p divides none of x_F,n,b. Then
3*3=9=3 modulo 6 proves the row identity, and -2*3=-6=0 modulo 6
proves the slot identity. If p divides x_F or n, the corresponding
character factors make both sides zero. If p divides b, the row
right side is zero through chi_p(nb)^3, and the slot right side is
zero through its explicit coprimality mask. These alternatives include
all overlaps and both empty-product cases. A zero exponent on a
nonunit has never been replaced by one. The x_F factors are fixed
row-only and tuple-only contractions.

The restrictions on (n,b) are fixed: n is squarefree and coprime to
N_F so n_0 stays squarefree; a B_F-assigned prime cannot divide n_0;
b has no new coprimality condition with N_F or B_F. In the N_F
assignment no power is extracted from b, including when that prime
divides b. Small Ramanujan summands impose no unit mask at their
prime. Every remaining frozen local factor is a function of this
full dual index alone. Thus allowed S-primes and all shared n/b
primes are retained.

For completeness define delta(n,b)=d(mu) alpha(mu) vartheta(lambda^4 mu)
divided by 27*3^(h/6)|B_F b| on the allowed support. This denominator
is positive, independent of R,P, and the assumed coefficient bound
gives |delta|<=1. Zero source coefficients cause no division problem.
Norm multiplicativity, without any coprimality assumption, gives

\[
 \frac{d(\mu)\alpha(\mu)\vartheta(\lambda^4\mu)}{\sqrt{q_\mu}}
 =27\delta(n,b)q_{\lambda^h}^{-1/3}
            q_{N_Fn}^{-1/2}q_{B_Fb}^{-1}.                     \tag{6}
\]

The powers of q_n,q_b and the kernel belong to the retained common
smooth profile. A frozen small Ramanujan or active zero-mask term
contributes q_p^(-1/2); a frozen divisibility term contributes
q_p^(1/2). The latter cancels the extracted N_F denominator at an
N_F-assigned prime, and leaves q_p^(-1/2) at a B_F-assigned prime.
Thus the remaining frozen magnitudes are
q_(F_sm)^(-1/2) q_(B_F)^(-1/2), in addition to
q_(lambda^h)^(-1/3) q_n^(-1/2) q_b^(-1). This is the normalization
used in L541, not an invocation of that lemma. Active marks retain
q_P^(-1/2). The scalar 27/81 and the frozen inactive factors are
contractions. The remaining bounded arithmetic factors split as
rho(R), a(tuple) and beta(n,b), with beta
independent of R,P and a independent of R,n,b. For disjoint labelled
lists the product determines its tuple. This yields (4) after the
retained smooth separation. Product form is used before frozen-slot
assignment, and general bounded tuple dependence is allowed only
afterwards. No arbitrary coupled mask has been absorbed into beta or a.
When R or P is empty all arguments use the stated empty-product
convention and give the same conclusion.

## Mathlib

A matching formal theorem for this conditional Eisenstein phase and
full-support coefficient separation was not checked. No claim of its
absence is made. Reuse L558's inspected `gaussSum_mulShift_eq`,
`gaussSum_one_left`, `gaussSum_one_right` and `gaussSum_one_one` in
[GaussSum.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/GaussSum.lean),
and L557's recorded `gaussSum_mul_gaussSum_eq_card` norm support.
These support the finite cases, with the nonprincipal and nontrivial
additive hypotheses above; they are not a matching assembly theorem.
No new Mathlib inspection or Lean verification was performed. The
canonical cusp construction, cubic reciprocity and common-profile
theorem have not been checked for formal coverage as a package.
L547 reproduces the finite canonical cusp application; it does not
independently audit the source theta theory.
