# Optimal absolute-cycle normalization — primary-source comparison

TARGET: Assess whether optimality and semistable Manin-constant theorems give a finite twist-free normalization certificate from L029's full-relative line and the integral absolute-cycle lattice, retaining real-component and isogeny factors.
CHECKED: 2026-10-10
DECISION: IMPORT
SEARCH_EVIDENCE: Searched optimal quotient/connected kernel/integral homology/period lattice and modular-symbol normalization/gcd terminology; compared L028/L029/L038/L040, the exact-normalization assessment and ATTEMPTS/023--024; inspected the primary integral boundary theorem, optimal-period equality, both real-lattice cases and direct period integration with its tail bound.
SOURCE_EVIDENCE: Stein GSM 79 (2007), equation (3.2.1) and Theorem 3.7 p.40; Cremona corrected second edition (1997), Proposition 2.2.3 pp.16--17, Section 2.8 p.30, Section 2.10 pp.33--35 and Propositions 2.10.1--2.10.2; Cremona appendix to Agashe--Ribet--Stein, equality before Proposition 5.1, Proposition 5.1 with proof and Theorem 5.2; Cesnavicius arXiv:1703.02951v3, Theorems 2.11/2.13 pp.8--9 with proofs; Wuthrich arXiv:1608.06423v2, Section 2.2 and Lemma 4 p.6 with proof.
COMPARISON: The integral-period mechanism is already known: optimality identifies the full period image, semistability supplies absolute Manin constant one, and Cremona explicitly states the total-period factor for both lattice types. L029 additionally identifies the entire relative line. Independent exact optimal-model identification and an orientation witness remain essential.
GAP: Source coverage is adequate for a restricted finite certificate; construction and replay of the integral boundary kernel, its rational functional image and an independent sign enclosure remain unperformed. No arbitrary-curve optimality certificate or nonoptimal isogeny-period transfer is supplied.
REASON: The comparison replaces the unreviewed integral-image premise by a published optimal-period equality and covers both real-component cases; no new formula or normalization production is claimed.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; its integral-image/total-period scope lay outside the ready twist-calibration assessments.
SCOPE: Non-CM semistable X_0(N)-optimal E/Q with independently certified exact conductor, global minimal equation and exact optimal-curve identification; L029's entire relative line and L038's complete torsion-free integral presentation; allow L(E,1)=0. No twist value, rank or Sha premise. Nonoptimal transfer requires separate coverage and explicit differential/period factors.

## Gap, relevance and test

The main gap remains rank E(Q)=m(E) for arbitrary analytic order at least
two. The intermediate target is finite normalization of the entire relative
real-integration functional using absolute integral periods. Its plausible
use is removing independent twist-value retrieval from L027's coefficient
pipeline on the certified optimal semistable subclass. Coefficient
nonvanishing, rational points, Sha and complex-order comparison remain
independent gaps. No BSD candidate exists.

Continue only with the full integral boundary kernel, its exact functional
image, independent identification of the optimal minimal model, and an
oriented nonzero-period witness. Rational kernels, integral plus
eigensublattices, isogeny-class labels or periods inferred from the desired
normalized symbols fail the test. Stop the affected construction if any
required identification or index is uncertified. A concrete conductor-eleven
test can use L039 and L040's already imported optimality input, excluding
L040's twist ratio. No lattice or period computation is performed here.

## Inspected primary results and qualifications

