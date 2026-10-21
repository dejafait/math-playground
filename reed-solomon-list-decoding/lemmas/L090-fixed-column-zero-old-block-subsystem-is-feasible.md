# L090 — The fixed-column zero-old-block subsystem is feasible

## Hypotheses

Use n=1024,w=68, L021's original pair prescription, L053's positive
singleton rho, and matrices divided by rho. The included-anchor
five/six/seven PSD base is exactly L073's, with L075's entire dictionary
and original seven-column RREF/completion. Import all ancestral PSD,
uniqueness, whole-kernel and coherent-normalization qualifications,
including foundations/04,09,10,12. No recursive ancestor audit is claimed.

Use L076's original affine columns and freeze their parameters to exactly
L086's columns: (1,t56,t63,t69) is the first four coordinates of
`witness/original` in `scripts/finite-support/affine-sign-phase-one-results.json`,
and t78 is L083's stationary s. Retain all 85 original domain rows,
90 weighted kernel equations, 500 full types/3000 presentations, 36 forced
eight/eight entries, full anchor and original pairs, with
p8=16792471/1181138102168120460>0. Only the 45 unrepresented eight/eight
moments may vary. No L088 moment is frozen.

Index z by (r,q) in lexicographic order, 0<=r,q<=8, r+q>=8. Put
V_rq=C(8,r)C(60,r)C(8,q)C(948,q)>0 and S=diag(p8/V_rq), so the raw
moment Y_88(8-r,8-q)=(S*z)_rq. Binomial coefficients outside their
ordinary range are zero. Impose all 28 L084 equalities, every moment
sign, and every original mode whose entire old source block is zero
entrywise after anchor transport, including empty blocks. No other mode,
scalar upper row, other-anchor matrix or global extension is imposed.

## Conclusion

This necessary subsystem has an explicit rational witness at the frozen
columns. Exactly 43 of the 81 old blocks are zero; their cross vectors
are all zero. The selected index set Z, with i=9a+b, is

    1,2,8,9,10,11,13,17,18,19,21,22,26,27,28,29,30,35,
    36,37,38,44,45,46,53,54,55,56,62,63,64,65,66,71,
    72,73,74,75,76,77,78,79,80.

This includes all 17 empty blocks, 20 modes already among the selected
equalities, and six additional mixed modes 13,22,63,64,65,66.
All 28 original/raw equalities vanish. All 43 original/raw selected
mode slacks are nonnegative: ten positive and 33 zero. All 45 scaled/raw
moments are nonnegative: 35 positive and ten zero. Both minimum retained
inequality values are exactly zero, meeting the required lower bound.

Thus zero-old-block modes, equalities and signs do not exclude these
columns. This is a RESEARCH / REPRODUCTION specialization of known
methods and an informative negative result for this exclusion test;
no source-level novelty is claimed. The 30 nonzero-old-block modes not
already imposed as equalities are not tested at this new witness.
L089's rejection of its different complete assignment remains valid.
Other columns/base/pairs, scalar upper rows, other anchors, global
consistency, representing measures and RS realization remain unresolved.
The arbitrary-center 67/68-agreement gap and 955–957 bracket are unchanged.
The separate conditional critical proof review below retains this finite result.

## Proof

**Known imports.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-fixed-column-zero-old-block-subsystem.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7. Ground sets 68,956 and layers 0,5,6,7,8 are in its
unequal-layer range. Retain L078's coherent positive congruence, both
rectangular directions and positive multiplicities. No actual-label
constraint is averaged; the suspect complement prefactor (61) is unused.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2 Corollary 2.2, Theorem 2.6 and Lemma 2.7. These apply to the
finite real symmetric old PSD blocks, including singular blocks. When
an entire old block is zero its whole cross vector must vanish; this
is checked, not replaced by a zero inverse-cost assertion. The remaining
PSD condition for each such enlarged block is its new diagonal >=0.
An empty old block is the scalar case. These are imported criteria,
not new general results.

