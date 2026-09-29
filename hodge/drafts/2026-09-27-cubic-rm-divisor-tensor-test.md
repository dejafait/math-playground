# Cubic RM divisor-tensor test — working record

Saved target: determine whether beta_U=(kappa tensor kappa)(u_U)
belongs to the full rational divisor-product span on A^4, for the
rank-eighteen Kuga--Satake variety at a very general point of the
four-dimensional cubic RM locus.

Prior gate: SPECIALIZE in the unchanged
[assessment](literature/2026-09-27-cubic-rm-kuga-satake-divisor-tensor.md).
The main local gap is a representative beyond the three-dimensional
Dickson family. Membership would supply the abelian tensor input to
the conditional transfer; kappa algebraicity would remain unresolved.
Nonmembership stops only this divisor recipe. The actual threshold
is membership of the whole tensor, including all mixed divisors.

## Interim reasoning saved before the proof

Over C, write T=T_1 orthogonal-sum T_2 orthogonal-sum T_3, with each
T_i of dimension six. The reviewed RM theorem gives the left action
of the product of the three Spin(T_i). In the exterior Clifford model,
each factor has two four-dimensional half-spin modules S_i^+, S_i^-.
Their tensor products W_epsilon give eight candidate isotypic blocks
of V=C^+(T); all occur with multiplicity 256. Their duality should
pair epsilon with -epsilon, to be checked explicitly before use.

The proposed test rescales V_(+++) by t and V_(---) by t^(-1),
fixing the other six blocks. If this preserves the polarization and
commutes with the full Hodge endomorphism algebra, it belongs to the
full group in Milne's divisor criterion. The first Clifford vector
factor should give a nonzero map T_1 into V_(+++) tensor V_(+--).
Projecting beta_U to two copies of this ordered tensor block would
then give a nonzero weight-two component, with coefficient sigma_1(U).

Checks identified at that save: half-spin duality and inequivalence; actual
isotypic multiplicities; nonvanishing for arbitrary invertible v_0 in
the map w -> v w v_0; identification through the actual polarization;
and exclusion of cancellation from T_2 and T_3 in this projection.
These checks, rather than a dimension comparison, decide the test.
No conclusion or new cycle was claimed at that save.

## Completed test

[L031](../lemmas/L031-cubic-kuga-satake-tensor-outside-divisor-algebra.md)
now proves nonmembership for the full divisor algebra. The final
proof uses commuting volume elements directly, so it does not need
the proposed half-spin multiplicity or simple-factor calculations.
Their eight projectors are nonzero in the actual full even Clifford
algebra. The polarization pairs opposite signs, and a rescaling
of one opposite pair belongs to the full polarization centralizer.
The actual embedding has an injective projected T_1 block; the
other two eigenspaces have zero projection. The resulting beta_U
component is nonzero and has weight t^2, hence is multiplied by four
at t=2. Auxiliary choices and transport through isogeny are retained.

The exact membership threshold fails. This is an informative negative
specialization of known tools, classified as REPRODUCTION, without
an originality claim. It closes this divisor supply on the third
turn of the window, following the two source-review explorations.
It proves no nonalgebraicity and leaves both algebraic kappa and
other algebraic sources for beta_U unresolved.

Exact check: `python3 scripts/cubic-kuga-satake/check_divisor_tensor.py`.
The split six-dimensional Clifford block has rank six and its
inverse-pairing tensor has 24 nonzero entries. The three-factor
sign table preserves the four dual pairs and gives projected
weight four under g_2. These are checks of the certificate's small
models; L031 supplies the proof for the full space and all choices.

## Mathlib

Coverage: **not checked**. The prior assessment supplies the precise
Milne, Schlickewei, van Geemen and Varesco references. Their general
results are supporting inputs; L031 supplies the individual tensor
test rather than citing those inputs as a preexisting full match.
