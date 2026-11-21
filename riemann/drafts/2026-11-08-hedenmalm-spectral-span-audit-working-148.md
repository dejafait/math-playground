# Finite spectral-span critical audit, step148 — working checkpoint

Approved target: critically audit L907's proof that ker L intersects
H_finite trivially, including the complex integral, finite invariance
and Fourier hypotheses. The supplied unchanged SPECIALIZE assessment
is `literature/2026-11-08-hedenmalm-spectral-span-critical-audit.md`.
This is one mathematical audit, with L906 and L907 as local inputs.

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
A passing audit would validate removal of finite-domain representative
ambiguity only. Positive metric, symmetry and any mixed-form transfer
remain unresolved; the enlarged V and positive-pair import stops stand.

Partial audit: for alpha=a+ib, the lower-end absolute bound is
C y^(-b-11/2) exp(-pi/y^2); substitution z=1/y gives exponent b+7/2,
as stated. Product differentiation gives delta u=-i alpha u+w and
D u=-alpha u+w/i. The kernel formula Lf=wD(f/w) is valid since w>0.
A nonzero kernel vector in a finite span F makes w belong to F; only
then does the generator identity give D(F) subset F. Cayley-Hamilton
therefore applies without an inverse or generator independence.

Still to finish: independently check every logarithmic Schwartz
seminorm, finite and improper FTC for each derivative, the exact 2pi
multiplier, continuity at polynomial roots and pointwise inversion.
Retain the theorem only if every obligation passes, without changing
the domain or importing Mellin normalization, RH or simplicity.
No verdict is certified by this preliminary checkpoint.

Completion: the audit passes, with all checks recorded in canonical
L907's step148 audit section. In particular the improper FTC follows
from finite-interval FTC, absolute integrability of the next derivative
and vanishing at minus infinity. The theorem and domain are unchanged.
This working record is preserved; it is not a separate proof source.
