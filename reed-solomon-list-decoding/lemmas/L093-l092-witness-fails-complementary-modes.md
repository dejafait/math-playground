# L093 — L092's frozen witness fails its complementary modes

## Hypotheses

Use exactly L092's ordinary union-moment model at n=1024,d=10,w=68,
with matrices divided by L053's positive rho. Retain L021's original
pairs, L073's included-anchor five/six/seven base, L075's complete
dictionary and seven-column RREF/completion, L076's original column
family, and L086's unchanged columns with t78=L083's s. In particular

    p8=16792471/1181138102168120460>0.

Freeze all 45 L092 moments, not just its columns. The exact vectors are
`witness/z` and `witness/raw_moments` in
`scripts/finite-support/zero-block-plus-3-4-results.json`; their complete
values agree with L092's separate critical verifier. Index them
lexicographically by 0<=r,q<=8,r+q>=8, with

    V_rq=C(8,r)C(60,r)C(8,q)C(948,q)>0,
    Y_88(8-r,8-q)=p8*z_rq/V_rq.

Keep all 85 domain rows, 90 original/weighted kernel equations, 500 full
types and 3000 presentations, 36 forced entries, full anchor, whole
singular ranges and positive raw normalization. Ancestral PSD,
uniqueness, whole-kernel and coherent-normalization qualifications from
foundations/04,09,10,12 remain conditional imports. This calculation
does not recursively audit them or assert a representing measure.

## Conclusion

Of the 29 complementary nonzero-old-block modes at this exact complete
witness, 13 have strictly negative remainder and 16 strictly positive
remainder. None is zero. In the index convention i=9a+b the negative
indices are

    {6,15,23,25,32,40,42,50,52,58,60,67,68}.

The minimum scaled remainder occurs at i=23, mode (2,5), and satisfies

    -194034874397435/10^6 <= b_23-A_23*z
                         < -194034874397434/10^6 < 0.

The required lower bound is zero. A full rational 4-by-4 offending block
and an exact four-coordinate negative quadratic vector are saved in
`scripts/finite-support/l092-complementary-modes-results.json` under
`offending_block`, independently reconstructed by the verifier below.

All 28 selected equalities remain zero; all 44 L092 retained mode rows
pass (11 positive,33 zero), including exactly zero remainder in mode
(3,4). The 43 zero-old-block rows now have 11 positive and 32 zero
remainders. All 45 moments retain 35 positive and ten zero values.
All frozen domain, kernel and dictionary controls pass.

Thus this complete assignment fails the included-anchor matrix test,
under the imported normalization contracts. L092's necessary-subsystem
pass remains valid. This does not exclude another moment completion at
the same columns, the whole zero plane, other columns/base/pairs or a
global moment extension. Scalar upper rows, other anchors, representing
measures and RS realization remain open. Arbitrary-center 67/68-agreement
safety and the 955–957 bracket are unchanged. This is an informative
negative result for this assignment, RESEARCH / REPRODUCTION using known
methods, with no progress beyond the sources checked claimed. The separate
conditional critical proof audit below retains this finite rejection.

## Proof

**Known inputs and specialization.** Reuse the pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-19-l092-complementary-mode-residuals.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7. Its unequal-layer decomposition applies to the finite
ground sets 68,956 and principal restriction to layers 0,5,6,7,8.
Retain L078's coherent positive congruence, both rectangular directions,
positive multiplicities and the full anchor. No actual-label averaging
or suspect complement prefactor (61) is used. The normalization relating
the beta block to the actual weighted block is the one retained in
L091's separate audit, unchanged by varying only the 45 moments.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2 Corollary 2.2, Theorem 2.6 (both singular proof directions),
Lemma 2.7. Finite real symmetric blocks and scalar new coordinates are
covered. Old PSD and the entire cross-vector range are required also
for singular nonzero blocks. A checked solution B*x=c computes the
range-inverse cost c^T*x: any two such solutions differ by a vector in
ker(B), orthogonal to c. No Euclidean quotient pseudoinverse is assumed.