**Integral absolute homology.** [Stein, *Modular Forms, a Computational
Approach*, GSM 79, 2007, equation (3.2.1) and Theorem 3.7,
p.40](https://wstein.org/books/modform/stein-modform.pdf#page=54)
identify the torsion-free relative module with integral relative homology
and its boundary kernel with H_1(X_0(N),Z), citing Manin (1972), Theorem
1.9. The boundary sends {alpha,beta} to [beta]-[alpha] in the free group on
cusp classes. Example 3.9, p.41, gives an integral N=11 basis; that example
does not replace replay in L039's different basis. No Manin reproof is needed.

**Optimal period image.** [Cremona's appendix to Agashe--Ribet--Stein,
*The Manin constant*, before Proposition 5.1](https://wstein.org/papers/ars-manin/html/node13.html)
explicitly states c Lambda_f=Lambda_E for the identified optimal quotient.
Lambda_f uses all integral absolute cycles; Lambda_E uses the minimal
Neron differential. Import this full-lattice equality, rather than
deducing it from rational homology surjectivity.

The appendix's Proposition 5.1 and complete proof give a finite
two-period optimality comparison with epsilon=B^(-1), conditional on a
complete isogeny class and rigorous period enclosures. Theorem 5.2 imports
published optimal-label identification at N<60000, with exception 990h.
L040 retains that computational-source qualification at N=11. A general
complete-isogeny-class/optimality implementation is not supplied here.

**Minimal differential.** [Cesnavicius, *The Manin constant in the
semistable case*, Compositio Math. 154 (2018), 1889--1920;
arXiv:1703.02951v3, Theorems 2.11/2.13,
pp.8--9](https://arxiv.org/pdf/1703.02951v3#page=8)
requires a new optimal elliptic quotient at the exact conductor N.
It gives ord_p(c)=0 when p^2 does not divide N, including p=2.
The introduction explicitly records absolute Manin constant one for
squarefree N. Its proof uses integral Neron pullback and Lie-surjectivity;
it does not identify an arbitrary isogenous curve as optimal. Optimal
means connected kernel. No higher-dimensional generalization is used.
The requested version is v3 (arXiv metadata: 26 April 2018); the retrieved
PDF displays 14 July 2021. These are the inspected theorem numbers.

**Real components and the full integral image.** [Cremona, *Algorithms
for Modular Elliptic Curves*, corrected second edition (1997), Section
2.8, p.30, definition following (2.8.9)](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=24)
states that the total real period is twice the least positive real
period in the rectangular case, and the least positive real period in
the nonrectangular case. It explicitly states that in both cases it is
twice the least positive real part of a full period. Section 2.10,
pp.33--34, (2.10.1)--(2.10.2), computes the full integral period image
using integer lattice arithmetic. Section 2.1.3, p.11, warns that integral
plus/minus eigensublattices may not generate all integral homology.

Proposition 2.2.3, pp.16--17, supplies finite cusp-equivalence tests;
its complete Bezout-lift proof was inspected. Propositions 2.10.1--2.10.2,
pp.34--35, with the vertical-integration proof, give direct convergent
Fourier evaluation of an oriented absolute period represented by a
Gamma_0(N) matrix, independent of central or twist nonvanishing.
These known algorithms need local lattice and orientation bookkeeping;
no reproof is justified. No specialization formula is derived this turn.

**Sign, tail and isogeny limitations.** [Wuthrich, *Numerical modular
symbols for elliptic curves*, arXiv:1608.06423v2, 23 March 2017,
Lemma 4, pp.5--6](https://arxiv.org/pdf/1608.06423v2#page=6)
bounds direct Fourier truncation at height y>0: truncation beyond
T(y,epsilon)=-log(2 pi y epsilon)/(2 pi y) has absolute error below
epsilon. Its complete proof bounds all omitted coefficients by a
geometric series. Outward finite-sum and elementary-function errors must
also be enclosed; a tail bound alone cannot certify a sign. No sign was
evaluated here.

Section 2.2, p.5, expressly records an index-two optimal-curve ambiguity
when only plus symbols are used. Section 2 and Proposition 2, pp.2--5,
retain Neron-period ratios and real-component changes for nonoptimal
models. The exceptional 2-isogeny cases and proof were read as exclusion
evidence. These ratios are not set to one for arbitrary E; the restricted
proposal uses an independently identified optimal model. Transferring
normalization to another isogenous curve is outside this approval.

## Comparison, source access and Mathlib

Queries included `optimal elliptic quotient connected kernel integral
homology surjective period lattice modular symbols Cremona` and `modular
symbols normalization gcd integral homology real period Cremona sign`.
The matched algorithm is known mathematics; no novelty is claimed.

The exact-symbol assessment approved twist calibration and correctly
warned that absolute cycles alone leave relative paths unidentified.
L029 supplies the entire relative line, while its scalar remains unknown.
ATTEMPTS/023--024 retain their production stops. The new proposal changes
the scale input and tests actual finite evidence instead of repeating
those conditional audits. No cross-notebook theorem is used.

Primary hypotheses and essential cases above were read, not inferred
from abstracts or snippets. A PDF screenshot timed out and shell DNS
prevented a redundant download; complete relevant statements and proof
text were accessible through the web tool, so there is no essential source
blocker. No downloaded source artifact or mathematical script was produced.
Full matching Mathlib coverage is not checked; this is unknown availability,
not absence.

IMPORT concerns the known source mechanism. The changed-basis certificate,
integral boundary kernel, full-relative specialization and sign replay
remain future work. The separate concrete SPECIALIZE assessment is saved
for next-turn approval. No new lemma, scale, denominator, coefficient or
rank claim is established by this review.
