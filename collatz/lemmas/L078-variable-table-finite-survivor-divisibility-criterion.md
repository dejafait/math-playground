# L078 — Variable-table finite-survivor divisibility criterion

## Hypotheses

Retain all of C077a's table and certified data hypotheses: integers
r>=3, B,tau>=0, strictly increasing integers 2<=J_0<...<J_(r-1),
integers H_i>=3, all order tests, support tests when B>0, and cutoff
tests (4) always and (5) when tau<=B, with their independent constants.
No data test is weakened or inferred from another certificate.
Set p=r-2, q=r-1, kappa=23/11 and

\[
k_i=3J_i+H_i,\quad K=\sum_i k_i,\quad
N=\sum_i(4J_i+H_i)+2r+18B,\quad
\Lambda=N\log2-K\log3,\quad \Delta=2^N-3^K.
\tag{1}
\]

For every integer 0<=t<=B, define the literal test allocation
beta_i(t)=0 for i<p, beta_p(t)=t, beta_q(t)=B-t, and put

\[
a_i(t)=2+18\beta_i(t),\quad d_i(t)=4J_i+H_i+a_i(t),
\quad T_i(t)=\sum_{j<i}d_j(t),\quad U_i=\sum_{j>i}k_j,
\]
\[
F_i=\frac{23\,3^{H_i}(27^{J_i}-16^{J_i})}{11}
       +(3^{H_i}-2^{H_i})16^{J_i},\qquad
\Phi(t)=\sum_{i=0}^{q}F_i2^{T_i(t)}3^{U_i}.
\tag{2}
\]

These are complete integer expressions, with an empty exponent sum zero.
The candidate set is

\[
\mathcal S=\{t\in\mathbb Z:0\le t\le B,\ t<\tau\}.
\tag{3}
\]

The additional arithmetic hypothesis is

\[
\text{for every }t\in\mathcal S,\qquad \Delta\nmid\Phi(t).
\tag{4}
\]

A sufficient way to certify (4) is, for every t in this same set, to
supply an integer m_t>1 with m_t dividing Delta and Phi(t) nonzero
modulo m_t. The moduli may differ with t and need not be prime. Direct
nondivisibility certificates are also allowed. All finite evaluations
must be justified; no such certificates are asserted for arbitrary tables.

## Conclusion

There is no tuple satisfying C077a (6) for which all unshifted inputs
s_k-kappa are integers. More precisely, for any feasible tuple, let z
be its unique position carrying indexed outgoing row 0, and normalize
x_i=s_((z+i) mod r), x_r=x_0 as in C077a. Its surviving parameter t
belongs to S, and necessarily

\[
x_0-\kappa=s_z-\kappa=\frac{\Phi(t)}{\Delta}\notin\mathbb Z.
\tag{5}
\]

The inequality Delta>0 and positivity/integrality of every Phi(t) hold
under the data hypotheses alone for every 0<=t<=B. When S is empty,
no feasible tuple exists already by C077a, and (4) is vacuous; no
arithmetic certificate is required.