The ordinary union-moment setting is imported from Sven C. Polak,
*Semidefinite Programming Bounds for Constant-Weight Codes*, IEEE TIT
65 (2019), 28–38, DOI 10.1109/TIT.2018.2854800,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1 and indicator proof p.2, Section
1.2 p.3, retaining its constant-weight qualification at n=1024,d=10,w=68.
No uniqueness, measure or common-center RS assertion is imported.
These general results are not reproved; none supplies this witness's
residual values. Their finite specialization requires the exact
reconstruction and substitution that follow.

**Full original rows.** Binomial coefficients outside their ordinary
range are zero. Use the source convention

    beta(n,l,m,a,t)=sum_(h=max(a,t))^min(l,m,n-a)
      (-1)^(h-t)C(h,t)C(n-2a,h-a)C(n-a-h,l-h)C(n-a-h,m-h).

Put S_l=C(68,l)C(956,l). In mode i=9a+b let the old layers be
l in {5,6,7} with l>=max(a,b). Using the original raw dictionary set

    T_lm=sum_(j,k=0)^min(l,m) beta(68,l,m,a,j)beta(956,l,m,b,k)Y_lm(j,k)
         -1_(i=0)*p_l*p_m*S_l*S_m,
    B_i=(T_lm), c_i=(T_l8), B_i*x_i=c_i.

The calculation reconstructs every old entry and affine cross vector
from the original pairs, base and column RREF. It checks both rectangular
directions and every coefficient of each affine range equation. All
306 nonempty old principal minors are nonnegative. For each block,
enumerate principal subsets by increasing size and lexicographic order,
choose the last with nonzero determinant, solve that principal system
by Cramer's rule and set remaining coordinates to zero. Direct
substitution checks the entire B_i*x_i=c_i, including singular and empty
cases. Its cost agrees exactly with the saved affine inverse action.
No invertibility conclusion is inferred merely from a nonzero block.

Let F_i be the forced contribution to the complete new diagonal,
H_i=1_(i=0)*p8^2*S_8^2 and K_i=c_i^T*x_i. Define

    D_i=C(68-2a,8-a)C(956-2b,8-b)>0, M_i=p8*D_i>0,
    A_(i,rq)=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)/(D_i*V_rq),
    b_i=(F_i-H_i-K_i)/M_i.

At the full unchanged L092 vector the raw remainder is exactly

    R_i=F_i-H_i-K_i
        +sum_(rq) beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)*p8*z_rq/V_rq
       =M_i*(b_i-A_i*z).

Both formulas are evaluated with complete rational arrays for all 81
modes. Forced entries, the constant-mode anchor and all inverse costs
are retained. Strictly positive M_i makes their signs identical.

**Partition and retained controls.** Set
I={9a+b:0<=a<=6,0<=b<=3}. Determine Z by testing every entry of each
complete old block for zero; empty blocks are included. There are 43
such blocks, including all 17 empty ones, and every whole cross vector
on Z is zero. All 81 membership decisions agree with L092's audited
membership. Put J=Z union {31}, the 44 L092 retained modes. One has
|I|=28, |I intersect Z|=20 and 31 outside I union Z. Thus I union J
has 52 elements, and its exact complement is

    {4,5,6,7,14,15,16,23,24,25,32,33,34,40,41,42,43,
     49,50,51,52,58,59,60,61,67,68,69,70}.

The scripts verify this complete partition rather than adding the
overlapping set sizes. All retained original/raw residuals equal L092's
full saved values. In particular the added row 31 remains zero, every
I equality is zero, and all J inequalities and signs pass with the
counts in Conclusion. The 85 domain factors and all 90 original and
weighted kernel equations are independently reconstructed from the
same affine columns. Full eight-atom presentations reconstruct every
one of the 500 types in all six orders, with all Boolean and forbidden
cases, the 36 forced entries and 45 distinct free keys retained.

**Complementary residuals and explicit negative vector.** Substitute
the same complete z into all 29 complementary rows. The certificate
stores every original row, raw beta coefficient, bound, old block,
cross, inverse, minor, cost and exact original/raw residual in `rows`.
Its complete `negative_indices` and `failing_remainders` give the
13 failures above; the other 16 remainders are strictly positive.
Integer cross multiplication verifies the displayed bound at index 23.

For this index let d=F_23-H_23 plus the full free raw beta sum, and form

    C=((B_23,c_23);(c_23^T,d)), v=(-x_23,1).

