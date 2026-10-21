# L230 — Quantitative remainder for the complete direct/mixed action block

## Hypotheses

Keep exactly L217's relative SU(2) cube D=(-4,4)^4, admitted even
meshes a=8/N, straight lower-rooted direction-1 forest, actual probes
i=3,6 at tau=1/16, and bare expansion at fixed mesh before refinement.
Use its original stored-coordinate residual A=C^T J_N C, covariance
Sigma, tensor K, direct/mixed response T_i^dm and coefficient A_i^dm.
The displacement and both strain insertions are the fixed smooth
compactly supported ones of the imported construction, including
their actual mesh samples. Constants may depend on these data and tau,
but not on N or heat labels.

Retain both generator orders, both insertion subtractions, all three
colors, the direct/direct and both original mixed orientations, every
relative boundary and normal end row, allowed constant modes and the
entire heat spectrum. In particular no two-prefix plateau term is
included in T_i^dm. L217's qualitative limit and L200/L211's exact
relative heat representation and local factorization are imported.

## Conclusion

For both actual probes, for all sufficiently fine admitted meshes,

    |a^3 T_i^dm-A_i^dm| <= C_i log(eN)/N,                 (1)

or equivalently

    |T_i^dm-a^(-3) A_i^dm| <= C_i N^2 log(eN).           (2)

This is stronger than the tested O(N^(5/2) log(eN)^2) allowance.
The separate critical audit in proof section 7 accepts this quantitative
argument relative to the stated imported inputs.
It gives no plateau-continuum rate, rate for every other response
component, interacting expansion or reflected-error bound <=c_box/2.
Continuum axioms and finite positive physical mass remain unresolved.
This is local standard-estimate progress under the prior EXPLORE
assessment, with no claim of originality beyond the sources checked.

## Proof

### 1. Compare kernels on compact internal rows, retaining every source

Write B_N=C Sigma and B_infinity=C_infinity Sigma_infinity, with the
integer lower-vertex indexing of L217. Put j_N=aJ_N and extend j_N
by zero to all infinite plaquette rows. By L211(10)--(12), its row
and column support lies in a fixed compact physical interior Q of D,
with bounded stencil range, bounded overlap and coefficients bounded
independently of N. Enlarge Q by the fixed stencils once. Its distance
from every face is at least rho>0 for all sufficiently large N.

For any internal row p in this enlargement and every actual source
link e, including normal end links, the following comparison is uniform:

    |B_N(p,e)-B_infinity(p,e)| <= C_rho N^-3,
    |B_infinity(p,e)| <= C(1+|p-e|)^-3.                  (3)

The second estimate is L217(9). To justify the stronger source domain
of the first, use L200(5)'s exact relative component heat images,
with one even own-direction reflection and three odd reflections.
Because p is rho N/8 lattice units from all faces, each nearest
nondirect image has distance at least c_rho N from p for *every*
source e in the closed box. This follows coordinatewise from
p_r+e_r>=c_rho N and 2N-p_r-e_r>=c_rho N in the reflected coordinate;
the staggered half-steps and bounded circulation shifts only change
the constant. The direct image is exactly the infinite component
kernel with the original offsets.

Integrate the m=1 heat estimate only up to N^2 for these images.
The nearest ones cost O_rho(N^-3). For a further period-2N image
indexed by z in Z^4, its distance is >=cN(1+|z|) after grouping
finitely many nearest images, and its integral is bounded by

    C_b N^-b (1+|z|)^-b
         integral_0^(N^2) (1+t)^((b-5)/2) dt
       <= C_b' N^-3 (1+|z|)^-b.

Choose b>10 and sum z. For t>=N^2 the full finite differentiated
product spectrum is bounded by C N^-5 exp(-ct/N^2), and the infinite
heat tail by C(1+t)^(-5/2). Each integral is O(N^-3).
These are precisely the image/time domains in L217's audit, now
using separation of the *internal row* instead of both arguments.
All allowed own-direction zero modes remain in the finite spectrum.

When a formal source in a traversal or prefix is a fixed tangential
link, set its finite column equal to zero, as in the actual relative
space. Such a source lies on a physical face, so |p-e|>=c_rho N
and the second bound in (3) gives the first directly. This convention
only adds zero finite columns. It neither deletes a variable normal
end link nor changes a covariance boundary condition.

