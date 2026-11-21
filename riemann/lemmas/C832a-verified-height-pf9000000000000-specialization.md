# Corollary 832a: verified-height PF order 9000000000000

## Hypotheses

Use the actual ordinary coefficient sequence of L832,

\[
G(w)=\frac18\xi\left(\frac12+\frac{\sqrt w}{2}\right)
 =\sum_{n\ge0}a_nw^n,\qquad
a_n=\frac{M_{2n}}{8\,4^n(2n)!},\qquad a_n=0\ (n<0).
\]

The square-root expression denotes the entire series. Retain L832's
imported closed verified height H=3000175332800 and its genus-zero
product, zero correspondence and positive normalization. Set exactly
m=9000000000000. No RH, simplicity, strict signs, numerical zero
enclosures or bound on L836(8) is assumed.

## Conclusion

The actual sequence (a_n) is PF_m: every ordered Toeplitz minor
det[a_(q_j-p_i)] of size 1<=d<=m, with increasing nonnegative row
indices p_i and column indices q_j, is nonnegative. In particular,

\[
D_{(r,k)}\ge0\qquad(1\le r\le9000000000000,\ k\ge0).
\]

This is a known sector-theorem specialization at the proposed order,
not a new PF theorem or a numerical overlap certificate. It includes
shift6002 only in this finite rank range. No strictness, all-rank sign
or growing-shift sign beyond this range follows. The bounded critical
audit recorded below accepts precisely this finite nonnegative scope.

## Proof

