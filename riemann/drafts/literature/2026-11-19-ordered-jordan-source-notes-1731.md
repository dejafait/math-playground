# Ordered Jordan-sign source review1731

Completed review, 19 November 2026. Literature only; no exclusion
theorem or specialization has been derived. Target remains exactly
review1730's ordered-sign finite Borel annihilator question.

Local interfaces inspected: C032m's hypotheses/conclusion and signed
integration section; C032q's hypotheses/conclusion and source imports;
C033g's hypotheses/conclusion. Reused source-notes1709's Musin scope.
Scoped duplicate searches found no recorded matching Borel application.
Read stops1534/1536/1711 and park1725; their conclusions remain unchanged.

## Inspected primary theorem

Moshe Shaked and J. George Shanthikumar, *Stochastic Orders*, Springer,
2007, first edition, DOI
[10.1007/978-0-387-34675-5](https://link.springer.com/book/10.1007/978-0-387-34675-5).
Inspected Note p.1, Section1.A definitions pp.3-4, Theorem1.A.1 and its
complete proof p.5, and Theorem1.A.8 and its complete proof p.8 in the
[reproduced book pages](https://www.slideshare.net/slideshow/stochastic-orders-1st-edition-moshe-shaked-j-george-shanthikumar-eds/279576121).
The publisher's [preview pp.3-4](https://page-one.springer.com/pdf/preview/10.1007/978-0-387-34675-5_1)
independently supplies the definitions. The full publisher PDF requires
subscription; nzdr mirrors failed. Text of the complete relevant proofs
was inspected, not merely search snippets. Image links returned no
inspectable image; shell image retrieval failed DNS. No visual check
of the scans is claimed.

Theorem1.A.1 characterizes stochastic order by an almost surely ordered
coupling; its quantile construction allows arbitrary distributions.
Theorem1.A.8 says ordered laws with equal expectations of a strictly
increasing function are equal. Its proof treats the identity test via
that coupling, then applies the identity case to the transformed laws.
Use only finite expectations. The Note assumes expectations exist;
an equality of infinite values is insufficient for this application.
There is no density hypothesis in these statements. No theorem about
the zeta kernel is supplied by the book.

## Reused measure input and scoped comparison

Reuse the inspected Bass2011 Theorem12.8/p97 Jordan decomposition
from sources1542, including mutual singularity and finite variation;
do not promote its signed-integration exercise to a theorem with a
supplied proof. Source-notes1709 already establishes Musin's density
scope, so no new Musin comparison or Gaussian-minor replay is needed.

The source comparison supports SPECIALIZE for the unchanged target,
not IMPORT of the kernel-specific exclusion. A future proof must:

- identify the two real kernel tests using the qualified C032m/C033g
  conventions and justify their integrals against both Jordan parts;
- handle a vanishing Jordan mass before any division, and otherwise
  check finite positive weighted masses and their normalization;
- establish the required order for the normalized laws for every cut,
  assigning its atom to its actual Jordan part, including cuts 1 and2;
- verify strict monotonicity of the proposed ratio test, its finite
  expectations, and any needed extension from [1,2] to the real line;
- check the equality conclusion against mutual singularity, including
  measures concentrated at the cut, without adding a density condition.

These are the unpaid applicability obligations, not a derivation of
their conclusion. General measure theory plus the inspected equality
theorem covers the essential source scope for testing them. This is
a routine specialization of known mathematics, with no originality
claim. Quantitative separation from zero in a measure norm, more sign
changes, unrestricted cancellation, output positivity, moments and
actual-Xi realization are outside the assessment.

## Discovery and nonessential leads

Queries: `Chebyshev system signed measure at most n sign changes
orthogonal measure theorem`; `signed measure one sign change strictly
monotone function zero integral theorem`; `Tchebycheff systems signed
measures sign changes annihilating moments`; exact Gierz--Shekhtman
title; `Shaked Shanthikumar stochastic orders theorem 1.A.1 strictly
increasing expectation pdf`; and `Stochastic Orders 1.A.8 filetype:pdf`.
No exact nonlinear-kernel result was located in this bounded search;
that is not evidence of novelty.

Search lead Gierz--Shekhtman (1988), Proposition 6, concerns annihilating
Borel measures; DOI and publisher PDF fetches failed. Its indexed
open-interval sign convention needs care with atoms. Not imported.

Pinelis, arXiv:1107.3493v1, was opened as a general moment-space lead;
no load-bearing theorem was extracted. Sbert et al., *Stochastic order
and generalized weighted mean invariance*, repository version, was
checked at Section2's scope: finite-support sequences. It is not used
for arbitrary Borel laws. Neither lead is needed after the book's
general-law equality theorem was inspected. No source blocker remains
essential to this bounded target.

Matching Mathlib coverage is unchecked/unknown. No formal theorem is
asserted absent. No lemmas, mathematical scripts, PROOF or DAG changed.

## Direct-URL recovery1732

19 November 2026; literature-only metadata repair. The ready assessment
had referred to these notes without carrying a direct URL in its own
SOURCE_EVIDENCE field. That field now contains the publisher chapter,
the actual reproduced primary-text access URL, the definition preview
and the Bass extract. The saved target, SPECIALIZE decision and unpaid
applicability obligations are unchanged; no new exclusion is asserted.

Reopened the publisher book record and its chapter link (edition2007,
chapter pp3-79), the reproduced book text at Theorems1.A.1/1.A.8, and
Bass's complete Theorem12.8 proof and total-variation definition p97.
The publisher preview returned a web-reader access error this turn;
the earlier inspected definition/proof coverage is reused, not withdrawn
or upgraded to publisher-full-text access. The reproduced book text
remains available; no image inspection is claimed. No essential new
source blocker was found. This is a process repair, not fresh theorem
coverage or mathematical progress; outcome STALLED is intentional.
