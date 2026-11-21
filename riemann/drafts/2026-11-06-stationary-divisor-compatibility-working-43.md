# Stationary actual-divisor compatibility — working checkpoint

Completed later in this invocation as unaudited L879,
`lemmas/L879-stationary-radial-graphs-have-one-phase-line.md`.
The canonical proof establishes a global phase line and an exact
odd-contact criterion for the mass gap. The original equality remains
open because actual stationary odd-contact realization or exclusion
is unresolved. The notes below preserve the earlier unfinished stage;
they are not a separate proof or independent audit.

Approved target: the exact TARGET in
`literature/2026-11-06-stationary-graph-phase-components.md` (EXPLORE,
saved before invocation). One bounded proof attempt, 6 November 2026.
Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Intermediate use: determine whether a regular stationary radial graph
necessarily attains the sharp mass threshold needed in L868.

Essential inputs: L847's full actual form, angular orientation and
compact homotopy; L878's accepted coordinate-torus variation as a
comparison; the assessment's known pullback-variation and holomorphic
finite-zero factorization inputs. L864–L866 assume nonnegativity and
are not sign premises here. Product, two-period and dual-jet stops stay.

Partial reasoning, not yet a verified result:

- With A=Du, H=I-iA and Q=F(Phi_u) det H, a supported real radial
  variation v should give delta Q=-i div(Q H^(-1)v). Integration by
  parts on a nonzero patch should give delta B equal to the mean of
  |Q| grad(arg Q) dot Re(H^(-1))v. The real matrix is
  (I+A^2)^(-1), invertible when det H is nonzero. Check indices,
  support, modulus differentiation and both implications explicitly.
- Compactness of the graph and isolated zeros of actual G put its
  G contacts on finitely many vertical/horizontal angular fibers;
  diagonal contacts lie on theta1=theta2. This is a finite covering
  by lines, not an assumed finite set of contacts.
- In an open edge between intersections, the density either connects
  the adjacent nonzero cells or vanishes along the whole edge. A
  full single-G edge has its actual multiplicity m in a transverse
  expansion, with nonzero leading coefficient from the own-angle
  derivative and J. Its two phases should differ by (-1)^m. The
  squared diagonal should have even order and preserve phase.
- If these edge checks and adjacency are valid, stationarity forces
  one global complex line of density values, but possibly two signs.
  An odd-multiplicity fiber can flip sign. This would identify the
  exact residual cancellation rather than prove B=|M|.

Remaining work: complete the finite-line and edge argument without
assuming isolated, transverse or simple contacts; account for all
line intersections, simultaneous contacts and diagonal coincidences.
Do not infer a global graph or even a local exact germ from a leading
jet. Stop automatic phase alignment if odd contacts remain compatible.
No global counterexample, equality, existence, compactness or RH claim
has been established by this checkpoint.
