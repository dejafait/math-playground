# L278 — Complete coefficient quantitative remainder

## Hypotheses

Use precisely L011(6)'s coefficient Gamma_(i,a) and L218(2)'s
coefficient mathcal L_i. Keep SU(2), the all-face relative fixed-link
cube (-4,4)^4, sufficiently fine admitted even N, a=8/N, tau=1/16,
the straight lower-rooted direction-1 forest, ordinary stored
coordinates and the bare small-coupling coefficient taken at fixed
mesh before refinement. Use both actual probes i=3,6 and the unchanged
fixed compact displacement. Retain three colors, both residual
insertion subtractions and their actual forms/orientations, every
source and normal/end row, upper pin and jump, allowed constant
component indices, ordered plaquette pairs and full exterior heat sums.

Import L218(6)--(8)'s exact ten-group identity and coefficient
conventions. Import the complete bounds C212i(2), L266(1), L254(2),
L263(1), L148(1), L024(1), L232(2), C057a(4) and L277(2), retaining
all their upstream analytic and audit qualifications. L023(1) identifies
the radial group. L154 identifies Lambda_i with the entire quartic
residual coefficient, L180 proof section 4 retains the complete
residual/action normalization, and L217(2) identifies the full
nonradial coefficient as P_i+A_i^dm. These are original scalar
cumulants; no coordinate change or new transfer estimate is assumed.

For the mixed group import L084(3)--(6) and proof sections 3--4:
its exact partition, the stated complete discarded-group bounds and
the centered first-pair identity and path/path bound. Import L221(2)
and L222(1) with their hypotheses, for precisely that centered
circulation trace and finite diagnostic. The torus constant gamma
is the same finite constant as in L084/L221; no numerical value is
used. All of these analytic inputs are conditional premises here;
this finite assembly does not independently verify them.

## Conclusion

There are finite constants C_i and one threshold N_0, independent of
N, such that for both actual probes and every admitted even N>=N_0,

    |Gamma_(i,a)-a^(-3)mathcal L_i|
                       <= C_i N^(5/2)log(eN)^2,                (1)

with exactly

    mathcal L_i=P_i+A_i^dm+Lambda_i
                +K_(i,T)+K_(i,Vmix)-6K_(i,R)
                +3K_(i,oo)+12 gamma D_i.                     (2)

