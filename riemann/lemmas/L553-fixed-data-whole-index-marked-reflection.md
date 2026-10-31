# L553 — Fixed-data whole-index marked reflection

## Hypotheses

Use exactly the Eisenstein ring O, lambda, norms q_z, angular function
alpha, zero-extended sextic characters and test transform Vsharp of
L548. Fix S, E, L, one base ray character Psi_0 and its periodic function
phi as there; L is fixed before any good primes vary. Fix X>0 and a
test V satisfying L548's two-ended smooth rapid bounds. Retain L548's
raw theta, coefficient/support and finite Fourier/Gauss inputs. Use
L547's simultaneous canonical choices and L548's fixed-data reflection
with absolutely convergent dual sums.

Let P_0 be a finite set of distinct good primary primes outside S,
with j_p in {0,...,5}, and set

\[
 \Psi(a)=\Psi_0(a)\prod_{p\in P_0}\chi_p(a)^{j_p}.
\]

Every integer character power is zero on nonunits, including exponent
zero. Let Q be a finite set of distinct good primary primes outside S,
initially disjoint from P_0. The primal n is squarefree primary and b
is any primary element, with (nb,E)=1. They may share primes. Define

\[
 \mathcal T_Q=
 \sum_{n,b}\frac{\gamma_2(n)\bar\alpha(n)\bar\alpha(b)^3
                \Psi(n)\Psi(b)^3}{\sqrt{q_n}\,q_b}
        V(q_nq_b^3/X)\prod_{q\in Q}1_{q\mid nb^3}.             \tag{1}
\]

For product-form marks, also permit finitely many pairwise disjoint
finite good-prime lists, one prime chosen from each list, with literal
coefficient product \(\prod_i a_i(p_i)\). Keep the stipulated independence
of these lists and coefficients from the row and dual indices. Any
row-character presentation as the displayed Psi, with one fixed L, is
an assumption; it is not derived here. No infinite-list or
arithmetic-uniform limit is assumed or concluded.

## Conclusion

For each h_0 modulo L choose a base partition P_0=A_0 disjoint-union I_0,
with every nonzero-exponent base prime in A_0, and a marked partition
Q=A_Q disjoint-union I_Q. Put

\[
 r=\prod_{p\in A_0\cup A_Q}p,\qquad c=c_F(h_0)r,\qquad
 x=\lambda^4\mu.
\]

Take d, vartheta and kappa_F from L547 for this actual active radical.
All sigma_p, epsilon_p and omega_(p,j) use this branch's entire c,
with the definitions in L548 (8) and its finite Gauss conventions.
The base columns are

\[
 B_p(x)=\begin{cases}
 \chi_p(x)^{-j_p-2},&j_p=1,2,3,5,\\
 q_p^{-1/2}(-1+q_p1_{p\mid x}),&j_p=4,\\
 q_p^{-1/2}\chi_p(x)^{-2},&j_p=0\text{ active}.
 \end{cases}                                                   \tag{2}
\]

There is the exact identity

\[
 \mathcal T_Q=\sum_{h_0,A_0,I_0,A_Q,I_Q}\zeta_Q
 \sum_{0\ne\mu\in\lambda^{-4}O}
 \frac{d(\mu)\alpha(\mu)\vartheta(x)}{\sqrt{q_\mu}}
 \prod_{p\in A_0}B_p(x)
 \prod_{q\in A_Q}q_q^{-1/2}\chi_q(x)^{-2}
 V^\sharp(q_\mu X/q_c^2),                                    \tag{3}
\]

where

\[
 \begin{split}
 \zeta_Q={}&-\frac i{81}\bar\alpha(c)^2
        \widehat\phi(h_0)\bar\kappa_F
        \prod_{p\in I_0}(1-q_p^{-1})\prod_{q\in I_Q}q_q^{-1}\\
 &\quad\cdot\prod_{p\in A_0}\chi_p(\sigma_p)^{-2}\omega_{p,j_p}
        \prod_{q\in A_Q}\chi_q(\sigma_q)^{-2}(-\omega_{q,0}),
 \qquad |\zeta_Q|\le1/81.                                  \tag{4}
 \end{split}
\]

The canonical dependence on h_0 and r modulo (lambda^12 L^4)^2 is
unchanged. Each dual sum is absolutely convergent over the entire
original nonzero lattice, retaining all coefficient zeros. Inactive
marked primes are absent from c and its kernel scale.