**Imported theorem and applicability.** Reuse the primary results
assessed for the approved test and precisely recorded in L832:
Wojciech Michałowski, *An explicit uniform cubic wedge for consecutive
Toeplitz minors of the Riemann xi-coefficients*,
[arXiv:2607.16795v1, Section1.2](https://arxiv.org/html/2607.16795v1#S1.SS2),
gives the sufficient finite-height condition m+1<=pi H. For all ordered
minors, the theorem used there is Schoenberg's sufficient polynomial
sector theorem, as stated in Olga M. Katkova, *Multiple positivity and
the Riemann zeta-function*,
[arXiv:math/0505174v1](https://arxiv.org/pdf/math/0505174v1),
TheoremB, printed p.5, with Definition2/(8), printed p.4: a real
polynomial with positive constant term and no zero in the open sector
|arg w|<pi m/(m+1) has its coefficient sequence in PF_m. Katkova (6),
printed p.3, and Theorem1's proof, pp.5–6, give the genus-zero
product and compact-product passage used in L832. We apply these
results; no general sector or product theorem is reproved.

The closed height is the imported theorem of Dave Platt and Tim
Trudgian, *The Riemann hypothesis is true up to 3 times 10^12*,
[arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1),
Theorem1, printed p.2. Its computational verification is imported,
not rerun. The additional Section2 simplicity inference in L834 is
unneeded for PF applicability.

The only changed parameter from L832's application is the integer m.
Using the standard bound pi>3, exact integer arithmetic gives

\[
m+1=9000000000001
 <9000525998400=3H<\pi H,
\qquad 3H-(m+1)=525998399>0.                       \tag{1}
\]

Here is the sector comparison explicitly, without presuming an enlarged
PF conclusion from PF6001 alone. L832's zero-location argument puts
every zero w of G with 0<|gamma|<=H on the negative real axis,
including |gamma|=H. It excludes gamma=0 and w=0. For |gamma|>H,
the same argument yields

\[
\pi-|\arg w|
 =2\arctan\frac{|\beta-1/2|}{|\gamma|}
 <\frac1H<\frac\pi{m+1}.                         \tag{2}
\]

The first strict bound uses 0<beta<1 and |gamma|>H; the second is
(1). Thus |arg w|>pi m/(m+1) for these zeros. Negative real zeros
also avoid the required open sector. No boundary zero above H is
excluded by an RH assumption.

L832's product representation of this exact G is
G(w)=G(0) prod_nu(1-w/omega_nu), with G(0)>0 and
sum_nu |omega_nu|^(-1)<infinity. Its finite conjugation-invariant
products have real coefficients and positive constant term; repeated
zeros are retained with multiplicity. By (2) every such polynomial
satisfies the cited sector theorem for this m. Hence every one is PF_m.
The compact convergence and fixed-minor limit already justified in
L832 apply unchanged: for each fixed finite pair of index sets,
Cauchy's coefficient formula gives convergence of all the finitely
many relevant coefficients, and determinant continuity preserves their
nonnegative signs. No limit uniform in d or the indices is required.
Since these index sets and 1<=d<=m were arbitrary, G is PF_m.

This is G itself, with ordinary coefficients. In Katkova's notation
G(w)=xi_1(w/4)/8, so a_n=8^(-1)4^(-n)b_n. Every ordered d-by-d
minor has the positive rescaling factor
8^(-d)4^(sum_i p_i-sum_j q_j), including the zero extension to
negative indices. Thus the import has the claimed normalization.
Taking p_i=i-1 and q_j=k+j-1 proves the displayed consecutive-minor
consequence. Strictness and quantitative determinant lower bounds
are not furnished by this limit.

The unexecuted endpoint/ball computation in L836 is independent of
this sector application. In particular (1) neither establishes its
strict overlap inequality nor proves positivity for r>m. This is local
progress by specialization of inspected known inputs only.

**Bounded critical audit, 6 November 2026.** The stated specialization
passes without a mathematical correction. The source coverage reused
is Katkova v1 Definition2/TheoremB and the entire-product passage,
Platt–Trudgian v1 Theorem1, and Michałowski v1 Sections1.1–1.2,
at the precise locations cited above. This audit checks their local
application; it does not reprove the sector theorem, inspect
Schoenberg's original proof or replay the verified-height computation.

For the sector direction, write u=beta-1/2. A zero above the verified
height has |u|<1/2 and |gamma|>H. The full comparison, also covering
u=0, is

\[
0\le\pi-|\arg w|=2\arctan(|u|/|\gamma|)
 \le 2|u|/|\gamma|<1/|\gamma|<1/H<\pi/(m+1).
\]

Thus its absolute argument is greater than pi*m/(m+1), as required
by the sufficient theorem, rather than smaller. The exact arithmetic
in (1) has positive margin 525998399 using pi>3. For heights through
H, including equality, the positive-height theorem and conjugation
put the image on the negative real axis. The gamma=0 case is excluded
by xi(beta)=Xi(i(1/2-beta))>0. Also G(0)>0, so no argument at zero
is used. A zero on the negative axis stays outside the open sector
with either principal-argument convention. None of these cases needs
simplicity or an assertion about the unverified boundary line.

The product is indexed by zeros of G with their own multiplicities;
it does not count the two reflected xi zeros twice. Its summable
reciprocal moduli and positive constant are facts established in
L832's proof independently of its PF6001 conclusion. Full nonreal
conjugate pairs and repeated real factors give real finite products
to which TheoremB applies at this new m. Compact convergence gives
each fixed nonnegative-index coefficient by Cauchy's formula, with
negative-index entries identically zero. For arbitrary fixed increasing
nonnegative row and column sets, their finite determinant is continuous
in just those entries. Its nonnegative approximating values therefore
have a nonnegative limit. Quantifying over these fixed choices after
the limit proves every minor of every size d<=m; no uniform limit over
indices or ranks, or preservation of strictness, has been used.

The diagonal rescaling has determinant
8^(-d)*4^(sum p_i-sum q_j)>0, including zero negative-index entries.
Taking p_i=i-1 and q_j=k+j-1 gives exactly a_(k+j-i), without a
transpose or reversal. Consequently the ordinary-coefficient and
consecutive-minor conventions agree for the full claimed family.
The single L832 input in the DAG is sufficient because its proof
establishes the product, zero locations and normalization just used;
PF6001 alone would not be sufficient. L834's simplicity argument
and L836's unpaid numerical inequality are not mathematical inputs.
The audit accepts a known-result specialization only. It establishes
no new bound beyond the cited sector mechanism, no strict minor
margin and no progress on the remaining all-degree sign implication.

## Mathlib

Full matching coverage has not been checked; neither presence nor
absence is asserted. The full finite-height PF specialization, cited
verification, sector theorem and compact product argument are imported
informally. Exact integer arithmetic, pi>3, coefficient rescaling and
continuity of a fixed determinant are supporting standard mathematics.