Equivalently the scaled error is at most
512 C_i N^(-1/2)log(eN)^2. The conclusion is a conditional finite
assembly under the unchanged pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-25-complete-coefficient-quantitative-assembly.md`.
It is local RESEARCH / REPRODUCTION, with no claim of discovery beyond
the checked sources. The separate critical audit in proof section 4
accepts this assembly conditional on its imported estimates. No value,
sign or cancellation of (2), O(N^2) remainder,
finer asymptotic, cutoff-uniform interacting expansion, nonzero physical
sector, reflection positivity, continuum axioms or finite positive
infinite-volume mass is proved. This is not a Yang--Mills solution
candidate; every upstream analytic/audit qualification remains.

## Proof

### 1. Match the original complete quantities on a common range

Use the scalar group names in L218(6). Its identity (8), obtained
from L011(6) before limits, is

    Gamma=F^(4)+F^(3)+I^(4)+I^(3)+H^coord
                         +G^rad+G^nr+T^top+M+O.              (3)

Here F^(3) is the joint difference of the two cubic-probe cumulants,
I^(3) is the complete negative single-action cumulant, M=kappa(f,r,C,Y)
and O=(1/2)kappa(f,r,Y,Y), with C=S3_top and Y=S3-C.
Thus the two mixed ordered regions have already combined into M once.
The Taylor jets use L011's Taylor coefficients, so no new factorial
is needed. The radial polynomial is exactly L023(1), as subtracted
inside G^nr; its action split does not delete insertion or probe jets.

Each imported complete bound concerns these same original scalar
quantities, fixed data and admitted even meshes. L024's orthonormal
coordinates represent the same radial cumulant by L023 and L218;
we do not apply its bound to a different stored-coordinate polynomial.
Take N_0 at least 8 and the maximum of the finitely many thresholds
of all bounds below for both probes, including their compact-stencil
support conditions. The finite a^2 T^top limit from C057a(4) also
gives a threshold: for each probe, convergence to its finite ell_i
implies |a^2 T^top|<=|ell_i|+1 eventually. Its analytic finiteness,
rather than a numerical sign enclosure, suffices. Enlarge N_0 to
include these two thresholds. Every bound now holds simultaneously.
Their constants depend only on the fixed data and imported estimates.

### 2. Assemble the mixed group with its single factor six

L084(6) gives exactly

    M=6[T_Z+E^(1)+F^dir+F^ax+S^dir+S^ax+R^other].          (4)

Its proof section 3 provides the following complete heat-summed
bounds, before the outside factor six:

| Quantity | Bound |
| --- | --- |
| T_Z | c_(Z,i) N^(3/2) |
| E^(1) | c_(E,i) N^(3/2) |
| F^ax | c_(F,i) N^2 |
| S^dir | c_(d,i) |
| S^ax | c_(a,i) N^2 |
| R^other | c_(r,i) N^(5/2) |

The first two bounds use a=8/N in their O(a^(-3/2)) statements.
Consequently their signed sum R_i has |R_i|<=r_i N^(5/2)
for some finite r_i and N>=N_0.

L084 proof section 4 imports the exact simultaneous centering
identity F^dir=bar P_i+bar F_i^circ, with |bar P_i|<=p_i N^2.
The bar F_i^circ here is exactly L221(2)'s F_(i,N)^circ:
both are the full circulation/path trace with the centered bar Q_l,
unchanged base row, covariance, pinned domains and full heat weights.
This is the identification already used in L084's surviving trace
argument, rather than an application to an uncentered trace.
The O(N^2) exterior-centering defect is retained in this decomposition:
simultaneous centering transfers it to bar P_i; it is not set to zero
or counted a second time. L221(2) already includes the O(N^2)
curl-energy comparison remainder in its complete trace bound.

Write D_(i,a) for the unchanged finite diagnostic. L221(2) and
L222(1) give constants j_i,d_i with

    |a^3 bar F_i^circ-2 gamma D_(i,a)|<=j_i N^(-1/2),
    |D_(i,a)-D_i|<=d_i/N.                                  (5)

First subtract 2 gamma D_i with its sign, then use the triangle
inequality. Since a^(-3)=N^3/512, (5) implies

    |bar F_i^circ-2 gamma a^(-3)D_i|
       <=(j_i/512)N^(5/2)+(2|gamma|d_i/512)N^2.             (6)

Substitution of F^dir=bar P_i+bar F_i^circ in (4) therefore gives

    |M-12 gamma a^(-3)D_i|
      <=6[(r_i+j_i/512)N^(5/2)
                         +(p_i+2|gamma|d_i/512)N^2]
      <=m_i N^(5/2).                                      (7)

This explicitly accounts for all nine original mixed placements
through L084's exact partition. The factor 12 is six times the
trace coefficient two. No extra ordered-pair half or color factor
is inserted. L084's conditional quartic is already inside M and
is not a further contribution to (3). No numerical diagnostic sign
or gamma enclosure is used in (5)--(7).

### 3. Subtract all ten coefficients before taking magnitudes

Let ell_N=log(eN)>=1. The complete row bounds are as follows, with
independent nonnegative finite constants in each row:

| Original complete row | Coefficient subtracted as a^(-3) times this entry | Absolute remainder bound | Input |
| --- | --- | --- | --- |
| F^(4) | 0 | c_(4,i) N^(5/2) ell_N | C212i(2) |
| F^(3) | 0 | c_(3,i) N^(5/2) ell_N^2 | L266(1) |
| I^(4) | Lambda_i | c_(I4,i) N^(5/2) ell_N^(3/4) | L254(2) |
| I^(3) | K_(i,T)+K_(i,Vmix)-6K_(i,R) | c_(I3,i) N^(5/2) ell_N | L263(1) |
| H^coord | 0 | h_i N^2/64 | L148(1) |
| G^rad | 0 | g_i | L023(1), L024(1) |
| G^nr | P_i+A_i^dm | c_(nr,i) N^(5/2)/512 | L232(2) |
| T^top | 0 | t_i N^2/64 | C057a(4), section 1 above |
| M | 12 gamma D_i | m_i N^(5/2) | (7) |
| O | 3K_(i,oo) | c_(oo,i) N^(5/2) ell_N | L277(2) |

The sum of the signed middle-column entries is exactly (2), in
L218's conventions. In particular the residual/action entry retains
its negative six, the other/other entry has its single outside three,
and Lambda_i has neither an extra three nor a two-action half.
K_(i,Vmix) is the residual/action coefficient, whereas K_(i,V)
inside K_(i,oo) is its different displacement-placement coefficient.
We do not identify them or use cancellation between them.

Subtract a^(-3) times that signed column sum from (3). The result
is exactly the sum of the ten coefficient-subtracted rows in the
table. Now apply the triangle inequality to that equality. For N>=1,
every displayed remainder bound is dominated by its constant times
B_N=N^(5/2)ell_N^2: N^2<=N^(5/2), 1<=N^(5/2), and
1, ell_N^(3/4), ell_N are all at most ell_N^2. Thus (1) holds,
for example with the sum of the ten row constants after absorbing
the displayed 1/64 and 1/512 factors. Taking the maximum of the two
resulting constants also gives a single constant for both probes.
Multiplication by a^3=512/N^3 proves the stated scaled bound.

Only complete allowances are used once. The five internal bounds of
L266, the branch/trace bounds of L263, the replacements of L254/L232
and the eleven sectors of L277 are not extra rows. C057a's shared
upper quartic remains within G^nr; only its separately identified
top/top cubic T^top appears in the table. Coordinate Haar density
is H^coord, distinct from L010's separate divergence insertion,
which is absent from the requested Gamma. No internal heat, spatial,
volume or mass limit is exchanged by this finite addition.

The specialization is solely exact applicability and finite signed
addition of already qualified estimates. The ready assessment records
the primary coverage, including Lawler--Limic, *Random Walk: A Modern
Introduction* (Cambridge, 2010), Theorem 4.3.1 pp. 81--84 and
Proposition 4.6.2(a) p. 97, used within L221
([author text](https://www.math.uchicago.edu/~lawler/srwbook.pdf)), and
NIST DLMF v1.2.8, section 1.4(vi), (1.4.35)--(1.4.37), used within
L222 ([primary text](https://dlmf.nist.gov/1.4#vi)).
No primary analytic theorem is reproved or newly applied
here. ATTEMPTS/030's nonuniform fixed-mass closure and ATTEMPTS/032's
divergent separate absolute kernel moments are preserved: (1) uses
neither shortcut. It does not establish actual signed growth, the
value of mathcal L_i, a finer bound, or an interacting conclusion.

### 4. Separate critical audit — 2026-10-25

Audit YM-20261025-471-complete-coefficient-assembly-critical-audit,
under the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-25-complete-coefficient-assembly-critical-audit.md`,
accepts (1) with exactly (2), conditional on the stated complete inputs.
No correction of the finite assembly is required. This is local
RESEARCH / REPRODUCTION verification, not a new analytic estimate,
recursive certification of the inputs or discovery beyond the checked
sources. The following checks are independent of any coefficient value.

