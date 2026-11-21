# Probability-law continuity: primary source notes1539

18 November 2026. Literature only; no application to the width family
is proved here. These are standard results, not a novelty claim.

## Laplace convergence and normalization

Ante Mimica, *Laplace transform*, Dresden course notes,
27 April–1 May 2015, [author PDF](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
Read Theorem 2.1 and complete proof, printed pp11–13, Corollary 2.2
and complete proof/p13, Proposition 1.4(ii) and proof/pp6–7, and
the uniqueness statement of Proposition 1.8/p9.

Corollary 2.2 concerns probability measures on [0,infinity). Pointwise
convergence of their Laplace transforms at every positive parameter,
with limit phi satisfying phi(0+)=1, gives a probability measure with
that transform and distribution-function convergence at positive
continuity points. It assumes no density, moment bound or separate
tightness. The proof identifies total mass by monotone convergence.
The continuity theorem uses exponential tilting, Helly selection and
uniqueness. Normalization excludes escaped mass.

Qualification: the general proof contains apparent displayed typos
(shifted transform argument and integration-by-parts signs).
Corollary 2.2's mass reference to Proposition 1.4(i) should be (ii).
Import the standard probability corollary, not those misprinted formulas
or an arbitrary signed-measure version. No general proof repair or
source-wide verification is claimed.

## Distribution functions and weak convergence

Joel A. Tropp, *Probability Theory & Computational Mathematics*,
CMS/ACM117, Fall2024, typeset 23 January 2025,
[author PDF](https://tropp.caltech.edu/notes/Tro24-Probability-Theory-LN.pdf).
Theorem 17.22/p260 is the usual Helly–Bray criterion: for probability
distribution functions on R, convergence at every continuity point of
the limiting distribution function is equivalent to weak convergence
of the laws. Read its full statement, Theorem 17.39 and quantile-coupling
proof/p268, and Proposition 17.40's statement/p268. Its following-page
proof was not retrieved. Only the standard named criterion is imported;
no full-chapter audit is claimed.

## Borel evaluation and topology qualifications

Tobias Fritz, Paolo Perrone and Sharwin Rezagholi, *Probability,
valuations, hyperspace: Three monads on Top and the support as a
morphism*, [arXiv:1910.03752v3](https://arxiv.org/pdf/1910.03752v3),
16 September 2021 submission, PDF dated 17 September 2021.
Read Definition 4.1/p39, Definition 4.6 and Proposition 4.7 with
complete proof/pp41–42, Proposition 4.10 and complete proof/p43,
and Section4's Polish-space qualification/p39.

P X consists of tau-smooth Borel probability measures with the
A-topology. Proposition 4.7 identifies this with the topology of
integration against bounded continuous real functions for completely
regular Hausdorff X. Probability measures on Polish spaces are covered.
Proposition 4.10 makes evaluation at every Borel set Borel measurable.
Its proof starts with lower semicontinuity for open sets, then uses
disjoint countable unions, nested-set differences and the pi-lambda
theorem. It asserts no continuity at arbitrary Borel sets, and needs
no density or finite moments. The versioned PDF fixes the citation;
generated HTML displayed an inconsistent later date and is not used.

## Local comparison and future applicability work

Ledger1528 and the compact-width/smoothed-law assessments distinguish
scalar holomorphic integration from probability-kernel measurability.
C032m supplies the former. Finite stop1302 and C032o's growth stop
remain; neither decides this probability contract. The large MIT
source was not retried. No cross-notebook input was read.

The future audit must retain C032j's probability-law and fixed-v1
qualifications, use C032k for identification and zero normalization,
and check C032m's transform input for every convergent width sequence,
including endpoints. Check the half-line/R topology interface and
continuity at zero without asserting convergence of every atom.
Check the Polish/completely regular hypotheses before using evaluation.
These are ordinary applicability checks, not a new mechanism. No
application, signed-mixture construction, positivity or moment claim
is made here. Full matching Mathlib coverage is unchecked and unknown.

## Search/access record

Queries included `probability Laplace transform continuity theorem
nonnegative random variables lecture notes theorem proof`;
`probability measures weak topology evaluation map Borel measurable
theorem lecture notes`; `"evaluation maps" "measurable" "Proof"
probability measures weak topology pdf lecture notes`;
`"Probability, valuations, hyperspace" pdf`; and `"weak convergence"
"distribution functions" "Proof" lecture notes pdf`.
Later queries selected the named source statements/proof cases above.

Geng's Theorem4.1, Feller II XIII.1 Theorem2/p431 and Orbanz's
evaluation exercise were leads, not essential proof coverage: Geng's
relevant proof was not retrieved; the Feller scan returned no readable
text or visible screenshot; Orbanz's item is an exercise. Bell's note
supplied no full evaluation theorem and is not imported. Several web
follow-ups timed out; one local arXiv download failed DNS resolution.
The inspected primary alternatives resolve the essential scope without
relying on these failures. No novelty follows from the search.
