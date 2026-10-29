# L277 — Complete other/other quantitative remainder

## Hypotheses

Use precisely L124's complete other/other group

    C=S3_top, Y=S3-C, O_i(a)=(1/2) kappa(f_(i,0),r0,Y,Y),

and its original nine-term coefficient K_(i,oo) in (1). The setting
is SU(2), the all-face relative fixed-link cube (-4,4)^4, the straight
lower-rooted direction-1 forest, sufficiently large admitted even N,
a=8/N, tau=1/16, ordinary stored coordinates and the bare
small-coupling coefficient taken at each fixed mesh before refinement.
Both actual probes i=3,6, the fixed displacement and the actual L018
residual are unchanged, including both of its insertion representations.

Retain every interior axial level, relative source and normal/end row,
the upper pin, ordered plaquette pairs including coincidences, both
connected pairing classes, both generator/residual orientations,
constant component indices and the complete exterior heat sums.
Import L124 proof section 1's exact finite partition and the complete
conclusions L086(1), L087(2), L093(2)--(4), L224's conclusion following
(1), L229(5), L234(2), L236(2), L241(3), L248(2), L253(2) and L276(1).
All their analytic and upstream audit qualifications remain in force.
This lemma does not recursively verify those inputs.

The coefficient is exactly

    K_(i,oo)=K_(i,E)+K_(i,ax)-K_(i,Q)+K_(i,G)+K_(i,R)
                      +K_(i,f)+K_(i,V)+K_(i,sc)+K_(i,en).       (1)

These are the original coefficients named in L124: respectively the
functionals in L101, L098, L097, L104, L107, L123, L120, L121 and
L122, with their signs, phases, physical normalization and heat
measures. In particular K_(i,V) is not K_(i,Vmix), and K_(i,R)
already includes its triangular half-weight. No coefficient identity,
value, sign or cancellation is assumed.

## Conclusion

There are finite mesh-independent constants C_i and one common
threshold N_0 such that, for both actual probes and all admitted even
N>=N_0,

    |O_i(a)-3a^(-3)K_(i,oo)|
        <= C_i N^(5/2)log(eN)
        <= C_i N^(5/2)log(eN)^2.                              (2)

Consequently

    |a^3 O_i(a)-3K_(i,oo)|
        <=512 C_i N^(-1/2)log(eN) ->0.                         (3)

This is local RESEARCH / REPRODUCTION under the pre-invocation
SPECIALIZE assessment
`drafts/literature/2026-10-24-complete-other-other-quantitative-assembly.md`.
It assembles qualified existing component bounds; it claims no
mathematical discovery beyond the sources checked. The separate critical
audit in proof section 4 accepts this finite assembly conditional on
the imported complete estimates. The complete
quantitative L011 assembly, upstream analytic audits, coefficient
evaluation/cancellation, interacting reflected-error bound, continuum
construction and axioms, infrared control and finite positive mass
remain unresolved. This is not a Yang--Mills solution candidate.

## Proof

### 1. Subtract the original nine coefficients at fixed mesh

L124 proof section 1 gives exact finite identities

    O_i=3(T_Z+T_UV),
    T_UV=T_gg+T_hh+R_H+R_E+R_gx+R_hx,
    R_H=R_H,ax+R_H,tr-R_H,Q,
    R_hx=R_L+R_R-R_Q.                                        (4)

Here R_H,Q is the H diagonal curvature subtraction whose coefficient
is K_(i,Q). The different R_Q is L093(3)'s off-diagonal crossed
curvature insertion and has no retained cubic coefficient. Neither
symbol is a newly modified sector. Both crossed residual orientations
are already included in R_gx and R_hx. L276 concerns precisely the
complete R_H,tr in (4), without an outside factor 3.

For brevity in this proof put

    K_(i,Htr)=K_(i,f)+K_(i,V)+K_(i,sc)+K_(i,en).