**Exhaustion and signed subtraction.** Reading L011(6) directly gives
three positive jet pairs, two negative single-cubic-action terms, one
negative quartic-action/density term and one positive two-action term
with factor 1/2. Combine the two terms involving f_(i,1) into F^(3).
Split the quartic-action/density term into H^coord, G^rad and G^nr.
For C=S3_top and Y=S3-C, symmetry and multilinearity give

    (1/2)kappa(f,r,C+Y,C+Y)
      =(1/2)kappa(f,r,C,C)+kappa(f,r,C,Y)
                              +(1/2)kappa(f,r,Y,Y).

This produces exactly the ten rows in (3), with the mixed halves
combined once. The homogeneous jets already have L011(2)'s Taylor
factorials. Subtracting a^(-3) times L218(2) from this identity yields,
before absolute values, the sum of F^(4), F^(3), H^coord, G^rad, T^top and
the five differences

    I^(4)-a^(-3)Lambda_i,
    I^(3)-a^(-3)[K_(i,T)+K_(i,Vmix)-6K_(i,R)],
    G^nr-a^(-3)[P_i+A_i^dm],
    M-12 gamma a^(-3)D_i,
    O-3a^(-3)K_(i,oo).

Their subtracted coefficients add to exactly L218(2). The complete
negative single-action cumulant in L263(1) agrees with L180 proof
section 4; its minus six is retained. L154 and L254 concern the
entire positive quartic residual covariance. L277 concerns the original
half-weighted other/other cumulant and already supplies its outside
three. Its K_(i,V) is distinct from K_(i,Vmix). No cancellation between
named coefficients is used.

**Centered trace, sign and allocation.** L084(3)--(6) partitions the
nine mixed covariance replacements into three same-row terms, two
residual-row-1 terms and the remaining four ordered placements. The
last four are exactly its two grouped lines. Splitting those lines as
L084 does gives the seven terms inside the single six in (4); no
additional mixed ordering or color factor remains to be applied.

For the delicate centered-trace identification, inspect L074(9)--(11)
and L076(1). At each exterior pair, L074 writes the original direct
first pair as P+F_circ and proves

    bar P=P+delta,  bar F_circ=F_circ-delta.

