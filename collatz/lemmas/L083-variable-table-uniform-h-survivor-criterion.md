# L083 — Variable-table uniform own-input H-survivor criterion

## Hypotheses

Assume **all** simultaneous hypotheses and independent O, S and C data
tests of C077a for the same indexed table and budget. In particular
r>=3, B>=0 and tau>=0 are integers, the J_i are strictly increasing
integers at least 2, and the H_i are arbitrary integers at least 3.
Retain the full support tests when B>0, the cutoff boundary tests when
tau<=B, and the unconditional cutoff tests even when tau>B. Constants
in those three packages need not agree with one another or with the
additional constants below. All logarithms are natural.

Put p=r-2, q=r-1, kappa=23/11. Use C077a's last-pair test allocations
a_i(t)=2 for i<p, a_p(t)=2+18t and a_q(t)=2+18(B-t),
for integers 0<=t<=B, and L077's c_i(t), C_i(t), eta_i and
Lambda=N log2-K log3. Thus C_0(t)=1 and C_r(t)=exp(-Lambda).
The survivor set is the integer range 0<=t<=B, t<tau.

If tau=0, impose no further data tests. Otherwise put

\[
m=\min(B,\tau-1),\qquad
A_i=\sum_{j<i}(3J_j+H_j),\qquad
D_i^0=\sum_{j<i}(4J_j+H_j+a_j(0))\quad(0\le i\le q).
\tag{1}
\]

Choose positive rational lambda_H,L_0,...,L_q,Q,U, rational T,u,
and positive rational ell, with certified inequalities

\[
0<\lambda_H\le\Lambda,\qquad
0<L_i\le C_i(m)\ (0\le i\le q),\qquad
Q\ge\kappa\sum_{i=0}^{q}\frac1{L_i},
\tag{2}
\]
\[
L_*:=\min_{0\le i\le q}L_i,\qquad
\frac{Q}{\lambda_H}+Q+\frac{\kappa}{L_*}
\le U\le\exp(T),\qquad
0<\ell\le\log2,\quad\log3\le u.
\tag{3}
\]

These are finite table-data tests. Prefix lower bounds may be exact
rational comparisons or certified lower bounds proved from the table;
they do not assume C_i>=1 or growth of either varying-tail map.
Only incoming indices 0,...,q occur in (2), never the closing C_r.
Define the rational numbers

\[
F_i=T+(A_i+3J_i)u-(D_i^0+4J_i+H_i)\ell
\quad(0\le i\le q).
\tag{4}
\]

For the exclusion conclusion require F_i<=0 for at least one indexed
row i. No unknown root, guard verdict, minimum or seed occurs in
these tests. The choice (2)–(4) is an additional sufficient condition,
not a claim that every table satisfies it.

## Conclusion

For tau>0, every integer survivor's unique cyclic endpoint root has
positive shifted inputs and, uniformly at every incoming index,

\[
\log s_i(t)<T+\log C_i(t),\qquad
\log s_i(t)+J_i\log(27/16)-H_i\log2<F_i.
\tag{5}
\]

Consequently, if a row passes F_i<=0, every survivor fails that row's
own-input **strict** H guard. Under these sufficient tests there is
no endpoint/domain/J/H real tuple for the table, in any cyclic order
and over the full nonnegative integer allocation simplex of budget B.
For tau=0 this exclusion follows already from C077a, with no H test.
In particular any full L051 system with these chronological rows is
infeasible; its extra minimum, seed and count requirements are unused.

The criterion recovers C082a's changed-table exclusion with one uniform
certificate for t=0,1 and exactly the same row18 upper margin
-457745289/50000000000. With the original table the same cap gives
F_i>0 at all 25 rows, so this sufficient test rejects neither L055's
t=0 witness nor L065's t=1 witness. More generally the sound implication
cannot exclude a table containing either matching feasible tuple.
Failure of the sufficient tests gives no feasibility verdict.

This is local RESEARCH/REPRODUCTION within the prior SPECIALIZE assessment
`drafts/literature/2026-10-18-variable-table-uniform-h-survivor-test.md`.
It extends the inspected affine/normalized-cap mechanism to a variable
table and whole survivor range; no originality beyond inspected sources
is claimed. The separate critical audit below found no defect. It establishes no
new-table certificate beyond the already excluded benchmark, survivor
feasibility, integer/parity/exact-valuation/primitive realization,
unrestricted cycle exclusion or universal eventual descent.

