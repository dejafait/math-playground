# Lemma 884: matched conjugate contact cells have strict checkerboard periods

## Hypotheses

Use L847's actual entire function and full form, without replacing G:

\[
 G(z)=\tfrac18\xi(\tfrac12+\tfrac{\sqrt z}{2})
     =\sum_{n\geq0}a_nz^n,\qquad a_n>0,\qquad
 R>0,\quad RG'(R)/G(R)=1,\quad C=R^2/G(R)^2>0,
\]
\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \quad \omega=F\frac{dz_1}{iz_1}\wedge\frac{dz_2}{iz_2}.
                                                               \tag{1}
\]

Let u:T^2 -> R^2 be smooth, real and 2pi-periodic. Put
z_j(y)=R exp(u_j(y)+iy_j), J=det(I-iDu) and Q=F(z_1,z_2)J,
with the original orientation dy1 wedge dy2. Assume J is nowhere
zero and L879's stationarity: the first variation of
B(u)=(2pi)^(-2) integral |Q| vanishes for every smooth real radial
variation supported compactly in {Q!=0}. Retain its actual phase
Q=lambda*s, |lambda|=1, with s real smooth.

Assume exactly L882's boundary odd-contact hypotheses and restrict
to its matched conjugate branch

\[
                 \eta=\theta=\overline\zeta\ne\zeta.
                                                               \tag{2}
\]

Thus zeta and its conjugate are simple actual G zeros. Choose a real
lift a=arg(zeta), and the unique b in (a,a+2pi) lifting
arg(conjugate(zeta)). L882 gives the four full fibers

\[
 z_1(a,t)=z_2(t,a)=\zeta,\qquad
 z_1(b,t)=z_2(t,b)=\overline\zeta \quad\hbox{for all }t.   \tag{3}
\]

Also retain L882's exact census: any single off-diagonal odd-contact
seed in either coordinate has label zeta or conjugate(zeta).
No classification of isolated simultaneous contacts is assumed.
Other zeros, arbitrary multiplicities, auxiliary angular subdivisions,
and every simultaneous or diagonal vertex remain in the graph.

Set E1=[a,b], E2=[b,a+2pi] and D_pq=interior(Ep x Eq).
Let I_pq be the unnormalized integral of Q over Ep x Eq. Use the
fixed lifts and L883's definitions

\[
 \begin{split}
 H_j(z)&=\sum_{n\geq0,\ n\ne j}\frac{a_nz^{n-j}}{n-j},\quad j=0,1,2,\\
 r&=(a_0,a_1,a_2),\quad T=2\pi i r,\\
 S(x,y)&=x_0y_2-2x_1y_1+x_2y_0,\\
 A&=H(\overline\zeta)-H(\zeta)+i(b-a)r.
 \end{split}                                                   \tag{4}
\]

Here A is purely imaginary by real coefficients. No product graph,
exchange symmetry, analytic u, prescribed collar, nonzero d, or
existence of an off-real zero or a stationary graph is asserted.

## Conclusion

There is epsilon in {1,-1} such that, on each whole closed cell,

\[
        \epsilon(-1)^{p+q}\overline\lambda Q\geq0,
                                                               \tag{5}
\]

with strict inequality wherever Q is nonzero. Every D_pq contains
nonzero points. Consequently all four integrals are nonzero, and

\[
        \epsilon(-1)^{p+q}\overline\lambda I_{pq}>0.
                                                               \tag{6}
\]

L883 makes all I_pq real under (2). Their strict nonvanishing now
forces the actual lambda to belong to {1,-1}, including when
d=a1^2-a0*a2=0. This inference uses (6), not the total period.

Put v=-iA, w=-i(T-A), and t=v+w=2pi*r, all real, and define

\[
       \alpha=S(v,v),\qquad \beta=S(v,w),\qquad
       \gamma=S(w,w).
\]

Then the necessary actual-label sign test is exactly

\[
 (I_{pq})=-C\begin{pmatrix}\alpha&\beta\\\beta&\gamma\end{pmatrix},
 \qquad \alpha\beta<0,\qquad\gamma\beta<0.               \tag{7}
\]

