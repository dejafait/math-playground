# Seven-adic image critical audit — source coverage ready

TARGET: Critically audit L090's exact primitive whole-fiber two-descent image at seven, including both branch neighborhoods and the canonical realization.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused unchanged exact-image and stronger good-prime searches in 2026-10-17-primitive-seven-two-descent-image.md; compared the full L090 proof, L047 rational-fiber/audited base-change ranges, history/295–296, the thirteen-image audit assessment and ATTEMPTS/039–040. No duplicate completed seven-image audit was found in these targeted records.
SOURCE_EVIDENCE: Reopened BPT arXiv:2001.02263v3 Definition 1.6, Theorem 1.8 split-case proof and Corollary 1.9 proof pp.3–6; FNS 10 June 2019 Section 7.2 pp.25–27, entire twelve-subgroup paragraph and complete 54a1 Table 5 polynomial; Stacks tags 04GK and 01JQ statements/proofs. Reused inspected Bruin–Stoll and Clark/Milne coverage from the construction assessment, with precise ranges below.
COMPARISON: Sources cover unrestricted Kummer classes, lifting and entire canonical-fiber transport, but do not certify the correlated two-class image. Repeated branches require L090's uniform arguments; the rational canonical fiber is reusable at seven, whereas its three-adic power witnesses are not.
GAP: No essential source blocker remains for this audit; independent verification of arithmetic, integral model/map, branches, tail, all identifications and shared primitive realizations remains outstanding. No global independence or dimension improvement is covered.
REASON: Approve one subsequent REPRODUCTION proof_audit of exactly TARGET; this source review neither verifies L090 nor derives a result or replays its mathematical certificate.
SCOPE: L090 and scripts/primitive-seven-two-descent/image-certificate.json; L033/L034 model/map, L047 rational canonical fiber and L069 fixed cubic. No global comparison on T or new image calculation.
LITERATURE_REASON: Gate-required separate approval of the newly proposed critical-audit scope, especially seven-adic map/branch arguments and canonical realization; reuse ready discovery and general methods.

## Source comparison and reuse

The construction assessment's exact-family, terminology and stronger-result
searches remain adequate for the unchanged field, map, cubic and primitive
predicate. No inspected exact-image match was established; this is not a
novelty claim. The thirteen-image audit assessment supplies methodological
comparison only, with no prime-specific conclusion imported at seven.

