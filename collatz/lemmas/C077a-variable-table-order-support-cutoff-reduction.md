# C077a — Variable-table order/support/cutoff reduction

## Hypotheses

Let r>=3, B>=0 and tau>=0 be integers. Fix integer pairs
2<=J_0<...<J_(r-1) and H_i>=3. All logarithms are natural. Set

\[
\kappa=23/11,\quad G_i=(27/16)^{J_i}(3/2)^{H_i},\quad
Q_i=(12/11)(3/2)^{H_i}+1,
\]
\[
K=\sum_i(3J_i+H_i),\quad
N=\sum_i(4J_i+H_i)+2r+18B,\quad
\Lambda=N\log2-K\log3.
\tag{1}
\]

Require the following three sets of certified data tests on this same
table and budget. Constants with superscripts O, S and C are separate
choices; no equality between the three certificates is required.

**Order tests: all of L075 (2)–(5).** Explicitly choose rational
lambda^O,T^O,ell^O,u^O,v^O such that

\[
0<\lambda^O\le\Lambda,\quad
\frac{23r}{11\lambda^O}+\kappa\le e^{T^O},\quad
0<\ell^O\le\log2,\quad \log3\le u^O,\quad
\log(11/4)\le v^O.
\]

For every row require d_i=81/44-(3/11)(3/2)^{H_i}<0. Define
the literal tail-2 prefixes

\[
A_k=\sum_{i<k}(3J_i+H_i),\qquad
D_k=\sum_{i<k}(4J_i+H_i+2),\qquad A_0=D_0=0.
\]

For every 0<=k<=r-2 require

\[
4J_{k+1}\ell^O-T^O-v^O-A_ku^O+D_k\ell^O>0.
\tag{2}
\]

**Support tests: all of L076 (2)–(4) if B>0.** Put
E=23(r-1)/(4*2^{4J_1}-23). Choose rational
lambda^S,U^S,T^S,ell^S,u^S,v^S with

\[
E<\lambda^S\le\Lambda,\quad
\frac{23}{11(\lambda^S-E)}+\kappa\le U^S\le e^{T^S},\quad
0<\ell^S\le\log2,\quad\log3\le u^S,\quad
\log(11/4)\le v^S.
\]

For every 0<=j<=r-3 require both

\[
Q_j>\kappa 2^{20},\qquad
(D_{j+1}+18+4J_{j+1})\ell^S-T^S-v^S-A_{j+1}u^S>0.
\tag{3}
\]

For B=0 none of these support tests or support certificate constants
is required.

**Cutoff tests: L077 (3), and (4)–(5) if tau<=B.** Put p=r-2,
q=r-1, and

\[
\eta_i=\kappa-\frac{12}{11}(16/27)^{J_i}
                   -(16/27)^{J_i}(2/3)^{H_i}.
\]

Choose rational lambda_-^C,lambda_+^C,e^C satisfying

\[
0<\lambda_-^C\le\Lambda\le\lambda_+^C<1,\quad
0<e^C\le\min(\eta_0,\eta_q),\quad
\frac{e^C(1-\lambda_+^C)}{\lambda_+^C}\ge47.
\tag{4}
\]

For each integer 0<=t<=B define the *test allocation*
beta_i(t)=0 for i<p, beta_p(t)=t, beta_q(t)=B-t, and

\[
\alpha_i(t)=2+18\beta_i(t),\quad
c_i(t)=\frac{3^{3J_i+H_i}}{2^{4J_i+H_i+\alpha_i(t)}},\quad
C_i(t)=\prod_{j<i}c_j(t),\quad C_0(t)=1.
\]

If tau<=B, choose positive rationals L_i^C (0<=i<=q),
Q^C,U^C and rationals T^C,ell^C,u^C,v^C such that

\[
0<L_i^C\le C_i(\tau),\quad
Q^C\ge\kappa\sum_{i=0}^q1/L_i^C,\quad
\frac{Q^C}{\lambda_-^C}+Q^C+\frac{\kappa}{L_q^C}
\le U^C\le e^{T^C},
\]
\[
0<\ell^C\le\log2,\quad\log3\le u^C,\quad
\log(11/4)\le v^C,
\]
\[
T^C+A_qu^C-
\left(\sum_{i<q}(4J_i+H_i+\alpha_i(\tau))+4J_q\right)\ell^C
+v^C<0.
\tag{5}
\]

