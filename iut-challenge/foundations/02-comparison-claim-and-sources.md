# Comparison claim under audit

## Exact source anchor

[Mochizuki, IUT III](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf), author-hosted PDF headed May 2020, 199 pages; the [author's list](https://www.kurims.kyoto-u.ac.jp/~motizuki/papers-english.html) dates this version 2020-05-18. Page numbers below are this PDF's printed numbers, not journal pagination. Accessed 2026-09-24.

Corollary 3.12, pp. 173–174, assumes Theorem 3.11: initial Θ-data of IUT I, Definition 3.1, and an LGP-Gaussian log-theta-lattice of IUT III, Definition 3.8(iii). These are retained in full by reference, not replaced by arbitrary valued-field data.

Set A = −|log(q)| < 0 and B = −|log(Θ)|. These are the corollary's procession-normalized mono-analytic log-volumes, not ordinary absolute logarithms. B is computed from the holomorphic hull of all possible Θ-pilot images under the relevant Kummer isomorphisms, with (Ind1), (Ind2), (Ind3); A uses the q-pilot without those indeterminacies. The claim is B ∈ ℝ and B ≥ A. For finite B, the inequality equivalently says every real C_Θ with B ≤ C_Θ |log(q)| satisfies C_Θ ≥ −1.

The selected inference is (xi-e) to (xi-f), pp. 183–184: input-volume membership in the output range. Remark 3.11.1(vi)–(viii), pp. 163–166, already discusses naive power maps. Its (iii), pp. 160–161, specifies comparison arrows via Remark 3.10.2.

## Prior critique and response

[Scholze–Stix, Why abc is still a conjecture](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf), author-hosted ten-page PDF bearing the date July 16, 2018, §§1.3 and 2.1.8–2.2, particularly pp. 9–10, identifies the abstract/concrete normalization issue and argues that their consistent comparison loses the j² gain. This is a prior argument, not a new result of this notebook. Their simplifications are not assumed to preserve every IUT hypothesis.

[Mochizuki, September 2018 comments on the August 2018 Scholze–Stix manuscript](https://www.kurims.kyoto-u.ac.jp/~motizuki/Cmt2018-08.pdf), (C10), (C12)–(C14), pp. 3–4, disputes the treatment of ring structures and of indeterminate regions. In particular, (C14) distinguishes scalar comparisons of degree lines from the nonlinear effect of indeterminacies on region volumes. This response identifies obligations for a faithful test; citing it does not prove those obligations are met.

## Quotient anchors checked on 2026-09-25

[Remark 3.9.5(v)–(vi), pp. 129–130](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf#page=129), collapses S ⊂ E to a point and applies this to the output hull. The stated criterion for equal images concerns **distinct** hulls both contained in S. Formal empty intersections are treated separately.

[Remark 3.9.5(ix), (cQ3)–(cQ4), pp. 141–143](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf#page=141), retains categories with structure poly-morphisms to the output determinant and applies log-Kummer transport before taking log-volumes. Loop closure is qualified by formal quotient indeterminacies. These categorical identifications have not been verified here; a collapse of sets cannot simply replace them.

## Scope of the audit

The exact claim above is an object of investigation, not an accepted theorem used to prove itself. The full initial-data definition and all prerequisite constructions have not been checked. No full IUT instance is constructed here. There is consequently no inference from a reduced example to falsity of Corollary 3.12.

## Mathlib

Full IUT comparison statement: **not checked**. Supporting library results: **not checked**. No claim of absence is made, and no formal verification is claimed.
