# Real-zero factor source review2225 — completed source record

Literature-only work; no quotient-kernel identity or sign result is proved.
The supplied assessment2224 fixes the exact target. Main gap remains
L030-L032/C032a. Local inputs read for scope: L018/L019/L024/L058,
C919f's hypotheses/conclusion and source contracts. The root is unspecified
in (14,29/2), with possible multiplicity and no census premise.

Sources actually inspected:

- E.O. Tuck, *On positivity of Fourier transforms*, Bull. Austral. Math.
  Soc.74 (2006),133–138, pp133–135, equations(1)–(4), publisher PDF:
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D232B9DEB4819E4D2FF17E8162B8B066/S0004972700047511a.pdf/on_positivity_of_fourier_transforms.pdf
  Its decreasing-amplitude sine-transform argument is relevant; its
  cosine-convexity criterion is a different assertion. The old review576
  already assessed these proof cases for another mixed determinant.
- NIST DLMF1.13(iii),(1.13.8)–(1.13.10): inhomogeneous ODE and
  variation of parameters, analytic coefficient/forcing hypotheses.
  https://dlmf.nist.gov/1.13.iii
- David Gross, *Advanced Quantum Mechanics — Incomplete Notes*, live
  PDF dated21July2026, Appendix D.1–D.2.2, printed pp143–145,
  (D.2)–(D.11): boundary-dependent Green solutions and real-pole warning.
  https://www.thp.uni-koeln.de/gross/files/aqm-23.pdf
  This is a source lead for ordinary division, not a positivity theorem.

Local nonduplicates: September23 nonreal deflation removes the detecting
nonreal pair and loses normalization; October28 finite-Blaschke energy
defect does not sign an inverse Fourier kernel. Review576's signed
mixed-determinant failure leaves its amplitude unpaid and is not a
failure of the ordinary single-amplitude sine theorem. Discovery1117
prevents extrapolating finite signs without another actual-Xi bridge.


## Exact known inputs and their scope

