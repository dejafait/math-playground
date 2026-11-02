# Corollary 582a: a compatible bridge defeats normalized scalar cutoffs

## Hypotheses

Use L582's real H, ell=log H, L=H ell, P=L+1, retained Hardy
segment f(s)=Z(H+s/ell) on [0,L], ordinary derivatives through two,
and fixed-order pointwise imports. Use L473 (1)--(2),(6),(9)--(10)
with exactly its 21 second and 126 fourth requirements. Constants
and onsets are uniform on an eventual ray of real H. The arithmetic
source proofs remain imports, including Bui--Hall Proposition 3's
omitted proof; this result does not audit them.

Permit a different C2 bridge only on [L,L+1]. For each fixed H let
phi_H:R->R be any C2 function with phi_H(0)=0 and phi_H'(0)=1.
No uniform bound on phi_H or its derivatives is assumed, and phi_H
may depend on the constructed bridge. There is no RH, simplicity,
positive clipped-mass or realization-of-nu_H premise.

## Conclusion

There is one such modified real C2 periodic function g_H, chosen
independently of phi_H, whose stationary uniform-phase paired jet V
satisfies every L473 (2) requirement and |V|<=C H^(1/6). More precisely,
the ordinary second comparison errors and every fourth comparison
error obey respectively

    C_2(H^(-2/3)/ell+1/H),
    C_4(H^(-1/3)/ell+ell^3/H),                              (1)

and the four tightly constrained signed odd second moments vanish.
The same constants
and onset work for all H on the eventual ray and all 147 entries.

For every allowed phi_H, put h_H=phi_H o g_H and let U be uniform
on [0,P). Its ordinary paired jet W=(h_H^(j)(U+r))_(r=0,1;j=0,1,2)
satisfies

    Pr{|W|>ell^2}>0.                                      (2)

Thus these tolerances, derivative-consistent stationarity and the
coarse jet bound alone cannot certify ell^2 support by normalized
scalar composition uniformly over compatible bridges. This does not
settle saturation of L582's specified original quintic, exclude maps
with another slope at zero, preserve positive clipping, or give Xi
transfer. It is a standard Hermite/chain-rule specialization, with no
claim of a new general interpolation or composition theorem. The separate
critical application audit below passes; arithmetic source proofs
remain unaudited imports.

## Proof

### Fixed-node construction and all joins

Use the six polynomials h_j0,h_j1, j=0,1,2, displayed and checked
in L582. Their kth derivatives at 0 and 1, for k<=2, are

    h_j0^(k)(0)=delta_jk, h_j0^(k)(1)=0,
    h_j1^(k)(0)=0,        h_j1^(k)(1)=delta_jk.

