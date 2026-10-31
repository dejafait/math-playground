# L552 — Full original-support polynomial raw total

## Hypotheses

Use O=Z[omega], q_a=|a|^2, lambda above 3, and the zero-extended
characters of the pinned source cited below. Fix its finite excluded
prime set S, finite character family and common modulus L. All fixed
finite character-expansion coefficients are bounded independently of Z.
Retain, as conditional inputs, `prop:completed-reflection` items (1)–(3),
`cor:marked-reflection`, their exact scalar/local-column formulas, and
the cusp coefficient support and majorant `old-eq:4.3`. These arithmetic
and theta statements are not independently proved here. In particular
all finite data and coefficient bounds are simultaneous in the moving
local prime sets. Do not assume the source's polynomial raw-total claim
or the raw-total clause formerly retained in L541 Hypothesis 3.

Let Z>=2. Fix m,v,q,z_1,...,z_s,nu>=0 in bounded ranges, with s bounded,
and fixed constants C_k,C_f,C_rho,C_i,A_slot>=1. The original rows and labels
satisfy

\[
 0<q_k\le C_k Z^m,\qquad q_f\le C_f Z^v,\qquad
 q_{\mathfrak r_\rho}\le C_\rho Z^q,\qquad
 X^{-1}\le Z^\nu.                                      \tag{1}
\]

Here f is squarefree and good, and the puncture radical r_rho is
squarefree. Both are fixed within the row/tuple sum. For each of s
pairwise disjoint good prime lists P_i, every member satisfies
q_p<=C_i Z^(z_i), and its coefficient a_i(p) has modulus at most A_slot.
The character, lists, coefficients and puncture have the independences
stipulated for the source's completed marked sum `eq:marked-completion`.
Only the upper norm bounds enter the estimate below. A bounded range
of N_* with X=Z^(N_*) is included by taking nu>=max(0,-N_*).

The base local set is exactly the good prime support of
(k) f r_rho, with exponents combined modulo six and zeros retained.
Remove a tuple having a marked prime in that set, as prescribed by
`cor:marked-reflection`; its primal summand vanishes. Expand each other
tuple using that corollary. One may further split every exponent-four
Ramanujan column into its small term and its divisibility term, and
split the latter by

\[
 1_{p\mid n_0b_0^3}
 =1_{p\mid n_0}+1_{p\nmid n_0}1_{p\mid b_0}.             \tag{2}
\]

This uses the original representation mu=u lambda^h n_0 b_0^3,
h>=-4, n_0 squarefree and n_0,b_0 primary; their shared primes remain
allowed. All support restrictions and zero masks stay in these
expressions. Freeze actual powerful/supported row parts only as
functions of the row, not as additional independent summation labels.
Extra residue sectors are the fixed finite sectors modulo M_ref^2,
M_ref=lambda^12 L^4, and do not have unbounded multiplicity.

Smooth partitions of the original row parts, if present, have only
finitely many labels meeting the bounded original norm ranges and bounded
absolute overlap: the sum of absolute products of their values at
each original row is at most a fixed C_part. Other original windows
kept outside the kernel are bounded by a fixed constant. Their actual
values, or their absolute upper bounds, are included in the weights.
Dual partitions satisfy L551 (3) when that lemma is applied; their
indices are not additional finite labels in the present count.

Import the unrestricted O(Y) ideal count for Y>=1 and the uniform
ideal divisor bound d_O(a)<=C_delta q_a^delta from the precise source
locations below. There is no dependence on analytic orders in these
arithmetic hypotheses.

## Conclusion

Put z=sum_i z_i and R=m+v+q+z. Let J enumerate all original nonzero
element rows, original full labelled prime tuples, and the finite
reflection/local/assignment branches just specified, including fixed
sectors and any original row-partition labels. It does not enumerate
mu, its unit, ramified valuation, residual ideals or dual dyads.
For each j write the unsimplified reflected summand as
b_j(mu) Vsharp(X q_mu/q_(c_j)^2), including all non-kernel scalars
and the indicated masks/windows in b_j. There are nonnegative weights
w_j, independent of mu and of kernel/Fourier orders, for which

\[
 |b_j(\mu)|\le w_j,\qquad
 \operatorname{TOTAL}:=\sum_{j\in J}w_j(1+q_{c_j}^2/X)
 \le C Z^{B},\qquad
 B=m+z+\tfrac72R+\nu.                                  \tag{3}
\]

