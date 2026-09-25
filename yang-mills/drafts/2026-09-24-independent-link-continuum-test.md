# Independent-link continuum test, 2026-09-24

## Preflight and bounded target

The notebook initially has no lemmas, attempts, or unfinished local changes. Changes in other notebooks and shared infrastructure are outside this step and are preserved. The complete overview and empty DAG were read before selecting work.

Gap: construct a nontrivial continuum theory with physical excitations of finite positive energy; a fixed-lattice gap does not supply this.

Intermediate target: at Wilson action coefficient beta = 0 (infinite bare gauge coupling, not zero bare coupling), compute the continuum law of smeared SU(2) plaquette traces and the Hilbert space reconstructed by reflection positivity. This exactly soluble endpoint tests whether retaining local random fluctuations alone certifies physical nontriviality.

Plausible downstream use: identify a concrete observable criterion that a continuum-limit construction must preserve, independently of proving a gap. Later unresolved work includes a coupling trajectory, renormalized gauge-invariant observables, all axioms, and a finite positive infinite-volume physical mass.

Discriminating test: choose the normalization giving a finite nonzero smeared covariance. If positive-time centered observables have nonzero reflection norm, investigate surviving physical states; if the limiting law has only contact covariance and all centered polynomial reflection norms vanish, stop this direct endpoint route. The negative test would not rule out scale-dependent couplings or nonlocal observables.

## Reasoning checkpoint

For independent Haar SU(2) links on Z^4, let W_x be the unnormalized fundamental trace around the (1,2) plaquette at x. Expected calculation: E W_x = 0 and E W_x W_y = delta_xy. Products on disjoint link sets are independent; the plaquette dependence graph has bounded degree.

Candidate normalization: X_a(f) = a^2 sum_x f(ax) W_x. Its covariance should approach integral f g. For each fixed r >= 3, a connected-tuple cumulant count should give kappa_r(X_a(f)) = O(a^(2r-4)); this would give Gaussian white-noise limits via moments and tightness. The needed justification is that the number of connected r-tuples is O(a^-4), not O(a^-4r), and that moment convergence actually implies law convergence.

For white noise, positive and negative open time half-spaces are independent. Thus E[conj(F(theta phi)) G(phi)] = conj(E F) E G for polynomial observables supported strictly at positive times, making the OS quotient one-dimensional. This must be proved for the whole polynomial algebra, not inferred solely from one vanishing two-point function.

Primary source checked: Jaffe and Witten, *Quantum Yang-Mills Theory*, section 4, p. 6, at https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf. It explicitly requires finite mass as well as a positive gap. Source audit and proof remain to be completed in canonical files.

## Simplification found during the test

The fixed-orientation plaquette traces are in fact jointly independent at beta = 0 on the infinite lattice. In any finite set, choose a plaquette whose first coordinate is maximal. Its right edge occurs in no other chosen plaquette. Integrating that Haar link makes any function of this plaquette trace independent of all the remaining links. Remove the plaquette and repeat. This finite peeling argument avoids both a dependent-variable central limit theorem and a connected-tuple estimate. It would fail as stated for arbitrary orientations or periodic wraparound; neither is in the proposed lemma.

The completed [canonical proof](../lemmas/L001-independent-plaquette-noise-has-trivial-reflection-space.md) uses this stronger observation, weighted characteristic functions for convergence of laws, and cumulants for convergence of polynomial moments. It asserts only the limit of the selected plaquette field, not triviality of all possible observables of lattice Yang-Mills. Earlier prospective wording above is retained as the saved reasoning checkpoint, not as an outstanding task.