This is only the four-coefficient sum in L276(1), not another
coefficient to add to (1). Substitute (4) and subtract (1) to obtain
the exact equality

    O_i-3a^(-3)K_(i,oo)
      =3{T_Z+T_gg+T_hh
          +[R_E-a^(-3)K_(i,E)]
          +[R_H,ax-a^(-3)K_(i,ax)]
          -[R_H,Q-a^(-3)K_(i,Q)]
          +[R_H,tr-a^(-3)K_(i,Htr)]
          +[R_gx-a^(-3)K_(i,G)]
          +R_L+[R_R-a^(-3)K_(i,R)]-R_Q}.                     (5)

In particular expansion of the negative bracket gives
-R_H,Q+a^(-3)K_(i,Q), as required by subtracting the negative
coefficient in (1). All nine coefficient subtractions occur once.
This algebra precedes absolute values; no sign of a coefficient or
cancellation among different coefficients is used.

### 2. Use the eleven complete sector bounds once

Write ell_N=log(eN). The rows below are the eleven scalar summands
inside braces in (5); constants can differ between rows.

| Complete quantity in (5) | Input | Absolute bound |
| --- | --- | --- |
| T_Z | L086(1) | c_(Z,i) N^(3/2) |
| T_gg | L087(2) | c_(gg,i) N^2 |
| T_hh | L229(5) | c_(hh,i) N^(5/2) sqrt(ell_N) |
| R_E-a^(-3)K_(i,E) | L224 conclusion following (1) | c_(E,i) N^(5/2) |
| R_H,ax-a^(-3)K_(i,ax) | L236(2) | c_(ax,i) N^(5/2) |
| R_H,Q-a^(-3)K_(i,Q) | L234(2) | c_(Q,i) N^(5/2) |
| R_H,tr-a^(-3)K_(i,Htr) | L276(1) | c_(Htr,i) N^(5/2) ell_N |
| R_gx-a^(-3)K_(i,G) | L253(2) | c_(G,i) N^(5/2) |
| R_L | L241(3) | c_(L,i) N^(5/2) sqrt(ell_N) |
| R_R-a^(-3)K_(i,R) | L248(2) | c_(R,i) N^(5/2) ell_N |
| R_Q | L093(4) | c_(crossQ,i) N^(5/2) |

The finite quantities and coefficients match as follows. L086 includes
both covariance path orders and coincident ordered plaquettes. L087
projects both rough lines in exactly T_gg. L229's conclusion is on
the original complete T_hh, after its two-mass comparison; its internal
comparison terms are not extra summands. L224's quoted conclusion
already combines its static E rate with L223's replacement. Likewise
L234(2) already includes L233's static replacement, and L236(2)
includes L235's reduction with both original generator orientations.
Their faster static rates cannot replace these complete allowances.

L241(3) bounds the complete original R_L, not only its bulk trace;
its proof section 5 supersedes the stale pending-audit statements
in its opening. L248(2) uses exactly L107(2)'s K_(i,R), the coefficient
in (1). Its factor 1/2 is not an additional cumulant multiplicity.
L253(2) estimates the entire R_gx against L104(6)'s K_(i,G), including
its G_L and G_Q comparisons. Finally L276(1) contains all eight
allowances of its transverse-H telescope, against the four original
coefficients in (1). No internal allowance from any of these complete
conclusions is added again. The remaining R_Q is precisely the
quantity defined and bounded in L093(3)--(4).

Every table conclusion concerns the same fixed box, displacement,
flow time, forest, stored normalization and original mesh sequence.
Its complete heat sum is already included. The auxiliary masses and
extensions in the component proofs are internal comparison choices;
they do not redefine the original sectors in (4) or impose mutually
inconsistent conditions on them. No mass is chosen or limit through
the heat spectrum is exchanged in the present assembly. Both
representations of the actual residual retain the imported equality
and qualifications; there is no new residual or separate orientation
sum in (5).

For each of the eleven rows and each of i=3,6 choose the asserted
sufficiently large admitted-mesh threshold. Include the thresholds
for the finite identities and, if the residual is represented in
either insertion form, those for both forms. There are finitely many
such choices. Let N_0 be their maximum and 8, and enlarge each
nonnegative row constant over these two representations if needed.
This yields a common admitted even-mesh range, not an explicit
numerical N_0 or a new uniform estimate over varying physical data.

