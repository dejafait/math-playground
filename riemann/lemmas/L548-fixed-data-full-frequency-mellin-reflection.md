# L548 — Fixed-data full-frequency Mellin reflection

## Hypotheses

Work in O=Z[omega], omega=exp(2pi i/3), lambda=1+2omega=i sqrt(3).
For nonzero z put q_z=|z|^2 and alpha(z)=z/|z|. Use
check-e(z)=exp(2pi i(z+bar z)) and e(z)=check-e(z/lambda).
Fix S containing the primes over 6, an integral modulus E with support
S, and one nonzero L with support S, E|(L) and (18)|(L).
Fix a finite ray character Psi_0, extended by zero away from E-units,
whose conductor divides E. Choose L so that the following function is
periodic modulo L:

\[
 \phi(x)=
 \begin{cases}
 \chi_x(\lambda)^2\Psi_0(x),&x\equiv1\pmod3,\ (x,E)=1,\\
 0,&\text{otherwise}.
 \end{cases}                                                   \tag{1}
\]

The zero branch is evaluated without evaluating a residue symbol.
Fix a finite set P of distinct good primary primes p outside S and
j_p in {0,...,5}. Every integer power of chi_p, including zero and
negative powers, is zero on nonunits. On primary elements let
Psi(x)=Psi_0(x) product_(p in P) chi_p(x)^(j_p).

Retain the coefficient/support and finite Gauss inputs specified below.
Use L547's simultaneous canonical cusp construction for every Fourier
frequency, including nonunit h_0, zero local frequencies and r=1.
Its finite construction has passed independent critical review under
the raw imports. Neither completed
Mellin reflection nor entire continuation of T is a premise.

Import the smooth cubic theta function, its raw automorphy and cusp
expansions from Dunn–Radziwill (DR) at the precise locators in the Proof.
For H chosen by L547 write

\[
 f_H(z,v):=\overline\theta(H(z,v))
   =C_H(v)+\sum_{\mu\ne0}d_H(\mu)vK_{1/3}(4\pi|\mu|v)
                      \check e(\mu z).                         \tag{2}
\]

The support is in lambda^(-4)O, and the conjugate coefficients use
bar(d_j(-mu)). The only possible constant is C_H(v)=(3^(5/2)/2)v^(2/3);
the other two raw cusp functions have zero constant. The raw bound is

\[
 \mu=u\lambda^k n b^3,\quad k\ge-4,\quad n,b\equiv1\pmod3,
 \quad n\text{ squarefree},\qquad
 |d_H(\mu)|\le27\,3^{k/6}|b|.                                \tag{3}
\]

Every supported index admits this representation, with u a unit;
primes may be shared by n,b and no S-mask is applied to the dual side.
Keep the whole source support, even where its coefficients vanish.
The same bound covers the infinity expansion, whose support is in
lambda^(-3)O. The unmasked infinity formula imported from DR is

\[
 d_I(\lambda^{-3}nb^3)=3^{5/2}|b|\widetilde g_3(n),
 \quad
 \widetilde g_3(n)=q_n^{-1/2}\sum_{y\bmod n}(y/n)_3\check e(y/n).
                                                               \tag{4}
\]

On (n,S)=1, use the cubic/sextic conventions checked below:
tilde-g_3(n)=chi_n(lambda)^(-2) gamma_2(n), with
|gamma_2(n)|=1 for squarefree n, including n=1. These two statements
are discharged by the composite application audit below. Bound (3) is
discharged separately by the full raw coefficient specialization below,
using the imported DR formulas and norm theorem. Use the finite Fourier/Gauss
identities and all-six-exponents computation now discharged in L546
from L547, L557 and L558, under their stated raw-import qualifications.
That computation uses only its Hypotheses 1–2, not its marked or
coefficient-separation assumptions. The branch scalar asserted in that
hypothesis is not a premise: its -i/81 normalization is checked here
in (19). Other Gauss inputs and imported source proofs retain
their separate audit status.

All arithmetic data are fixed. Let X>0 and V be C^infinity on
(0,infinity), with every (x d/dx)^j V(x) decaying faster than every
power at both endpoints: O(x^A) at zero and O(x^(-A)) at infinity
for every A>0 and integer j>=0. Set Vhat(t)=integral V(x)x^t dx/x.

## Conclusion

The initially absolutely convergent product

\[
 \begin{split}
 T(s)&=D(s)L_0(s),\\
 D(s)&=\sum_{n\equiv1(3),\ (n,E)=1}^{\rm sf}
       \gamma_2(n)\bar\alpha(n)\Psi(n)q_n^{-s},\\
 L_0(s)&=\sum_{b\equiv1(3),\ (b,E)=1}
       \bar\alpha(b)^3\Psi(b)^3 q_b^{-3s+1/2},\qquad \Re s>1,
 \end{split}                                                   \tag{5}
\]

extends to an entire function with polynomial growth on each fixed
vertical strip. Constants may depend on all the fixed arithmetic data.
Put

\[
 K=(2\pi)^4/27,\quad
 R(t)=\prod_{\pm}\frac{\Gamma(1+t\pm1/6)}{\Gamma(1-t\pm1/6)},
 \quad
 V^\sharp(x)=\frac1{2\pi i}\int_{(\sigma)}
               \widehat V(-t)R(t)(Kx)^{-t}\,dt.                 \tag{6}
\]

For every sigma>=0 the integral is absolutely convergent and gives
the same function. With all canonical branches retained, and a>1,

