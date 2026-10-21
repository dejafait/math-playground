# Ordinary nonspin normalized tensor — source comparison

TARGET: Assess strict exact-h stability and acyclicity of K=E tensor B tensor O_S(-k) for the L080 and audited L088 ordinary factors as a candidate L079 rank-four block.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped L080/L088 hypotheses, L087 normalization and witness, L079 block requirement, ATTEMPTS/056 and histories 207/208/211/212/214; searched tensor Hermite–Einstein irreducibility, joint holonomy/Goursat and exact-real-Kähler slope-Hom results; primary passages and access limitations below.
SOURCE_EVIDENCE: Perego 1910.01867v1 Propositions 3.10,3.15 with full proofs, Theorem 4.19 with both slope cases and extension across the singular set, Proposition 4.15 and Corollary 4.16; Huybrechts Chapter 9 Section 4.2 and Chapter 1 (2.6); Nomizu (1955) Section I.1 and Proposition 2 with reduction proof; Bauer–Sen–Zvengrowski 1109.0024v3 Theorem 2.1 with forward/converse proof; Balaji–Kollár (2008) Propositions 4,7 and Section 8 inspected for comparison only.
COMPARISON: Known connection, holonomy and cohomology tools cover a bounded specialization; tensor Hermite–Einstein implies polystability, while strict stability needs a separate joint-holonomy argument. No inspected theorem states this exact normalized-tensor conclusion.
GAP: At unchanged h, verify determinant cancellation and the symmetric form; test factor and joint projective holonomy including proper projections and linked-factor cases; evaluate full Chern character and actual cohomology against L079. None of these specializations is proved in this review.
REASON: Essential source coverage is sufficient for one separate mathematical attempt using ready factors and standard analytic/group/cohomology inputs; no reproof of K3 existence or general Kobayashi–Hitchin is justified.
SCOPE: L052's S,h,k; an L080 locally free h-stable E of rank two, determinant k and c_2=-2 eta; an L088 locally free h-stable B of rank two, determinant k and c_2=-eta; the ordinary tensor E tensor B tensor O_S(-k). No actual image, common F or transport is assumed.

## Gap, target, use and decision test

The main gap remains algebraic realization of all primitive rational
(2,2)-classes, already unresolved on arbitrary fourfolds. Locally the
common kernel F with its full negative mixed tensor remains
unconstructed. The intermediate target is an actual individual L079
K_4 block: rank four, determinant trivial, c_2=8 eta, strictly h-stable,
with a perfect symmetric form and cohomology (0,0,0). It could supply
one candidate block before actual image and common-kernel construction.
Those constructions and transverse transport remain independent gaps.

Continue for one mathematical attempt after separate approval of this
changed assessment. Its discriminating test is the actual normalized
tensor's irreducibility and cohomology at h. A forced summand, nonzero
cohomology, or wrong Chern datum stops this recipe. If an additional
choice of B is needed, state and justify it; individual stability
does not establish joint independence. Success supplies only an
individual block, not either actual L079 image or their common F.

## Inspected inputs and precise qualifications

