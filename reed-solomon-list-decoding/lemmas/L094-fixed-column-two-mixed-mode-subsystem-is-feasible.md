# L094 — Both prescribed mixed rows survive at the fixed columns

## Hypotheses

Use the ordinary union-moment model at n=1024,d=10,w=68 with matrices
divided by L053's positive rho. Retain L021's original pairs, L073's
included-anchor five/six/seven base, L075's entire immutable dictionary
and seven-column RREF/completion, L076's original affine column family,
and precisely L086's columns with t78=L083's s. In particular

    p8=16792471/1181138102168120460>0.

Keep all 85 domain rows, 90 original/weighted kernel equations, 500 full
types/3000 presentations, 36 forced eight/eight entries, full anchor,
whole singular ranges and L078's coherent positive normalization.
Foundations/04,09,10,12's ancestral PSD, uniqueness, whole-kernel and
normalization qualifications remain conditional imports; this finite
calculation is not their recursive critical audit.

Vary only the 45 free eight/eight moments. In lexicographic order on
0<=r,q<=8,r+q>=8 use

    V_rq=C(8,r)C(60,r)C(8,q)C(948,q)>0,
    S=diag(p8/V_rq), Y_88(8-r,8-q)=(S*z)_rq.

Retain L084's 28 selected equalities, all 45 signs z>=0 and L090's
43 entrywise-zero-old-block mode rows. Add exactly the two nonzero-old-
block modes i=23=(2,5) and i=31=(3,4), with i=9a+b. Keep their complete
old blocks, cross vectors, range conditions and inverse costs as in
L091–L093. Other mode inequalities, scalar upper rows, other anchors
and global moment conditions are not imposed here.

## Conclusion

This fixed-column necessary subsystem has a rational witness. All 28
original and 28 raw equalities vanish. All 45 retained mode remainders
are nonnegative, with 14 positive and 31 zero. The new row (2,5) has
exactly zero original/raw remainder. For the simultaneously retained
row (3,4), its original normalized remainder satisfies

    153320960 <= b_31-A_31*z < 153320961.

All 45 original/raw moments are nonnegative, with 33 positive and 12
zero. The minimum original and raw inequality values are exactly zero,
meeting the required lower bound zero. All frozen column contracts hold.

Thus these two mixed rows together do not exclude L086's columns under
the retained conditions. This is RESEARCH / REPRODUCTION of assessed
methods and an informative negative result for this exclusion diagnostic,
not a claim of progress beyond the sources checked. L092's different
witness and L093's rejection of that complete assignment remain valid.
The other 28 complementary modes, scalar upper rows, other anchors,
columns/base/pairs, global moments, representing measures and RS
realization remain unresolved. The arbitrary-center 67/68-agreement gap
and 955–957 bracket are unchanged. The separate conditional critical
proof and saved-trace review below retains this subsystem. Historical runtime and the single-run claim are
not independently observed by replay.

## Proof