This conditional criterion supplies neither certificates for a new table
nor existence or feasibility of any candidate. It asserts nonintegrality
only at the normalized row-0 input, not at every individual junction.
It is a local REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-variable-table-survivor-divisibility.md`,
not progress beyond the checked affine/divisibility machinery. Its
separate critical audit below found no defect. Actual-word application, other-table
exclusions and universal eventual descent remain unresolved.

## Proof

### Import the integer pair at the literal cut

Use Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
For a finite nonempty chronological binary word of length N and K ones,
it gives the formal map (3^K n+phi)/2^N with integer numerator phi and
unique fixed point phi/(2^N-3^K), provided the denominator is nonzero.
Later letters/maps compose on the left. Here 0 denotes E(n)=n/2 and
1 denotes O(n)=(3n+1)/2. Only the formal identities are imported; no
integer-itinerary converse or primitive-word hypothesis is needed.
The prior assessment inspected the primary statements and relevant
printed proof cases. General coding and rotation-gcd results are not
reproved here; the rotation-gcd theorem is unnecessary for this criterion.

For each t, the chronological word is the literal concatenation of
(OOEO)^{J_i} O^{H_i} E^{a_i(t)} for i=0,...,q. It is nonempty, has
exactly k_i odd letters and d_i(t) letters in row i, and has total
length N and odd-letter count K. In particular its closing tail a_q(t)
is included in d_q(t), N and the last map.

L020's compressed row offset is exactly F_i in (2). It is a positive
integer: its stated formula has positive summands, and the apparent
division by 11 is integral because 27^{J_i}-16^{J_i} is divisible by
11. The formal row map is (3^{k_i}n+F_i)/2^{d_i(t)}. Applying the
imported concatenation rule to these rows, the earlier denominators
contribute 2^{T_i(t)} and the later odd multipliers contribute 3^{U_i}.
Thus the full map and the source numerator are exactly

\[
W_t(n)=\frac{3^K n+\Phi(t)}{2^N},\qquad \phi=\Phi(t).
\tag{6}
\]

All weights and F_i are positive integers, so Phi(t)>0 is integral.
C077a's positive-Lambda tests give Lambda>0; consequently
2^N>3^K and Delta is a positive nonzero integer, independent of t.
These verify the source's qualifications without assuming an actual word.

### Match the normalized unshifted coordinate

First apply C077a to a feasible tuple with its attached allocations.
Only after its cyclic-order implication choose the position z of
indexed row 0. Its normalization preserves every endpoint, both cyclic
cuts and each own-input guard. Its support and cutoff conclusions then
give an integer t in S and a_i=a_i(t) at every indexed row, including q.
Write n_i=x_i-kappa. These are real coordinates at this point.

Use L077 (7)–(9), with the cutoff certificates from C077a. To avoid
confusing integer offsets with incoming products, denote those products
by P_i(t), not F_i. Explicitly,

\[
c_i(t)=3^{k_i}/2^{d_i(t)},\quad
P_i(t)=\prod_{j<i}c_j(t)=3^{\sum_{j<i}k_j}/2^{T_i(t)},
\]
\[
\eta_i=\kappa-\frac{12}{11}(16/27)^{J_i}
                    -(16/27)^{J_i}(2/3)^{H_i},\quad
R(t)=\sum_{i=0}^{q}\frac{\eta_i}{P_i(t)},\quad
D=2^N/3^K-1>0.
\tag{7}
\]

L077 gives n_{i+1}=c_i(t)(n_i+eta_i) at every edge and its unique
cyclic root n_0=R(t)/D. The exact row-coordinate calculation is

\[
3^{k_i}\eta_i
=\frac{23\,3^{3J_i+H_i}-12\,3^{H_i}16^{J_i}
                         -11\,2^{H_i}16^{J_i}}{11}=F_i.
\tag{8}
\]

The equality to F_i follows by expanding its two summands in (2);
the coefficient of 3^{H_i}16^{J_i} is -23/11+1=-12/11.
Thus the unshifted endpoint is precisely the formal row map used in
(6), rather than a map for the shifted coordinate x_i. More explicitly,
K-sum_{j<i}k_j=k_i+U_i, so every summand satisfies

\[
3^K\frac{\eta_i}{P_i(t)}
=F_i2^{T_i(t)}3^{U_i}.
\]

Summing all r terms gives 3^K R(t)=Phi(t). Since Delta=3^K D,
L077's unique root is n_0=R(t)/D=Phi(t)/Delta. C077a identifies
this n_0 with x_0-kappa=s_z-kappa. This proves the coordinate identity
in (5); the same fixed-point computation applies to each test t even
when it does not satisfy the J guards. No survivor feasibility follows.

### Apply the finite arithmetic hypothesis

The elementary integer divisibility criterion says that, for nonzero
integer Delta, Phi(t)/Delta is an integer exactly when Delta divides
Phi(t). The source fixed-point formula above is being specialized to
that criterion, not replaced by a new integrality theorem. Hypothesis
(4) makes n_0 nonintegral. If all original s_k-kappa were integers,
s_z-kappa would be an integer, contradicting (5).

For the sufficient modular certificate, Delta dividing Phi(t) would
force every divisor m_t of Delta to divide Phi(t), contrary to its
certified nonzero residue. This implication requires neither primality
nor a modular inverse of Delta. A common zero residue gives no verdict.
When evaluating F_i modulo a modulus sharing factors with 11, its
integral quotient must be computed before reduction or with a justified
lift; division by a nonunit is not licensed by (2). The source binary
recursion is an alternative exact evaluation. No modular computation
is performed or assumed successful here.

### Boundaries and scope

At r=3 there is one early row and the same three chronological weights
are retained. At B=0 the only pre-cutoff parameter is t=0; it needs
one arithmetic certificate when tau>0 and none when tau=0. At B=1,
the candidates are empty for tau=0, {0} for tau=1 and {0,1} for tau>1.
For general B, tau=1 leaves just {0}; tau=B>0 leaves 0,...,B-1;
tau>B leaves all 0,...,B. Thus no candidate is omitted merely because
the cutoff rejection range is empty. At t=B the final tail is 2 and
still occurs in the full word, its total length and its closing edge.
C077a's full cutoff test (4) remains required even when tau>B.

If S is empty, C077a would require an element of an empty set from
any feasible tuple, so none exists. Otherwise a single uncovered
candidate prevents use of this criterion. Failure of a chosen modular
test implies neither feasibility nor integrality. L056/L066 are
fixed-allocation precedents only; none of their residues is transferred
to a new table. Both rational witnesses and Attempts 026–031 remain
valid. No H guard, seed, minimum location, shifted integrality,
integer-realization converse, primitive/count-ray condition or
actual-word application has been introduced.

### Independent critical audit — 2026-10-18, step 297

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-17-variable-table-survivor-divisibility-critical-audit.md`.
This RESEARCH/REPRODUCTION audit found no defect in the conditional
criterion. It checks a local input; it supplies neither a stronger
theorem nor progress beyond the inspected affine/divisibility machinery.
The primary source import above is reused with its nonempty-word and
nonzero-denominator qualifications. No general coding theorem, rational
parity converse or rotation-gcd theorem is reproved or needed.