## Proof

### Imported formulas and uniform incoming data

For the cap proof suppose tau>0; the empty tau=0 case is treated below.
Import L077 (8)–(10), under the unconditional C077a cutoff tests.
For every 0<=t<=B the cyclic endpoint solution is unique, all n_i(t)>47,
and, writing n_i=s_i-kappa,

\[
D=\exp(\Lambda)-1>\Lambda\ge\lambda_H>0,\qquad
S(t)=\sum_{j=0}^{q}\frac{\eta_j}{C_j(t)},\qquad
n_0(t)=S(t)/D,
\]
\[
n_i(t)=C_i(t)\left(S(t)/D+
                       \sum_{j<i}\eta_j/C_j(t)\right),
\qquad 0<\eta_j<\kappa.
\tag{6}
\]

The finite-word affine input is Halbeisen–Hungerbuehler, *Optimal bounds
for the length of rational Collatz cycles*, Acta Arithmetica 78 (1997),
227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Our integer rows define a finite nonempty formal word with lengths K,N;
C077a supplies positive Lambda and hence a nonzero denominator.
L077 already proves the needed coordinate specialization and includes
the final varying tail in closure. We use its formal real affine
formulas, without a parity-realization converse or a coding reproof.

Reuse the positive-real logarithm/exponential and remainder coverage
recorded in the prior assessment: [DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19).
The strict exp(Lambda)-1>Lambda in (6) is already justified in L077.
No source's rotation-minimum theorem is used to bound a specified input.

Suppose tau>0. Every survivor satisfies 0<=t<=m. L077's explicit
prefix formulas give C_i(t)=C_i(0) for i<=p and
C_q(t)=C_q(0)2^(-18t). Thus, including the final varying input,

\[
C_i(t)\ge C_i(m)\ge L_i>0\qquad(0\le i\le q).
\tag{7}
\]

The closing prefix C_r is deliberately excluded; its value is
exp(-Lambda)<1 and is already retained in (6). By eta_j<kappa,
the **complete** finite sum satisfies
0<S(t)<kappa sum_j 1/L_j<=Q. Every partial sum in (6) is nonnegative
and strictly less than Q, including the empty one. Hence

\[
0<\frac{s_i(t)}{C_i(t)}
=\frac{S(t)}D+\sum_{j<i}\frac{\eta_j}{C_j(t)}
                    +\frac{\kappa}{C_i(t)}
<\frac{Q}{\lambda_H}+Q+\frac{\kappa}{L_*}
\le U\le e^T.
\tag{8}
\]

All terms are positive where divided or logged. Taking logarithms
proves the first part of (5), for every incoming input. No minimum
location, seed, J/H guard or growth of a varying row was assumed.

### Uniform own-input H margin

For incoming i<=p the denominator exponent is D_i(t)=D_i^0;
for i=q it is D_q(t)=D_q^0+18t. These exhaust all incoming indices.
Therefore D_i(t)>=D_i^0, while the numerator exponent A_i is fixed.
Using (8) with that row's own parameters gives

\[
\begin{aligned}
\log s_i(t)+J_i\log(27/16)-H_i\log2
&<T+(A_i+3J_i)\log3
           -(D_i(t)+4J_i+H_i)\log2\\
&\le T+(A_i+3J_i)\log3
           -(D_i^0+4J_i+H_i)\log2\le F_i.
\end{aligned}
\tag{9}
\]

The coefficients A_i+3J_i and D_i^0+4J_i+H_i are positive, so
the directions of u and ell in the final comparison are correct.
The first inequality is strict, so F_i=0 also rejects the required
strictly positive H margin. This proves (5) without evaluating any
root-failure predicate. One fixed row suffices for all survivors;
the criterion need not identify every failed guard or every feasible root.

### All orders, full allocations and boundary cases

If an endpoint/domain/J/H tuple exists, temporarily forget only its
H guards. C077a, with all its independent tests retained, normalizes
at the unique input of indexed row 0. It gives literal cyclic order,
zero early allocation and an integer survivor t. For tau=0 this is
already impossible. Otherwise use (9) at a row with F_i<=0.