**Known inputs and specialization.** Reuse the pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-19-fixed-column-two-mixed-mode-subsystem.md`.
Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7, covers these finite unequal-layer restrictions on ground
sets 68,956 and layers 0,5,6,7,8. Retain both rectangular directions,
positive multiplicities and the full anchor. Neither actual-label
averaging nor the suspect complement prefactor (61) is used.

Takashi Sano, *Moore-Penrose inverse, generalized Schur complement and
inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2 Corollary 2.2, Theorem 2.6 (including both singular proof
directions), Lemma 2.7, applies to finite real symmetric blocks with a
scalar new coordinate. It requires old PSD, the whole cross vector in
the old range, and nonnegative Schur remainder. For any verified B*x=c,
the inverse cost is c^T*x; another solution differs by a kernel vector
orthogonal to c. No quotient pseudoinverse or full-block invertibility
assumption is used.

The ordinary moment model is Sven C. Polak, *Semidefinite Programming
Bounds for Constant-Weight Codes*, IEEE TIT 65 (2019), 28–38,
DOI 10.1109/TIT.2018.2854800,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1 and indicator proof p.2, Section
1.2 p.3. Retain constant weight and constraint-preserving averaging;
no representing measure or RS realization is imported.

For equality elimination import Yinyu Ye, *Conic Linear Programming*,
revised October 2017, [monograph](https://web.stanford.edu/class/msande310/sdpmain.pdf),
Theorem 1.11 printed p.13, Section 1.5.1 pp.23–24. For rational standard
form use MIT 6.854 (2020), [Notes 11](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
Introduction, Linear Equalities and Basic Feasible Solutions. The finite
alternative is Michel X. Goemans, *Advanced Algorithms*, Lecture 3,
19 September 2001, Theorems 1,3 printed pp.1–2,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf).
Pivoting/initialization use Goemans, *An Introduction to Linear Programming*,
October 1994, The Simplex Method pp.7–8,
[notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/908fe54d659623efadda2d033b895caf_notes_lp.pdf),
and Nannicini–Nasrabadi, MIT 15.053 Spring 2013, Recitation 3 solutions,
Problem 3.A–B pp.4–6,
[worked notes](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/05885823def0372adb5eae09c7f5490d_MIT15_053S13_rec03sol.pdf).
No general theorem is reproved. None supplies this finite witness or a
bounded termination guarantee; exact substitution decides the result.

**Complete original and raw rows.** C(n,k) is zero outside its ordinary
range. Use

    beta(n,l,m,a,t)=sum_(h=max(a,t))^min(l,m,n-a)
      (-1)^(h-t)C(h,t)C(n-2a,h-a)C(n-a-h,l-h)C(n-a-h,m-h).

Put S_l=C(68,l)C(956,l). For i=9a+b use old layers l in {5,6,7}
with l>=max(a,b), and reconstruct from the full fixed raw dictionary

    T_lm=sum_(j,k=0)^min(l,m) beta(68,l,m,a,j)beta(956,l,m,b,k)Y_lm(j,k)
         -1_(i=0)*p_l*p_m*S_l*S_m,
    B_i=(T_lm), c_i=(T_l8), B_i*x_i=c_i.

All original pairs, column RREF, domain factors, kernel equations, full
keys and six presentations are reconstructed. Both rectangular directions,
every affine range coefficient and all 306 old principal minors are
checked. Fresh principal solves give whole-range solutions and costs,
including empty/singular cases. For each added i in {23,31}, B_i is
three-by-three. Enumerate its seven nonempty principal minors in
increasing size and lexicographic order; choose the last nonsingular
principal minor, solve it by Cramer's rule and fill zeros outside it.
Every coordinate of B_i*x_i=c_i is checked, all minors are nonnegative,
and the cost agrees with the full saved affine inverse action and
L091/L093's complete fixed-block data. Neither nonzero block is assumed
invertible. The full blocks, cross vectors, fresh inverses, minors,
energies and normalizations are saved under `added_modes` in both the
constructor and independent verification certificates.

Let F_i be the complete forced raw diagonal sum and
H_i=1_(i=0)*p8^2*S_8^2. Define

    D_i=C(68-2a,8-a)C(956-2b,8-b)>0, M_i=p8*D_i>0,
    A_(i,rq)=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)/(D_i*V_rq),
    b_i=(F_i-H_i-c_i^T*x_i)/M_i.

The full raw Schur remainder at any z is

    R_i=F_i-H_i-c_i^T*x_i
        +sum_(rq) beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)*(S*z)_rq
       =M_i*(b_i-A_i*z).

The source reconstruction checks every coefficient, forced term, full
anchor and cost before selecting rows. Determine Z by testing every
entry of each entire B_i for zero; empty blocks are included. Exactly
43 modes qualify, including all 17 empty modes, and every selected
whole c_i vanishes. Set I={9a+b:0<=a<=6,0<=b<=3} and
J=Z union {23,31}. Both added modes lie outside I union Z. Thus |J|=45,
|I intersect Z|=20, |I union J|=53, with 28 complementary modes.
No overlapping counts or zero/duplicate pullbacks are discarded.

**Full equality locus.** Let E=A_I,e=b_I. Specialize L084's quadratic
particular solution to P at the frozen columns and retain its constant
45-by-18 matrix N. Let F select the 18 nonpivot coordinates. Let G have
row p_k equal to row k of L084's invertible row transform, with all
nonpivot rows zero. Check completely

    E*P=e, E*N=0, F*N=I_18, F*P=0,
    G*e=P, G*E+N*F=I_45.

It follows that z=P+N*h, h=F*z ranges over all equality solutions,
not just a particular family. In augmented coordinates set

    Q=(-e,E), L=((1,0);(P,N)), R=((1,0);(0,F)), K=(0;-G).

Then Q*L=0, R*L=I_19 and L*R-I_46=K*Q. All entries are checked.
For raw coordinates use Q_raw=-diag(M_I)*Q*diag(1,S)^(-1),
L_raw=diag(1,S)*L, R_raw=R*diag(1,S)^(-1), and
K_raw=-diag(1,S)*K*diag(M_I)^(-1). The same complete forward/reverse
identities hold. The augmented first coordinate remains one.

**Single bounded construction and witness verification.** Stack the 45
rows (b_i,-A_i), i in J in increasing order, then the 45 sign rows
(0,e_j), to form H. Its 90 inequalities are H*(1,z)>=0. The raw mode
rows are M_i times their original rows after applying S^(-1), and raw
signs are the unscaled coordinate signs. Pull every row through L.
For each d0+d*h>=0, split h=h_plus-h_minus and impose

    -d*h_plus+d*h_minus+slack=d0.

Orient the whole equation, including its slack, by +1 if d0>=0 and
-1 otherwise; add one artificial identity column per row. Order the
216 coordinates as 18 positive parts,18 negative parts,90 slacks,
90 artificials. Artificial columns begin at index 126. The artificial
basis is feasible. The full original/raw model, both lift directions,
row labels, orientations and pulled inequalities are saved before pivots.

Run precisely one Phase I, entering the least eligible negative-reduced-
cost column and leaving by minimum ratio with least basic index on ties.
The cap is 10000 pivots/300 seconds, completing a pivot that crosses the
time threshold. The actual run reaches zero artificial sum after 317
pivots; recorded finalization time is 13.55773904104717 seconds.
No second run, scan, retuning, extra row, full-row/conic restart or
budget increase occurs. A guard rejects invoking this constructor once
its saved evidence exists. Complete initial/terminal tableaux, bases,
row transforms and every pivot are saved in
`scripts/finite-support/two-mixed-row-initial-state.json` and
`scripts/finite-support/two-mixed-row-state.json`.

The complete rational witness is `witness/z`, with raw vector
`witness/raw_moments`, in
`scripts/finite-support/two-mixed-row-results.json`. Equivalently it is
specified by the deterministic construction above: set nonbasic standard
coordinates to zero and basic coordinates to the terminal right side,
subtract the two 18-vectors to obtain h, and set z=P+N*h. Every one of
the 216 standard coordinates is nonnegative, all 90 artificials vanish,
and the original 90 standard equations hold exactly.

Independently of the pivot provenance, substitute this full z into all
28 original/raw equalities, 45 retained original/raw mode rows and all
45 signs. All 56 equality residuals vanish; every inequality is
nonnegative. Every retained raw mode remainder equals M_i times its
original remainder. There are 14 positive and 31 zero mode remainders;
row 23 is zero and row 31 is positive with the integer interval stated
in Conclusion, checked by exact rational comparison. There are 33
positive and 12 zero moments, and both minimum inequalities equal zero.
Sano's criterion therefore retains each selected block, under the stated
ancestral contracts. No omitted mode at this new witness is evaluated.

Reproduce arithmetic verification without rerunning Phase I:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_two_mixed_row.py

The construction uses `two_mixed_row.py` in the same directory; its
completed single run must not be restarted. The original reconstruction
passes 1597 checks, the constructor 1229, and the independent verifier
426, with zero failures. The verifier invokes no constructor or optimizer;
it separately reconstructs original beta rows and full bounds from the
audited affine source blocks, both added principal solves and both
original/raw lift directions, and substitutes every retained witness
coordinate. Complete exact evidence is
`scripts/finite-support/two-mixed-row-original-reconstruction.json` and
`scripts/finite-support/two-mixed-row-verification.json`.
The original reconstruction's L086 failures and L092 regression controls
are tests of older assignments, not failures of this new witness.
All mathematical checks consume complete rational arrays, not previews.
The independent verifier was rerun only to add the exact manuscript
interval/zero check; this did not rerun Phase I or change the witness.

This witness parks only this two-row necessary-subsystem exclusion test.
It neither supplies full simultaneous PSD, a global moment extension,
a packing nor an RS list. The capped full-row and conic prescriptions
remain stopped. Construction-time arithmetic verification alone did not complete
dedicated critical proof/trace review. The separate audit below supplies
that finite review, while ancestral contracts remain conditional.

**Separate conditional critical audit, 2026-10-19 (step 344).**
The pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-19-two-mixed-row-witness-critical-audit.md`
covers exactly this witness and saved trace. The methods and precise
source citations above are reused; no theorem is reproved, no source-level
novelty is claimed, and no recursive ancestral audit is inferred.

