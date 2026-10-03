# Complete first-associated parity blocks — calculation checkpoint

The prior SPECIALIZE assessment is
[the saved parity review](literature/2026-09-27-first-associated-parity-blocks.md).
This calculation stays within its fixed reflected infinite blocks.

Let e(u)=Σ_{n even}q_n(u) and o(u)=Σ_{n odd}q_n(u) for u≥0,
with q_n from L254. Local differentiated Gaussian convergence and
integrable derivative envelopes, rather than finite-sum limits of
Fourier asymptotics, are needed. L234's exact cancellation gives
e′(0)+o′(0)=0, while direct differentiation gives e′(0)=−b<0.
The even sublattice has the exact identity
e(u)=2^(−1/2)K(u+log 2), so its reflected boundary is not a symmetry
point of the smooth full K. Scalar Poisson resummation also leaves
this derivative intact.

Write E,O for the Fourier transforms of e(|u|),o(|u|).
With d=e′(0)=−o′(0), separate half-line integrations by parts give
E=−2d/x²+O(x^(−4)), E′=4d/x³+O(x^(−5)),
E″=−12d/x⁴+O(x^(−6)); O has the opposite leading coefficients.
The exact block transforms at frequency 2x are

- same parity: ((E′)²−EE″+(O′)²−OO″)/4;
- opposite parity: (2E′O′−E″O−EO″)/4.

Thus their respective leading tails are −4b²/x⁶ and +4b²/x⁶,
with O(x^(−8)) remainders. This is an informative negative test for
separate block positive definiteness, not a negative total spectrum.
The total is still L233's unsigned actual-theta expression.

At this checkpoint the remaining write-up work is to give the full
infinite derivative envelope, pointwise modular coset identities,
Fourier/Fubini bounds and positive-definiteness necessity in one
canonical proof, and check the signs and normalization. No extension
of a Laguerre sign or zero-exclusion range is claimed. This reproduces
the known boundary-tail method in the newly tested infinite grouping;
no originality is asserted.

The completed proof is now [L356](../lemmas/L356-complete-parity-blocks-have-opposite-fourier-tails.md).
Its exact recurrence check corrected the derivative polynomial in L234
and L254 from −16v³+68v²−30v to −16v³+60v²−30v. The sign arguments
and the displayed block-tail coefficients survive this correction.
The write-up tasks mentioned above describe the earlier checkpoint;
their infinite-series and modular bounds are supplied in the canonical
lemma.
