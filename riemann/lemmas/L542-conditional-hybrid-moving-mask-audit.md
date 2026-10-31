# L542 — Conditional hybrid moving-mask audit

## Hypotheses

Work with nonzero ideals of O=Z[omega], their norms q_x, and the pinned
source's primary representatives. Fix a finite prime set S containing
lambda above 3. A good ideal avoids S. The zero-extended sextic symbols
are multiplicative in numerator and denominator; on coprime arguments
they have sixth power one. Negative symbol powers mean the corresponding
power on units, extended by zero at collisions, never division by zero.
Retain the source's identification of chi_P(j)^(-2) with a cubic symbol
and its reciprocity/conjugation orientation on primary ideals.
In the source setting where S contains every prime above 6, that
identification is discharged below by L548 (A2) and L545: it is not
an additional premise there. In that setting use the source Euler
definition chi_p(x) congruent to x^((q_p-1)/6) modulo p on units,
with chi_p(x)=0 at p|x, for each good prime p. The wider domain with
only lambda in S remains conditional on the original identification and sextic-symbol
conventions; no sextic character at the prime above 2 is supplied here.

Fix K,N,B,L>=1 and fixed support-comparison constants. Rows k and tuple
indices P are squarefree good primary ideals with q_k<=A_k K and
q_P asymp L. Source indices n are squarefree primary ideals with
q_n asymp N; b are arbitrary primary ideals with q_b asymp B. Source
ideals can have S-primes other than lambda, and n,b can share primes.
Let |a(P)|<=1 and |beta(n,b)|<=1. Their supports are fixed independently
of the other moving indices: a is independent of k,n,b and beta of k,P.
Fixed row restrictions, fixed P restrictions, fixed (n,b) restrictions
and fixed ray sectors are allowed only with these independences.

Use the following two estimates, with uniform constants for this
fixed S and fixed comparison constants. Estimate (1) remains a
**conditional input** of this audit. Estimate (2) is now imported
by L545 under the primary conventions and symbol identification above.

