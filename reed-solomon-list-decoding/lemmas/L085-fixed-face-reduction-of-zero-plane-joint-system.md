# L085 — A fixed partial face for the full zero-plane joint system

## Hypotheses

Keep precisely L083's prescribed family: n=1024,w=68, L021's pair
moments, L053's positive singleton rho, and
p8=16792471/1181138102168120460>0. Matrices are divided by rho.
The old included-anchor PSD base is L073's, with L075's entire immutable
dictionary and original seven-column RREF/completion. Retain L076's
original affine column family with parameter order (t56,t63,t69,t78),
all 85 factor inequalities and all 90 weighted whole-kernel equations.
Preserve all 500 full-key types/3000 presentations, Boolean/forbidden
cases, 36 forced eight/eight entries and the other 45 free entries.
Ancestor PSD, uniqueness, coherent normalization and whole-kernel
exhaustion contracts retain their existing qualifications.

Let s be L083's exact stationary t78 value and substitute only t78=s.
The remaining parameters u=(t56,t63,t69) are real and subject to the
same 85 original affine inequalities. The 45 real variables z_(r,q),
0<=r,q<=8, r+q>=8, are lexicographically ordered, with

    V_rq=C(8,r)C(60,r)C(8,q)C(948,q)>0,
    Y_88(8-r,8-q)=p8*z_(r,q)/V_rq.

Here C(n,k)=binomial(n,k), zero outside 0<=k<=n. Require all z>=0
in the full system; the face implication itself also allows signed z.
Keep L078/L083's complete 81 included-anchor modes, both rectangular
directions, full anchor subtraction, and all singular/empty old ranges.
Use exactly L082's unchanged canonical weights y, reconstructed from
its specified 46-by-46 rational system. Its positive support I consists
of i=9a+b with 0<=a<=6, 0<=b<=3 (28 modes).

L084's selected equality and all-solution formulas are retained for
comparison, without discharging their pending separate critical review.
No scalar upper rows, other anchors, changed pair/base/column data,
global moment extension or RS realization are assumed.

## Conclusion

There is an explicitly specified fixed rational PSD product multiplier
of rank 28 for the complete zero-plane affine-LMI system. Its trace
with the entire affine pencil is identically zero: all 49 coefficients
(constant, three parameters, 45 moments) vanish, as do all 45 original
raw-moment coefficients. It acts nontrivially after removal of the
fixed old-base kernels.

An exact partial-face restriction reduces the sum of the retained mode
block sizes from 140 to 112. The equivalent formulation keeps all 85
domain inequalities, all 45 moment signs, all original equalities and
the 53 untouched mode blocks. For the 28 selected blocks it keeps the
compressed PSD conditions AND every mixed and removed-coordinate zero
equation. These zero equations reduce to the same 28 selected scalar
equalities already isolated in L084; no additional exclusion is obtained.

This is a known-method REPRODUCTION establishing a local certificate
and exact reformulation, not progress beyond the checked general sources.
It supplies no feasibility/infeasibility verdict, minimal face, Slater
point, rational feasible-point guarantee, global bound or RS boundary
improvement. The full zero-plane system remains undecided, arbitrary-center
67/68-agreement safety remains open and the bracket remains 955–957.
The separate critical proof review below retains L085 under these same
ancestral contracts; it does not discharge L084's independent review.

## Proof

