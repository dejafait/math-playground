# L218 — The complete L011 residual coefficient has a finite cubic limit

## Hypotheses

Use exactly L011's bare fixed-mesh expansion and its coefficient
Gamma_(i,a) in (6), for SU(2), the all-face relative cube (-4,4)^4,
admitted even meshes a=8/N, the straight lower-rooted direction-1
forest, L008's complete compact displacement and both actual L010
Wilson-flow probes i=3,6 at tau=1/16. Take the small-coupling
coefficient first, then refine the mesh. All cumulants below are
L011's finite-partition cumulants in the exact forest Gaussian.

Import the complete statements L024(1), C057a(4), L147(1)--(5),
L148(1), L154(1)--(2), L180(1)--(3), L211(4), C212i(2) and
L217(2). Their analytic estimates and upstream limit arguments remain
inputs, including the separately audited local arguments in L180,
C212i and L217. This is an assembly, not a recursive audit.
Use L023(1)'s exact radial polynomial and L058(1)'s exact split
C=S_(3,top), Y=S_3-C. L048 fixes the original two-action normalization.

For numerical intervals only, keep every imported complete-spectrum,
moment, node, weight, saved-hexadecimal and time-integration premise,
and L039's stated IEEE binary64 addition/multiplication/FMA model,
arbitrary summation order, no overflow and local underflow allowance
10^-290. L084 supplies the matching complete D_3 interval and L147
imports the established bound 0<gamma<=1/3. No new numerical
integration or processor/BLAS verification is claimed. The limit
assembly itself needs only the analytic limit identities.

## Conclusion

The complete residual coefficient has a finite real limit

\[
 \lim_{a\to0}a^3\Gamma_{i,a}=\mathcal L_i,
 \qquad i=3,6,                                      \tag{1}
\]

where, in the unchanged canonical coefficient conventions,

\[
 \boxed{\mathcal L_i=P_i+A_i^{\rm dm}+\Lambda_i
       +K_{i,T}+K_{i,Vmix}-6K_{i,R}
       +3K_{i,oo}+12\gamma D_i.}                    \tag{2}
\]

Here P_i+A_i^dm=A_i^nr is the full nonradial action coefficient
of L217(2); it is not assigned a value or sign. In particular the
exact cubic compensation condition is

\[
 P_i+A_i^{\rm dm}
   =-\Lambda_i-K_{i,T}-K_{i,Vmix}+6K_{i,R}
                      -3K_{i,oo}-12\gamma D_i.      \tag{3}
\]

Equation (3) is equivalent to mathcal L_i=0 for each probe; it is
not established for either probe. Simultaneous compensation requires
both equalities with their actual, linked probe coefficients.

Writing mathcal K_i^rest for the right side of (2) without P_i+A_i^dm,
the imported numerical qualifications imply the coarse enclosures

    -51833.666572 < mathcal K_3^rest < 11235.893,
    -13341.12472  < mathcal K_6^rest < 18061.222.       (4)

Consequently compensation would require

    -11235.893 < A_3^nr < 51833.666572,
    -18061.222 < A_6^nr < 13341.12472.                (5)

These are necessary conditions only. Both rest intervals contain
zero, and there is no enclosure here for A_i^nr. Neither vanishing
nor nonvanishing of the complete coefficient is decided.

L010's separate divergence coefficient is bounded, so the full Ward
coefficient Gamma_(i,a)+gamma^H_(i,a) has the same cubic-scaled limit.
Even mathcal L_i=0 would give only Gamma_(i,a)=o(a^-3): smaller
powers, logarithms, finite matching and a cutoff-uniform coupling
expansion would remain unresolved. There is no interacting reflected
bound <=c_box/2, continuum construction, infrared finite positive mass
or Yang--Mills candidate. This is local REPRODUCTION of established
specialized limits by finite assembly, without a novelty claim.

## Proof

### 1. An exhaustive finite identity before any limits

For this paragraph abbreviate f=f_(i,0), r=r_0. Define the following
finite-mesh scalar contributions solely to display L011(6):

