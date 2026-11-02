# Fixed-pair calculation working record — 31 October 2026

Approved target: decide D_(pi/2)(pi/4) for F(x)=(1-x^2)^2 exp(-2x^2), with positive even Schwartz inverse kernel, real-zero class verification and complete harmonic remainder.

Assessment reused: drafts/literature/2026-10-31-reflected-majorant-fixed-pair-test.md (SPECIALIZE, saved before this invocation). Essential mathematical inputs: L233 and the convergence/reflection portion of L598; the latter is being checked only in this specialization. Imports: Knapp VIII Props. 8.1/8.2/8.10, Thms. 8.4/8.15, and Csordas v2 Definition 1.1/(2.1), as precisely cited in the assessment.

Main gap: actual-Xi all-degree positivity at unbounded heights. Downstream use: discriminate a generic spectral-to-reflected shortcut; no actual-Xi transfer. Stop if hypotheses/reconstruction fail or the fixed-pair full-tail comparison is inconclusive; no wider grid.

Unfinished derivation (not a certificate): with g(u)=exp(-u^2/8)/sqrt(8*pi), Fourier differentiation suggests k=g+2g''+g''''=g(11/16+u^2/32+u^4/256), which is strictly positive. Product differentiation suggests Ahat(2x)=(1-x^2)^2(x^4-x^2+2)exp(-4x^2). The reflected derivative should be the alternating periodization of A; its normalization and integration constant remain to be checked. No sign is claimed until the complete odd-harmonic remainder is bounded.

## Completed analytic comparison, pending canonical write-up

The reconstruction gives D_h(r)=(2/pi) sum over positive odd n of Ahat(n*pi/h) sin(n*pi*r/h)/n, with D_h(0)=0. At the fixed pair, the n=1 term vanishes and n=3 contributes -(4736/3)exp(-36) inside the factor 2/pi. For n>=5, the absolute coefficient is at most n^7 exp(-4n^2). Consecutive odd-index envelopes have ratio at most (7/5)^7 exp(-96)<2^(-89)<1/2. Thus the entire remainder is smaller than 156250 exp(-100), whose ratio to the negative main magnitude is smaller than 100 exp(-64)<100/2^64<1/2. This yields a strictly negative value once normalization and convergence are written out. No numerical quadrature is needed. Preserve the exact two-sided enclosure and verify the polynomial algebra mechanically before canonicalizing.

Canonicalized after exact algebra checks in L599, with all analytic
justifications and the complete two-sided bound. The preceding unfinished
notes record the calculation's development, not additional unresolved
premises. Independent audit remains pending in PROGRESS.md.