Barrera Salazar–Pacetti–Tornaría, *On 2-Selmer groups and quadratic
twists of elliptic curves*, [arXiv:2001.02263v3, 17 September 2020](https://arxiv.org/pdf/2001.02263v3),
Section 1 pp.3–6: Definition 1.6(ii) applies over a finite extension of
Q_p to an integral monic square-free cubic whose polynomial order is
maximal. Theorem 1.8 gives norm-square unit containment; Corollary 1.9
gives equality for odd residue characteristic using Lemmas 1.3 and 1.5.
The full split-case valuation proof and cardinality argument were reread.
Split cubics are allowed; Section 2 global narrow-class and two-torsion
hypotheses are not required here. Audit the actual cubic, maximal-order
premise and coordinate change over U. This is only the unrestricted
baseline, with no common-scalar or whole-fiber assertion. No reproof of
the general theorem is needed.

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents
2, 3, n*, Compositio Math. **156** (2020), 77–113,
[10 June 2019 manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, printed pp.25–27: reread the entire twelve-subgroup
Galois-set/irreducibility paragraph and full 54a1 Table 5 polynomial.
The canonical rational fiber is identified with a degree-twelve field
before the GRH-dependent Selmer computation; its dimension column is
not an unconditional input. Equation (7.4) is an elimination identity,
not by itself a whole projective fiber presentation. Reuse the prior
assessment's complete general Lemma 7.5 proof and specifically dyadic
Lemma 7.6 comparison. Neither certifies the seven-adic branch arguments.
L047's rational-fiber identification is reusable; its Q3 square root is
not a Q7 power witness.

The Stacks Project, [Lemma 10.153.7, tag 04GK](https://stacks.math.columbia.edu/tag/04GK),
statement and entire proof reread: reduction over a henselian local ring
is an equivalence for finite etale algebras, including morphisms. Verify
finite etaleness of the regular integral fiber before applying it;
repeated branch reductions do not satisfy that premise.
[Lemma 26.17.2, tag 01JQ](https://stacks.math.columbia.edu/tag/01JQ),
statement and tensor-product proof reopened, supplies affine fiber
products. Reuse L047's audited application to the rational canonical
coordinate field, preserving the entire algebra under base change.
A point defined over a field of smaller degree is not a substitute.

Reuse Bruin–Stoll, *Two-cover descent on hyperelliptic curves*, Math.
Comp. **78** (2009), 2347–2370,
[14 March 2008 manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Remark 2.1, Section 4 pp.6–10, Lemmas 4.3–4.4 with proofs/local algorithm
cases, and Section 9 p.15. The construction assessment inspected the
odd-degree full-algebra convention, exceptional root/origin values and
constancy hypotheses. The unrestricted algorithm does not automatically
retain the shared-scalar predicate. Audit L090's direct specialization;
do not claim that algorithm was executed for the restricted image.

Reuse Milne, *Algebraic Number Theory*,
[v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
Theorem 7.33/Remark 7.36 pp.121–123 (coprime factor lifting), Corollary
7.42/Remark 7.43 p.124 (local degree), Proposition 7.50 and Example 7.54
pp.127–129 (unramified extensions); Clark, *Algebraic Number Theory II*,
[161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
revision unidentified, Theorem 1.79 p.58: over a complete valued field,
the strict inequality v(f(r))>2v(f'(r)) gives the root lift.
Actual residue roots and derivatives must be checked. Coprime block
lifting does not require internal squarefreeness of each block. These
inputs were already inspected in the construction assessment and were
not reopened simply to repeat reading. No essential unread source
remains. Mathlib full/supporting coverage is not checked, with no
absence claim.

## Bounded audit and decision test

Main gap: positive primitive integer emptiness, in the 54a1 branch and
across residual signatures. Intermediate target: independent critical
verification of L090's exact seven-adic image. Downstream use: a reliable
necessary filter for a separately assessed comparison on L084's T.
L088's global norm may instead make it redundant; this remains unresolved.
Both global dimension bounds remain unchanged.

Inspect complete load-bearing certificate fields and independently replay
required arithmetic, rather than trusting the reported 33 checks. Use
bounded JSON previews only for orientation; inspect complete selected
values for proof. Check coefficient provenance against L034, full-field
irreducibility, the entire cubic, fixed theta and all field identifications.
Check every integral-map open, their agreement and coverage at x=16,
the origin chart, full reduced polar divisor, degree and separability.
Check the properness-to-integral-coordinate passage for finite scalars.

For all five regular residue disks check full factorizations,
irreducibility, squarefreeness, reconstruction and lifting/exhaustion,
including the removable chart. Replay full character tables and both
quadratic-root orderings, retaining every isomorphism. At zero check
irreducibility of the degree-four reduction, coprimality, nonzero unit
differences, characters and their preservation under the actual extension
degree. This bounds compatible point classes without claiming etale
lifting of repeated fibers. At 1728 check all coprime squared blocks,
their lifted degrees, y reconstruction and the point-field degree
contradiction. Check the origin's rational lift and algebra-map
contradiction uniformly for all negative valuations and unit parts.
Do not replace uniform arguments with sampled centers or depths.
Retain exceptional Kummer values until their exclusion is justified.

Audit both directions of the primitive scalar criterion, including
residual power solvability, integrality, nonzero coordinates and the
same c in both identities. Independently verify the entire fibers and
common primitive witnesses at 2 and 9261/8. The canonical realization
must use L047's rational entire field and lift b^4=169 directly; a square
root of +13 at seven is not an imported premise. Only the full upper
bound and both exact realizations establish image equality/subgroup
status. No extra classification of compatible zero-branch scalars is
required beyond L090's actual claims.

Continue if every essential hypothesis, calculation and uniform proof
passes, or repair a concrete defect and narrow the conclusion. An
unresolved branch, chart, identification or realization leaves exactness
pending and blocks downstream use. Success verifies a local reproduction,
not independence on T, rank or Beal. Inputs: L090 and its named full
certificate, L033/L034, L047 and L069. No cross-notebook input. No global
S-unit basis, class-kernel value, global tuple realization or integer
lift is assumed.

History/296 is construction, not a completed critical audit. ATTEMPTS/039
stops thirteen-adic independence; ATTEMPTS/040 stops a sufficient
eleven-adic envelope certificate. Neither bans this audit or authorizes
repeating those stopped calculations. Unfinished work is preserved.
This literature turn changed no lemma or mathematical script, performed
no new derivation and did not run the image checker.
