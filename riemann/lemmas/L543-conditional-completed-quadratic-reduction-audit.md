# L543 — Conditional completed quadratic reduction audit

## Hypotheses

Work with nonzero integral ideals of O=Z[omega], omega=exp(2pi i/3),
with norm q_x. Primary representatives are the unique generators
congruent to 1 modulo 3, so all ideals called primary avoid the prime
lambda above 3 and primary representatives multiply. Fix a finite set S
containing every prime above 6 and the supports of the fixed character
presentations and ray moduli. Good ideals avoid S. S and all support
comparison constants are fixed independently of the lengths and indices.

Retain the source's sextic symbol conventions. For good primary a,
chi_a(x) is multiplicative in a and x, including its zero at (a,x)>1;
its values on coprime arguments have sixth power one. Put
Q_a(x)=chi_a(x)^3. Then Q_a(xy)=Q_a(x)Q_a(y),
Q_(ab)(x)=Q_a(x)Q_b(x), and Q_a(x^2)=1_((a,x)=1).
In particular Q_1(x)=1. Numerators may contain S-primes other than lambda.

Assume the displayed base quadratic large sieve: for U,V>=1, every
delta>0, and arbitrary complex coefficients z_j on squarefree good
primary ideals with q_j<=V,

\[
 \sum_{\substack{a\ {\rm sf,good}\\q_a\le U}}
   \left|\sum_{\substack{j\ {\rm sf,good}\\q_j\le V}}
                  z_j Q_a(j)\right|^2
 \ll_{\delta,S}(UV)^\delta(U+V)\sum_j|z_j|^2.       \tag{1}
\]

This is the pinned source's `eq:quadratic-large-sieve`, retained as a
conditional input. Its independent Hecke-family specialization is not
proved here. Also retain the standard ideal estimates
#{x:q_x<=Y}=O(Y) for Y>=1 and d_O(x)<<_delta q_x^delta.

Fix K,N,B>=1. Let I be any fixed set of squarefree good primary rows k
with q_k<=A_k K. Let beta(n,b) be arbitrary complex coefficients,
independent of k, with n squarefree primary, q_n asymp N, b primary,
q_b asymp B. Fixed restrictions on this coefficient support are allowed.
No boundedness assumption on beta is made. Write uniquely

\[
 b=gt^2,\quad c=(n,g),\quad n=cm,\quad g=ch,
\]