\[
\begin{aligned}
 F_i^{(4)}&=\kappa_0(f_{i,2},r),\\
 F_i^{(3)}&=\kappa_0(f_{i,1},r_1)
                      -\kappa_0(f_{i,1},r,S_3),\\
 I_i^{(4)}&=\kappa_0(f,r_2),\qquad
 I_i^{(3)}=-\kappa_0(f,r_1,S_3),\\
 H_i^{\rm coord}&=-\kappa_0(f,r,M_2),\\
 G_i^{\rm rad}&=-\kappa_0(f,r,S_{4,\rm rad}),\qquad
 G_i^{\rm nr}=-\kappa_0(f,r,S_4-S_{4,\rm rad}),\\
 T_i^{\rm top}&=\tfrac12\kappa_0(f,r,C,C),\qquad
 M_i=\kappa_0(f,r,C,Y),\qquad
 O_i=\tfrac12\kappa_0(f,r,Y,Y).
\end{aligned}                                                     \tag{6}
\]

The finite partition definition makes a cumulant multilinear and
symmetric in its arguments: each argument occurs linearly in exactly
one moment in each partition summand, and argument permutations
permute partitions. Therefore S_3=C+Y gives the exact identity

\[
 \tfrac12\kappa_0(f,r,S_3,S_3)=T_i^{\rm top}+M_i+O_i.\tag{7}
\]

Both ordered mixed regions contribute 1/2 and combine to M_i once.
L058(1) defines Y to contain every other plaquette, including zeros;
no assumption about boundary plaquette estimates is needed for (7).
Likewise multilinearity splits S_4+M_2 into exactly the three
negative-action/density terms in (6). Substitution into L011(6) yields

\[
 \Gamma_{i,a}=F_i^{(4)}+F_i^{(3)}+I_i^{(4)}+I_i^{(3)}
       +H_i^{\rm coord}+G_i^{\rm rad}+G_i^{\rm nr}
                         +T_i^{\rm top}+M_i+O_i.     \tag{8}
\]

This is an equality for the original mesh, probe and forest, not a
replacement by separate curvature-only or frozen polynomials.

### 2. Take limits of complete groups in their established scope

Apply the imported results to (8), in the following precise groupings.

| Finite contribution | Cubic-scaled limit and canonical justification |
| --- | --- |
| F_i^(4) | 0 by C212i(2), for the entire original quartic probe |
| F_i^(3) | 0 by L211(4), for the joint cubic probe group |
| I_i^(4) | Lambda_i by L154, for the entire quartic residual |
| I_i^(3) | K_(i,T)+K_(i,Vmix)-6K_(i,R) by L180, proof section 4 |
| H_i^coord | 0 by L148(1), which bounds its magnitude by C_i a^-2 |
| G_i^rad | 0 by L023(1) and L024(1), which bounds the whole term by C_i |
| G_i^nr | P_i+A_i^dm by L217(2), for every nonradial action plaquette and pairing class |
| T_i^top | 0 by C057a(4), which gives a finite a^2-scaled limit for this cubic term alone |
| M_i+O_i | 12 gamma D_i+3K_(i,oo) by L147's imported full-group limit identities |

For the top/top row, if a^2 T_i^top tends to the finite ell_i in
C057a(4), then a^3 T_i^top=a(a^2 T_i^top) tends to zero. Its
nonzero quadratic-scale coefficient does not survive the extra a.
The same elementary argument applies to the stated O(a^-2) and O(1)
rows. C212i supplies O(N^(5/2)log(eN)); multiplication by (8/N)^3
gives a vanishing O(N^-1/2 log(eN)). L211 applies to F_i^(3) jointly;
no separate limits of its two terms are required or inferred.

C057a's joint group is W_i+T_i^top, with
W_i=-kappa_0(f,r,S_(4,nr,top)). W_i is already inside G_i^nr.
Only T_i^top, as separately identified by C057a(4), appears in (8).
Thus no shared upper quartic is counted twice. L084's conditional
quartic also stays inside M_i; it is not an additional row. The
outside factor 3 in 3K_(i,oo) is already the one in L147. There is
no outside factor 3 on Lambda_i or the complete I_i^(3), and no
two-action 1/2 on the single-action I_i^(3).

Every nonzero row limit is finite under its imported hypotheses.
Since (8) has finitely many rows, convergence is preserved by their
sum: given any positive tolerance, choose a refinement threshold for
each complete row with error below that tolerance divided by ten,
then use the most restrictive threshold and the triangle inequality.
No internal heat sum, spatial sum or mass limit is interchanged here;
those have already been controlled in the respective input theorems.
This proves (1)--(2), and rearranging (2) proves the equivalence (3).

### 3. Exact arithmetic for the remaining compensation threshold

