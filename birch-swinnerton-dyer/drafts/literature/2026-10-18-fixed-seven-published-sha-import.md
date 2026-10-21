# Conductor-389 seven-primary Sha — published fixed-case import

TARGET: Import Stein--Wuthrich Theorem 12.3 at seven for the exact conductor-389 model, retaining computational-source qualifications and justifying the passage from seven-torsion to seven-primary Sha.
CHECKED: 2026-10-18
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse the completed exact-target source comparison in drafts/literature/2026-10-18-fixed-seven-integral-leading-term.md; the published fixed-case theorem covers the proposed target, so a new regulator or main-conjecture proof would duplicate known work.
SOURCE_EVIDENCE: Stein--Wuthrich, Algorithms for the arithmetic of elliptic curves using Iwasawa theory, Math. Comp. 82 (2013), 1757--1792, Theorem 12.3 and proof p.1788; Section 12.4 pp.1787--1788 and Algorithm 11.1 with ordinary proof pp.1783--1784; published offprint https://wstein.org/papers/mcom2649-iwasawa-alg.pdf . Exact model identification reuses L034's inspected Cremona sources; L030/L033 supply conductor/minimality and good ordinary reduction at seven.
COMPARISON: The published theorem gives vanishing of p-torsion on this fixed curve throughout a range including seven. Only exact applicability and the elementary torsion-group passage remain to assemble; no regulator computation, reverse divisibility or new mathematical mechanism is needed.
GAP: No essential source is unread for this bounded import. Preserve the original computational proof as a cited input rather than claiming a fresh replay; this assessment does not yet create a canonical lemma or assert the completed application.
REASON: Separately approve the newly ready continuation, then import the stronger known fixed-case theorem instead of reproducing already covered arithmetic.
SCOPE: Only E=[0,1,1,-2,0] over Q at p=7, using the published computation. No L026 premise package, independent regulator valuation, full Sha finiteness, arbitrary-curve rank equality or refined formula is covered.

The [completed source review](2026-10-18-fixed-seven-integral-leading-term.md)
records the exact primary statement, all relevant ordinary proof cases,
source qualifications, local comparison and failed-route distinctions.
The supervisor must separately approve this newly written ready
continuation before invoking research. No additional source discovery is
needed while its target and hypotheses stay unchanged.

In the later canonical file, identify 389a/389a1 with the exact L030 model
using L034's published group/model source, use L033's good-ordinary-seven
certificate and check the theorem's range/exception. State precisely what
the theorem asserts, then write out why a nonzero seven-primary torsion
element would give a nonzero element killed by seven. Preserve the original
computation's un-replayed status. Do not use L081 as a regulator, transfer
the theorem to arbitrary curves, or claim that L004 acquired integral
divisibility without its extra hypotheses. A model mismatch or an actual
source correction would stop the application and require reassessment.

The downstream purpose is a fixed arithmetic input independent of the
unfinished degree-48 unit/class computation. The main rank/order gap is
unchanged. Mathlib full matching and supporting coverage: **not checked**.
