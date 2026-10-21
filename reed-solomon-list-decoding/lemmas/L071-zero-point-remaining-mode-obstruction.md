# L071 — The fixed zero point fails the remaining simultaneous modes

## Hypotheses

Retain L061's entire anchored five/six-shell PSD base and the complete
L062 moment dictionary on the 68-subsets of a 1024-point set. Use the
original positive normalization

    rho=(binomial(1024,64)/binomial(68,64)+1)/(2 binomial(1024,68)),
    p5=1/68881143660, p6=133/9357995374380,
    p7=3539/248922676958508.

Use L065's original RREF and its family f=c+u*a^27+v*a^33+w*a^42.
Fix exactly L069/L070's point u=v=0,w=w_star, with
w_star=M03/(-M33) from L068's objective matrix M. Every five/seven
and six/seven column is prescribed by this same point. Retain every
old lookup, Boolean/forbidden entry, unordered presentation, singular
range condition and the full anchor correction. This point differs
from L067's old immutable column.

Index the 36 remaining seven/seven entries lexicographically by
(r,q) in {0,...,7}^2 with r+q>=7, with the original positive scaling

    Y_(7,7,7-r,7-q)=p7*z_(r,q)/v_(r,q),
    v_(r,q)=binomial(7,r)binomial(61,r)binomial(7,q)binomial(949,q).

Impose L070's 24 tight-mode equalities and all remaining 40 original
L067 mode inequalities at this fixed point. Initially require z>=0.
No new/new scalar upper row, parameter variation or other matrix is
included.

## Conclusion

This system is infeasible. In fact it remains infeasible with signed z:
a product combination with 24 strictly positive mode weights and all
other weights zero cancels every free coefficient and has fixed sum in

    [-1927568495789246,-1927568495789245),

strictly below the required lower bound zero. Sixteen of these weights
use L070's tight modes and eight use remaining modes. All 64 weights
are nonnegative, and no sign-row weight is needed. Thus the full
simultaneous included-anchor five/six/seven-shell PSD extension at this
point is impossible.

L070's equality consistency remains valid. This rejects only the fixed
u=v=0,w=w_star point, not the whole zero plane or L065 family. It does
not provide a uniform support/list bound, RS safety, or a change to the
955–957 bracket. This is a local REPRODUCTION of assessed matrix and
linear-certificate tools, without a novelty claim. The separate critical
proof review below retains this fixed-point obstruction.

## Proof

