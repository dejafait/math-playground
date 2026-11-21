# Theta/contour evaluator source comparison1608

18 November2026. Literature only. No new identity, bound, lemma,
mathematical script or source-proof audit is asserted.

The main gap is L030-L032/C032a. The saved question1607 concerns
dictionary1570, with its strict residual below1/2 on the entire width
interval[1,2] for the variation-at-most-2 class. An evaluator would
only support that necessary-constraint test. Arbitrary variation,
full cancellation, positive output and unsmoothed Xi realization
remain open.

Read the exact definitions and evaluator statements in C032j/m/q/w/y/z,
C032z's representation/Fourier proof and audit passages relevant to the
zero-frequency cancellation, L019/L021, assessment1570, notes1555/1572/1582,
and stop1586. Reused audited identities, rather than redoing them.
Notes1603 preserve the exhausted three central signed-payment leads;
none is reopened here. Existing notebook changes are preserved.

The direct-theta proposal has no supplied theorem converting L019/L021's
linear Xi integral into this divisor smoothing. The unconditional
explicit-formula interface is already available in C032w/z; merely
renaming it a contour evaluator supplies no different error estimate.
The literal expanding-disk and integrated-series stops remain scoped
implementation obstructions, not lower bounds on the actual kernels.

New primary source inspected: NIST DLMF version1.2.8 (15 September2026),
[5.9(ii), equation5.9.16](https://dlmf.nist.gov/5.9.E16), including the
preceding Re(z)>0 restriction and both integral forms. Its exact input is

    psi(z)+gamma_E=integral_0^infinity
                    (exp(-t)-exp(-z*t))/(1-exp(-t)) dt,
    Re(z)>0.

This applies pointwise on z=1/4+i*r/2 for real r, without an asymptotic
remainder. It does not by itself authorize integration against C032z's
complex-valued h or separating divergent endpoint pieces. C032z already
supplies its ordinary Fourier transform, zero mean and uniform inverse-
square bound. A combined-integrand interchange, endpoint control and
effective new-variable tail are outstanding specialization obligations.
No formula for their combination has been derived in this turn.

Exactly three candidate mechanisms compared: (1) direct theta/logarithmic-derivative
contour, with no new error premise; (2) asymptotic subtraction of the
spectral gamma tail, requiring additional uniform derivative/remainder
coverage; (3) exact digamma integral with the existing zero-frequency
cancellation before numerical estimation. Candidate3 is an independently
testable error mechanism: it would avoid enumerating C032z's digamma
series and does not need certified zero coordinates or a zero-free
integration contour. Its proposed bound remains unproved.

Queries run: `site.dlmf.nist.gov 5.9.16 psi integral representation Re z`;
`"explicit formula" "Gaussian" "digamma" "Riemann" integral`;
`"Riemann" "theta" "zeros" "trace formula" logarithmic derivative contour Gaussian`.
Only primary inspected passages and reused named coverage are inputs;
search-result claims and unrelated purported spectral realizations are
not evidence. Narrow local searches covered spectral/Gaussian/smoothed
assessments and stops for Binet, digamma-integral and gamma-elimination
terms. The checked earlier Binet use1555 is an asymptotic heat estimate,
not the proposed exact integrated-test specialization. No claim of
exhaustiveness, novelty or absent Mathlib coverage is made.

Two further queries were run: `"Guinand" "Weil" "digamma" "integral" Fourier`;
`"explicit formula" "h" "archimedean" "Fourier transform" "h(0)"`.
No search snippet is imported. Numerical agreement claims and purported
spectral realizations in returned results are unverified leads.

Reused and checked primary scope: Connes, *Heat Expansion and Zeta*,
arXiv:2402.13082v1 (20 February2024),
[author PDF, Section2, equations(4)-(10), printed p.4](https://alainconnes.org/wp-content/uploads/heat-zeta.pdf).
The source requires smooth Mellin tests on positive reals, some delta>0,
decay O(x^delta) at0 and O(x^(-1-delta)) at infinity. The complex-zero
identity(5) includes both pole integrals, all prime powers and the
subtracted archimedean term(7)/(9). The real-spectrum rewriting(11)
assumes RH and is excluded. This source already places the spectral
and ordinary archimedean forms in the same explicit-formula framework.
Its smooth-test hypotheses do not automatically cover the cusp in
C032z's Fourier transform at0. No direct Mellin application to that
cusp, contour limit or new error constant is imported.

Final decision: park candidate1 as an unsupported error mechanism,
preserving its scope in ATTEMPTS/2026-11-18-theta-contour-evaluator-park-1608.md.
Candidate2 would require separate uniform asymptotic-remainder coverage;
it was not developed or approved. Select candidate3 for a separate
bounded specialization, using DLMF5.9.16 and C032z's already audited
ordinary transform rather than assuming a smooth Mellin test. There
is no essential inaccessible source for this selected question.

The exact next target and approval scope are saved in
2026-11-18-gamma-integral-specialization-1608.md. Seek an ordinary-integral
representation of the gamma contribution, keeping endpoint cancellation
inside the integrand until justified; then test its tail after v=16,
where v is the Fourier variable t/2, against1/16. This is a proposed
analytic error benchmark, not a necessary dictionary accuracy or an
achieved bound. No formula for the combined gamma term, interchange,
tail bound or numerical certificate was proved here. The next turn's
separate approval precedes mathematical use of this new assessment.

This completes the saved source question1607. Outcome EXPLORATION:
new exact-source coverage and a bounded independent continuation, with
no new mathematical result, impossibility claim or advance beyond the
sources checked. It does not reset exploration/recovery counters by
self-report. Creative central-gap routing remains blocked by the
absence of an independent signed theta upper term; a standard integral
specialization is not relabeled creative. Full matching Mathlib coverage
remains unchecked and unknown. No cross-notebook input was used.
