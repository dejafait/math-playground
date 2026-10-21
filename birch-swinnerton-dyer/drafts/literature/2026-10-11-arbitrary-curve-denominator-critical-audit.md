# Arbitrary-curve denominator bound — approved critical-audit coverage

TARGET: Critically audit L048's arbitrary-curve full-relative denominator bound, checking the existential degree/scalar bound, all cusp endpoints, both real-lattice cases and the independently computable clearing integer.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the prior exact-target discovery and source comparison; checked ATTEMPTS/022--024 and history/157--159; located Stein definitions and Propositions 3.10--3.11/Theorem 3.13 in the primary author PDF to complete integral-relative scope coverage.
SOURCE_EVIDENCE: Reused prior inspected inputs: Cesnavicius--Neururer--Saha Theorems 1.2/7.2 https://maths.qmul.ac.uk/~asaha/research/manin-paper.pdf#page=45; von Kanel Sections 4/5.2 and Lemma 5.1(i) https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/tlms/tlu003; Wuthrich v2 Proposition 1 proof https://arxiv.org/pdf/1608.06423v2#page=3; Cremona second edition Section 2.8 p.30 https://johncremona.github.io/book/fulltext/chapter2.pdf#page=24; newly inspected Stein (2007), Sections 3.2--3.3 pp.39--44 https://wstein.org/books/modform/stein-modform.pdf#page=53.
COMPARISON: Known sources cover the retained arbitrary-target hypotheses and integral relative generation; authorize checking L048's assembly and applicability, not reproving imported theorems. Wuthrich's conditional displayed denominator formula remains excluded.
GAP: Source approval is complete; the independent mathematical audit of L048 remains pending, including its numerical factors and computability. Exact normalized values and BSD inference remain absent.
REASON: Separate literature review approves the saved audit target after reusing ready theorem coverage and inspecting the additional integral-generation citation; this does not certify the L048 assembly.
LITERATURE_REASON: The newly written audit assessment required separate approval; Stein's explicit integral-generation citation in L048 needed a primary passage check beyond the four-source assessment.
SCOPE: The full L048 statement, arbitrary global minimal E/Q including CM/additive reduction, certified exact N/newform, all relative paths, zero values and both real-lattice cases; no supplied optimal equation or isogeny map.

The initial proposal is retained below as audit instructions; separate
literature approval was completed on 2026-10-11. Preserve the prior
RESEARCH outcome independently of this approval. This file approves
source coverage only; the mathematical audit has not been performed. Reuse the existing [source comparison](2026-10-11-effective-full-relative-denominator-bound.md)
and [approved specialization coverage](2026-10-11-arbitrary-curve-denominator-specialization.md)
for source statements and access qualifications, including the unread
original Kenku proof and the conditional Wuthrich displayed formula.
Additional browsing is justified only by a specific essential unread
hypothesis or newly identified source discrepancy.

The audit should inspect the canonical L048 proof in full: exact-level
optimal quotient degree; bounded existential isogeny; integrality and the
unconditional factor six for the composite scalar; cusp fields and good
split-prime torsion injection including prime-primary torsion; both
endpoints; real projection versus purely real periods; full integral
relative generation; and size versus divisibility in the lcm consequence.
No local lemma is a direct mathematical input to L048; L027 is downstream
and L028/L038 are convention comparisons. No cross-notebook result is used.

Continue if all of L048 follows from these inputs with independently
computable data. Repair a precise flaw or record an obstruction if any
step requires an unavailable map, unknown normalized scale, unproved
optimality or an absolute-cycle-only premise. Independent finite
integration enclosures, exact recovery, coefficient nonvanishing,
rational directions, Sha and complex-order comparison remain unresolved.
Mathlib coverage is not checked, and no absence claim is made.


## Separate source approval — BSD-2026-10-11-160

Read L048 in full to identify its actual imports, without testing or
certifying its assembly. The four-source comparison and its separate
specialization approval remain adequate for the unchanged degree,
classification, differential, cusp and period hypotheses. No re-browsing
of those ready inputs is needed. Kenku's original proof remains unread;
the named classification is imported through von Kanel's inspected
argument. Wuthrich's displayed conditional conclusion remains excluded.

New primary reading: Stein, *Modular Forms, a Computational Approach*,
GSM 79 (2007), author PDF, Sections 3.2--3.3 pp.39--44 (PDF pages 53--58).
Definitions quotient ordered cusp symbols by triangle relations, group
action and torsion, and identify the result with relative homology.
Proposition 3.10 describes right cosets; Proposition 3.11 gives integral
cusp-symbol generation for every positive N. Read both generation proofs
in full. Theorem 3.13 states the integral presentation modulo torsion;
its proof supplies surjectivity and relation checking, with injectivity
referred to Manin (1972), Section 1.7, not proved in this book. That
original proof was not read. The named theorem is imported; L048 needs
integral generation, not a new presentation proof or software certificate.
This source fits weight two, trivial character and the full relative
module; an absolute-cycle restriction is not imposed.

The additional reading closes source coverage for an existing citation;
it creates no new lemma and establishes no result beyond the sources.
ATTEMPTS/022--024 concern repeating conditional audits as input
production. This first audit of the newly assembled arbitrary bound is
not another fixed coefficient audit and does not reopen those stopped
routes. No cross-notebook input is used. Mathlib remains not checked.

The exact approved action is the TARGET above. Required input is the
full canonical L048, the retained four-source comparison and this
integral-generation passage. L028/L038 are convention comparisons and
L027 is downstream, not direct mathematical inputs. The main gap remains
rank equality for arbitrary analytic order at least two. A successful
audit would validate a denominator input for later independent enclosure
and rational-isolation work. Continue only if every bound and both
endpoint/lattice cases survive independently; repair or stop on a precise
failure involving unavailable maps, unknown scale or unsupported
hypotheses. No exact recovery, coefficient nonvanishing, rational
membership, Sha finiteness or complex-order comparison follows from
source approval. These remain unresolved and the status is IN_PROGRESS.