In detail, let z be the old position of indexed row 0, rho_i=(z+i)
mod r for i<r, rho_r=z and x_i=s_(rho_i). Each indexed outgoing
pair and its tail remains attached to x_i. The edge at old input
r-1 uses s_r=s_0 and becomes edge i=r-1-z. The new closing edge
i=r-1 is the old edge z-1 modulo r; the cuts coincide when z=0.
All endpoints, lower domains and own-input inequalities thus persist.
In particular each old H guard becomes
0<log x_i+J_i log(27/16)-H_i log2 at the same outgoing row.
Endpoint uniqueness in (6) identifies x_i with s_i(t). Equation (9)
contradicts that strict H guard. Neither a minimum nor a seed is
transported or needed. Repeated values are still input occurrences.

When B=0 and tau>0, m=0 and the same proof covers the single survivor;
C077a omits only its specified support tests. When tau>B, m=B and
the final-tail-2 endpoint is included, while C077a omits only its
specified boundary tests. Tau=1 gives m=0; r=3 gives p=1,q=2
and leaves every sum and incoming-index argument intact. Empty
survivor ranges require no additional H test. A full L051 system
contains the excluded subsystem, regardless of its extra requirements.

### Changed and original benchmark certificate

For L079's changed table choose r=25, B=9250245, tau=2, m=1 and
lambda_H=10584/10^14. Import its complete independent O/S/C tests.
Take

\[
L_0=1,\quad L_i=10^8 2^{i-1}\ (1\le i\le24),\quad
Q=\frac{23}{11}(1+2/10^8),\quad L_*=1,\quad
U=20000000000,\quad T=24,
\]
\[
\ell=693147180559/10^{12},\qquad
u=1098612288669/10^{12}.
\tag{10}
\]

Here C_0(m)=1 and c_0=3^63/2^73>10^8. Incoming rows 1,...,22
have tail 2 and multiplier at least 19683/8192>2. Row23 at m=1
has tail 20; its own J>=8,H>=39 give multiplier at least
3^63/2^91>2. Thus (7)'s required L_i bounds hold through i=24,
including that changed row, without a tail-2 estimate for it. The
finite geometric sum of inverse L_i is strictly below 1+2/10^8.
Both changed closing tails remain in N=630138897, K=397573379.

Exact rational analytic checks certify lambda_H<Lambda,
ell<log2, log3<u and

\[
\frac{Q}{\lambda_H}+Q+\kappa
=\frac{435606069410390910013}{22050000000}
<20000000000<\sum_{k=0}^{40}\frac{24^k}{k!}<e^{24}.
\tag{11}
\]

Use the previously assessed rational remainder scheme: for x=2,3,
z=(x-1)/(x+1), take the first 100 terms
2 sum_(k=0)^99 z^(2k+1)/(2k+1), with upper remainder
2z^201/(201(1-z^2)). Its positive-real domain holds, and the certificate
retains both large coefficients N,K and all errors. No general analytic
theorem is reproved. Fresh prefix summation gives A_18=6078923,
D_18^0=6862840. With J_18=693015,H_18=3295208, (4) becomes

\[
F_{18}=24+8157968u-12930108\ell
=-457745289/50000000000<0.
\tag{12}
\]

This is one uniform sufficient certificate recovering C082a's two
exclusions. L081/L082's separate single-root proofs are comparisons,
not assumptions licensing a general cap.

For the original L055 table, the same counts, lambda_H and all
constants (10) apply to the incoming-cap calculation; c_0 becomes
3^64/2^74>10^8. Its row23 floor is unchanged. Fresh summation in
(4) gives F_18=39631020233/100000000000>0, and every other F_i
is positive too. No original row passes this sufficient rejection test
for either survivor. This is consistent with the full positive witnesses
in L055 and L065; their feasibility is imported, not recertified here.
Even with different certificate constants, (9) shows that a feasible
matching survivor with positive H margins precludes any F_i<=0.
Attempts 026–031 and the arithmetic diagnostics remain unchanged.

