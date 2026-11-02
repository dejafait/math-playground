# Full angular Chebyshev energy: bounded test inconclusive

[C645q](../lemmas/C645q-complete-angular-hilbert-schmidt-energy.md)
records the full signed energy and a factor sqrt(m) comparison with
the angular root mean square of the largest operator norm. The varying
radius family is admissible, but the energy remains unevaluated at
the required exponential scale. The 32-family diagnostic in
`scripts/one-sided-hankel/angular-chebyshev-full-energy-screen.json`
is explicitly nonrigorous. The completed step is EXPLORATION, not
a mathematical stop on the family or a counterexample to the detector.

WHY IT FAILS: Replacing the largest norm by the Hilbert--Schmidt norm
does not cost an exponential factor, but the resulting signed angular
sum has not been uniformly bounded. Sampling found no convincing
countersequence radius; this neither certifies an upper bound nor
excludes an asymptotic radius sequence. No spatial-tail, quadrature,
or rounding enclosure supports the sampled values. A single favorable
angle or a small projected response would not repair that gap. The
preserved refinement tests a rigorous positive-real-grid endpoint
lower estimate on a compact radius band, including finite-node errors
and angular integration; the current result does not assert that it
works. Existing ellipse, inner-input, entry-sign and zero-evaluation
stops remain distinct and unchanged.