Consider a direct source e and one of the two actual endpoint fibers
f_r, 0<=r<j, of a transverse traversal at axial level j<N. Any fixed
endpoint uses the zero-column convention just explained. In the exact
formula

    a mathscr V(e,f)=sum_(p,q) B_N(p,e) j_N(p,q) B_N(q,f),
    mathscr V=Sigma A Sigma,                           (4)

replace both B_N factors by B_infinity, keeping j_N unchanged.
There are O(N^4) internal rows, a bounded number of q per p, and

    sum_(p in Q_N) (1+|p-e|)^-3 <= C N

uniformly over all sources, by the four-dimensional shell count.
Thus the sum of the absolute product errors over the *whole fiber*
is at most

    C[N^-3 sum_(r<j,p) ((1+|p-e|)^-3+(1+|q-f_r|)^-3)
                         +N^-6 N^4 j]
       <= C/N.                                        (5)

Bounded shifts q-p and coefficient overlap are absorbed into C.
For the direct/direct pair the same count is O(N^-2).
The transposed mixed orientation has exactly the same bounds with
the two kernel factors interchanged. This proves (5) for each
orientation separately, without asserting positivity or commuting J_N.

### 2. Sum the joint kernel/fiber spatial tail before freezing

Use the equivalent lattice norm |(s,t)|=|s|+|t|_1, s in Z,
t in Z^3. Let

    b(s,t)=(1+|s|+|t|_1)^-3,
    H(t)=sum_(n in Z) b(s+n,t) <= C(1+|t|_1)^-2,
    F(s,t)=b(s,t)H(t).                                 (6)

H does not depend on s. Extending a finite or a half-infinite fiber
to the full line only enlarges this nonnegative majorant. Every
bounded traversal/stencil shift is covered by a fixed multiple of F:
the transverse positions of the direct edge and the endpoint fiber
differ by a uniformly bounded amount. The same holds for the other
mixed orientation, choosing its direct edge as origin.

We need the following complete tail, with constants independent of
the fiber length:

    sum_(|s|+|t|_1>L) F(s,t) <= C/(1+L),   L>=1.         (7)

For |t|_1>L/2, sum s first. The bounds in (6) and
sum_s b(s,t)<=C(1+|t|_1)^-2 give

    C sum_(q>L/2) (1+q)^2 (1+q)^-4 <= C/(1+L),

where C(1+q)^2 bounds each Z^3 shell. For |s|>L/2,
sum these s first instead; their b sum is at most
C(1+L+q)^-2. Including every transverse shell gives

    C sum_(q>=0) (1+q)^2 (1+q)^-2 (1+L+q)^-2
       <= C/(1+L).

The union of these two sets covers the tail. This proves (7),
and also sum F<=C. The layer-cake identity for nonnegative sums
now gives the truncated first moment

    sum_(|z|<=L) (1+|z|) F(z) <= C log(eL).             (8)

For example bound |z| by sum_(m=0)^(floor L) 1_(|z|>m),
up to a fixed constant, and apply (7) to every layer. Combining
(7) and (8) at L=N yields

    sum_z min{(1+|z|)/N,1} F(z) <= C log(eN)/N.         (9)

A direct/direct product b(p-e)b(q-f) at bounded separation is
also covered by a fixed multiple of this majorant, or by b^2
directly. No separate first absolute moment of an individual
Green kernel or an alternating projection kernel has been assumed.

### 3. Freeze the complete local coefficient with a finite error

At the physical plaquette anchor x, let J_x be exactly L217(3).
Retain each finite-range offset and component pair separately in
the comparison of j_N and J_x. L211's explicit formula and L222(4)
for the actual coefficients imply, after zero extension of j_N,

    |j_N(p,q)-J_x(p,q)|
       <= C min{(1+|p-e|)/N,1},   |p-q|<=r_*.          (10)

Here e is any traversal direct edge at bounded offset from the
anchor. To see the global scope, extend only the smooth compact
displacement and strain coefficients by zero outside D. Their
extensions are smooth and Lipschitz. Each coefficient of the two
ordered generator stencils is a fixed finite linear combination
of displacement values at its original shifts; replacing those
values by u(x) costs C a(1+|p-e|), capped by their uniform bounds.
The actual displacement samples differ from the smooth ones by
O(a^2). The normalized subtraction coefficients in j_N carry a
factor a and are uniformly bounded. These contributions obey (10)
as well. The zero extension of the matrix agrees with this local
formula because every nonzero stencil is interior for large N.
No field or forest potential has been extended across its upper pin.