\[
 \frac1{2\pi i}\int_{(a)}\widehat V(s-1/2)X^{s-1/2}T(s)\,ds
  =\sum_{\rm branches}\zeta
     \sum_{0\ne\mu\in\lambda^{-4}O}
       \frac{d_H(\mu)\alpha(\mu)\vartheta(\lambda^4\mu)}{\sqrt{q_\mu}}
       \prod_{p\mid r}B_p(\lambda^4\mu)
       V^\sharp(q_\mu X/q_c^2).                               \tag{7}
\]

Every dual sum is absolutely convergent. Here r is the active radical,
c=c_F r and H,vartheta,kappa_F are L547's canonical data. The factors are

\[
 \begin{split}
 B_p(x)&=\begin{cases}
 \chi_p(x)^{-j_p-2},&j_p=1,2,3,5,\\
 q_p^{-1/2}(-1+q_p1_{p\mid x}),&j_p=4,\\
 q_p^{-1/2}\chi_p(x)^{-2},&j_p=0\text{ active},
 \end{cases}\\
 \zeta&=-\frac i{81}\bar\alpha(c)^2\widehat\phi(h_0)\bar\kappa_F
       \prod_{p\ {
m inactive}}(1-q_p^{-1})
       \prod_{p\mid r}\chi_p(\sigma_p)^{-2}\omega_{p,j_p},
       \qquad |\zeta|\le1/81.                                \tag{8}
 \end{split}
\]

The finite constants sigma_p,omega_(p,j) have exactly L546's conventions.
No constant-term residue occurs. This verifies the fixed-data analytic
reflection portion of L541 Hypothesis 1 under the retained inputs.
It does not verify L547 independently, reprove theta or Gauss-norm theory,
discharge the other finite Gauss inputs,
prove the marked expansion or uniform kernel seminorm estimates, or
close the global energy argument or actual-Xi positivity gap.
The fixed-data analytic implication has passed the separate critical
review recorded below, using L547's already reviewed finite input.

## Proof

### Sources and scope of this reproduction

