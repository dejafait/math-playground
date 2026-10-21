# L092 — The fixed-column zero-block subsystem survives mode (3,4)

## Hypotheses

Use precisely L090's n=1024,w=68 ordinary moment model and frozen L086
columns, with t78=L083's s. The original pair prescription is L021's,
the positive singleton is L053's rho, the included-anchor five/six/seven
base is L073's, and its complete immutable dictionary and seven-column
RREF/completion are L075's. Matrices are divided by rho. Retain L076's
original four-parameter affine column family, all 85 domain rows, all
90 original/weighted kernel equations, 500 full types/3000 presentations,
36 forced eight/eight entries, the entire anchor and

    p8=16792471/1181138102168120460>0.

All ancestral PSD, uniqueness, whole-kernel and coherent-normalization
qualifications in foundations/04,09,10,12 remain conditional imports.
This finite calculation does not recursively audit them.

Only the 45 free eight/eight moments vary. In lexicographic order on
0<=r,q<=8,r+q>=8 put

    V_rq=C(8,r)C(60,r)C(8,q)C(948,q)>0,
    S=diag(p8/V_rq), Y_88(8-r,8-q)=(S*z)_rq.

Impose L084's 28 equalities, all 45 signs z>=0, and L090's 43
entrywise-zero-old-block mode inequalities. Add exactly mode i=31,
(a,b)=(3,4), using L091's full nonzero old block, whole cross vector,
range condition and inverse cost. No other mode, scalar upper row,
other-anchor condition or global moment constraint is added.

## Conclusion

This necessary subsystem has a rational witness at the frozen columns.
All 28 original and 28 raw equalities vanish. All 44 retained original/raw
mode remainders are nonnegative: 11 positive and 33 zero. In particular
the added mode's scaled and raw remainders are exactly zero. All 45
scaled/raw moments are nonnegative, with 35 positive and ten zero.
The minimum original/raw inequality value is exactly zero, meeting
the required lower bound zero. The frozen domain and kernel contracts
still hold.

Thus adding this single nonzero-old-block row does not exclude these
columns under the retained conditions. This is an informative negative
result for that exclusion diagnostic, RESEARCH / REPRODUCTION under
the prior SPECIALIZE assessment, without a source-level novelty claim.
L090's pass and L091's rejection of a different complete assignment
remain valid. The other 29 complementary modes, scalar upper rows,
other anchors/columns/base/pairs, global moments, representing measures
and RS realization remain unresolved. The arbitrary-center 67/68-agreement
gap and 955–957 bracket are unchanged. The separate conditional critical
review below retains this finite witness and its exact saved-trace
provenance, without independently observing historical runtime.

## Proof