**Imported face theorem.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-zero-plane-fixed-face-reduction.md`.
Import Frank Permenter and Pablo Parrilo, *Partial facial reduction:
simplified, equivalent SDPs via approximations of the PSD cone*,
[arXiv:1408.4685v3](https://arxiv.org/pdf/1408.4685v3), submitted
17 May 2017, manuscript dated 19 May 2017: Lemma 1, Section 2.2,
equations (1)–(4), pp.4–5; Lemma 3 and proof, Section 2.4, pp.7–8;
Remark 1, p.7; and the complete constraint reformulation in Section 4.1,
p.18. A checked PSD multiplier orthogonal to an affine pencil permits
restriction to its kernel face; the compressed PSD condition must be
accompanied by mixed and removed-coordinate zero equations. Apply this
blockwise to the finite real product cone. Neither Lemma 2's existence
direction (which assumes nonemptiness), terminal strict feasibility nor
minimal-face conclusions are invoked. No general face theorem is reproved.

The mode and singular-Schur contracts remain those of L078/L083:
Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7; and Takashi Sano, *Moore-Penrose inverse, generalized
Schur complement and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2, Theorem 2.6 and Lemma 2.7. Foundations/04,09,10,12
keep their source qualifications. The finite rational transport below
is needed because these general results do not supply this multiplier.

**Original affine blocks and existing kernel removal.** For i=9a+b,
0<=a,b<=8, put

    n_i=p8*C(68-2a,8-a)C(956-2b,8-b)>0.

Let B_i and c_i(u) be L083's original source base and cross divided
by n_i, after its fixed full-anchor Schur congruence. Let F_i(u) be
the forced affine term minus the complete anchor correction. Let A_i
be the original beta coefficient row in L084's displayed definition.
The normalized original mode block is

    P_i(u,z) = [ B_i         c_i(u)        ]
               [ c_i(u)^T   F_i(u)-A_i*z ].

The complete original data and these blocks were saved in step 298's
`scripts/finite-support/zero-plane-joint-feasibility-results.json`.
No quadratic equality parametrization is substituted into this pencil.
Its variables remain the three u coordinates and all 45 z coordinates.

For each B_i, use step 298's unit lower triangular rational congruence
T_i, computed by increasing-column symmetric elimination, skipping
zero pivots. The exact identities checked here are

    T_i B_i T_i^T = diagonal(d_i, zeros),
    (T_i c_i(u)) at every zero pivot = 0 identically on the plane.

The notation places positive and zero coordinates in their saved order;
let J_i insert the positive coordinates followed by the new last index.
Write E_i=diag(T_i,1). Then

    M_i=J_i^T E_i P_i E_i^T J_i
       = [ D_i           h_i(u)       ]
         [ h_i(u)^T     F_i(u)-A_i*z ],

where D_i is diagonal with strictly positive diagonal d_i, of size r_i.
For r_i=0, M_i is just the last scalar. Full zero rows and cross rows
vanish before deletion, so

    P_i=E_i^(-1) J_i M_i J_i^T E_i^(-T).

This identity is checked in all 49 affine coefficients for all 81 modes.
The exact unit triangular inverse is also checked. Thus this prior
removal is an equivalence, including singular and empty ranges.

**Constancy and multiplier.** For every i in I, all three linear
coefficients of h_i(u) are exactly zero. Define the fixed rational
vectors and scalar affine functions

    x_i=D_i^(-1)h_i,
    v_i=(-x_i,1),
    ell_i(u,z)=F_i(u)-A_i*z-h_i^T*x_i.

For r_i=0 use empty x_i and v_i=(1). Constancy is checked entrywise on
the complete plane, not on a selected parameter point. It is also
consistent with L083's negative-square identity: on this plane the
weighted Schur bound is identically zero. Its quadratic coefficient in
each u coordinate is minus the sum of y_i times the corresponding
squared h_i slope divided by positive d_i. Nonnegative summands force
each selected slope to vanish. No constancy of an unselected mode is
assumed.

Set S_i=y_i*v_i*v_i^T for i in I and S_i=0 otherwise. Give all domain
and moment-sign scalar blocks multiplier zero. Every selected S_i is
rational PSD of rank one because y_i>0 and the last entry of v_i is 1.
These are 28 separate retained blocks, so total rank is exactly 28.
They do not act only on directions previously removed by J_i.

For every u,z, direct multiplication gives

    v_i^T M_i v_i=ell_i(u,z),
    sum_i trace(S_i M_i)=sum_i y_i*ell_i=0.

Indeed, the moment coefficients cancel by L082's y^T*A=0; the remaining
weighted bound vanishes identically on t78=s by L083. The calculation
checks separately the constant coefficient, all three u coefficients
and all 45 z coefficients. For original raw Y coordinates the change
z_(r,q)=V_rq*Y_88(8-r,8-q)/p8 is positive and diagonal; all 45 resulting
coefficients are separately checked to vanish.

The corresponding fixed multiplier in original normalized coordinates is

    w_i=E_i^T J_i v_i,
    S_i^original=y_i*w_i*w_i^T.

Its trace with P_i is the same. This transport is checked coefficientwise
directly against B_i,c_i,F_i, retaining both cross directions and the full
anchor. For the unnormalized source block n_i*P_i, use
S_i^original/n_i. Thus no positive normalization or raw scaling is lost.
Original coherent mode multiplicities and the positive anchor elimination
remain qualified imports from L078/L083, not fresh audits of those inputs.

**Exact kernel-face formulation.** For i in I take

    U_i = [ I_(r_i) ],       H_i=[U_i v_i].
          [ x_i^T   ]

The columns of U_i span ker(S_i). They are independent from their top
identity submatrix and v_i^T U_i=0. With h=1+x_i^T*x_i>0, the inverse is

    H_i^(-1) = [ I-x_i*x_i^T/h     x_i/h ]
               [ -x_i^T/h          1/h   ].

Both inverse identities are checked exactly. For an unselected mode
use U_i=I and no complement, preserving the whole M_i.

The source's complete face formulation is, for every i in I,

    U_i^T M_i U_i >=PSD 0,
    U_i^T M_i v_i = 0,
    v_i^T M_i v_i = 0.

All three conditions are retained. Direct multiplication gives

    M_i v_i=(0,ell_i)^T,
    U_i^T M_i v_i=x_i*ell_i,
    v_i^T M_i v_i=ell_i.

Hence all the face equations are exactly ell_i=0; every component is
saved and checked, including redundant mixed equations. The scalar
equations are the original 28 L084 selected Schur equalities. Their
right sides are affine here: all six quadratic coefficients vanish,
and their constant/linear coefficients agree with L084's complete arrays.
The rank-27 and 18-free-coordinate results remain imports from L084,
with its pending review; they are not necessary to infer face equivalence.

For completeness, when ell_i=0,

    M_i=[I;x_i^T] D_i [I,x_i],
    U_i^T M_i U_i=(I+x_i*x_i^T) D_i (I+x_i*x_i^T).

For r_i>0 this is positive definite: D_i has positive diagonal and
I+x_i*x_i^T has the displayed positive-definite quadratic form
||a||^2+(x_i^T*a)^2 for a!=0. For r_i=0 the compressed PSD condition
is the empty 0-by-0 condition; the removed scalar equation still says
M_i=0. No selected PSD condition is used to discard a zero equation.

If the original system is feasible, the checked fixed PSD multiplier
and imported face theorem force these face equations and compressed
PSD conditions. Conversely, retain the 53 untouched PSD blocks and all
original domain/sign/equality rows. For a selected block the mixed and
removed equations give

    M_i=H_i^(-T) diag(U_i^T M_i U_i,0) H_i^(-1),

which is PSD. The original-block pullback above restores every P_i.
The calculation checks the full transformed coefficient matrix and
its inverse pullback for each of the 49 coefficients in every selected
mode, without assuming the equations in those checks. Thus this is an
equivalence of full affine systems even if both are infeasible.

The old retained block sizes sum to 140. Each of the 28 selected
rank-one multipliers removes exactly one coordinate, so the reduced
sizes sum to 112. This count asserts neither the minimal face nor
strict feasibility of the remaining blocks. No second conic solve is run.

**Evidence and limitations.** Reproduce from this notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/zero_plane_fixed_face.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_zero_plane_fixed_face.py

The constructor passes all 10999 exact checks with no failures. Its full
certificate is `scripts/finite-support/zero-plane-fixed-face-results.json`.
It consumes complete relevant arrays of the step-290/292/294, equality
and step-298 evidence, reconstructs canonical weights and original beta
rows, retains all domain/full-key/kernel contracts, and checks every
original, retained and face pullback coefficient. The saved rank-one
factors specify the full rational multipliers. All 49 coefficients of
each mixed/removed equation are saved. The compressed pencil is saved
by its first four matrices and its exact moment rank-one coefficient
formula, avoiding redundant large outer products.

The separate verifier invokes no constructor or optimizer. It computes
all 49 traces directly in the original source coordinates, checks the
fixed original kernel equation and canonical weights against the audited
input, and reconstructs all mixed/removed equations and compressed PSD
factorizations. It passes 491 exact checks with no failures. Full evidence:
`scripts/finite-support/zero-plane-fixed-face-verification.json`.
Actual affine/raw trace coefficients are all 0 against required 0;
removed rank is 28 against the nontriviality requirement >0.
These arithmetic checks alone do not constitute a critical proof review.
Input hashes bind data but are not used in place of the
complete relevant coefficient checks.

The stopped unreduced numerical run and reconstruction in ATTEMPTS/067
remain intact. This reduction adds no new admissibility restriction
beyond the selected equalities; its use is an exact numerical/proof
reformulation for a later attempt. It does not clear L084's review,
other ancestor qualifications, scalar upper rows, other-anchor tests,
global consistency, alternative moments or RS realization.

**Separate critical proof review — step 302, 2026-10-18.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-18-fixed-face-critical-audit.md`.
This review retains the certificate and both equivalence directions.
It reuses the inspected Permenter–Parrilo theorem/proof cases above;
the application is to fixed real symmetric pencils and verified PSD
multipliers, not an existence theorem assuming feasibility. The precise
Section 4.1 reformulation is on printed p.18. No new theorem or weights
are introduced and no optimizer is invoked.

