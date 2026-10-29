# L276 — Complete transverse-H quantitative remainder

## Hypotheses

Use exactly R_H,tr and the finite differences in L124 proof section 2,
(7)--(8). The setting is SU(2), the all-face relative fixed-link cube
(-4,4)^4, sufficiently fine admitted even N, a=8/N, tau=1/16, the
straight lower-rooted direction-1 forest, ordinary stored coordinates
and the bare small-coupling coefficient taken at each fixed mesh before
refinement. Both actual probes i=3,6, the full fixed displacement and
both residual insertion forms are unchanged.

Retain both generator orientations and mixed exterior-circulation
orientations, all original coefficient levels, finite path/component
filters, min(s,t), every covariance source and normal/end row, the
upper pin, constant component indices and complete heat sums. Import
the complete bounds L112(2), L114(3), L267(3), L268(3), L269(1),
L270(1), L271(1) and L275(4), and L118(3)'s exact identity, with all
their analytic and upstream audit qualifications. This assembly does
not independently audit those estimates.

The four coefficients are exactly K_(i,f), K_(i,V), K_(i,sc) and
K_(i,en) appearing in L124(10), as defined in L123(2), L120(3),
L121(3) and L122(2). In particular K_(i,V) is not K_(i,Vmix).
No coefficient value or cancellation identity is assumed.

## Conclusion

For both actual probes there are C_i<infinity and a common mesh
threshold N_0 such that for every admitted even N>=N_0,

    |R_H,tr-a^(-3)[K_(i,f)+K_(i,V)+K_(i,sc)+K_(i,en)]|
                       <= C_i N^(5/2)log(eN)
                       <= C_i N^(5/2)log(eN)^2.            (1)

Thus the complete transverse-H block meets the assessed component-rate
threshold. Equivalently its cubic-normalized remainder is bounded by
512 C_i N^(-1/2)log(eN). The outside factor 3 of the later other/other
response is not part of (1).

This is local RESEARCH / REPRODUCTION under the invocation-start EXPLORE
assessment `drafts/literature/2026-10-23-transverse-h-quantitative-remainder.md`.
It assembles imported estimates by finite algebra and inequalities,
without a novelty claim beyond the checked sources. The separate critical
audit in proof section 4 accepts this finite assembly conditional on
the imported complete estimates. Complete quantitative
L011 assembly, its remaining component/audit qualifications, finer
asymptotics and interacting estimates remain unresolved. No interacting
reflected-error bound, continuum theory, axioms or finite positive
infinite-volume mass follows; no Yang--Mills candidate is asserted.

## Proof

### 1. Subtract the coefficients in the exact finite telescope

L124 proof section 2, (7), defines

    Delta_V=R_bulk-R_bulk,moved,
    Delta_sc=R_bulk,moved-R_bulk,sc,
    Delta_P=R_bulk,sc-R_bulk,sc,Pbulk,
    Delta_en=R_bulk,sc,Pbulk-R_prod,
    Delta_C=R_prod-R_inf.

With E^f=E_(i,N)^f, its (8) is the finite scalar identity

    R_H,tr=E^f+R_pin+Delta_V+Delta_sc+Delta_P
                                      +Delta_en+Delta_C+R_inf. (2)

All five differences have plus signs. In particular Delta_en is the
energy-placement difference in its original orientation, and Delta_C
is the compression difference, distinct from Delta_P. The definition
already includes both generator orientations; no factor 1/2 or 2 is
restored. L124's later factor 3 has not been applied.

Use L268 and L269's identical finite insertion V_N to write exactly

    Delta_V-a^(-3)K_(i,V)
        =(Delta_V-V_N)+(V_N-a^(-3)K_(i,V)).               (3)

Subtracting the four coefficients from (2), and using L118(3), gives

    R_H,tr-a^(-3)[K_(i,f)+K_(i,V)+K_(i,sc)+K_(i,en)]
      =[E^f-a^(-3)K_(i,f)]+R_pin
        +(Delta_V-V_N)+[V_N-a^(-3)K_(i,V)]
        +[Delta_sc-a^(-3)K_(i,sc)]+Delta_P
        +[Delta_en-a^(-3)K_(i,en)]+Delta_C,              (4)

where R_inf=0 exactly. This subtraction is at fixed N, before any
absolute value or limit. The brackets use the original coefficients,
including their signs, physical lower-distance weights and heat
normalizations. No numerical coefficient comparison enters (4).

### 2. Match the complete finite allowances once

Put ell_N=log(eN). The following bounds apply to precisely the eight
summands of (4); constants in different rows may differ.

