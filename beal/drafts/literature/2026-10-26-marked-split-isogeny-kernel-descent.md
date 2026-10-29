# Proposed mixed descent through the fixed marked split cover

TARGET: Determine L127's finite isogeny kernel as a Q-Galois module and test whether it supplies a mixed obstruction to marked lifts beyond the separate quotient conditions.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused both L127 assessments; read L127, targeted L110/L111/L113 and L138/L139/L141 statements, L118/L124/L125 statements, and ATTEMPTS/050-052,055 plus history/507; searched explicit Prym kernel/Galois-module descent and general isogeny descent. The newly inspected Docking Proposition 5.4 Case II supplies the missing finite branch-label construction; no exact-instance obstruction was found in the inspected material and no novelty inference is made.
SOURCE_EVIDENCE: Freshly read Docking arXiv:2108.09564v2 Lemmas 4.1/5.3 with complete proofs pp.6/8, Sections 5.2.2-5.2.4 and Proposition 5.4 with its complete Case II proof pp.8-9; Bruin arXiv:math/0408069v2 Section 2.2 Proposition 2.2/proof pp.4-5; Schaefer corrected arXiv:1507.08325v1 Section 2 pp.2-3, Theorem 2.3 and full proof pp.6-7, Assumption II p.7, Section 2.3 Steps 4-6 p.8 and Proposition 2.7/proof p.10.
COMPARISON: Known kernel and branch-divisor theorems cover a finite instance specialization and Q-action by root permutation, beyond L127's rank-only conclusion. General descent supplies connecting maps and their hypotheses, not a certified extra marked-lift obstruction. L111 already gives the exact point-lift square condition; a new group condition must be compared with that condition and the existing local fake images.
GAP: Specialize the finite kernel and reverse-map kernel with correct transport and Galois action, then distinguish a test on quotient Jacobian classes from an identity automatic for actual marked points. Neither nonredundancy nor any Selmer/rank improvement is established; function-evaluation descent would require additional dual-kernel, injectivity and arithmetic checks outside this gate.
REASON: The explicit-kernel input passes the stated continuation test as a known, independently checkable structural input to joint-image comparison. Approve one bounded specialization/redundancy attempt, with no claim that a useful mixed obstruction exists and no reopening of saturated witness or blocked backend searches.
LITERATURE_REASON: Explicit kernel/Galois-module descent and a mixed marked-lift condition are changed hypotheses and conclusions outside the ready L127 rank-identity and L141 local-audit assessments.
SCOPE: Exactly TARGET, limited to finite branch-module specialization and a formal joint-image/redundancy test using L110/L111/L113/L127 and the recorded restrictions; no full Selmer computation, new local/point search, backend probe, unit/class search or numerical rank assertion. This is known-theory development, not an approved creative mechanism.

## Bounded test, not an established instance result

The main gap remains exclusion of residual positive primitive Beal
solutions. A plausible intermediate use is to retain compatibility between
the two quotient images of one marked point, which separate rank bounds
need not settle. This does not assert that such a constraint exists or
that it improves the rank of Jac(B). Point control and all integer,
degree-nine and other-signature obligations remain independent.

The exact map is L127's
F:Jac(B) x E -> Jac(C), given by the two actual pullbacks and L113's
Q-isomorphism. Its already proved reverse composition is multiplication
by two. Inspect the existing exact sources for their kernel statements
and then primary isogeny-descent statements, hypotheses and relevant proof
cases. Search standard terminology and stronger results before proposing
an instance calculation. A finite geometric kernel description must not
be mistaken for its rational points or for a cohomology/local-solubility
calculation. Import a matching theorem rather than reprove it.

Essential starting inputs are L110,L111,L113,L127 for the actual curves,
maps and twist, and L138-L141 for the present supported Jacobian bound.
The existing assessments for L127 are the first reuse candidates. Compare
only relevant existing marked-point claims in L114,L118-L125, located by
targeted search before reading their proof ranges. They concern another
descent representation and cannot be transferred without justification.
No cross-notebook input is proposed; preserve unfinished L108.

The finite later test would describe the kernel within geometric
two-torsion, its Q-action and one precisely stated induced compatibility
condition, then determine whether that condition is already forced by
the recorded separate quotient/marking equations. Continue only if a
primary theorem supplies a valid, independently testable mixed condition
or an essential explicit-kernel input with a plausible downstream use.
If it merely repackages the rank identity or existing cover equations,
record that overlap and abandon this mechanism without a new lemma.
Missing source access is not evidence of a mathematical obstruction.

This is preparation for possible discovery, not an approved creative
attempt. Routine kernel specialization must remain labeled reproduction
or specialization. No instance kernel, Galois-module calculation or new
mixed condition was derived in either the L141 audit or this source turn.

## Primary coverage completed in step 508