where g is squarefree. Consequently c,m,h are pairwise coprime and
squarefree; g and t may share primes. Fix a single block
q_c asymp C, q_g asymp G, q_t asymp T, B asymp GT^2, with positive
C,G,T and fixed comparison constants. For squarefree good r and fixed t,
D_r(t) consists of precisely the triples (c',m,h) reconstructing the
original support and this block by

\[
 c=rc',\qquad n=rc'm,\qquad b=rc'ht^2,
\]

with c,m,h squarefree and pairwise coprime. In particular c' retains its
S-part. Let E be the sum over k in I of the squared modulus of the
block-restricted sum of beta(n,b) Q_k(nb).

## Conclusion

For every epsilon>0,

\[
 E\ll_{\epsilon,S}(KNB)^\epsilon T
 \sum_{q_t\asymp T}
 \sum_{\substack{r\ {\rm sf,good}\\q_r\ll\min(K,C)}}
 \left(\frac K{q_r}+\frac{NG}{C^2}\right)\frac C{q_r}
 \sum_{(c',m,h)\in D_r(t)}
       |\beta(rc'm,rc'ht^2)|^2.                       \tag{2}
\]

The implicit constants depend only on epsilon, fixed S and the fixed
comparisons. Fixed row sectors and row scalars of a fixed bounded modulus
are permitted, with dependence on that modulus bound. Empty ranges
contribute zero, and bounded nonempty ranges include units.

This reproduces `eq:completed-quadratic-reduction` under its fixed source
S hypotheses. It discharges L542 Hypothesis 1 in that setting, conditional
on (1) and the retained conventions/counts. It does not discharge that
hypothesis for a broader S setting, independently verify (1), audit the
bounded-beta corollary, or prove the cubic input, reflection, global
closure or Xi signs. L542 and L541 describe downstream uses, not inputs.

## Proof

Primary citation: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, 30 September 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[pinned primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
lines 519–588 (arithmetic conventions), 2480–2517 (base estimate),
2518–2566 (statement), and 2567–2626 (weighted proof).
The exact labels are `eq:quadratic-large-sieve`,
`lem:completed-quadratic-reduction`, `eq:completed-quadratic-zero-mask`
and `eq:completed-quadratic-reduction`.

The source attributes (1) to Goldmakher–Louvel, *A quadratic large sieve
inequality over number fields*, Math. Proc. Cambridge Philos. Soc. 154
(2013), 193–212, [arXiv:1112.1642v2](https://arxiv.org/pdf/1112.1642v2),
Definition 1 and Theorem 1.1, PDF pp. 1–2. Their Hecke-family assumptions
are separate from the retained display (1); citing that theorem alone
does not verify the specialization. Reproducing the weighted implication
is necessary to check its exact support and coefficient interface for
L542; importing (2) would bypass the approved audit. No improvement or
novelty beyond the source claim is asserted.

Write Q=KNB. We use a small parameter delta>0 in three estimates below
and choose it at the end. All sums are finite.

### Zero mask and full collision expansion

Since nb=c^2mht^2, the retained zero/multiplicative conventions give

\[
 Q_k(nb)=Q_k(mh)1_{(k,ct)=1}.                          \tag{3}
\]

This identity includes collisions: a prime of k meeting mh zeros both
sides, and otherwise a collision with ct zeros the square factor on the
left and the indicator on the right. Shared g/t or n/t primes cause no
exception.

There are O(T) possible t in the block. Indeed their norms are at most
A_t T; if A_t T<1 there are none, and otherwise ideal counting applies.
Hilbert-space Cauchy therefore bounds E by O(T) times the sum of the
squared row norms with t fixed. For fixed t restrict rows to (k,t)=1.
Expand the entire remaining mask as

\[
 1_{(k,c)=1}=\sum_{r\mid(k,c)}\mu(r).                  \tag{4}
\]

For each k, Cauchy over r|k costs at most d_O(k)<<_delta Q^delta.
After summing these nonnegative terms, write k=rk', c=rc'. Then
r is squarefree good, q_r<=A_k K and q_r<=A_c C; all relevant r thus
lie in q_r<<min(K,C). Terms with (r,t)>1 have no rows. Otherwise set

\[
 I_{r,t}=\{k':rk'\in I,\ k'\ {\rm sf,good},\ (k',rt)=1\}.
\]

This is a fixed row set for fixed r,t. The coefficient set is D_r(t),
also fixed independently of k'. Put I_{r,t}=empty when (r,t)>1.
Multiplicativity gives the bound

\[
 E\ll_\delta TQ^\delta\sum_t\sum_r
 \sum_{k'\in I_{r,t}}
 \left|\sum_{D_r(t)}\beta(rc'm,rc'ht^2)
                   Q_r(mh)Q_{k'}(mh)\right|^2.        \tag{5}
\]

The sign mu(r) has modulus at most one and disappears after Cauchy.
There is no residual condition (k',c')=1: (4) represented that
cancellation before Cauchy. Adding such a mask to the individual
r-summands would not be justified. Restrictions involving r and c',m,h
remain in D_r(t), and none depends on k'.

### S-parts and genuinely row-independent coefficients

Split m=m_S m_g and h=h_S h_g into their S-supported and good parts.
Because m,h are squarefree, the pairs (m_S,h_S) belong to a fixed finite
set, of cardinality at most 4^{|S|}. Apply Cauchy over that finite set in
each inner sum in (5), at a constant depending only on S. Fix one pair.
Since k' is good,

\[
 Q_{k'}(mh)=Q_{k'}(m_S h_S)Q_{k'}(j),\qquad j=m_g h_g,
\]

where the first factor has modulus one and j is squarefree good.
The fixed S-parts have primary representatives and their product is
primary, so no unrecorded unit correction occurs. Removing the modulus-one
row factor is legitimate. Define, for this pair and fixed r,t,

\[
 z_j=\sum_{\substack{(c',m,h)\in D_r(t)\\
                   m_S,h_S\ {\rm as\ fixed},\ m_g h_g=j}}
       \beta(rc'm,rc'ht^2)Q_r(mh).                    \tag{6}
\]

Every summand and its support in (6) is independent of k'. The original
support may correlate c',m,h,t arbitrarily; it remains inside (6) and is
never removed from a column sum. Also q_j<=q_m q_h and

\[
 q_m q_h=\frac{q_nq_g}{q_c^2}\asymp\frac{NG}{C^2}.  \tag{7}
\]

### Quotient ranges and the sieve charge

Put U_0=K/q_r and V_0=NG/C^2. Choose fixed constants A_U,A_V so
q_k'<=A_U U_0 on I_{r,t} and q_j<=A_V V_0 for every column in (6).
Apply (1) with U=max(1,A_U U_0) and V=max(1,A_V V_0).

This application is needed only if both the row set and the relevant
coefficient support are nonempty. Then some q_k'>=1 gives
U_0>=1/A_U, and some q_mq_h>=1 together with (7) gives
V_0>=1/A_V after increasing the fixed A_V if necessary. Consequently
U+V<<U_0+V_0. An empty row or coefficient set already contributes zero.
This argument includes unit columns and rows; a quotient center below
one is not by itself an empty range.

The product cutoff also costs only Q^delta. We have U<<K. On a nonempty
block, q_c<=A_c C and q_c>=1 give C>=1/A_c, while
q_g<=q_b<<B and q_g asymp G give G<<B. Hence V<<NB and UV<<Q.
Thus (1), followed only by enlargement of the positive row sum, yields

\[
 \sum_{k'\in I_{r,t}}\left|\sum_jz_jQ_{k'}(j)\right|^2
 \ll_{\delta,S}Q^\delta
       (K/q_r+NG/C^2)\sum_j|z_j|^2.                  \tag{8}
\]

Any fixed row sector remains a subset of this positive row sum. A fixed
bounded row scalar is removed by its modulus bound, not moved into z_j.
The constant is uniform in all permitted support restrictions.

### Multiplicity and reconstruction

For each j in (6), choosing m_g|j determines h_g=j/m_g, so there are
at most d_O(j) choices. Since q_j<=q_nq_g<<NB, this number is
O_delta(Q^delta). For each such choice, q_c'<=A_c C/q_r. Ideal counting
bounds the number of possible c' by O(C/q_r): when the upper cutoff is
below one there are none, and when it is at least one the standard count
applies. All original constraints can only reduce this count. Therefore
Cauchy within (6), using |Q_r(mh)|<=1 only now in a positive sum, gives

\[
 \sum_j|z_j|^2\ll_\delta Q^\delta\frac C{q_r}
 \sum_{\substack{(c',m,h)\in D_r(t)\\m_S,h_S\ {\rm as\ fixed}}}
                 |\beta(rc'm,rc'ht^2)|^2.             \tag{9}
\]

Summing over the fixed S-parts reconstructs each original triple exactly
once. In particular c' was never stripped of its S-part, m,h are restored
to their original ideals, and no (g,t)=1 restriction has appeared.
Combining (5), (8), and (9) gives (2) with Q^{3delta} in place of
Q^epsilon. Choose delta=epsilon/3; all other losses are fixed constants.
The initial Cauchy supplied exactly the factor T, the sieve supplied
K/q_r+NG/C^2, and grouping supplied C/q_r. This proves (2).

## Mathlib

Coverage of this complete weighted reduction and its arithmetic
specialization has not been checked. No matching formal theorem is
claimed. The proof above uses finite Cauchy inequalities, ideal
factorization/counting, the retained symbol identities and the explicitly
conditional sieve (1); elementary supporting library results would not
establish that full arithmetic input.
