# L088 — The fixed-column equality/new-only/sign subsystem is feasible

## Hypotheses

Retain exactly L076,L078,L082,L083,L084,L086,L087's original ordinary
moment slice: n=1024,w=68, L021's pair prescription, L053's positive
singleton rho, and matrices divided by rho. The included-anchor
five/six/seven base is L073's, with L075's entire immutable dictionary,
original seven-column RREF/completion and

    p8=16792471/1181138102168120460>0.

All ancestral PSD, uniqueness, whole-kernel-exhaustion and coherent
source-normalization qualifications remain imported. This finite
calculation is not a recursive critical audit of those inputs.

Freeze the columns to precisely L086's rational column parameters:
take the first four coordinates of `witness/original` in
`scripts/finite-support/affine-sign-phase-one-results.json` as
(1,t56,t63,t69), and set t78 to L083's exact stationary s. All these
coordinates are consumed as complete numerator/denominator pairs.
Keep the 85 original domain rows, all 90 weighted kernel equations,
500 full unordered types/3000 presentations, 36 forced eight/eight
entries, full anchor and all original pair values. Only the 45
unrepresented eight/eight moments may change.

Index these 45 signed real coordinates z lexicographically by (r,q),
0<=r,q<=8, r+q>=8. Preserve the positive raw scaling

    V_rq=C(8,r)C(60,r)C(8,q)C(948,q),
    S=diag(p8/V_rq), Y_88(8-r,8-q)=(S*z)_rq.

C(n,k) is zero outside 0<=k<=n. Require all 28 selected equalities
from L084, the 17 original modes indexed by i=9a+b with max(a,b)=8,
and all 45 signs z>=0. The selected indices are
I={9a+b:0<=a<=6,0<=b<=3}. These sets are disjoint. No other mode,
scalar upper row, other-anchor PSD condition or global moment extension
is imposed in this subsystem.

## Conclusion

There is an explicit rational witness for this subsystem at these
unchanged columns. All 28 original equalities and all 28 unnormalized
raw equalities have residual zero. All 17 original/raw new-only modes
are nonnegative: 11 have positive slack and six have zero slack.
Exactly 31 of the 45 scaled/raw moments are positive and 14 are zero.
The minimum original and raw retained inequality values are both zero,
meeting the required lower bound zero.

Thus the new-only modes together with the tight equalities and signs
cannot exclude these fixed columns. L087's rejection of the different,
unchanged L086 moment assignment remains valid. The 36 omitted mixed
mode inequalities have not been evaluated at this new witness. Other
plane points, scalar upper rows, other anchors, global consistency,
representing measures and RS realization remain unresolved. In
particular this is no full PSD completion, uniform family bound or
improvement of the 955–957 bracket.

This is a local RESEARCH / REPRODUCTION specialization of known exact
LP methods, an informative negative result for this exclusion test.
No discovery beyond the sources checked is claimed. The separate
critical proof review below retains this finite result with its
ancestral qualifications.

## Proof

**Imported results and scope.** The pre-invocation SPECIALIZE assessment
is `drafts/literature/2026-10-18-fixed-column-new-only-face-feasibility.md`.
Reuse Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7. The ground sets 68 and 956 and principal layer
restriction 0,5,6,7,8 meet its unequal-layer hypotheses. Retain L078's
coherent positive congruence, both rectangular directions and singular
cases; the suspect complement prefactor (61) is unused. Every new-only
mode has an empty old block and no anchor, as independently checked.

