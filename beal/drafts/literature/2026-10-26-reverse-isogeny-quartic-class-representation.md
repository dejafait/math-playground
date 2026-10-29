# Reverse connecting classes: coefficient image and its obstruction

TARGET: Determine whether every rational G-connecting class of L142 lies in the image of A_4*/(Q* A_4*²) in H¹(Q,ker G), and identify the obstruction if not.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the split-kernel assessment, audited L142/L127 and ATTEMPTS/062; searched explicit descent quotient Brauer obstruction, Poonen–Schaefer cyclic covers, and Prym isogeny fake descent; followed primary references to Bruin–Poonen–Stoll Sections 3,4,6.
SOURCE_EVIDENCE: Read Bruin–Poonen–Stoll https://math.mit.edu/~poonen/papers/genus3.pdf Section 2 p.5, Section 3 p.6, Section 4 pp.6–8, Definition 6.7/Remark 6.8 p.16, Section 6.3 and Proposition 6.10 with complete proof pp.17–20, Proposition 6.14/proof pp.20–21 (74-page author manuscript); Poonen–Schaefer https://math.mit.edu/~poonen/papers/descent.pdf diagram (12) p.15, Theorem 9.4/proof and Corollary 9.5 pp.16–17; Antieau–Auel https://math.dartmouth.edu/~auel/papers/docs/AA_g1c.pdf Theorem 3.18 proof pp.18–19; Docking arXiv:2108.09564v2 Section 2 p.4 for the dual map, reusing assessed kernel cases.
COMPARISON: The exact coefficient image is a Brauer-boundary kernel, not all of H¹ by formal quotient manipulation. Generalized descent includes arbitrary smooth projective geometrically integral varieties and their Albanese, hence supplies a framework for products; equality with actual δ_G still needs checked instance data and map identification.
GAP: Specialize the coefficient sequence to L142 and verify product divisor data, dual-kernel embedding and connecting-map normalization to decide whether the obstruction vanishes on all rational G-connecting classes; neither vanishing nor an actual evaluation formula is proved here.
REASON: Essential source coverage now supports one bounded known-theory specialization; the remaining work is mathematical applicability rather than another search. No inspected theorem states the exact marked instance, and no novelty is claimed.
SCOPE: Exactly TARGET for L142's actual G, origins and quartic algebra; permits finite cohomology/divisor specialization and its evaluation interface, but no class enumeration, Selmer implementation, rank bound or point search.

## Pre-review proposal, retained scope rather than a proved result

The following is the original proposed test. Its prospective source-review
instructions record the pre-review state; the current gate above and
the completed source comparison below supersede that state.

Here A_4=Q[T]/(Q4) with Q4 exactly as in L142. The proposed arrow
is the one induced by the quotient of finite coefficient modules in
that lemma. Its domain notation means quartic units modulo rational
scalars and squares. The next source review must justify that arrow's
cohomological interpretation and determine its image, rather than
assume the quotient operation commutes with first cohomology. In
particular any degree-two cohomology/Brauer obstruction and any
special vanishing for rational G-images must be checked, not discarded.
No such vanishing is asserted here.

The main gap remains point control in the residual Beal systems.
The intermediate use would be an exact coefficient interface for a
later compatibility test on independently retained quotient classes.
This is a different question from imposing an extra condition after
exact same-T point equations: ATTEMPTS/062 already stops that shortcut.
Representation alone would still give no extra exclusion or rank gain.

Begin by reusing the recorded Schaefer comparison, retrieving only
essential primary statements about the relevant coefficient sequence
and product-target connecting images. Search exact terminology and
stronger results before approving a specialization. Treat generalized
descent or Brauer results as unread leads until their hypotheses are
inspected. Neither a citation about descent to a single Jacobian nor
the finite module identification alone settles this target.

The bounded continuation test is a precise theorem-backed image or
obstruction criterion applicable to the actual δ_G. Continue only if
it makes the later class test independently evaluable or identifies a
specific missing hypothesis that can be tested. Do not substitute an
identity for exact same-T points, assume a class basis, or launch a full
Selmer implementation. If sources are essentially missing, preserve
that blocker rather than derive uncovered mathematics in the review.

Essential inputs are L142 and L127 for G and its Q-defined maps,
L110/L111/L113 for the actual curves and origins, and L138 for the
quartic algebra transport. L139–L141 supply the existing bound only;
their local images are not already product-isogeny images. Unresolved
obligations include representation, an evaluation formula, mixed-class
nonredundancy, full descent, Abel-image membership, point control,
degree-nine/integer recovery, both L095 systems and other signatures.
No cross-notebook input is proposed. Mathlib coverage is not checked.

This is not yet a creative proof target: a new exclusion mechanism has
not been justified. The immediate route is theorem comparison; only a
concrete nonredundant detector with its own bounded test would justify
a later creative attempt. This proposed assessment requires separate
review and supplies no ready mathematical gate.

## Completed source comparison — 2026-10-26

**Imported coefficient criterion.** For a field k of characteristic
prime to n and nonempty finite étale Δ=Spec L, Bruin–Poonen–Stoll,
Section 6.3.3, equation (8), gives the exact sequence

    k*/k*ⁿ → L*/L*ⁿ → H¹(k,μ_n^Δ/μ_n) → Br(k).