If tau>B, omit (5) and its constants, but retain (4). All analytic
certificate inequalities must be justified as in the cited criteria;
floating-point approximations do not suffice. The test allocations here
define data only and are not assumed to describe a feasible tuple.

Now let indexed b_i>=0 be integers with sum b_i=B and attach
a_i=2+18b_i to row i. Let pi be any permutation of the r rows.
Suppose real s_0,...,s_r satisfy s_r=s_0, s_k>=540/11 and

\[
s_{k+1}=2^{-a_{\pi(k)}}(G_{\pi(k)}s_k-Q_{\pi(k)})+\kappa,
\qquad
4J_{\pi(k)}\log2\le\log s_k+\log(11/4)
\quad(0\le k<r).
\tag{6}
\]

Every outgoing indexed row carries its pair and allocation with its own
input. Only the endpoint/domain/non-strict J subsystem is imposed.
No H guard, seed, minimum location, integer junction, actual word,
parity, residue, exact valuation, primitive-period or count-ray premise
is assumed.

## Conclusion

Every feasible tuple in (6) has literal cyclic order. Let z be the unique
chronological position with pi(z)=0, put rho_i=(z+i) mod r for i<r,
rho_r=z, and x_i=s_(rho_i). Then x_r=x_0 and indexed row i is
the outgoing row at input x_i. Its allocation necessarily has

\[
b_i=0\ (0\le i<r-2),\qquad
b_{r-2}=t,\quad b_{r-1}=B-t,\qquad
0\le t\le B,\quad t<\tau,
\tag{7}
\]

for an integer t. Every endpoint and own-input non-strict J guard holds
in this literal normalization. The normalized unshifted row-0 coordinate
is x_0-kappa=s_z-kappa, without an integrality assertion.

This is a necessary reduction, not a converse or a survivor-existence
claim. In particular tau=0 leaves no feasible tuple under all the tests.
Passing t=0 or 1 is not asserted for arbitrary tables. Failure of a test
gives no feasibility verdict. No new table, survivor integer exclusion,
actual-word application or universal eventual descent is established.
This local REPRODUCTION composes audited inputs under the prior SPECIALIZE
assessment `drafts/literature/2026-10-17-variable-table-order-support-cutoff-assembly.md`.
No originality beyond the sources checked is claimed. The separate
critical audit below found no defect in this conditional assembly.
It is not a complete Collatz candidate.

## Proof

### Normalize only after the order implication

The table, budget, attached allocations, arbitrary permutation, real
lower domain and all equations and guards (6) match L075 exactly.
The order tests above are its full (2)–(5), with constants renamed O.
Thus L075 gives that pi is a rotation of 0,...,r-1. Use only this
cyclic-order conclusion; no given location of a minimum is required.

Since pi is a permutation, z exists uniquely. Literal cyclic order gives
pi(rho_i)=i for each 0<=i<r. The rho_i form a bijection of all input
occurrences. For each i<r, rho_(i+1)=rho_i+1 modulo r. When rho_i<r-1,
the old output is s_(rho_i+1)=x_(i+1). When rho_i=r-1, the old output
is s_r=s_0=x_(i+1). Hence every edge becomes exactly

\[
x_{i+1}=2^{-a_i}(G_i x_i-Q_i)+\kappa,
\qquad
4J_i\log2\le\log x_i+\log(11/4),\qquad x_i\ge540/11.
\tag{8}
\]

The old closing edge occurs at new position i=r-1-z. The new closing
edge at i=r-1 is the old edge z-1 to z modulo r. If z=0 they coincide;
otherwise the old closing edge is now interior. Thus neither cut loses
an equation or changes either affine offset. Each guard still uses the
input of its own outgoing row. Repeated junction values do not identify
distinct time occurrences. The indexed b_i, their sum B and their
attached tails are unchanged. In particular x_0=s_z; no chronological
position has been presumed to carry row 0 before this rotation.

### Remove early support, then invoke the cutoff

The literal tuple (8) has exactly L076's hypotheses. For B>0, (3)
and its preceding certificate inequalities are all of that lemma's
(2)–(4), with constants renamed S. Its conclusion gives b_i=0 for
i<=r-3. For B=0 the same conclusion follows directly from a sum of
nonnegative integers equal to zero, as L076 states; no support tests
have been used in that case.

Put t=b_p. Nonnegativity, integrality and the allocation sum give
0<=t<=B and b_q=B-t. Thus a_i=alpha_i(t) at *every* row, including
the final outgoing row. Substitution into (8) gives exactly L077 (6)
for this parameter, with all endpoints, domain bounds and guards
retained. Its K,N,Lambda, eta_i and c_i,C_i definitions agree with
(1), (4) and the test-allocation definitions above. In particular the
two remaining tails sum to 4+18B; no total or closing multiplier changes.

