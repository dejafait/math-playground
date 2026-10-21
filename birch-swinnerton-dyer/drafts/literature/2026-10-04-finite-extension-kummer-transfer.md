# Finite-extension global Kummer witness: ready transfer specialization

TARGET: Apply restriction/corestriction and the finite Kummer sequence to test whether global Kummer realization over one finite extension F/Q of L018's prescribed basis at a depth m >= 2 exceeding v_p([F:Q]) forces r = 2, keeping the extension degree and realization premise explicit.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The parent arithmetic-certificate comparison screened fixed-extension/global-Kummer transfer and located Milne's primary transfer and Kummer statements; exact searches are recorded in 2026-10-04-arithmetic-rank-two-exterior-certificate.md. No exact named version of the proposed L018-specific depth criterion was located, and no novelty inference is made.
SOURCE_EVIDENCE: Milne, Class Field Theory v4.03 (2020-08-06), Chapter II Example 1.29/Proposition 1.30, printed p. 70, and Proposition 4.2, p. 87; Milne, Elliptic Curves second edition (2021), Chapter IV Section 2 equations (28)--(29), pp. 112--113 and coefficient diagram p. 129; L018's assessed Selmer/Sha structure is reused.
COMPARISON: Standard transfer controls the kernel of restriction by the extension degree, and the global finite Kummer sequence distinguishes point realization from local Selmer conditions. The remaining work is a short conditional application to L018's basis and divisible quotient, including the exact p-power loss; no actual global-point realization is supplied by the sources.
GAP: Check the proposed finite-depth sufficient criterion for eliminating the divisible Sha quotient. A field F and points realizing the restricted prescribed classes have not been constructed, and must remain a separate arithmetic premise.
REASON: Approve this independently testable conditional mechanism after the direct derived-class import failed its scope comparison. Import transfer and Kummer exactness by citation, and derive only their identified L018-specific consequence.
SCOPE: Retain all L018 hypotheses, its downward coefficient-compatible basis x_i^(m), and Sha(E/Q)[p^infinity] = (Q_p/Z_p)^(2-r). Introduce a finite extension F/Q and require res_F(x_i^(m)) to belong to the image of E(F)/p^m E(F) in H^1(F,E[p^m]) for both i. Assume neither finite Sha over either field nor any rational rank. The new global Kummer condition is an additional test premise, not ordinary Selmer membership over F.

## Exact primary coverage

J. S. Milne, *Class Field Theory*,
[v4.03, Chapter II Proposition 1.30 and Example 1.29, printed p. 70/PDF p. 79](https://www.jmilne.org/math/CourseNotes/CFT.pdf#page=79):
read the norm/corestriction construction and the proposition's proof.
Restriction followed by corestriction is multiplication by the finite
subgroup index. [Proposition II.4.2, printed p. 87/PDF p. 96](https://www.jmilne.org/math/CourseNotes/CFT.pdf#page=96)
identifies discrete continuous cohomology with the direct limit over
finite quotients. Use these known inputs for finite coefficients and
the discrete module E(Qbar); do not assume integral restriction is
injective when p divides the degree. The relevant extension need not
be Galois: its absolute Galois subgroup has the required finite index.
Compatibility with the point-to-cohomology connecting map must be
stated in the application rather than replaced by a height argument.

Milne, *Elliptic Curves*, second edition (2021),
[Chapter IV Section 2, equations (28)--(29), pp. 112--113/PDF pp. 117--118](https://www.jmilne.org/math/Books/EC2.pdf#page=117):
read the finite multiplication exact sequence, its cohomology sequence,
the global point image, and the Selmer/Sha sequence. The text explicitly
extends these definitions to number fields. Reuse the
[coefficient diagram, p. 129/PDF p. 134](https://www.jmilne.org/math/Books/EC2.pdf#page=134)
for reduction on points and multiplication on Sha. Neither exact
sequence assumes finite Sha. The global E(F)/p^m image is stronger
than satisfying Kummer conditions at each completion of F.

L018 and its [ready source assessment](2026-10-04-central-vanishing-all-depth-classical-lifting.md)
already supply the basis and divisible quotient. Do not reprove Kim's
structure theorem, impose higher P_(m,0) eligibility, or identify the
chosen compatible lifts with a new prime-deletion family.

## Relevance, discriminating test and limits

The proposed threshold is m > d, with d = v_p([F:Q]) and m >= 2.
Test whether the known transfer identity and both global Kummer
realizations at that one depth exclude the nonzero quotient dimension
2-r permitted by L018. Track the basis's images in Sha[p^m], the
restriction map into H^1(F,E), and the degree factor. This paragraph
specifies the future calculation; it proves no new implication.

If the conditional criterion works, its plausible downstream use is
a finite geometric witness for the lower bound r >= 2 on this branch.
The key later task would be producing the required E(F) points and
matching their Kummer classes to the actual prescribed arithmetic
classes. An algebraic cycle in a higher-dimensional variety, a local
logarithm, or a classical Selmer class alone is not that witness.
Production of the two-prime premise from m(E)=2, uniform hypotheses,
analytic comparison and higher ranks also remain open.

Continue if the argument establishes the proposed bound without hidden
finiteness or coefficient assumptions. If it fails, identify the
precise extra assumption or degree loss and stop that inference.
Do not treat separate splitting fields for torsors, or a sequence of
fields with unbounded p-part of their degrees, as the stated witness.
The relevant conditional statement is a specialization of standard
descent, expected to be REPRODUCTION, not a new general theorem or BSD
advance. There is no essential unread source for this bounded task.

## Mathlib

Full coverage of the proposed L018-specific finite-depth certificate
and supporting restriction/corestriction/Kummer results: **not checked**.
Milne II.1.30 and IV.(28)--(29) cover supporting named inputs, not the
full depth criterion or a Mathlib declaration. No absence or originality
claim is made.