Reproduce with
`python3 scripts/postspell-word-count/certify_variable_table_uniform_h.py`.
Full rows, all incoming exponents at t=0,1, rational lower bounds,
complete log and exp terms, coefficients, 146 exact comparisons and
their differences are in
`scripts/postspell-word-count/variable-table-uniform-h-certificate.json`.
All certification checks pass; the negative H margin is a mathematical
guard failure, not a failed certification check. The universal implication
is the proof (6)–(9); the finite calculation verifies only its benchmarks.

### Independent critical audit — 2026-10-19, step 333

This RESEARCH/REPRODUCTION proof audit uses the unchanged SPECIALIZE
assessment `drafts/literature/2026-10-18-variable-table-uniform-h-critical-audit.md`.
It found no defect in the conditional statement, its uniform proof or its
two benchmark checks. This is verification of a local input, not a new
table exclusion or progress beyond the inspected source machinery.

**Hypotheses and fixed-point identity.** Every O/S/C test of C077a is
still assumed, with independent constants. Its cutoff tests (4) hold
even if tau>B; only its specified boundary tests may then be omitted.
Thus the invocation of L077's domain/uniqueness assertion is licensed
for every parameter, irrespective of whether any J or H guard holds.
In unshifted coordinates its recurrence is n_(i+1)=c_i(n_i+eta_i).
Dividing by C_(i+1)=c_i C_i gives
n_(i+1)/C_(i+1)=n_i/C_i+eta_i/C_i. Summing and imposing
C_r=exp(-Lambda) and n_r=n_0 gives n_0=S/(exp(Lambda)-1).
This checks the incoming index in (6): the summand is eta_i/C_i,
including i=q, not eta_i/C_(i+1). The closing multiplier remains
in the denominator. The finite-word input and analytic citations are
those explicitly given above; their already assessed hypotheses suffice.
No general coding reproof, parity converse or minimum theorem is used.

**Uniform inequalities.** If tau>0, integrality gives exactly
0<=t<=m=min(B,tau-1). The incoming product for i<=p uses only
unchanged rows less than p. For i=q it includes row p's additional
18t halvings, so C_q(t)=C_q(0)2^(-18t). Consequently all incoming
C_i(t)>=C_i(m)>=L_i. The final outgoing row's compensating tail
does not enter any incoming prefix; it restores the fixed full product.
Since every eta_i is strictly between zero and kappa and there are
finitely many positive summands, 0<S(t)<kappa sum 1/L_i<=Q.
Every proper partial sum, including zero at i=0, is less than Q.
Also D=exp(Lambda)-1>Lambda>=lambda_H>0. Therefore the first two
terms of s_i/C_i in (8) have strict upper bounds Q/lambda_H and Q;
the third is at most kappa/L_i<=kappa/L_*. This proves the strict
cap even when later rational inequalities or U<=exp(T) are equalities.
No C_i>=1 assumption was used in this general proof.

The exponent D_i(t) equals D_i^0 for i<=p and D_q^0+18t for i=q.
Thus replacing it by D_i^0 increases the H upper bound, since log2>0.
Both remaining coefficients in (9) are positive, licensing upper u
and lower ell without a reversal. The strict normalized cap persists
through the non-strict rational comparisons, so F_i=0 also contradicts
the required strictly positive H margin. These observations separately
check both uses of the final input: its lower prefix uses t=m while
its H upper expression uses t=0. No monotonicity of a varying map or
of the whole H margin is being presumed.

**Normalization and boundaries.** Under an alleged feasible all-order
tuple, C077a is applied first to its endpoint/domain/J subsystem. It
supplies literal cyclic order and the integer survivor range, without
assuming feasibility of any survivor. Only then is indexed row 0
placed at the new cut. With rho_i=(z+i) mod r, the entire outgoing
row, tail and input move together. The old closing edge becomes
i=r-1-z and the new closing edge starts at old z-1 modulo r.
At z=0 they coincide; at z=r-1 the old closing edge becomes the first
edge. Every H guard therefore has exactly its original own input,
including both boundary occurrences. Endpoint uniqueness identifies
these normalized values with (6). A strictly negative upper H bound
then contradicts that same row's strict guard. Repeated values remain
distinct occurrences, and no minimum or seed is asserted invariant.