**Imported tools and applicability.** Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-15-zero-point-remaining-mode-feasibility.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
[DOI 10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
and Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://doi.org/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2, Theorem 2.6 and Lemma 2.7. Factors 68,956
and layers 0,5,6,7 stay in the assessed ranges. Singular old blocks
are allowed; their whole cross-vector range conditions and the entire
anchor congruence are retained. L067's audited coherent positive
mixed-layer normalization and full-space exhaustion are imported.

Ordinary constraint-preserving averaging and union moments use Sven C.
Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Section 1.1
(1)–(3), Proposition 1.1 and its indicator proof, p. 2, and Section 1.2,
p. 3, with foundations/12's constant-weight qualification. The ordinary
slice is invariant under S_68 x S_956, which preserves the atom-key
lookups and prescribed columns. No actual subgroup-label constraint
is averaged, and no representing measure is assumed.

For finite rational LP certificate machinery import Michel X. Goemans,
*Advanced Algorithms*, Lecture 3, 19 September 2001, Theorems 1 and 3,
printed pp. 1–2 (PDF pp. 2–3),
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
and MIT 6.854, 2020 collection,
[Linear Programming notes](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
sections “Introduction”, “Linear Equalities” and “Basic Feasible Solutions”.
Foundations/10 records the precise inspected statements, proofs and
version qualifications. Only the finite linear alternative and exact
rational certificate checking are used, with no Slater hypothesis or
general SDP strict-separation claim. No general theorem is reproved.
The sources do not decide the prescribed coefficients; their evaluation
is the local specialization.

**Original system reconstructed.** Write E=(D\X) union Y and
G=(D\U) union V, with |X|=|Y|=l, |U|=|V|=m,
i=|X intersection U| and j=|Y intersection V|. The eight atoms with
bits D,E,G of weights 4,2,1 are

    (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

Use (l,m)=(5,5),(5,6),(6,6),(5,7),(6,7),(7,7), and 0<=i,j<=l.
These give all 270 types and 1620 presentations. L070 supplies the
fixed dictionary at w_star, with exactly 36 free unordered keys.
The 28 forced seven/seven entries are

    Y77(7,7)=p7;
    Y77(7-r,7-q)=0 for 1<=r+q<=4;
    Y77(7-r,7-q)=Y_(r+q,7,q,r) for r+q=5,6.

All are retained. The verifier recovers the point from L065's original
RREF and L068's matrix, reconstructs every old and column lookup,
checks all 49 original whole-base weighted kernel equations, and
realizes each type by actual subsets to count all six presentations.
No new identification between free keys is imposed.

Use L067's beta sums and Johnson eigenvalues E_(n,a)(r), with
S_l=binomial(68,l)binomial(956,l) and
D7=binomial(68-2a,7-a)binomial(956-2b,7-b)>0.
For each a,b in {0,...,7}, let B_ab be the present old layer block
and t_ab its cross vector to layer seven after the full anchor has
been eliminated. Its entries are exactly

    C_lm=sum_(i,j) beta(68,l,m,a,i)beta(956,l,m,b,j)Y_(l,m,i,j)
          -1_(a=b=0)*p_l*p_m*S_l*S_m.

Set R_ab=t_ab^T B_ab^dagger t_ab/(p7*D7), or zero in a new-only mode.
All 64 old PSD and range conditions are checked, including zero blocks.
Exact positive-pivot elimination and an independent determinant-based
inverse-on-range calculation agree with every L070 cost. In particular
neither calculation applies an ordinary inverse to a singular block.

Define

    F_ab=sum_(r+q<=6) [Y77(7-r,7-q)/p7] E_(68,a)(r)E_(956,b)(q),
    A_ab=1_(a=b=0)*p7*S7,
    K_(ab,rq)=-E_(68,a)(r)E_(956,b)(q)/v_(r,q),
    b_ab=F_ab-A_ab-R_ab.

The original 64 Schur conditions are Kz<=b. The 24 rows selected in
L070, a<=5,b<=3, are equalities here; the other 40 are inequalities.
Both the original beta formula and the Johnson formula reconstruct
every coefficient with the stated positive v scaling. The constant
anchor term is p7*S7, since D7=S7 at a=b=0. No immutable L067 right
side is reused at the changed point.

**Explicit product separator.** Put

    h=(1,12261/455,15555/56,4099261/3640,0,0,0,0),
    k=(1,4531475/6657,136607358056/632415,27321109096/665,
       1028453048809043/210805,9295091464315239/30115,0,0),
    lambda_ab=h_a*k_b.

These are strictly positive exactly for a<=3,b<=5. Their complete
Johnson transforms, indexed by r or q from zero to seven, are

    sum_a h_a E_(68,a)(r)
      =(50116/35,12228304/35,110054736/7,1442939872/7,
        5230657036/7,0,0,0),

    sum_b k_b E_(956,b)(q)
      =(313573206376,595161945701648,141053381131290576,
        0,0,0,0,0).

For r+q>=7, either r>=5 or q>=3. Hence each product transform vanishes,
and lambda^T K=0 in every one of the original 36 columns. Independent
direct substitution into all original coefficients also checks these
cancellations. All lambda are nonnegative, so any completion satisfying
the hypothesized equalities and inequalities would give

    0=lambda^T Kz<=lambda^T b.

Evaluating b by the finite recipes above at the fixed rational w_star
gives the exact integer-comparison certificate

    -1927568495789246 <= lambda^T b < -1927568495789245 < 0.

The complete rational lambda^T b is saved at `/certificate/rhs_pairing`
in the constructor certificate and `/rhs_pairing` in the independent
verification certificate below. The full fractions, not rounded values,
are used in both integer comparisons. This contradicts the preceding
inequality. No sign assumption on z is needed because every coefficient
has canceled. This proves the claimed fixed-point infeasibility.

As a separate normalization check, the verifier forms the source C77
directly in raw Y coordinates. For each of the 36 free raw entries it
checks that the weighted coefficient sum

    sum_(a,b) lambda_ab beta(68,7,7,a,7-r)beta(956,7,7,b,7-q)/(p7*D7)

is zero. It independently reconstructs each fixed Schur term from all
forced entries, subtracting p7^2*S7^2 in the constant source block
before dividing by p7*D7 and subtracting R_ab. The resulting weighted
fixed sum equals lambda^T b exactly and has the same strict negative
interval. This checks the row sign, positive scaling, 28 forced entries
and full anchor subtraction in the unreduced system.

**Discovery, exact evidence and limits.** L070's RREF supplies z=c+Tx
with 13 coordinates, precisely its original nonpivot z entries. The
constructor checks this map in every selected original row, substitutes
it in the 40 remaining rows and all 36 sign conditions, and saves every
unscaled reduced row. Positive row and variable scalings are recorded.
A 180-digit Decimal phase-I simplex proposes a basis. Its negative
phase-I value is small and is not proof of infeasibility. Exact rational
basis reconstruction gives a separator, which is translated back using
L070's complete left row transformation and checked against every
original coefficient. A positive normalization yields the displayed
product weights. All sign-row weights are exactly zero and all original
mode weights are nonnegative, so the final certificate does not depend
on the numerical basis or on the choice of equality-space coordinates.

From the notebook run

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/zero_point_remaining_modes.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_zero_point_remaining_modes.py

The constructor passes 2591 exact checks with no failures. Its complete
certificate is `scripts/finite-support/zero-point-remaining-modes-results.json`.
The independent verifier imports no notebook code or optimizer and uses
no floating arithmetic. It passes 1643 checks with no failures; its full
certificate is `scripts/finite-support/zero-point-remaining-modes-verification.json`.
Both pin their input hashes. The verifier reconstructs the original
dictionary, all 64 singular-mode data and beta coefficients, checks the
displayed rational factors, all 36 scaled and raw cancellations, and the
strict fixed pairing. It also checks every saved L070 row transformation
and the full reduced system used in discovery. Full summaries, empty
failures, complete cancellations and the load-bearing pairing were
inspected; the programs consume the full evidence, not a preview.

The ancestral PSD decomposition and kernel exhaustion are imported
established inputs, not rederived in their entirety. The separate critical
review below retains this local result. This is a new verdict
for prescribed coefficients using known tools, not progress beyond the
sources in the form of a general theorem. Preserve L067's distinct old
column obstruction and all earlier scalar/equality passes. Other u,v on
the zero plane, other columns/base/pairs, other matrices, global moments,
labels, measures and RS realization remain unresolved. No main-target
resolution or complete candidate is asserted.

**Separate critical proof review — step 246, 2026-10-16.** Reuse the prior
SPECIALIZE assessment
`drafts/literature/2026-10-16-zero-point-remaining-mode-critical-audit.md`.
The audit retains the exact hypotheses and conclusion, without a
coefficient or mathematical repair. Rerunning the independent verifier
passes all 1643 checks. The additional standard-library-only program
`scripts/finite-support/critical_audit_zero_point_remaining_modes.py`
passes 6004 exact checks with no failures; its complete certificate is
`scripts/finite-support/zero-point-remaining-modes-critical-audit.json`.
This is a REPRODUCTION audit of a prescribed finite obstruction, not a
new general theorem or progress beyond the cited sources.

The audit recomputes the positive original rho and pairs, recovers all
49 column coordinates from L065's original RREF and L068's objective
matrix, and checks the full negative-square identity at this point.
It retains u=v=0,w=w_star and verifies that this differs from L067's
immutable column. Every original compatibility row is substituted.
Each of the 86 orbit weights is recomputed from the actual four-region
binomial counts, including anchor weight one, and all 49 weighted kernel
residuals vanish. The complete old dictionary and column entries agree.
The ancestral kernel-exhaustion and source-decomposition theorems remain
imported established inputs, not newly proved by these finite checks.

The rerun verifier counts actual subsets point by point. The additional
audit separately permutes all eight atom counts for all 270 types,
retaining all 1620 presentations, and compares every complete record.
Source equalities indexed by the sorted distances and i-j agree with
the full atom keys. All 28 forced seven/seven entries are retained;
the remaining 36 keys are distinct and acquire no extra identification.
Atom bijections exhaust the ordinary stabilizer orbits, so averaging
preserves this particular dictionary, also with signed free entries.
It makes no assertion about actual subgroup-label constraints.

For each factor n=68,956 and each ordered pair l,m in {5,6,7}, the audit
reconstructs all 118 relation matrices by actual subset counts:

    Q_lm^t(i,j)=sum_x binomial(i,x)binomial(7-i,j-x)
      binomial(l-i,t-x)binomial(n-7-l+i,m-j-t+x).

The four factors count the new m-subset in the four regions determined
by the fixed seven-subset and the current l-subset; impossible counts
are zero. Full row sums and every entry agree with L067's audited data.
Importing L067's monic orthogonal bases, the audit recomputes their
positive norms and orthogonality and verifies every coordinate of
Q_lm^t h_m,a=gamma_lm,a(t)h_l,a, including the zero actions for a>l.
Thus it uses full actions, not isolated matrix entries or previews.

At the changed point, tensor these actions and let N_l be the product
of the two basis norms. Subtract p_l*p_m*S_m from the constant-mode
action before forming its weighted matrix. With L067's established
positive scales s_l and s_7=1, every old entry and both cross directions
again satisfy

    K_lm=(N_7/D7)*s_l*C_lm*s_m.

This checks the coherent normalization on the whole matrix at this
point; no isolated pseudoinverse is transported. Eliminate layer 6
before layer 5 on the weighted form. All positive pivots and every
zero-pivot residual row and cross entry are checked. The 36 two-old-layer
modes have ranks 2,1,0 in respectively 9,8,19 cases; the 13 one-old-layer
modes have ranks 1,0 in 10,3 cases; 15 modes are new-only. In all 64 cases
the inverse-action cost divided by p7*N_7 equals the source R_ab.
The positive multiplicity sums recover S5,S6,S7, in agreement with the
imported full-space decomposition. This independently retains every
singular range and the full anchor correction.

The audit reads h,k and both complete displayed transforms directly
from this manuscript. Every fraction agrees with the certificate and
independent Johnson evaluation. Precisely 24 weights are positive:
16 selected tight modes and eight remaining modes; all sign weights
are zero. Every entry of the 64-by-36 original matrix agrees with both
saved reconstructions, and every beta/Johnson normalization is checked.
The source C77 fixed part is reconstructed from all 28 forced entries,
subtracting p7^2*S7^2 in the constant mode before division by p7*D7.
Together with the independently computed inverse cost, this gives each
original right side, not L067's distinct immutable right side.

All 36 scaled and all 36 raw-Y coefficient sums are exactly zero.
The complete rational fixed pairing agrees with both earlier certificates.
For its numerator N and positive denominator D, direct integer comparison
gives

    -1927568495789246*D <= N < -1927568495789245*D < 0.

The certificate stores N/D and both exact bound slacks. Consequently
the cited free-variable linear alternative applies without nonnegativity
of z, strict feasibility, numerical phase-I status or a general SDP
separation theorem. The equality-only L070 pass remains unaffected.

The initial additional audit reported one comparison failure: its
lexicographic record order differed from the saved old-types-first
order at position 72. All 270 full records already agreed when keyed
by type; no mathematical value differed. The comparison now uses the
specified order. The failed evidence is preserved at
`scripts/finite-support/zero-point-remaining-modes-critical-audit-initial.json`.
This is an audit-harness correction, not a repair of L071.

Reproduce with
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_zero_point_remaining_modes.py`.
Full summaries, failures and cancellation vectors were inspected; the
complete load-bearing rational pairing was read, and all remaining
arrays were consumed by exact checks. Only this fixed point is rejected.
Other zero-plane points, different moments, scalar upper rows, other
matrices, global consistency and RS realization remain unresolved.
The 955–957 bracket and Mathlib qualifications below are unchanged.

## Mathlib

Full matching theorem for this fixed finite system and its product
separator: not checked. Full matching mixed-layer decomposition,
singular-Schur criterion, Farkas alternative and rational LP certificate
coverage: not checked in Mathlib. The cited primary sources and exact
finite certificates supply the inputs used here. Unknown availability
is not evidence of absence.
