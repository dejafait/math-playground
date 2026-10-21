# Boundary arithmetic attempt — saved reasoning

Approved target: determine the rational boundary fibers of L107's quotient
above s=0,1,infinity and their normalized minus-three lifting classes.
Prior SPECIALIZE assessment: drafts/literature/2026-10-20-quotient-rational-boundary-fibers.md.

Main gap: neither L095 integer system nor remaining global-factor
compatibility is solved. Boundary arithmetic could identify base points
for a later rational-point method. Essential inputs are audited L106,
L107, their fixed rational model and complete geometric branch counts.
L097 identifies phi(T)-1=-T^3 h(T), where h is the audited irreducible
octic. No external source refresh or new mechanism is proposed.

Provisional complete-local calculation, to be justified before claiming:
at s=1, three roots tend to zero, with ratios 1,zeta_3,zeta_3^2.
Their unique all-three branch has quotient parameter r, and
z/r^2 -> -(zeta_3-zeta_3^2)^2/12=1/4. Other rational points would
need rational r; irreducibility of h rules out simple r. A pair of
simple h-roots cannot be Galois-stable because h has degree eight;
a mixed pair with one zero-limit root would require a rational h-root.
Thus the all-three branch appears to be the only rational point at one.

At infinity normalize the root labels by r. Ratios tend to distinct
11th roots of unity. The 45 inertia branches correspond to unordered
pairs of distinct nonidentity roots. Cyclotomic multiplication has one
orbit of size five (inverse pairs) and four of size ten. This should give
residue fields Q(zeta_11)^+ and four copies of Q(zeta_11), and no rational
point; exact local-normalization justification is still required.

At zero rationality forces r to tend to gamma=1/5. The only potentially
rational unordered pair has one root in each q=3T^2+T+1 cluster.
Its five inertia branches require arithmetic slope descent over
Q(sqrt(-11)), not just cluster residues. Leading coefficients satisfy
(c_beta/c_alpha)^5=-(1-5alpha)/(1-5beta). No rational point or absence
is yet claimed. Remaining branch residue fields are also uncomputed.

Continuation/abandonment test: account for all 99 branches of index five,
168 of index one and 109 of index three, and 45 of index eleven;
weighted degree must be 495 at each fiber. No completeness claim if a
residue field, descent action or rational normalized leading term is
unproved. Only rational normalized points receive L107's lifting test.


Further saved arithmetic: at zero put d^2=-11,
alpha=(-1+d)/6, beta=(-1-d)/6. With r=1/5+O(s),
the leading residue h of the ratio (b-beta)/(a-alpha) satisfies h^5=C, where
C=-(11-5d)/(11+5d). At the split three-adic place d=1 mod 3,
v(C)=2, so X^5-C is irreducible over E=Q(d), also over E(zeta_5).
Conjugation sends h to h^{-1}. Thus the five mixed-cluster branches
with rational limiting r form a degree-five residue point, not five
rational points. The other possible r=1/5 branches use a same-cluster
pair and have nonrational cluster residue. This proves no rational
point over zero once the complete-local ratio argument is justified.

At one the complete normalized support can be expressed without any
Galois-group claim for h: write A=Q[T]/h, A^[2] for its ordered
unequal-pair algebra, B for its unordered unequal-pair algebra and
D for its distinguished-root/unordered-other-two algebra. The e=1
part is D (dimension 168); the e=3 part is
A^[2] x A x B x (A tensor Q(sqrt(-3))) x Q,
of dimensions 56,8,28,16,1. This has 109 geometric points. These are
exact finite-etale algebras, but their decomposition into individual
number fields has not been computed. Irreducibility of h excludes
rational points in every factor except Q; in B a rational point would
supply a rational quadratic factor of h, impossible. Thus no assumption
about the full octic Galois group is needed for rational-point selection.
The stronger requested explicit residue-field decomposition remains
incomplete if these algebra presentations are not split. Do not infer
that any multiple-root affine image is a single normalized point.


Completed step: canonical L108 now contains the rigorous rational boundary
selection, the exact quotient local parameter and lifting unit, all infinity
residue fields, and the complete support-algebra presentation at one.
The provisional degree-five field description above was not needed for the
rational exclusion and is not promoted to a canonical proved field
classification here. It remains unfinished descent reasoning. The complete
nonrational zero-field decomposition and splitting of the support algebras
at one are not claimed. The certificate passes 775 checks; the proof, rather
than this draft or a certificate preview, supplies the rational result.
The sole active continuation is recorded in PROGRESS.md, with a separate
REVIEW_REQUIRED critical-audit assessment. No complete Beal candidate exists.