The interpretation of the selected equalities retains Takashi Sano,
*Moore-Penrose inverse, generalized Schur complement and inertia*,
version of record 27 February 2026,
[Section 2](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Corollary 2.2, Theorem 2.6 and Lemma 2.7. The original real symmetric
PSD base and full kernel compatibility are qualified inputs; the full
anchor remains in every selected equality. Ordinary equal-union
moments retain Sven C. Polak,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Sections 1.1–1.2, Proposition 1.1 and its indicator proof p.2. Its
proof gives the constant-weight conclusion despite the displayed
notation. No actual-label constraint is averaged.

Import the finite free-variable LP alternative from Michel X. Goemans,
*Advanced Algorithms*, Lecture 3, 19 September 2001, Theorems 1 and 3,
printed pp.1–2,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf).
Free-variable splitting, slacks and rational standard-form solutions
are covered by MIT 6.854 (2020 compilation),
[Notes 11](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
Introduction, Linear Equalities and Basic Feasible Solutions. For
pivoting reuse Goemans, *An Introduction to Linear Programming*,
October 1994, The Simplex Method pp.7–8,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/908fe54d659623efadda2d033b895caf_notes_lp.pdf),
and Nannicini–Nasrabadi, MIT 15.053 Spring 2013, *Recitation 3 solutions*,
Problem 3.A–B pp.4–6,
[worked initialization](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/05885823def0372adb5eae09c7f5490d_MIT15_053S13_rec03sol.pdf).
The worked example is not a convergence or complexity theorem. No
general result is reproved: these sources do not evaluate this finite
shared-moment subsystem, which requires exact specialization. Direct
original/raw substitution, rather than simplex termination, proves
the conclusion.

**Original system reconstructed before solving.** Use exactly

    beta(n,l,m,a,t)=sum_(h=max(a,t))^min(l,m,n-a)
      (-1)^(h-t)C(h,t)C(n-2a,h-a)C(n-a-h,l-h)C(n-a-h,m-h).

For every i=9a+b, retain L082/L083's original source base B_i, cross
vector c_i(t), inverse action x_i(t), forced term F_i(t), anchor H_i,
and positive D_i=C(68-2a,8-a)C(956-2b,8-b). Their original normalization is

    b_i=F_i-H_i-c_i^T*x_i/(p8*D_i),
    A_(i,rq)=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)/(D_i*V_rq).

All source range equations B_i*x_i=c_i are checked, including
singular/empty cases. The fresh full-key reconstruction preserves
every frozen column/domain/kernel/presentation contract. Complete
original and raw coefficients agree with step 316's saved full system;
its stopped tableau is consumed as historical evidence only and is
not resumed. In particular E=A_I and e=b_I give the 28 equalities
E*z=e, with their original full-anchor right sides.

For J={9a+b:max(a,b)=8}, |J|=17, the necessary inequalities are
b_i-A_i*z>=0. Their unnormalized raw remainders are

    p8*D_i*b_i + sum_(rq)
      beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)Y_rq.

They equal p8*D_i*(b_i-A_i*z). In J both old range cost and anchor
are zero; forced terms remain. The selected equality raw residuals
have the identical formula, with required value zero. All 81 original
bounds are reconstructed for coordinate comparison, but only the
approved 28 equalities and 17 inequalities are tested at the new witness.

**Both directions of the specialized equality lift.** Evaluate L084's
complete particular coefficient matrix at (1,t56,t63,t69), with its
specified quadratic monomial order, obtaining P in Q^45. Let N be its
45-by-18 homogeneous matrix, F the 18-by-45 selector of its nonpivot
coordinates, and G the 45-by-28 matrix whose row at pivot p_k is row k
of L084's row transform U, with other rows zero. Exact checks give

    E*P=e, E*N=0, F*N=I_18, F*P=0,
    G*e=P, G*E+N*F=I_45.

These are compared with L086's saved full lift and reverse multipliers
at the frozen columns. Hence z=P+N*h describes every solution, with
h=F*z uniquely determined and completely signed. No positivity is
imposed on h and no equality is deleted because of rank 27.

For the unnormalized raw equations set M=diag(p8*D_i:i in I),
E_raw=-M*E*S^(-1), e_raw=-M*e, P_raw=S*P, N_raw=S*N,
F_raw=F*S^(-1), G_raw=-S*G*M^(-1). All entries of S and M are
positive. Every raw forward and reverse identity is checked:

    E_raw*P_raw=e_raw, E_raw*N_raw=0,
    F_raw*N_raw=I, F_raw*P_raw=0,
    G_raw*e_raw=P_raw, G_raw*E_raw+N_raw*F_raw=I_45.

In augmented coordinates w=(1,z), v=(1,h), use

    Q=(-e,E), L=( (1,0) ; (P,N) ),
    R=( (1,0) ; (0,F) ), K=( 0 ; -G ).

