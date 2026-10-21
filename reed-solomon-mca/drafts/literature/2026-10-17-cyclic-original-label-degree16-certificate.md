# Proposed original-label certificate comparison

TARGET: Assess whether a degree-sixteen polynomial certificate in the original cyclic labels, with explicit subgroup and collision equations, gives a bounded independent rank-27 exclusion test.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 280 searched NulLA coefficient matrices, certificate degree and roots-of-unity coloring; inspected the primary statements/proof cases below, L089's statement, L090/L091's gate reductions, ATTEMPTS/032–034 and the step-279 comparison; a targeted local search found no prior degree-sixteen test.
SOURCE_EVIDENCE: De Loera–Lee–Malkin–Margulies arXiv:0801.3788v1 Lemma 1.1, section 2 algorithm, Lemmas 3.1–3.2, finite-characteristic remark and section 3.2/Theorem 3.5 with proofs; De Loera et al. arXiv:1410.6806v1 definitions/Theorems 1.1–1.2 and 2.1 with proof; reused step 279's finite-set comparison.
COMPARISON: Known coloring equations encode H membership and collisions without auxiliary variables; NulLA specifies a complete formal multiplier basis. The raw degree-sixteen template has 1,255,800,216 coefficient unknowns and 601,080,390 ambient rows; neither the cutoff nor a manageable complete reduction follows from the sources.
GAP: No manageable complete search or degree-sixteen existence theorem is supplied; no certificate, failed bounded solve, cyclic exclusion or rank-27 labeling is established.
REASON: Known machinery permits precise formulation but fails the saved practical continuation test. Park the full degree-sixteen search; SPECIALIZE records partial known coverage, not approval to run or enlarge it. Route to a separately assessed independent lower-bound target.
LITERATURE_REASON: The completed chart review does not cover an exact degree-bounded original-label system, its collision encoding or a feasible complete search space.

Review only fixed H, F_(97^20), L087–L089 and L090/L091's necessary
cyclic gates. L095 is a comparison, not a required parametrization.
This is source comparison and formulation, not certificate search.

The proposed ansatz is a formal polynomial identity for 1, with each
summand of total degree at most sixteen, from an explicitly stated
F_97 polynomial system. Membership h_i^16=1 refers to original labels.
Nonzero pairwise differences require a justified encoding; every
rational-gate denominator remains. The cutoff is provisional, not a
proved threshold. No generator list, symmetry, dimension reduction or
finite multiplier basis has been derived or approved. Do not confuse
the sources' functional multiplier-degree bounds with this formal
summand-degree cutoff. Review these distinctions before any calculation.

A verified identity for a necessary gate subsystem would exclude this
cyclic family. A complete negative test would exclude only the chosen
certificate ansatz; an incomplete search would do neither. A gate
solution still needs L089's full rank test and the audited actual-error
application before any sixteen-count claim. Arbitrary families, uniform
triangle twelve and challenge-definition gaps remain independent.

Compare ATTEMPTS/032–034 and the completed chart assessment. Continue
only if a bounded, independently checkable system and manageable
complete search basis can be specified; otherwise abandon this
candidate without enlargement or H-label enumeration. Mathlib coverage
has not been checked. No cross-notebook input is proposed.

## Completed comparison — step 280

The main gap is exclusion or realization of sixteen actual bad parameters
at the fixed code. The reviewed intermediate target is exactly TARGET.
A verified identity for one would exclude this cyclic family; arbitrary
families, uniform triangle twelve and challenge qualifications would remain
open. The saved continuation test requires both an exact bounded system
and a manageable complete basis. Only the first requirement is supplied.
This is source specialization for formulation and size comparison, not
a certificate search or a new exclusion theorem. The proposal above is
preserved as historical scope; this completed section controls its decision.

### Primary coverage and qualifications