Consequently L*/(L*ⁿ k*) embeds and its image is exactly the kernel
of the last arrow. The arrow comes from the diagonal μ_n coefficient
sequence, with H²(k,μ_n)=Br(k)[n]. Section 3 supplies finite étale
Kummer theory. This is a cited general statement, not a computation
of the boundary on δ_G. Antieau–Auel, *Explicit descent on elliptic
curves and splitting Brauer classes*, author version 21 July 2021,
Theorem 3.18 proof pp.18–19 independently displays the same sequence
for a chosen étale extension splitting a Brauer class. It does not
give vanishing for the present connecting images.

**Applicable generality and exact hypotheses.** N. Bruin, B. Poonen
and M. Stoll, *Generalized explicit descent and its application to
curves of genus 3*, Forum Math. Sigma 4 (2016), e6, DOI
https://doi.org/10.1017/fms.2016.1. The inspected author PDF is
74 pages, with publication placeholders on its title page; all page
numbers here refer to that manuscript, retrieved 2026-10-26, not the
80-page published layout. Section 6.1 takes a smooth projective
geometrically integral X and J=Alb(X), not just a curve Jacobian.
Definition 6.7 requires n prime to char k, nonempty finite étale Δ,
and a line bundle on X×Δ whose nth power comes from X. In divisor
terms it requires β,D,f with div(f)=nβ−D×Δ. Proposition 6.10
compares degree-zero cycle evaluation with the cohomological map
induced by the associated dual-torsion map.

The complete essential proof was read: choice-independence of H,h
and nth roots, diagram (11), the square and Weil-pairing triangle,
and the final cohomology comparison. Proposition 6.14 and its proof
check the induced isogeny through the actual dual-kernel image and
functoriality of connecting maps. These results cover a product
Albanese setup but do not construct this notebook's setup for it.
Cycle representability and the precise dual map are essential instance
obligations; abstract module dimensions cannot replace them.

**Narrower comparison.** B. Poonen and E.F. Schaefer, *Explicit
descent for Jacobians of cyclic covers of the projective line*,
J. Reine Angew. Math. 488 (1997), 141–188, DOI
https://doi.org/10.1515/crll.1997.488.141, author manuscript dated
10 February 1997: Theorem 9.4 compares evaluation on Pic^(p)(X)
with the cohomological map; Corollary 9.5 gives vanishing of its
Brauer composite. The proof uses the generalized-Picard diagram,
its surjectivity and Theorem 9.3. This single cyclic-cover Jacobian
statement cannot by itself settle the present product G. Schaefer's
corrected arXiv:1507.08325v1 Theorem 2.3 and Assumptions I/II retain
the previously assessed scope. The generalized framework removes
that source-scope restriction, with instance hypotheses still to check.

## Approved finite specialization and stopping boundary

Use L142's embedded kernels, actual origins and norm coordinates,
L127's F,G and both [2] composites, and L110/L111/L113/L138's actual
models and quartic transport. Docking, arXiv:2108.09564v2 (24 July
2023), Section 2 p.4 explicitly states the dual Prym isogeny.
Its transport through the actual elliptic Prym identification must
be checked if duality is used: L127 expressly imported no polarization
formula. Do not infer the required dual pairing just from GF=FG=[2].

The later attempt may test the generalized setup on B×E with Q4's
four branch labels. It must supply divisor/line-bundle data, match
the induced dual-kernel map with the embedded ker F, and identify
the resulting cohomology map with actual δ_G under the specified
coefficient identification. Alternatively, it may use a fully checked
functorial diagram with the factor Kummer maps. Rational cycle/divisor
representability, scalars, origins and exceptional evaluations must be
justified. These are future instance tasks, not derivations in this
literature step. Reprove none of the cited general theorems.

Continue if this proves representability on all rational target pairs,
or identifies an applicable obstruction with an independently testable
nonvanishing criterion. Stop an affirmative proof at any failed pairing
or cycle hypothesis and retain the precise missing condition. Abandon
an extra detector that only restates exact same-T lifting. Even an
affirmative representation theorem leaves mixed-class nonredundancy
against L138–L141, full descent, Abel-image membership, point control,
integer recovery and the other residual signatures unresolved. Thus
the main-gap use and limitations of the original proposal remain.

Queries included `isogeny Brauer Prym descent quartic`, `explicit
descent quotient Brauer hyperelliptic Schaefer`, `Poonen Schaefer
explicit descent cyclic covers projective line Brauer exact sequence
mu quotient`, and `Prym fake descent isogeny`. Searches do not establish
originality. Creutz's generalized-Jacobian work and Schaefer–Wetherell
remain unread leads, not essential inputs to this finite specialization.
No cross-notebook theorem is used. Mathlib matching coverage remains
unchecked; unknown availability is not evidence of absence.

Readable primary web text supplied all essential ranges. Two PDF
screenshots timed out and shell download failed DNS resolution; these
did not prevent source-text review. No source PDF, mathematical script,
lemma, DAG edge or argument-overview change was made. This assessment
now supplies source coverage, not a proof of TARGET. The supervisor
retains ownership of the next invocation's gate.