Use (10) in the infinite-kernel version of (4) *before* any fiber
truncation or coefficient replacement in the covariances. Bounds
(6)--(9) give, for each mixed orientation with its actual finite
fiber, error at most C log(eN)/N. The direct/direct error is bounded
by the same allowance. This sum includes all p in Z^4: outside
the original support j_N is zero but J_x need not be, and the
tail in (9) pays for this difference. It is not a fixed-ball limit
evaluated at a growing radius.

It remains to extend the frozen finite fiber to L217's half-line.
The exact finite levels 0,...,j-1 become -j,...,-1 after translating
the anchor to zero. Both original mixed orientations therefore have
the same last included axial link -1; their order and minus signs
remain those in L217(14). Because J_x is linear in u(x), L211's
infinite convolution calculation, equivalently L217(13), gives

    |W_x(e,f_n)| <= C |u(x)| (1+n)^-2,
    sum_(n>j) |W_x(e,f_n)| <= C |u(x)|/(1+j).           (11)

If u(x) is nonzero, compact support implies j>=cN, for a fixed
c>0. If u(x)=0, the entire frozen kernel vanishes. Consequently
(11) is O(N^-1) uniformly over *all* plaquette anchors. The finite
zero columns at pinned endpoints cause no missing frozen contribution:
such endpoints occur only at anchors within a bounded number of
steps of a face, where u(x)=0 for sufficiently large N. One can
equivalently use the full formal fibers throughout (5)--(11), with
zero finite source columns as in section 1.

Combining (5), (9)--(11) with the exact three-term row identity
L217(14) proves the global entrywise estimate

    |a V_p^dm-mathcal D^(mu nu)(x_p)|
                           <= C log(eN)/N.           (12)

Colors simply repeat the diagonal blocks. Every fixed traversal row,
normal transverse end link, lower source and upper-adjacent cut has
been retained. There is no moving boundary collar in (12). The
limiting matrix mathcal D is precisely L217(6), not a newly selected
tensor. It is a fixed finite collection of linear functions of u(x),
with bounded coefficients by the complete absolutely convergent
kernel/fiber sum. In particular it is smooth, compactly supported
in D and has bounded first derivatives.

### 4. Match the actual exterior matrix on that compact support

We need an exterior rate only where mathcal D is nonzero. Elsewhere
the global bound |a^-2 U_(i,p)|<=C_i from L214(13) suffices in
(12). Choose a fixed compact interior containing supp u and its
bounded mesh enlargement. On that set we now establish

    |a^-2 U_(i,p)-mathcal U_i^(mu nu)(x_p)| <= C_i/N.    (13)

Use L216(13)--(14)'s exact modal expansion, whose exterior column
is v_(k,a)=a R_F A_(k,a), where A_(k,a)=f_k/sqrt(lambda_(k,a)).
L222(2)--(4) give, for r=|k|>=sqrt(3),

    ||A_(k,a)||_(C^m)+||A_k||_(C^m) <= C_m r^(m-1),
    ||A_(k,a)-A_k||_(C^m) <= C_m a^2 r^(m+1).

For a *raw* transverse edge of direction mu at level j, rather than
the endpoint-averaged diagnostic row, the exact normalized prefix is

    phi_(k,a)(j,y)=a sum_(ell=0)^(j-1)
                      A_(k,a,1)(-4+(ell+1/2)a,y),
    (v_(k,a)/a)_mu
       =A_(k,a,mu)(edge midpoint)
           -[phi_(k,a)(j,y+a e_mu)-phi_(k,a)(j,y)]/a.    (14)

The formula is just the original lower-prefix retraction; signs for
backward traversals are applied afterwards. L222(9) controls this
same phi and its transverse first derivatives uniformly in j<N.
Its transverse C^2 norm is <=C r, since its total summed length
is at most 8. Comparing the forward difference in (14) with its
derivative costs C a r by the integral difference formula. Combining
that with L222(9) and the normalization estimate above gives

    |(v_(k,a)/a)_mu-(mathfrak r A_k)_mu(x_p)| <= C a r^2,
    |v_(k,a)/a|+|mathfrak r A_k| <= C.                  (15)

All four traversal midpoints differ from x_p by O(a); their changes
are included using the C^1 bound of the continuum lift. This bound
is <=C(1+r), since a transverse derivative differentiates a length-8
integral of a first derivative, while an axial derivative of that
integral evaluates its integrand. The value bound in (15) is separate
from the error bound: the direct mode and the length-8 prefix of
bounded first derivatives are uniformly bounded even at high labels.
For the axial zero mode phi is exactly its linear lower-prefix
profile; it has not been discarded. No value at the pinned upper
transverse row is used in (14).

