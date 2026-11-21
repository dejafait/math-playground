# Vanishing-exponent finite-window comparison: nomination1982, review1983

TARGET: Assess source coverage for a uniform O(1/d) finite-window Jensen-error bound at exponent 1/(4d), using C029i and retaining every root singularity.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1983 searched exact small-exponent/Jensen-gap/exponential-remainder terms and the named C028/C029 and stop1963/source-limit1966/closure1982 records; no completed exact match located. Queries, inspected ranges and limits: drafts/literature/2026-11-20-vanishing-exponent-window-source-notes-1983.md; no novelty claim.
SOURCE_EVIDENCE: Roos--Seeger, Analysis: Foundations and Selected Topics, revision2026-10-30, Section2.4 Theorem2.49/(2.5), p71, https://people.math.wisc.edu/~aseeger/book/Real_Analysis_Vol_1.pdf ; NIST DLMF1.4.35-37 and4.5.4, https://dlmf.nist.gov/1.4#vi and https://dlmf.nist.gov/4.5.E4 ; full Taylor proof read. Reuse Cover--Thomas Section2.6 Theorems2.6.1-2.6.2 pp24-26 and source-notes1962/1966/1978. Compare Gao--Sitharam--Roitberg AJMAA16(2)(2019) Art14 Theorem2.1 p6/p14, https://ajmaa.org/searchroot/files/pdf/v16n2/v16i2p14.pdf .
COMPARISON: Scalar Taylor with integral remainder, Jensen and log x<=x-1 supply the standard method; C029i supplies the audited absolute norm. Gao et al.'s polynomial-growth theorem excludes exponentials; fixed-family log-partition smoothness supplies no uniform rate. No source states the exact actual-family bound. Fixed-q and paired stops remain distinct.
GAP: Prove applicability and the exact uniform O(1/d) bound through the entire L/q=8Ad^2 factor, including integrability, positive finite Z, all singularities and all d,A. No E bound is established here; signed upper payment and H_d=o(d) remain open.
REASON: Essential scalar source coverage is now inspected; one bounded standard specialization can follow separate approval of this newly ready continuation. No further browsing or norm audit is needed under unchanged hypotheses; no uncovered mathematics is proved here.
SCOPE: Scalar Taylor/Jensen/logarithm method for the actual C028b/C028d family using audited C029i, integers d>=3, real A>=1, finite-interval uniform probability, all multiplicities, real roots and a possible origin root. No RH, simplicity, real-rootedness, signed mean sign, log-partition differentiation or degree/cutoff interchange.
COVERED_TARGET: Establish or refute 0<=E_(d,A)<=C_*/d uniformly for integers d>=3 and real A>=1, with q_d=1/(4d), L=2Ad and E=(L/q_d)log[L^(-1) integral_[-Ad,Ad] exp(q_d t_d)]-integral_[-Ad,Ad] t_d, using C029i and C028d.

## Completed source review1983

[Source-notes1983](2026-11-20-vanishing-exponent-window-source-notes-1983.md)
records the completed comparison. SPECIALIZE approves the source scope
and covered proof target, not its truth. Import the scalar theorems and
prove the local applicability/normalization in a later research turn.
The newly ready continuation remains subject to separate supervisor
approval. The nomination below preserves its original test and mechanism
comparison; its1982 pending status is historical.

## Exact proposed mathematical test, not a result

Keep C028d's centered monic Q_d and t_d=f_d/d. Set

    q_d=1/(4d), L_(d,A)=2Ad,
    Z_(d,A)=(1/L_(d,A)) integral_(-Ad)^(Ad) exp(q_d t_d(y)) dy,
    E_(d,A)=(L_(d,A)/q_d) log Z_(d,A)
                       -integral_(-Ad)^(Ad) t_d(y) dy.

The proposed threshold is existence of one finite C_* such that

    0<=E_(d,A)<=C_*/d      for every integer d>=3 and real A>=1.

These are definitions and a research question, not an established
finiteness, inequality or asymptotic conclusion. The growing prefactor
is L_(d,A)/q_d=8Ad^2; forgetting it would change the test. The exact
exponent of the polynomial quotient is 1/(4d^2), since t_d=f_d/d.
The already audited input is only
integral_R t_d^2 exp(|t_d|/4)<=C from C029i. C028d supplies L1 of
t_d at each degree, not a uniform signed upper payment.

Possible downstream use: a vanishing comparison cost would isolate the
remaining actual-family moment upper estimate without the fixed-q loss.
It would not prove that estimate, remove the compact nonreal divisor,
or establish C028b's H_d=o(d). No unproved sign of Z-1 is a premise.

## Three mechanisms and recovery choice

1. A new fixed-q positive-moment upper payment repeats the obstruction
   in audited C029f and stop1963. Do not reopen it without changing its
   mathematical premise; the present audit changes no fixed-q floor.
2. Fixed-q positive/negative moment pairing still needs the full signed
   complement missing in source-limit1966. Separate nonnegative bounds
   do not provide that cancellation. Do not retry Carbery--Wright access
   or repeat the old paired diagnostic merely because C029i is now checked.
3. Select the one-sided vanishing-exponent window comparison above.
   The new usable input is C029i's audited full-line norm. The task
   changes from establishing absolute domination to controlling the
   nonlinear moment-to-mean error after its exact window factor. It
   requires no conjectural signed-complement cancellation. This is a
   distinct, independently testable intermediate gap, not a repeated
   source approval, q sweep, or reproof of the norm.

No justified creative signed-payment mechanism is available from these
inputs. Do not label this ordinary specialization creative to meet a
scheduling preference. Source coverage must first determine whether a
short mathematical application is warranted or already duplicated.
C034p was briefly screened as another possible pending audit, but its
exact stop record already records completion1902; it is not a next task.

## Bounded source review and continuation test

Reuse the recorded Jensen and log-partition interfaces. Compare the
exact threshold with standard exponential-remainder inequalities and
existing local small-exponent/window results; retrieve only essential
primary hypotheses and proof cases missing from the reused coverage.
Full-line Lebesgue measure is not a probability: the finite interval
normalization L_(d,A) must stay explicit. Check all root singularities,
including multiple roots and the reference origin, and all d,A
quantifiers. A fixed-d differentiability statement alone is insufficient.

Continue to one mathematical specialization only if the source comparison
supports an integrable remainder through the full prefactor with no
unpaid degree/window factor. Import an exact match if found. Otherwise
identify the missing estimate or an existing duplicate and park this
comparison; do not infer failure of RH or of other signed mechanisms.
No derivation or theorem application for E is performed in1982.

Essential inputs for a later attempt are C029i and C028d, retaining
C028b/C028f's actual normalization and uniform constants. C029f and
source-limit1966 are contrasts, not assumptions. The upper moment
sign, signed mean, S_F=0 and actual-Xi mixed positivity remain open.
Full matching Mathlib coverage is unchecked/unknown. Nomination1982
approved no new coverage and required a literature-only turn. Review1983
above completes that comparison; the proposed inequality remains unproved.
