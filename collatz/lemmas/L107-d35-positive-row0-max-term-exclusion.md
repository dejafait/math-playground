# L107 — Positive-row0 full-simplex maximum-term exclusion

## Hypotheses

Use L055's literal chronological25-row J,H table, changing only H0=5
and H24=32670656. Let B=9250245 and kappa=23/11. Take any integers

\[
b_i\ge0\ (0\le i<25),\qquad \sum_{i=0}^{24}b_i=B,
\qquad b_0\ge1,\qquad a_i=2+18b_i.
\tag{1}
\]

Set G_i=(27/16)^{J_i}(3/2)^{H_i},
Q_i=(12/11)(3/2)^{H_i}+1 and g_i=(4/11)2^{4J_i}.
The real endpoint system whose necessary relaxation is tested is

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa\quad(0\le i<25),
\qquad s_{25}=s_0,\qquad s_i\ge540/11,
\qquad s_i\ge g_i.
\tag{2}
\]

The last inequalities are exactly the non-strict own-input J guards
4J_i log2<=log s_i+log(11/4). The own-input H guards are explicitly
omitted. There is no minimum-junction, seed, integer/residue junction,
exact valuation, actual-word realization or primitive-period premise.
Repetitions and every closing-tail2 allocation allowed by (1) are retained.
All logarithms below are natural; cyclic subscripts are modulo25.

## Conclusion

The25-guard,25-summand maximum-term necessary relaxation (8) below is
infeasible on the entire integer simplex (1). Consequently (2) is
infeasible, and adding its omitted H guards cannot restore feasibility.

This is a support-wide exclusion, with no support enumeration: for
every allocation, one of the original inputs r in{1,...,24} has a
largest numerator term M_r satisfying

\[
M_r<\frac{46}{11},\qquad
\frac{D(g_r-\kappa)}{25}
 >\frac{4611686018427387881}{2750000000000}>10^6.
\tag{3}
\]

These incompatible bounds refute the necessary relaxation, not merely
one selected maximum branch. The index r can depend on the allocation.

This is a local RESEARCH/POTENTIALLY_NEW result under the invocation-start
EXPLORE assessment
`drafts/literature/2026-10-26-positive-row0-max-term-feasibility-test.md`.
The finite-affine and finite-sum inputs are known mathematics. The label
means the assessed search did not establish coverage of this literal
coupling verdict; it does not certify originality. The separate critical
audit below validates this construction without repair. It supplies no actual-word transfer,
arbitrary-order exclusion, entry or divergence argument, or universal
descent, and is not a candidate complete solution of Collatz.

## Proof

### Allocation-independent denominator and one common tuple

Write

\[
p_i=3J_i+H_i,\quad q_i^0=4J_i+H_i+2,\quad
c_i=\frac{3^{p_i}}{2^{q_i^0+18b_i}},\qquad
\eta_i=\kappa-(16/27)^{J_i}\bigl(12/11+(2/3)^{H_i}\bigr).
\tag{4}
\]

Every J_i>=8 and H_i>0. Thus the two factors in the subtraction are
positive, (16/27)^{J_i}<1/2 and 12/11+(2/3)^{H_i}<kappa.
It follows that kappa/2<eta_i<kappa, in particular eta_i>1. This is
the tail-independent estimate in L106, applicable unchanged here.
The finite comparison 2*16^8<27^8 verifies the only power bound needed.

The H changes cancel in the sum. L055's literal table and (1) give

\[
\sum J_i=66061058,\quad \sum H_i=199390205,\quad
\sum a_i=50+18B=166504460,
\]
\[
K:=\sum p_i=397573379,\quad
N:=\sum(q_i^0+18b_i)=630138897.
\tag{5}
\]

Therefore these are the identical operands in L104's audited enclosure,
which may be imported for every allocation in (1):

\[
0<\lambda_-:=10584/10^{14}<\Lambda:=N\log2-K\log3
 <\lambda_+:=10585/10^{14}<1.
\]

Put P=product_i c_i=3^K/2^N=exp(-Lambda), and
D=P^{-1}-1. The positive-real exponential bounds used in L104 and
L106 give

\[
D>\lambda_->10^{-10},\qquad
0<D<\delta:=\frac{\lambda_+}{1-\lambda_+}
 =\frac{2117}{19999999997883}<\frac1{100},
\qquad P^{-1}=1+D<\frac1{1-\lambda_+}<2.
\tag{6}
\]