Our (4) is exactly L077 (3), with constants renamed C. If tau<=B,
our (5) is exactly its full (4)–(5): its incoming odd exponent k_q
is A_q, and its incoming denominator exponent d_q(tau) is the displayed
sum over i<q. L077 therefore rejects every tau<=t<=B by a strict
failure of row q's own non-strict J guard. Since (8) satisfies that
guard, t<tau. If tau>B, (5) is not required or invoked: t<=B<tau
already proves the same conclusion. This proves (7). Each invocation
uses its own certificate; no cap or log enclosure is substituted from
another criterion. No affine fixed-point or analytic estimate is reproved.

### Boundary ranges and limitations

For r=3 there is one early index, 0, and the two remaining indices are
p=1,q=2. The same rotation covers all three edges, L076 removes b_0,
and L077 tests row 2. No prefix or row disappears.

For B=0 all b_i vanish and t=0. If tau>0, tau>B and no boundary tests
are needed; (4) still remains required. If tau=0, the boundary tests
are required, and L077 rejects t=0, so the full conjunction has no
feasible tuple. For B=1 the only remaining parameters before cutoff
are 0 and 1; support tests are required because B>0. If tau=0 both
are rejected, if tau=1 only 0 remains a possibility, and if tau>1
neither is rejected by the cutoff. None of these statements asserts
existence. For general B and tau=1 the only possible survivor is 0.
For tau=B the boundary tests are required and reject t=B, retaining
the final tail alpha_q(B)=2 in its endpoint. This includes B=tau=0.
For tau>B the rejection interval is empty, but (4) is not removed.

The inspected source assessment distinguishes this conditional
variable-table conjunction from the fixed-table C074a rotation assembly
and L068 classification. They are precedents, not additional theorem
inputs here. The two rational witnesses and the failed optional <-4
probe are unaffected. No survivor arithmetic or stopped prime diagnostic
is reused to infer an exclusion. The upstream formal affine identity is
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its nonzero-denominator qualification is retained by the positive Lambda
certificates of the imported criteria. Only their already proved
implications and the explicit finite relabeling above are needed; no
integer-itinerary converse or new analytic theorem is imported.