A. Wintner, *A Note on the Riemann ξ-Function*, J. London Math.
Soc.10 (1935),82–83, DOI https://doi.org/10.1112/jlms/s1-10.1.82,
is the original citation for strict decrease of the theta kernel.
Its full classical statement was read in G. Csordas, *Fourier transforms
of positive definite kernels and the Riemann ξ-function*,
[arXiv:1309.0055v2,21February2014](https://arxiv.org/pdf/1309.0055v2),
Theorem4.1 and (4.2), printed p10. That statement supplies positivity,
evenness, strip analyticity, super-exponential decay of each derivative,
and strict decrease on the positive half-line. The normalization in
(4.2) matches L019 by K(u)=4 Phi(u/2), term by term; no zeta zero
assumption is involved. This is a comparison of definitions, not a
new monotonicity proof. The original Wintner proof is not independently
inspected or recertified here. Csordas's complete restatement, rather
than a snippet, is the inspected source for that named classical input.
The selected application needs no log-concavity or higher derivative
sign assumption. Those stronger questions are outside this review.

Tuck's sine theorem concerns a positive strictly decreasing amplitude
on the positive half-line with a convergent integral and decay. For the
bounded continuous integrable case proposed here there is no singular
endpoint issue. Read its full positive/negative half-period comparison
on p134 and the distinct cosine integration-by-parts argument pp134–135.
The parsed display(4) is incomplete, so it is not transcribed. The exact
alternating-half-period argument is also readable in Csordas Remark3.11,
printed p9; only this ordinary sine theorem is relevant, not the adjacent
RH-equivalent positive-definiteness criterion. The translated amplitude
v -> K(u+v), for a fixed u>=0, has the source's positivity, strict
decrease and integrability hypotheses under the imported theta result.
No assertion that a newly constructed residual amplitude is decreasing
has been found or approved. Neither theorem is a division theorem.

DLMF1.13(iii) gives a particular solution by variation of parameters
for a second-order inhomogeneous equation with analytic coefficients
and forcing on the domain, and describes the homogeneous ambiguity.
Here the intended coefficients are constants and the forcing is a
multiple of the actual kernel. These are inside its source scope on
a strip around the real axis. The source does not select the condition
at infinity, prove a half-line even extension, or sign that solution.
Those are explicit specialization obligations, not imported conclusions.
The exact inverse kernel is deliberately not derived during review.

T. Tao, *245C, Notes2: The Fourier transform*,6April2009,
[Section3](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
Exercise30 with its absolute-continuity and L1 derivative hypotheses,
Remark31 and the proof of inversion(11), were inspected. Reuse its
already assessed Fourier convention from discovery1117. A later
application must verify those integrability/boundary hypotheses for
the constructed kernel before using differentiation twice. The notebook
uses angular frequency and a half-line cosine integral, so normalizing
constants must be checked explicitly. The source general identities
are imported, not reproved. Its theorem supplies no positivity.

Gross's real-pole warning is only an explanatory comparison: generic
Green inverses are not unique without a boundary choice and can be
oscillatory. His gamma>0 oscillator example is not silently applied
with gamma=0. No distributional Green theorem or contour shortcut is
needed in the proposed ordinary variation-of-parameters specialization.

## Access and search evidence

Original Wintner publisher metadata was inspected through the Oxford
issue and article pages. The article is purchase-only; its first-page
GIF preview is unsupported by the web tool. Spira, *The integral
representation for the Riemann Xi-function*, J.Number Theory3 (1971),
498–501, DOI10.1016/0022-314X(71)90016-3, was located, but the article/PDF
requests return403. Both original proofs remain unread; neither is
claimed as independently checked. CNV1986 TheoremA p523 is another
restatement lead: the Kent PDF has no readable text, screenshots return
no usable image, and a shell download failed DNS. Its indexed theorem
passage alone is not source verification. These failures do not block
using the exact named classical theorem in the completely inspected
Csordas statement. No API key, paid access or purchase was used.

The bounded search used the following specific terms (grouped variants):

- Fourier transform divide real zero positive kernel Polya factor removal;
  Xi real zero division Fourier kernel positive sine integral.
- Fourier transforms division real zeros kernel; kernel removing real
  zeros Fourier; Xi factor positive kernel; Fourier divide Polya.
- admissible kernel division; Fourier kernel real zero quotient;
  Polya division kernel; Csordas division Fourier.
- characteristic function real zero division; characteristic functions
  real zeros dividing; positive definite real zero divide;
  characteristic functions quadratic factor.
- Fourier division lemma zero; Fourier transform dividing out zeros;
  Fourier transform zero primitive; Fourier division Schwartz zero.
- Riemann Xi kernel strictly decreasing Csordas; admissible kernel
  Riemann derivative; exact Wintner/Spira titles and citations.

General distribution-division and sampling-space results found by these
queries were not imported as kernel positivity. Unrelated alleged RH
solutions and recent web claims were not inputs. Dimitrov–Rusev's survey
was searched only as a pointer for division/removal terminology, with no
matching text; it is not theorem evidence. A search miss establishes
neither novelty nor nonexistence of a stronger known result.

## Decision and bounded mathematical continuation

SPECIALIZE: the inspected sources cover the ordinary tools and the
classical actual-kernel shape input, but not the full combined quotient
statement. A later research turn can attempt exactly one construction
and sign application; it must prove all remaining origin, infinity,
transform and removable-pole obligations in a canonical lemma. No
quotient formula or positive residual result has been obtained today.
This is not a missing essential-source claim for the basic tools; the
unread original proofs are disclosed and no reproof is needed.

The continuation test requires an even decaying kernel with the exact
quotient transform and strict pointwise positivity on u>=0. Merely
constructing a formal ODE solution or sampling positive values fails.
Abandon that application if a nonzero origin/distributional boundary
term or an uncontrolled nondecaying homogeneous term remains. A failed
sign argument does not disprove RH. A successful one-removal result
would furnish a qualified actual-kernel input for a later shape test;
it would leave repeated-removal closure and the all-degree bridge open.
The sources do not justify a creative iteration claim. Matching Mathlib
coverage for the full proposed result is unchecked.
