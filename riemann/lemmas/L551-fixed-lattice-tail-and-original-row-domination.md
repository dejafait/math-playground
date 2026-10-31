# L551 — Fixed-lattice tail and original-row domination

## Hypotheses

Embed O=Z[omega] in C, with omega=exp(2 pi i/3), and put
q_mu=|mu|^2. Fix an Eisenstein prime lambda above 3, so
|lambda|=sqrt(3). Let Lambda be either O or lambda^(-4)O. In the
respective cases put delta=1 or delta=1/9. Exclude mu=0 throughout.
Let A>1, a>0, U>=1, and let K:(0,infinity)->C satisfy

\[
 |K(x)|\le C_A x^{-A}\quad(x\ge1),\qquad C_A\ge0.       \tag{1}
\]

No smoothness or measurability of K is needed for this discrete claim.
For the Vsharp specialization use precisely L549's test class,
normalization and seminorm M_(A,B); all orders are fixed and finite.

For the conditional original-sum application fix Z>=2, tau_ref>0,
and C_ker>=1. The finite nonfrequency index set J consists of the
original rows, active tuples and reflection/local branches under
consideration. It does not enumerate the infinitely many dual indices
or their dyads. Each j has an original row r(j), branch denominator
c_j!=0, scale a_j=X/q_(c_j)^2>0 independent of mu, and coefficient
b_j(mu). Assume there are nonnegative weights w_j such that

\[
 |b_j(\mu)|\le w_j,\qquad
 \sum_{j\in J}w_j(1+a_j^{-1})\le C_{\rm raw}Z^{B_{\rm tail}}.
                                                               \tag{2}
\]

Here B_tail>=0, C_raw and the index/weight bounds are fixed before
choosing A or any Fourier order. This is the retained raw coefficient
and nonfrequency-count contract of L541, stated as a positive total
bound, including ALL original rows. It is not proved in this lemma.
Any multiplicity from representatives or local splitting is included
in the weights/count in (2).

For each j let eta_(j,d)(mu) be the cutoff for a dual dyad d. Retain the
original source support and masks in b_j or eta. Assume bounded absolute
overlap, uniformly in j,mu:

\[
 \sum_d|\eta_{j,d}(\mu)|\le C_{\rm cut}.                \tag{3}
\]

For every nonzero term in dyad d assume the actual-annulus comparison

\[
 a_jq_\mu\ge C_{\rm ker}^{-1}Z^{E_{j,d}},\qquad
 E_{j,d}=v+3\ell_b+e_\lambda-T_d.                     \tag{4}
\]

These are original annuli, before Fourier inversion or row enlargement.
Call a whole dyad discarded when E_(j,d)>tau_ref. Assume

\[
 \log Z\ge 2\log C_{\rm ker}/\tau_{\rm ref}.           \tag{5}
\]

The common kernel is Vsharp for one V in L549's class. Set
b_A=ceil(4A)+2 and Q_A(V)=M_(A,b_A)(V). A moving family of tests
requires a separate bound on these displayed seminorms.

## Conclusion

The complete fixed-lattice tail is absolutely summable, and

\[
 \begin{split}
 \sum_{\substack{0\ne\mu\in\Lambda\\a q_\mu>U}}|K(aq_\mu)|
 &\le C_A\left\{
  \frac{2U^{-A}}{1-2^{-A}}+
  \frac{16\delta^{-2}a^{-1}U^{1-A}}{1-2^{1-A}}\right\}\\
 &\ll_A C_A(1+a^{-1})U^{1-A}.                         \tag{6}
 \end{split}
\]

Constants are uniform in a>0 and U>=1 and for the two stated fixed
lattices, including subunit radii. For K=Vsharp, replace C_A in this
bound by C_(A,0)Q_A(V), where C_(A,0) is the constant in L549 (2).

Under (2)–(5), form the original discarded linear row vector

\[
 T(r)=\sum_{j:r(j)=r}\sum_{0\ne\mu\in\lambda^{-4}O}
       b_j(\mu)\sum_{d:E_{j,d}>\tau_{\rm ref}}
                  \eta_{j,d}(\mu)V^\sharp(a_jq_\mu).          \tag{7}
\]

All these sums are absolutely convergent, including the sum over
cutoffs in absolute value. They satisfy

