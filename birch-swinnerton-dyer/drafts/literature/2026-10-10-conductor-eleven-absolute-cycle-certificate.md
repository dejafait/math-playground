# Conductor-eleven absolute-cycle normalization — proposed ready specialization

TARGET: Construct a twist-free normalization certificate for L039's conductor-eleven model using its full integral absolute boundary kernel and a rigorously enclosed nonzero absolute period to fix orientation.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed optimal-absolute-cycle source comparison, its exact normalization/gcd and optimal homology searches, and local L039/L040; ATTEMPTS/023--024 prohibit repeated conditional audits as production but do not settle this different finite test.
SOURCE_EVIDENCE: Reuse drafts/literature/2026-10-10-optimal-absolute-cycle-normalization.md: Stein (2007), equation (3.2.1)/Theorem 3.7 p.40 https://wstein.org/books/modform/stein-modform.pdf#page=54; Cremona corrected second edition (1997), Proposition 2.2.3 pp.16--17 and Sections 2.8/2.10 pp.30,33--35 https://johncremona.github.io/book/fulltext/chapter2.pdf; Cremona appendix, optimal-period equality and Theorem 5.2 https://wstein.org/papers/ars-manin/html/node13.html; Cesnavicius arXiv:1703.02951v3, Theorems 2.11/2.13 pp.8--9 https://arxiv.org/pdf/1703.02951v3#page=8; Wuthrich arXiv:1608.06423v2, Lemma 4 pp.5--6 https://arxiv.org/pdf/1608.06423v2#page=6. Complete relevant proof cases were inspected in the reused assessment; direct primary access was confirmed on 2026-10-10.
COMPARISON: The normalization algorithm and period-image statements are known; the permitted difference is exact specialization to L039's integral coordinates, complete boundary-kernel evidence, oriented absolute-period enclosure and all twelve relative generator values. No new optimality or homology theorem is sought.
GAP: The actual integral boundary lattice, its primitive rational image, orientation enclosure and resulting all-generator denominator remain uncomputed; the existing twist-normalized result is a comparison, not an input for recovering the scale.
REASON: A concrete finite instance can test normalization production using already imported model optimality, without the parked uniform twist-source retrieval or another purely conditional certificate.
SCOPE: Only E=[0,-1,1,-10,-20], N=11, L039's entire saturated relative lattice and real line; use L040 solely for its published optimality input, not its twist value. Retain minimal differential, full absolute homology, total real period, both factor-of-two conventions and an independent oriented sign witness.

The separate literature approval on 2026-10-10 repairs the missing direct
source URLs and retains SPECIALIZE for this exact target. No mathematics
or scripts have been executed under it. The approval changes no theorem
comparison or computational-source qualification.

The main gap remains arbitrary-curve rank equality at analytic order at
least two. This intermediate target supplies normalization/denominator
data for later L027 applications, with no coefficient nonvanishing,
point production, central vanishing or rank-two inference. It is a
known-method reproduction; no novelty is claimed.

## Permitted finite attempt and discriminating test

Use L039's certified presentation, endpoints, coordinate transforms and
functional, supported by L029/L038. Certify endpoint cusp classes using
Cremona Proposition 2.2.3, the integral boundary on every generator and
its descent through every saturated relation. Supply unimodular
normal-form witnesses for the complete kernel over Z. A rational basis
of the same dimension or a geometric-plus sublattice does not suffice.

Evaluate the unnormalized functional on every integral kernel generator,
with exact rational image/Bezout evidence for primitivity. Import the
optimal-period equality and semistable Manin theorem from the completed
review; explain why L039's exact minimal model meets the conductor and
squarefree hypotheses. L040's published optimality theorem is sufficient
with its existing computational-source qualification. Do not use its
q=5, L041's calibrated values or a guessed scalar to identify this image.

Choose an absolute integral cycle with nonzero functional value and
certify its oriented period by Cremona's direct Gamma_0(11) formula.
Grant no numerical sign: give complete Fourier coefficients, path/matrix
identification, an outward finite-sum enclosure and Wuthrich's full tail.
An interval strictly excluding zero is the orientation threshold.
A separate sign-free magnitude result must be labeled as such if the
bounded orientation attempt fails.

Only after those checks specialize the known total-period normalization
to the entire relative line; carry the resulting scalar through all twelve
integral generators, retaining every denominator and every prime.
Comparison with audited L041 may check the final output independently,
but cannot provide recovery inputs. Put full reasoning and citations in
one canonical lemma and full finite evidence under scripts/ only in the
later approved research turn; record relevant Mathlib coverage honestly.

Continue if the complete integral kernel/image and independently signed
scale agree with the full relative line and produce an all-generator
denominator. Stop the affected construction and retain evidence if a
nonprimitive lattice, factor of two, unidentified model, sign interval
containing zero or unexplained disagreement prevents certification.
Source theorems must be cited rather than reproved. No general
nonoptimal isogeny transfer is authorized: the exact optimal model
identification is why no unverified isogeny scale enters this instance.

Essential local inputs are L029, L038, L039 and L040's optimality import;
L028 supplies the generator-denominator convention. L027 is downstream,
and L041 is a final comparison only. No cross-notebook theorem is used.
Full matching Mathlib coverage is not checked.

## Separate source-link recovery review — 2026-10-10

The supplied continuation omitted direct source URLs even though its
completed parent assessment had them. This review adds the primary URLs
to SOURCE_EVIDENCE and reuses that adequate assessment; it does not
repeat its theorem search or claim a new mathematical input. Access to all
five primary documents was confirmed. Selected passages checked again
were Stein Theorem 3.7, Cremona Proposition 2.2.3 and Propositions
2.10.1--2.10.2, the two real-period cases, the appendix's full-period
equality and Theorem 5.2, and Cesnavicius Theorem 2.13. Wuthrich's
complete Lemma 4 proof coverage is reused from the parent assessment;
this turn's search also returned Lemma 5, which is not substituted for it.

The exact-model input remains L040's cited ecdata row
`11 a 1 [0,-1,1,-10,-20] 0 5` at
https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.00000-09999
with table conventions at https://johncremona.github.io/ecdata/.
L040's existing import and the published Theorem 5.2 supply optimality;
no new database replay, optimality proof or use of the rank column occurs.
L039's conductor/minimality certificate remains essential. Retain the
complete-isogeny-class/two-period computational qualification and every
orientation and full-integral-lattice requirement above.

LITERATURE_REASON: Supervisor-required direct-source-URL repair and separate approval of the saved specialization; existing theorem coverage is reused unchanged.

ATTEMPTS/023--024 are preserved: this future finite kernel/sign test is
actual input production by a different scale mechanism, not another
conditional twist-calibration audit. L041 remains only a final comparison.
No new matching Mathlib search was needed; full coverage remains unchecked.