### Independent critical audit — 2026-10-17, step 293

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-17-variable-table-assembly-critical-audit.md`.
This RESEARCH/REPRODUCTION audit found no defect in the composition,
including its independent certificates, both cyclic cuts and boundary
ranges. It verifies a local input, without strengthening the conclusion
or claiming progress beyond the sources checked. The full statements
and relevant audit passages of L075, L076 and L077 were compared with
the statement and proof above. Their existing component audits are
imported; no component benchmark is being recertified here.

**Data and quantifiers.** All three inputs require the same integer
r>=3, B>=0, strictly increasing integer J_i>=2 and integer H_i>=3.
Their totals are exactly (1): permutation changes neither sum, and the
attached allocations contribute sum a_i=2r+18B. The definitions of G_i,
Q_i and kappa coincide. L075's full tests (2)–(5) are reproduced in
the order paragraph and (2), including the negative offset at every
row and all k=0,...,r-2 margins. Its prefixes are the displayed A_k,D_k;
the larger-index prefixes needed below are defined by the same sums.
The lower bound lambda^O and minimum cap are not used as support or
cutoff certificates.

For B>0, the support paragraph and (3) reproduce precisely L076
(2)–(4). In particular E uses J_1, the denominator is positive because
J_1>=3, and the residual lambda^S-E is explicitly positive. The
input-zero cap uses that residual, not lambda^O. The negative tail-20
offset and the margin indexed j+1 are imposed for every j=0,...,r-3.
For B=0 L076 expressly dispenses with these tests, so their omission
in C077a is legitimate. Equation (4) reproduces all of L077 (3),
including the upper bound lambda_+^C<1, both eta bounds and the uniform
domain inequality, in every cutoff branch. When tau<=B, the paragraph
leading to (5) includes every positive L_i^C for 0<=i<=q, the sum bound
for Q^C, the cap with kappa/L_q^C and all log enclosures. These are
L077 (4); (5) is its strict boundary test. No equality of constants
between the three certificates is needed. All analytic tests remain
certified hypotheses; this audit does not assert them for a new table.

**Rotation independently checked.** Equation (6), before normalization,
matches L075's tuple hypotheses exactly, including each indexed b_i
and its own outgoing input. L075 first supplies cyclic literal order.
Only then choose the unique position z of indexed row 0. The map
i -> rho_i=(z+i) mod r is a bijection on input occurrences and satisfies
pi(rho_i)=i. For i<r, its next position is rho_i+1 modulo r.
If rho_i<r-1, the original endpoint is s_(rho_i+1); otherwise it is
s_r=s_0. Both equal x_(i+1), also when i=r-1 and x_r=x_0.
Thus the entire endpoint, including -2^(-a_i)Q_i and +kappa, becomes
(8); no offset, tail or guard is transported separately from its row.
The own-input guard and lower domain transfer pointwise by the same
bijection, without any strictness change.

The old closing edge has rho_i=r-1, which solves to i=r-1-z in
0,...,r-1. The new closing edge i=r-1 starts at old position z-1
modulo r and ends at old z. At z=0 these are the same closing edge;
at z=r-1 the old closing edge is the new first edge and the new closing
edge is old r-2 to r-1. The intermediate values of z obey the same
explicit formulas. This covers all cuts, not only nonboundary cuts.
Coincident s values do not affect the bijection of occurrences. In
particular the coordinate at indexed row 0 is exactly s_z-kappa,
not necessarily the old chronological s_0-kappa. No integrality or
minimum-location premise is used or concluded.

**Support precedes cutoff.** The normalized (8), unchanged b_i and
support tests satisfy L076 literally. Hence all indices i<p=r-2
have zero support. The integer t=b_p then obeys 0<=t<=B, and the
unchanged sum forces b_q=B-t at q=r-1. Consequently the actual a_i
equals the test alpha_i(t) at every row, rather than merely in total.
The coefficients c_i(t), incoming products C_i(t) and eta_i therefore
match L077 (2). Its k_q equals A_q and its d_q(tau) is exactly the
sum in (5). The final tail remains in N and the closing endpoint even
though it is absent from the *incoming* prefix at q, as it must be.
No prefix for a different allocation has been substituted.

If tau<=B and a feasible t also satisfied t>=tau, L077 would make
row q's right-minus-left J margin strictly negative. Equation (8)
requires that same margin to be nonnegative. This is a contradiction,
including at equality t=tau. If tau>B, the arithmetic inequalities
t<=B<tau give the conclusion directly; only the boundary tests are
omitted, and (4) remains a hypothesis. The endpoint/domain existence
part of L077 is not used to infer that a surviving parameter satisfies
all guards.

**Boundary check.** At r=3 the early range is precisely {0}, with
p=1,q=2; the support margin uses A_1,D_1 and the cutoff incoming
prefix uses rows 0 and 1. The order test at k=0 retains A_0=D_0=0.
For B=0 all entries are zero before any theorem application: tau=0
requires the boundary tests and rejects the only t=0, while tau>0
omits those tests and asserts no feasibility. For B=1 the support
tests are required and leave only the possible t=0,1: tau=0 rejects
both, tau=1 rejects 1, and integer tau>1 has an empty rejection range.
For any B, tau=1 leaves at most t=0. At tau=B the tested t=B has
alpha_q=2, still satisfies the exact last endpoint convention and is
rejected if feasible; B=tau=0 is included. These are conditional
statements, so they do not assert that all data tests are simultaneously
satisfiable at every boundary choice. No exceptional empty range is
silently interpreted as an existing survivor.

The precise upstream citation remains Halbeisen–Hungerbuehler (1997),
section 2 equations (2)–(4), Lemma 2, pp. 228–229, as cited above.
The already audited implications contain the necessary formal-affine
specializations and analytic qualifications. The current proof adds
only the explicitly checked finite normalization and implication
matching; a source reproof or a fresh numerical certificate would not
test a missing step in this assembly. C074a is a precedent, not a
fourth input. The DAG's three direct inputs therefore remain accurate.
The inspected histories show that this is the first completed C077a
audit; the earlier scope comparison was not a no-defect verdict.
Attempts 026–031, both rational witnesses and the failed optional <-4
probe retain their meanings. Survivor arithmetic, actual-word use,
other tables and universal eventual descent remain unresolved.

## Mathlib

Full matching theorem coverage is not checked. The argument is an
explicit finite cyclic relabeling and composition of L075, L076 and
L077. General finite-permutation, logarithm and affine facts would be
supporting results, not a matching theorem for this conditional reduction.