C is uniform for the stated labels and bounded ranges; it can depend
on the fixed arithmetic datum, slot cap, coefficient/support constants
and C_part. B is chosen before any analytic order. This is L551 (2),
over the full original support, conditional on the retained arithmetic
inputs. It is a deliberately crude reproduction of the source's raw
cost, not an improved arithmetic estimate.

With L551's remaining cutoff/annulus/test hypotheses, its linear
discarded-row norm is therefore

\[
 \|T\|_2\ll_A Q_A(V)
       Z^{B+(\tau_{\rm ref}/2)(1-A)},\qquad A>1.          \tag{4}
\]

Its saving threshold is A>1+2(B+D_tail)/tau_ref. Test seminorms and
height costs stay outside B. Fixed-label uniformity in (3) does not
include a sum over f or punctures. Unbounded slot number, changing L,
unbounded row-partition multiplicity, recursive reconstruction fibres,
the proof of the marked/theta inputs and actual-Xi signs are excluded.

## Proof

### Source scope and purpose

OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
Re(s)>7/8*, 30 September 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[pinned build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex):
`prop:completed-reflection`, items (1)–(3), lines 1655–1726;
`old-eq:4.3`, lines 1674–1683; `cor:marked-reflection` and its proof,
lines 6914–6990; `par:reflected-energy-data`, lines 7200–7281;
actual denominator at lines 7377–7384. The ideal count is at lines
566–574, and the divisor-bound convention and proof at 681–698.
These are the cited counting inputs; no new ideal-count theorem is
being reproved. The raw-cost assertion itself, lines 7421–7443, is
the audit target and is not used as a premise.

The prior SPECIALIZE assessment authorizes checking this particular
assembly: L551 had retained its positive total. The following proof
supplies that total from finite source indexing. It leaves the
coefficient and marked-reflection hypotheses conditional and claims
no advance beyond the source's stated conclusion.

### The original index set and its denominators

Fix a row k and an admissible full tuple t=(p_1,...,p_s), including
primes which later take inactive marked branches. Set

\[
 D(k,t)=\operatorname{rad}\bigl((k)_{\rm good}
                         f\mathfrak r_\rho\prod_i(p_i)\bigr).
                                                               \tag{5}
\]

Its norm is at most the norm of the product inside the radical, so

\[
 q_D\le q_k q_f q_{\mathfrak r_\rho}\prod_i q_{p_i}
      \le C_D Z^R.                                     \tag{6}
\]

This inequality permits every overlap among k,f and the puncture.
After removal of marked/base collisions, marked primes are distinct
from the base primes and from each other. Repeated base primes have
already been combined into a single local column, including exponent
zero. Thus the union of base and marked primes is precisely the
prime set of D; no prime appears twice as an independent local choice.
Dropping a restriction later in a positive bound does not change this
identification of the original source expression.

Every branch has c=c_F r, where r is its active radical, hence r|D.
The marked identity's inactive primes are absent from r; c_F belongs
to the one fixed finite set determined by h_0 modulo L. Therefore

\[
 q_c\le C_F q_D,\qquad
 1+q_c^2/X\le C'(1+q_D^2 Z^\nu).                       \tag{7}
\]

In the frozen notation this is exactly c=c_F F_act R_row P_active,
not the conductor of a different active subset. Neither (6) nor (7)
uses an enlarged residual row or a retained dual length.

For a fixed k its powerful part, supported valuation-one part and
remaining squarefree part are determined uniquely by prime valuations.
The six possible row units are included in counting elements k.
There is no further count of freely chosen row factors. Fixing separate
residual-row and active-product classes modulo M_ref^2 partitions the
existing indices, with at most a fixed finite multiplicity if all
sector displays are retained. The same applies to h_0 modulo L and
the fixed finite character presentation. Include this fixed multiplicity
in C_sec. The cusp coefficient and additive function are determined
by these choices, not three freely repeated infinite columns.

### All local branches, including further assignments

Let omega(D) count distinct prime ideals in D. The following bounds
refer to the literal coefficients before normalization by dyadic
lengths. Every character or additive phase has modulus at most one;
its zero remains part of the coefficient until this upper bound.

At a base prime with exponent other than zero or four there is one
local column, of modulus at most one. At exponent zero there are two
choices: inactive, or active with column of modulus at most
q_p^(-1/2). The inactive scalar contains 1-q_p^(-1), of modulus at
most one. At exponent four, after both allowed splittings, the local
pieces are