1. The weighted statement of `lem:completed-quadratic-reduction`,
   `eq:completed-quadratic-reduction`. For arbitrary complex row-independent
   coefficients gamma(n,b), put b=gt^2, c=(n,g), n=cm, g=ch. Here
   c,m,h are squarefree and pairwise coprime; g,t need not be coprime.
   In a block q_c asymp C, q_g asymp G, q_t asymp T, B asymp GT^2,
   and for squarefree good rows of length U, its squared norm is at most

   \[
   (UNB)^\delta T\sum_{q_t\asymp T}
   \sum_{\substack{r\ {\rm sf,good}\\q_r\ll\min(U,C)}}
   \left(\frac U{q_r}+\frac{NG}{C^2}\right)\frac C{q_r}
   \sum_{(c',m,h)\in\mathcal D_r(t)}
       |\gamma(rc'm,rc'ht^2)|^2.                         \tag{1}
   \]

   D_r(t) reconstructs precisely the original support and block with
   c=rc'. In particular c' keeps its S-part and m,h are the original
   ideals. This estimate already handles the row-t restriction and
   the full row-c divisor expansion. No row-c' mask remains. It admits
   bounded row scalars and fixed row sectors, and holds for every
   delta>0. Empty supports vanish and bounded supports include units.
2. The source's displayed `eq:cubic-large-sieve`, supplied by L545:
   for arbitrary complex
   coefficients z_v on squarefree primary ideals, squarefree primary
   rows u of norm <=U and columns v of norm <=V,

   \[
   \sum_u\left|\sum_v z_v(v/u)_3\right|^2
   \ll_\delta (UV)^\delta
       \{U+V+(UV)^{2/3}\}\sum_v|z_v|^2.                 \tag{2}
   \]

   Retain its stated conjugation/reciprocity orientation. Both stars
   mean ideal squarefreeness. There is no additional S-exclusion or
   rational-norm-squarefreeness restriction on its rows or columns.
   Fixed coefficient support is implemented by zero extension.

Also retain ideal counting # {x:q_x<=Y}=O(Y) for Y>=1 and divisor
bounds d_O(x)=O_delta(q_x^delta). Constants below may depend on S,
the fixed support constants and the requested epsilon. All sums are
finite. No primitive estimate is inferred from L541 or a downstream
application.

## Conclusion

For every epsilon>0, the hybrid norm

\[
\mathcal H=\sum_k\left|
 \sum_P\frac{a(P)}{\sqrt{q_P}}1_{(P,k)=1}
 \sum_{n,b}\beta(n,b)\chi_k(nb)^3
                  \chi_P(n)^{-2}1_{(P,b)=1}\right|^2
\]

satisfies

\[
\mathcal H\ll_\epsilon (KNBL)^\epsilon
      (K+NB)B\{N+L+(NL)^{2/3}\}.                       \tag{3}
\]

Thus both moving masks are handled under (1) and (2), with the original
source primes and shared factors retained. This reproduces the pinned
source's `lem:hybrid-energy`, `old-eq:4.6b`. It reduces the norm contract
in L541 Hypothesis 2 to these primitives. It does not establish the
quadratic primitive estimate, structural reflection, global external
closure or actual-Xi signs. L545 supplies the cubic primitive by
citation and application, with no improvement beyond the source claim.
For S containing all primes above 6, its symbol interface is now also
verified; no reciprocity premise is needed for that interface.

## Proof

Primary citation: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, 30 September 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[pinned build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
The exact locators are `lem:completed-quadratic-reduction` and
`eq:completed-quadratic-reduction` (2518–2566, essential support cases
2567–2626); `eq:cubic-large-sieve` (7036–7053); and `lem:hybrid-energy`,
`eq:hybrid-mark-mask-reduction`, `eq:hybrid-after-quadratic-reduction`,
`old-eq:4.6c` (7054–7194). The source attributes (2) to Heath-Brown,
*Kummer's conjecture for cubic Gauss sums*, Israel J. Math. 120A (2000),
97–124, Theorem 2. L545 now records the original theorem's precise
manuscript citation and ideal-indexed application, including units,
collision zeros and complex transpose/conjugation. Its analytic proof
is imported, not independently audited. For the source domain, the
finite symbol identification is verified in the next subsection.
Reproof of this particular conditional implication is justified by the
need to test the two coefficient interfaces and reduce L541's contract;
importing its conclusion would bypass that test. Existing literature
comparison is reused; no novelty is claimed.

Write Q=KNBL. At intermediate stages Q^{O(delta)} denotes finitely many
adjustable small losses, with an absolute finite multiplier independent
of all lengths. We choose delta only after specifying the final epsilon.

### Cubic-symbol interface in the source domain

Assume in this subsection that S contains all primes above 6. Use only
L548's finite definitions (A1) and Euler comparison (A2), including
its all-residue and unit conventions. Their proof requires good prime
denominators, the Euler definitions and multiplicativity, not the
theta, Gauss-norm or Mellin-reflection hypotheses of that lemma.
The ordinary cubic convention is Dunn–Radziwill, *Bias in cubic Gauss
sums: Patterson's conjecture*, arXiv:2109.07463v3 (14 May 2024),
[Section 1.2 through (1.4)](https://arxiv.org/html/2109.07463v3#S1.SS2).
No new reciprocity identity or sieve estimate is being proved.

Let P' be any squarefree good primary ideal and j any squarefree
primary ideal prime to lambda. Write their unique primary generators
when evaluating symbols, exactly as in L545. For each prime p|P',
L548 (A2) identifies chi_p(j)^2=(j/p)_3 on every residue class.
It imposes no coprimality of j with S: primes of S in j are allowed
because no prime of S divides P'. Multiplication over p|P' gives
chi_(P')(j)^2=(j/P')_3, with both sides zero whenever (j,P')!=1.
Thus, with the stated zero extension of negative powers,

\[
 M_{j,P'}:=\chi_{P'}(j)^{-2}
      =\overline{(j/P')_3}.                              \tag{I}
\]

On a coprime pair this is inversion of the cube root chi_(P')(j)^2;
on a colliding pair both entries in (I) are zero, not reciprocals of
zero. The empty-product convention gives M_(j,1)=1 for every j,
and M_(1,P')=1 for every P', including M_(1,1)=1.
No residue-degree or rational-norm-squarefreeness restriction is added.

For U,V>=1 take the full L545 matrix B with rows P' of norm <=V
and columns j of norm <=U, both squarefree and prime to lambda,
and entries B_(P',j)=(j/P')_3. Initially B includes all such P',
not only the good ones. L545, importing Heath-Brown's Theorem 2
(author manuscript pp. 3–4, cited above), bounds its squared
operator norm by

\[
 C_\delta(UV)^\delta\{U+V+(UV)^{2/3}\}.
\]

By (I), the matrix needed here, with rows j and good columns P',
is B* restricted to those columns. L545's finite complex duality
gives exactly the same bound for B*, with the row/column lengths
exchanged and the symmetric charge unchanged. A vector z on the
good columns is extended by zero to every other P'; its squared norm
is unchanged. Restricting the final positive j sum is also permitted.
Consequently, for arbitrary such z independent of j,

\[
 \sum_{\substack{j\ {\rm sf},\ (j,\lambda)=1\\q_j\le U}}
   \left|\sum_{\substack{P'\ {\rm sf,good}\\q_{P'}\le V}}
                 z_{P'}\chi_{P'}(j)^{-2}\right|^2
 \ll_\delta(UV)^\delta\{U+V+(UV)^{2/3}\}
                       \sum_{P'}|z_{P'}|^2.              \tag{II}
\]

This is an adjoint application, not an assertion that transpose equals
adjoint, nor an appeal to arbitrary two-index phase invariance.
There is no remaining phase in (I). In the later use (7), h,t,D,r
are frozen before z is defined. Its factors a_D(P'), chi_(P')(r)^(-2),
1_((P',ht)=1) and q_(P')^(-1/2) depend only on P' and those frozen
data. The zero at a collision with r and the fixed ht mask remain in
z; neither creates a j-dependent coefficient. The row j=c'm=n/r
is squarefree and prime to lambda, retaining its permitted S-part.
Thus (II) applies to precisely that vector with exactly the mass in
(7), giving (8) without an extra length charge. Unit and empty
supports are covered above; subunit quotient centers are treated in
the existing final subsection. This discharges only the retained
cubic-symbol interface in the stated source domain.

### Full row-mark expansion

The finite Mobius identity is
\(1_{(P,k)=1}=\sum_{D\mid(P,k)}\mu(D)\). For each row, Cauchy over divisors
D|k costs at most d_O(k). After summing the positive row norms, put
k=Dk', P=DP'. Both D and the quotients are squarefree good, with fixed
restrictions (D,k')=(D,P')=1. Define

\[
 a_D(P')=a(DP')1_{(D,P')=1},\qquad
 \beta_D(n,b)=\beta(n,b)\chi_D(nb)^3
                    \chi_D(n)^{-2}1_{(D,b)=1}.
\]

The first coefficient depends only on P',D; the second only on n,b,D.
Both are bounded by one, including at collisions. Multiplicativity,
including zeros, and q_P^(-1/2)=q_D^(-1/2)q_(P')^(-1/2) give

\[
\mathcal H\ll Q^{O(\delta)}\sum_D q_D^{-1}
 \sum_{k'}\left|\sum_{n,b}\beta_D(n,b)\chi_{k'}(nb)^3
       F_D(n,b)\right|^2,                              \tag{4}
\]

where

\[
 F_D(n,b)=\sum_{P'}\frac{a_D(P')}{\sqrt{q_{P'}}}
               \chi_{P'}(n)^{-2}1_{(P',b)=1}.
\]

All original support conditions are still present. Here q_k'<<K/q_D,
q_P' asymp L/q_D, q_D<<min(K,L). Crucially no (P',k') condition
belongs in an individual summand: the complete divisor expansion
already represents that cancellation before Cauchy. The fixed original
row support becomes a fixed support for k' once D is fixed.

### Weighted quadratic interface and the second mask

For fixed D, gamma=beta_D F_D is arbitrary complex and independent of
k'. This is exactly the coefficient class of (1), even though F_D need
not be bounded. Partition c,g,t into dyads as in (1). There are at most
a fixed power of log(2+Q) such blocks, because c|n,g and g,t^2|b.
Cauchy over blocks costs another adjustable small power. For one block,
(4) is bounded by the sum of

\[
 Q^{O(\delta)}\sum_D\frac1{q_D}T\sum_{q_t\asymp T}
 \sum_{\substack{r\ {\rm sf,good}\\q_r\ll\min(K/q_D,C)}}
 \left(\frac K{q_Dq_r}+\frac{NG}{C^2}\right)\frac C{q_r}
 \sum_{\mathcal D_r(t)}|\beta_D(rc'm,rc'ht^2)|^2
                   |F_D(rc'm,rc'ht^2)|^2.              \tag{5}
\]

The fixed restrictions on k' and its ray class are permitted in (1).
Its internal S-part separation has not changed the original m,h,c'.
In particular it adds no (g,t)=1 requirement.

For every P', including collisions, the character factor in F_D equals

\[
 \chi_{P'}(rc'm)^{-2}1_{(P',rc'ht^2)=1}
 =\chi_{P'}(r)^{-2}\chi_{P'}(c'm)^{-2}1_{(P',ht)=1}.
                                                               \tag{6}
\]

To verify (6), a collision with r or c'm makes both sides zero. Without
such a collision, the remaining coprimality condition is exactly that
with ht, because t and t^2 have the same prime support. Multiplicativity
then gives equality. This covers intersections of t with g or n as well.
Thus a_(D,r)(P')=a_D(P')chi_(P')(r)^(-2) is a tuple-only bounded
coefficient, with its zero at (P',r)>1 preserved.

Only now discard |beta_D|^2<=1 in the positive sum (5). Fix h,t,D,r.
Its remaining polynomial depends on c',m solely through j=c'm=n/r.
The ideal j is squarefree primary, q_j<<N/q_r, and retains all original
allowed S-primes. For any j the number of pairs (c',m) is at most
d_O(j). All the original constraints on c',m can therefore be bounded
by this multiplicity in a positive sum. Enlarge that positive j sum
to all squarefree primary ideals in its norm bound.

The coefficients in this cubic sieve are

\[
 z_{P'}=\frac{a_{D,r}(P')1_{(P',ht)=1}}{\sqrt{q_{P'}}},
 \qquad \sum_{P'}|z_{P'}|^2\ll1.                       \tag{7}
\]

For (7), ideal counting bounds the number of P' in an annulus of
center V=L/q_D by O(V), and each inverse norm there is O(1/V),
with the bounded-range interpretation proved below. Restrictions
only decrease this coefficient mass. The ht mask is fixed after h,t
are fixed, hence z_(P') is independent of the cubic row j. In the
source domain apply (II); in the wider conditional setting apply (2)
with its retained identification. Take U a fixed multiple of N/q_r and
V a fixed multiple of L/q_D. Put A(x,y)=x+y+(xy)^(2/3).
The positive sum over c',m is consequently

\[
 \ll Q^{O(\delta)} A(N/q_r,L/q_D).                    \tag{8}
\]

No modulus-monotonicity for column sums was used; fixed supports were
encoded in z and only the positive row sum was enlarged. Counting h
with q_h asymp G/C gives O(G/C) possibilities, including the original
S-parts. It is legitimate to sum (8) over h after taking its uniform
bound: each h has its own fixed coefficient vector satisfying (7).

### Exact charges and final sum

Fix dyads q_D asymp d and q_r asymp s. Counting t gives O(T), in
addition to the factor T in (5). The factors for t,c',h combine as

\[
 T^2\frac C{s}\frac G{C}\asymp\frac B{s}.            \tag{9}
\]

There are O(s) ideals r in that dyad. The inverse-norm sum of D over
its dyad is O(1). Thus (5), (8), and (9) give, for each set of blocks,

\[
 \ll Q^{O(\delta)} B
       \left(\frac K{ds}+\frac{NG}{C^2}\right)
       A(N/s,L/d).                                    \tag{10}
\]

Use dyadic centers d,s>=1 for actual integral ideals. Hence
K/(ds)<=K and A(N/s,L/d)<=A(N,L). Also C,T are bounded below on
nonempty blocks and G<<B from B asymp GT^2, so NG/C^2<<NB.
All these inequalities allow fixed comparison constants. Summing the
logarithmically many blocks in C,G,T,d,s and absorbing divisor losses
gives (3): choose delta small enough that their finite combined exponent
and the logarithmic costs are <=epsilon. No lost L, N, D or r power
is hidden in this choice.

### Empty and bounded quotient cases

All dyadic centers for actual ideals c,g,t,D,r can be chosen >=1,
with a unit block. Quotient centers K/q_D, L/q_D, N/q_r, C/q_r and
G/C need not be >=1. On any original nonempty range each is bounded
below by a fixed positive constant: the corresponding actual ideal
has norm at least one and norm at most a fixed multiple of that center.
The same holds for K/(q_D q_r) when the inner row range is nonempty.
If that row range is empty, the contribution before applying a sieve
is zero and may be omitted.

For (1) or (2) replace a positive quotient center x by max(1,x) when
necessary; on these nonempty ranges max(1,x)<=C_* x with a constant
depending only on the fixed comparisons. Both the linear sieve terms
and their 2/3 powers therefore change by fixed factors. Similarly
O(max(1,x))=O(x) justifies the h and c' counts on nonempty ranges and
the inverse-norm bound (7). Constants do not depend on D,r,h,t.

In particular, a merely subunit center is not sufficient to declare a
range empty: its upper comparison constant may still admit the unit.
Only a range whose actual upper norm bound is below one is necessarily
empty. The source's sentence at 7191 about subunit ranges is interpreted
with this support qualification, rather than used literally. Bounded
nonempty cases satisfy the same estimates, so this wording issue does
not change (3). Every step is finite; no limiting interchange or
RH-equivalent positivity has been invoked.

## Mathlib

Full matching coverage was not checked. In particular this audit does
not assert formal availability of either retained Eisenstein sieve,
the source symbol conventions, or this two-mask implication. Generic
finite Cauchy inequalities alone do not establish the arithmetic inputs.
Coverage of the finite identification (I) and its adjoint application
(II) was not checked; no matching Mathlib theorem is claimed.