Its simultaneous determinant-one shear preserves their sum. With
bar B_b=B_b-D/2, the exact DS=0 implies bar B_b S=B_b S. Consequently
using barred rough paths in bar Q, as L078 does, gives the same
circulation trace as L074's centered exterior coefficients. In the
notation of those inputs, that trace is exactly

    sum_(k,l)c_(i;kl) sqrt(N)
      Tr[G C_(r_k) G E_0^T A_0 I_T Sigma_T D^T bar Q_l S].

This is L076(1), with the same operator order, covariance, source/end
rows, axial levels and heat weights. L078(3) compares this very trace
with J_(i,N); L079(1)--(3) fixes its diagnostic and full-torus gamma.
These identify the objects in L221(2) with those in L084's surviving
trace. L222's diagnostic uses the same upper average, physical sa
weight, prefix and full heat sum. No uncentered or frozen trace has
been substituted.

The complete exterior defect delta is retained inside bar P. L084
imports an O(N^2) bound for that complete bar P; adding another defect
allowance is unnecessary, and setting the defect to zero is invalid.
The distinct curl-energy O(N^2) comparison is already included in
L221(2). Thus the unscaled error follows directly from

    a^3 bar F_i^circ-2 gamma D_i
      =[a^3 bar F_i^circ-2 gamma D_(i,a)]
                              +2 gamma[D_(i,a)-D_i].

Its magnitude is at most j_i N^(-1/2)+2|gamma|d_i/N.
Multiplication by N^3/512 gives the two terms in (6).
The six other complete terms of L084 have orders
N^(3/2), N^(3/2), N^2, 1, N^2 and N^(5/2), respectively.
They and bar P are therefore covered by (7). The coefficient is
precisely six times two, with a positive sign: 12 gamma D_i.
L084's conditional quartic is internal to this same M, not an
eleventh complete group.

**Complete bounds and overlaps.** The inspected hypotheses and
conclusions of C212i, L266, L254, L263, L148, L024, L232 and L277
identify exactly the corresponding original scalar cumulants above.
L266 bounds the joint cubic difference, so separate bounds for its
two original cumulants are unnecessary. Its five internal allowances
are already included. L254 and L263 likewise include their complete
replacement/branch errors, and L277 includes its eleven sectors.
Their internal estimates are not further rows of the full response.
L023(1) identifies the radial polynomial bounded by L024(1), so its
orthonormal representation creates no new coordinate conversion here.
L148 bounds coordinate Haar density, not the separate Ward divergence.

C057a's proof paragraph "Compare the same quartic once" obtains the
finite limit of a^2 T^top by subtracting the shared upper quartic from
the joint upper group. L278 imports only this cubic limit. The upper
quartic remains in G^nr, where L232 bounds the complete group against
L217(2). For a finite limit ell_i, eventually
|a^2 T^top|<=|ell_i|+1, giving the stated N^2/64 bound. Numerical
sign enclosures are not needed for this implication.

**Common range and final threshold.** All complete statements keep
the same fixed relative SU(2) cube, lower-rooted forest, a=8/N,
tau=1/16, displacement and actual probes; their constants may depend
on these fixed data. All require only sufficiently large admitted even
N. Take the maximum of their finitely many thresholds, the two eventual
top/top thresholds and the fixed-support requirements, and 8. This
retains both probes, all forms/orientations, constant modes and upper
pins. There is no mesh-dependent choice of an internal regulator.

Put ell=log(eN) and divide each row's allowance by N^(5/2)ell^2.
Apart from its mesh-independent constant, in table order the ratios are

    ell^(-1), 1, ell^(-5/4), ell^(-1),
    N^(-1/2)ell^(-2)/64, N^(-5/2)ell^(-2),
    ell^(-2)/512, N^(-1/2)ell^(-2)/64,
    ell^(-2), ell^(-1).

Each is at most one on the common range. The triangle inequality
therefore proves (1) with a finite sum of constants; multiplying by
a^3 gives exactly 512 C_i N^(-1/2)log(eN)^2. This uses a finite sum
of already complete inequalities, with no new heat, mass or volume
limit interchange. ATTEMPTS/030/032's stopped shortcuts are not used.

The audit verifies the conditional remainder against the unevaluated
coefficient. It does not use L220, decide cancellation, improve the
N^(5/2)log(eN)^2 threshold to N^2, or provide an interacting bound.
All upstream analytic/audit qualifications and the continuum and
infrared gaps remain. Mathlib coverage remains as stated below.

## Mathlib

Full matching specialized complete coefficient remainder: **not
checked**. Supporting finite sums, triangle inequalities, scalar
big-O and elementary power/log comparisons: **not checked**. Unknown
availability is not absence. No Mathlib declaration is asserted to
replace the qualified component estimates or the missing continuum
and infrared construction.