The modal probe coefficient in L216 is precisely the whitened
polarized form B_(i,a;kl) in L222(7). Thus that result gives

    |B_(i,a;kl)-beta_(i;kl)| <= C_i a(1+|k|+|l|)^2,
    |B_(i,a;kl)|+|beta_(i;kl)| <= C_i,

for the actual triplet average of four products and both polarized
shear placements, in the same normalization. L222(12) gives the
heat-weight difference C a^2(r^4+t^4)exp[-c(r^2+t^2)].
Telescope those weights, the probe coefficient and the two exterior
factors in L216's expansion, using their separate value bounds and
(15). The absolute summand error is bounded by

    C_i a(1+r+t)^4 exp[-c(r^2+t^2)].                  (16)

Its sum over every retained pair is O_i(a), by the complete product
of polynomially weighted Gaussian series. Missing continuum labels
are handled separately: at least one index is >=N, so their indicator
is at most (r+t)/N. The same complete Gaussian sum bounds their
contribution by C_i/N. This proves (13) with no mode cutoff or
limiting exchange. Termwise first derivative estimates, with the
same Gaussian majorant and one extra fixed polynomial, also prove
||mathcal U_i||_(C^1)<=C_i on the compact set. All traversal signs
and all three colors remain. We used L222's specific modal estimates,
not its diagnostic conclusion as a theorem for this different matrix.

The calculus source already imported in L222 is Taylor's theorem
with remainder, NIST DLMF v1.2.8, section 1.4(vi), (1.4.35)--(1.4.37),
<https://dlmf.nist.gov/1.4#vi>. Here it is applied only to the same
smooth trigonometric modes and compact coefficients. The specialization
to the raw forward difference in (14), instead of a diagnostic average,
is written explicitly; no source theorem is reproved.

### 5. Complete signed response and quadrature

Keep the original finite identity L217(17), with -24 applied once:

    a^3 T_i^dm=-24 a^4 sum_(p in P_T)
                         K:(a^-2 U_(i,p)):(a V_p^dm). (17)

First replace a V_p^dm by mathcal D(x_p) using (12). The global
exterior bound and a^4 #P_T<=C make the total error at most
C_i log(eN)/N. This step includes every original boundary row.
Next replace a^-2 U_(i,p) by mathcal U_i(x_p), only in its product
with mathcal D, using (13). The resulting error is O_i(N^-1).

The final integrand K:mathcal U_i:mathcal D is C^1 with compact
support in the physical interior and C^1 norm bounded by C_i.
For large N all grid cells meeting that support have exactly the
usual anchors in P_T for each of the three positive transverse
planes. On each cell the difference between its integral and a^4
times its anchor value is at most C_i a^5. Summing the O(a^-4)
cells gives O_i(a); zero cells near physical faces introduce no
correction. This is the same elementary rectangle estimate as
L222(5), now applied to this explicitly matched smooth integrand.
Its integral is exactly A_i^dm in L217(6).

These three comparisons prove (1). Since a^-3=(N/8)^3, (2)
follows with an N-independent constant. In particular
N^2 log(eN)<=N^(5/2) log(eN)^2 for N>=1, meeting the approved
threshold. No coefficient evaluation, L219 contraction, L220 cubic
cancellation, plateau rate or numerical arithmetic premise is needed.

### 6. Scope and verification

Reuse the prior assessment
`drafts/literature/2026-10-18-direct-mixed-action-quantitative-remainder.md`.
Its inspected scalar whole-space Green theorems do not by themselves
give this pinned response rate. The proof uses the already established
L200 relative heat representation and L211/L217 differentiated kernels;
no additional scalar asymptotic expansion or new literature claim is
required. L025 fixes the contraction, L214 supplies its global exterior
bound, L216 its exterior normalization, and L222 its quantitative modal
inputs. The new work is their joint finite comparison (3)--(17).

The checks here are analytic: the internal support in the image bound,
the two N^-1 fiber product errors, the complete cylindrical shell tail,
the finite normalized subtractions, both half-fibers ending at -1,
fixed tangential zero columns versus variable normal sources, the raw
four-edge exterior normalization, full omitted heat labels and a^4
response quadrature. No preview or finite-mesh test is used as evidence.
The raw-loop and upper-pin failures in ATTEMPTS/011--013 are preserved:
only smooth deterministic coefficients are extended, and the covariance
and all forest rows retain their original boundary conditions.
The stronger bound is for this selected block alone. The separate audit
below verifies its quantitative specialization, without an upstream audit.