For N>=N_0 we have ell_N>=1, sqrt(ell_N)<=ell_N, and
N^(3/2)<=N^2<=N^(5/2). Each table row is therefore at most its
constant times N^(5/2)ell_N. Taking absolute values in (5) and
applying the triangle inequality proves (2) with C_i equal to three
times the sum of the eleven nonnegative row constants. This is the
only outside factor 3. The squared-log bound follows from
ell_N<=ell_N^2. Since a^3=512/N^3, (3) follows exactly; the elementary
limit N^(-1/2)log(eN)->0 proves its stated convergence.

### 3. Relevance and stopped shortcuts

The achieved bound meets the assessed N^(5/2)log(eN)^2 threshold
and strengthens L124's qualitative o(a^(-3)) remainder under the
imported quantitative premises. Its downstream use is the complete
other/other block of a later quantitative L011 assembly. The other
blocks and analytic/audit qualifications remain independent gaps.
Neither an O(N^2) remainder nor coefficient cancellation follows.

ATTEMPTS/030's fixed-mass nonuniform shortcut is not used: every
row is already a complete quantitative statement on the original
sector. ATTEMPTS/032's separate first absolute kernel moments are
not assumed. No L220 scalar cancellation, signed-growth inference,
numerical bound or interacting limit is used. The only new operation
is finite signed assembly followed by a triangle inequality.

### 4. Separate critical audit — 2026-10-25

**Verdict and scope.** Accept (2)--(3) conditional on the complete
estimates and exact partition in the hypotheses, under the unchanged
SPECIALIZE assessment
`drafts/literature/2026-10-25-complete-other-other-assembly-critical-audit.md`.
This audit read L124's full partition and telescope, all eleven complete
input statements, and the relevant component assembly/audit passages.
No coefficient, multiplicity, domain, threshold or rate mismatch was
found within this finite assembly. This is RESEARCH / REPRODUCTION:
validation of an existing conditional bound, not a stronger estimate,
discovery beyond the checked sources or recursive analytic audit.

**Independent signed expansion.** Substituting the two last splits of
L124(5) into its first partition gives, before any estimates,

    O_i/3=T_Z+T_gg+T_hh+R_E+R_H,ax-R_H,Q+R_H,tr
                                  +R_gx+R_L+R_R-R_Q.

The coefficient to subtract from this expression is exactly

    a^(-3)[K_(i,E)+K_(i,ax)-K_(i,Q)+K_(i,G)+K_(i,R)
                              +K_(i,f)+K_(i,V)+K_(i,sc)+K_(i,en)].

Thus the H-curvature contribution to the remainder is
-R_H,Q+a^(-3)K_(i,Q), whereas the different crossed curvature
contribution is simply -R_Q. The transverse-H bracket subtracts four
coefficients and the other five brackets subtract five; this accounts
for all nine coefficients once and reproduces (5) exactly. The five
unretained sectors are T_Z, T_gg, T_hh, R_L and R_Q. Together with the
six coefficient-subtracted brackets they make eleven scalar summands.
No numerical value or relation among coefficients enters this check.

L086 defines T_Z with both covariance path orders and T_UV with all
distinct-row replacements on the full ordered pair set. L087 projects
both rough lines for exactly T_gg. L093(2)--(3) defines the complete
R_hx split, already including the two residual orientations; its R_Q
bound in (4) is therefore the correct unretained crossed subtraction.
L124's R_gx likewise already contains both orientations. Multiplying
either of these pairs by another 2 would change the original partition.
L248(2) explicitly uses L107(2)'s K_(i,R), including its triangular
half-weight; it is not an additional weight on the whole group.
L276(1) uses exactly the four coefficients in L124(10), in particular
K_(i,V), not K_(i,Vmix), and has no outside factor 3. Hence only the
original identity O_i=3(T_Z+T_UV) supplies that factor in (2).