**Known methods and specialization.** Reuse exactly the prior assessment
`drafts/literature/2026-10-18-zero-old-block-plus-3-4-subsystem.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7. Ground sets 68,956 and layers 0,5,6,7,8 satisfy its
finite unequal-layer ranges. Retain L078's coherent positive congruence,
both rectangular directions, positive multiplicities and full anchor.
No actual-label averaging or suspect complement prefactor (61) is used.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2 Corollary 2.2, Theorem 2.6 (both singular proof directions),
Lemma 2.7. Finite real symmetric blocks and a scalar new coordinate
are covered. One must retain old PSD and the full cross-vector range,
also for singular nonzero old blocks. A checked solution B*x=c computes
the inverse cost c^T*x: any two solutions differ by a kernel vector,
orthogonal to c in range(B). No quotient pseudoinverse is asserted.

Import Yinyu Ye, *Conic Linear Programming*, revised October 2017,
[monograph](https://web.stanford.edu/class/msande310/sdpmain.pdf),
Theorem 1.11 printed p.13 and Section 1.5.1 pp.23–24, for the assessed
equality/elimination method. For finite rational LP conversion use
MIT 6.854 (2020), [Notes 11](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
Introduction, Linear Equalities and Basic Feasible Solutions; for the
finite feasibility alternative use Michel X. Goemans, *Advanced Algorithms*,
Lecture 3, 19 September 2001, Theorems 1,3 printed pp.1–2,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf).
Pivoting and artificial initialization use Goemans, *An Introduction to
Linear Programming*, October 1994, The Simplex Method pp.7–8,
[notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/908fe54d659623efadda2d033b895caf_notes_lp.pdf),
and Nannicini–Nasrabadi, MIT 15.053 Spring 2013, Recitation 3 solutions,
Problem 3.A–B pp.4–6,
[worked notes](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/05885823def0372adb5eae09c7f5490d_MIT15_053S13_rec03sol.pdf).
The worked initialization supplies no termination or complexity guarantee.
General results are not reproved. The needed finite-system verdict is
absent from those sources and rests on the exact witness substitution below.

**Original row and full added-mode cost.** Binomial coefficients outside
their ordinary range are zero. Use the source convention

    beta(n,l,m,a,t)=sum_(h=max(a,t))^min(l,m,n-a)
      (-1)^(h-t)C(h,t)C(n-2a,h-a)C(n-a-h,l-h)C(n-a-h,m-h).

For i=9a+b use old layers l in {5,6,7} with l>=max(a,b), and
S_l=C(68,l)C(956,l). From the full dictionary reconstruct

    T_lm=sum_(j,k=0)^min(l,m) beta(68,l,m,a,j)beta(956,l,m,b,k)Y_lm(j,k)
         -1_(i=0)*p_l*p_m*S_l*S_m,
    B_i=(T_lm) on old layers, c_i=(T_l8), B_i*x_i=c_i.

Every old entry, affine cross, both rectangular directions, singular/empty
range, forced term and anchor is reconstructed before row selection.
All 306 old principal minors are nonnegative. Select Z entrywise exactly
as in L090: 43 zero old blocks, including all 17 empty blocks, with
the entire selected cross vectors zero. Reconstruct every membership
decision rather than inferring it from a rank or determinant.

Let F_i be the full forced raw beta sum and
H_i=1_(i=0)*p8^2*S_8^2. Put

    D_i=C(68-2a,8-a)C(956-2b,8-b)>0, M_i=p8*D_i>0,
    A_(i,rq)=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)/(D_i*V_rq),
    b_i=(F_i-H_i-c_i^T*x_i)/M_i.

Then the full raw remainder at any free z is

    R_i=F_i-H_i-c_i^T*x_i
        +sum_(rq) beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)*(S*z)_rq
       =M_i*(b_i-A_i*z).

This identity retains every forced entry, full anchor and inverse cost.
For i=31 the old layers are exactly 5,6,7; B_31 is a nonzero 3-by-3
matrix. Enumerate all seven nonempty principal minors and choose the last
nonsingular one in increasing-size, lexicographic order. Cramer's rule
on this minor, with zeros outside it, gives a fresh x_31. Check every
coordinate of B_31*x_31=c_31 and every minor's nonnegativity; its energy
agrees with the saved full inverse action and L091's audited energy.
No nonsingularity assumption is made about the entire old block. The
constructor and independent verifier save this full added block, cross,
fresh inverse, all minors, energy, normalization and bound under
`added_mode` in their respective certificates.

**Complete equality reduction.** Let I={9a+b:0<=a<=6,0<=b<=3},
E=A_I, e=b_I. Specialize L084's quadratic particular solution at the
frozen columns to P, and retain its constant 45-by-18 matrix N. Let
F select its 18 nonpivot coordinates and G have row p_k equal to row k
of the original invertible row transformation, all nonpivot rows zero.
Check every entry of

    E*P=e, E*N=0, F*N=I_18, F*P=0,
    G*e=P, G*E+N*F=I_45.

Hence all and only equality solutions are z=P+N*h, with h=F*z in R^18.
The reverse identity prevents a restricted ansatz. For the raw system
use E_raw=-diag(M_I)*E*S^(-1), e_raw=-diag(M_I)*e,
P_raw=S*P, N_raw=S*N, F_raw=F*S^(-1),
G_raw=-S*G*diag(M_I)^(-1). Both complete raw directions are checked.

In augmented coordinates Q=(-e,E), L=((1,0);(P,N)),
R=((1,0);(0,F)), K=(0;-G), verify

    Q*L=0, R*L=I_19, L*R-I_46=K*Q.

Also verify the full raw counterparts. The augmented first coordinate
remains one. Retain every row, including the 20 equality rows already
among Z and all duplicate/zero pullbacks. No sign is imposed on h.

**Single bounded run and full witness.** Set J=Z union {31}, ordered
increasingly. It has 44 elements, since 31 is in neither Z nor I.
Let H contain all 44 rows (b_i,-A_i), i in J, followed by the 45
coordinate sign rows (0,e_j). All 89 inequalities are pulled back as
H*L; all 28 equalities are retained separately. For each pulled row
d0+d*h>=0 set h=h_plus-h_minus and impose

    -d*h_plus+d*h_minus+slack=d0,
    h_plus,h_minus,slack>=0.

Orient the entire equation, including its slack, by sign +1 for d0>=0
and -1 otherwise. Add one artificial identity column per row. The
standard system has 89 rows and 214 columns, ordered 18 positive parts,
18 negative parts, 89 slacks, 89 artificials. The artificial basis
has nonnegative right side. The full original/raw models, lifts,
membership, labels, orientations and pulled system are saved before
any pivot in `scripts/finite-support/zero-block-plus-3-4-results.json`.

Run exactly one Phase I with a 10000-pivot/300-second cap. Enter the
least-indexed nonbasic column of negative reduced cost; leave by minimum
ratio with least-indexed basic variable on ties. Complete a pivot that
crosses the time bound. The run reaches artificial sum zero after
277 pivots, with recorded finalization time 7.162295291898772 seconds.
There is no second run, retuning, point scan, extra row, full-row restart,
conic restart or budget increase. Entire initial/terminal tableaux,
bases, row transformations and trace are saved in
`scripts/finite-support/zero-block-plus-3-4-initial-state.json` and
`scripts/finite-support/zero-block-plus-3-4-state.json`.

The exact 45-vector is `witness/z`, and its raw vector is
`witness/raw_moments` in the results certificate. They are equivalently
specified by the deterministic recipe above: all nonbasic standard
coordinates zero, basic coordinates equal to the terminal right side,
h equal to the positive-minus-negative parts, z=P+N*h. The complete
214-coordinate vector is nonnegative, all 89 artificial coordinates
are zero, and direct substitution checks every original standard row.

Independently of that provenance, substitute the entire rational z into
all 28 original/raw equalities and all 89 original/raw inequalities.
Every equality residual is exactly zero and every inequality is
nonnegative. For every retained mode verify R_i=M_i*(b_i-A_i*z).
The 44 mode slacks have 11 positive and 33 zero values; i=31 has both
remainders zero. The moments have 35 positive and ten zero values.
Both minimum inequalities equal zero against the required bound zero.
Sano's criterion therefore retains each selected block, under the
imported old PSD and range hypotheses. No omitted mode is tested at
this new witness.

**Evidence and limits.** The completed construction used

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/zero_block_plus_3_4.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_zero_block_plus_3_4.py

Do not rerun the constructor in this completed bounded attempt. The
redirected original reconstruction passes 1597 checks, the constructor
1220, and the independent verifier 421, all without failures. Complete
source and independent evidence are
`scripts/finite-support/zero-block-plus-3-4-original-reconstruction.json`
and `scripts/finite-support/zero-block-plus-3-4-verification.json`.
The source reconstruction's old L086 negative remainders are regression
controls only, not residuals of this witness. It rebuilds the original
RREF family, all domain/kernel rows, full-key presentations and source
blocks. The independent verifier invokes no constructor or optimizer;
it reconstructs every original beta row and bound from the audited
affine source blocks, checks the full added principal solve, both
original/raw equality-lift directions and every retained witness row.
Complete rational arrays, rather than previews or success flags, enter
these checks.

The verdict is conditional finite-subsystem feasibility, not a complete
PSD extension, global moment assignment, packing or RS list. L091
rejects its different complete assignment, not these columns universally.
Preserve ATTEMPTS/071's capped full-row stop and all conic/point stops.
The construction-time arithmetic verification did not itself complete
critical review; the separate review below checks the canonical claim,
complete source coefficients, witness substitutions and saved pivots.

**Separate conditional critical audit, 2026-10-19 (step 336).** Reuse the
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-19-zero-block-plus-3-4-witness-critical-audit.md`
and the precise Schrijver, Sano and rational-elimination/LP citations
above. Their hypotheses remain finite real symmetric blocks, a scalar
new coordinate, and finite rational equality/inequality systems. The
general theorems are imported, not reproved. The result remains conditional
on the ancestral contracts stated in Hypotheses; no recursive ancestor
audit, full-moment feasibility or RS conclusion is claimed.