Every entry of this four-by-four block and of v is stored, without
rounding, under `offending_block`. Since B_23*x_23=c_23,

    v^T*C*v=d-c_23^T*x_23=R_23=M_23*(b_23-A_23*z)<0.

Thus C is not PSD. The retained positive congruence places this beta
block inside the prescribed matrix: if its weighted block is
alpha*diag(s_l,1)*C*diag(s_l,1), alpha and all s_l positive, the vector
diag(s_l,1)^(-1)*v has quadratic value alpha*R_23<0. This uses the
unchanged coherent-normalization import, with no numerical eigenvalue
or assumption that a quotient inverse is a pseudoinverse.

**Independent verification and evidence.** The second calculation uses
the independent Johnson eigen-coefficient expression

    e(n,a,r)=sum_(h=0)^r (-1)^h C(a,h)C(8-a,r-h)C(n-8-a,r-h).

It verifies beta(n,8,8,a,8-r)=C(n-2a,8-a)*e(n,a,r) for every used
coefficient, independently obtains each bound using the original full
affine inverse action, and checks every original/raw identity and
retained residual. It consumes complete relevant L092 construction,
source reconstruction and conditional-audit arrays, distinguishing the
source audit's old L086 residuals from the current witness. For index
23 it separately sums all 81 actual raw new-diagonal orbit terms and
rebuilds the entire block. Its inverse action need not equal the sparse
principal solution, but their exact costs agree; both saved vectors
give the same strictly negative quadratic value.

Reproduction commands, containing no constructor or optimizer, are

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/l092_complementary_modes.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_l092_complementary_modes.py

The first has 1210 passing checks, the second 2018, with no failures.
Their full certificates are respectively
`scripts/finite-support/l092-complementary-modes-results.json` and
`scripts/finite-support/l092-complementary-modes-verification.json`.
The latter stores all 81 independent rows and the complete load-bearing
diagonal terms, block, vector and quadratic value. These checks consume
complete arrays; an inspector preview is not evidence of correctness.

Two wrapper corrections are preserved. The initial partition check
omitted the added row 31 from its exhaustiveness union and stopped
before complementary substitution; see
`scripts/finite-support/l092-complementary-modes-initial-partition-failure.json`
and `scripts/finite-support/l092_complementary_modes_initial.py`.
The next run compared the 43 zero-block sign counts with L090's old
10/33 counts instead of L092's 11/32 counts and withheld its verdict;
see `scripts/finite-support/l092-complementary-modes-control-count-failure.json`
and `scripts/finite-support/l092_complementary_modes_count_initial.py`.
Correcting these wrapper expectations changes no mathematical input,
constraint, moment or residual formula. All retained full residuals
are compared entrywise with L092, in addition to the corrected counts.

No solver, retuning, column scan, new constraint, separator search,
full-row restart or conic restart occurs. Preserve L090's subsystem
pass, L091's rejection of different moments, L092's subsystem pass and
all historical full-row/conic stops. The initial arithmetic verification does not
resolve ancestral qualifications; the separate critical audit below
retains the fixed verdict with those qualifications.
Only this complete assignment is rejected.

