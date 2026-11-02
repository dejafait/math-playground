# Lemma 582: unit Hermite closure preserves the paired moment tolerances

## Hypotheses

Let H be real and sufficiently large, ell=log H held fixed, L=H ell,
and P=L+1. Use the actual real Hardy function Z, L473's coordinate
order I={(r,j): r=0,1; j=0,1,2}, reference integrals S_ab(H), F_m(H)
from its (1), and precisely the tolerances in its (2). In particular
the four tight odd second requirements are absolute bounds, not
approximation errors of size O(1). Import L473 (6),(9)--(10), including
its arithmetic-source qualifications: the proof of Bui--Hall
Proposition 3 remains imported and unaudited here.

Also import, for each fixed k=0,1,2, the pointwise estimate

    |Z^(k)(t)| <= C_k T^(1/6), t of order T,

from H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function
Z(t)*, Bull. Lond. Math. Soc. 55 (2023), 2304--2323,
[DOI 10.1112/blms.12859](https://doi.org/10.1112/blms.12859),
[arXiv:2304.05178v1](https://arxiv.org/html/2304.05178v1), Introduction,
printed p.1 immediately before (1). Only these three fixed orders on
heights in [H,3H] are used; no uniform-in-order bound is asserted.
Its arithmetic proof is an import. There is no RH, simplicity,
stationarity of dyadic Hardy sampling or process-realization premise.

Define f(s)=Z(H+s/ell). Retain f on [0,L], append on [L,P] the
quintic matching its value and first two ordinary s derivatives at L
to those at 0, and repeat with period P. Call this proposed function g.
All assertions concern this specified bridge, without changing its
length or selecting special endpoints.

## Conclusion

The prescription gives a real C2 periodic function. If U is uniform
on [0,P), the random path X(s)=g(U+s) defines a translation-invariant
Borel probability law on C2(R;R). Its ordinary lag-one jets

    V_(r,j)=g^(j)(U+r), r=0,1; j=0,1,2,

satisfy all 21 second and 126 fourth requirements of L473 (2) on one
eventual ray of real H. More precisely, with constants independent of
H, for every second pair and every |m|=4,

    |E V_a V_b-S_ab(H)|
        <= C_2 (H^(-2/3)/ell+1/H),                         (1)
    |E product_a V_a^m_a-F_m(H)|
        <= C_4 (H^(-1/3)/ell+ell^3/H).                     (2)

In addition, at both lags the four tight entries are exactly zero:

    E V_(r,0)V_(r,1)=E V_(r,1)V_(r,2)=0.                 (3)

The paired law has the weaker deterministic support bound
|V|<=C H^(1/6); no support bound ell^2 is established. No positive
clipped-mass lower bound, realization of L473's particular nu_H,
derivative-preserving rare/bulk decomposition, actual-Xi transfer or
RH conclusion follows. This is a standard interpolation/occupation
specialization; it is local progress, with no claim of originality
beyond the sources checked. The separate critical application audit
below passes without repair; arithmetic source proofs remain imports.

## Proof

### Polynomial bridge and endpoint matching

Ordinary Hermite interpolation with two distinct nodes and
multiplicity three at each has a unique polynomial of degree at most
five. One precise source is Van Manh Phung, *Continuity and Convergence
Properties of Integral Means of Bojanov--Xu Interpolation*, Z. Anal.
Anwend. 37 (2018), 251--268,
[DOI 10.4171/ZAA/1612](https://doi.org/10.4171/ZAA/1612),
[publisher PDF](https://ems.press/content/serial-article-files/35980),
Theorems 2.1--2.2, pp.253--254. All six endpoint data here are supplied.
For quantitative derivative bounds we explicitly replay the polynomial
formula instead of inferring an operator bound merely from existence.

On 0<=u<=1 take

    h00=1-10u^3+15u^4-6u^5,
    h10=u-6u^3+8u^4-3u^5,
    h20=(u^2-3u^3+3u^4-u^5)/2,
    h01=10u^3-15u^4+6u^5,
    h11=-4u^3+7u^4-3u^5,
    h21=(u^3-2u^4+u^5)/2.

Differentiation and evaluation give the following triples, in the
order (value, first derivative, second derivative):

| Polynomial | At 0 | At 1 |
| --- | --- | --- |
| h00 | (1,0,0) | (0,0,0) |
| h10 | (0,1,0) | (0,0,0) |
| h20 | (0,0,1) | (0,0,0) |
| h01 | (0,0,0) | (1,0,0) |
| h11 | (0,0,0) | (0,1,0) |
| h21 | (0,0,0) | (0,0,1) |

Thus the bridge is explicitly

    b(u)=sum_(j=0)^2 [f^(j)(L) h_j0(u)+f^(j)(0) h_j1(u)],
    g(L+u)=b(u).

There is no extra length scaling: the bridge interval has length one.
The table verifies the joins through order two at L and P=0 modulo P.
The periodic extension is consequently C2, including its second
derivative at both joins; no third-derivative match is claimed.
Uniqueness can also be checked directly: a difference with all six
zero endpoint data is divisible by u^3(u-1)^3, which has degree six.

For a polynomial on [0,1], its supremum is at most the sum of the
absolute values of its coefficients. Summing these coefficient bounds
over the six displayed polynomials gives respectively 101, 483 and
1143 after zero, one and two derivatives. Therefore

    max_(k<=2) sup_[0,1] |b^(k)|
        <=1143 max_(j<=2, q in {0,L}) |f^(j)(q)|.           (4)

The explicit formula and (4) are necessary applicability calculations,
not a reproof of an arithmetic or realization theorem. They also avoid
the inconsistent coefficient row noted in Finn's interpolation notes
by the source assessment.

### Uniform endpoint and neighborhood bounds

For each j<=2, the chain rule with ell fixed gives

    f^(j)(s)=ell^(-j) Z^(j)(H+s/ell).                      (5)

Choose H sufficiently large that ell>=1, L>2 and
[H,2H+1/ell] is contained in [H,3H]. The fixed-order pointwise input
and the finite set of orders give one constant A_0 such that

    |f^(j)(s)|<=A_0 H^(1/6), 0<=s<=L+1, j<=2.            (6)

Here f beyond L is used only as the reference Hardy function, not as
the bridge. In particular (6) covers [0,1], [L-1,L+1] and all six
bridge data. By (4), with A=1143 A_0 enlarged if necessary, every
coordinate of the periodic jet g,g',g'' is bounded by A H^(1/6).
All constants are independent of real H on the same eventual ray.

### The path law and the complete phase comparison

The map from the phase circle R/PZ to C2(R;R), u -> g(u+.), is
continuous in the topology of uniform convergence of the function and
its first two derivatives on compact sets. Indeed each g^(j), j<=2,
is continuous and periodic, hence uniformly continuous. The pushforward
of normalized Lebesgue measure is a Borel probability law. Translation
of paths by any real a corresponds to u -> u+a modulo P; Lebesgue
measure on the circle is invariant. This proves full real-shift
stationarity, not just invariance at integer times. This is the
elementary periodic occupation construction discussed by F. Colonius
and W. Kliemann, *Stability radii and Lyapunov exponents*, in *Control
of Uncertain Systems* (1990), pp.19--55,
[institutional scan](https://opus.bibliothek.uni-augsburg.de/opus4/files/47118/47118.pdf),
Section 7, p.39, Stat paragraph; no manifold or stability theorem is
needed for the explicit circle pushforward just proved.

Let M be any monomial of total degree d in the six lagged coordinates,
where d=2 or d=4, with repetitions permitted and no factorials. Write

    W_f(s)=(f^(j)(s+r))_(r,j),
    W_g(s)=(g^(j)(s+r))_(r,j),
    m_f=(1/L) integral_0^L M(W_f(s)) ds.

By (5) and the substitution t=H+s/ell, this m_f is exactly the
appropriate S_ab(H) or F_m(H), including the original lag-one samples
past 2H. Define psi_f=M(W_f) and psi_g=M(W_g). These agree on
[0,L-1]. The remaining periodic phases consist of [L-1,L] and [L,P].
On the first interval, s is on the Hardy segment and s+1 is on the
bridge. On the second, s is on the bridge and s+1 modulo P lies in
[0,1]. Thus wrap-around is accounted for without using a Hardy value
in place of a bridge value. Endpoint coincidences are harmless by C2
matching. The reference integrand on [L-1,L] uses f on [L-1,L+1],
which is covered by (6).

Subtracting the complete reference integral, with its normalization,
gives the exact identity

    E M(V)-m_f
      =-m_f/P
        +(1/P) [integral_(L-1)^L (psi_g-psi_f) ds
                                      +integral_L^P psi_g ds]. (7)

The first term is (L/P-1)m_f; it must not be dropped. Each of the
three integrands in the bracket has absolute value at most
A^d H^(d/6), and each interval has length one. Consequently

    |E M(V)-m_f| <= (|m_f|+3 A^d H^(d/6))/P.              (8)

This bound covers every monomial separately, including mixed height
allocations and odd total derivative orders. It does not assume any
cross-height cancellation.

L473 (6) gives |m_f|<=B_2 ell for each second monomial on an eventual
ray. For fourth monomials, |M(Y)|<=|Y|^4 and L473 (10) give
|m_f|<=B_4 ell^4. Choose common constants using the finite index
sets. Since P>=H ell, (8) is exactly (1)--(2) after enlarging constants.
Both terms in (1) are O(1). The right side of (2) is O(ell^3), since
ell>=1 and H>=1. Thus all ordinary second and every fourth tolerance
pass. In fact these comparison errors tend to zero; their stronger
size does not give the missing hard support or clipped lower bound.

### The four absolute odd requirements and a common ray

The generic comparison is not used to prove the four tight absolute
bounds. Periodicity and the fundamental theorem of calculus give

    (1/P) integral_0^P g(u)g'(u) du
       =[g(u)^2]_0^P/(2P)=0,
    (1/P) integral_0^P g'(u)g''(u) du
       =[g'(u)^2]_0^P/(2P)=0.

The integrands are continuous; g is C2 and periodic together with
g', so both endpoint identities are valid. Translating u by r=0 or 1
leaves each period average unchanged. Hence all four moments are
exactly zero, proving their required O(H^(-2/3)ell^(-1)) and
O(H^(-2/3)ell^(-3)) absolute bounds. There is no substitution of an
O(1) approximation for a small odd moment.

Take the maximum of the finitely many source onsets and constants,
and impose ell>=1 and L>2. All conditions then hold on one eventual
ray of real H, without a subsequence or endpoint selection. The six
coordinate bounds give |V|<=sqrt(6) A H^(1/6), so every observable
used above is integrable for fixed H. This bound exceeds ell^2
asymptotically and therefore does not certify L473's hard support.
There is also no positive lower bound for E(x_0 z_0-y_0^2)_+ here.
L581's exact-law impossibility is preserved: the periodic law changes
the marginal and has not been identified with nu_H.

### Separate critical application audit, 31 October 2026

This audit uses the unchanged source scope recorded in
`drafts/literature/2026-10-31-l582-closure-audit-scope.md`. It checks
the application, not the imported arithmetic estimates. In particular
L473's Proposition 3 qualification is retained.

**Endpoint data and operator bound.** Direct evaluation of each of the
six displayed polynomials and its first two derivatives gives exactly
the endpoint triples in the table. As an independent arithmetic check,
their absolute coefficient sums are as follows; the columns refer to
derivative orders zero, one and two:

| Basis | Order 0 | Order 1 | Order 2 |
| --- | --- | --- | --- |
| h00 | 32 | 120 | 360 |
| h10 | 18 | 66 | 192 |
| h20 | 4 | 14 | 38 |
| h01 | 31 | 120 | 360 |
| h11 | 14 | 55 | 168 |
| h21 | 2 | 8 | 25 |
| Sum | 101 | 483 | 1143 |

On the unit interval each monomial has absolute value at most one,
so these sums imply (4) for arbitrary real endpoint data. The second
derivative data multiply h20 and h21 without another factorial, since
their second endpoint derivatives are already one. The joins at L
and P=0 therefore agree through order two. The chain rule (5) keeps
ell fixed; it introduces exactly ell^(-j), not a derivative of ell.
The pointwise input on [H,3H] covers every endpoint and all reference
arguments up to 2H+1/ell. Only three fixed orders and finitely many
height windows are involved, so (6) has a common eventual constant.

**Law and phase partition.** For each fixed H the periodic derivatives
through order two are uniformly continuous on R. This proves
continuity into the stated compact-open C2 topology for every compact
set and hence Borel measurability. Uniform circle phase is invariant
under every real rotation; its pushforward is a stationary probability
law without a dyadic-Hardy stationarity premise. All its jet moments
are finite by (4)--(6).

For s in [0,L-1], both s and s+1 belong to the retained segment.
For s in [L-1,L], only the lag-one coordinate can enter the bridge.
For s in [L,L+1], the lag-zero coordinate is on the bridge and the
lag-one coordinate modulo P is in [0,1]. These exhaust a period.
At boundary points the matching jets agree, so interval endpoints
cause neither an omitted region nor a discontinuity. The reference
last strip still uses the unmodified Hardy values on [L,L+1].

Writing I for the reference integral and J for the periodic integral
gives J=I+integral_(L-1)^L(psi_g-psi_f)+integral_L^P psi_g.
Since I=L m_f and P=L+1, division by P and subtraction of m_f
give exactly (7), including -m_f/P. There are three terms bounded by
A^d H^(d/6) in the two boundary integrals, proving (8). Under
t=H+s/ell, ds=ell dt and L=H ell, so I/L is precisely L473's
reference integral, including its derivative divisors and shifted
upper endpoint. No binomial or factorial coefficient belongs in a
single monomial comparison.

**Complete tolerances and constants.** There are binomial(7,2)=21
unordered second pairs of six coordinates and binomial(9,4)=126
degree-four multi-indices. The argument for (8) applies to every one,
including repetitions and both-height odd allocations. L473 (6)
implies |m_f|<=B_2 ell for degree two; for degree four,
|M(Y)|<=|Y|^4 and L473 (10) imply |m_f|<=B_4 ell^4. Thus (8)
gives exactly (1) and (2). Their ratios to the ordinary required
error scales 1 and ell^3, respectively, are bounded and tend to zero.
This checks the ordinary second entries and every fourth entry,
without assuming any cross-height cancellation.

The four exceptional second requirements are different: their
absolute moments, rather than approximation errors, must be small.
For each fixed H, g^2 and (g')^2 are continuously differentiable and
periodic, with derivatives 2gg' and 2g'g''. Their integrals over a
period vanish exactly. Rotation by either lag leaves these integrals
unchanged. All four exceptional moments are therefore zero, which
satisfies both specified power-saving scales without estimating the
small reference moments by O(1).

Maximizing the finitely many imported onsets and constants and imposing
ell>=1, L>2 gives one eventual ray of real H for all 147 entries.
No endpoint selection or subsequence has entered. The claimed support
bound follows only as |V|<=sqrt(6) A H^(1/6); an upper bound on that
larger scale does not prove or disprove hard ell^2 support for this law.
The audit passes without changing any conclusion or dependency. It
supplies no clipped lower bound, identification with nu_H, arithmetic
source-proof audit or Xi transfer. L581's exact-law stop remains intact.

## Mathlib

Full matching Mathlib coverage of the Hardy inputs, this closure and
the paired moment conclusion has not been checked. No absence claim
or matching theorem is asserted. The standard interpolation source,
explicit polynomial verification, chain rule, periodic fundamental
theorem of calculus and circle-measure pushforward are the inputs
used here. L473 supplies the imported moment bounds; its arithmetic
source proofs and the fixed-order pointwise arithmetic proof remain
unaudited. The separate critical application audit above verifies this
specialization without asserting matching formal-library coverage.
