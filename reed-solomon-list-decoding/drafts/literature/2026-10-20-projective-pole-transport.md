# Projective transport of the fixed-pole family — source comparison

TARGET: Assess whether a projective change of evaluation coordinate over E preserving H can transport L102's centers into L100's bounded family while preserving the degree<64 code and simultaneous column agreement.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched generalized Reed–Solomon projective/fractional transformations, monomial equivalence, automorphism groups, and multiplicative-subgroup stabilizers; reused the Proposition 3.6 lead in the local 2026-10-08 nonprime-coordinate assessment and inspected the primary statements listed below. No inspected theorem decides the exact center-family transport.
SOURCE_EVIDENCE: Marquez-Corbella–Pellikaan arXiv:1508.02187v1 Section 3.1 pp.7–9 Proposition 3.6 and its cited-proof notice, Remark 3.7 and full Corollary 3.8 proof; Beelen–Glynn–Hoholdt–Kaipa arXiv:1611.04341v1 Section 2 pp.3–6 equations (4)–(8), Proposition 2.5 with preceding construction, Theorem 2.7/full proof and Lemma 2.9/full proof, Theorem 2.10 statement; Joyner–Ksir–Traves arXiv:0801.4007v1 Theorem 3/Remark 3 p.5.
COMPARISON: Known GRS results cover code-compatible projective transformations and constrain multipliers; they do not supply the stabilizer of this H or matching of these complete received-word families. Approve only that finite specialization, with explicit code/isometry and whole-family verification.
GAP: Determine the H-preserving projective maps and test the induced multipliers on the entire L102 parameter family against L099/L100; no pole-only inference, equivalence, family exclusion or sharp-boundary conclusion is established.
REASON: Essential code-equivalence coverage is now accessible and adequate; the remaining finite domain and center-family comparison is a mathematical specialization, not a reason for further general browsing.
SCOPE: E=F_65537, H=<19139> of order 1024, F=F_(65537^28), strict degree<64, every m>=1, projective maps over E defined on and preserving H, and their compatible nonzero column multipliers; literal transport into the L099 family.

## Gap, relevance and bounded test

The main gap remains arbitrary-center safety at 67/68 agreements and the
955–957 bracket. The intermediate target is exactly TARGET. If a single
code isometry transports the whole L102 family into L099's family, L100's
existing upper bound could exclude it. This would still leave arbitrary
centers and the ABF-model comparison open. A failed transport is a stop
only on this mechanism, not on all isometries or on safety.

Continue only with a complete exact description of the eligible maps and
multipliers and a test of every parameter, or a necessary-condition
obstruction excluding them all. Abandon this route if domain preservation,
code preservation or whole-family containment fails. A failed individual
map is not exhaustion. No such mathematical test is performed this turn.

## Primary sources actually inspected

[Marquez-Corbella and Pellikaan, arXiv:1508.02187v1](https://arxiv.org/pdf/1508.02187v1),
Section 3.1, Proposition 3.6 (printed p.8), covers equality of GRS codes
for 2<=k<=n-2 with distinct projective locators and nonzero multipliers.
It gives an invertible matrix M and nonzero scalar lambda, with transformed
locators phi(M,a_i) and multipliers lambda*theta(M,a_i)^(k-1)*b_i.
Here phi(M,z)=(Az+B)/(Cz+D); on the denominator-nonzero branch,
theta(M,z)=Cz+D. Infinity has separate normalization cases. The proposition
refers to earlier proofs rather than proving the classification there.
Remark 3.7 and the full Corollary 3.8 proof give uniqueness from three
locator images and constant proportionality when three locators are fixed.
The proposed n=1024,k=64 satisfy the dimension restrictions over both E
and F. This is a code-representation theorem, not a statement about centers.
No zero-denominator branch is needed for a map sending H into H; it must
nevertheless be excluded explicitly in the specialization.

[Beelen, Glynn, Hoholdt and Kaipa, arXiv:1611.04341v1](https://arxiv.org/pdf/1611.04341v1),
Section 2, supplies independent primary construction coverage. Equations
(4)–(8) and Proposition 2.5 (printed pp.3–4) describe the projective action
on the normal rational curve using the dual symmetric-power representation,
including positive-characteristic normalization. Its coordinate convention
is (gamma+delta*t)/(alpha+beta*t), so matrices cannot be copied between
sources without conversion. Theorem 2.7 and Lemma 2.9 (p.5), whose full
proofs were inspected, establish uniqueness from k+2 general-position
points and preservation of the curve by a projectivity mapping those points
onto it. The proof uses GRS duality and three fixed projective locators.
Theorem 2.10 (p.6) identifies the curve's projective linear automorphism
group with PGL_2(K), assuming k<|K|. That hypothesis holds here. The latter
theorem's full proof is not needed or imported: the proposed mechanism is
already restricted to PGL_2(E), and the explicit construction suffices.
None of these results classifies the stabilizer of this finite H.

[Joyner, Ksir and Traves, arXiv:0801.4007v1](https://arxiv.org/pdf/0801.4007v1),
Theorem 3 and Remark 3 (printed p.5), concern lifting permutation
code automorphisms to curve automorphisms preserving the evaluation and
message divisors. On P^1 their stated sufficient restriction is positive
message-divisor degree and n>2*deg(D). This narrower permutation theorem
is not substituted for monomial equivalence. Its deeper lifting proof
was not inspected and is not an essential input. Finite-group classification
leads are unnecessary for the direct finite-domain test and remain unused.

## Exact remaining applicability obligations

L099 hypotheses/conclusion and L100 hypotheses/conclusion were read:
L099's scalar center is X^64+a/X+b/X^2+c/X^3, with a,b in E and
c nonzero; L100 handles c in H and L099 supplies emptiness outside H.
L102's corresponding expression is (X-3)^64+a/(X-3)+b/(X-3)^2+
c/(X-3)^3. Its dictionary and unsuccessful allowance are preserved;
ATTEMPTS/085 stops only the absolute-sieve estimate. Foundations/02
specifies degree<64 and simultaneous closed column balls. No new proof
or mathematical script is written in this source review.

The next attempt must state its action direction explicitly and check
nonzero multipliers and inverse. It may use homogeneous substitution of
degree 63 from the cited construction, checking all strict-degree messages,
including lower degrees and zero, over F. A generic equivalence to some
weighted GRS code does not suffice: the image must be the same unweighted
code on H. Apply the same column permutation/scaling to every tuple row
and received word and prove preservation of simultaneous equality and
list cardinality. Keep ambient F and threshold T unchanged.

Classify eligible projective maps by a proved finite-domain argument or
complete finite certificate; do not assume the stabilizer is dihedral.
A polynomial identity involving X^1024-1 is an available test formulation,
not a result already established here. Three-point uniqueness can support
finite exhaustion, but a sampled collection is not complete. Check all
source parameters a,b in E,c in E^*, permitting the destination parameters
to depend on them. Literal equality must hold on all H, not merely as a
pole heuristic. No codeword translation, semilinear map, changed domain,
changed degree or changed field is covered by this assessment. If the
attempt needs one, preserve this target and request separate coverage.

This is a SPECIALIZE assessment because known code equivalence is imported,
while the finite-domain and center-family difference remains to be tested.
Reproving the general GRS classification is unnecessary. Any elementary
argument is restricted to that difference and the simultaneous-column
applicability check. No novelty is asserted. Mathlib coverage of the full
projective/monomial equivalence theorem has not been checked.

Essential local inputs for the next attempt: L102, L099, L100, C012a and
foundations/02. Their existing proofs supply only their stated results;
none supplies the unproved transport. No cross-notebook input is used.
