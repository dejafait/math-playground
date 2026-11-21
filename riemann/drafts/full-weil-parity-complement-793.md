# Fixed 120-mode complement attempt — working record

13 November 2026, step793. Gate: the unchanged SPECIALIZE assessment
`literature/2026-11-13-full-weil-parity-complement-test-792.md`.
This records unfinished reasoning before computation; it is not a certificate.

Completion pointer: the attempt is now recorded canonically in
`lemmas/C759a-120-mode-absolute-complement-budget-stop.md` and its
certificate. The original pending notes below are preserved as partial
reasoning; they are not current instructions or a second proof.

The target is the full even/odd Rayleigh comparison for L744(6) on
(-1,1), with exactly 120 retained odd sine modes. The remaining main
gap is actual-Xi all-degree mixed positivity. A parity gap alone would
leave even simplicity, realization and global signs unresolved.

Inputs read: L741's full-line normalization, L744(5)-(6) and asymptotic
symbol bounds, the ready Suzuki/Schur source assessment, and L759's
general-entry reduction (its different-window finite certificate is
only contrast). C998z's modulus stop is preserved.

Attempt: first bound the full odd complement by a Fourier low-frequency
leakage estimate plus the complete bounded prime and pole terms. For
an odd unit function orthogonal to sin(pi*j*x), 1<=j<=120, its Fourier
transform is controlled below the first omitted frequency 121*pi by
the square-sum of all omitted sine transforms. No high-mode cutoff is
permitted. Test whether this lower estimate can supply d>0 after an
even Ritz shift before doing a finite Schur calculation.

Pending: prove domain/core applicability, the leakage estimate, full
prime/pole costs and rigorous numerical thresholds; enclose the constant
even trial as the least expensive admitted Ritz vector. If this entire
lower-bound family is insufficient, stop this certificate at 120; no
conclusion against the actual gap and no larger matrix sweep. No
coupling estimate or finite Schur sign is currently established.