### 7. Separate critical audit, 2026-10-18

**Verdict: accepted relative to L025, L200, L211, L214, L216, L217
and the specified supporting estimates of L222.** No load-bearing
failure was found in (3)--(17). This is an independent analytic check
of the new finite comparison, not a recursive certification of those
inputs, a stronger bound, or a new discovery beyond the sources checked.
The unchanged EXPLORE assessment is
`drafts/literature/2026-10-18-direct-mixed-rate-critical-audit.md`.

**Internal support and all sources.** L211(10)--(11) gives the exact
stored-coordinate factorization: J has one factor 1/a in its two
generator orders and bounded subtraction coefficients. Both ends of
every nonzero J entry lie in a fixed compact interior enlargement.
Thus j_N=aJ_N is uniformly bounded with bounded range and overlap;
no covariance or cell-volume normalization enters B_N=C Sigma.

For an internal coordinate p_r in [cN,(1-c)N] and a source coordinate
e_r in [0,N], both p_r+e_r and 2N-p_r-e_r are at least cN.
The bounded staggered offsets can be absorbed by reducing c. These
inequalities apply even if the source is at a boundary. Hence every
nearest nondirect image is separated in at least one coordinate;
no source-interior assumption is needed. L200's even own-direction
and odd transverse reflections retain the actual relative grids.
Further images are summed only after integration up to N^2: for
b>10 their contribution is N^-3 times the convergent Z^4 series
sum_z(1+|z|)^-b. For the remaining time interval, integration of
N^-5 exp(-ct/N^2) and (1+t)^(-5/2) separately gives O(N^-3).
The finite spectrum has at least three positive indices per component,
so this estimate retains, rather than suppresses, its allowed zero
own-direction index. This proves precisely the uniform domain in (3).

A fixed tangential source column is zero in the relative space. Its
infinite column has magnitude O(N^-3) at the compact internal rows,
so padding such columns with zeros obeys the same comparison. Variable
normal end links are actual sources and use the image argument, not
that padding convention. For each source the sum of its infinite
first-difference kernel over the compact internal set is O(N), since
the four-dimensional shells give sum_(r<=CN) r^3(1+r)^-3=O(N).
For j<=N fiber sources the two product-error terms in (5) are therefore
at most C N^-3(jN)=O(N^-1); the double error is
C N^-6 N^4 j=O(N^-1). With one direct source in each factor they
are O(N^-2). The bounded q-p offset and finite overlap do not add a
volume sum. This verifies both mixed placements in their original order.

**Joint moment and coefficient comparison.** The endpoint dipoles of
any traversal have bounded transverse distance from every direct edge
of the same plaquette. After summing an entire axial line, each mixed
absolute product is therefore bounded by a fixed multiple of F in (6).
For a transverse shell q, summing s gives an O((1+q)^-4) product,
with O((1+q)^2) points in the shell. Its q>L/2 tail is O(L^-1).
For |s|>L/2 at unrestricted q, the shell contribution is bounded
by C(1+L+q)^-2; its q sum is also O(L^-1). These two domains cover
|s|+|t|_1>L, proving (7) without restricting the relative sizes of
the axial and transverse offsets. Layer cake then gives
sum_(|z|<=N)(1+|z|)F(z)<=C log(eN), while the complement is
O(N^-1). Division of the truncated moment by N proves (9).
Bounded shifts change only C. The direct/direct product is bounded
by b^2 and, since H(t)>=b(s,t), is also covered by F.

For each fixed stencil offset, the normalized generator coefficient
differs from its frozen counterpart by at most
C min{a(1+|p-e|),1}. This follows from the compact smooth displacement,
its O(a^2) sampling error in L222(4), and the exact finite stencil
in L211(11). The other two coefficients of j_N have a factor a;
their uniformly bounded values fit the same estimate. Outside the
finite matrix support the zero-extended coefficients obey it as well:
only the smooth compact deterministic coefficients are extended, and
their local formula agrees with the zero matrix whenever the stencil
leaves the box. No covariance or forest field is extended. Since a=8/N,
this is (10), with a fixed change of C. Applying (9) before any
fiber truncation gives the claimed O(log(eN)/N) error, including
internal rows outside the original compact support of j_N.