**Hypothesis matching.** C077a's table, integer budget and cutoff are
retained exactly, as are all of its independent order, support and
cutoff certificates. In particular its (4), which is L077 (3), applies
also when tau>B; only its (5) and associated constants are omitted then.
The support tests may be omitted only when B=0. The totals K,N here
are C077a (1), since sum_i a_i(t)=2r+18B for every test t. Integer
J_i,H_i and a_i(t)>=2 give positive integer row lengths and odd counts.
Thus the formal word is nonempty, and Lambda>0 implies
Delta=3^K(exp(Lambda)-1)>0 with Delta an integer. No actual orbit is
needed for this implication.

**Row offset and every chronological contribution.** The displayed
F_i is L020's offset C with J,H replaced by J_i,H_i. Its quotient by
11 is integral since 27 and 16 have equal residues modulo 11; both
summands are strictly positive. L020's unrelated actual-word and
least-root conclusions are not imported. The formal extension is
checked directly by (8): multiplying eta_i by 3^(3J_i+H_i) gives
coefficients 23/11, -12/11 and -1 on respectively
3^(3J_i+H_i), 3^H_i 16^J_i and 2^H_i 16^J_i. Expanding F_i gives
the same coefficients. Hence L077's pointwise recurrence is exactly
the formal row map, on real inputs as well as actual ones.

For fixed t, the contribution of row i's additive term to the final
unshifted output is

\[
\frac{F_i}{2^{d_i(t)}}\prod_{j>i}\frac{3^{k_j}}{2^{d_j(t)}}
=\frac{F_i2^{T_i(t)}3^{U_i}}{2^N}.
\]

Here the equality uses N=T_i(t)+d_i(t)+sum_{j>i}d_j(t), so no
current or later denominator is omitted. This verifies the application
of the imported concatenation rule term by term, rather than relying
on a count-only comparison. Row 0 contributes F_0 3^(K-k_0);
row q contributes F_q 2^(N-d_q(t)); every interior row has exactly
the two stated weights. At r=3 the three contributions are
F_0 3^(k_1+k_2), F_1 2^d_0 3^k_2 and F_2 2^(d_0+d_1).
The closing tail belongs to d_q(t) and N. Its absence from Phi(t)'s
earlier-prefix exponents is correct: appended even branches scale the
whole denominator, with no additive term. At t=B this remains true
with final tail 2. Positive F_i and integer weights prove Phi(t)>0
and integrality throughout the entire test interval.

**Root and cut.** Audited C077a supplies literal cyclic order before
choosing z, rotates each outgoing row with its own allocation and
input, and retains both cuts. Its support conclusion then identifies
every row tail with a_i(t), not merely their sum. Therefore L077's
incoming products C_i are exactly P_i(t), and its S(t) is R(t).
The positive denominator is D=Delta/3^K. For each individual index,
K-sum_{j<i}k_j=k_i+U_i and 3^k_i eta_i=F_i give
3^K eta_i/P_i(t)=F_i 2^T_i(t) 3^U_i. All r terms, including i=q,
are present. Thus the unique cyclic root is R(t)/D=Phi(t)/Delta
at n_0=x_0-kappa=s_z-kappa. No shifted integrality or old
chronological cut is substituted. L077's root formula does not require
passing J guards, so its use to define test roots for all 0<=t<=B
adds no feasibility assertion. Integrality of all original unshifted
inputs would include this particular input, which is all the
contradiction needs.

**Quantifiers and arithmetic.** Since B,tau are nonnegative integers,
S is empty exactly when tau=0. Otherwise S contains every integer
from 0 through min(B,tau-1). This checks B=0 (one candidate when
tau>0), B=1 (one or two), tau=1, tau=B>0 and tau>B without
discarding an endpoint. When tau=B=0 the empty case applies. All
these are necessary candidates, not claimed feasible tuples. For an
empty set C077a itself contradicts feasibility; otherwise each member
requires the additional nondivisibility premise. For integers Phi and
nonzero Delta, an integral quotient is equivalent to divisibility;
no coprimality or square-free assumption is needed. If m>1 divides
Delta, Delta dividing Phi would imply m divides Phi, so a nonzero
residue suffices even for composite m. A zero residue, including common
zero residues at several tested factors, yields no conclusion. The
proof's prohibition on dividing by a nonunit 11 or by Delta modulo a
certificate modulus is retained. There is no successful modular
evaluation asserted in this audit.

L020, L077 and C077a are exactly the direct mathematical inputs used;
the DAG needs no change. L056/L066 are only precedents, and Attempts
027/030 retain their uniform-prime and complete-cancellation stops.
The broader preserved Attempts 026–031 and both rational witnesses
are not contradicted by an implication with independent arithmetic
hypotheses. No new table, survivor certificate, survivor feasibility,
actual-word application or universal eventual descent has been proved.

## Mathlib

Full matching Mathlib coverage is **not checked**. Integer divisibility,
finite sums/products and formal affine identities would be supporting
results, not a matching theorem for this conditional variable-table
criterion. No Mathlib absence or formal verification is claimed.
