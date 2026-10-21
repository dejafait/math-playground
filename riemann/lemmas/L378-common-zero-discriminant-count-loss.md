# Lemma 378: distinct common zeros bound the discriminant count loss

## Hypotheses

Let H be real. Let F,G be real analytic on a connected open interval
I containing [H,infinity), neither identically zero. For ordinary real
derivatives set

\[
 \mathscr L(U)=U'^2-UU'',\qquad
 B(U,V)=2U'V'-UV''-U''V,\qquad
 D=B(F,G)^2-4\mathscr L(F)\mathscr L(G).
\]

Assume D(t)≤0 and \(\mathscr L(G)(t)>0\) for every t≥H.
Common zeros are allowed. In a closed interval [H,X], count G zeros
distinctly, F zeros with full analytic multiplicity, and common zeros
distinctly; denote these counts by N_G, N_F^mult and N_common.
Analyticity on an open neighborhood of the ray is equivalent to the
stated domain after restricting to its connected component.

## Conclusion

For every X≥H, including both endpoints in all three counts,

\[
 N_G([H,X])-N_F^{\rm mult}([H,X])
       \le N_{\rm common}([H,X])+1.                 \tag{1}
\]

Thus the approved target holds with the universal C_H=1. If F,G are
dependent over the real constants, the left side is zero. For an
independent pair, the Wronskian is nonzero at every noncommon point
of the ray, but its signs on different common-free pieces need not
agree. No actual-family discriminant sign, common-zero estimate,
Laguerre-sign extension or RH consequence is asserted. This new
conditional input is retained by the separate critical audit below.

## Proof