\[
 -q_p^{-1/2},\qquad
 q_p^{1/2}1_{p\mid n_0},\qquad
 q_p^{1/2}1_{p\nmid n_0}1_{p\mid b_0}.                 \tag{8}
\]

Each has modulus at most q_p^(1/2). Identity (2) is valid also when
n_0 and b_0 share p. Since p is good, multiplication by lambda^4
does not affect its divisibility. Formula (8) explicitly charges the
extra two-way assignment of a divisibility term; the unsplit source
count O_L(4^|P|) is not silently reused after this operation.

A marked prime has two choices. Its inactive contribution has scalar
factor q_p^(-1), and its active column has modulus at most q_p^(-1/2)
and a scalar of modulus one. These formulas use the exact compatible
marked expansion, already conditional here. In particular, no bound
is obtained by giving an inactive term the active term's conductor.

Thus there are at most C_sec 3^omega(D) local branches, and on each
branch the product of local column magnitudes is at most q_D^(1/2).
This allows an overcount at inactive primes and is harmless. If only
the first Ramanujan split is used, the same bound covers that count.
One can instead keep the original unsplit columns, all of modulus
at most q_p^(1/2), with fewer choices.

The exact source scalar has modulus at most 1/81. The angular factor
has modulus one, and all remaining additive/character factors have
modulus at most one, including at permitted shared primes. On the
retained cusp support the coefficient majorant gives

\[
 \frac{|d(\mu)|}{\sqrt{q_\mu}}
 \le 27\,3^{-h/3}q_{n_0}^{-1/2}q_{b_0}^{-1}
 \le 27\,3^{4/3}=:C_0,\qquad h\ge-4.                 \tag{9}
\]

Here norms multiply even at shared primes. The inequality uses only
the retained `old-eq:4.3`, q_(n_0),q_(b_0)>=1 and q_lambda=3.
The coefficient is zero off its support. Each product of slot
coefficients has modulus at most A_slot^s. Consequently, if H_j is the
absolute product of original row-partition window values, a suitable
weight is

\[
 w_j=C_* A_{\rm slot}^s H_j q_{D(k,t)}^{1/2},                    \tag{10}
\]

where C_* includes C_0/81 and the fixed bounded remaining windows
and character-presentation coefficients. Without row partitions put
H_j=1. For each fixed source branch the sum of H_j over its original
row-partition labels is at most C_part. Thus partitions do not add
an uncharged power of log Z or depend on kernel orders.

To apply the cited divisor estimate to the branch count, D is squarefree,
so d_O(D)=2^omega(D). Hence
3^omega(D)<=d_O(D)^2. Use the source bound with delta=1/2 on each
of these two factors to obtain

\[
 3^{\omega(D)}\le C q_D.                              \tag{11}
\]

The constant is uniform in all moving labels. This fixed exponent,
rather than an optimized adjustable loss, suffices for the raw total.
It is independent of all analytic choices.

### The positive total and the infinite dual sum

Summing (10) over branches, sectors and original row partitions, and
then using (7), gives, for one row and tuple,

\[
 \sum_{j\text{ over }(k,t)} w_j(1+q_{c_j}^2/X)
 \le C q_D^{3/2}(1+q_D^2 Z^\nu)
 \le C' Z^{(7/2)R+\nu}.                              \tag{12}
\]

The last inequality uses R,nu>=0, Z>=2 and (6), including the case
D=1. An empty local set has one branch for each allowed fixed h_0
and no moving prime cost. An empty slot list has one empty tuple.

By the cited ideal count, the original element-row count is at most
6 C C_k Z^m: each nonzero principal ideal has exactly six generators.
No second row-unit factor is added. Each prime list has at most
C' C_i Z^(z_i) elements by enlargement to all ideals. Multiplying
these counts gives at most C'' Z^z full tuples. Disjoint lists mean
that a tuple product determines its labelled entries; counting the
tuples directly already includes all needed multiplicity. Empty
supports give zero total; zero nominal lengths give bounded counts.
Sum (12) over these rows and tuples to obtain (3).

The dual unit, h, n_0 and b_0 have not been counted as finite
nonfrequency data. For a supported nonzero mu its representation is
unique: away from lambda, a valuation has the form e+3b with
e in {0,1}, determining the squarefree and cube valuations uniquely;
primary generators then determine the remaining unit, and the lambda
valuation determines h. Assignments in (8) impose restrictions on
this original mu. Extracting N_F or B_F is an exact reindexing under
those restrictions and does not create a second copy of mu within
one branch. In particular b_0 may share a prime with n_0 or N_F.
For L551, keep b_j as a function of the original mu and keep its
scale X/q_c^2. Reintroducing the length-normalized internal coefficients
without their extracted scalars would be a different expression and
is not justified by (10).

