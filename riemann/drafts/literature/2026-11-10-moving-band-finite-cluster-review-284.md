# Moving-band finite-zero-cluster mechanism: uncovered continuation

TARGET: Assess source coverage for extracting a finite zero cluster from L994's actual (G_1,G_2), with a common continuation domain and a holomorphic complementary term at a candidate cluster singularity, without rightmost-zero or nonresonance assumptions.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step285 completed bounded searches for moving-cutoff Laguerre/zeta generating functions, Hadamard continuation, parameter-integral pinches, finite-cluster singularities and mixed Laguerre/Lagrange inversion; exact queries and inspected versus unread leads are below. Local comparisons include reviews212/279/280/282, stops214/244/279 and the older complete-response/rational-response assessments. No matching actual-pair complementary-holomorphy theorem was identified; no novelty inference.
SOURCE_EVIDENCE: Reuse the approved MV MNT I section5.1 Theorems5.1-5.2/Corollary5.3 pp137-140 and DLMF18.12.13/18.14.8 only for the initial germ. Newly read Li–Sauzin–Sun arXiv2012.14175v1 Definition1.1/TheoremA, Lemmas2.1/2.3 and proof pp1-7; Pérez-Marco author PDFs Local monodromy Theorem1.1/Section2.1 pp2-5 and Monodromies Theorem1.5/Sections4.2/5.1 pp4-5,16-17; DLMF1.10(iv),(vii),(viii); Gessel1609.05988v1 Theorems2.1.1/4.1.1 and residue proof pp1-3,22-23. Direct URLs and precise scope below; none is imported as an actual-pair extraction theorem.
COMPARISON: Hadamard continuation requires an identified product of already continuable factors; monodromy formulas require isolated singularities and retain coincident contributions and polar residue terms. Neither theorem identifies L994's coupled (w,s) integral with such a product or controls its infinite-height complement. Finite-contour holomorphy is available, but compact-uniform convergence on the new domain remains a hypothesis. This changes the route from actual extraction to an independently defined single-quartet transform test.
GAP: The actual common continuation domain, singularity isolation from all other zeros, compatible contours and compact-uniform complementary height limit remain unproved. A rational quartet can test survival through the transform independently; even success cannot supply the actual complement.
REASON: Step285 completes this source assessment and parks direct actual-cluster extraction because its proposed source justification leaves the defining complement condition unpaid. Prepare a finite-pole detector test using inspected local inversion tools; no new formula, lemma, proof or mathematical script is derived in this literature-only step.
LITERATURE_REASON: The new target crosses from the approved absolute-convergence Perron line to zero-sensitive continuation and complementary holomorphy, neither covered by review282.
SCOPE: Source assessment only, actual Lambda including all powers and exactly L994's r=1,2 germs. Retain multiplicities, all four jumps, both Dirichlet branches and the complete continuum term. No RH, rightmost zero, nonresonance, simple zeros or unproved infinite-zero exchange.

## Main gap and proposed discriminating test

L030-L032/C032a actual-Xi positivity and L966/L968 signed forcing
remain open. Use L994 as the initial analytic object, with L985's
exact kernel and L989's endpoint convention. L990/C990a/L993 and
L984(H) are downstream context only, not inputs to this review.
No cross-notebook theorem is proposed. Full matching Mathlib coverage
is unchecked and unknown.

The proposed future mathematical test would isolate a finite cluster
of nontrivial zeros with full multiplicities, starting at finite
Perron height and keeping both shifted zeta branches. A source-supported
construction would have to identify a concrete candidate singularity
and a common continuation neighborhood in which the complete
complement is holomorphic. Only then could it test whether the
cluster's contribution to at least one of G_1,G_2 is nonremovable.
This paragraph defines a desired test, not a decomposition, formula,
existence assertion, or approved mathematical target.

Other zeros may not be discarded or assumed to have smaller real
part. The complementary term must include all uncrossed contributions,
horizontal edges, the limiting contour, J_r and -C_r with their actual
signs. A bound on a fixed finite contour is not uniform passage to
infinite height. A branch in an integrand alone does not establish a
singularity after either contour integration or addition of remainders.

Continue only if primary statements and essential proof cases support
a concrete deformation/domain contract and an independently testable
remainder condition beyond the original identity. A theorem requiring
RH, rightmost-zero dominance, nonresonance, or an assumed holomorphic
complement does not pay that condition. If the only result is a formal
cluster extraction, record the exact obstruction and park this test;
do not schedule repeated source approvals or assert a global ban.

## Three mechanisms compared at nomination

1. Direct interval/PNT or absolute-prefix payment: stops244 and279
   record unpaid signed correlations and mismatched source hypotheses.
   There is no new input here to reopen that route.