Reproduce the independent audit from this notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_zero_plane_fixed_face.py

Its complete certificate is
`scripts/finite-support/zero-plane-fixed-face-critical-audit.json`.
All 12009 exact checks pass with zero failures. The program imports only
arithmetic helpers from the earlier L078 audit, no L085 constructor or
verifier. It consumes the complete relevant step-290/292/294, equality,
step-298 and face arrays. Hash checks bind inputs but do not replace
coefficient reconstruction. Original pairs, rho and p8 are retained;
the original seven-column RREF and defining completion equations are
reconstructed before using the immutable dictionary. Ancestor uniqueness,
whole-kernel exhaustion and coherent mode-decomposition contracts remain
qualified imports, not recursively completed critical reviews.

All 85 column factors and 90 weighted kernel equations are reconstructed
coefficientwise. Bit-permuted full atoms check all 500 types and 3000
ordered presentations, including Boolean/forbidden values, all 36 forced
and 45 distinct free eight/eight entries. Fresh original beta sums rebuild
every base, cross and forced coefficient and full anchor subtraction.
Both symmetric source directions are retained under the imported coherent
normalization. Reverse-variable exact elimination solves the canonical
46-by-46 weight system afresh, with 46 nonzero pivots; its positive support
is precisely the stated 28 modes. All 85 plane-domain rows and all 45
positive raw-to-scaled sign conversions are retained.

