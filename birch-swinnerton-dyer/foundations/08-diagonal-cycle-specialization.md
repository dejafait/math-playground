# Diagonal-cycle specialization: checked maps

Checked 2026-09-25 against Darmon--Rotger, *Diagonal cycles and Euler
systems II*, JAMS 30 (2017), 601--672, [published offprint](https://www.math.mcgill.ca/darmon/pub/Articles/Research/63.DR2/jams.pdf).
Retain the construction hypotheses, including ordinary E, reciprocal
tame characters, p-regular classical weight-one forms, p not dividing
N phi(N), and the non-Eisenstein condition on f in Section 1.6.

- [Equations (52)--(54), page 620](https://www.math.mcgill.ca/darmon/pub/Articles/Research/63.DR2/jams.pdf#page=20):
  the cycles lie in CH^2(W_s^dagger)_0(Q); their etale Abel--Jacobi
  images lie in H^1(Q,H^3_et(W_s^dagger_bar,Z_p)(2)).
- [Equations (60)--(63), page 622](https://www.math.mcgill.ca/darmon/pub/Articles/Research/63.DR2/jams.pdf#page=22),
  then [Definition 1.15 and (71), page 628](https://www.math.mcgill.ca/darmon/pub/Articles/Research/63.DR2/jams.pdf#page=28):
  ordinary normalization, inverse limit, and Hecke projection produce
  kappa(f,gh) in H^1(Q,V_fgh(N)).
- [Proposition 2.5, page 632](https://www.math.mcgill.ca/darmon/pub/Articles/Research/63.DR2/jams.pdf#page=32)
  identifies weight-two specializations with projected Abel--Jacobi
  images. Section 2.2.2, pages 632--633, defines the weight-one class
  by cohomological specialization.

Our inference: these maps do not supply a Chow-valued specialization
to Pic^0(E) tensor Q_p. The missing comparison is not justified by
base change of coefficient modules. L007 tests one proposed way to
supply it; no nonexistence theorem for other motivic lifts is asserted.

## Mathlib

Full coverage: **not checked**. The cited maps support this audit;
they do not match a global Kummer-membership theorem.