The prior EXPLORE assessment is
`drafts/literature/2026-10-08-count-bound-with-common-zeros.md`.
It reuses inspected primary separation and pencil comparisons, including
MIT 18.034 Spring 2009,
[Lecture 9, Theorem 9.1, printed pp. 1–2](https://ocw.mit.edu/courses/18-034-honors-differential-equations-spring-2009/0cdeb657491010f0f8c60aa49f2d5248_MIT18_034s09_lec09.pdf),
and J. Borcea, P. Brändén and B. Shapiro,
[*Pólya–Schur master theorems for circular domains and their boundaries*](https://staff.math.su.se/shapiro/Articles/Master4.pdf),
author Master4 manuscript, §3.1, Theorems 9–10, p. 9 (revision date
unverified; version inspected in the assessment on 2026-10-08).
Their common regular ODE or global polynomial
zero hypotheses are absent here; neither is imported. L374 supplies
the pencil/Taylor argument. Its disjoint-ray conclusion cannot be
applied directly to bounded pieces, so we justify the needed local
use explicitly. L373 is obstruction context, not a mathematical input.
No new search or historical originality claim is made.

**Localizing the Wronskian argument.** By the square completion in
L374, at every t≥H and every constant real a,b,

\[
 \mathscr L(aF+bG)
 =\mathscr L(G)\left(b+\frac{aB(F,G)}{2\mathscr L(G)}\right)^2
     -\frac{a^2D}{4\mathscr L(G)}\ge0.               \tag{2}
\]

For any constant pencil members U,V this implies
\(B(U,V)^2\le4\mathscr L(U)\mathscr L(V)\), including the case
\(\mathscr L(V)=0\): then the linear coefficient of the everywhere
nonnegative polynomial \(\mathscr L(U+sV)\) must be zero.

The finite-order contradiction in L374 uses only a right neighborhood
of the point in question. Explicitly, if V(t0)=v≠0 and
U(t0+x)=a x^m+O(x^(m+1)), a≠0, m≥2, differentiated analytic Taylor
expansions give

\[
 \mathscr L(U)=ma^2x^{2m-2}+O(x^{2m-1}),\qquad
 B(U,V)=-m(m-1)avx^{m-2}+O(x^{m-1}),\qquad
 \mathscr L(V)=O(1).
\]

Dividing the pencil inequality by x^(2m−4) and letting x decrease to
zero through positive values would give
\(m^2(m-1)^2a^2v^2\le0\), a contradiction. This reasoning needs
neither disjointness beyond t0 nor an entire common-free ray. The
hypothesized inequalities hold for all sufficiently small positive x,
even if t0=H or t0 is the upper counting endpoint X.

Assume now that F,G are independent. Write W=FG'−F'G. At any
noncommon t0≥H with G(t0)≠0, W(t0)=0 would make
U=F−(F(t0)/G(t0))G satisfy U(t0)=U'(t0)=0, while V=G is nonzero
there. Independence and the analytic identity theorem on I ensure
that U is not identically zero and has a finite zero order at least
two. The preceding contradiction applies. If G(t0)=0, noncoincidence
gives F(t0)≠0; W(t0)=0 would give G'(t0)=0 and the same contradiction
with U=G,V=F. Thus W(t0)≠0 at every noncommon point. Independence
persists on every open subinterval by the identity theorem, so no
piece has an unnoticed dependent exception. At a noncommon F zero,
W=−F'G≠0, proving simplicity there. Also every G zero, common or
otherwise, is simple directly from \(\mathscr L(G)=G'^2>0\) at that
zero. No restriction on F multiplicity at common points is needed.

**Finite partition and exact count.** Fix X>H. The zero sets of both
functions in [H,X] are finite by compactness, analyticity on I and the
identity theorem. Let k=N_common([H,X]) and remove these k distinct
points from [H,X]. The remaining set has at most k+1 nonempty connected
pieces, each an interval with any included boundary endpoints inherited
from [H,X]. In particular a common H or X is removed, rather than
counted in an adjacent piece.

On each piece W is continuous and nowhere zero, hence has one fixed
sign. Let r_i be its number of G zeros (all noncommon). If r_i≥2,
each consecutive pair a<b of these zeros has no G zero in (a,b):
any such zero would be noncommon and in the same piece. G therefore
has a nonzero constant sign there. Simplicity shows that G'(a) and
G'(b) have opposite signs. Since W(a)=F(a)G'(a) and
W(b)=F(b)G'(b) have the same nonzero sign, F(a),F(b) have opposite
signs. The intermediate value theorem gives an F zero in (a,b).
This zero is noncommon, because the entire interval lies in this
piece. Distinct consecutive gaps give distinct F zeros, including
when a=H or b=X is an included noncommon endpoint.

Consequently piece i contributes at least max(r_i−1,0) noncommon
F zeros, each of multiplicity one. For r_i=0 or 1 this bound is
zero and needs no separation argument. Put q=sum_i r_i, the number
of all noncommon G zeros, and let p be the number of pieces with
r_i≥1. Then p≤k+1 and

\[
 \sum_i\max(r_i-1,0)=q-p,\qquad
 N_G=q+k,\qquad N_F^{\rm mult}\ge q-p+k.             \tag{3}
\]

The final k contribution is justified because every removed common
point is an F zero of positive finite multiplicity, counted once or
more with full weight even at H or X. It is distinct from every
interior zero counted above. There is no duplication between pieces
or at removed endpoints. Subtracting (3) gives
N_G−N_F^mult≤p≤k+1, proving (1).

If X=H, there is at most one G zero and the F count is nonnegative;
hence the left side is at most one, which is at most N_common+1.
This handles the degenerate interval independently of the partition.

Finally, if F,G are dependent, their nonzero assumptions give F=cG
for a nonzero real constant c. All G zeros are simple by strict
\(\mathscr L(G)>0\), and F has exactly the same zeros with the same
multiplicities. Thus N_G−N_F^mult=0 for every closed [H,X], and (1)
holds without using a Wronskian sign. ∎

**Qualifications.** Only the local portion of L374 is reused; no
deflation, variable pencil coefficient, ODE, or global Wronskian sign
across common zeros is assumed. The proof is exact and requires no
numerical or mathematical script. The inequality supplies a conditional
count input, not a proof of the separate actual-theta hypotheses. Its
POTENTIALLY_NEW classification records the limited assessment outcome,
not certified novelty or progress beyond the inspected literature.

**Separate critical audit, 2026-10-08.** The prior EXPLORE coverage is
`drafts/literature/2026-10-08-common-zero-count-loss-audit.md`.
The following verification retains (1) without correcting or
strengthening it. L374 remains the only direct lemma input.

At a fixed point the pencil matrix has diagonal entries L(F), L(G)
and off-diagonal entry B(F,G)/2. Since L(G)>0, its Schur complement
is -D/(4L(G))≥0, proving positive semidefiniteness, including D=0.
For fixed constant pencil members U,V, the polynomial in s obtained
from L(U+sV) is therefore nonnegative for every real s. If L(V)>0
its discriminant gives the stated inequality; if L(V)=0, its linear
coefficient B(U,V) must vanish. This also handles both diagonal entries
being zero. The values used to choose a pencil member at t0 are then
held constant as t varies. No derivative of a variable coefficient is
being omitted.

For the local Taylor test, the leading coefficients of U'^2 and UU''
are m²a² and m(m−1)a², respectively, at order 2m−2. Their difference
is ma². Since V=v+O(x) and V',V'' are bounded, the unique contribution
at order m−2 in B(U,V) is −U''V, with coefficient −m(m−1)av.
Analyticity justifies the differentiated remainders. For m=2 one
already has L(U)(t0)=0 but B(U,V)(t0)=−2av≠0, contradicting the
pencil inequality at t0. For m>2, division by the positive power
x^(2m−4) leaves a positive left limit and a right side O(x²).
All sufficiently small x>0 are in I and in the hypothesized ray.
In particular this remains valid at either counting endpoint; the
assumptions extend to the right of X, even though the count stops at X.

If a constant pencil member vanishes identically on any open piece,
the real analytic identity theorem on connected I makes it vanish on
I. Likewise an infinite-order zero would imply local and hence global
vanishing. Thus independence on I guarantees the required nonzero
finite Taylor coefficient, on every piece. At G(t0)≠0 the chosen
U has derivative −W(t0)/G(t0); at G(t0)=0, noncoincidence gives
W(t0)=F(t0)G'(t0) with F(t0)≠0. Both possible W=0 cases are
therefore excluded by the local argument. Strict L(G)>0 already rules
out G'(t0)=0 at any G zero, including a common zero. For an independent
pair every noncommon F zero is simple since W=−F'G≠0 there.
Nothing in this reasoning bounds the multiplicity of a common F zero
or asserts that W keeps its sign through a common zero.

For X>H, both zero sets in [H,X] are finite: an infinite set would
accumulate in that compact interval, whose endpoints lie inside the
open analytic domain, contradicting identity and nonzero assumptions.
Removing k distinct common points leaves at most k+1 interval pieces.
Removal of H or X can only reduce this number; neither endpoint is
assigned to a piece when common. On each piece the now nonvanishing
W has a constant sign. If a<b are consecutive noncommon G zeros in
that piece, its interval property puts [a,b] inside the piece and
excludes every common zero there. The sign of G on (a,b) equals
sign G'(a) and −sign G'(b), so the derivative signs are opposite.
The equal signs of F(a)G'(a) and F(b)G'(b) then force opposite F
signs and an F zero strictly between a and b. These open gaps are
disjoint, both within a piece and across pieces. Included noncommon
H or X cause no endpoint loss.

An occupied piece with r_i≥1 contributes r_i−1 such F zeros; a
piece with r_i=0 contributes the lower bound zero. Thus q−p is
nonnegative and counts distinct noncommon F zeros, each with full
multiplicity one. If m_j≥1 is the full multiplicity of F at the j-th
removed common zero, the actual accounting is

\[
 N_F^{\rm mult}\ge q-p+\sum_{j=1}^{k}m_j\ge q-p+k,
 \qquad N_G=q+k.
\]

All common endpoints contribute their full m_j, and no such zero
was counted in an open gap. Subtraction gives a deficit at most p,
and p≤k+1 proves precisely (1). This includes q=0, k=0 and pieces
with a single G zero. For X=H, the distinct G count is at most one,
so the separately stated trivial bound applies regardless of endpoint
coincidence or F multiplicity. In the dependent case F=cG with c≠0;
strict L(G)>0 makes all shared zeros simple, so both counts agree
exactly. The independent-case W argument is not used in that case.

All load-bearing cases pass. No change of hypotheses, proof correction,
new theorem, numerical certificate or actual-family application results
from this audit. The argument needs neither a common ODE nor deflation.
L371/L373's failures without common-zero accounting remain intact, as
do the independent missing actual discriminant and common-zero premises.
The completed review does not certify historical novelty or advance an
RH sign or zero-exclusion range.

## Mathlib

Full matching theorem: **not checked**. No Mathlib theorem is imported.
Supporting analytic identity, finite-order zero, connected-sign and
intermediate value results have not been checked in Mathlib; unknown
coverage is not evidence of absence.