The two strict inequalities are equivalent to a nonzero checkerboard
for this real matrix up to a common sign. This equivalence concerns
the four numbers only; it is not sufficient for a stationary graph.
The stationary mass, if this graph exists, is determined by its labels:

\[
 \begin{split}
 \mathcal B(u)&=\frac{C}{4\pi^2}
                  (|\alpha|+2|\beta|+|\gamma|),\\
 M&=2Cd,\qquad
 \mathcal B(u)-|M|
     =\frac{C}{2\pi^2}
             \min\{|\alpha|+|\gamma|,\,2|\beta|\}>0.
 \end{split}                                                   \tag{8}
\]

These are local necessary sign and mass conclusions relative to
the checked L879/L882/L883 results. The independent conceptual audit
of 7 November 2026 below accepts them under the unchanged hypotheses.
The prior EXPLORE search did not identify the signed assembly;
POTENTIALLY_NEW did not certify originality. The audit is a REPRODUCTION.

The signs are not consequences of conjugate reality and the total
period alone: the algebraic controls below both fail and satisfy
(7) with the same actual coefficient vector r. Those controls are
not zero labels or graph constructions. It remains unproved whether
the actual vector v in (4), at any conditional actual conjugate zero
pair allowed by L882, satisfies or violates (7). Thus no actual-label
exclusion, off-line zero, stationary graph, sharp L868 bound or Xi
positivity claim follows. Other branches and global gaps remain open.

## Proof

### Covered inputs and why a signed assembly is needed

The invocation-start assessment
`drafts/literature/2026-11-07-signed-contact-cell-conjugate-test.md`
has decision EXPLORE for exactly this bounded attempt. Its completed
source and duplicate comparison is reused without new browsing.
L847 supplies the full oriented form, L879 supplies the finite
angular arrangement and its edge parity comparisons, L882 supplies
the exact odd-seed census, and L883 supplies the fixed-lift periods.
No source reproof, new zero estimate or extension to another branch
is made here.