If Q meets P_0, the entire corresponding primal sum (1) is zero,
for every base exponent including zero. Such tuples are removed before
using (3). Finite product-form marked sums follow by multiplying (3)
by each tuple's coefficient and summing the noncolliding tuples.

This supplies the conditional fixed-data marked identity retained in
L546/L541 and used in L552. It establishes a source-claimed implication,
not a new reflection theorem. It does not prove the raw imports,
row-character presentation, broader arithmetic uniformity, global
closure or any actual-Xi sign. This conditional finite implication has
passed the separate critical review below; downstream uniform contracts
are not silently replaced.

## Proof

### Citation and scope

The matching claimed result is OpenAI, *The Quasi-Riemann Hypothesis:
A Zero-Free Half-Plane Re(s)>7/8*, 30 September 2026,
[pinned primary TeX, commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`cor:marked-reflection`, `eq:marked-reflection`,
`eq:marked-reflection-phase`, statement/proof lines 6914–6991.
Its hypotheses/normalization are in `prop:completed-reflection`,
1551–1726; the simultaneous-compatibility proof is 2113–2122;
product-form definitions/normalization are 6825–6907. These complete
cases were inspected. The corollary is not a premise below.
Reproduction checks the finite implication retained locally; L547/L548
make a reproof of theta theory unnecessary.

There is no marked-identity circularity through the local inputs.
L548 explicitly uses only the all-six local computation from L546
Hypotheses 1–2, not its marked Hypothesis 3 or separation Hypothesis 4.
L547 constructs its data without a marked identity. We use only their
fixed-data conclusions, with their raw imports and conditional bounds.

### Primal identity and normalization

Let m_q(a)=chi_q(a)^0=1_(q does not divide a), the zero-extended
character function. Then m_q(nb^3)=m_q(n)m_q(b)^3: each factor
is zero or one, and q divides nb^3 precisely when it divides n or b.
Shared factors create no exception. Thus pointwise

\[
 \prod_{q\in Q}1_{q\mid nb^3}
  =\sum_{J\subseteq Q}(-1)^{|J|}\prod_{q\in J}m_q(nb^3).       \tag{5}
\]

Set Psi_J=Psi product_(q in J) m_q. Multiplication in (5) changes
Psi(n)Psi(b)^3 into exactly Psi_J(n)Psi_J(b)^3, without dividing
by any zero factor. Psi_J has the same Psi_0, phi and L; its added
local primes all have exponent zero.

The primal sums are absolutely convergent. For example |V(y)|<=C y^(-2)
for all y>0 follows from the test hypotheses. L548's |gamma_2(n)|<=1
and character bounds majorize the absolute sum in (1) by

\[
 C X^2\sum_n q_n^{-5/2}\sum_b q_b^{-7}<\infty.
\]

The rank-two lattice count used in L548 gives convergence for either
exponent greater than one; primary/squarefree restrictions only reduce
these positive sums. Marks and added masks have modulus at most one.
Consequently (5) gives

\[
 \mathcal T_Q=\sum_{J\subseteq Q}(-1)^{|J|}
                      \mathcal T_\varnothing(\Psi_J).          \tag{6}
\]

Each term is exactly L548's unmarked completed Mellin integral. Indeed
putting t=s-1/2 on a>1 gives the n,b factor
X^t q_n^(-t-1/2) q_b^(-3t-1). Mellin inversion yields
V(q_nq_b^3/X)/(sqrt(q_n)q_b), with no extra power of X.
Absolute Dirichlet convergence and rapid decay of Vhat justify this
termwise inversion, as in L548. Apply its reflection to each term.

### Exact subset collection

Fix h_0, an allowed base partition (A_0,I_0), and an active marked set
A contained in Q. In a reflected term of the J-summand, the active
marked set can be A if and only if A is contained in J. Write uniquely
J=A disjoint-union K, where K is contained in I=Q minus A. The primes
of K are included but inactive; those of I minus K are absent.
Conversely every such K gives exactly one of these terms. Nonzero
base exponents cannot be inactive: their zero-frequency Fourier
coefficient vanishes in L548.

For all these K, L547 supplies literally the same active radical
r=product_(A_0 union A) p, c_F, c, d, vartheta, kappa_F and kernel.
The active sigma, epsilon and omega data also agree because they use
this same whole c. After removing inactive marked scalars, the terms
therefore have a common dual summand. Its scalar is

\[
 C_A=-\frac i{81}\bar\alpha(c)^2\widehat\phi(h_0)\bar\kappa_F
       \prod_{p\in I_0}(1-q_p^{-1})
       \prod_{p\in A_0}\chi_p(\sigma_p)^{-2}\omega_{p,j_p}
       \prod_{q\in A}\chi_q(\sigma_q)^{-2}\omega_{q,0}.
\]

The literal scalar of the K term, including inclusion-exclusion, is
(-1)^(|A|+|K|) C_A product_(q in K)(1-q_q^(-1)). Hence their sum is

\[
 \begin{split}
 C_A(-1)^{|A|}\sum_{K\subseteq I}(-1)^{|K|}
                         \prod_{q\in K}(1-q_q^{-1})
 &=C_A(-1)^{|A|}\prod_{q\in I}\bigl(1-(1-q_q^{-1})\bigr)\\
 &=C_A(-1)^{|A|}\prod_{q\in I}q_q^{-1}.                    \tag{7}
 \end{split}
\]

Absorb one minus sign into omega_(q,0) for every q in A. Formula (7)
is (4), with A_Q=A, I_Q=I. L548's active zero-exponent column is
q_q^(-1/2)chi_q(x)^(-2), giving exactly (3). In particular its scalar
uses -omega_(q,0)=tau_(q,2)^+ chi_q(epsilon_q)^(-2); the new sign
changes no other local data.

This collection is separate for each active set. Adding an active
mark changes c, potentially all local phases and the cusp sector.
We never factor across different active sets or substitute the
conductor of the full marked set for their actual conductors.

For active p, c/p is a unit modulo p by disjointness and the support
of c_F. Thus sigma_p, epsilon_p are units. All active scalar character
factors and omega_(p,j) have modulus one under the retained Gauss
inputs. Also |hat(phi)(h_0)|<=1, |kappa_F|=|alpha(c)|=1, and the
positive inactive factors are less than one. This proves (4)'s bound.

### Cases, collisions and analytic legality

All six base exponents keep exactly their L548 scalars and columns:
nonzero exponents are active, including the unsplit exponent-four
Ramanujan column, while exponent zero can be active or inactive.
Collection (7) acts only at new marked primes and changes none of
these base cases. It does not identify the Ramanujan column with a
zero-extended character.

If Q is empty, (5)–(7) have one term and recover L548. If A_Q is
empty, the inactive marked coefficient is product_(Q) q_q^(-1)
at the base active conductor. If I_Q is empty, only K=empty occurs,
with one minus sign per active mark. Empty base sets and r=1 are
allowed by L547/L548; empty products equal one. Nonunit h_0 and
h_0=0 are included by their construction. No inverse of h_0 or x
is used.

If a marked q belongs to P_0, fix a primal pair (n,b). If q does not
divide nb^3, its mark is zero. Otherwise q divides n or b, and the
base factor in Psi(n) or Psi(b)^3 vanishes for every j_q, including
zero. The summand vanishes in either case. If q divides both n and b,
the same reasoning applies, without any coprimality assumption on
them. Thus colliding sums vanish before reflection, without dividing
by a character or applying the disjoint-set formula outside its domain.

There are finitely many J, h_0 and active subsets. L548 supplies
absolute convergence for each reflected series at its actual fixed
data and scale; the finite sum of their absolute sums is finite.
Rearrangement by (A_0,A_Q,K) and termwise collection in (7) are
therefore legal, with every original nonzero mu and coefficient zero
retained. No infinite subset limit, conductor-uniform estimate or
dual-series/integral interchange on the zero contour is needed.
Finite summation of tuple coefficients is legal for the same reason.
Remove collisions separately for each original tuple and keep its
product coefficients and prescribed independences. This proves the
claimed conditional fixed-data identity.

### Independent critical review, 2026-10-31

The implication passes under the stated inputs. The matching primary
statement and complete proof at 6914–6991, its normalization at
1591–1629, all local cases at 1655–1726 and 2086–2122, and the
product-form definitions at 6825–6907 were checked against the local
argument. The source's marked corollary is the claim being tested,
not an input. This is verification of a conditional reproduction,
not a new result beyond that claim or an audit of the full manuscript.

**Normalization and applicability.** For each J, the local set is
exactly P_0 union J, all its primes are distinct and outside S, and
every added exponent is zero. The fixed character, E, L, phi and V
are unchanged, so L548 applies separately to every J. On s=a+it
with a>1, absolute Dirichlet convergence is available; Vhat on the
line Re(s-1/2)=a-1/2 decays faster than every power. Inserting its
Mellin inversion therefore gives, exactly,

\[
 X^{s-1/2}q_n^{-s}q_b^{-3s+1/2}
 =q_n^{-1/2}q_b^{-1}
      (q_nq_b^3/X)^{-(s-1/2)}.
\]

Thus (1) has neither a missing X power nor an extra cube-root scale.
The primal majorant in the proof has exponents 5/2 and 7, both
strictly above the rank-two lattice threshold 1. It covers shared
primes, all masks, and all finite tuple coefficients individually.

**Multiplicity, signs and canonical data.** The indexing is a genuine
bijection: a fixed reflected term has one h_0, one base active set,
one marked active set A, and one original subset J containing A.
Its remaining marked set K=J minus A is uniquely a subset of Q minus A.
Conversely these data specify one original reflected branch, without
any choice for a prime in Q minus J. Hence there is no extra factor
of 2 at an absent prime. L547 gives equality of the canonical data
for equal active frequencies before their finite summation, not just
equal sector labels. After that summation it gives the common d,
vartheta and kappa_F used here. Consequently each K contributes
literally the same dual series times its displayed inactive scalar.
For one remaining inactive prime the scalar sum is
1-(1-q_q^{-1})=q_q^{-1}; an active marked prime occurs only in the
subtracted term and contributes one minus sign. Finite distributivity
gives (7) for every size of Q. No division by C_A, phihat or a dual
coefficient occurs, so their zero values are covered. Conductors are
identified only within a fixed active group, never across different A.

**Local cases and zero values.** The unmarked local computation in
L546 uses just its Hypotheses 1–2: it changes h_p to its inverse
only on the nonzero local-frequency set. For j=1,2,3,5 the resulting
Gauss indices j+2 are 3,4,5,1 modulo six, all nontrivial. Their
columns are respectively chi_p(x)^3, chi_p(x)^2, chi_p(x),
chi_p(x)^5 on units, and all vanish when p divides x. For j=4
the inner exponent is zero and its sum over nonzero frequencies is
q_p-1 at p|x and -1 otherwise; this is exactly the unsplit column
in (2), with scalar tau_(p,4)^-. For j=0, zero frequency gives
1-q_p^{-1}; nonzero frequency gives scalar
-tau_(p,2)^+ chi_p(epsilon_p)^(-2) and column
q_p^{-1/2}chi_p(x)^(-2), which vanishes at p|x. These seven
active/inactive possibilities exhaust all six base exponents.
The marked sign changes only that active j=0 scalar. Since p occurs
once in r and not in c_F lambda, c/p, sigma_p and epsilon_p are
units modulo p, justifying each scalar's unit modulus. No inverse
of x or h_0 is used. Nonunit h_0, the zero h_0 class and r=1 are
within L547/L548's conclusions, with no additional branch deletion.

The collision proof is pointwise before any reflection: at a base
prime, either the divisibility mark is zero or at least one of the
two base-character factors is zero. This holds for exponent zero,
for a prime dividing both n and b, and for every other mark and
tuple coefficient. Finite tuple linearity thus removes exactly the
colliding original tuples; it imposes no new dual support mask.

**Convergence and logical scope.** A direct bound also checks the
recombination. In a fixed branch let M_B be the product of suprema of
its finitely many local column moduli. These are finite: the
nonzero-character columns are bounded by 1, the active j=0 column
by q_p^{-1/2}, and the j=4 column by
max{1,q_p-1}/sqrt(q_p). For any fixed A>1/2, L548 supplies
|Vsharp(y)|<=C_(A,V)y^{-A}. Thus that branch's absolute dual sum
is at most

\[
 M_B C_{A,V}(q_c^2/X)^A
       \sum_{\mu\ne0}|d(\mu)|q_\mu^{-A-1/2}<\infty,
\]

by L548 (9), since A+1/2>1. There are only finitely many branches
and J for the fixed data. Their summed absolute majorants justify
every collection without a uniform bound as primes vary, and retain
the complete original lattice including its coefficient zeros. No
exchange on the zero Mellin line is invoked. L548's use of the
all-six local computation does not invoke L546 Hypothesis 3 or 4,
and L547's construction likewise contains no marked premise. There
is therefore no circular import from the marked identity or its
downstream energy application. No new direct mathematical input is
needed beyond L547 and L548.

## Mathlib

Full matching coverage has not been checked. Formula (7) uses finite
distributivity over subsets; that fact is not a citation for theta
reflection. The primary claimed reflection is cited above; its raw
imports and analytic qualifications remain those of L548. No claim
that Mathlib contains or lacks the full theorem is made.