The full exact identities Q*L=0, R*L=I_19 and L*R-I_46=K*Q are
also saved. These are the specialized complete-locus contract, not
merely a forward feasible-point construction.

**Single bounded calculation and complete witness.** Let H have the
17 rows (b_i,-A_i), i in J in increasing order, followed by all 45
coordinate sign rows (0,e_j). Set d=H*L, retaining every one of its
62 rows, even if zero or duplicate. For each row d0+d'*h>=0 introduce
h=h_plus-h_minus with 18 coordinates in each nonnegative part and

    -d'*h_plus+d'*h_minus+slack=d0.

Multiply this equality by +1 for d0>=0 and by -1 otherwise, and append
one positive artificial coordinate per oriented row. The initial
matrix has 62 rows and 160 columns, ordered 18 positive parts, 18
negative parts, 62 slacks and 62 artificials. Its artificial identity
basis has nonnegative right side. The full original/raw system,
equality lift, row labels and pulls are saved before the first pivot.

Minimize the artificial sum in exact rational arithmetic. Enter the
least indexed nonbasic coordinate with negative reduced cost; use
the exact minimum ratio and least indexed leaving basic variable on
ties. Column numbers never change. This one run reaches objective
zero after 233 pivots, in recorded 6.208 seconds, below 10000 pivots
and 300 seconds. No second run, scan, warm start, retuning or changed
variable bound occurs. Initial/final tableaux, row transforms and the
entire pivot trace are saved in
`scripts/finite-support/fixed-column-new-only-initial-state.json` and
`scripts/finite-support/fixed-column-new-only-state.json`.

The witness is canonically specified by the complete rational arrays
`witness/z` and `witness/raw_moments` in
`scripts/finite-support/fixed-column-new-only-results.json`. Equivalently,
the deterministic 233-pivot recipe above specifies those arrays without
an optimization oracle. At the final tableau set nonbasic coordinates
to zero and basic coordinates to the saved rational right side. The
resulting 160-vector is nonnegative, has all artificial coordinates zero
and directly satisfies every original standard-form equation. Its
positive-minus-negative h lifts through P+N*h to precisely the saved z.

Independent of that algorithmic provenance, complete direct substitution
at this rational z checks all 28 E*z-e residuals and all 28 raw residuals
are zero, all 17 b_i-A_i*z values and their unnormalized raw remainders
are nonnegative, and all 45 coordinates z and S*z are nonnegative.
The exact counts are those in the conclusion. All 85 frozen domain
factors remain nonnegative, with original and weighted kernel contracts
unchanged. The minimum required inequality value is zero and the
achieved minima are zero, with no tolerance or rounded coefficient.

**Reproduction, verification and limits.** The completed run and its
independent verification are reproduced from the notebook by

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/fixed_column_new_only.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_fixed_column_new_only.py

Do not rerun the constructor as part of this completed bounded attempt.
Its redirected original-system reconstruction passes 1597 exact checks,
and it records 155 additional checks, all with no failures. Its full
fresh reconstruction is
`scripts/finite-support/fixed-column-new-only-original-reconstruction.json`.
The independent verifier invokes neither constructor nor solver. It
reconstructs the original beta rows and bounds from ancestral
cross/inverse/forced/anchor arrays, the frozen domain/kernel equations,
both equality-lift directions and all original/raw witness residuals.
It passes 254 exact checks with no failures; complete evidence is
`scripts/finite-support/fixed-column-new-only-verification.json`.
All load-bearing arrays are read in full, not inferred from previews
or earlier success labels. The verifier does not critically replay
all 233 pivots; the separate review below supplies that check.

This proves nonemptiness only of the stated necessary subsystem. The
other 36 mixed inequalities were omitted from solving and from new
witness substitution. No Slater hypothesis, representing measure,
common-center list, full-system feasibility or strict uniform bound is
inferred. Preserve the unreduced full-row cap and both conic stops,
which concern different prescriptions and remain inconclusive.