| Summand | Canonical complete estimate | Absolute bound |
| --- | --- | --- |
| E^f-a^(-3)K_(i,f) | L275(4) | c_(f,i) N^(5/2) ell_N |
| R_pin | L112(2) | c_(pin,i) N^(5/2) log N |
| Delta_V-V_N | L268(3) | c_(V0,i) N^(5/2) |
| V_N-a^(-3)K_(i,V) | L269(1) | c_(V1,i) N^(5/2) |
| Delta_sc-a^(-3)K_(i,sc) | L270(1) | c_(sc,i) N^(5/2) ell_N^(3/4) |
| Delta_P | L114(3) | c_(P,i) N^(5/2) (log N)^(3/4) |
| Delta_en-a^(-3)K_(i,en) | L271(1) | c_(en,i) N^(5/2) |
| Delta_C | L267(3) | c_(C,i) N^(5/2) |

The hypotheses match as follows. L112's R_pin is the retained pinned
energy correction in L124 proof section 2's split, with compact generator output
and every covariance input. L114 changes only the projection in the
collected scalar trace, so its difference is exactly Delta_P. L267
bounds R_prod-R_inf, so its first estimate is exactly Delta_C; its
second estimate for R_prod is not another allowance. L268 reduces
the same generator difference Delta_V to V_N that L269 compares with
K_(i,V); neither is the complete bound on the other summand of (3).

L270 already estimates the complete scalar-placement difference
Delta_sc against K_(i,sc), including its internal finite-P comparison.
That internal allowance is not added to its table row again. The
separate Delta_P in (2) compares different finite scalars and must
still be retained. L271 estimates the energy-placement difference
with compressed P_bulk already present; no additional finite-P
comparison is required there. L275 estimates the entire E^f,
including its f,f part, both mixed orientations and the combined
axial/static/boundary comparisons. None of those intermediate terms
is added separately to (4). Both heat polarizations, all constant
indices and the full heat sums are already part of each complete
estimate. There is no new infinite-sum exchange in this assembly.

All rows concern the same fixed displacement, forest, relative domains,
stored normalization and admitted mesh sequence. For each row and each
of i=3,6 choose its asserted finite mesh threshold. Take N_0 to be the
maximum of these finitely many thresholds, the threshold for (2) and
R_inf=0, and 8. This gives a common threshold without asserting an
explicit numerical N_0 or discharging any imported premise.

For N>=N_0, ell_N>=1 and 0<log N<=ell_N. Therefore
(log N)^(3/4)<=ell_N^(3/4)<=ell_N and 1<=ell_N.
Apply the triangle inequality to (4) and sum the eight nonnegative
constants in the table. Every summand is bounded by its constant
times N^(5/2)ell_N, proving the first inequality in (1). Since
ell_N<=ell_N^2, the assessed threshold follows. Multiplication by
a^3=512/N^3 gives the stated normalized bound, tending to zero.

### 3. Scope and failure checks

The relevant literature assessment was already saved before invocation
for this exact complete target; its known scalar inputs are reused
through the component results. No additional primary theorem or
reproof of a Green, Fourier, Wick or localization estimate is needed
for finite subtraction and the triangle inequality. This proves an
assembly consequence of those local inputs, not new mathematics
beyond the sources checked.

ATTEMPTS/030's failure concerns inserting varying masses into a
fixed-mass qualitative limit. Here only uniform complete finite bounds
are added, with no new mass choice. ATTEMPTS/032's separate absolute
kernel moments are not used. L118 cancels only R_inf; it does not
cancel any of the retained differences. Neither L220's pending scalar
recombination nor a presumed cancellation among the four coefficients
is used. The bound is an upper bound on the full signed remainder,
not a growth lower bound, an O(N^2) conclusion, or a full-response
estimate. The independent construction and infrared gaps persist.

### 4. Separate critical audit — 2026-10-24

**Verdict and scope.** The finite assembly (1)--(4) is accepted under
the stated imported premises, for both actual probes. This review used
the saved SPECIALIZE assessment
`drafts/literature/2026-10-24-transverse-h-assembly-critical-audit.md`.
It checked the full L124 telescope, the complete hypotheses/conclusions
of every table input, and the definition and projection passages
identified below. It does not recursively certify their analytic
proofs. No error requiring a repair, improved rate or coefficient
evaluation was found. This is RESEARCH / REPRODUCTION, not a new
bound beyond the existing component estimates or checked sources.

**Independent finite subtraction.** Expand the five differences of
L124(7) in order. Their sum is

    (R_bulk-R_bulk,moved)+(R_bulk,moved-R_bulk,sc)
      +(R_bulk,sc-R_bulk,sc,Pbulk)
      +(R_bulk,sc,Pbulk-R_prod)+(R_prod-R_inf)
        =R_bulk-R_inf.