2. Further adjustment of L994's initial contour or convergence disk:
   the audited representation is adequate as an initial germ. A larger
   absolute-convergence disk alone supplies neither signed outputs nor
   complementary analyticity. No further construction/audit is nominated.
3. Finite-cluster continuation with a common holomorphic complement:
   selected for source assessment. It tests actual cancellation after
   resummation and is distinct from source approval or absolute bounds.
   Review212/stop214 concern the full-Li contour, not this moving-band
   pair; preserve their sign and horizontal-estimate warnings and do
   not import their disputed conclusion. No novelty is inferred.

After adequate separate coverage, a genuinely new noncancellation
test could warrant proof_attempt/creative, deep_research/max. The
precise prospective escalation is that a zero contribution visible
before the coefficient contour may disappear after integration or
cancel against the complementary term; testing one specified cluster
and neighborhood would decide whether this mechanism can constrain
the actual corrections relevant to signed forcing. Coverage and a
concrete neighborhood are presently missing, so that proof is not
approved or scheduled now. The next invocation is literature_comparison,
standard/high. No formula, estimate or lemma is derived here.

## Completed source comparison — step285, 10 November 2026

The nomination above is preserved as historical scope. Its literal
source-review TARGET has now been completed. EXPLORE records the
bounded no-match comparison, not approval of the full extraction or
proof that no applicable theorem exists. The new evidence is a
specific hypothesis mismatch; the original full-complement test is
parked, rather than sent through another unchanged approval/audit.

### Primary hypotheses and essential cases actually read