For the exact free-variable LP method import Michel X. Goemans,
*Advanced Algorithms*, Lecture 3, 19 September 2001, Theorems 1,3,
printed pp.1–2,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
and MIT 6.854 (2020),
[Notes 11](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
Introduction, Linear Equalities and Basic Feasible Solutions. Pivoting
uses Goemans, *An Introduction to Linear Programming*, October 1994,
The Simplex Method pp.7–8,
[notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/908fe54d659623efadda2d033b895caf_notes_lp.pdf),
and Nannicini–Nasrabadi, MIT 15.053 Spring 2013, Recitation 3 solutions,
Problem 3.A–B pp.4–6,
[worked initialization](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/05885823def0372adb5eae09c7f5490d_MIT15_053S13_rec03sol.pdf).
The worked example is no complexity or termination theorem. Direct exact
substitution proves this finite feasibility claim, independent of simplex
status. General results need no reproof; none evaluates this subsystem.

**Full source reconstruction and selection.** Reconstruct all old entries
and affine cross vectors from L075's dictionary and L076's original RREF,
as in L089. In mode i=9a+b let the old layers be those l in {5,6,7}
with l>=max(a,b), and S_l=C(68,l)C(956,l). The source entries are

    beta(n,l,m,a,t)=sum_(h=max(a,t))^min(l,m,n-a)
      (-1)^(h-t)C(h,t)C(n-2a,h-a)C(n-a-h,l-h)C(n-a-h,m-h),
    T_lm=sum_(j,k=0)^min(l,m) beta(68,l,m,a,j)beta(956,l,m,b,k)Y_lm(j,k)
         -1_(i=0)*p_l*p_m*S_l*S_m.

Set B_i=(T_lm) on the old layers and c_i=(T_l8) at the fixed columns.
All 81 matrices, both rectangular directions, affine and point range
residuals, all 306 old principal minors, forced coefficients and full
anchor are reconstructed before selecting any row. Compare the complete
relevant step-318/320/322/324 arrays with their respective schemas,
including the original pair/base, seven completion, kernel and full-key
contracts. Prior witness signs are controls, not new completion verdicts.

For each original i inspect every entry of B_i, recording its layers,
full matrix, cross, empty flag, zero-block flag and range residuals.
The complete `membership` array has 81 records; its true flags give
exactly Z above. All selected c_i vanish in every coordinate; their
range costs are zero. In particular i=66 retains B_66=[0], c_66=[0].
The empty blocks are exactly max(a,b)=8. The nonempty zero-block count
is 26; selection does not use determinant zero, diagonal zero alone,
a rank label or L089's list of failures.

Put D_i=C(68-2a,8-a)C(956-2b,8-b)>0 and M_i=p8*D_i. Let F_i be the
full forced raw beta sum, H_i=1_(i=0)*p8^2*S8^2, and x_i any checked
solution of B_i*x_i=c_i. The original coefficients and bounds are

    A_(i,rq)=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)/(D_i*V_rq),
    b_i=(F_i-H_i-c_i^T*x_i)/M_i.

The original raw remainder is

    R_i=F_i-H_i-c_i^T*x_i
        +sum_(rq) beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)(S*z)_rq
       =M_i*(b_i-A_i*z).

Every M_i and S diagonal entry is positive. This keeps the complete
anchor and forced terms; on Z the cross cost vanishes by whole-vector
verification. The selected equalities use I={9a+b:0<=a<=6,0<=b<=3},
E=A_I, e=b_I. Necessity of E*z=e is imported from L082/L083, with the
complete L084 equality locus; selection of Z does not change it.

**Complete lift, not a restricted ansatz.** Use L088's reviewed original/raw lift specialization. Specialize L084's
quadratic particular solution at (1,t56,t63,t69) to P, and retain its 45-by-18
matrix N. Let F select its nonpivot coordinates and let G have row p_k
equal to row k of the saved invertible row transform, all other rows zero.
The full original-coordinate identities checked before solving are

    E*P=e, E*N=0, F*N=I_18, F*P=0,
    G*e=P, G*E+N*F=I_45.

Hence all and only equality solutions are z=P+N*h, h=F*z in R^18.
For raw equalities E_raw=-diag(M_I)*E*S^(-1), e_raw=-diag(M_I)*e,
use P_raw=S*P, N_raw=S*N, F_raw=F*S^(-1),
G_raw=-S*G*diag(M_I)^(-1). All raw forward and reverse identities are
also checked in full. In augmented coordinates define

    Q=(-e,E), L=((1,0);(P,N)), R=((1,0);(0,F)), K=(0;-G).

Then Q*L=0, R*L=I_19 and L*R-I_46=K*Q. The raw counterparts are
checked independently. No sign is imposed on h; no equality is dropped.

**One bounded exact Phase I and full witness.** Let H have all 43 rows
(b_i,-A_i), i in Z in increasing order, followed by 45 coordinate
sign rows (0,e_j). Keep all 88 rows, including the 20 redundant rows
already imposed as equalities and all zero/duplicate pulls. Compute H*L.
For each pulled row d0+d*h>=0 use h=h_plus-h_minus and

    -d*h_plus+d*h_minus+slack=d0.