L147 gives -86414.508<3K_(3,oo)<-46729.107. Its imported
0<gamma<=1/3 and L084's -237.289643<D_3<0 give

    -949.158572=-4(237.289643)<12 gamma D_3<0.

Thus the complete triplet two-action contribution M_3+O_3 has
cubic limit in (-87363.666572,-46729.107). L147(5) already gives
the shear two-group interval (11864.87528,33336.222).
Add L154(2) and L180(3), whose original cumulant signs agree with
(6). All endpoint arithmetic is exact terminating-decimal arithmetic:

    -49200+84730-87363.666572 = -51833.666572,
    -43073+101038-46729.107 = 11235.893,
    20982-46188+11864.87528 = -13341.12472,
    21570-36845+33336.222 = 18061.222.

This proves (4). No independence between coefficients is assumed:
simultaneous valid interval inclusions can always be added, although
correlations can make the resulting enclosure wider. Negating (4)
gives the necessary conditions (5) if (3) holds. Membership in these
intervals cannot establish the equality (3).

### 4. Ward convention, known traps and source scope

L011(14) adds gamma^H to Gamma for the full Ward response.
L010(8)--(9) gives a finite limit for gamma^H, so a^3 gamma^H tends
to zero. The coordinate density in (8) remains a different term.
L019(2)--(5) asserts complete fixed-mesh forest invariance through
compensation of jets, not that the coefficient vanishes. No such
vanishing premise or termwise forest invariance is used here.

All imported row limits concern the same probes, bare normalization,
relative boundary conditions and straight forest. They retain their
colors, both residual subtractions, single-/two-action factors,
ordered/coincident plaquettes, boundary rows, constant modes, upper
jumps and full heat sums. Finite-group addition deletes none of
these. It does not certify the upstream estimates anew.

The unchanged ready assessment is
`drafts/literature/2026-10-16-complete-residual-coefficient-cubic-assembly.md`.
Its inspected Del Debbio--Patella--Rago, JHEP 11 (2013) 212,
1306.1173v1 section 6 (6.1)--(6.16), Luescher--Weisz,
JHEP 02 (2011) 051, 1101.0963v2 sections 7.1--7.4 and 8.2/8.4,
and Ramos--Sint, 1508.05552v1 sections 3.1/3.4 do not evaluate
this bare all-face forest coefficient. No external theorem is
reproved or newly specialized: the work is the finite applicability
and overlap check above. Prior local failures of isolated forest
interpretations and removal of I_i^(3) remain valid. No full matching
result or originality follows from the failed literature match.

### 5. Separate critical audit, 2026-10-17

Audit YM-20261017-272-complete-residual-assembly-audit accepts
(1)--(5) relative to the imported statements in the hypotheses.
No local mathematical correction is required. This is verification
of the finite assembly and applicability, not an independent proof
of all upstream estimates or numerical inclusions.

**Exhaustion from the original coefficient.** Independently track the
coefficient of s t g^2 in the formal expression

    log E_0 exp(s[f_0+g f_1+g^2 f_2]
               +t[r_0+g r_1+g^2 r_2]
               -g S_3-g^2[S_4+M_2]).

Here f_j denotes f_(i,j), and this expression means a finite formal
moment computation through the indicated degree, not a convergent
moment generating function for quartics. L011's partition definition
makes its source coefficient a cumulant. Selecting degree two in g
leaves exactly: the three pairs (f_2,r_0), (f_1,r_1), (f_0,r_2);
the two single-action triples (f_1,r_0,-S_3), (f_0,r_1,-S_3);
the one triple (f_0,r_0,-S_4-M_2); and the four-cumulant with two
-S_3 occurrences and coefficient 1/2. In particular, the insertion
jets already use Taylor coefficients, not raw derivatives requiring
another factorial. These are precisely L011(6)'s seven terms.

Grouping the f_1 terms removes one row, splitting S_4+M_2 adds two,
and splitting the two cubic-action occurrences adds two. This gives
exactly the ten scalar rows in (8). In the cubic split the ordered
regions are top/top, top/other, other/top and other/other, including
coincident plaquettes where allowed. Cumulant symmetry identifies
the two mixed regions; their two halves give one M_i. L058's proof
section 1 includes every remaining plaquette in Y, including vanishing
axial cubics and boundary zero rows. No support sector is omitted.