The source reconstruction rebuilds the original pair prescription and
positive rho,p8, the seven-column RREF and immutable completion, the
four-parameter column family, all 85 domain factors, and all 90 original
and weighted kernel equations. It checks all 500 full types and 3000
actual-support presentations, including all 36 forced entries and all
45 free keys. Fresh orthogonal bases and all 220 direct subset transitions
check both rectangular directions and a coherent positive four-layer
congruence. All 81 complete old blocks, their 306 principal minors,
affine cross ranges, fresh principal solves, inverse costs, forced beta
rows and full anchor terms are reconstructed. The old L086 remainder
checks in this reused source audit are regression controls, not tests
of omitted modes at the L092 witness.

Every one of the 81 entrywise membership decisions agrees with the
original reconstruction and L090's audited membership. Exactly 43 old
blocks vanish entrywise, including all 17 empty blocks, and all selected
whole cross vectors vanish. Their overlap with the selected equalities
has size 20. The only added row is 31, outside both those sets. The
complete B_31,c_31, seven principal minors and fresh three-coordinate
range solve agree with the independent verifier and the fixed data in
L091. The equality of inverse costs is checked as a full rational
identity, not a rank test or numerical approximation.

The independent verifier reconstructs P,N,F,G from L084's original
coefficient arrays and nonpivot coordinates. Both complete augmented
forward and reverse lift identities displayed above hold in original
and raw coordinates. The audit separately checks these identities
against freshly reconstructed Q and H. It retains every one of the
89 pulled rows, its label, orientation, duplicate or zero value and
slack sign, then reconstructs the entire 89-by-214 initial standard
tableau in the prescribed column order.