Here exp(x)>1+x and exp(x)<=1/(1-x) apply at 0<x=Lambda<1.
No fixed-allocation cap, minimum or seed from L104 is imported.

For completeness, specialize the finite-affine formula underlying
L055 and L106 to the changed allocations, rather than importing their
fixed tuples. Define C0=1, C_i=product_(j<i)c_j, and
S_i=sum_(j<i)eta_j/C_j. Set
n0=S25/D, n_i=C_i(n0+S_i), s_i=n_i+kappa.
Then C_(i+1)=C_i c_i and S_(i+1)=S_i+eta_i/C_i imply
n_(i+1)=c_i(n_i+eta_i) at all original indices. Since C25=P and
S25=Dn0, n25=P n0(1+D)=n0 exactly.
Also c_i=2^{-a_i}G_i and eta_i=kappa-Q_i/G_i, so substituting
s_i=n_i+kappa gives every endpoint in (2), including row24 to row0.
Conversely composing any such closed endpoint tuple gives
n0=P(n0+S25), hence this unique n0 and the same full tuple.

This is precisely a local specialization of the finite-affine
composition/fixed-point input: Halbeisen and Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica78 (1997),227–239, DOI10.4064/aa-78-3-227-239,
[section2, equations(2)–(4), Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The assessed real affine formula is used; its odd-denominator rational
cycle interpretation supplies no junction integrality or word realization.
The preceding algebra checks the changed block coefficients and common
tuple, without a new general parity-coding reproof.

For each original cut i put P_(i,0)=1 and
P_(i,k)=product_(h=0)^(k-1)c_(i+h). Dividing the recurrence by its
prefix and summing one traversal yields, on that same tuple,

\[
n_i=\frac{\mathcal B_i}{D},\qquad
\mathcal B_i=\sum_{k=0}^{24}T_{i,k},\qquad
T_{i,k}=\frac{\eta_{i+k}}{P_{i,k}}>0.
\tag{7}
\]

Indeed the composed equation is n_i=P(n_i+mathcal B_i), whose
unique solution is (7). This proves L106's equation(9) specialization
for every allocation, with no independently selected roots at other
cuts. Its k=0 term eta_i>1 and (6) also give n_i>100, so every
constructed endpoint already has s_i>100+kappa>540/11. The lower
domains are thus accounted for without using a guard.

### Exact25-by25 necessary alternatives, with the shift retained

Since g_i>=g_0=(4/11)2^32>kappa, the positive threshold g_i-kappa
can be logged. Put M_i=max_(0<=k<25)T_(i,k). Import the finite real
maximum bound
max x_k<=log(sum exp x_k)<=max x_k+log25 from Blanchard,
Higham and Higham, *Accurate Computation of the Log-Sum-Exp and
Softmax Functions*, MIMS EPrint2019.16, author version2019-09-08,
[section4, equations(4.1)–(4.2), printed p.8](https://eprints.maths.manchester.ac.uk/2728/1/paper.pdf).
Its hypotheses hold for the25 finite real numbers x_k=log T_(i,k);
ties are allowed. In particular mathcal B_i<=25M_i. Therefore
the non-strict J guard in (2), by (7), necessarily implies

\[
M_i\ \ge\ R_i:=\frac{D(g_i-\kappa)}{25}
\quad(0\le i<25).
\tag{8}
\]

Equivalently max_k log T_(i,k)>=log D+log(g_i-kappa)-log25.
The shift kappa is subtracted exactly before applying the25-term bound;
it is not counted as an extra term or dropped. This is a necessary
relaxation; no converse or equivalence to the summed guards is asserted.

Here are all the alternatives in exact coefficient form. For each i,k
let j=(i+k) mod25, let I_(i,k) be the k consecutive row indices starting
at i, and put
A_(i,k)=sum_(h in I)p_h, E_(i,k)=sum_(h in I)q_h^0, and
U_(i,k)=sum_(h in I)b_h. Empty prefixes have all three sums zero.
Then

\[
\log T_{i,k}=\log\eta_j+
  (E_{i,k}+18U_{i,k})\log2-A_{i,k}\log3.
\tag{9}
\]

For each i, (8) requires at least one of these25 affine expressions
to be at least its stated threshold, on the *same* budget vector b.
Equation(9) defines all625 expressions including every wrapping prefix.
The certificate stores their full integer operands and budget coefficient
vectors. The proof below cancels the common products symbolically;
no floating-point log coefficients, numerical optimization or branch
sampling is needed. The only numerical transcendental enclosure used is
the audited (6), after exact matching of (5).

### One finite-prefix minimum covers all alternatives

Select an index r minimizing the25 positive numbers C0,...,C24;
a finite minimum exists and ties require no uniqueness. By H0=5,
J0=8 and b0>=1,

\[
C_1=c_0=\frac{3^{29}}{2^{39+18b_0}}
 \le\frac{68630377364883}{144115188075855872}<1=C_0.
\tag{10}
\]

Consequently r cannot be0, and the literal table gives J_r>=15.
This is a derived minimum of cumulative coefficients, not an assumed
minimum of junctions, an imposed seed or a rotation of the guards.

For any of the25 terms at cut r, put j=(r+k) mod25. If r+k<25,
the prefix product is C_j/C_r. If r+k>=25, it is P C_j/C_r:
the path first goes from r through the actual closing row24 to0,
then from0 to j. Thus, with w=0 or1 for these cases,

\[
P_{r,k}^{-1}=\frac{C_r}{P^w C_j}\le P^{-w}\le P^{-1}.
\tag{11}
\]

The first inequality uses C_r<=C_j, and the last uses 0<P<1.
Both cases include their endpoints: k=0 uses C_r/C_r=1, and
k=24 retains all24 traversed rows. The full25-row product P is
already in D and has not been discarded. Since every eta_j<kappa,
(6),(11) yield

\[
M_r<\kappa P^{-1}<2\kappa=46/11.
\tag{12}
\]

On the other hand J_r>=15 and D>10^-10 give

\[
R_r>\frac{10^{-10}}{25}
       \left(\frac4{11}2^{60}-\frac{23}{11}\right)
 =\frac{2^{62}-23}{275\cdot10^{10}}
 =\frac{4611686018427387881}{2750000000000}.
\tag{13}
\]

Its excess over46/11 is exactly
4611674518427387881/2750000000000>0. Thus M_r<R_r, contradicting
the necessary non-strict inequality (8). Every b satisfying (1) has
such an r, so this covers the complete simplex and every possible
maximum-term branch. No claim of infeasibility is inferred from a failed
numerical search, a single witness or one selected support.

### Verification and qualifications

Run `python3 scripts/postspell-word-count/certify_d35_positive_row0_max_term.py`.
The full certificate is
`scripts/postspell-word-count/d35-positive-row0-max-term-certificate.json`.
It parses the canonical literal table, applies only the two H changes,
matches K,N, records all625 exact prefix exponent/budget vectors and
checks their nonwrap/wrap identities. It covers each possible minimum
r=1,...,24 and all25 terms there, and records the full rational caps,
required lower bounds, and positive differences. It passes2699 finite
checks with no failures, zero allocation samples and no floating-point
operations. The critical bound is (12) versus (13), not the check count.
The finite-minimum and common-tuple arguments above supply the universal
coverage; the certificate does not purport to prove those arguments by
sampling. This is construction verification, not an independent audit.

The analytic inequalities and audited enclosure are imported from L104
and L106 with unchanged positive-real hypotheses; their assessed source
coverage includes [NIST DLMF4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.5.8–4.5.11](https://dlmf.nist.gov/4.5), recorded version1.2.8.
The finite-sum result is cited above, rather than reproved or presented
as a new theorem. No standard geometric-programming feasibility claim
or local solver certificate is used.

L105's triangle and L106/C106a's fixed-allocation evidence remain valid
and are not feasibility premises here. Attempt032/033/034 are not global
bans and are preserved. This result concerns b0>0 in this one literal
table/order only. Combining it with a b0=0 exclusion, applying it to
actual words and critically auditing those later steps are not done here.

### Independent critical audit — 2026-10-26, step515

This is RESEARCH/REPRODUCTION under the unchanged, separately approved
SPECIALIZE assessment
`drafts/literature/2026-10-26-l107-max-term-exclusion-critical-audit.md`.
The entire statement and proof, construction script and complete relevant
certificate data were checked. No mathematical defect was found; the
hypotheses, conclusion and argument (1)–(13) are retained. This establishes
an audited local input, not a further theorem beyond the construction
or a claim of originality beyond the inspected sources.

First, the literal table was independently transcribed and compared with
L055. Exactly H0-=35,H24+=35 were applied. For arbitrary budgets (1),
the resulting sums are K=397573379 and N=630138897, including the total
18B contribution. Thus L104's audited logarithm enclosure concerns the
identical real number Lambda for every allocation. Its proof and audit
were inspected; its fixed-allocation endpoint cap is not used. The
positive-real exponential comparisons imply precisely (6), with the
strict lower bound on D and strict upper bound on P^-1 required here.
The complete saved rational bounds and differences match these operands.
The already audited logarithm computation was not rerun.

Second, direct substitution gives
n_(i+1)=c_i*n_i+c_i*kappa-2^(-a_i)*Q_i
=c_i(n_i+eta_i). All c_i are positive, and the literal J,H values give
1<kappa/2<eta_i<kappa. For any original cut i, let z_k=n_(i+k) and
P_k=P_(i,k), with the cyclic identification z25=z0. Dividing each
recurrence by P_(k+1)=P_k*c_(i+k) gives

\[
\frac{z_{k+1}}{P_{k+1}}-\frac{z_k}{P_k}
 =\frac{\eta_{i+k}}{P_k}.
\]

Summing all25 equations gives D*z0=mathcal B_i because P25=P.
It is therefore the same closed tuple that obeys every formula (7).
Conversely the prefix formula preceding (7) satisfies every endpoint
and n25=P*n0*(1+D)=n0; D>0 makes the root unique. There are no separate
choices of roots at the different cuts. The k=0 summand and D<1/100
give n_i>100 and hence all lower domains. No guard is needed for that
fact, and no logarithm is taken at a nonpositive argument.

Third, write the guard comparison without logarithms:

\[
s_i\ge g_i\quad\Longrightarrow\quad
D(g_i-\kappa)\le\mathcal B_i\le25M_i.
\]

The first inequality uses D>0 and the exact shift; the second is the
cited25-term maximum bound applied to25 finite positive terms. Thus (8)
has the necessary direction and is non-strict. Neither a converse nor
independent allocation choices for its25 rows are used. Equation(9)
is precisely the logarithm of each term for the shared budget vector.

Finally select any minimum of C0,...,C24. The table gives
c0<=3^29/2^57<1, excluding index0 even if other minima tie. No C25
minimum or minimum-junction premise is needed. In the nonwrapping case
P_(r,k)=C_j/C_r; in the wrapping case it is P*C_j/C_r, because row24
is traversed before index0. Since C_r<=C_j and 0<P<1, both reciprocal
prefixes are at most P^-1. This includes k=0 and k=24 without dropping
the closing row. All25 terms are strictly less than kappa/P, so their
finite maximum is also strictly less than kappa/P<46/11. Every possible
r=1,...,24 has its own J_r>=15. Equation(13) therefore gives

\[
R_r>\frac{4611686018427387881}{2750000000000}>10^6,
\qquad
R_r-\frac{46}{11}>
\frac{4611674518427387881}{2750000000000}>0.
\]

This contradicts M_r>=R_r on every allocation in (1). Choosing r does
not rotate the chronological J,H labels or assume a distinguished
junction. The proof uses b0>=1 only to exclude index0 and uses the other
budgets through their total and the shared products. It imposes no
condition b24>0, so closing tail2 remains covered, as do repetitions.

Run `python3 scripts/postspell-word-count/audit_d35_positive_row0_max_term.py`.
The full independent certificate is
`scripts/postspell-word-count/d35-positive-row0-max-term-audit-certificate.json`.
It incrementally walks all625 cyclic prefixes and independently compares
their exponent pairs, every symbolic budget coefficient and their
nonwrap/wrap product identities. It checks the full saved cut records,
all600 terms for the24 possible minima, all decisive rational bounds,
and all2699 construction comparisons, exact differences and flags.
All10165 audit checks pass with no failures, allocation samples or
floating-point operations. Complete decisive values and the matched
enclosure operands were inspected. The universal logical arguments are
the ones above; a preview or number of passing checks does not prove them.

The direct mathematical inputs remain L055, L104 and L106; no new
dependency is introduced. The assessed finite-affine and finite-maximum
sources cited above cover the imported machinery, with the displayed
specialization providing the required changed-coefficient argument.
H guards are still omitted, and no integrality, residue, valuation,
realization, seed or primitive-period conclusion is imported. This audit
does not assemble the b0=0 branch or transfer the result to actual words.
Attempt032/033/034 and the endpoint counterexample remain intact.

## Mathlib

Full matching theorem: not checked. Supporting finite-affine, finite
maximum, logarithm, exponential and rational-arithmetic coverage: not
checked. No absence or formal-verification claim is made. The argument
is the explicit informal proof above with precisely qualified sources.