For r=3, p=1,q=2, the unchanged incoming range is {0,1} and the
one varying incoming prefix is C_2; every displayed sum is defined.
For B=0 the only possible t is zero; tau>0 gives m=0 and requires
all additional H tests, while tau=0 excludes the empty survivor range
using C077a alone. For B=1, tau=1 leaves only zero and tau>1 leaves
at most zero and one. In general tau=1 gives m=0; tau=B>0 excludes
t=B by the cutoff and leaves m=B-1; tau>B gives m=B and includes
the final-tail-2 allocation. Its domain follows from L077, not from
growth across that tail. None of these conditional cases asserts that
the data tests can all hold for an arbitrary table. For tau=0 the H
constants and logarithms of hypothetical roots are never invoked.

**Complete independent finite evidence.** Reproduce with
`python3 scripts/postspell-word-count/audit_variable_table_uniform_h.py`.
It reads the construction certificate without importing or executing
the constructor and writes
`scripts/postspell-word-count/variable-table-uniform-h-audit-certificate.json`.
It separately transcribes all 25 L055 pairs, verifies the source table
and hash, changes exactly the two stated H entries and independently
reconstructs every mathematical certificate field. It traverses all
200 stored logarithm terms, both remainders and endpoints, all 41
exponential terms, both complete 25-row tables and incoming-prefix
arrays, and all 146 named comparisons with their operands, differences
and verdicts. The result is 2387 checks with no failures. The stored
success flags are compared only after fresh arithmetic has checked
the actual inequalities. The construction certificate remains unchanged.

The analytic audit generates successive powers and exponential terms
by recurrence. For 0<z<1, the positive omitted logarithm terms start
at exponent 201; replacing their denominators by 201 bounds their sum
by 2z^201/(201(1-z^2)), strictly since later denominators are larger.
Positive omitted terms make the lower enclosure strict as well. For
exp(24), all omitted terms beyond degree 40 are positive. These facts
justify every exact rational comparison, not just agreement with the
constructor. With positive N and K, the Lambda lower bound uses the
lower log2 and upper log3, and its upper bound uses the opposite
choices. As a second evaluation, 120-term intervals [a,b] for log2
and [c,d] for log(3/2), using z=1/3 and z=1/5, give
(N-K)a-Kd<Lambda<(N-K)b-Kc. Both endpoints lie strictly within
the construction's interval and between lambda_H and 10585/10^14.
All terms, amplified errors and exact endpoints are retained on disk.

The row-0 multipliers are freshly checked as 3^63/2^73 and
3^64/2^74, both exceeding 10^8. For rows 1 through 22 the checked
J>=2,H>=3 and actual tail 2 give multiplier at least 19683/8192>2.
For row23 at m=1, the checked J>=8,H>=39 and actual tail 20 instead
give at least 3^63/2^91>2. Induction thus proves all 25 incoming
lower bounds, including L_24, without computing enormous powers.
Their entire reciprocal sum is
1+(2/10^8)(1-2^(-24))=167772163355443/167772160000000.
It yields precisely the strict normalized cap in (11), below U and
the degree-40 exponential lower sum. The closing exponents at both
t=0 and t=1 are separately checked to be N, and the total odd exponent
is K; neither changing tail is lost.

Independent prefix sums for the changed table at row18 give
A=6078923, D^0=6862840 and H coefficients 8157968 and 12930108.
They reproduce F_18=-457745289/50000000000<0. For the original
table the corresponding prefix exponents and coefficients each
increase by one where appropriate, giving
F_18=39631020233/100000000000>0. Every original F_i is positive
under fresh exact evaluation; no original row passes rejection.
These are upper tests, so positive F_i alone does not prove feasibility.
The positive witnesses are imported with their precise allocations
from audited L055 and L065. L079 supplies the already audited complete
O/S/C tests for the changed table; L081/L082 and C082a are comparison
benchmarks, not extra premises of this uniform proof. Attempts 026–031
remain valid, and no stopped arithmetic route has been reopened.

The DAG's direct inputs remain accurate. This audit changes no argument,
so PROOF.md and the DAG are unchanged. Arbitrary-table coverage,
integer/parity/exact-valuation/primitive realization, unrestricted cycles,
divergence and universal eventual descent remain unresolved.

## Mathlib

Full matching coverage for this variable-table sufficient criterion has
not been checked. Supporting real exponential, logarithm and finite-sum
facts do not constitute a full matching theorem. Unknown coverage is
not evidence of absence. No Lean verification is claimed.
