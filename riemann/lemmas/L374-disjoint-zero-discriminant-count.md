# Lemma 374: disjoint zeros turn weak discriminant control into a count bound

## Hypotheses

Let H be real and let F,G be real analytic on an open neighborhood of
[H,infinity). Neither function is identically zero on the connected
component containing this ray. For ordinary real derivatives put

\[
 \mathscr L(U)=U'^2-UU'',\qquad
 B(U,V)=2U'V'-UV''-U''V,
 \qquad D=B(F,G)^2-4\mathscr L(F)\mathscr L(G).
\]

At every t≥H assume F(t),G(t) are not both zero, D(t)≤0, and
\(\mathscr L(G)(t)>0\). No common differential equation, nonvanishing
Wronskian, or simplicity assumption is made.

## Conclusion

For every X≥H, with full analytic multiplicities for F and distinct
zeros for G and with both endpoints included,

\[
 N_F^{\rm mult}([H,X])\ge N_G([H,X])-1.                 \tag{1}
\]

If F,G are linearly independent over the real constants, their Wronskian
W=FG'−F'G never vanishes on the ray, both real zero sets there are simple,
and each open interval between consecutive G zeros contains an F zero.
If they are dependent, both zero sets on the ray are empty. Thus (1)
also holds with distinct F zeros. This proves the approved restricted
implication with the universal choice C=1, stronger than a pair-dependent
finite C. It does not prove any premise for the actual F_0,G pair, any
actual-theta sign, or RH. The separate critical audit below retains this
conditional theorem; no stronger conclusion is claimed.

## Proof

