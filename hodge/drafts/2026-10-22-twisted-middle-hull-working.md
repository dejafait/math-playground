# Twisted middle stalk — step 465 working record

Approved target: determine the ordinary middle stalk and its canonical
reflexive-hull map at a selected actual split fibre for
Rp_2*(F tensor p_1^*L^{-1}). Reuse the pre-invocation SPECIALIZE
assessment `literature/2026-10-22-twisted-split-middle-hull-defect.md`.

Main gap: universal primitive Hodge realization; F existence is independent.
The local input could supply defect bookkeeping, without effectivity or
global positivity. Continue if the actual differentials force a unit
in the kernel description; otherwise identify the missing coefficient.

Read L145 fully, L134's actual weight-rank argument, L095's actual
curvature/form and determinant-fixed passages, L071's hypotheses and
ATTEMPTS/060. Existing uncommitted audit/source work is preserved.
L111 is comparison only, not a twisted scalar self-duality input.

Candidate computation, not yet certified: the actual minimal complex is
R -> R^26 -> R, with last-row ideal m by L145. The incoming boundary
on the central section (1,0) is q(u), the negative-weight KS block.
After row reduction to (x,y,0,...), the kernel is free on
(-y,x,0,...) and the remaining 24 coordinate vectors. Write the incoming
column as h*(-y,x,0,...)+(0,0,b_3,...,b_26). Rank-two incoming variation
alone does not make h a unit. The needed further check is nonvanishing
of the alternating coefficient pairing B(u,v)=T(p(u) wedge q(v)).
The exact chain relation makes its symmetric part zero. The actual
ordered trace form on KS is B(u,v)-B(v,u), which should be nonzero by
L095's quaternionic positive-scale identity. Check its actual Dolbeault
normalization before concluding h is a unit. Retain all higher terms.

No global IT, nonempty split locus, scalar self-pairing of the twisted
coefficient, metric extension or universal resolution is claimed.

Completion: the canonical proof is L146. Use the incoming coefficients
instead of first normalizing the row: write v=x a+y b, whose residues
are the independent q_1,q_2. The exact relation gives rho(a)=y t,
rho(b)=-x t. With T=(2pi i)^(-2) integral sigma wedge -, the mixed
Serre matrix B has B_11=B_22=0 and B_21=-B_12. The actual curvature
identity gives B_12-B_21=2lambda sigma_B(u_1,u_2), so t mod m=B_21
is nonzero. This retains the full t and both full incoming vectors.
The full complementary row can then be killed inside their direct
summand, leaving a free rank-24 middle complement. The canonical
hull map is an isomorphism, with zero defect. This completion needs
separate critical audit; it does not rely on a twisted self-pairing.