**Separate critical proof review — step 320, 2026-10-18.** Reuse the
pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-18-fixed-column-new-only-critical-audit.md`
and the precise decomposition, singular-Schur and rational-LP citations
above. The conditional audit retains this finite witness. It establishes
a reviewed local input, not new mathematics beyond the inspected sources
or a recursive approval of ancestral PSD, uniqueness, whole-kernel or
source-normalization claims. Reproduce without a constructor or optimizer:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_fixed_column_new_only.py

The inspected L087 audit implementation reconstructs the unchanged
source recipes into
`scripts/finite-support/fixed-column-new-only-critical-source.json`.
All 7993 checks pass. It rebuilds rho, original pairs and p8, the seven
RREF/completion and immutable dictionary, the 85-factor family, all
90 weighted kernel equations, all 500 types/3000 actual-support
presentations and the 36-forced/45-free partition. Independent monic
orthogonal bases, every one of the 220 subset transitions in both
rectangular directions and coherent positive congruences recover all
81 original beta rows and bounds, including the entire anchor and every
singular/empty case. This reused reconstruction evaluates L086's OLD
moments as its regression control; its negative values are not values
at L088's new moments. Every coefficient and bound is compared with
step 318 and the full step-316 original system before new substitution.

The original/raw verifier is rerun into
`scripts/finite-support/fixed-column-new-only-critical-verification.json`.
All 254 checks pass, and its complete bounds, domain factors, witness
and residual arrays agree with the original verification. In particular
the full P,N,F,G identities, not merely a forward particular solution,
are reconstructed. The audit additionally verifies all augmented forward,
left-inverse and reverse identities in both coordinate systems. Since
R*L=I and L*R-I=K*Q, every original equality solution w with Q*w=0
satisfies w=L*(R*w); the raw identities give the same conclusion after
the positive invertible diagonal scaling. Thus no hidden restriction
on the 18 signed free coordinates is introduced.

The additional 1907 audit checks pass, with complete evidence in
`scripts/finite-support/fixed-column-new-only-critical-audit.json`.
All 62 labels, original/raw rows, pulled rows and row orientations are
reconstructed. Splitting each signed coordinate into a difference of
nonnegative coordinates is reversible, and setting the slack equal to
the original row value proves both directions of the standard-form
conversion when artificials vanish. Negative constants reverse the
entire equality, including its slack coefficient. Zero and duplicate
rows are retained. The entire 62-by-160 initial tableau, nonnegative
right side, artificial identity basis and empty initial trace agree.

The audit replays exactly the 233 saved choices. At every step it checks
the positive pre-pivot objective, least-index negative reduced cost,
minimum ratio and least-index leaving-variable tie, exact positive
pivot, all nonnegative basic values, complete basis identity and exact
objective update. No new pivot sequence or solver is run. All final
tableau entries, right sides and basis coordinates agree. The artificial
columns give the full row transformation U; the audit also directly
checks U*T_initial=T_final and U*b_initial=b_final. Each replayed pivot
is a nonzero-pivot invertible row operation, so these checks retain the
whole standard system rather than only the extracted feasible point.

Setting all nonbasic coordinates to zero gives exactly the saved
160-vector. Every coordinate is nonnegative, all 62 artificial values
are zero, and every original standard equation holds. Its signed
18-vector lifts to the complete saved 45-vector and positively scaled
raw moments. Independent direct substitution checks all 56 original/raw
equality residuals are zero and all 124 original/raw retained inequality
values are nonnegative. The 17 mode slacks have exactly 11 positive
and six zero values; the 45 moments have 31 positive and 14 zero values.
Both minimum inequality values are zero against required lower bound
zero. The unchanged 85 domain factors and 90 kernel equations pass.

Recorded limits and elapsed-time fields agree with the declared caps;
the exact replay establishes mathematical tableau provenance, not an
independent observation of historical runtime or the absence of other
unrecorded runs. Those historical claims are not needed for nonemptiness.
No mathematical discrepancy was found. No mixed-mode inequality was
substituted at L088's new witness, and none of the unresolved scalar,
other-anchor, global-consistency or RS claims is inferred. The direct
full-row cap and both conic stops remain unchanged, as does 955–957.

## Mathlib

Full matching fixed-column finite witness: not checked. Supporting
rational elimination, LP alternatives, singular Schur complements and
mixed-layer decomposition: not checked here. Unknown availability is
not absence. General methods are imported by the precise citations
above; this finite specialization carries no source-level novelty claim.