**Both half-fibers and their boundary cases.** L214(5) and L217(14)
place each finite prefix at levels 0,...,j-1. Translation by the
plaquette's axial level gives -j,...,-1 for both orders; transposition
does not add level zero. Each endpoint in L216(4) retains its traversal
sign, and the two mixed terms each retain their minus sign. L217(13),
with the linear dependence of J_x on u(x), bounds the omitted levels
n>=j+1 by C|u(x)|/(1+j). If u(x) is nonzero then j>=cN; otherwise
the entire frozen matrix is zero. Thus no lower collar is lost.
Fixed tangential traversals or fixed transverse endpoints occur only
within bounded lattice distance of a face and also have u(x)=0 for
large N. The padded finite identities remain exact there. Normal end
rows use their actual unpadded covariance. This verifies the global
bound (12) at the upper-adjacent cuts and transverse end rows too.
No smooth interpolation across the upper pin is required.

**Raw exterior normalization and the full heat sum.** L216(13)--(14)
uses v_(k,a)=a R_F A_(k,a), with A_(k,a)=f_k/sqrt(lambda_(k,a));
its probe coefficient is q_(i,a)(A_(k,a),A_(l,a)), exactly the
whitened coefficient B_(i,a;kl) in L222(7). Dividing the raw forest
row by a yields the forward difference of the physical prefix in
(14), with no additional 1/a. On the compact set where D is nonzero,
the prefix is smooth in its transverse coordinates and has C^2 norm
at most Cr. Its forward-difference error is O(ar). L222(9) adds
O(ar+a^2r^2), and the direct-mode normalization and O(a) shifts of
the four traversal midpoints add O(a+a^2r). Together these are
O(ar^2) for r>=sqrt(3) and a<=1, as in (15).

The separate uniform value bound follows from the bounded first
derivatives of A_(k,a), the prefix length <=8 and the integral
formula for a forward difference. It is not inferred from the
high-mode error bound. The continuum lift has first derivatives
bounded by C(1+r): transverse differentiation uses at most two mode
derivatives in an integral of length <=8; axial differentiation of
that integral gives its endpoint integrand. The allowed axial zero
mode has the exact linear prefix and obeys these bounds as well.
Traversal signs are applied to all four rows after this comparison.

The two complete polarized probes in L222(7), their uniform value
bounds, and the heat-weight error in L222(12) give (16) by telescoping.
The polynomial degree four is sufficient: the exterior and probe
errors have degree at most two, and the heat error degree four with
a^2<=a. The eight-dimensional product of Gaussian series sums this
bound uniformly in N. For missing labels r+t>=N, the indicator bound
1<=(r+t)/N gives a separate O(N^-1) tail using the same uniform
value bounds. Differentiating the continuum exterior adds only a
fixed polynomial factor, proving its required C^1 bound. This is
the raw traversal matrix, not L222's diagnostic conclusion.

**Final signed trace and scope.** L025(6) supplies -24 for the
no-internal-action-pair contraction. L214(4) identifies its V as
R Sigma A Sigma R^T without a Gaussian-tilt factor 2. The two mixed
orders in L217(14) and all three diagonal color blocks are counted
once. In (17), a^4(a^-2)(a)=a^3 exactly. L214(13)'s global exterior
bound pays for replacing aV on every original plaquette, giving
O(log(eN)/N) after the a^4 volume sum. The exterior replacement is
then needed only on supp D and costs O(N^-1). The resulting product
is compactly supported and C^1, so its cell error O(a^5) sums to
O(a), with no face contribution. Its integral is L217(6)'s original
A_i^dm. Multiplication by a^-3=(N/8)^3 gives O(N^2 log(eN)),
which is within the proposed O(N^(5/2)log(eN)^2) threshold.

All these checks are analytic; no finite mesh or spectral preview
stands in for the complete sums. The DLMF calculus citation in
section 4 is reused in its stated smooth-function domain, without
an additional source theorem or a reproof. ATTEMPTS/011--013 concern
raw undifferentiated loops and upper-pin extensions, neither used here.
The two-prefix plateau, other component rates and interacting reflected
bound remain independent. This acceptance does not establish a full
quantitative remainder, continuum axioms or finite positive mass.
The Mathlib qualifications below remain unchanged.

## Mathlib

Full matching direct/mixed response rate: not checked. Supporting
relative discrete heat kernels, lattice shell estimates, Taylor bounds,
Gaussian-series summability and quadrature: not checked. Unknown coverage
is not absence. The new joint kernel/fiber estimates and applicability
details are proved above; no matching Mathlib declaration is asserted.