Orient the equation by +1 if d0>=0 and -1 otherwise, then append an
artificial identity column. Column order is 18 positive parts, 18
negative parts, 88 slacks, 88 artificials: 88 rows and 212 columns.
The artificial basis has nonnegative right side. Save the entire
original/raw model, lift, membership and pulled system before pivoting.
Enter the least indexed nonbasic column of negative reduced cost and
use minimum ratio with least indexed leaving basic variable on ties.
Exact rational Gauss–Jordan operations preserve the initial column order.

The single Phase I reaches artificial sum zero after 280 pivots in
recorded 7.045152249978855 seconds, within 10000 pivots/300 seconds.
No second solve, point scan, retuning, resumed full-row tableau or conic
restart occurs. Initial/final tableaux, transforms, bases and every pivot
are saved in `scripts/finite-support/fixed-column-zero-old-block-initial-state.json`
and `scripts/finite-support/fixed-column-zero-old-block-state.json`.

The complete rational witness is `witness/z` and `witness/raw_moments`
in `scripts/finite-support/fixed-column-zero-old-block-results.json`.
Equivalently it is specified by the deterministic finite pivot recipe
above: nonbasic standard coordinates are zero, basic coordinates are
the final right side, h is the positive-minus-negative part and z=P+N*h.
The full nonnegative standard vector, with zero artificial coordinates,
satisfies every original standard-form row by direct substitution.

Independently of this provenance, substitute the complete 45-vector into
all 28 original/raw equalities and all 88 original/raw inequalities.
Every equality is exactly zero and every inequality is nonnegative,
with precisely the counts in the conclusion. Every raw selected mode
remainder is separately equal to M_i times its scaled slack. The fixed
85 domain factors remain nonnegative and all 90 kernel equations retain
their complete original/weighted residuals. This is a rational certificate,
not a numerical preview, rounded sign, or inferred optimizer verdict.

**Verification and qualifications.** Reproduction commands are

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/fixed_column_zero_old_block.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_fixed_column_zero_old_block.py

Do not rerun the constructor in this completed bounded attempt. Its
redirected original reconstruction passes 1597 exact checks; the new
constructor passes 1215, and the independent verifier passes 415,
all without failures. Full reconstruction is
`scripts/finite-support/fixed-column-zero-old-block-original-reconstruction.json`;
full independent evidence is
`scripts/finite-support/fixed-column-zero-old-block-verification.json`.
The verifier invokes no constructor or optimizer: it independently
selects Z from ancestral original matrices, reconstructs original beta
rows and bounds, checks all ranges, both scaled/raw lift directions,
and every retained original/raw witness substitution. Complete relevant
arrays are consumed; previews and success labels are not evidence.

An initial wrapper stopped before the first tableau because audit-only
rows lack the source/verifier field `original_row`. Its preserved record
is `scripts/finite-support/fixed-column-zero-old-block-pre-pivot-schema-failure.json`.
Correcting that schema mapping changed no mathematical data; no
mathematical comparison failed and no Phase I had run. Inspector calls
needed PYTHONINTMAXSTRDIGITS=0 without changing certificate values.
The separate critical audit below checks full pivot provenance and manuscript
comparison. The claimed finite witness rests on exact substitution; it is
not a completed RS candidate or a full-mode witness.

