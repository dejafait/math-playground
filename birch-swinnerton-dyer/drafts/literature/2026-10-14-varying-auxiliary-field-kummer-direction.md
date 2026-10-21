# Auxiliary-field variation — completed source comparison

TARGET: Assess whether varying the auxiliary imaginary quadratic field in generalized Kato constructions can produce a nonzero strict rational Kummer class under L026's corank-two hypotheses, without assuming positive rational rank or finite Sha.
CHECKED: 2026-10-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Searches for varying imaginary quadratic fields, auxiliary independence and rationality of generalized Kato classes found Castella's non-CM Iwasawa-main-conjecture comparison; exact queries, versions and read ranges appear below. Reused the recorded exterior-certificate and fixed-field assessments.
SOURCE_EVIDENCE: Castella, author GKC-IMC.pdf dated 2024-06-20, Sections 2.3--2.4, equation (3.2), Theorem 4.2.1, Sections 5.1--5.4, especially Theorem 5.2.3 and equations (5.6)--(5.7), printed pp. 7--8, 10, 14--19; compared arXiv HTML locator 2312.01481 with displayed date 2026-08-24; rechecked Castella--Hsieh (2022), Theorems A/B, Remarks 1.6/1.8 and Section 5.7, printed pp. 4--6, 28--29.
COMPARISON: The newly inspected theorem makes nonzero rational Selmer localization necessary as well as sufficient for generalized Kato nonvanishing at Selmer dimension two, under its extra auxiliary hypotheses; its nonzero class spans the strict Selmer group. It supplies no point-membership comparison, and the inspected point-valued formula still adds finite p-primary Sha.
GAP: L026 supplies dimension two but neither nonzero localization nor rational Kummer membership. No inspected source makes auxiliary-field variation remove either gap without additional arithmetic input; existence of admissible auxiliary data is also not inferred for arbitrary L026 curves.
REASON: Park variation as a direct membership/nonvanishing-production route: the new necessary-localization statement gives a field-independent bottleneck in its covered scope. Propose a distinct cyclotomic local-condition comparison for separate review; do not repeat fixed-field scalar, height, determinant or torsor-transfer tests.
SCOPE: Source comparison only, with every auxiliary hypothesis retained. EXPLORE records the absence of an adequate inspected membership theorem, not approval of an unformulated calculation or a claim of novelty.
LITERATURE_REASON: The saved variation was REVIEW_REQUIRED and needed primary coverage of auxiliary choices and their rationality/nonvanishing scope; the earlier fixed-field and exterior assessments did not inspect Castella's necessary-localization theorem.

## Gap, intermediate target and decision test

The main gap remains rank equality for arbitrary analytic order at least
two. Under L026's additional arithmetic, central-vanishing, parity and
certified-coefficient hypotheses, one nonzero strict class in the rational
Kummer image would activate L005's rank lower bound. Those L026 premises
are retained, not produced from complex order two. L018's separate
residual-family hypotheses must not silently be inferred from L026.

The reviewed intermediate target was an actual nonzero strict class in
the rational Kummer image obtained through auxiliary-field variation.
Its downstream use was L005's rank lower bound, matching L026's upper
bound. The continuation test required a new arithmetic membership
comparison or an independent discriminating test; auxiliary nonvanishing
values, repeated local models and formulas assuming points do not meet it.
The test fails for direct import from the sources inspected below. This
does not assert impossibility of future geometric comparisons or BSD.

## Primary sources and precise qualifications