**Complete allowances.** The table in section 2 quotes the full
quantities, not their faster internal comparisons. L229 proof section
4 adds the bulk, boundary and mass/projection errors to obtain (5)
for the original T_hh. L224's conclusion after (1) expressly includes
the dynamic-to-static replacement in R_E. L234(2) likewise includes
that replacement for R_H,Q. L236(2) retains both the static error and
N^2 log(eN) replacement; the latter is bounded by a constant times
N^(5/2), as log(eN)/sqrt(N) is bounded for N>=1.

L241(3), not its bulk-only (2), supplies the complete R_L allowance
with sqrt(log(eN)); its section 5 explicitly supersedes its stale
opening audit language. This does not discharge the recorded upstream
premises. L248 proof section 4 uses its complete original reverse-trace
comparison once, including the finite axial tail, then adds quadrature
and mass removal to obtain (2). L253 proof section 5 and audit section
6 use the complete original-pair comparison, already including the
removed G_L and G_Q terms, to obtain (2) for R_gx. Finally L276(1)
already combines the eight complete transverse-H allowances; its
section 4 separately checks the signed telescope and overlapping
projection estimates. None of these internal allowances is a twelfth
scalar summand of (5), nor may its slower part be dropped. The present
audit uses their stated complete conclusions with all qualifications.

**Common domain and quantitative threshold.** Every complete statement
uses the same relative SU(2) cube, straight lower-rooted forest, stored
coordinates, bare-first order, a=8/N, tau=1/16 and actual probes 3,6.
The complete quantities retain original levels, source/end rows,
ordered coincidences, upper pin, constant indices and heat sums.
The insertion forms represent the same actual residual; no estimate
for arbitrary replacement residuals or extra orientation sum is needed.
The different auxiliary mass schedules in L229, L241, L248 and L253
are internal choices in different comparisons. Their conclusions are
bounds on the original sectors, not simultaneous choices of a shared
mass parameter. Thus they impose no incompatible restriction on N.

For each row and each probe take its asserted finite threshold on
the same admitted even sequence. Their finite maximum, together with
the finite-identity thresholds and 8, is a legitimate N_0. If the
same residual is estimated in its two representations separately,
take the maximum of those thresholds and constants too. This asserts
neither an effective numerical N_0 nor uniformity over changing
physical data. All heat sums have already been performed in the input
statements, so this maximum is not over infinitely many heat labels.

On this range, with ell_N=log(eN)>=1, the eleven ratios of the table's
rates to N^(5/2)ell_N, in table order, are

    N^-1/ell_N, N^(-1/2)/ell_N, ell_N^(-1/2),
    ell_N^-1, ell_N^-1, ell_N^-1, 1, ell_N^-1,
    ell_N^(-1/2), 1, ell_N^-1.

Each is at most 1. Applying the triangle inequality to the independently
checked signed identity gives (2) with exactly three times the sum of
the eleven nonnegative constants. Since ell_N<=ell_N^2, this meets
the requested budget. Multiplication by a^3=512/N^3 gives (3), and
N^(-1/2)log(eN) tends to zero. There is no numerical certificate or
additional limiting interchange in this finite check.

ATTEMPTS/030's nonuniform fixed-mass closure and ATTEMPTS/032's separate
first absolute moments remain stopped; neither is used here. This
acceptance supplies one conditional block for quantitative L011
assembly, not that assembly itself. It supplies no O(N^2) remainder,
coefficient cancellation, upstream analytic verification, interacting
bound, continuum axioms or positive infinite-volume mass.

## Mathlib

Full matching complete other/other quantitative theorem: **not
checked**. Supporting finite algebra, triangle inequalities, finite
maxima and real-power/logarithm comparisons: **not checked**. Unknown
availability is not evidence of absence. The specialized estimates
are imported by the canonical equation/section citations above.
No fresh external theorem or reproof of a scalar Green, Fourier,
heat, Taylor or Wick estimate is required here. This is an informal
conditional assembly proof; section 4 audits the finite assembly only.