The independent source reconstruction rebuilds the original pair
prescription, positive rho and p8, seven-column RREF and completion,
entire old dictionary and L076 affine family. It reconstructs all 85
domain factors and all 90 original/weighted kernel equations, actual
68-subsets realizing all 500 types and every one of their 3000 ordered
presentations, and the 36 forced/45 free eight/eight partition. Monic
orthogonal bases and all 220 subset transitions in both rectangular
directions independently check the coherent positive congruence with
the beta normalization. All affine whole-range equations, complete
anchor corrections and all 306 old principal minors agree. Its old
L086 residual evaluations are regression controls only; no omitted row
is evaluated at L094's moments.

The audit compares complete coefficient arrays with the L094 original
reconstruction and a fresh independent original/raw verifier. Entrywise
zero tests on all 81 old blocks select exactly the same 43 modes, whose
whole cross vectors vanish. The 17 empty modes remain included. The two
added indices 23,31 lie outside both this set and the 28 equality indices;
there are 45 retained inequalities, 20 equality/zero-block overlaps and
28 untested complementary modes. Fresh principal solves independently
check both three-by-three old PSD blocks, every range coordinate and
inverse cost, including singularity. No nonzero-block invertibility is
assumed. The complete original/raw forward and reverse equality lifts
are verified, so all equality solutions, not merely the exhibited one,
are represented. All 90 retained inequalities, including zero or duplicate
pullbacks, signs, row labels and orientations agree.