J. A. De Loera, J. Lee, P. N. Malkin and S. Margulies,
[*Hilbert's Nullstellensatz and an Algorithm for Proving Combinatorial
Infeasibility*, arXiv:0801.3788v1](https://arxiv.org/pdf/0801.3788v1),
Lemma 1.1, p. 1; section 2, pp. 2–4; Lemmas 3.1–3.2 and following
finite-field remark, pp. 5–6; section 3.2/Theorem 3.5, pp. 6–9.
Read the coloring argument, coefficient-field descent, algorithm cases,
matrix construction and complete averaging/orbit proof. The coloring
encoding extends to finite characteristic coprime to the number of colors.
NulLA tests a specified multiplier cutoff by coefficient matching; failure
at one cutoff does not establish feasibility. Coefficients descend to the
input field. Orbit compression requires generator invariance and invertible
group order. These tools give neither a cyclic exclusion nor a practical
size theorem.

J. A. De Loera, S. Margulies, M. Pernpeintner, E. Riedl, D. Rolnick,
G. Spencer, D. Stasi and J. Swenson,
[*Gröbner Bases and Nullstellensätze for Graph-Coloring Ideals*,
arXiv:1410.6806v1](https://arxiv.org/pdf/1410.6806v1),
pp. 1–4, definitions/Theorems 1.1–1.2 and Theorem 2.1 with complete proof.
Its certificate degree is maximum MULTIPLIER degree, unlike this proposal's
maximum SUMMAND degree. The modular/minimum-degree obstruction concerns a
pure coloring ideal of a noncolorable graph. Here K_16 is 16-colorable and
cyclic generators are added; that obstruction cannot be imported for the
joint system. Version metadata is retained as displayed: v1 identifier
October 24, 2014, PDF title-page date August 30, 2018. No newer version is
asserted.

Reuse step 279's Moshkovitz–Yu Theorems 1–2 and Ghorpade Theorem 2.3
comparison in `2026-10-17-cyclic-exact-subgroup-chart-review.md`, without
rereading unchanged sources. Functional equality modulo field equations
does not supply the formal summand-degree-sixteen identity. Those theorems
neither prove emptiness of this zero set nor guarantee the cutoff. No
general theorem is reproved. Full matching and supporting Mathlib coverage
for the joint system was not checked; no absence claim is made.

### Source-specialized formulation, not a certificate

Work in F_97[x_0,...,x_15], without projective normalization. Indices
are modulo sixteen; x_i denotes an ORIGINAL label. The standard complete-
graph 16-coloring encoding supplies

    V_i = x_i^16 - 1                         (16 generators),
    E_ij = sum_(l=0)^15 x_i^(15-l) x_j^l      (120, i<j).

The necessary applicability check is that 97 does not divide 16 and all
sixteen roots already lie in H. At distinct roots E_ij vanishes; at a
repeated root it equals 16*x_i^15, nonzero. Thus this cited encoding means
exactly bijective H membership, also over F_(97^20) or its algebraic closure.
No auxiliary inverses or product of all differences is needed. This is the
root/characteristic specialization, not a reproof of the coloring theorem.

Include all sixteen L090 determinants, with its original labels
a=x_(t-1), b=x_t, c=x_(t+4), d=x_(t+6), e=x_(t+8), f=x_(t+9):

    D_t = det [[ab,a+b,1],[cf,c+f,1],[de,d+e,1]].

For L091 additionally write u=x_(t-2), x=x_(t+1), q=x_(t+2),
y=x_(t+5), z=x_(t+7), k=x_(t+10). Specify its denominator clearings by

    NF1=(c-a)(x-z)(x-e)(d-u), QF1=(c-e)(x-u)(x-a)(d-z),
    NF2=(x-b)(y-f),           QF2=(x-f)(y-b),
    NS1=(q-e)(z-a),           QS1=(q-a)(z-e),
    NS2=(q-b)(q-x)(d-k)(e-f), QS2=(q-f)(q-k)(d-x)(e-b),
    Ftilde_t=NF1*QF2+NF2*QF1-QF1*QF2,
    Stilde_t=NS1*QS2+NS2*QS1-QS1*QS2.

These mechanically transcribe existing equations. Ftilde and Stilde have
degree six and D has degree three. Every denominator is a product of
differences at distinct indices, so all denominator gates follow from the
coloring encoding. There are no L095 projectivity poles because that chart
is unused. These 48 gates are necessary only: a solution is not asserted
to have rank R=2. Excluding this system would exclude rank 27 by L089–L091;
a survivor needs the full L089 rank test and the separately audited L096
conditional application before any sixteen-count claim.

The formal ansatz is

    1 = sum_i A_i V_i + sum_(i<j) B_ij E_ij
        + sum_t (C_t D_t + U_t Ftilde_t + W_t Stilde_t),

with multiplier degree bounds 0,1,13,10,10 respectively. Identity means
coefficient equality in the polynomial ring, not equality on sampled H
points or after unspecified high-degree reductions. This specifies the
provisional summand-degree-sixteen ansatz completely. No identity has been
obtained or claimed to exist.

### Size comparison and route decision

Substitute these caps in the cited NulLA monomial template; no matrix was
constructed:

| Generators | Number | Multiplier degree | Coefficient unknowns |
| --- | ---: | ---: | ---: |
| V | 16 | 0 | 16 |
| E | 120 | 1 | 120*17 = 2,040 |
| D | 16 | 13 | 16*binomial(29,13) = 1,085,822,640 |
| Ftilde, Stilde | 32 | 10 | 32*binomial(26,10) = 169,975,520 |

Total: 1,255,800,216 coefficient unknowns. Ambient rows are the monomials
in sixteen variables of degree at most sixteen:
binomial(32,16)=601,080,390. These are uncompressed template sizes, not
lower bounds on every implementation or proof; some rows/columns may be
redundant. Even one byte per unknown exceeds 1.25 GB before indices, matrix
entries or elimination. No manageable complete reduction/resource bound
was supplied. The symmetry theorem does not authorize arbitrary H-label
permutations or projective normalization. Naming sparsity or averaging
does not specify the missing complete reduced basis. No impossibility of
a structured method is inferred.

This differs from ATTEMPTS/033–034's rational-function elimination but
fails the saved practical continuation test. Park the raw full-basis
search without running it, increasing its cutoff, repeating L095's stopped
elimination or substituting a labeling sweep. There was no negative linear
solve: both absence of a degree-sixteen certificate and existence of a
gate solution remain undecided. No original discovery is claimed.
L090/L091 already passed canonical audits at steps 240/242; they were not
audited anew. Routing checks also found L096 and L098–L101 already audited;
stale pending wording in PROOF.md is not a reason to repeat them.

Queries: `Nullstellensatz proof system degree d monomials n variables
linear algebra certificate size polynomial calculus degree`; `Alon
combinatorial Nullstellensatz finite grid ideal membership degree bound
theorem 1.1`; `De Loera Lee Margulies Onn Nullstellensatz graph coloring
x_i^k - 1 sum x_i k-1 certificates linear algebra`; `NulLA Nullstellensatz
linear algebra degree certificate number monomials coefficient matrix
paper`; `Alon Tarsi graph coloring polynomial roots of unity sum x_i x_j
k-1 Nullstellensatz`. Snippets, later algorithm papers, general sparse-
bound leads and Alon–Tarsi papers were discovery leads only; no unread
theorem is imported. Failed searches establish no novelty. No mathematical
script, certificate search, lemma or DAG change was made; no cross-notebook
input was used.