Y. Li, D. Sauzin and S. Sun,
[*Hadamard Product and Resurgence Theory*, arXiv:2012.14175v1,
28 December 2020](https://arxiv.org/pdf/2012.14175v1),
Definition1.1 and TheoremA, pp1-2: an A-continuable germ continues
along every path avoiding the nonempty closed discrete set A.
For A-continuable f and B-continuable g, with both sets closed
discrete, f Hadamard-product g is continuable outside {0} union A*B.
This is a possible-singularity inclusion, not nonvanishing of a
singular part. Lemma2.1, pp5-6, proves product-set discreteness using
positive minimum nonzero moduli. Definition2.2/Lemma2.3 and proof,
pp6-7, transport a
contour by homeomorphisms fixing A and carrying the moving points
z/B, and glue local holomorphic integrals by Cauchy's theorem.
No assumption establishing
the input factors' continuability is proved by the theorem.

L994 is not presented as f(w)g(z/w): its S arguments also depend
on s, its zeta arguments depend on w, and the height limit is only
verified on the initial disk. A Hadamard identification, closed
discrete singular sets for the resulting factors and a path avoiding
their full collision set have not been supplied. Applying TheoremA
before those checks would assume the missing continuation.

R. Pérez-Marco,
[*Local monodromy formula of Hadamard products*, author-hosted
18-page version](https://webusers.imj-prg.fr/~ricardo.perez-marco/publications/articles/Hadamard6.pdf),
Theorem1.1, p2, and Section2.1, pp3-5, require isolated integrable
singularities, defined by the Stolz limit (z-alpha)F(z) tending to
zero. The iterated monodromy is a sum over every factor pair with
the same product. The proof shrinks turning loops using integrability;
there are then no polar contributions. This theorem cannot simply
be applied to the poles of -zeta'/zeta. Nor does its sum imply that
one selected contribution survives cancellation.

The stronger
[*Monodromies of singularities of the Hadamard and ene product*,
author-hosted 24-page version](https://webusers.imj-prg.fr/~ricardo.perez-marco/publications/articles/enemonodromy11.pdf),
Definitions1.1-1.4/Theorem1.5, pp4-5, allows an isolated singularity
whose monodromy is holomorphic, retaining a possibly polar
single-valued part. Its formula includes both residue sums and a
convolution of monodromies. Section4.2, p16, sums coincident product
pairs; Section5.1/Lemma5.1, pp16-17, computes the shrinking-loop
residues and their change-of-variable sign. Thus the integrable-only
restriction is not a general prohibition on polar inputs. The
unidentified product and actual complementary height limit still
prevent its use here. These source formulas were compared, not
specialized, audited or reproved.

[NIST DLMF1.10(viii), (1.10.18)-(1.10.19)](https://dlmf.nist.gov/1.10#viii)
states holomorphy for a jointly continuous integrand analytic in
the parameter on a common domain over a finite interval. Improper
integration additionally requires convergence uniform on every
compact subset of that domain. The M-test gives a sufficient
integrable majorant. L994's initial-disk convergence is not evidence
for this condition on a new neighborhood. A finite-height contour
without a pole on it cannot replace that missing hypothesis.

For an independently testable finite-kernel question, read
[DLMF1.10(vii), (1.10.12)-(1.10.17)](https://dlmf.nist.gov/1.10#vii):
analytic f with f'(z0) nonzero has a local analytic inverse; the
extended version treats a convergent leading power of order mu>0
with nonzero leading coefficient and distinguishes fractional-power
branches. These are local assertions, not global sheet selection.
[DLMF1.10(iv), (1.10.8)](https://dlmf.nist.gov/1.10.E8)
applies to a positively oriented closed contour with finitely many
interior singularities and none on the contour. Its hypotheses must
be checked before closing a finite-pole integral. Live DLMF text was
read on 10 November 2026; the visible site version is not separately
verified in this step.

I. M. Gessel,
[*Lagrange inversion*, arXiv:1609.05988v1, 20 September 2016](https://arxiv.org/pdf/1609.05988v1),
Section1.1/Theorem2.1.1, pp1-3, works over an integral domain
containing the rationals, with formal series R independent of x
and f=x*R(f). In the safe subcase R(0) nonzero and power-series psi,
(2.1.4) identifies [x^n]psi(f)/(1-x*R'(f)) with
[t^n]psi(t)*R(t)^n. Theorem4.1.1 and its residue-change proof,
pp22-23, require a substitution with nonzero linear coefficient;
the proof treats exponent -1 separately. These formulas can match
finite response coefficients. Formal substitution alone establishes
neither an analytic domain nor a surviving singularity. No moving-band
specialization is performed here.

### Search, duplicate and failure record

External discovery queries included:

- `Laguerre polynomials generating function L_n(n x) Lambert W singularities`
- `Hadamard multiplication theorem contour integral analytic continuation singularities product theorem`
- `Riemann zeta zeros Laguerre moving cutoff generating function prime sums`
- `Laguerre Lagrange generating functions Carlitz`
- `Hadamard Product and Resurgence Theory theorem closed discrete`
- `singularities parameter integrals pinch theorem analytic continuation`
- `Laguerre finite zero cluster zeta generating`
- `Hadamard zeta moving Laguerre`
- `Carlitz Some generating functions for Laguerre polynomials pdf`

Broader pinch/physics results were screened as leads only: no theorem
from them is relied on. Carlitz's Duke1968 paper and SIAM1977 paper
were identified bibliographically but their proofs were not retrieved.
Dattoli–Lorenzutta–Sacchetti, JMAA257(2001), 308-320,
DOI10.1006/jmaa.2000.7345, was located with author-uploaded mixed
Laguerre formulas; the OSTI preprint endpoint returned502. No formula
from that lead is imported. This optional access failure is not an
essential blocker: the general inversion statements above were read.
The JHU Fill–Flajolet–Kapur PDF endpoint failed to fetch; it is not
used. Search snippets and abstracts establish no theorem hypotheses.

Local scoped searches first located reviews212/279/280/282 and
stops214/244/279, then searched specific pole-response/Hadamard/
Lagrange terms in this notebook's assessments and attempts.
The November3 inner-spatial rational-response and complete-response
support-germ assessments concern the L666 spatial family, not these
actual moving-band germs. Their useful warning is preserved: a
singularity of an isolated term need not pass to the complete sum.
The November9 joint pole-integral residual review12 concerns L929's
finite energy operator and has different inputs. The old exact-residue
projection stop concerns L666's unsigned norm threshold; it supplies
no missing complement here. None is reused as a theorem for L994.

The full-Li stop214 continues to forbid importing the defective
printed residue/horizontal argument. Stop244's unpaid signed
correlations, stop279's interval/PNT mismatch, and unfinished
inverse work271 are preserved. There is no retry of the Coffey2007
retrieval or new claim about zero-free regions, so no quasi-RH
baseline reassessment is invoked.

### Decision and distinct bounded continuation

No inspected theorem provides the requested actual finite-cluster
extraction with an independently verified holomorphic complement.
The common-domain and compact-uniform-height requirements are now
explicit, but assuming them would merely rename the unresolved
cancellation problem. Park that direct import/test. This is a
source-scope negative, not a proof of a natural boundary, impossibility
of isolation, or absence of a theorem anywhere in the literature.

The independently testable continuation replaces F in both branches
of L994(4) by the rational principal parts of one complete hypothetical
off-line symmetry quartet. It asks whether the transform itself
can erase its singularities; it requires no assertion about the
complement of the actual G pair. The precise prospective target and
source scope are in
[the finite-pole response nomination](2026-11-10-rational-quartet-response-review-285.md).
It is a new nomination requiring separate approval, not mathematics
performed in this turn. Success would supply a necessary detector
ingredient only; actual complementary holomorphy, signed outputs,
L993 recovery and L984(H) remain independent unpaid steps.
Full matching Mathlib coverage is unchecked and unknown.