**Factors and overlaps.** L048's proof sections 2--3 count the two
surviving connected classes with the original two-action half: the
split quadratic paths have coefficient 3, and the two serial quadratic
orientations each have 3/2 before exchanging the ordered plaquette
pair. Thus the factor in the already contracted other/other input
cannot be applied to every row of (8). L147 defines O_i and M_i
exactly as (6), and supplies 3K_(i,oo) and 12 gamma D_i for them.
L180's proof section 4 explicitly identifies the complete negative
single-action cumulant with K_(i,T)+K_(i,Vmix)-6K_(i,R), with no
additional half or factor 3. L154 identifies Lambda_i with the whole
positive quartic residual covariance, likewise without a new factor.

C057a defines its joint group as W_i+C_i, where W_i is the upper
nonradial quartic and C_i=(1/2)kappa(f,r,C,C). Its proof section
“Compare the same quartic once” obtains C_i's limit by subtracting
W_i. Hence importing C057a(4) for T_i^top, while keeping W_i inside
G_i^nr, is disjoint accounting. Importing the joint group instead
would double count W_i; (8) does not do so. L084(2)'s conditional
quartic is already within the imported M_i and is not added again.
The radial polynomial in L023(1) agrees with the polynomial subtracted
in the definition of G_i^nr inherited by L217 from L025; the split is
of the action S_4 only, not a deletion from r_2 or the probe jets.

**Applicability of complete inputs.** The inspected hypotheses of
all row inputs agree on SU(2), the relative all-face cube, the actual
two L010 probes at tau=1/16, bare normalization, and coefficient-first
refinement along a=8/N. The forest-dependent inputs use the straight
lower-rooted direction-1 forest. Different stored, physical or
whitened coordinates inside their proofs do not introduce a new
conversion here: their conclusions identify the original L011 scalar
cumulants. In particular, L148's proof section 1 explicitly restores
the density's three-color normalization; the density is not L010's
separate divergence insertion.

L211(4) and its proof section 5 concern the *joint* f_1 group, not
each summand. C212i(2), via its proof section 5 and imported C212h,
concerns the whole original forest f_2 response, not an isolated
co-closed flow term. L217(2) and proof section 4 restore the entire
nonradial action via L216(16); P_i alone is not that coefficient.
No estimate is newly transferred across a forest change, a boundary
row, a nonlinear flow summand or a residual component. All colors,
normal end rows, constant modes, upper jumps, both subtractions and
full heat sums remain inside those original complete statements.

The subcubic conversions are valid with fixed aN=8: a finite a^2
limit, O(a^-2), O(1), and O(N^(5/2)log(eN)) each give zero after
multiplication by a^3. For the joint cubic probe only its asserted
zero limit is used; no unjustified O(N^(5/2)) bound is assigned to
that whole group. The finite sum of the resulting scalar limits
requires no further interchange with any internal spectral sum.
The top/top limit's finiteness uses its analytic identity, not the
IEEE-dependent sign enclosures. L010(8)--(9) is bounded, so L011(14)'s
plus divergence convention changes no cubic coefficient.

**Independent endpoint check and disposition.** L147's triplet
other/other interval and 0<gamma<=1/3, together with L084's complete
D_3 interval, give (-87363.666572,-46729.107) for M_3+O_3.
The strict lower bound remains strict even if gamma=1/3 because
D_3>-237.289643. The corresponding shear interval is exactly
L147(5). Reexpressing all endpoints as integers in units of 10^-6,
the four additions in (4) are

    -49200000000+84730000000-87363666572 = -51833666572,
    -43073000000+101038000000-46729107000 = 11235893000,
     20982000000-46188000000+11864875280 = -13341124720,
     21570000000-36845000000+33336222000 = 18061222000.

These reproduce (4) exactly; reversing and negating endpoints gives
(5). Shared coefficient correlations affect sharpness, not inclusion.
Neither interval membership nor L019's forest-change invariance
establishes (3). ATTEMPTS/022's frozen-cancellation failure and
ATTEMPTS/038's isolated residual/action nonvanishing remain compatible
with this audit. The audit supplies a checked assembly for the later
compensation test, not a value for P_i+A_i^dm or a new result beyond
the assessed sources. All imported analytic and IEEE premises remain.
Full matching Mathlib coverage is still not checked.

## Mathlib

Full matching specialized complete residual limit: **not checked**.
Supporting finite-sum limit, multilinearity of cumulants and interval
arithmetic coverage: **not checked**. Unknown coverage is not absence.
The analytic and numerical inputs are the canonical statements cited
above; no Mathlib theorem is asserted to replace them.
