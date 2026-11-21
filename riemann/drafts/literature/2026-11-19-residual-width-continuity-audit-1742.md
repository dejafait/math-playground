# Residual width exclusion: conceptual audit coverage1742

TARGET: Critically audit C033j's exclusion of C033i's residual mu from finite real signed width mixtures on [1,2], checking uniform endpoint bounds, density continuity and all-Borel signed deconvolution at x=1.
CHECKED: 2026-11-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse assessment1740/source-notes1740's target-specific signed-mixture, convolution-exponential and regularity searches and duplicate/failure comparison; this audit introduces no new family, hypothesis or mechanism and makes no fresh novelty search claim.
SOURCE_EVIDENCE: Reuse separately approved1740/recovery1741: Sra2610.00584v1 Lemma2.1/PropositionB.1 https://hexagonmath.org/pdf/2610.00584v1 ; Sra2611.00345v1 Proposition3.1/C.1 https://hexagonmath.org/pdf/2611.00345v1 ; Cekanavicius--Vellaisamy2018 Section1/(23)-(24) https://www.vmsta.org/journal/VMSTA/article/114/read ; Mimica2015 Propositions1.4(iv)/1.8 https://web.math.pmf.unizg.hr/~amimica/lt.pdf ; DLMF5.12.1 https://dlmf.nist.gov/5.12.E1 . Exact inspected hypotheses/proof cases and source qualifications remain in source-notes1740/1552/1736; no fresh external read is claimed.
COMPARISON: The sources supply heat errors, finite signed measure exponentials, positive Laplace uniqueness and beta integration; they do not supply C033j's continuum regularity or exact range exclusion, which now have a written local proof requiring critical checking.
GAP: Audit that the common integrable envelope and simplex/series dominators hold for all widths and that signed mixture construction and transform uniqueness identify measures including zero before the continuous-representative contradiction; do not assume positivity of a quotient or a variation cap.
REASON: This is the essential conceptual audit of the newly completed target, using unchanged source techniques; no additional source discovery or stronger theorem is nominated.
SCOPE: Audit only C033j under C032j/q/s and C033i, preserving actual-divisor, multiplicity, finite-zero, counting, heat and fixed-v1 qualifications; W=[1,2], arbitrary finite real signed eta, I=[1,3/2], exact residual mu and lambda. No J_eta=0, moment, positivity-reflection or Xi-realization theorem is covered.

New ready continuation nominated after research1742; separate literature
approval1743 now confirms the unchanged EXPLORE audit scope for the next
turn. See [approval notes1743](2026-11-19-residual-width-audit-approval-notes-1743.md).
This assessment does not certify the proof or retroactively approve uncovered mathematics.
The completed proof attempt used the unchanged assessment1740 that was
saved and separately approved before its invocation.

Check the following load-bearing steps in the canonical C033j proof:

1. C032s's j=0,1 errors imply |K'(u)|<=C/u with one positive onset.
   Integrating over [u_sigma,u_1] gives a uniform t^(-1/2) majorant;
   compact heat times give a t^(-3/2) tail. No differentiation of an
   O term or extension of an endpoint sign is permitted.
2. The signed exponential is finite, mass one and supported on X;
   its zero atom is exp(-M_sigma). Its transform identifies nu_sigma
   using positive uniqueness applied to signed Jordan parts, including
   zero. This is not a finite inverse of nu_1 or positivity reflection.
3. Absolute simplex integrability, beta constants, the parity-series
   ratio and uniform convergence must identify a continuous density
   representative near 1, not merely an L1/total-variation limit.
4. Norm continuity and the uniform measure bound must justify the
   setwise signed mixture, its countable additivity and all bounded
   Borel interchanges for each arbitrary finite |eta|, without a
   common variation cap or assumptions on the density of nu_sigma.
5. Cancellation of exp(-B_1(s)) must give equality on all Borel sets.
   The support intervals for C033i's inverse must force incompatible
   one-sided limits by continuity and almost-everywhere equality,
   rather than by the value assigned to a density at one point.

Pass only if all these checks and the direct mathematical inputs are
correct. If a gap is found, correct or downgrade the exact claim and
retain the failed bound or identification. The result is not an RH
candidate; C032q/r cancellation, moments/tails and actual-Xi positivity
remain independent. Full matching Mathlib coverage remains unknown.