\[
 \|T\|_{\ell^2}\le\|T\|_{\ell^1}
 \le C_{A,\rm raw,cut}\,Q_A(V)
       Z^{B_{\rm tail}+(\tau_{\rm ref}/2)(1-A)}.       \tag{8}
\]

For any desired linear-norm saving D_tail>0, choose, AFTER B_tail,

\[
 A>1+\frac{2(B_{\rm tail}+D_{\rm tail})}{\tau_{\rm ref}}.
                                                               \tag{9}
\]

Then (8) is O(Q_A(V)Z^(-D_tail)); its squared row energy is
O(Q_A(V)^2 Z^(-2D_tail)). Under V(x)->x^(iu_0)V(x), the displayed
linear bound has the further factor (1+|u_0|)^b_A by L549 (5),
and the energy bound has its square. Orders/constants may depend on
the requested saving; B_tail and the scale threshold (5) do not.
No height-uniform decay is asserted when this explicit test cost grows.

This discharges the imported lattice-tail primitive in L541 (12),
conditional on that lemma's raw arithmetic contract. It does not prove
that contract, marked expansion, a moving-lattice estimate, global
closure or any Xi sign. It does not assert the bound at A=1 or U<1.

## Proof

### Precise source and purpose of reproduction

OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
Re(s)>7/8*, 30 September 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[pinned build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
Lemma `lem:lattice-kernel-tail`, lines 2460–2477, states and proves
this lattice estimate. Its discarded-dyad use follows
`eq:reflection-actual-annuli`, lines 7377–7443. Source support and
all three local-column cases are in `prop:completed-reflection`,
lines 1633–1685. The pre-existing SPECIALIZE assessment covers exactly
this reproduction audit. A citation states the known estimate; it
does not independently verify the retained primitive. The proof below
checks its small-scale count, summation and conditional original-norm
application. No stronger conclusion or novelty is claimed.

### Disk count at every radius

For m,n in Z, the squared modulus of m+n omega is m^2-mn+n^2.
For a nonzero element this is a positive integer, since
m^2-mn+n^2=(m-n/2)^2+3n^2/4. Thus distinct O-points have distance
at least 1. Multiplication by lambda^(-4) has modulus 1/9, so distinct
points in the second lattice have distance at least delta=1/9.

For R>=0, put N_Lambda(R)=#{mu in Lambda:|mu|^2<=R}, including
zero. Around each such point place an open disk of radius delta/2.
Their interiors are disjoint and they lie in the disk of radius
sqrt(R)+delta/2. For any finite collection, comparison of areas gives

\[
 N_{\rm finite}\le(1+2\sqrt R/\delta)^2
                \le 2+8R/\delta^2.                         \tag{10}
\]

The second inequality follows from (s+t)^2<=2s^2+2t^2.
If there were more points than the right side, a finite subcollection
would contradict this bound. Thus the disk is finite and (10) bounds
N_Lambda(R) itself. This argument is valid below unit radius too.
In particular no nonzero point exists when R<delta^2; no large-radius
asymptotic or ideal-count theorem has been used.

### Both geometric series and the strict cutoff

The disjoint shells 2^j U<a q_mu<=2^(j+1)U, j=0,1,..., partition
exactly the strict tail a q_mu>U. An endpoint at an upper shell bound
belongs to that shell and not the next. By (10) the number in shell j
is at most 2+16 delta^(-2)2^j U/a. Since its arguments are greater
than or equal to 1, (1) bounds its absolute contribution by

\[
 C_A\{2+16\delta^{-2}2^jU/a\}(2^jU)^{-A}.             \tag{11}
\]

Summing positive bounds gives (6): the two series have ratios 2^(-A)
and 2^(1-A), strictly less than 1 because A>1. Their finite sums bound
every finite tail subcollection, proving absolute convergence as well
as the estimate. Since U>=1, U^(-A)<=U^(1-A), which yields the final
form in (6). The dependence on delta is bounded for these two fixed
lattices. No uniformity for other lattices is inferred.

L549 (2), at j=0 and x>=1, gives
|Vsharp(x)|<=C_(A,0) Q_A(V)(1+x)^(-A)
<=C_(A,0)Q_A(V)x^(-A). This establishes the asserted specialization.
Its seminorm is finite by L549 (4); it need not be bounded uniformly
in a family of V without an additional hypothesis.

### Original support and absolute domination

On any discarded dyad, (4), E_(j,d)>tau_ref and (5) imply

\[
 a_jq_\mu\ge C_{\rm ker}^{-1}Z^{E_{j,d}}
       > C_{\rm ker}^{-1}Z^{\tau_{\rm ref}}
       \ge Z^{\tau_{\rm ref}/2}=:U.                  \tag{12}
\]

The strict inequality uses Z>1. The last inequality is exactly (5),
and U>=1. This is a containment of the union of actual discarded
supports in a full lattice tail for each original j. It does not
claim a cutoff comparison on shorter added rows. In L541 the exact
identity (10) and compact normalized annuli give (4), uniformly in
all dual dyad centers; q_(c_F)^(-2) is absorbed into fixed C_ker.
The exact ramified norm is already included in e_lambda. Thus
h>=-4 and unbounded positive h cause no extra count here.

For clarity, the retained source bound also controls small ramified
indices. In its representation mu=u lambda^h n b^3, with n,b primary
and n squarefree, its coefficient bound is
|d(mu)|<=27 q_lambda^(h/6) q_b^(1/2). Norm multiplicativity, including
when n and b share primes, therefore gives

\[
 \frac{|d(\mu)|}{\sqrt{q_\mu}}
 \le27q_\lambda^{-h/3}q_n^{-1/2}q_b^{-1}
 \le27q_\lambda^{4/3},\qquad h\ge-4.                 \tag{13}
\]

This uses q_n,q_b>=1 and is conditional on the cited coefficient
bound, not a proof of it. Character and additive phases have modulus
at most one, with their original zero values retained. Of the local
columns, the generic character has modulus at most one, the active
exponent-zero column at most q_p^(-1/2), and
q_p^(-1/2)(-1+q_p 1_(p|x)) at most q_p^(1/2).
If this last column is split, the sum of absolute coefficients is
q_p^(-1/2)+q_p^(1/2)<=2q_p^(1/2). Such split/marked factors and
branch multiplicities belong to the raw weights/count in (2).
They have not been bounded anew by a retained dual length.

All source indices lie in lambda^(-4)O. Enlarging their set to the
full nonzero lattice in a positive bound includes the permitted S
primes and all shared n/b or N_F/b primes. It introduces no new
coprimality restriction. Masks and zeros can only reduce this bound;
no symbol is divided at a zero. If extraction has introduced repeated
representatives, their multiplicity must already be included in (2)
or the absolute overlap (3). A per-row version of (2) alone would not
justify the total bound claimed here.

For any finite collection of j,mu,d appearing in (7), triangle
inequality, (3) and (12) give the upper bound

\[
 C_{\rm cut}\sum_{j\in J}w_j
     \sum_{\substack{0\ne\mu\in\lambda^{-4}O\\a_jq_\mu>U}}
                          |V^\sharp(a_jq_\mu)|.              \tag{14}
\]

Bound (6) and then (2) make this at most the right side of (8).
This positive bound is independent of the finite collection. Taking
the supremum over such collections proves absolute summability and
justifies regrouping into the row vector (7). Bounded overlap has
been used pointwise in mu; infinitely many dyads have not been
charged as a finite collection of retained-length blocks.

For finitely many original rows,
(sum_r |T(r)|^2)^(1/2)<=sum_r |T(r)|, since the square of the
right side is the sum of squares plus nonnegative cross terms.
A further triangle inequality bounds that l1 norm by the absolute
total just established. This proves (8) without a new square-root
row-count factor or a common-density assumption for the discarded
terms. Row enlargement and Fourier absolutization have not occurred.

Finally substitute U=Z^(tau_ref/2). Its exponent is exactly
B_tail+(tau_ref/2)(1-A), strictly less than -D_tail under (9).
The constants depend on the chosen fixed A but not on Z or a_j;
the raw exponent was chosen first. L549 (5) supplies the stated pure
twist cost with order b_A, and squaring the norm bound squares that
cost and Q_A(V). If test norms or twist heights vary with Z, those
factors remain in the estimate; arbitrary uniform negative powers
cannot be inferred without controlling them. This completes only
the specified conditional tail interface.

## Mathlib

Full matching coverage has not been checked. The proof uses elementary
Euclidean disk packing, the positive Eisenstein norm, geometric-series
summation, and the explicit analytic input L549. No Mathlib theorem is
imported as a full certificate for (6) or the original-row application.
Unknown formal availability is not evidence of absence.
