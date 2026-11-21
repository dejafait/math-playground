# Exact gamma-integral specialization1608

TARGET: Specialize DLMF5.9.16 to C032z's zero-mean integrated test, justify an ordinary-integral representation of its gamma contribution, and test whether the tail after Fourier variable v=16 has uniform absolute error below1/16 for real sigma in[1,2] and complex |w|<=2.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1608 searched exact digamma/Fourier/archimedean terminology and compared three error mechanisms with C032w/y/z and stops1576/1581/1586. Queries, primary read ranges, inspected versus unread evidence and duplicate limits are recorded in drafts/literature/2026-11-18-theta-contour-source-notes-1608.md. No exact matching effective integrated-test bound was inspected; no novelty is inferred.
SOURCE_EVIDENCE: NIST DLMF version1.2.8 (15 September2026), Section5.9(ii), equation5.9.16 https://dlmf.nist.gov/5.9.E16 supplies the exact combined digamma integral for Re(z)>0. Reuse C032z equations(2)-(4), its ordinary-transform/zero-mean proof and audit1585, and existing Haslinger2.39/Fubini coverage. Connes2402.13082v1 Section2(4)-(10), p.4, https://alainconnes.org/wp-content/uploads/heat-zeta.pdf is a known archimedean-form comparison, not a smooth-test import at the Fourier cusp.
COMPARISON: The literal series stop1586 bounds the separate T_G(R)+T_psi(R,K) allowances. This target instead integrates the exact digamma representation with the established zero-frequency cancellation before estimating, with no digamma-term enumeration, spectral cutoff R, zero coordinates or zero-free contour. C032w/x's expanding spatial disk is not used. A new-variable tail bound is still a specialization to prove.
GAP: Justify the combined-integrand exchange for complex h, identify all signs and Fourier scaling factors, retain the origin cancellation, and obtain a uniform explicit tail at v=16; no such identity, error or computational feasibility is assumed.
REASON: This independent analytic error test addresses the specific gamma-series bottleneck without repeating its cost audit or enlarging its cutoffs. If successful it can supply one component of E for dictionary1570's variation2 certificate, while finite quadrature, other evaluator errors and the actual residual remain unresolved.
LITERATURE_REASON: Changed essential error mechanism: DLMF5.9.16's exact integral was not covered by notes1582's digamma-series scope. Source comparison is completed now; the next approved turn should be mathematical, not another generic evaluator search.
SCOPE: Exactly C032z's h(a)=e_(sigma,a)(w), real sigma in[1,2], complex |w|<=2, and gamma contribution integral_R h(r)*Re psi(1/4+i*r/2)dr/(4*pi). Put v=t/2 only for specifying the proposed Fourier cutoff. Actual-divisor/multiplicity/zero-ordinate/strip/counting qualifications persist; probability interpretations additionally retain C032j/m/q's finite-zero/heat/fixed-v1 qualifications.

This is a newly written ready assessment. The supervisor supplies its
separate approval before a research invocation; no proof is supplied
by this source review. A successful specialization is REPRODUCTION,
not a creative mechanism or a mathematical discovery beyond sources.

Import DLMF5.9.16 by precise citation. At z=1/4+i*r/2 its positive-
real-part hypothesis holds for every real r. Keep the difference of
exponentials in its numerator combined until the relevant integral
is justified. Its validity pointwise in r is not an interchange theorem.
C032z already gives h's evenness, uniform inverse-square bound, ordinary
Fourier transform and integral_R h=0. Do not rederive those inputs or
import an RH-dependent spectral identity. Complex h must remain complex;
taking the real part of an identity after multiplication by h is not
automatically valid. Treat the real-valued digamma kernel correctly.

One bounded attempt:

1. Identify the gamma contribution as an ordinary integral in v, using
   the combined cancellation, with every sign, factor2/pi and endpoint
   value justified. Supply an integrable majorant or a justified
   regularized-limit argument before exchanging the noncompact r,t
   integrals. The cusp in the known Fourier transform at zero is
   allowed only with explicit endpoint control; do not assert smooth
   Mellin-test hypotheses that it does not satisfy.
2. Prove an explicit absolute upper bound for the discarded v>16
   contribution, uniform on the entire closed parameter set, and
   compare it strictly with1/16. Use the exact Gaussian transform input
   and elementary exponential estimates, rather than differentiating
   an uncontrolled asymptotic remainder. This cutoff and tolerance
   are a fixed analytic benchmark, not asserted necessary for a future
   coefficient-weighted dictionary certificate.

Continue if the identity is justified and the stated tail benchmark
passes. An identity without the target bound is partial progress;
preserve the actual bound or failed interchange and stop this test.
Do not increase16, shrink the parameter disk/width interval, add
asymptotic subtraction, implement quadrature or start an optimizer
within this attempt. If the test fails, a repeat requires materially
new input or a refined mechanism, not automatic cutoff growth.

The intended output is a canonical qualified analytic result if proved,
or saved partial reasoning with its precise obstruction. An existing
formula can be imported instead if a full matching result is found;
no reproof is justified merely to add a lemma. No mathematical script
is needed unless genuinely useful for exact arithmetic; a numerical
preview cannot verify an analytic interchange or uniform inequality.

The tail concerns only the gamma contribution. Pole/prime truncation,
the compact integral's finite arithmetic, O_sigma evaluation and
coefficient amplification remain independent obligations. The desired
dictionary residual is still strictly below1/2 on[1,2], and no bound on
it is inferred here. Arbitrary variation, full odd cancellation, signed
positive output, H_d=o(d), S_F=0, unsmoothed realization and all-degree
actual-Xi positivity remain open. Full matching Mathlib coverage has
not been checked and is unknown. No cross-notebook input is required.