From these reconstructed rows the audit builds the entire 90-by-216
initial tableau, right side and artificial basis with index start 126.
It replays only the saved 317 pivots. At each pivot it checks the positive
artificial objective, negative entering reduced cost and absence of an
eligible smaller index; all positive-column minimum ratios and the
least-basic-index tie rule; the exact positive pivot; every row operation;
nonnegative right sides; all basis identity entries; and the exact
objective update. Thus degeneracy is allowed without a convergence
assumption. No pivot is searched for beyond the recorded sequence.
The final tableau, basis and row transform agree entrywise. If T0,b0
are the initial tableau and right side and U the final transform, the
complete identities U*T0=T and U*b0=b are checked. The terminal standard
vector has all 216 coordinates nonnegative and all 90 artificials zero,
satisfies every original standard equation and lifts to exactly L094's
saved h,z and raw moments. These checks establish exact saved provenance,
not independently observed historical runtime or uniqueness of the run.

Independently of that provenance, the same full witness is substituted
into every original/raw equality, retained mode and sign. All 56 equality
residuals vanish. Mode remainders are 14 positive and 31 zero; moments
are 33 positive and 12 zero. Both minimum inequality values are zero.
Row23 has exactly zero raw and normalized remainder; row31's normalized
remainder is verified in [153320960,153320961). Every raw mode remainder
is exactly M_i times its normalized value, with M_i>0.

The audit additionally reconstructs each complete four-by-four added
block K_i=[[B_i,c_i],[c_i^T,d_i]]. With the freshly checked B_i*x_i=c_i,
set P_i=[[I,-x_i],[0,1]]. Direct multiplication checks det(P_i)=1 and

    P_i^T*K_i*P_i = diag(B_i,d_i-c_i^T*x_i).

For both i=23,31, all 15 nonempty principal minors of K_i are also
computed directly and are nonnegative. The last diagonal entry is the
same raw remainder already verified; it is zero for 23 and positive
for 31. These complete identities retain all cross coordinates and handle both
old-block cases: B_23 has strictly positive determinant and is nonsingular,
whereas B_31 has determinant zero and is singular. Thus the cited
singular-Schur criterion applies without a uniform invertibility assumption.
The zero-old-block rows use the checked zero whole cross vector and
nonnegative scalar remainder. Equality-only retained modes also have
checked old PSD, whole range and zero remainder. This proves exactly
the claimed necessary-subsystem pass under the imported contracts.

The completed audit command was

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_two_mixed_row.py

It calls no constructor or optimizer and refuses to overwrite its main
audit evidence without inspection. All 7993 source-reconstruction checks,
426 fresh original/raw-verifier checks and 2725 additional manuscript,
model, trace and full-block checks pass, with no failures. Full rational
arrays, both full blocks and all 30 minors, congruences, complete replay,
final transform, witness and residuals are saved in
`scripts/finite-support/two-mixed-row-critical-audit.json`; source and
verifier evidence are respectively
`scripts/finite-support/two-mixed-row-critical-source.json` and
`scripts/finite-support/two-mixed-row-critical-verification.json`.
The complete arrays are consumed by exact arithmetic, not inferred from
previews or success flags. The saved log is
`scripts/finite-support/two-mixed-row-critical-run.log`. A four-check
supplement, `scripts/finite-support/inspect_two_mixed_row_block_ranks.py`,
recomputes both complete determinants and their signs from the audited
matrices; all four checks pass, with full evidence in
`scripts/finite-support/two-mixed-row-critical-block-classification.json`.
This corrects the audit scope's informal reference to both old blocks as
singular; the construction, range tests and witness require no such
assumption and are unchanged.

This separate review retains the conditional finite input and the stop
on two-row exclusion. It supplies no full simultaneous PSD, scalar upper
row, other-anchor, global-moment, packing, RS-list or boundary conclusion.
The full-row/conic caps and all prior fixed-assignment rejections remain
unchanged; the 28 complementary modes were not tested at this witness.

## Mathlib

Full matching finite two-row subsystem witness: not checked. Supporting
singular Schur, unequal-layer decomposition, equality elimination and
rational LP results: not checked here. Unknown coverage is not absence.
General methods are imported by the precise citations above.