The principal new source is Francesc Castella, *Nonvanishing of generalised
Kato classes and Iwasawa main conjectures*, [author PDF dated June 20,
2024](https://web.math.ucsb.edu/~castella/GKC-IMC.pdf). Theorem 5.2.3 is on
printed p. 16; its hypotheses start on p. 15. Its construction is over a
chosen imaginary quadratic K, with p > 3 good ordinary for E and p split
in K. Retain the following additional source conditions:

- Residual absolute irreducibility; a prime q dividing the conductor N
  exactly once, with residual ramification at q if q = +/-1 mod p;
  and either p > 5 or residual image containing a conjugate of SL2(F_p).
- A prime ell not dividing 6pN, split in K and ordinary for E; q inert
  in K and every prime dividing N/q split. Retain the coprimality of
  the discriminant and character conductor with pN from Section 2.3.
- A ring class character chi of ell-power conductor with
  L(E^K,1)L(E/K,chi,1) nonzero, chi = psi/psi^c for the ray class
  character used in the dual primitive CM Hida families, and residual
  chi nontrivial at the chosen p-decomposition group as in (3.2).
  This last condition is retained explicitly even though Choice 5.2.1(6)
  prints nontriviality of chi itself.
- Positive even complex central order, and the paper's coefficient and
  projected-class conventions. For the notebook comparison retain
  the Q_p coefficient restriction; do not silently descend a class
  defined only over a larger coefficient field.

Theorem 5.2.3 states that nonzero kappa implies dimension two of
Sel(Q,V_p E); when that dimension is two, kappa is nonzero exactly
when loc_p on that Selmer space is nonzero, and then kappa spans its
strict kernel. Corollary 5.1.3 and Remark 5.1.4 give rational Selmer
membership and strictness, not membership in E(Q) tensor Q_p.

Essential proof cases were inspected before drawing the scope decision:
Section 5.4, pp. 18--19, uses auxiliary twisted-Selmer finiteness,
Theorem 4.2.1's anticyclotomic equality after inverting p, and Proposition
5.3.3's finite-error control. Equations (5.6)--(5.7) compare the actual
specialized class with the relaxed-strict Selmer rank. Lemma 5.3.1's
local-image cases supply the converse; the final paragraph explicitly
retains loc_p rather than replacing it by rational-point localization.
This is source proof inspection, not an independent audit or reproof.

Version caution: [the arXiv HTML locator](https://arxiv.org/html/2312.01481)
displays arXiv:2312.01481v1 but an internal August 24, 2026 date. It uses
GL2(F_p), rather than the author PDF's SL2(F_p), in (h3), and adds Remarks
5.2.4--5.2.5. Do not identify the two versions. The theorem conclusion
used for comparison occurs in both. L026's residual surjectivity meets
either image restriction, but no weaker-image application is made here.
The HTML's Remark 5.2.5 labels its displayed P,Q a **Selmer** basis;
its notation cannot supply a rational-point basis. Published Springer
pagination was not compared.

Reused [Castella--Hsieh coverage](../../foundations/07-castella-hsieh-nonvanishing.md)
was sufficient for the unchanged fixed-field theorem. The [published
2022 PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf)
was reopened specifically at Theorems A/B, Remarks 1.6/1.8 and Section
5.7. Theorem B adds positive rational rank; Section 5.7 adds finite
p-primary Sha before Theorem 5.5's point formula. Remark 1.8 and the
new source's Remark 5.2.2 discuss many auxiliary choices, not rational
membership. Their BFH90/Vat03 references were located but not read
directly in this step. No uniform auxiliary-existence theorem is imported;
the negative comparison grants all auxiliary choices for which the
inspected theorem applies, so those unread existence leads are not
essential to this decision.

## Applicability and comparison with recorded failures

L026's good ordinary prime, surjective residual representation, central
vanishing and sign agree with part of the source setting; its corank
two concerns the same rationalized classical Selmer group used in L005.
L026 does not supply a q dividing N exactly once, K, chi, their auxiliary
values or the coefficient-field condition. These remain additional
premises. Even granting them, the inspected theorem leaves loc_p as the
condition for nonvanishing and says nothing about the quotient q(kappa)
in L005's Kummer sequence. No theorem is specialized into a new lemma
during this literature-only turn.

The scope comparison is the useful negative evidence: for each admissible
choice the theorem refers to the same Sel(Q,V_p E), the same loc_p, and
its strict kernel. Thus the source supplies no field-choice escape from
the localization condition and no second point-valued comparison.
This inference is confined to the inspected theorem's auxiliary scope;
it does not refute field variation outside that scope or future rationality
results. Nonzero localizations on Selmer classes remain weaker than
membership of a strict class in the rational Kummer image by L006.

Duplicate/failure checks reused foundations/06--08, L005/L006 and the
[actual exterior assessment](2026-10-04-arithmetic-rank-two-exterior-certificate.md).
L010 already separates scalar Coleman order from full localization;
L013/L019 obstruct formal determinant/height promotion to rational
membership. L018 retains a possible divisible Sha quotient despite
compatible lifts; L020 requires actual global point realization and a
strict extension-degree threshold. ATTEMPTS/003, /004 and /020 preserve
the direct point import, positive-rank/finite-Sha, and equality-degree
failures. These do not become global bans, and no model is recreated.
The ordinary analytic-zero/one theorem in foundations/02 cannot be
substituted for the retained positive-even-order setting.

## Search, access and continuation

Queries issued on 2026-10-14:

- `generalised Kato classes varying imaginary quadratic field rationality rank two Castella Hsieh`
- `generalized Kato classes rationality auxiliary quadratic field rank two 2025 2026`
- `"generalised Kato" "varying" "field"`
- `"generalized Kato" "rationality" "rank" elliptic 2024 2025 2026`
- `"generalised Kato" "auxiliary" "independent"`

The author's publication page supplied the GKC-IMC.pdf link. Web retrieval
provided the theorem hypotheses and essential proof cases above; a local
curl download failed with DNS resolution, so no local PDF copy or checksum
is claimed. This is not an essential source blocker. The Rivero
exceptional-zero and Darmon--Rotger Stark--Heegner search hits were not
newly inspected as theorem inputs; earlier BSV and arithmetic-exterior
coverage remains reused. Failure to find a matching membership theorem
in this bounded search is not evidence of novelty or nonexistence.

Park the reviewed variation as direct membership production. The distinct
proposal is to examine the **cyclotomic** ordinary/strict Selmer comparison
at augmentation: can L026's TM=0 and two-dimensional specialization
force loc_p nonzero without rational rank or finite Sha? This tests a
global arithmetic input absent from the auxiliary-choice theorem, not
the already-tested height-radical surjection. Its plausible use would be
to settle the nonvanishing prerequisite for the inspected construction
under separately verified auxiliary hypotheses. Rational Kummer
membership, auxiliary availability and complex-order comparison would
still be independent gaps even if that intermediate test succeeded.
The proposed target is uncovered and requires its own source review;
no proof, model or mathematical script for it is produced here.

Mathlib coverage of the new source theorem and proposed comparison:
**not checked**. Existing lemma coverage qualifications are unchanged.

