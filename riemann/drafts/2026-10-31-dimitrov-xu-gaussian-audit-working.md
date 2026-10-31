# Fixed Gaussian phase audit — working checkpoint

Approved target: the unchanged SPECIALIZE scope in
`literature/2026-10-31-dimitrov-xu-fourier-phase-audit.md`.
This is a RESEARCH / REPRODUCTION conceptual proof audit, not a new
actual-theta mechanism. Existing notebook changes are retained.

Read L233 in full and the completed translate-proof assessment, exact
autocorrelation/parity stops, and the relevant three-mechanism comparison.
Primary arXiv:1606.05011v1 pp. 3, 11–14 fixes the negative Fourier phase,
the Wronskian determinant, (3.3), (3.7), product (3.8), Lemma 3.3 and
Section 3.1. The n=2 integral is explicit also on p. 7. Web text was
retrieved; local PDF download failed DNS. No source hypothesis is inferred
from a search snippet, and no general correlation theorem is imported.

Preliminary exact calculation to finish checking: write
A(x)=sqrt(pi) exp((1-x^2)/4). For K(u)=exp(-u^2), y=1,
the known Gaussian transform gives real part A cos(x/2), imaginary
part -A sin(x/2), and Fourier transform of sinh(u)K(u) equal to
-i A sin(x/2). Thus the proposed real equality loses a phase.
Direct differentiation appears to give the Wronskian sum -A^2.
The explicitly normalized correlation is sqrt(pi/2) exp(-t^2/2),
whose cosh(t)-weighted Fourier transform is A^2 cos(x).
Finish domination, exact nonzero-frequency comparison, normalization,
and the Gaussian's exclusion by (3.8) before stating the verdict.

Do not infer a counterexample to Theorem 3.2: the nonconstant zero-free
Gaussian transform lacks its displayed zero-product representation.
No actual-Xi sign or approximation error has been obtained. Any new
central mechanism must receive separate coverage before mathematics.

Completed: all provisional calculations above are checked and written
in canonical L563, including the exact witness x=pi, the factor 1/2,
the corrected difference-weight correlation and the (3.8) exclusion.
The completed verdict is NEGATIVE source evidence. No mathematical
script was needed. The next Hermite remainder question is only a
REVIEW_REQUIRED nomination; none of its estimates has been derived.