The standard interpolation input is Van Manh Phung, *Continuity and
Convergence Properties of Integral Means of Bojanov--Xu Interpolation*,
Z. Anal. Anwend. 37 (2018), 251--268,
[DOI 10.4171/ZAA/1612](https://doi.org/10.4171/ZAA/1612),
[publisher PDF](https://ems.press/content/serial-article-files/35980),
Theorems 2.1--2.2, pp.253--254: distinct real nodes and positive
multiplicities give the unique polynomial below the total multiplicity
matching all supplied derivative data. Apply this twice with two
nodes, multiplicity three each. The explicit basis is needed for
the scale bound, rather than reproving the interpolation theorem.

Write a_j=f^(j)(L), c_j=f^(j)(0), and

    (m_0,m_1,m_2)=(0,0,2 ell^2).

For 0<=u<=1 define

    b(u)=sum_(j=0)^2 2^(-j)
                [a_j h_j0(2u)+m_j h_j1(2u)],   0<=u<=1/2,
    b(u)=sum_(j=0)^2 2^(-j)
                [m_j h_j0(2u-1)+c_j h_j1(2u-1)], 1/2<=u<=1.
                                                               (3)

The ordinary kth derivative introduces 2^k. At an endpoint the
only nonzero basis derivative has j=k, so 2^(k-j)=1. Consequently
the endpoint triples of b are (a_0,a_1,a_2) at 0 and
(c_0,c_1,c_2) at 1. Both one-sided midpoint triples are exactly m.
These facts verify every value, first- and second-derivative join.
Define g_H=f on [0,L], g_H(L+u)=b(u), and extend periodically with
period P. This is C2, including the midpoint and the join P=0.
No third-derivative matching or global polynomial bridge is claimed.

### A common quantitative bound

L582's basis coefficient sums imply that the sum of absolute bounds
of the six kth basis derivatives on [0,1] is at most 1143 for
each k<=2. In (3), 2^(-j)<=1 and 2^k<=4. Thus, with
D_H=max_(j<=2){|a_j|,|c_j|,|m_j|},

    max_(k<=2) sup_[0,1] |b^(k)|<=4572 D_H.                (4)

This bound holds on both halves and their common join. L582's imported
fixed-order pointwise bound gives, on a common eventual ray,

    |f^(j)(s)|<=A_0 H^(1/6), 0<=s<=L+1, j<=2.

It includes reference values past L and both sets of bridge data.
Since ell^2/H^(1/6)->0, enlarge the onset so ell>=1, L>2 and
ell^2<=H^(1/6). Then D_H<=max{A_0,2}H^(1/6). Taking
A=4572 max{A_0,2} bounds every g_H derivative through two and every
reference f derivative on [0,L+1] by A H^(1/6). The constants are
independent of H; no endpoints or heights have been selected.

The circle pushforward U->g_H(U+.) is continuous into C2(R;R)
with its compact-open derivative topology: each derivative through
two is continuous and periodic, hence uniformly continuous. It
therefore defines a Borel probability law invariant under every real
translation. The six coordinate bounds give |V|<=sqrt(6)A H^(1/6).

### Complete moment comparison and the tight entries

For any degree-d monomial M in the six coordinates, d=2 or 4,
let W_f(s)=(f^(j)(s+r))_(r,j), W_g(s)=(g_H^(j)(s+r))_(r,j),
psi_f=M(W_f), psi_g=M(W_g), and

    m_f=(1/L) integral_0^L psi_f(s) ds.

Substitution t=H+s/ell, with ell fixed, identifies m_f with exactly
S_ab(H) or F_m(H), including the shifted reference values past 2H.
The integrands agree on [0,L-1]. On [L-1,L] the lag-one entry can
enter the new bridge; on [L,L+1] lag zero is in the bridge while
lag one wraps into [0,1]. These two strips exhaust all changed phases,
irrespective of the internal midpoint join. Exact subtraction gives

    E M(V)-m_f=-m_f/P
          +(1/P)[integral_(L-1)^L (psi_g-psi_f) ds
                              +integral_L^(L+1) psi_g ds].     (5)

All three integrands in the bracket are bounded by A^d H^(d/6).
It follows that

    |E M(V)-m_f|<=(|m_f|+3 A^d H^(d/6))/P.                (6)

L473 (6) gives |m_f|<=B_2 ell for each second monomial. Its (10)
gives |m_f|<=B_4 ell^4 for each fourth monomial, since
|M(Y)|<=|Y|^4. Taking common constants over the finite index sets
and using P>=H ell proves (1). The second bound is O(ell^3)
and the first is O(1). This proves every ordinary second requirement
and every fourth requirement, including repeated coordinates and
mixed lag allocations; no cross-lag cancellation is presumed.

For the four exceptional requirements, comparison errors are
insufficient. Instead g_H^2 and (g_H')^2 are C1 and periodic, so

    integral_0^P g_H g_H' = [g_H^2]_0^P/2=0,
    integral_0^P g_H' g_H'' = [(g_H')^2]_0^P/2=0.

Rotation by r=0 or 1 leaves each period average unchanged. All four
signed odd second moments vanish, so their absolute values satisfy the
respective H^(-2/3)ell^(-1) and H^(-2/3)ell^(-3) bounds.
There are binomial(7,2)=21 second pairs, of which four use this exact
cancellation, and binomial(9,4)=126 fourth monomials. Thus all 147
entries pass. The finitely many onsets and constants, including the
pointwise and reference-moment imports, can be maximized on the same
real-H ray. This establishes no source-proof audit.

### Normalized scalar composition fails on positive phase measure

Fix any H on that ray and any allowed phi_H. C2 composition is C2
and periodic. The classical second-order chain rule is

    h_H''(s)=phi_H''(g_H(s))(g_H'(s))^2
                         +phi_H'(g_H(s))g_H''(s).         (7)

This standard identity is also recalled in Section 1 of Gérard
Bourdaud, *The higher order chain rule in Sobolev spaces*,
[arXiv:2401.16987v1](https://arxiv.org/html/2401.16987v1).
Only the classical C2 identity is used, not a global Sobolev-space
composition theorem for this periodic function.

At s_*=L+1/2, construction (3) gives g_H(s_*)=g_H'(s_*)=0 and
g_H''(s_*)=2 ell^2. Normalization therefore yields

    h_H(s_*)=0, h_H'(s_*)=0, h_H''(s_*)=2 ell^2.         (8)

Since h_H'' is continuous and ell>0, some delta>0, possibly depending
on H and phi_H, satisfies delta<1/4 and

    |h_H''(s)|>3 ell^2/2
                    whenever |s-s_*|<delta.

This interval lies strictly inside the bridge and [0,P). For phases
U in it, the lag-zero second coordinate alone exceeds ell^2, so
|W|>ell^2. Its uniform-phase probability is 2 delta/P>0, proving
(2). There is no assertion of a cutoff-independent probability lower
bound, nor is one needed to refute support in the closed ell^2 ball.
The law has finite moments for each fixed H because h_H is C2 and
periodic, although its moments are not asserted to satisfy (2) of
L473 after composition. Support failure already rules out the desired
conjunction for every normalized scalar cutoff.

The modification leaves the actual Hardy segment unchanged. It supplies
a generic-certification countermodel, not an obstruction established
at a zero of the actual Hardy function or for the original L582 bridge.
Neither positive clipping nor actual-Xi signs have been obtained.

### Separate critical application audit, 31 October 2026

The pre-existing SPECIALIZE assessment in
`drafts/literature/2026-10-31-c582a-independent-audit-scope.md`
covers precisely this audit. The arithmetic estimates in L473 and L582
are retained as imports; no assertion about their source proofs is added.

**Scaled basis and all joins.** Independent differentiation of L582's
six explicit polynomials gives these sums of absolute coefficients:

| Basis | Order 0 | Order 1 | Order 2 |
| --- | --- | --- | --- |
| h00 | 32 | 120 | 360 |
| h10 | 18 | 66 | 192 |
| h20 | 4 | 14 | 38 |
| h01 | 31 | 120 | 360 |
| h11 | 14 | 55 | 168 |
| h21 | 2 | 8 | 25 |

For example h20' = u-(9/2)u^2+6u^3-(5/2)u^4 and
h20'' = 1-9u+18u^2-10u^3, giving 14 and 38. Evaluating
all six polynomials through derivative order two at 0 and 1 gives
the stated Kronecker endpoint identities. In particular the
second-derivative basis is already normalized, with no missing factorial.
For either half of (3), multiply each order-j row by 2^(k-j).
The total coefficient bounds at derivative orders k=0,1,2 are then

    63+16+3/2=161/2,
    480+121+11=612,
    2880+720+63=3663.

All are bounded by 4572, so (4) is conservative. At each endpoint
only j=k survives, with factor one. The first half starts at a and
ends at m; the second starts at m and ends at c. Thus the retained
segment/bridge join at L, both midpoint limits at L+1/2, and the
periodic join at P=0 agree in all three derivatives. Piecewise C2
regularity with these matches proves global C2 regularity; no third
derivative is needed.

L582's pointwise import is on the full reference neighborhood
[0,L+1], where the Hardy heights are in [H,3H] for all sufficiently
large H. Holding ell fixed gives the factors ell^(-j). Taking one
constant for j<=2, then using ell^2/H^(1/6)->0, bounds a,c,m
on a common eventual real-H ray. The ray can also impose ell>=1 and
L>2. There is no selection of endpoint heights. Continuity of the
periodic derivatives verifies the circle pushforward and real-shift
stationarity. The Euclidean six-jet bound is sqrt(6) times the common
coordinate bound, uniformly before composition.

**Phase partition, normalization and all tolerances.** For
0<=s<=L-1 both reference samples lie on the retained segment. For
L-1<=s<=L the lag-one sample can lie on the bridge. For
L<=s<=L+1 lag zero lies on the bridge and lag one, modulo P, lies
in [0,1]. These are all phases, regardless of the bridge's internal
midpoint. The reference comparison on the penultimate strip uses the
original Hardy extension up to L+1. The pointwise import covers it.

The reference integral is L m_f. The periodic integral is that
integral plus the two correction integrals in (5). Since L/P-1=-1/P,
the normalization term is exactly -m_f/P. Bounding the difference
integral by two monomial bounds and the last integral by one gives
three, not two, copies of A^d H^(d/6). Under t=H+s/ell,
ds=ell dt and L=H ell, so m_f has exactly the normalization and
derivative divisors of L473 (1).

For degree two, (6) is bounded by
B_2/H+3A^2 H^(-2/3)/ell. For degree four it is bounded by
B_4 ell^3/H+3A^4 H^(-1/3)/ell. Ratios to the respective required
scales 1 and ell^3 tend to zero. The same degree-d estimate applies
to every monomial, not merely a representative selection: there are
6*7/2=21 unordered second pairs and binomial(9,4)=126 fourth
multi-indices, including repeated factors and both lags. The bound
|M(Y)|<=|Y|^4 handles all fourth entries, without factorials or any
cross-lag odd cancellation.

The four exceptional second requirements are absolute values of signed
expectations. They do not require expectations of absolute products to
vanish. The fundamental theorem of calculus for g_H^2 and (g_H')^2,
both C1 and periodic, makes the two corresponding period averages
exactly zero. Rotation gives the same at each lag. This handles all
four exceptional entries at their tight scales, in addition to the
17 ordinary pairs and 126 fourth entries. The finite imported
constants/onsets and the new elementary onset can be maximized once
for all 147 entries on the same eventual real-H ray.

**Cutoff quantifiers and positive measure.** The bridge and its ray
have been chosen before any phi_H. For each H on that ray and every
allowed C2 map, the classical chain rule at the common midpoint gives
exactly (8); the phi_H'' term is zero because g_H'=0. The matched
second derivatives make h_H'' continuous there. Thus some
0<delta<1/4 gives |h_H''|>3 ell^2/2 on the indicated open interval,
which lies inside (L,L+1) and [0,P). Its positive probability
2 delta/P proves failure of the almost-sure Euclidean jet bound.
A single exceptional phase would not suffice; this continuity argument
supplies an interval. Neither delta nor this probability is required
to be uniform in H or phi_H. No bound on the derivatives of phi_H is
used. Compactness of a period gives finite composed moments for each
fixed map, but their moment tolerances are not asserted.

The audit passes without changing the statement's mathematical scope
or its direct inputs. The clarification about signed odd expectations
does not strengthen a moment conclusion. The countermodel concerns a
modified compatible bridge, not the original L582 quintic or an
actual-Hardy zero. Original-path support, maps with another slope at
zero, positive clipped mass and actual-Xi signs remain open. This is
an independently checked local specialization, not a new standard
interpolation theorem or an advance beyond the cited source theorems.

## Mathlib

Full matching coverage for this modified bridge, paired moment statement
and scalar-cutoff obstruction has not been checked. No absence claim
is made. Hermite interpolation and the classical chain rule are the
precisely cited standard inputs; L582 provides the checked basis and
pointwise imports, and L473 supplies the reference moment bounds.
The fixed-order arithmetic proofs and Bui--Hall Proposition 3 remain
unaudited imports. The separate critical application audit above checks
this local specialization; full matching formal coverage remains unchecked.