Adding E^f+R_pin+R_inf gives R_H,tr by the two finite equalities
at the start of L124 proof section 2. Thus every placement difference
has the sign used in (2). Only R_inf is set to zero by L118(3).
Inserting +V_N-V_N and subtracting the four signed coefficients
gives exactly (4), with eight scalar summands before absolute values.
There is no additional coefficient or surviving full-grid term.

**Insertion and coefficient identity checks.** Both L268 and L269
start with precisely L119(3)'s V_N: its kernel is
B_(r,j,m)(d)=sum_(h,q)(d_m+h_m)A_r(h)C_r(q)e_j(d+h+q),
its output multiplier is partial_m u_(rho(r))(xi_t,xi_x), and its
middle factor is F_l(s)^T P F_k(t), with the original min(s,t).
Neither input has first replaced this finite P in the definition
of V_N. L269's coefficient is L120(3), whose tensor pairs B(d)
with q(-d); it is not the differently ordered Vmix coefficient.
L270 uses exactly L121(3)'s n_m and -(d_m-n_m) terms. L271 uses
L122(2)'s positive (d_m-n_m) product derivative; L122(4)--(6)
fixes the finite difference as psi(y+d-n)-psi(y), consistent with
Delta_en, rather than its negative. L275(4) uses L123(2)'s sum of
both mixed orientations with measure dtheta/(2pi)^3, while its
finite E^f is all three terms of L123(5), including f,f. Each of
these is the coefficient named in L124(10). These are definition
checks of the imported estimates, not additional analytic premises.

**Projection accounting.** The potentially overlapping comparisons
do not invalidate (4). To check this algebraically, write M(P) for
R_bulk,moved and S(P) for R_bulk,sc, and let replacement of the
displayed P by P_bulk define M(P_bulk), S(P_bulk). Then

    Delta_sc=M(P)-S(P),  Delta_P=S(P)-S(P_bulk),
    Delta_sc^bulk=M(P_bulk)-S(P_bulk),
    Delta_sc-Delta_sc^bulk
        =[M(P)-M(P_bulk)]-Delta_P.

L270 proof section 2 estimates this last whole comparison internally
and its conclusion estimates Delta_sc-a^(-3)K_(i,sc). It is not a
bound only on Delta_sc^bulk. Accordingly (4) still needs Delta_P,
bounded by L114(3). The underlying projection-row estimate may be
used in both bounds: this is a conservative triangle inequality,
not an extra copy of a scalar summand or an assumed independence.
No internal L270 allowance is added a third time. L271 already
starts at S(P_bulk), so no analogous projection allowance is added
to its complete conclusion. Likewise L267(3)'s second bound is
not added to its first, and L275(4) already includes the complete
L274(5) transfer and f,f part. The table uses all eight complete
conclusions once, including both parts of the generator split.

**Uniformity and normalization.** Each table input asserts a bound
for all sufficiently large admitted even N in the same fixed box,
at a=8/N and tau=1/16, with the same lower-rooted forest, stored
coordinates and bare-first order. None requires choosing a new
mesh-dependent mass or truncation in this assembly. All original
levels, source/end rows, upper pin, finite stencil filters, constant
indices and heat sums remain in the imported complete quantities.
The two insertion representations are those of the same actual
residual fixed in L124; this audit makes no replacement of that
residual or its orientation multiplicity. There are finitely many
table bounds and two probes (and, if represented separately, two
insertion forms). Taking the maximum of their asserted thresholds,
the identity thresholds and 8 is therefore legitimate. Constants
can similarly be enlarged over the two forms without claiming an
explicit N_0 or an unproved uniformity over varying physical data.

For that common N_0, the eight logarithmic factors are respectively
ell_N, log N, 1, 1, ell_N^(3/4), (log N)^(3/4), 1, 1.
All are at most ell_N=log(eN). Thus C_i can be the sum of the eight
nonnegative constants, proving the first bound in (1); ell_N>=1
gives the requested weaker ell_N^2 bound. Multiplying by
a^3=512/N^3 gives exactly 512 C_i N^(-1/2)ell_N, tending to zero.
L124 applies the outside factor 3 only in the complete other/other
group, so no such factor is missing in (1).

ATTEMPTS/030 and ATTEMPTS/032 remain valid stopped shortcuts: neither
a varying parameter in a qualitative limit nor a separate absolute
kernel moment occurs in this finite argument. No L220 cancellation
is used. This acceptance supplies no full quantitative L011 result,
upstream analytic audit, interacting bound, continuum axioms or
positive infinite-volume mass.

## Mathlib

Full matching transverse-H quantitative assembly: **not checked**.
Supporting finite telescoping, triangle inequalities, finite maxima
and elementary real-power/logarithm comparisons: **not checked**.
Unknown availability is not evidence of absence. This proof imports
the specialized analytic inputs by the precise canonical equations
above; section 4 audits their finite assembly, not their analytic
proofs. It is not a formal verification.
