# Step 513: fixed-H2 complete-pairing working record

Gate: the invocation-start EXPLORE assessment is
`literature/2026-11-11-fixed-h2-cell-train-complete-pairing-512.md`.
One research attempt only; no source search or new source theorem import.
The main gap is actual-Xi positivity, L030-L032/C032a. The bounded target
is detection by one fixed neutral profile at a prescribed H2 budget,
not an independent positive margin or an RH resolution.

The read inputs are L742(8)-(12) and its Fourier-convention calculation,
L744(1),(6), C744q's hypothesis and sufficient threshold, and L743's
return/correction limitations. Ready Suzuki compact-test coverage is
reused from steps279/283/512. The signed Gram-dual and removed-remainder
stops remain in force for their exact unpaid estimates.

Initial reasoning, saved before the complete-pairing attempt:

- Disjoint cell supports should give the exact norm identity for each
  derivative order 0,1,2. Neutral moments and the actual smooth generator
  domain must be checked before using the energy.
- With F(z)=integral f(x)exp(-izx)dx and P(w)=sum c_j w^j, the train
  transform factors as F(z)P(exp(-i ell z)). The unconditional zero side
  pairs z with conjugate(z), not a modulus square at z.
- Smooth-strip decay gives absolute convergence for each fixed train,
  but alone gives no uniform control as its degree grows. All points
  with equal exp(-i ell z) must be grouped. A single quartet is not a
  sign certificate.
- Possible bounded test: assume all admitted trains are nonnegative;
  their two-cell sections bound the complete translated correlations.
  Strict H2 slack allows small neutral profile perturbations. Whether
  these facts isolate a nonreal zero without an unpaid infinite tail
  is the precise question to investigate, not an established premise.

Continuation requires a complete negative energy at the unchanged
budget, or a precisely qualified alias/tail/realization obstruction.
Finite-K transfer to every eventual K_R is a separate obligation.

## Developing the bounded-correlation test

Assume for contradiction that every admitted fixed-profile finite train
has nonnegative energy. A two-cell principal section then gives
|H(f,tau_m f)|<=E_ell(f) for every admissible profile and every integer
m>=1. Write q_m(v)=H(v,tau_m v). For a strict-slack reference f0,
the profiles f0+epsilon v and f0-epsilon v remain admitted for uniformly
small epsilon when v ranges over a bounded H2 set. The exact quadratic
second difference isolates 2 epsilon^2 q_m(v); hence q_m(v) is bounded
uniformly in m on each such set. Complex polarization also bounds
H(v,tau_m w) for independent bounded neutral profiles v,w.

Choose a neutral smooth phi supported in an interval of length w<ell/2.
Its translates inside a single cell have uniformly bounded H2 norms.
Their relative shifts cover [-ell/2,ell/2], so the preceding cross bound
controls H(phi,tau_t phi) for every real t>=0, not just lattice t.
This is the proposed way to retain and resolve aliases without assigning
individual lattice atoms a favorable sign.

For an off-line ordinate z0 with Im(z0)<0, choose phi=(D^2-1/4)eta
with eta a sufficiently narrow nonnegative bump, so both F_phi(z0)
and F_phi(conjugate(z0)) are nonzero. The complete correlation is
sum_z a_z exp(i t z), a_z=r_z F_phi(z)conj(F_phi(conjugate(z))).
If it is bounded, its one-sided Laplace transform is holomorphic in
Re(s)>0. In Re(s)>1/2 absolute convergence gives sum_z a_z/(s-i z).
The latter has a normally convergent meromorphic continuation and a
nonzero residue at s=i z0. No rightmost zero is needed. Verifying all
constants, signs, convergence, and strict-slack quantifiers is ongoing;
this paragraph was saved reasoning before the completed write-up.

## Completion

The derivation, all hypotheses and full tail argument are now canonical
in [C744r](../lemmas/C744r-fixed-h2-neutral-train-zero-detector.md).
The working paragraphs above are retained as unfinished-stage evidence,
not an additional proof or a separate audit. The finite-K transfer was
resolved by unchanged-profile zero-padding. A separate conceptual audit
is still required; no RH sign or actual off-line zero was obtained.