**Separate critical proof review — step 328, 2026-10-18.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-18-zero-old-block-witness-critical-audit.md`.
Reuse the precise decomposition, singular-Schur and rational-LP citations
above. The audit retains the conditional finite result. It establishes a
reviewed local input using known methods, without source-level novelty
or recursively approving the ancestral PSD, uniqueness, whole-kernel
and normalization hypotheses. Reproduce without a constructor or optimizer:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_fixed_column_zero_old_block.py

The inspected source reconstruction is redirected to
`scripts/finite-support/fixed-column-zero-old-block-critical-source.json`.
All 7993 checks pass. Original pair equations, rho and p8, the original
seven RREF/completion, the immutable dictionary and the entire 85-factor
column family are reconstructed. All 90 original/weighted kernel equations,
500 types and 3000 actual-support presentations, the 36-forced/45-free
partition, 220 two-direction subset transitions, coherent positive
congruences and all 306 old principal minors agree. All 81 original beta
rows, full anchor terms, affine and point ranges and inverse costs are
reconstructed, with singular and empty cases retained. This reused code
evaluates L086's OLD moments as regression controls; those old negative
residuals are not residuals at L090's new witness.

The original/raw verifier is independently rerun into
`scripts/finite-support/fixed-column-zero-old-block-critical-verification.json`.
All 415 checks pass, including the full P,N,F,G identities, positive raw
scales and every retained witness substitution. Its complete bounds,
domain factors, witness and residual arrays equal the original verifier's.
The additional audit has 5291 passing checks and no failures, with full
matrices, row selection, lift, replay and residuals saved in
`scripts/finite-support/fixed-column-zero-old-block-critical-audit.json`.
Complete relevant step-318/320/322/324/326 arrays are consumed and compared
under their respective schemas, not inferred from their hashes or counts.

For every original mode the audit reconstructs the layer set, every old
matrix entry and cross coordinate. All 81 membership records equal the
saved records, and the resulting index list equals the full manuscript
list Z. All 43 selected whole cross vectors vanish, not merely one
coordinate or an inverse cost. Of these modes, 17 have empty old blocks,
20 are already selected equalities and six are additional mixed modes,
precisely 13,22,63,64,65,66. Thus there are 26 nonempty zero old blocks;
the union of Z with the 28 equality indices has 51 elements and leaves
30 other modes. Sano's criterion applies to each selected block: after
its checked zero cross, only its scalar new diagonal remains. No
zero-determinant or rank-label surrogate is used.

Both full augmented lifts are checked in original and raw coordinates:
Q*L=0, R*L=I_19 and L*R-I_46=K*Q, with the corresponding raw identities.
Thus Q*w=0 implies w=L*(R*w), while every L*v satisfies the equalities.
The first augmented coordinate stays one. These identities give all
18 signed free parameters, not only a forward particular solution.
Positive invertible moment scaling gives the same equivalence for raw
moments. No sign on the free parameters is silently introduced.

Every one of the 88 labels, original/raw inequality rows, pulled rows
and row orientations is reconstructed. The 20 selected equality rows
already present in Z and all duplicate/zero pulls are retained. Splitting
h into h_plus-h_minus is reversible over nonnegative standard coordinates;
with artificials zero, the slack is exactly d0+d*h. Reversing a negative
constant reverses the entire equality, including its slack coefficient.
Hence the conversion preserves the whole equality/sign/selected-mode
system. The complete 88-by-212 initial tableau, right side, artificial
identity basis, row transform and empty initial trace agree.

Exactly the saved 280 pivots are replayed. For each, the audit checks the
positive pre-pivot objective, the least-index negative reduced cost,
minimum ratio and least-index leaving-variable tie, positive pivot,
nonnegative updated right side, complete basis identity and exact objective
update. These are invertible rational row operations. Every entry of the
final tableau, right side, basis and row transform agrees. Independently,
U*T_initial=T_final and U*b_initial=b_final hold for the entire matrices.
No new pivot search, optimizer, retuning or stopped full-system restart
is performed; checking the saved choices is separate from solving anew.

The extracted 212-coordinate standard vector equals the saved vector.
It is nonnegative, all 88 artificial coordinates vanish and every original
standard-form equation holds. Its 18 signed coordinates lift exactly to
all 45 saved scaled/raw moments. All 56 original/raw equality residuals
are zero. All 176 original/raw inequality values are nonnegative, and
every selected raw remainder equals its positive normalization times the
scaled slack. The 43 mode slacks have ten positive and 33 zero values;
the 45 moments have 35 positive and ten zero values. Both original/raw
minimum inequalities equal zero, meeting the required lower bound zero.
The complete frozen domain and kernel contracts also remain satisfied.

The preserved pre-pivot schema exception reports zero pivots, zero Phase I
runs and no mathematical comparison failure. Its differing audit-row schema
is handled explicitly. Recorded elapsed-time and cap fields are consistent,
but the audit does not independently observe historical wall time or prove
absence of unrecorded runs. The exact replay certifies mathematical tableau
provenance; independent substitution certifies feasibility even without
that provenance. No mathematical or replay discrepancy was found.

The argument and direct mathematical inputs are unchanged by this audit.
The 30 remaining nonzero-old-block rows are not evaluated at L090's new
witness. Scalar upper rows, other anchors, other columns/base/pairs, global
consistency, representing measures and RS realization remain unresolved.
All fixed-assignment rejections, full-row caps and conic stops are preserved;
no full PSD completion, uniform bound or change to 955–957 follows.

## Mathlib

Full matching fixed-column subsystem feasibility: not checked.
Supporting rational elimination, singular Schur, invariant unequal-layer
and LP results: not checked here. Unknown coverage is not absence.
The known methods are imported by precise citations; no originality
claim is made for this finite specialization.