**Connection and slope inputs.** Reuse L087's assessed ordinary
operations. Perego, *Kobayashi–Hitchin corrispondence for twisted
vector bundles*, [1910.01867v1, 4 October 2019](https://arxiv.org/pdf/1910.01867v1),
Proposition 3.10, printed p. 47, adds tensor Einstein functions;
Proposition 3.15, pp. 49–50, gives parallel morphisms and parallel
kernel/image splittings when the target function is no larger. Both
complete proofs were read. Theorem 4.19, pp. 63–65, treats arbitrary
saturated subsheaves, the equality case, and extension of the splitting
across the codimension-two exceptional set before induction. Thus
irreducibility is essential for strict stability. Proposition 4.15 and
Corollary 4.16, pp. 61–62, give slope-Hom constraints with rank/degree
hypotheses retained. Use twist one and zero B-field, at the chosen
Kähler metric; integrality of the polarization is not required.
None asserts that tensors of stable bundles are stable.

**HE existence, RR and duality.** Huybrechts, *Lectures on K3 Surfaces*,
[author-hosted draft](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf),
Chapter 9 Section 4.2, Remark 4.8(i) and Theorem 4.9, printed
pp. 181–182, gives the line HE metric and compact-Kähler
correspondence at a real Kähler form. Reuse the assessed existence
input. Chapter 1 Section 2.4, (2.6), printed p. 13, gives
chi(S,V)=ch_2(V)+2 rank(V) for coherent sheaves on a K3 surface.
For locally free V use standard Serre duality
H^2(S,V)=H^0(S,V^vee)^vee because omega_S=O_S (Hartshorne,
*Algebraic Geometry*, III, Theorem 7.6). An Euler number alone
does not establish acyclicity; control both endpoint groups.
No Euler number of this tensor is calculated here.

**Analytic holonomy.** Nomizu, *Reduction theorem for connections and
its application to the problem of isotropy and holonomy groups of a
Riemannian manifold*, Nagoya Math. J. 9 (1955), 57–66,
[Section I.1, pp. 58–59, and Proposition 2, pp. 60–61](https://doi.org/10.1017/S002776300002328X),
was inspected in primary text. Its setup is a smooth second-countable
principal bundle with Lie structure group; the K3 unitary frame and
projective frame bundles meet these hypotheses. The definitions and
connected restricted-holonomy statement concern general connections.
Proposition 2 reduces the connection to its holonomy bundle; its
proof uses radial parallel trivializations, holonomy-valued transitions
and tangency of horizontal vectors. No tangent-bundle, completeness
or homogeneous-space hypothesis is imposed on this proposition.
The classical connectedness theorem is also Kobayashi–Nomizu,
*Foundations of Differential Geometry*, vol. I, Chapter II Section 4,
Theorem 4.2. For simply connected bases full and restricted holonomy
agree. Do not assume general holonomy subgroups are closed; justify
the compact closure and its parallel invariant spaces in the attempt.

**Subdirect-product cases.** Bauer, Sen and Zvengrowski,
*A generalized Goursat lemma*,
[1109.0024v3, 8 June 2015](https://arxiv.org/pdf/1109.0024v3),
Theorem 2.1, manuscript p. 2, describes a subgroup of A x B by its
projected groups, normal kernels and isomorphism of quotients. The
forward construction and converse graph pullback were both read.
This is a group theorem, not tensor stability. For compact SO3
projections justify the relevant normal-subgroup cases and continuity
of the quotient isomorphism, then relate a linked case to actual
parallel adjoint bundles. Product holonomy is not an assumption.
The elementary low-rank group/representation checks are the identified
specialization, not a proposed new general theorem.

**Stronger algebraic-holonomy lead and scope difference.**
Balaji–Kollár, *Holonomy groups of stable vector bundles*, Publ. RIMS
44 (2008), 183–211,
[Propositions 4,7 and Section 8, pp. 185–187](https://www.cmi.ac.in/~balaji/Publications/HolonomyGroupsOfStableVectorBundles.pdf),
was read at theorem level. It gives algebraic connectedness for
simply connected smooth projective varieties and low-rank restrictions;
Proposition 7 assumes determinant triviality. Section 8 distinguishes
algebraic from differential holonomy. These statements do not directly
settle a joint connection at irrational h. No equality of the two
notions is imported; no curve tensor theorem constructs a K3 factor.

## Applicability obligations for the mathematical attempt

Use L052's simply connected projective K3 and exact h, and the actual
locally free factors from L080 and audited L088. Keep their common
determinant O_S(k) and different second Chern classes. Obtain their
HE connections at the same metric, with the dual determinant metric
on O_S(-k). Verify scalar cancellation on the global ordinary tensor
without introducing a square root of O_S(k). Check that the two
determinant wedge pairings give a global nondegenerate symmetric
O_S-valued form, and check integral determinant triviality.

Justify proper projective-holonomy projections and linked
joint-holonomy cases. In a linked case establish the parallel adjoint
identification before testing characteristic classes; distinct
bundles alone do not prove independent holonomy. Test all invariant
complex subspaces of the surviving representation, not just sections
of the separate factors. A direct parallel-End argument is also
within this same scope. Reprove only these elementary applicability
checks, not general existence, holonomy reduction or HE splitting.

For cohomology identify the actual Hom bundle by rank-two determinant
duality, apply the real-metric Hom constraints with their exact
ranks/slopes, and retain Serre duality. Compute the full normalized
Chern character and RR only in the later mathematical turn. Compare
actual/required rank, c_1, c_2 and all three cohomology groups. Section
vanishing is not underlying-vector stability; polystability and an
Euler identity alone are not acyclicity. No extra genericity or
algebraic/differential-holonomy comparison is assumed.

## Search, failures, access and coverage

Queries included `Balaji Kollar holonomy groups stable vector bundles
tensor product rank two Goursat`, `Kobayashi differential geometry
complex vector bundles tensor product Hermitian Einstein irreducible
holonomy theorem`, `Goursat lemma compact Lie groups SO(3) subdirect
product`, and `holonomy restricted connected simply connected
principal connection theorem Kobayashi Nomizu 4.2`. Snippets were
discovery only; the primary passages above are evidence. No full
exact statement was identified; this does not establish novelty.

Kobayashi's MSJ Vol. 15 book opened once, but targeted text requests
failed. The Kobayashi–Nomizu and Ambrose–Singer scans supplied no
inspectable proof text through this interface; TIFR alternatives
failed to open. These failed extracts are not evidence. Essential
coverage instead uses Nomizu's inspectable general-principal-bundle
passages and Perego's complete HE splitting proof. There is no
remaining essential source blocker for the bounded specialization.
No successful source download or API key was used.

Local duplicate/failure checks retain ATTEMPTS/056's necessary-index
stop. L087 gives conditional normalization and formal witnesses;
L080/L088 give individual factors. None supplies a tensor stability
proof. The constructive test is materially different from repeating
the exhausted index filter. No cross-notebook input is used.

Full matching and supporting Mathlib coverage: not checked. Goursat
support appeared as a discovery lead but was not inspected or imported;
no matching theorem is claimed absent. This changed ready assessment
awaits the supervisor's separate approval before mathematical
invocation. No tensor conclusion, lemma or mathematical script is
produced in this literature turn.