DR means Dunn and Radziwill, *Bias in cubic Gauss sums: Patterson's
conjecture*, Annals of Mathematics 200 (2024), no. 3, 967–1057,
[arXiv:2109.07463v3, 14 May 2024](https://arxiv.org/html/2109.07463v3).
Import its unrestricted coordinate action (5.1), theta automorphy
(5.2)–(5.7), and raw cusp expansions (5.9), (5.12)–(5.16), with
Appendix A rows 1,19,10 as identified in L547. Equation (4) is the
fourth case of (5.7) with ramified exponent -3, then conjugation by
(5.16); its hypotheses (5.8) require no coprimality between n and b.
None of these theta inputs uses DR's GRH-conditional prime asymptotics.
DR Lemma 5.2, Corollary 5.1 and their Proposition 5.1 application require
unit Fourier support and are not being applied to the present masks.

The claim audited is OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, 30 September 2026,
[commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`prop:completed-reflection`, `eq:reflection-translated-theta`,
`eq:reflection-direct-mellin`, `eq:reflection-reflected-mellin` and
`eq:reflection`. Relevant inspected lines are 1551–1678, 1782–1934,
2139–2260, with the pointwise Mellin-tail hypothesis at 1078–1091.
This is a reproduction of that claimed application, justified because
the implication was retained as an unchecked local premise. It is not
a new transform and does not reprove theta theory.

Import NIST DLMF [10.43.19](https://dlmf.nist.gov/10.43.E19):
the Mellin integral of K_nu has domain Re(w)>|Re(nu)|. Use nu=1/3
and positive arguments throughout. Endpoint bounds follow from
[10.25.3](https://dlmf.nist.gov/10.25.E3),
[10.30.2](https://dlmf.nist.gov/10.30.E2), and the derivative formula
[10.29.5](https://dlmf.nist.gov/10.29.E5), with the K convention:
K_nu^(m)(y)=(-1/2)^m sum_(j=0)^m binom(m,j)K_(nu-m+2j)(y).
Use also Stirling's modulus formula
[5.11.9](https://dlmf.nist.gov/5.11.E9), uniform for bounded real part.
The ready assessment records the inspected DLMF version as 1.2.8.
Dominated convergence, Mellin inversion, the identity theorem and
the maximum-modulus principle are used with the bounds below.

### Squarefree composite cubic normalization and modulus

This application audit removes only the two finite statements following
(4). Let n be primary, ideal-squarefree and prime to S. For n!=1
write n as the product of the distinct primary generators p of its
prime ideal factors. This is an equality of elements: the product is
primary and the only unit congruent to 1 modulo 3 is 1. Define

\[
 \chi_n(x)=\prod_{p\mid n}\chi_p(x),\qquad
 \rho_n(x)=\prod_{p\mid n}(x/p)_3,\qquad
 \gamma_2(n)=q_n^{-1/2}\sum_{x\bmod n}\chi_n(x)^2e(x/n).
                                                               \tag{A1}
\]

Both characters are zero whenever any p divides x. At n=1 set
chi_1(x)=rho_1(x)=1 for every x and gamma_2(1)=tilde-g_3(1)=1,
as in the pinned source, definitions 582–591 and 1827–1830.
These definitions do not assert a prime-product formula for gamma_2.

Import DR v3, Section 2, (2.1)–(2.2): for primary c its sum
g(c)=sum_(x mod c)(x/c)_3 check-e(x/c) satisfies
g(c)^3=mu(c)c^2 bar(c); its stated consequence is
|g(c)/|c||=mu(c)^2. Here mu is the ideal Moebius function. This is
an unconditional finite identity; DR's GRH-dependent prime averages
are unused. DR cites Hasse (1950), pp. 443–445; that upstream proof
is not independently audited. The imported norm already covers
composite primary c and both residue degrees. No reproof of Gauss
theory or use of a finite-field norm theorem on O/(n) is needed.

For every good p, reduction is injective on the sixth roots of unity,
since the residue characteristic is neither 2 nor 3. The Euler
definition of chi_p therefore gives, on units,

\[
 \chi_p(x)^2\equiv x^{(q_p-1)/3}\pmod p,
 \qquad \chi_p(x)^2=(x/p)_3.                              \tag{A2}
\]

The latter equality uses DR's Euler orientation, not its conjugate.
If the cubic symbol is initially described using primary numerators,
CRT supplies a primary representative of every class modulo p:
impose x'=x modulo p and x'=1 modulo 3. Thus (A2) holds on every
unit class. At the zero class both sides are zero by definition.
Multiplying (A2) over the factors gives rho_n=chi_n^2 on the entire
quotient O/(n), with zeros on every nonunit class, not just at zero.
There is no rational-squarefree restriction: distinct conjugate prime
ideals may both divide n, and inert factors are allowed.

For a+b omega in O one has Tr((a+b omega)/lambda)=b, so e is one
on O. Also check-e is one on O because its trace is integral.
Consequently both e(x/n) and check-e(x/n) are well-defined additive
characters on O/(n). The identity check-e(z)=e(lambda z) is exact.
Since lambda divides only the prime over 3 and n avoids S,
multiplication by lambda is a bijection on O/(n). Moreover,
rho_n(lambda)=chi_n(lambda)^2 is a nonzero cube root of unity.
For y=lambda x in that quotient, multiplicativity gives
rho_n(x)=rho_n(lambda)^(-1)rho_n(y) on units. On nonunits the
same equality holds with both sides zero, since a unit shift
preserves nonunits. Substitution in the full finite sum yields

\[
 \begin{split}
 \widetilde g_3(n)
 &=q_n^{-1/2}\sum_{x\bmod n}\rho_n(x)e(\lambda x/n)\\
 &=\rho_n(\lambda)^{-1}q_n^{-1/2}
                          \sum_{y\bmod n}\rho_n(y)e(y/n)\\
 &=\chi_n(\lambda)^{-2}\gamma_2(n).                       \tag{A3}
 \end{split}
\]

The normalization is q_n^(1/2)=|n|, exactly DR's. Squarefreeness
gives mu(n)^2=1, so its imported norm gives |tilde-g_3(n)|=1.
The factor chi_n(lambda)^(-2) has modulus one; (A3) therefore gives
|gamma_2(n)|=1. For n=1 the quotient has one class, both characters
are identically one under the explicit conventions, q_1=1 and both
additive factors at representative zero are one. Thus (A1) and (A3)
give 1=1 and modulus one without applying any nonprincipal-character
theorem to the zero ring. This covers every allowed n.

The exact phase agrees with the pinned source's
`eq:reflection-cubic-sextic-conversion`, lines 1865–1871.
No CRT factor was dropped: the proof never factors a Gauss sum.
DR (2.3)'s twisted multiplicativity is not required. The short
reindexing verifies the retained local normalization rather than
reproving the known composite norm. It discharges these two finite
premises of the fixed-data reflection. That composite audit alone
leaves the raw formula (4), full raw coefficient bounds, other Gauss inputs, arithmetic
uniformity, global closure and actual-Xi signs separate. In particular
it imposes no S-mask on the raw dual coefficients and makes no sextic
claim at primes in S.

### Full raw three-cusp coefficient specialization, 2026-10-31

This verifies (3) from the imported formulas, rather than importing the
pinned manuscript's final bound. Its purpose is removal of that retained
premise. It reproduces the claim at pinned TeX lines 1806–1854; no
stronger estimate or new theta theorem is claimed. Keep the hypotheses
of (3), with nonzero primary n,b, ideal-squarefree n, no S-mask and no
coprimality condition between n and b. L547 (9) supplies the three
coefficient functions, including their otherwise-zero cases.

Write rho_n(x)=(x/n)_3 for the ordinary cubic symbol, zero on every
nonunit class when n!=1. Unlike the sextic symbol used in (A1), this
symbol is available at every prime other than lambda, including primes
above 2. For n=1 use the empty-product character identically one and
g(t,1)=1. For n!=1 define the source Gauss sum

\[
 g(t,n)=\sum_{x\bmod n}\rho_n(x)\check e(tx/n).
                                                               \tag{B1}
\]

This is DR's normalization in Section 1.3, consistent with (2.1).
The additive factor is well-defined: replacing x by x+ny multiplies
it by check-e(ty)=1 for integral t,y. Import DR (2.1)–(2.2), already
stated above, on its entire primary domain, not just the good-prime
subdomain used for (A2). Taking absolute values of its cubic identity
gives |g(1,n)|^3=|n|^3 for squarefree n, hence |g(1,n)|=|n|.
DR Section 2 includes split and inert primes; no prime exclusion
other than lambda enters this import. The upstream Hasse proof remains
unaudited. In particular this does not apply a finite-field norm theorem
directly to a composite quotient.

For t in {1,lambda^2,omega lambda^2,omega^2 lambda^2}, primary n
is coprime to t: n is coprime to lambda and omega is a unit. Thus
multiplication by t permutes O/(n). If y=tx, multiplicativity gives
rho_n(x)=rho_n(t)^(-1)rho_n(y), including all nonunits, since a unit
shift preserves them. The factor rho_n(t) is a cube root of unity.
Reindexing the whole sum, without factoring it, yields

\[
 g(t,n)=\rho_n(t)^{-1}g(1,n),\qquad |g(t,n)|=|n|.          \tag{B2}
\]

For n=1 the sole representative zero contributes one under the stated
conventions, so (B2) also holds with every factor equal to one. This
avoids a nonprincipal-character assertion for the zero ring. The same
argument applies when -2 divides n: only the ordinary cubic symbol is
used. Other primes in S are equally allowed. No condition involving b
has occurred. This short specialization verifies the relevant unit
shift; the composite norm itself is imported, not reproved.

In DR (5.7), rename its integer ramified parameter h, and take its
primary parameters c=n and d=b. Every displayed factor outside its
Gauss sum and positive power of 3 has modulus |b/n| or one. Applying
(B2) gives the following exhaustive nonzero cases. The ratio column
compares the achieved magnitude with the required 27*3^(k/6)|b|.

| Source family | Index in its own argument | Magnitude | Ratio |
| --- | --- | --- | --- |
| DR (5.7), first three cases, h>=1 | ±omega^j lambda^(3h-4) n b^3, j=0,1,2 | 3^(h/2+2)abs(b)=3^(k/6+8/3)abs(b), k=3h-4 | 3^(-1/3)<1 |
| DR (5.7), fourth case, h>=0 | ±lambda^(3h-3) n b^3 | 3^(h/2+5/2)abs(b)=3^(k/6+3)abs(b), k=3h-3 | 1 |
| DR (5.13), its three cases | omega^j lambda^(-4) n b^3, j=0,1,2 | 9abs(b), k=-4 | 3^(-1/3)<1 |
| DR (5.14), its three cases | -omega^j lambda^(-4) n b^3, j=0,1,2 | 9abs(b), k=-4 | 3^(-1/3)<1 |

The first equality uses h=(k+4)/3; the second uses h=(k+3)/3.
For the last two rows the required size at k=-4 is 3^(7/3)|b|,
and 9/3^(7/3)=3^(-1/3). These comparisons are exact for every
allowed h, not numerical sampling. All displayed ninth-root and omega
phases have modulus one. All remaining source cases have coefficient
zero, and therefore satisfy the bound whenever parametrized as in (3).

For completeness track the actual conjugate cusp arguments. By L547
(9), d^(0)(mu) uses tau(-mu); d^(1)(mu) uses tau_1(-omega^2 mu);
d^(2)(mu) uses tau_2(-omega mu). Multiplication by these units changes
only the unit u in (3), preserving k,n,b and their sizes. Conjugation
preserves modulus. The additional omega and check-e(-mu) factors
also have modulus one, the latter because mu+bar(mu) is real. At
k=-4, tau_1's support translates exactly to u in {-1,-omega,-omega^2}
for d^(1); tau_2's support translates to u in {1,omega,omega^2} for
d^(2). Both are zero at every other k. For d^(0), the first row
covers k=-1,2,5,... and all six units; the second covers k=-3,0,3,...
and units ±1. Every other k/unit case is zero, including k=-4 and
k=1 mod 3. This includes the infinity expansion d_I=d^(0).

The source hypotheses are exactly primary n,b and squarefree n;
DR (5.8) imposes no (n,b)=1 condition. Shared factors cause no
change to (B2), whose shift depends only on n. All source indices
lie in the parametrized set in (3), and multiplication by units in
the cusp formulas preserves this set. Nonzero lattice indices outside
that set have zero coefficients and are retained as zero terms.
No claim that every point of lambda^(-4)O has such a representation
is required. The constant term mu=0 is outside (3).

Thus (3) passes the full raw application check, under the precise DR
theta and norm imports. The sharp ratio among the listed cases is one;
no larger constant or extra mask is necessary. This removes the size
premise from the conditional reflection/tail uses of (3), while leaving
the imported source proofs, other finite inputs, arithmetic-uniform
closure and actual-Xi positivity unresolved. No downstream theorem
depending on these independent assumptions is thereby unconditional.

### Independent critical review of the full raw bound, 2026-10-31

The specialization (B1)–(B2) and its complete case table pass this
separate review under the stated DR imports. The review rechecked DR
v3 Section 1.3, (2.1)–(2.2), every branch of (5.7)–(5.8) and
(5.13)–(5.16), and Appendix A rows 1,19,10, against the canonical
proof above. Pinned TeX 1806–1854 identifies the reproduced claim;
its final envelope is not used as a premise for this verification.

In particular (B1) uses the source's trace character, not the e
character without its lambda rescaling. For n!=1, every permitted t
is a unit modulo n, since primary n is prime to lambda. If x is a
nonunit, tx is a nonunit too, so the character relation used in (B2)
has both sides zero. On units it follows by multiplicativity and
rho_n(t)!=0. Thus the substitution is valid on the entire finite
quotient, including composite n, and requires neither (n,b)=1 nor a
finite-field theorem on that quotient. The absolute value of the
imported identity (2.2) is |g(1,n)|^3=|n|^3, because ideal-squarefree
n has |mu(n)|=1. This applies also at the prime -2 of norm 4 and at
other S-primes; no sextic symbol is introduced there. At n=1 the
explicit empty-character convention makes the one-term sum one, so
no assertion about a nonprincipal character on the zero ring is used.

The four table rows include all nonzero source cases: h>=1 and
k=3h-4 for all six units in the first three branches of (5.7);
h>=0 and k=3h-3 for units +/-1 in its fourth branch; and k=-4 for
the three positive or the three negative unit classes in (5.13) or
(5.14), respectively. Their exponents relative to 3^(3+k/6)|b|
are, in order, -1/3, 0, -1/3 and -1/3. At the endpoint h=0 of
the fourth branch, n=b=1 gives mu=lambda^(-3) and magnitude
3^(5/2)=27*3^(-3/6). Hence the largest ratio is actually attained;
the threshold is 27, not a strictly smaller uniform constant in this
normalization. This is an exact source-case check, not a numerical
certificate or a claim about the constant term.

For the actual cusps, -mu leaves the first family's six-unit set
and its +/-1 set invariant. The condition -omega^2 u in {1,omega,
omega^2} gives u in {-1,-omega,-omega^2} for d^(1); the condition
-omega u in {-1,-omega,-omega^2} gives u in {1,omega,omega^2}
for d^(2). Unit multiplication leaves k,n,b unchanged. All factors
outside tau, tau_1 or tau_2 in L547 (9), including check-e(-mu),
have modulus one, and complex conjugation preserves modulus.
The otherwise-zero source cases therefore remain zero after the
exact cusp changes, including k=-4 for d^(0) and every k!=-4
for d^(1),d^(2). No raw lattice term is removed by an S-mask.

Thus there is no missed unit/ramified case, invalid character shift
or enlarged constant in (3). This verdict validates the already
written specialization, not the upstream Patterson/Hasse proofs or
any further finite, uniformity, global-closure or actual-Xi assertion.
Its only notebook input for the cusp identification is L547 (9);
the other direct inputs of L548's full reflection theorem are
unchanged. No downstream coefficient estimate is used circularly.

### Convergence available before the Mellin operations

For each beta>1, (3) implies

\[
 \sum_{\mu\ne0}|d_H(\mu)|q_\mu^{-\beta}
 \le C\left(\sum_{k\ge-4}3^{k(1/6-\beta)}\right)
       \left(\sum_n^{\rm sf}q_n^{-\beta}\right)
       \left(\sum_b q_b^{1/2-3\beta}\right)<\infty.              \tag{9}
\]

The sums over n,b are primary. A rank-two lattice has O(Y) elements
of norm <=Y: place disjoint disks of radius smaller than half its
shortest spacing at those elements and compare their area with a disk
of radius sqrt(Y) plus that fixed radius. Dyadic summation therefore
gives convergence of sum q^(-z) for z>1. Apply this with z=beta
and z=3beta-1/2; the k sum is geometric. Including all representations
in the upper bound is harmless; their prime valuations in fact fix n,b
and k and a choice among six units. Shared primes require no deletion.

The lattice lambda^(-4)O has |mu|>=1/9 for mu!=0. Also (3) gives
|d_H(mu)|<=C q_mu^(1/6): use |b|=q_b^(1/2) and q_n>=1.
Thus every finite z,v derivative of the Bessel series converges
absolutely and locally uniformly for v>0. Indeed derivatives add only
fixed powers of |mu|, v and v^(-1); for v in a compact subinterval of
(0,infinity), the large-argument Bessel bounds dominate the resulting
polynomial lattice sum exponentially. Finitely many small arguments
do not affect this assertion. Differentiation and the chain rule on
these expansions are consequently legitimate.

### All frequencies, the cusp derivative, and the zero term

Finite Fourier inversion gives

\[
 C(h)=\widehat\phi(h_0)\prod_p C_{p,j_p}(h_p),\qquad
 z_h=\lambda^2(h_0/L+\sum_p h_p/p),\qquad
 \mathcal F(z,v)=\sum_h C(h)\bar\theta(z+z_h,v).                 \tag{10}
\]

The sums include all h_0 modulo L and all h_p modulo p. Its infinity
coefficient multiplier is phi(lambda^3 mu) product chi_p(lambda^3 mu)^j_p,
because check-e(mu z_h)=e(lambda^3 mu(h_0/L+sum h_p/p)). Terms with
zero finite coefficient may be omitted; this does not impose a unit
condition on h_0. L547 gives each remaining z_h=a/c, with gcd(a,c)=1,
c!=0, g=[[a,b],[c,delta]]=GH and G in Gamma_1(3).

Write Q=q_c. Substitute g^(-1)=[[delta,-b],[-c,a]] and z+a/c
into DR (5.1), using a delta-bc=1. The coordinates simplify to

\[
 z'=-\delta/c-\frac{\bar z}{c^2(v^2+|z|^2)},\qquad
 v'=\frac{v}{Q(v^2+|z|^2)}.                                 \tag{11}
\]

For example the horizontal numerator is
-delta bar(c)(|z|^2+v^2)-(bar(c)/c)bar(z), over denominator
Q(|z|^2+v^2), which verifies the complex conjugates in (11).
At z=0, the Wirtinger derivatives with respect to bar(z) are

\[
 \partial_{\bar z}z'=-1/(c^2v^2),\quad
 \partial_{\bar z}\bar z'=0,\quad
 \partial_{\bar z}v'=0.                                    \tag{12}
\]

Automorphy and (12), with u=1/(Qv), therefore give the exact identity

\[
 A_h(v):=\left.\partial_{\bar z}\bar\theta(z+a/c,v)\right|_{z=0}
 =-\frac{\bar\kappa(G)}{c^2v^2}
      (\partial_z f_H)(-\delta/c,u).                         \tag{13}
\]

In particular C_H(v') contributes C_H'(v')partial_bar(z)v'=0.
It is not enough merely to say that C_H has no horizontal variable
before composing coordinates; (12) supplies the necessary extra fact.
Only nonzero modes remain in (13). This argument also covers a=0,
c a unit, empty r and either of the cusps with no original constant.
There is no inverse of h_0 or of a dual frequency.

### Endpoint estimates and the two Mellin identities

For each j>=0, the direct expansion and its derivatives imply, at v>=1,
|(v d/dv)^j A_h(v)|<=C_j v^(m_j) exp(-b v), for suitable m_j and b>0.
To see an exponential bound after summing, split exp(-4pi|mu|v)
into two factors, use |mu|>=1/9 in one, and sum the polynomially
weighted other factor at v>=1. The same reasoning applies to every
logarithmic u derivative of partial_z f_H at the fixed real-plane
point -delta/c. Apply (13) and v d/dv=-u d/du to obtain, for small v,

\[
 |(v\partial_v)^j A_h(v)|\le C_{h,j}v^{-m'_{h,j}}e^{-b_h/v},
 \qquad b_h>0.                                             \tag{14}
\]

The constants are allowed to depend on c and all the fixed data.
The finite sum A(v)=sum_h C(h)A_h(v) has the same endpoint property.
Consequently J(s)=integral_0^infinity A(v)v^(2s) dv/v is entire,
by domination uniform on compact sets of s. With v=e^y, it is the
Fourier transform in y of A(e^y)e^(2 Re(s)y). All y derivatives
are integrable with bounds uniform on a fixed real strip by (14).
Integration by parts gives J(s)=O_(I,N)((1+|Im(s)|)^(-N)) for every
N and compact real interval I, with all boundary terms zero.

For Re(s)>1, (9) and the positive-real Bessel Mellin integral justify
Fubini for the differentiated infinity expansion: the sum of absolute
integrals is a constant depending on Re(s) times sum |d_I(mu)|q_mu^(-Re(s)).
The multiplier is bounded, so it does not change convergence. Since
partial_bar(z) check-e(mu z)=2pi i bar(mu)check-e(mu z), the result is

\[
 J(s)=\frac i4(2\pi)^{-2s}\Gamma(s+1/3)\Gamma(s+2/3)
  \sum_{\mu\ne0}d_I(\mu)\phi(\lambda^3\mu)
        \prod_p\chi_p(\lambda^3\mu)^{j_p}
        \bar\alpha(\mu)q_\mu^{-s}.                          \tag{15}
\]

Here the Bessel exponent is w=2s+1, so Re(w)>1/3 as required.
The numerical factor follows directly from
2pi i times 2^(2s-1)(4pi)^(-2s-1)=i(2pi)^(-2s)/4.

By DR (5.7), the mask lambda^3 mu=1 modulo 3 isolates exactly
mu=lambda^(-3)nb^3 in (4). Its other ramified powers make lambda^3 mu
divisible by lambda; the opposite sign in the remaining pair is -1
modulo 3. The whole-index E mask first restricts to (nb,E)=1.
On that domain chi_(nb^3)(lambda)^2=chi_n(lambda)^2 since
chi_b(lambda)^6=1, and finite characters, with their zero values,
give Psi(nb^3)=Psi(n)Psi(b)^3. This remains true at a shared moving
prime, including j_p=0. On discarded indices nothing is evaluated.
Insert (4) and its cubic/sextic conversion into (15), using
q_(lambda^(-3))=1/27 and bar(alpha(lambda^(-3)))=-i. This proves

\[
 J(s)=\frac{3^{5/2}}4\left(\frac{27}{(2\pi)^2}\right)^s
              \Gamma(s+1/3)\Gamma(s+2/3)T(s).                \tag{16}
\]

For Re(s)<0, apply (13) and substitute u=1/(Qv) into the integral
for a single A_h. Before evaluating the Bessel integral this is

\[
 -2\pi i\,c^{-2}Q^{2-2s}\bar\kappa(G)
  \sum_{\mu\ne0}d_H(\mu)\mu\check e(-\delta\mu/c)
       \int_0^\infty u^{2-2s}K_{1/3}(4\pi|\mu|u)\,du.
                                                               \tag{17}
\]

The sum of absolute integrals is finite by (9) with beta=1-Re(s)>1.
The Bessel exponent is now w=3-2s, still strictly in its valid domain.
Using c^(-2)=bar(alpha(c))^2/Q gives

\[
 \begin{split}
 J_h(s)={}&-\frac i4(2\pi)^{2s-2}\bar\alpha(c)^2Q^{1-2s}
       \bar\kappa(G)\Gamma(4/3-s)\Gamma(5/3-s)\\
 &\hspace{8mm}\times\sum_{\mu\ne0}d_H(\mu)\alpha(\mu)
                   \check e(-\delta\mu/c)q_\mu^{s-1},
 \qquad J(s)=\sum_h C(h)J_h(s).                             \tag{18}
 \end{split}
\]

The endpoint estimates preceded both representations. No equality of
two disjoint Dirichlet-series half-planes is assumed by formal algebra.

### Entire continuation and polynomial strip growth

Define T on the plane by (16) solved for T, using the entire reciprocal
gamma functions. This gives an entire function agreeing with (5) on
Re(s)>1, hence its unique analytic continuation. Zeros of the reciprocal
gamma factors cause no poles. Formula (18) remains a representation
of this same J on Re(s)<0.

Fix a_0<0 and b_0>1. On Re(s)=b_0, absolute convergence bounds T
uniformly in Im(s). On Re(s)=a_0, use (18), its absolutely convergent
series and Stirling. The numerator gamma pair has size
O(|t|^(2-2a_0)e^(-pi|t|)); the denominator pair has size comparable
to |t|^(2a_0)e^(-pi|t|), for large |t|. Thus
T(a_0+it)=O((1+|t|)^(2-4a_0)). Any bounded portion of the line is
covered by continuity of the already entire T, even if a reciprocal
gamma factor vanishes there. In the whole strip, the rapid bound for
J and reciprocal Stirling initially imply
|T(s)|<=C(1+|Im(s)|)^C exp(pi|Im(s)|).

Choose a positive B with B+a_0>1 and an integer m>=2-4a_0.
Then F(s)=T(s)/(B+s)^m is analytic on the closed strip and bounded
by one constant C_0 on its two vertical boundary lines. For epsilon>0,
apply maximum modulus on a height-H rectangle to F(s)exp(epsilon s^2).
The horizontal sides tend uniformly to zero as H tends to infinity,
because exp(-epsilon H^2+pi H) dominates their polynomial factor.
The vertical sides are bounded by C_0 exp(epsilon M^2), where
M=max(|a_0|,|b_0|). Taking H to infinity first yields, at each fixed s,

\[
 |F(s)|\le C_0\exp\{\epsilon(M^2-\Re(s^2))\}.
\]

Let epsilon decrease to zero; C_0 is independent of epsilon. Hence
|F|<=C_0 throughout and T has a polynomial strip bound. Every fixed
vertical strip is contained in one of this form. This argument does
not infer polynomial growth merely from rapid decay of J.

### Contour shift, scalar, and absolutely convergent dual sum

The assumptions on V imply that for each compact real interval I,
each integer N and every j, the weighted integrals
integral x^eta |(x partial_x)^j V(x)| dx/x are bounded uniformly for
eta in I, and all logarithmic integration-by-parts boundary terms
vanish. The pointwise bound
|Vhat(eta+it)|<=C_(I,N)(1+|t|)^(-N) follows by setting x=e^y
and integrating by parts. This also shows Vhat entire. Its pointwise
decay and the polynomial strip bound for T make the horizontal joins
vanish when shifting the left integral of (7) from a>1 to
s_0=1/2-sigma<0, sigma>1/2. No poles are crossed.

Insert (18)/(16) on that line and put t=1/2-s. The reversed
orientation cancels ds=-dt. The gamma ratio is exactly R(t), and
the scalar and scale follow from

\[
 \begin{split}
 &(2\pi)^{4s-2}27^{-s}3^{-5/2}=81^{-1}K^{-t},\\
 &Q^{1-2s}q_\mu^{s-1}X^{s-1/2}
       =q_\mu^{-1/2}(q_\mu X/Q^2)^{-t}.                    \tag{19}
 \end{split}
\]

This yields -i/81, with bar(alpha(c))^2, C(h), bar(kappa(G)) and
the additive phase retained. Stirling gives |R(sigma+iu)| bounded
by a constant times (1+|u|)^(4sigma) on the fixed line; the exponential
factors cancel. The sum of absolute values after integrating is
bounded by a constant times

\[
 \left(\sum_{\mu\ne0}|d_H(\mu)|q_\mu^{-1/2-\sigma}\right)
 \int_{\mathbb R}|\widehat V(-\sigma-iu)|(1+|u|)^{4\sigma}\,du,
                                                               \tag{20}
\]

which is finite by sigma>1/2 and (9). This proves the sum/integral
exchange on this line. The finite Fourier sums now use L547's
multiplier and additive-phase identities, and the all-six-exponents
local calculation discharged in L546 under the cited finite-field inputs.
They give exactly (8): inactive j=0 gives 1-q_p^(-1); active j=4
keeps its Ramanujan divisibility term; the remaining active cases
retain their zero extensions. This proves (7) at sigma>1/2, with
all frequencies and the unmasked dual support.

For completeness, definition (6) also makes sense on the zero line.
The numerator gamma poles of R have negative real part, the closest
at -5/6; its reciprocal denominator factors are entire. On each
closed strip 0<=Re(t)<=A it is therefore holomorphic, and Stirling
gives |R(t)|<=C_A(1+|Im(t)|)^(4A), including bounded imaginary parts
by continuity. Rapid pointwise decay of Vhat makes (6) absolutely
convergent and permits shifting it between any two nonnegative lines.
Representing each individual kernel on a line A>1/2 gives
|Vsharp(x)|<=C_(A,V)x^(-A). Since q_mu>=1/81, this estimate and (9)
make the dual series in (7) absolutely convergent at fixed X,c.
The finite local columns in (8) are bounded for the fixed primes.
Thus the same series has the same value when each kernel is represented
at sigma=0. We never exchange a dual Dirichlet series with its integral
on the zero line; (20) would not justify that exchange there.

Finally |phihat(h_0)|<=1 since |phi|<=1, all remaining phase and Gauss
scalars in (8) have modulus one, and 0<1-q_p^(-1)<1. Hence
|zeta|<=1/81. This uses the retained finite bounds, not a new arithmetic
estimate. There was no surviving zero mode in (13), so no extra residue
or correction term is omitted. All six analytic obligations pass at
fixed arithmetic data; neither arithmetic-uniform constants nor the
independent hypotheses listed after the Conclusion have been obtained.

### Independent critical review, 2026-10-31

The implication (1)–(8) passes an independent analytic review under
the stated raw-theta, coefficient and finite Gauss inputs. This review
uses neither the completed-reflection proposition as a premise nor
L541's downstream conclusion. It reproduces a source-claimed result;
it does not strengthen that result or independently prove theta theory.
The following checks address the possible failures of the application.

**Cusp chain rule and endpoints.** Put D=v^2+z bar(z). Direct
differentiation of (11), before setting z=0, gives

\[
 \partial_{\bar z}z'=-\frac{v^2}{c^2D^2},\qquad
 \partial_{\bar z}\bar z'=\frac{z^2}{\bar c^2D^2},\qquad
 \partial_{\bar z}v'=-\frac{vz}{QD^2}.
\]

Thus only the first term of the real-smooth Wirtinger chain rule
survives at z=0. In particular the composed constant C_H(v') has
zero derivative; it cannot supply a residual Mellin pole. No step
requires a!=0, r!=1, or a unit Fourier or dual index. The constant
in the F_1 case and its absence in F_19,F_10 exhaust the raw cusp
cases. Formula (9), the lattice lower bound, and exponential Bessel
decay justify the differentiated expansions locally before this rule
is applied. Repeated logarithmic differentiation of (13) is a finite
linear combination of v^(-2)(u partial_u)^k partial_z f_H at
u=1/(Qv). Each term is a power times exp(-b/(Qv)) near zero for
some b>0. This proves (14) for every needed order without claiming
uniformity in Q. At infinity the direct nonconstant expansion gives
the corresponding bound. The integrations by parts for J therefore
have integrable derivatives and vanishing boundary terms, uniformly
over every compact interval of Re(s).

**Absolute half-planes, masks and normalizations.** With nu=1/3,
the Bessel integral (DLMF 10.43.19) is evaluated at w=2s+1 and
w=3-2s respectively. Both satisfy Re(w)>1/3 on their asserted
half-planes. Including the horizontal derivative, the sums of absolute
integrals are multiples of sum |d_I(mu)|q_mu^(-Re(s)) and
sum |d_H(mu)|q_mu^(-(1-Re(s))). Their exponents exceed one,
so (9) justifies Fubini; endpoint decay alone is not used to justify
these termwise operations. DR (5.7)–(5.8) leave exactly the plus
branch mu=lambda^(-3)nb^3 after the lambda^3 mu=1 modulo 3 mask.
Every other ramified case is divisible by lambda after multiplication
by lambda^3, and the negative member is -1 modulo 3. The E-mask
then gives (nb,E)=1 before the cubic/sextic conversion is evaluated.
The multiplicative identity at a moving prime remains zero on both
sides if that prime divides n or b, including j_p=0. Shared n,b
primes have not been silently removed.

The direct scalar is i(2pi)^(-2s)/4 before inserting (4);
bar(alpha(lambda^(-3)))=-i converts it to the positive scalar in
(16). The reflected substitution contributes
-2pi i c^(-2)Q^(2-2s) before its Bessel integral. Dividing the two
identities and setting s=1/2-t gives

\[
 3^{-5/2}27^{-1/2+t}(2\pi)^{-4t}
       =3^{-4}\bigl((2\pi)^4/27\bigr)^{-t},
\]

with the remaining phase -i, and gives exactly the scale in (19).
For the finite active sums, changing h to h^(-1) makes the local
character exponent j+2. The four nontrivial cases vanish when p|x;
j=4 instead gives q_p 1_(p|x)-1, and j=0 has Fourier coefficient
-q_p^(-1). These are precisely L546's three local cases in (8).
Only inactive j=0 contributes 1-q_p^(-1). No unit-frequency theorem
or Gauss formula for a nontrivial character at exponent zero was used.

**Continuation and both contour operations.** Reciprocal gamma
functions make the definition from (16) entire, including their zeros.
On the left boundary a_0<0, Stirling gives polynomial powers
2-2a_0 and 2a_0 for the numerator and denominator pairs respectively,
with the same exp(-pi|Im(s)|) factor. Their quotient therefore has
power 2-4a_0, as used above. The preliminary interior exponential
bound suffices for the maximum-modulus argument: fix epsilon>0,
send rectangle height to infinity, then send epsilon to zero at the
fixed interior point. The vertical boundary constant C_0 is
independent of epsilon. No boundedness of the reciprocal gamma
functions on an entire strip is assumed.

The stated two-ended bounds on every logarithmic derivative of V
make Vhat entire and rapidly decreasing uniformly in each closed
vertical strip. Consequently the horizontal joins in the s-contour
shift vanish against the proved polynomial bound for T. On the
t-line sigma>1/2, the dual interchange is justified by (20), with
Dirichlet exponent 1/2+sigma>1 and at most polynomial gamma-ratio
growth. For moving an individual kernel to sigma=0, the nearest
numerator pole is -5/6 and denominator poles become zeros. Thus no
residue is crossed. Absolute summability of the resulting kernels
is proved on any line A>1/2, then their pointwise contour independence
identifies the same series at sigma=0. The review does not license a
dual-series/integral interchange on that zero line.

These checks validate fixed-data reflection, zero-term removal and
entire/polynomial-strip continuation only. The full three cusp cases,
all original Fourier frequencies and every nonzero raw dual index
remain present. The raw source proofs, other finite Gauss estimates,
conductor-uniform kernel seminorms, marked expansion, global energy
closure and actual-Xi signs retain their separate status. The later
composite audit above discharges the good squarefree conversion and
unit modulus. The later full raw coefficient specialization also
discharges (3), under the DR imports; it does not discharge the other
source premises listed here.

## Mathlib

Full matching coverage has not been checked. The precise imported
theta/cusp and special-function results are the DR and DLMF references
above; the rest is the displayed conditional application. No claim
that Mathlib contains or lacks this full theorem is made.
For the composite finite specialization, the inspected supporting
theorem is `gaussSum_mulShift_eq` in official
[GaussSum.lean, lines 54–76](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/GaussSum.lean#L54),
read 2026-10-31. It applies to a finite commutative source ring and a
unit shift, as in (A3). Its finite-field norm theorem is not a norm
theorem for a composite quotient. A full matching Eisenstein cubic
normalization theorem was not identified in that file; global
coverage is not checked. DR supplies the precise norm import.
For (B2), the same finite-ring unit-shift theorem supports reindexing
on O/(n); its hypotheses are checked explicitly above, with n=1
handled by its stated convention. The full matching three-cusp
coefficient envelope has not been checked in Mathlib. The imported
theta formulas and all-primary norm, rather than supporting formal
algebra alone, supply its substantive mathematical inputs.