[Docking, arXiv:2108.09564v2](https://arxiv.org/pdf/2108.09564v2),
24 July 2023, published in J. Number Theory 265 (2024), 208-225,
DOI 10.1016/j.jnt.2024.06.009: for a connected unramified double
cover pi:D->B with class epsilon and Prym P, Lemma 5.3 gives
ker(phi)={(x,y) in Jac(B)[2] x P[2]: pi^*x=y}.
Lemma 4.1's proof identifies ker(phi^t)=pi^*(Jac(B)[2]) and
ker(pi^*)={0,epsilon}. Section 5.2.2 represents hyperelliptic
two-torsion by even branch subsets modulo complements. Proposition
5.4, Case II, assumes B:y^2=f g, deg(f)=4, deg(g)=2, with the
split cover and Prym Jac(y^2=f): the preimages of a quartic-root
pair class beta are that same pair class on B and its translate by
epsilon. Its full Case II proof uses divisor pullbacks. The last
display on p.9 has an apparent radical-index typo, confirmed visually:
one point with first coordinate gamma_i contains g(gamma_j).
Use the theorem table; check the actual pullback coordinates when
specializing, rather than copy that display. These are geometric
statements, not counts of rational kernel points.

The actual Q-model assignments are already canonical in L127:
quartic factor b/9 with coordinate R/3 and quadratic factor a with
coordinate h. Bruin's Proposition 2.2 identifies the quartic pullback
with this Prym over the ground field for squarefree even factors.
Its proof was reread; the existing L127 audit supplies the actual
rescaling to (E,O_E), cover hypotheses and transport through alpha.
The finite source construction therefore has matching hypotheses;
writing its branch labels and Q-action for these exact maps is the
approved later specialization, not an assertion made here. No degree,
rational kernel enumeration or splitting-field group is computed here.

[Schaefer, corrected arXiv:1507.08325v1](https://arxiv.org/pdf/1507.08325v1),
29 July 2015, Math. Ann. 310 (1998), 447-471, DOI
10.1007/s002080050156: Section 2 assumes a number field K,
an isogeny phi:A->J(X) with prime-power-exponent kernel, and support
including bad primes, primes over that exponent's prime, and real
places for two. Its connecting map has kernel phi A(K); Selmer
conditions use local connecting images. Function evaluation additionally
requires rational-divisor representability (Assumption I) and
cohomological injectivity for the chosen dual-kernel spanning set
(Assumption II). Theorem 2.3 identifies evaluation with the
Weil-pairing/Kummer composite; its proof includes comparison with
multiplication by q. Proposition 2.7 makes Assumption I sufficient
when the curve's index is prime to p. Steps 5-6 still require global
supported generators and complete local images. Thus the abstract
F-direction isogeny has the right framework, but no evaluation-map
injectivity or effective Selmer calculation follows merely from its
finite kernel. The printed correction to Proposition 2.4 is present
in this version; no uncorrected local cardinality formula is imported.

L113 already supplies rational infinity points on C, relevant to
the representability hypothesis. Any application must explicitly use
one and verify its transport; this review does not construct a new
Abel map. L127 supplies F and the reverse G with both composites [2].
For compatibility of a PAIR in Jac(B) x E with a Jacobian lift, the
map to examine is G, whose target is the product, not F. Schaefer's
function algorithm as stated has Jacobian target: it is not permission
to run it unchanged on G. The later bounded test may use the ordinary
Galois-cohomology connecting sequence and functoriality for these
isogenies, but an implementation on the product needs separate coverage.
No polarization identification beyond L127 is assumed.

## Exact duplicate comparison and continuation boundary

L111 already states all rational point lifts from E, including h=0
ramification and the missing rational fibers: the retained condition
is precisely h^2=3(4-T^2). L113 transports the same marked curve,
not an independent cover. L118-L125 give fake point-image restrictions
in the degree-eight algebra, while L138-L141 concern the odd-model
Jacobian Kummer map in Q x K. Their targets, scalar conventions and
point-versus-group images differ. No equality of these descent
representations has been proved or may be presumed. In particular,
a condition automatic after a marked point is supplied is not evidence
of extra pruning of the current separate ambient conditions.

ATTEMPTS/050 stops fixed point/divisor boxes; /051 rejects elliptic
rank zero; /052 parks a particular octic class backend. /055 excludes
a rational three-isogeny on E. None rules out this two-primary fixed
product isogeny. Conversely, none supplies its missing local images,
global arithmetic or a mixed obstruction. L124's joint norm/real/dyadic
test and L125's exhausted quadratic family are not a joint F/G descent.
These comparisons preserve their original limits and unfinished L108.

The approved later attempt has one finite stopping boundary: instantiate
the source kernel construction and its Q-action, identify the direction
and target of a proposed compatibility test, and compare it with the
existing same-T lift equations and recorded quotient restrictions.
Continue beyond that attempt only with a concrete test on quotient
classes whose extra content is justified, or an essential explicit
kernel input with a stated use in a separately assessed descent.
If the proposed constraint is merely automatic from the exact lift
equations, record redundancy and stop that proposed shortcut. Unknown
nonredundancy is not a rank bound; lack of source access is not a
mathematical obstruction. No unbounded Selmer implementation is approved.

Search queries included `unramified double cover genus two Prym isogeny
kernel descent Jacobian elliptic Galois module`, `Schaefer computing a
Selmer group of a Jacobian using functions on the curve isogeny descent
kernel exact sequence`, and `Prym isogeny descent genus 3 hyperelliptic
elliptic genus 2 kernel Selmer compatibility`. The primary sources above
were actually read, including the complete relevant proof cases.
Schaefer-Wetherell, JNT 115 (2005), 158-175, DOI
10.1016/j.jnt.2004.11.014, was found through its publisher abstract
only; its general auxiliary-Jacobian algorithm is an UNREAD lead,
not an essential input to the bounded finite-module test and not
approval for a G-direction implementation. Generalized-descent and
other search hits were not used as theorem inputs.

The unchanged Beal statement is reused from foundations' same-day
primary audit; the AMS access limitation is unchanged. Full matching
Mathlib coverage of this kernel/Prym descent was not checked, and no
absence claim is made. This source turn changes readiness only:
no lemma, mathematical script, DAG edge or PROOF.md argument changes.
