# Gaussian zero-mode subtraction — calculation checkpoint

The saved [SPECIALIZE assessment](literature/2026-10-03-gaussian-regulated-modular-zero-mode.md)
covers exactly the regulated objects in this calculation. No source
refresh or spectral-sign calculation is part of this step.

Put x=e^(2u), f(t)=ψ(t)−1/(2√t) and R(t)=t^(−1/2)ψ(1/t).
L016's scalar Poisson identity gives f(t)=R(t)−1/2. Applying
P=2D_u²−1/2 to the complete prefactor gives

\[
 h_\varepsilon(u)=e^{u/2}
       [12x f'(x+\varepsilon)+8x^2 f''(x+\varepsilon)],
 \qquad
 \partial_\varepsilon h_\varepsilon(u)=e^{u/2}
       [12x f''(x+\varepsilon)+8x^2 f'''(x+\varepsilon)].
\]

At ε=0, P annihilates the zero-mode generator e^(−u/2)/2,
so h_0 is the actual theta kernel on the whole line. The modular
identity makes that kernel even; reflection therefore has the same
limit, with no extra factor of two.

For 0<x≤1 and 0≤ε≤1, the argument x+ε lies in (0,2].
R'' and R''' are bounded there: on (0,1] their differentiated
dual sums have bounds C t^(−2j−1/2)e^(−π/t), and on [1,2]
they are continuous. Hence |∂_ε h_ε(u)|≤C e^(5u/2) for u≤0.

For x≥1, use the original sum instead:
f''=ψ''−(3/8)t^(−5/2) and
f'''=ψ'''+(15/16)t^(−7/2). L016's derivative tails and
x+ε≥x give |∂_ε h_ε(u)|≤C e^(−5u/2) for u≥0.
Integrating in ε would give

\[
 |h_\varepsilon(u)-k(u)|\le C\varepsilon e^{-5|u|/2},
 \qquad |k_\varepsilon(u)-k(u)|\le C\varepsilon e^{-5|u|/2}.
\]

This is the desired whole-line estimate, including the moving
transition x comparable to ε. It would imply the weighted L¹ limit
and uniform convergence of the Fourier transform with two real
derivatives. It supplies no Fourier or Laguerre sign: a uniform
absolute error is not a relative sign margin at unbounded frequency.
This is a specialization of the covered scalar theta tools, reported
as REPRODUCTION, without a claim of originality.

Remaining write-up checks at this checkpoint: audit P and the three
derivatives of R, justify every compact differentiation, integrate
the common envelope, and store the resulting proof in lemma format.
The required threshold is weighted error tending to zero; compact
convergence alone would still be insufficient. No RH candidate appears.

Completed: [L357](../lemmas/L357-gaussian-zero-mode-subtraction-repairs-weighted-convergence.md)
now supplies those checks and the full proof, including uniform O(ε)
control of the first Laguerre expression in absolute error. The exact
rational audit in `scripts/gaussian-zero-mode/check_derivatives.py`
checks P, the three dual derivatives, the zero-mode coefficients and
the envelope integral 132/125. No spectral sign is tested in this step.