The finite ambient-zero input used in L879 is Jiří Lebl, *Guide to
Cultivating Complex Analysis*, v1.10 (5 November 2026),
[Theorem 2.4.7 and its proof, pp49-50](https://www.jirka.org/ca/ca.pdf#page=49).
It applies because G is entire, G(0)>0, and the graph's coordinate
radii lie in compact annuli. It does not assert finiteness of the
smooth pullback contact sets. The constant-phase stationarity source,
Lawrence-Yamauchi, *Convex optimization and contour deformations*,
[arXiv:2311.13002v2, Section II B (9)-(16), pp3-4](https://arxiv.org/html/2311.13002v2#S2.SS2),
allows different phases across zeros. The required signed conclusion
therefore uses L879's specialized parity proof and L882's census,
not stationarity alone. The already audited Stokes and Laurent
applications in L883 are imported as its exact formula (5); no
boundary comparison or primitive is rederived in this step.

### Connectivity and parity inside each open cell

Use the whole finite angular arrangement from L879: all vertical and
horizontal circles at arguments of possible ambient G zeros in the
coordinate annuli, its auxiliary cut circles, and the angular
diagonal y1=y2 modulo 2pi. Denote their union by Sigma. Every zero
of Q lies in Sigma because J never vanishes. The angles a and b in
both coordinates are already among these lines by (3).

In the lifted open rectangle D_pq, Sigma consists of finitely many
vertical, horizontal and diagonal line segments, with finitely many
intersection vertices. Its complement is nonempty and dense and has
finitely many open polygonal faces. Q is nonzero on each face and
has constant phase there by L879. The adjacency of these faces
*within D_pq* is connected. Indeed join two interior face points
by a polygonal path inside the open rectangle. Its image is compact
inside that rectangle. A sufficiently small perturbation avoids
the finitely many vertices, crosses each encountered segment
transversely and avoids following an edge. It yields a finite chain
of faces without crossing a boundary of D_pq. This argument needs
neither connectedness of {Q!=0} nor isolated pullback contacts.

Consider an interior open edge in this arrangement. If it contains
a point where Q!=0, continuity identifies the phases on its two
adjacent faces, including when the remaining edge has a nonisolated
contact subset. Otherwise an open vertical edge is a whole contact
with one fixed G-zero label: the second G factor and the diagonal
factor are nonzero there, and connectedness fixes the first label.
L879 (11)-(12) says that the phases differ by (-1)^m, where m is
the actual multiplicity of that label. If m were odd, any point of
this edge would be a single off-diagonal odd seed. L882's census
would force its first-coordinate angle to be a or b modulo 2pi.
Neither distinguished angle lies in the open coordinate interval
of D_pq. This is impossible, so m is even and the phases agree.
The horizontal argument uses the same census in the other coordinate.

An interior open diagonal edge has no G contact except possibly at
its excluded vertices. L879 (13) shows that its squared factor
never flips adjacent phases, whether the edge consists entirely
of contacts or has noncontact points. These cases exhaust interior
open edges. Connected face adjacency therefore gives a single phase
on all faces within D_pq.

Since s=conjugate(lambda)Q is real and continuous, its common sign
on those faces extends weakly across their edges and all vertices.
Any nonzero value has that sign strictly. No vertex is deleted or
classified: it is recovered by density and continuity. In particular
an isolated simultaneous odd contact introduces no extra relative
sign between these already connected faces. On the external sides
of the closed cell, (3) gives Q=0, including every corner. Thus the
same weak sign extends to the entire closed cell.

### Neighboring cells and strict integrals

Choose a point on the common vertical boundary y1=b of D_1q and
D_2q, with y2 in the open interval Eq and away from the finitely
many arrangement vertices. Such points exist. There z1 is the
simple zero conjugate(zeta), G(z2)!=0, and z1!=z2. L879's
single-G parity comparison changes phase by -1. Hence these two
cell signs are opposite. The same argument on y2=b gives opposite
signs for D_p1 and D_p2. Choosing epsilon to be the sign of s on
D_11 proves the checkerboard (5). The seam fibers yj=a modulo
2pi have the same simple-contact comparison; the resulting pattern
agrees across that seam as well.

Each open cell contains an open face and therefore a point with
Q!=0. Continuity supplies an open neighborhood with a strictly
nonzero value of the appropriate sign. All other values on that
closed cell have the weak same sign. Its signed integral is thus
strictly positive, proving (6). This argument retains all contact
sets and uses no cancellation or approximation. In particular

\[
             \int_{E_p\times E_q}|Q|=|I_{pq}|.            \tag{9}
\]

### Conjugate periods, actual phase and mass

L883 (4)-(5), with b=c and B=A in its notation, gives
I11=C S(A,A), I12=I21=C S(A,T-A), and
I22=C S(T-A,T-A). Real coefficients give A=i*v and T-A=i*w
with real v,w, including the full fixed angular increments. Complex
bilinearity of S yields the matrix in (7). In particular I11 is
real. By (6) it is nonzero and lies on the actual line lambda*R,
so lambda is either 1 or -1. This proves the asserted d=0 case
without selecting a line from a zero total period.

The checkerboard now says that the diagonal entries have the same
strict sign and that either off-diagonal entry has the opposite
strict sign. Since C>0, this is equivalent to alpha*beta<0 and
gamma*beta<0. Conversely these two inequalities make the displayed
real matrix a strict checkerboard up to a common sign; they do not
imply any pointwise assertion or existence of u.

Sum (9) over the four cells and normalize by (2pi)^2 to get the
first equality in (8). Cell boundaries overlap only on sets of
area zero and have Q=0. Also

\[
 \alpha+2\beta+\gamma=S(t,t)
       =(2\pi)^2(2a_0a_2-2a_1^2)=-8\pi^2d.             \tag{10}
\]

L883's total-period identity gives M=2Cd. By (7), alpha and gamma
have one common sign and beta the opposite sign. Therefore the
absolute value of their sum in (10) is
abs((|alpha|+|gamma|)-2|beta|). The elementary identity
X+Y-|X-Y|=2 min(X,Y) for X,Y>0 proves the remaining formula in (8),
including its strictness and d=0. It quantifies L879's existing
qualitative gap on this branch; it does not reach a sharp graph bound.

### Exact algebraic controls and the remaining actual-label question

The following controls keep the actual r and t fixed but temporarily
allow v to be a free real vector with w=t-v. They test implications
of the period algebra only. They are not claimed to have the
primitive representation (4).

First set v=w=t/2. Writing q=S(t,t), this gives
alpha=beta=gamma=q/4. The entries are real and their sum has exactly
the required total, but (7) fails, including q=0 where all entries
vanish. Thus conjugate reality and (10) alone do not imply the
new strict test.

Conversely put e=(0,1,0), v=t/2+k*e, w=t/2-k*e, where k>0.
Since S(e,e)=-2 and S(t,e)=-2t1, exact expansion gives

\[
 \alpha=q/4-2kt_1-2k^2,\quad
 \beta=q/4+2k^2,\quad
 \gamma=q/4+2kt_1-2k^2.                                  \tag{11}
\]

Choose k so large that 2k^2>|q|/4+2k|t1|; such k exists because
the left side is quadratic and the right side is at most linear.
Then alpha<0, gamma<0 and beta>0, so (7) holds while (10) is
unchanged. This construction works for the fixed actual coefficients
for every sign of d and for d=0. Consequently the new sign pattern
does not contradict the total-period algebra by itself.

Neither free-vector control establishes selectivity or compatibility
on the actual G-zero label set. The next mathematical issue after
independent validation of this lemma is the constrained vector
v=-i[H(conjugate(zeta))-H(zeta)+i(b-a)r], not freely chosen vectors.
No estimate deciding its two products in (7) has been proved here.
The bounded sign-assembly attempt ends with this necessary test and
mass formula; repeating only reality, counts or free-vector algebra
cannot exclude the matched conjugate branch. This is a local limit,
not a global ban on actual-label or relative-period methods.

### Independent conceptual audit, 7 November 2026

STEP_ID: 2026-11-07-l884-conceptual-audit-63. This audit uses the
unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-07-l884-signed-cell-conceptual-audit.md`.
The full proof above was checked against L847's oriented form,
L879's finite arrangement and edge comparisons, L882's exact seed
census, and L883's audited fixed-lift periods. The already inspected
primary coverage is reused through these local results. In particular,
the Laurent primitive source's exercise qualification recorded in
L883 remains; no new theorem or actual-label estimate is imported.

**Faces, contacts and vertices.** Since the two labels are distinct
conjugates, their arguments differ modulo 2pi. Hence both E1 and E2
have positive length. Restricting the lifted finite angular arrangement
to each open rectangle gives finitely many straight segments, including
every relevant translate of the diagonal, and finitely many vertices.
Its complement is dense, nonempty and consists of connected polygonal
faces. A generic polygonal path between any two face points stays
inside this open rectangle and avoids all vertices. Its finite set of
transverse crossings proves face adjacency there without leaving the
cell or assuming connectedness of the actual nonzero locus.

At a vertical open edge, every horizontal G-angle and diagonal
intersection is excluded as a vertex. Thus G(z2) and z1-z2 are nonzero.
If some point of the edge has Q!=0, both adjacent constant normalized
phases approach its unique normalized value; they agree, regardless
of the remaining contact subset. If the entire edge is zero, its
connected image z1 lies in the finite ambient zero set and has a
single label. The transverse coefficient in L879 (11) is nonzero:
the other G factor, diagonal, J and zeta are nonzero, and
partial_1 u1+i cannot vanish for real u1. Thus the exact adjacent
phase ratio is (-1)^m. Odd m would give a single off-diagonal seed
at an angle strictly inside one of the intervals, contrary to L882's
census a,b. Hence m is even. The horizontal case has the same proof
with coordinates exchanged and without an orientation change.

On an open diagonal edge both G factors are nonzero. A noncontact
point again identifies phases, while a wholly contacting edge has
the nonzero quadratic transverse coefficient in L879 (13) and no
sign reversal. These alternatives exhaust the open edges. Therefore
all faces of one cell have the same normalized phase. The real smooth
function s=conjugate(lambda)Q has that weak sign on their closure;
at a nonzero point the sign is strict. This includes every interior
vertex, irrespective of simultaneous multiplicities or tangency.
Every external side has Q=0 by its fixed G-zero coordinate. No vertex
or possibly nonisolated single-contact subset is discarded.

**Boundary flips and strictness.** On y1=b choose y2 in the relevant
open Eq outside the finitely many horizontal angles and vertices.
This is possible because Eq has positive length. There z1 is the
simple label conjugate(zeta), G(z2)!=0, and the angles ensure z1!=z2.
The same nonzero coefficient with m=1 gives opposite phases in the
two incident cells. The analogous choice on y2=b gives the second
flip. The fibers at a modulo 2pi give the same comparison across the
periodic seam; angular translation preserves dy1 wedge dy2. Thus the
four signs are exactly (5), with epsilon determined by D11.

Each cell contains a face point with s!=0, and a small neighborhood
where its signed value is bounded below by a positive constant.
Combined with the weak sign everywhere else and continuity on the
compact rectangle, this proves the strict integral (6) and equality
(9). It does not merely assert that the integrand is nonzero on a
set of unspecified measure. Additional contacts cannot cancel these
signed integrals.

**Actual phase, real bilinear signs and mass.** L883 applies with
b=c and B=A. Its convergent real-coefficient primitives satisfy
H(conjugate(zeta))=conjugate(H(zeta)); the modulus logarithm is zero
and the retained angular increment is imaginary. Consequently A=i*v
and T-A=i*w with real v,w. S is complex bilinear, so each pair of
factors i contributes -1 and the matrix is exactly -C times the
matrix in (7). No additional orientation sign occurs. Since I11 is
both real and strictly nonzero and conjugate(lambda)I11 is real,
Im(lambda)=0; unit modulus gives lambda in {1,-1}. This uses no
division by d and no inference from a zero total period.

The checkerboard implies I11*I12<0 and I22*I12<0. Substitution of
the matrix gives C^2*alpha*beta<0 and C^2*gamma*beta<0, equivalent
to (7) because C>0. Conversely these products force all three real
numbers to be nonzero, the two diagonal signs equal and the middle
sign opposite. That converse concerns only the displayed numbers.

With t=2pi*r, S(t,t)=8pi^2(a0*a2-a1^2)=-8pi^2*d. Hence the
sum of the cell integrals is 8pi^2*C*d and its normalized value is
2C*d=M, agreeing with L883. Set X=|alpha|+|gamma| and Y=2|beta|.
Both are strictly positive, and (7) gives |S(t,t)|=|X-Y|. The cell
integrals of |Q| equal their absolute periods, so

\[
 \mathcal B=\frac{C}{4\pi^2}(X+Y),\qquad
 |M|=\frac{C}{4\pi^2}|X-Y|,
 \qquad \mathcal B-|M|=\frac{C}{2\pi^2}\min(X,Y)>0.
\]

This checks every factor in (8), also when d=0 and X=Y. The cell
boundaries have zero area and Q=0, so summing does not introduce an
overlap term. There is no uniform positive lower bound over labels
in this identity and no compactness or attainment conclusion.

**Formal controls and scope.** For v=w=t/2, bilinearity gives all
three numbers q/4; their products are nonnegative, including the
zero case, and strict (7) fails. For v=t/2+k*e and w=t/2-k*e,
S(e,e)=-2 and S(t,e)=-2t1 give precisely (11). The stated bound on
k makes the larger diagonal value at most
|q|/4+2k|t1|-2k^2<0 and makes beta>=-|q|/4+2k^2>0. It is possible
for every fixed finite t. Both controls preserve v+w=t and the total
period, but neither is required to equal the actual primitive vector
(4). Thus they establish neither actual-label feasibility nor an
actual counterexample to a label inequality.

No mathematical error was found in (5)-(11). This establishes the
checked conditional input, without a new result beyond L884 or a
certified novelty claim. Actual-label selectivity, the other branches,
graph existence, compactness, the sharp bound, higher signs and Xi
transfer remain open. The direct uses of L847, L879, L882 and L883
are exactly those already recorded in the DAG; no edge changes.

## Mathlib

Full matching coverage for the cell-sign assembly and label-mass
formula has not been checked. Supporting formal coverage for the
finite arrangement, edge comparison and L883 primitives is also
unchecked in this step. No Mathlib theorem is imported, and unknown
coverage is not evidence of absence. The accepted independent audit
is informal and does not change this unchecked formal coverage or
any stated hypothesis or remaining limitation.
