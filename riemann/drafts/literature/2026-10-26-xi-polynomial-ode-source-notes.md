# Xi polynomial ODE source review — source record

Completed source inspection on 2026-10-26. The initial checkpoint below
is preserved; its unfinished reading tasks are resolved in the final
inspection record. The mathematical application is still deferred.

The authorized task is literature-only. No lemma or mathematical script is
being written. The exact target remains the assessment in
`2026-10-26-xi-polynomial-ode-closure-coverage.md`.

Primary sources retrieved before the final comparison:

- G. Valiron, *Sur les fonctions entières vérifiant une classe d'équations
  différentielles*, Bull. SMF 51 (1923), 33–45, Proposition I, pp. 33–34,
  linear-equation proof §2, pp. 35–38:
  https://www.numdam.org/item/10.24033/bsmf.1030.pdf . Text retrieved;
  equation-level visual checks and scope comparison remain to finish.
- J. C. Lagarias and E. Rains, *On a two-variable zeta function for number
  fields*, Ann. Inst. Fourier 53(1) (2003), 1–68, §4 opening p. 23 and
  Theorem 4.1: https://www.numdam.org/item/10.5802/aif.1939.pdf .
  Its recorded xi growth must be compared with L018's exact normalization.
- F. Bornemann, arXiv:0910.1841v4, §8.1, Theorem 8.1, printed p. 28,
  explicitly identifies the coefficient class and points to Valiron's
  book p. 108. This is corroboration; the original Valiron article above
  is available, so its primary proof is preferred.

Unfinished: verify the primary theorem's transcendental-function context,
normal-type constants, exceptional-radius completion and same-modulus
branch case; inspect the xi source formulas rather than relying on OCR.
Affine-height specialization and a canonical impossibility result belong
to a later approved research turn. No Xi nonexistence theorem has yet
been installed locally and no RH sign claim is made.

## Final inspection record

**Valiron.** Proposition I concerns a transcendental entire solution of a
finite linear ODE with rational-function coefficients, hence includes
complex polynomial coefficients with nonzero leading polynomial. Its
conclusion is
`log M(r)=k r^l+O(r^(l'))`, with positive finite k, rational l>=1/p
and l'<l. The polynomial exception is implicit in the unbounded central
index used in §1 and explicit in Bornemann's formulation. Read the full
linear proof: the maximum-point derivative estimates (1)–(8), Newton
polygon/Puiseux branches (9)–(10), monotonic stabilization across ordinary
and exceptional intervals, same-modulus roots, and the all-radius
conclusion (11). No simple-root, real-zero, monic-equation or constant
leading-coefficient hypothesis is imposed. Visual inspection of all six
printed pages 33–38 resolved the extracted equations. Valiron explicitly
repairs an incompleteness in Wiman's earlier argument; cite this proof,
not the earlier argument alone. The nonlinear sections are outside scope.

**Completed xi.** Lagarias–Rains §4, p. 23 explicitly states order one
and infinite type for the formula matching L018's completed xi. This is
a recorded classical fact in their introduction to §4, not a newly
numbered xi theorem. Theorem 4.1 is instead an upper growth bound for
their two-variable function; its proof does not by itself establish
infinite type. Read and visually checked pp. 23–25, including the
positive-theta and gamma-integral upper bound; do not mistake the upper
bound for a lower bound. Import the p. 23 xi statement by its exact
citation rather than claim a new growth proof. The affine Xi application
is the separate continuation, not an assertion derived in this source
record. No gamma-factor holonomicity closure is used.

**Corroboration and optional check.** Bornemann's Theorem 8.1 and
definition (8.5) say normal type and explicitly exclude polynomials.
His book reference was followed; the original article provides the
needed proof without depending on inaccessible book pages. NIST DLMF
[5.11.1](https://dlmf.nist.gov/5.11.E1) was inspected for the usual
log-gamma expansion in `|arg z|<=pi-delta`; it is a supporting check only,
not a license for a new sector-growth derivation this turn. No reproof
of the classical growth theorem is needed or proposed.

**Access.** Numdam's legacy BSMF PDF URL failed in the web reader; its
article-page PDF link above succeeded. The NMU book link returned an
empty page, and the Archive book PDF later redirected unsuccessfully.
The book's full-text route was accessible but no p. 108 proof was read
there. The original article removes this nonessential blocker.
CiteSeer/TUM derivative-paper PDF routes failed, while the exact
arXiv:0910.1841v4 PDF succeeded. Web screenshots produced no viewable
images in this interface, so direct public PDFs were rendered locally
with Poppler and viewed. These were read-only source operations, with
temporary files outside the notebook, not mathematical scripts or
certificates. No source blocker remains for the bounded application.

**Mathlib.** Full matching non-D-finiteness, growth-class and supporting
affine-composition coverage were not checked. No absence is claimed.
