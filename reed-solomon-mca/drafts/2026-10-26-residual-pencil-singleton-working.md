# Step 503 — residual singleton equations (work in progress)

Ready target: the unchanged four-row finiteness question in
`drafts/literature/2026-10-25-four-row-finiteness-review.md` (EXPLORE).
Main gap: uniform twelve-row exclusion. A finite four-row locus could
support later-row tests; second-pair extraction and coding gates remain
independent. Test: exclude every residual dimension-two K_t, or construct
an eligible original quadruple with a complete exact-rank infinite family.
Do not replace this test by another membership count or rank census.

L161 reduces the defect to one S-overlap, named I_a intersect I_c,
and three constant-product polynomial pencils h=8,12,22. Write
d_j(X)=X^2-s_j X+h and Z(r)=r+h/r. The four s_j are distinct.
After dividing the original coordinate by P(r)/r, each kernel is
E^{I_j}+E(1/(Z(r)-s_j))_r. All denominators are nonzero since
S and J are disjoint. Write the coefficients of x,y,x+y,x+t*y
as alpha,beta,gamma=u alpha+v beta, delta=w alpha+z beta.
L161's coefficient injection makes alpha,beta independent on a
putative dimension-two K_t; t!=0,1.

Let B=Z(I_b), D=Z(I_d), A=Z(the singleton of I_a),
C=Z(the singleton of I_c). The first two are well-defined constant
values on those two root pairs, and B!=D. Singleton equations imply

    u=(D-s_c)/(D-s_a), v=(D-s_c)/(D-s_b),
    z/t=v*(B-s_d)/(B-s_c)=(C-s_d)/(C-s_b),
    w=(C-s_d)/(C-s_a)=u*(A-s_d)/(A-s_c).

These are necessary equations independent of t. If A=C then the
last identity forces u=(A-s_c)/(A-s_a), hence A=D by distinctness
of s_a,s_c, impossible for different fibers. Thus the common
coordinate cannot be the leftover singleton of S: the remaining
two singleton coordinates must occupy distinct Z-fibers, the unused
paired fiber and the leftover fiber. The equations above still need
a complete exact compatibility test and justification. No conclusion
about realization or universal finiteness is yet recorded.

Completion: the exact necessary scalar test retained 24 of 864
assignments, so the attempted universal exclusion failed. Select its
first h=8 survivor: B=9,D=40,A=45,C=74 and
(s_a,s_b,s_c,s_d)=(52,88,23,57). Choose overlap coordinate 12,
I_a={12,33}, I_b={1,8}, I_c={12,27}, I_d={18,22} in this
temporary naming. Solving the remaining singleton equation supplies
a cross-ratio; reorder the first designated pair to the original
lexicographic ordering, inverting that parameter to 26.

The independent actual-map construction and complete proof are now
canonical in L162. Its proof needs neither this residual derivation nor
L161's completeness: explicit vectors, exact original-map identities
and two nonzero pair minors suffice. There are no excluded projective
parameters, and injectivity gives an infinite family over E. All
load-bearing certificate values were inspected. The universal four-row
finiteness route is contradicted, with a separate critical audit still
required. Preserve the necessary scalar tests and their failed exclusion
threshold as discovery evidence; do not present them as the family proof.