Dual dyads, including arbitrarily large positive h, are dealt with
by L551's absolute cutoff-overlap and full lattice tail. Where two
assignments restrict the same supported coefficient their local
indicators in (2) are disjoint; bounded dual-cutoff overlap therefore
is used inside each branch and does not require counting infinitely
many dyads in J. Any separately chosen original row or fixed finite
branch restriction only removes terms. No extra condition on primes
of S or any shared-prime coprimality is introduced in this argument.

Now (3) supplies exactly the positive total in L551 (2). Applying
that lemma, with its independent annular comparison, scale threshold,
bounded dual-cutoff overlap and test class unchanged, proves (4).
The choice of B precedes A and Fourier orders. Pure-twist or moving-test
seminorms remain those explicitly displayed in L551 and are not
absorbed into B.

The estimate is uniform for each fixed f and puncture satisfying (1).
If a later application asks to sum such labels, their cardinality
and any weights must additionally be charged. In particular uniformity
alone does not grant that sum, and no recursive-fibre estimate follows.
This completes just the conditional original-support raw-total audit.

### Independent replay and L541 handoff (2026-10-31)

An independent replay rechecked the pinned source's complete local cases
at 1655–1718, the marked statement and compatible-branch proof at
6914–6990, the original labels at 7200–7281, and actual denominators at
7377–7439. The arithmetic counting inputs at 566–574 and 681–698 were
also rechecked. The scalar and coefficient assertions remain hypotheses;
this replay verifies their use, not their derivation from theta theory.

More explicitly, before any length normalization, the absolute value of
each branch coefficient is bounded by the product of: its fixed
character-expansion coefficient; its slot coefficients; its original
window values; a scalar of modulus at most 1/81; the cusp ratio in (9);
and at most one local factor of size q_p^(1/2) for each p|D.
The angular factor and additive character have modulus one. Inactive
base and marked scalars have modulus at most one. Thus (10) bounds the
literal coefficient uniformly in mu, even as h tends to infinity.
No extracted inverse-root scalar has been silently omitted. The lower
endpoint h=-4 gives exactly the upper constant in (9).

The three exponent-four pieces in (8) do not multiply the two
exponent-zero choices: these are different local exponent cases at a
single combined base prime. A marked prime is disjoint from that base
set and has only two choices. Therefore three choices per prime of D
suffice for the fully split expression. Together with (10), (11) and
(7), the per-row-and-tuple total costs q_D^(3/2) times
1+q_D^2 Z^nu, not a product of separate counts of the frozen row
factors. Counting all original rows and labelled tuples then gives
exactly B=m+z+(7/2)R+nu, including empty lists and D=1.

For L541 set m=M, take the upper f and puncture norm exponents for
v,q, sum the upper lengths of ALL original slots for z, and take
nu at least the nonnegative upper bound for -N_*. The symbol v here
is the f upper exponent in (1), not L541's residual dual length v.
All these choices precede A. For one common A over moving bounded
log-length ranges, use the finite supremum of B on those ranges in
L551's saving threshold. This upper exponent is still chosen before A.
Fixed f and puncture labels are not summed.
Original row-partition labels are charged by C_part at fixed k, while
dual cutoff labels are charged pointwise by L551 (3) at fixed mu.
These two bounded-overlap hypotheses have distinct uses.

Now a_j^(-1)=q_(c_j)^2/X, so (3) is literally L551 (2) with
B_tail=B. Retaining L551's independent actual-annulus comparison,
scale threshold and test hypotheses gives L541 (12a). The strict
discarding condition E>tau_ref still implies a_j q_mu>U at equality
in the logarithmic scale threshold. The l1 domination charges every
original coefficient before any grouping into residual rows, and
requires neither an extra row-count square root nor Fourier inversion.
Thus the substitution passes under precisely the displayed premises.
Unbounded row-partition overlap, additional sums over f or punctures,
and a replacement of literal coefficients by normalized internal ones
are not covered. The exponent, test costs and arithmetic qualifications
are unchanged by this review.

## Mathlib

Full matching coverage has not been checked. The proof uses the cited
source ideal/divisor counts, retained exact arithmetic formulas, elementary
finite positive sums and L551's analytic consequence. No full matching
Mathlib theorem is imported; unknown availability is not evidence of
absence. No formal verification of the cusp/marked inputs is claimed.