The audit reads only the saved 277 pivot events. At each event it checks
the positive pre-objective, the declared least eligible entering index,
all earlier reduced costs, the complete minimum-ratio and basic-index
tie comparison, the positive pivot and the leaving basic coordinate.
It performs the stated invertible rational row operation on every
tableau entry and right side, checks the entire new basis identity and
nonnegative right side, and verifies the exact objective update. No
pivot search beyond checking a declared event, new solve or optimization
is performed. The final tableau, basis and right side match in every
entry. Its artificial-column submatrix U is the full row transform:
U times the complete initial tableau equals the final tableau, and U
times the original right side equals the final right side. The final
standard witness has all 214 coordinates nonnegative and all 89
artificials zero, and maps to precisely the saved h,z and raw moments.

Direct original/raw substitution checks all 28 equalities, all 44 mode
rows and all 45 signs. Every equality residual is zero. The mode slacks
have 11 positive and 33 zero values; the moments have 35 positive and
ten zero values. Both minimum inequalities are exactly zero, meeting
the required bound zero. In the added full block let x be the checked
range solution and d its reconstructed new diagonal. The audit verifies
d=c_31^T*x exactly, and saves the complete four-by-four matrix M and

    T = ((I_3,-x);(0,1)), det(T)=1,
    T^T*M*T = diag(B_31,0).

Every entry of this congruence and all 15 nonempty principal minors
of M are checked; the minors are nonnegative. This verifies the added
singular case directly without assuming invertibility of B_31. The
other 29 complementary remainders at this new witness are not evaluated.

Reproduce this certificate audit, without rerunning the constructor:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_zero_block_plus_3_4.py

All 7993 source-reconstruction, 421 independent original/raw-verifier
and 2437 additional audit checks pass. Full exact evidence is saved in
`scripts/finite-support/zero-block-plus-3-4-critical-source.json`,
`scripts/finite-support/zero-block-plus-3-4-critical-verification.json`
and `scripts/finite-support/zero-block-plus-3-4-critical-audit.json`.
The latter contains both complete lifts, original/raw systems, all replay
checks and terminal arrays, retained witness residuals and the full
added-block congruence and minors. Mathematical checks consume complete
rational arrays, not certificate previews or saved success labels.

The first audit invocation completed the source and witness checks but
raised a schema `KeyError: 'original_row'` while comparing L091 data,
before any saved pivot replay. Its script and exception are preserved in
`scripts/finite-support/critical_audit_zero_block_plus_3_4_initial.py`
and `scripts/finite-support/zero-block-plus-3-4-critical-audit-schema-failure.json`.
The corrected comparison uses L091's full B,c,energy and normalization
fields; every original coefficient and bound is still independently
reconstructed and compared elsewhere. This tooling correction drops
no mathematical condition and restarts no optimization. The exact trace
is verified, but its saved elapsed time and single-run historical claim
are not independently observed facts. L090's pass, L091's distinct
rejection, the full-row/conic stops and all unresolved conditions remain
unchanged. No progress beyond the assessed source methods is claimed.

## Mathlib

Full matching finite subsystem feasibility: not checked. Supporting
singular Schur, unequal-layer decomposition, rational elimination and
LP results: not checked here. Unknown coverage is not absence. The
general methods are imported by precise citations without novelty claims.