For each of the 81 original blocks, the audit independently inverts the
old congruence, checks every diagonal and discarded cross row, and verifies
both extraction and inverse pullback on all 49 affine coefficients. Thus
old singular and empty ranges introduce no lost equations. For every
selected block the entire plane cross is constant, the saved rank-one
factor is fixed and nonzero, and the kernel/complement basis is invertible.
All original, normalized and unnormalized multiplier traces agree. The
49 affine totals and 45 raw totals are exactly zero against required zero.
Full transformed coefficient matrices and their inverse pullbacks are
saved, retaining every mixed and removed-coordinate equation. Their scalar
coefficients match the existing selected equalities; this comparison does
not audit L084's rank-27 or all-solution claims.

The selected retained base ranks are zero in 20 modes, one in six modes
and two in two modes. In each zero-rank selected mode, the retained block
is a scalar: original PSD and zero positive-weight trace force that scalar
to be zero. The compressed matrix is empty, but the removed scalar equation
is still imposed. This endpoint is checked directly, without extending
Lemma 1's wording for nonzero proper faces. For the other selected modes,
the assessed trace/kernel theorem forces the face equations. Conversely,
the full invertible H_i congruence restores each selected PSD block from
its compressed PSD block and all zero equations; the old extraction/lift
identities then restore every original block. The 53 untouched blocks,
domain, moment signs and original equalities are carried through verbatim.
These implications also hold when the common feasible set is empty.

The rank and sizes are exactly 28 and 140 to 112. This audit establishes
the claimed equivalent partial-face formulation as a checked local input,
not an additional exclusion or progress beyond the cited general methods.
It preserves ATTEMPTS/067 and all earlier stops. Full-plane feasibility,
minimality, strict feasibility, rational existence, L084's separate review,
other anchors, global moments and arbitrary-center RS safety remain open.

## Mathlib

Full matching finite fixed-face certificate and affine-system equivalence:
not checked. Supporting PSD trace/range and matrix-congruence coverage:
not checked here. Unknown coverage is not evidence of absence. General
face methods are imported by precise citation above, without a claim
of source-level novelty.