The prior EXPLORE assessment is
`drafts/literature/2026-10-07-disjoint-zero-multiplicity-count.md`.
It and the parent assessment screen the relevant separation and pencil
results. For example, MIT 18.034 Spring 2009,
[Lecture 9, Theorem 9.1, printed pp. 1–2](https://ocw.mit.edu/courses/18-034-honors-differential-equations-spring-2009/0cdeb657491010f0f8c60aa49f2d5248_MIT18_034s09_lec09.pdf),
assumes independent solutions of one regular homogeneous second-order
equation. That is a comparison, not a theorem imported here. We prove
the missing Wronskian assertion directly from the present weaker
hypotheses, then give the elementary interval argument in full.
L371 and L373 are obstruction context only: their pairs have common
zeros, explicitly excluded here. No mathematical conclusion from those
lemmas or from actual-family estimates is an input to this proof.

**The quadratic form on the real pencil.** At each t≥H, for real a,b,
direct expansion and completion of the square give

\[
\begin{aligned}
 \mathscr L(aF+bG)
 &=a^2\mathscr L(F)+abB(F,G)+b^2\mathscr L(G)\\
 &=\mathscr L(G)\left(b+\frac{aB(F,G)}{2\mathscr L(G)}\right)^2
       +a^2\frac{-D}{4\mathscr L(G)}\ge0.             \tag{2}
\end{aligned}
\]

Consequently, for any two fixed real linear combinations U,V of F,G,

\[
 \mathscr L(U)\ge0,\quad \mathscr L(V)\ge0,\quad
 B(U,V)^2\le4\mathscr L(U)\mathscr L(V).              \tag{3}
\]

Indeed, \(\mathscr L(U+sV)\) is nonnegative for all real s.
If \(\mathscr L(V)>0\), its discriminant is nonpositive; if
\(\mathscr L(V)=0\), its linear coefficient B(U,V) must vanish.
This includes every semidefinite degeneracy. The argument is pointwise;
U,V have constant coefficients, and no variable coefficient is
differentiated in (2) or (3).

**A pencil member cannot have a finite multiple zero beside a nonzero
member.** Suppose at t0≥H that V(t0)=v≠0 and that U has finite zero
order m≥2. Put x=t−t0 and write
U(t)=a x^m+O(x^(m+1)), a≠0. Analytic Taylor expansions, including their
differentiated forms, give

\[
\begin{aligned}
 \mathscr L(U)(t)&=m a^2x^{2m-2}+O(x^{2m-1}),\\
 B(U,V)(t)&=-m(m-1)av x^{m-2}+O(x^{m-1}),\\
 \mathscr L(V)(t)&=O(1).                              \tag{4}
\end{aligned}
\]

The leading coefficient in the second line comes from −U''V; the
terms 2U'V' and −UV'' have orders at least m−1 and m. Dividing (3)
by x^(2m−4) for x>0 sufficiently small would give, as x decreases to
zero, the impossible inequality

\[
 m^2(m-1)^2 a^2v^2\le0,
\]

since its right side is O(x²). This treats m=2 as well as every higher
finite order. Using x>0 only makes the argument valid at t0=H without
assuming either differential inequality to the left of H.

**Dependence and Wronskian cases.** Restrict the analytic domain to the
connected open interval containing the ray. If F,G are dependent, their
individual nonzero assumptions imply F=cG with a nonzero real constant
c. A zero of either would then be common, contrary to the hypothesis.
Both counts vanish and (1) follows.

Now assume they are independent. Suppose W(t0)=0 at some t0≥H.
If G(t0)≠0, take
U=F−(F(t0)/G(t0))G and V=G. Then U(t0)=0 and
U'(t0)=−W(t0)/G(t0)=0, while V(t0)≠0.
Independence ensures U is not identically zero on the interval. By
real analyticity and the identity theorem its zero at t0 therefore has
finite order at least two, contradicting (4).
If G(t0)=0, disjointness gives F(t0)≠0 and
W(t0)=F(t0)G'(t0). Hence G'(t0)=0. Taking U=G,V=F yields the same
contradiction. These exhaust the possibilities, so W never vanishes.
Continuity and connectedness give it one fixed sign on the entire ray.
At an F zero, W=−F'G≠0, so F'≠0; at a G zero, W=FG'≠0, so G'≠0.
Thus every F and G zero on the ray has full analytic multiplicity one.
In particular no infinite-order or multiple-zero case has been omitted.

**Closed-endpoint counting.** Fix X≥H. Both zero sets in [H,X] are
finite: an infinite set would have an accumulation point in this compact
interval, and analyticity on an open neighborhood and the identity
theorem would contradict the nonzero assumption. Let the G zeros there
be t1<...<tk. If k≤1, nonnegativity of the F count gives (1), including
X=H. If k≥2, G has constant nonzero sign on each (ti,t(i+1)) and has
simple zeros at its endpoints. Its Taylor expansions on the interior
sides show that G'(ti) and G'(t(i+1)) have opposite signs. At those
endpoints W=FG'; since W has one fixed nonzero sign, F(ti) and
F(t(i+1)) also have opposite signs. The intermediate value theorem
therefore places an F zero in each open interval (ti,t(i+1)).

These k−1 intervals are disjoint, so their F zeros are distinct and
each contributes its full multiplicity one. They lie strictly between
the counted G endpoints, even if t1=H or tk=X. Any additional F zeros,
including ones at H or X, only increase the left side of (1). Thus
N_F^mult([H,X])≥k−1 for every X≥H, as required. There is no endpoint
limit, asymptotic error, or finite onset adjustment. ∎

**Scope and verification.** The load-bearing step is the finite-order
contradiction (4); it derives Wronskian nonvanishing rather than assuming
a regular ODE. The constant C=1 does not depend on X, the pair, or H.
Only exact expansions and the identity and intermediate value theorems
are used; no numerical certificate or mathematical script is needed.
The original common-zero counterexamples remain valid. The actual-family
conditions D≤0 and eventual disjointness, and any signed arithmetic
comparison needed downstream, remain unproved. The result is local
progress under the assessed hypotheses; POTENTIALLY_NEW is only the
process classification of the bounded literature search, not a claim
of historical originality or progress beyond the sources checked.

**Separate critical audit, 2026-10-07.** The audit used the prior EXPLORE
coverage `drafts/literature/2026-10-07-disjoint-zero-count-audit.md`.
No source theorem replaces the physical-inequality argument. Rechecking
the complete proof gives the following findings.

At a fixed t the pencil matrix is
\(M=\left(\begin{smallmatrix}\mathscr L(F)&B/2\\B/2&\mathscr L(G)\end{smallmatrix}\right)\).
Its lower diagonal is positive and its Schur complement is
\(-D/(4\mathscr L(G))\ge0\), exactly the second coefficient in (2).
Thus it is positive semidefinite even when D=0 or L(F)=0. Applying
constant pencil coefficients to this same quadratic form yields (3),
without differentiating point-dependent coefficients. When L(V)=0,
the polynomial L(U+sV)=L(U)+sB(U,V) cannot be nonnegative for every
real s unless B(U,V)=0. When both diagonals vanish the same reasoning
applies. No strict determinant premise has slipped into (3).

For the local contradiction, the leading terms of U'^2 and UU'' are
respectively \(m^2a^2x^{2m-2}\) and
\(m(m-1)a^2x^{2m-2}\); their difference is the first line of (4).
With V=v+O(x), V' and V'' bounded, only −U''V has order m−2,
with the stated nonzero coefficient. Analyticity justifies differentiated
Taylor remainders of every order used. If m=2, already at t0 one has
L(U)=0 and B(U,V)=−2av≠0, contradicting (3) directly.
For m>2, (3) divided by x^(2m−4) has left limit
\(m^2(m-1)^2a^2v^2>0\) and right limit zero, since L(V) is bounded.
The right approach stays in the hypothesized ray even when t0=H.
Consequently neither a boundary zero nor semidegeneracy avoids the
contradiction.

The connected component of the real analytic domain containing the ray
is an open interval. If every derivative of a pencil member vanishes
at t0, its convergent Taylor series is zero on a neighborhood; the
identity theorem then makes it zero on that component. In the independent
case the chosen U cannot have this behavior. For G(t0)≠0 the derivative
of U=F−(F(t0)/G(t0))G is exactly −W(t0)/G(t0). For G(t0)=0,
disjointness gives F(t0)≠0, and W(t0)=0 forces G'(t0)=0.
Both cases therefore reduce to the verified finite-order contradiction.
Dependence is separate: neither function is identically zero, so the
proportionality constant is nonzero and disjointness excludes every zero.
The proof never asserts W≠0 in that dependent case.

Compact finiteness uses the open analytic neighborhood at both H and X;
an accumulation there cannot escape the identity theorem. In the
independent case W is continuous and never zero, so it has one sign
on the connected ray and both original zero sets are simple. For
consecutive counted G zeros a<b, the nonzero interior sign of G equals
sign G'(a) and −sign G'(b). Since F(a)G'(a) and F(b)G'(b)
have the same sign as W, F(a) and F(b) have opposite signs.
The resulting F zero lies in (a,b), with multiplicity one; the k−1
open gaps are disjoint and all lie in [H,X]. For k=0,1 the right side
of (1) is −1,0 respectively. At X=H there is at most one G zero,
so the same check applies. Closed-endpoint zeros cause no lost term.

All audited cases pass. No correction, strengthened bound, additional
lemma input or mathematical script is needed. This closes the previously
pending correctness review of the conditional C=1 input, without proving
the actual pair's missing premises or advancing beyond the source search's
limited originality assessment. The common-zero obstructions remain
excluded solely by the stated disjointness hypothesis.

## Mathlib

Full matching theorem: **not checked**. No Mathlib theorem is imported.
The proof uses elementary quadratic-form algebra, finite-order analytic
zeros, the real analytic identity theorem and the intermediate value
theorem. Supporting formal coverage has not been checked, and unknown
coverage is not evidence of absence.