**Separate conditional critical audit, 2026-10-19 (step 340).** Reuse the
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-19-l093-complementary-rejection-critical-audit.md`.
The precisely cited Schrijver, Sano and Polak inputs above apply with
unchanged hypotheses. This audit specializes their known methods; it
neither reproves a general theorem nor recursively audits the ancestral
PSD, uniqueness, whole-kernel or normalization assumptions.

A fresh source reconstruction checks the original pairs/rho, seven-column
RREF/completion, L086 columns, all 85 domain factors, all 90 original and
weighted affine kernel equations, 500 types/3000 presentations and the
36-forced/45-free partition. Its complete arrays agree with L092's
separate source audit. All 220 subset transitions in both directions,
positive orthogonal norms and multiplicities, coherent layer scales and
306 old principal minors are checked. Its old L086 residuals are only
regression controls: they are not L092's residuals.

The complete L092 z and raw vector agree with its audited witness.
Every old-block membership decision is compared entrywise; the 29-index
complement and 13 negative indices are exactly the two manuscript lists.
For every one of the 81 modes, the audit constructs a fresh principal
range solve, checks every equation in the whole old block and retains
all affine range residuals, including empty and singular cases. The
full raw diagonal is reconstructed from all 81 actual orbit values.
Its independent weighted diagonal uses the direct subset-transition
coefficients. Every original/raw/weighted remainder agrees exactly;
the 28 selected equalities, 44 retained mode inequalities and 45 moment
signs have the stated counts, including zero in mode (3,4). The minimum
is at (2,5) and the displayed interval follows by exact integer comparison.

For clarity, the actual congruence is explicit here. Use L091's monic
orthogonal factors h_(n,l,a) with squared norms nu_(n,l,a), under weights
C(8,i)C(n-8,l-i), and its direct transition coefficients g. For each
nonzero beta, compute

    sigma_(n,l,m,a)=nu_(n,l,a)*g_(n,l,m,a,k)/beta(n,l,m,a,k).

All used ratios are positive and independent of k; zero beta has zero
action. At (a,b)=(2,5), with old layers 5,6,7, put

    N=nu_(68,8,2)*nu_(956,8,5),
    D=C(64,6)*C(946,3),
    alpha=N/D=460885983370444800/6510326953>0,
    s_l=sigma_(68,l,8,2)*sigma_(956,l,8,5)/alpha.

The computed scales at l=5,6,7,8 are all exactly 1. Independently
construct every entry of the actual weighted block as

    W_lm=nu_(68,l,2)*nu_(956,l,5)
         *sum_(j,k=0)^min(l,m) g_(68,l,m,2,j)*g_(956,l,m,5,k)*Y_lm(j,k).

There is no anchor subtraction in this nonconstant mode. Both rectangular
directions, the entire old block and the new diagonal give, entry by
entry,

    W=alpha*diag(s_5,s_6,s_7,1)*C*diag(s_5,s_6,s_7,1)=alpha*C.

All sixteen block entries agree with the saved block and independent
verifier. All four vector coordinates agree with the saved vector; the
independent verifier checks both that vector and its own range-inverse
vector against the full block, obtaining the same quadratic value. Thus
the transported saved vector is exactly v and

    v^T W v=alpha*(v^T C v)=alpha*R_23<0.

Its last coordinate is 1, and the product-mode multiplicity is the
positive integer 14476499038856010. The nonzero orthogonal factors and
the retained source decomposition put this weighted block in the
prescribed matrix. This explicitly connects the rational negative value
to a PSD violation; no arbitrary quotient pseudoinverse is used.

The original partition-failure certificate contains no substituted rows;
its frozen arrays agree completely with the final calculation. The
count-failure certificate has exactly the same full rows, failing values
and offending block as the final calculation. Exact script comparison
shows only the partition-union replacement and the stale 10/33 to 11/32
zero-block counts (including summary fields). No mathematical input or
formula changed. Historical hashes are checked against the preserved
script versions that actually produced those artifacts.

Reproduce this separate audit without a constructor or optimizer:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_l093.py

The source reconstruction has 7993 passing checks, the independent
original/raw verifier 2018, and the additional audit 1279, with no
failures. Full certificates, including complete current diagonal terms,
blocks, vectors, scales and exact quadratic values, are
`scripts/finite-support/l093-critical-source.json`,
`scripts/finite-support/l093-critical-verification.json` and
`scripts/finite-support/l093-critical-audit.json`.

An initial additional-audit wrapper stopped before current residual
substitution: it compared the two historical script hashes with the
current script instead of the preserved versions, and its string matcher
for the count correction had itself inherited the corrected counts.
The initial script, full failed certificate and log are preserved as
`scripts/finite-support/critical_audit_l093-initial.py`,
`scripts/finite-support/l093-critical-audit-initial.json` and
`scripts/finite-support/l093-critical-run-initial.log`. The corrected run
used `--reuse-reconstruction` to reuse the unchanged fresh source and
verifier evidence, then completed all additional checks. No mathematical
discrepancy was found or hidden. L091's different-witness rejection,
L092's necessary-subsystem pass and the full-row/conic stops remain.
This retains only L093's conditional fixed-assignment rejection, without
source-level novelty, a full-column exclusion or RS boundary improvement.

## Mathlib

Full matching fixed-witness rejection: not checked. Supporting singular
Schur, unequal-layer decomposition and rational arithmetic coverage:
not checked here. Unknown availability is not absence. General methods
are imported by precise citations without a novelty claim.
