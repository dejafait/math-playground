# Complete density asymptotic — critical-audit coverage

TARGET: Critically audit L282's complete-density N^2 asymptotic, including uniform polynomial approximation, boundary-layer control, fixed-mode normalization, and strict nonvanishing for the exact product bump.
CHECKED: 2026-10-25
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the ready 2026-10-25-density-response-separated-kernel-asymptotic.md scalar/trace comparison and ATTEMPTS/047–049; searched lattice Green polynomial approximation, sparse matrix-function decay and lattice Schur-product Green functions; inspected Benzi–Razouk's primary Theorem 3.4 and its graph-power and diagonalization proof, rather than relying on search snippets.
SOURCE_EVIDENCE: Benzi–Razouk, ETNA 28 (2007), 16–39, sections 3.2–3.5, Proposition 3.2 p. 20, Theorem 3.3 p. 21 and Theorem 3.4 with proof pp. 24–25; reused Dowker 1207.2096v2 sections 7–8 (29)–(37), pp. 10–13, and the prior assessment's precise Lawler–Limic, Ginovyan–Sahakyan and Michta–Slade exclusions. Read L282's full proof, L281's bound/tail argument, L003's relative-mode conventions, L002's explicit-bump passage and histories 493–494 for scope comparison, without accepting their estimates.
COMPARISON: Polynomial graph propagation is a standard input; the inspected analytic matrix-function theorem does not certify uniform approximation at a closing spectral gap, nor the complete density's entrywise reversed product. The prior scalar identities remain usable with their exact endpoint conventions. No inspected theorem imports the full density limit, coefficient or strict sign; these are the explicit local claims to audit.
GAP: Independently verify L281's tail and L282(8)–(25), especially weighted spectral errors uniform in N, row/column estimates for the reversed product, finite-range boundary passage, actual source-field convergence, factor 6/64 and strict sign for the exact product bump. No mathematical acceptance or repair occurs in this review.
REASON: Approve exactly the saved critical-audit target as a bounded direct audit using ready scalar coverage and the newly inspected polynomial-method comparison; no inaccessible source is essential. EXPLORE authorizes checking the local argument, not assuming its new estimates or certifying originality.
LITERATURE_REASON: The supervisor required separate approval of this newly registered audit; the polynomial/boundary mechanism was not explicitly compared in the prior scalar-kernel assessment. This turn fills that specific source-scope gap and does not repeat browsing for the balance target.
SCOPE: Exactly TARGET for SU(2), even N>=2, a=8/N, fixed cube, all boundary-contained pins, boundary-fixed gauges, all normal links, both density determinants, both source orders, three colors and L002's exact product bump, on L280's real source domain. Includes auditing L281's essential tail input; no action/insertion cancellation or continuum claim.
COVERED_TARGET: Critically audit L282's complete-density N^2 asymptotic, including uniform polynomial approximation, boundary-layer control, fixed-mode normalization, and strict nonvanishing for the exact product bump.

## Original registration, retained with its gate superseded

## Exact proposed scope and evidence to retain

Essential input IDs: L002 L003 L280 L281 L282. No other notebook is
needed. Preserve SU(2), even N>=2, a=8/N, the fixed cube, all-face
boundary-contained pins, boundary-fixed gauge transformations, every
normal link, both density determinants, both source orders and all
three colors. Retain the real source domain of L280.

Unlike the upper bound, strict nonvanishing uses the actual formula
f_*(x,t)=rho(x)tau_0(t), not just nonnegativity and support. Its use
is explicit in L282(1),(24)–(25). Do not silently extend the result to
arbitrary test functions or use inverse-square reflection positivity.

The audit's discriminating checks are:

- Verify (8)–(14), including normal endpoint eigenvectors, uniformity
  over N, and row/column estimates for both determinant terms.
- Verify the reversed-displacement Fourier product (15), the scalar
  d_* and the order of limits controlling all boundary layers.
- Verify strong convergence of the actual C* source fields on the
  relative domain, including zero edge indices and fixed-mode tails.
- Check (22)'s factor 6/64 and L281's complete uniform external tail
  before any infinite-series passage.
- Check that the exact product bump makes the mixed pairings strictly
  positive, rather than inferring it from a norm or a density sign.

Continue if every load-bearing step survives these checks, or repair a
specific error while preserving evidence. Otherwise identify precisely
which claimed limit, constant or sign fails. Neither acceptance nor
failure would resolve the full action/insertion cancellation, uniform
higher remainder, interacting continuum axioms or physical mass.

The preceding text records the original proposal. The separate source
comparison below now approves its unchanged target; critical-audit
acceptance is still outstanding.

## Completed primary comparison (2026-10-25)

M. Benzi and N. Razouk, *Decay bounds and O(n) algorithms for
approximating functions of sparse matrices*, **Electronic Transactions
on Numerical Analysis 28** (2007), 16–39,
[published primary PDF](https://etna.ricam.oeaw.ac.at/vol.28.2007-2008/pp16-39.dir/pp16-39.pdf).
Read section 3.2, Proposition 3.2, p. 20; section 3.3, Theorem 3.3,
p. 21; and section 3.5, Theorem 3.4 and its full proof, pp. 24–25.
The graph-power argument preceding Theorem 3.4 proves that matrix
powers have zero entries beyond their degree in graph distance.
The theorem assumes diagonalizability, spectrum in a compact connected
set F and analyticity on an enclosing region; its entrywise decay
bound includes the eigenvector condition number. The proof combines
polynomial approximation, diagonalization and graph propagation.
Proposition 3.2 gives size-independent band truncation when decay
constants are uniform. For the notebook's positive symmetric Delta,
diagonalization is applicable. However, L282(8) records eigenvalues
approaching zero, where the inverse function is singular: no fixed
analytic neighborhood as required for a uniform inverse approximation
has been supplied. This is a hypothesis comparison, not a disproof of
L282(13). That estimate concerns the complete density after incidence
and entrywise products, and must be checked as written. Graph locality
may be cited directly in the audit; no reproof of the general decay
theorem is needed. Its special composed-density conclusion is absent
from this inspected theorem.

Reuse the earlier density-asymptotic assessment's inspected Dowker
interval statements, with Dirichlet vertices and half-shifted Neumann
edges, including the constant edge mode. They support L003's conventions;
they do not certify the physical normalization of L282's generated
one-forms or its infinite external-mode passage. Reuse unchanged the
whole-space/killed scalar Green and Toeplitz comparisons there. In
particular Michta–Slade's massless inverse-square conclusion requires
d>2q, excluding d=4,q=2. L282 explicitly proposes finite weighted
spectral estimates instead, so this exclusion is not an access blocker
and is not grounds to reject the proof without auditing those estimates.

## Audit obligations beyond the inspected theorem statements

The graph result covers propagation of each fixed polynomial. It does
not establish L282(10)–(13)'s uniform error for the complete D_N, the
boundary strip estimate in physical norm, or the reversed-displacement
Fourier contraction. Check those explicit finite estimates and the order
N then polynomial degree, retaining the full density. This comparison
does not derive them or substitute a generic exponential-decay bound.

L003's exact tensor modes and L280(21)–(25) provide the recorded
framework for testing the source-field argument. Audit L282(20)–(21)'s
physical cochain normalization, source differences on their true grids,
three positive indices, zero edge indices and inverse tails. No unread
finite-element or continuum resolvent theorem is essential to that
explicit finite-mode test. Audit L281(4)–(16)'s reflected positive
factorization and rectangular trace estimates before using its tail.

L002 explicitly supplies a space/time product bump. L282(24)–(25)
uses that stronger hypothesis for its positivity argument; it cannot be
replaced by positivity for arbitrary reflected inverse-square profiles.
Check its scalar Dirichlet kernel and nonzero spatial derivative in
the mathematical audit. The source review establishes the scope of this
check, not its success. The coefficient 6/64 also remains an obligation.

## Search limits, duplicates, failures and decision

New bounded queries were `"lattice" "Green" "polynomial approximation"
boundary`, `"functions of banded matrices" "positive definite" Demko
decay inverse`, `"lattice" "Schur product" "Green function"`,
`Benzi Razouk decay bounds spectral functions sparse matrices 2007
theorem polynomial approximation pdf`, and `"lattice" "relative"
"density" "Faddeev" "asymptotic" boundary`. Secondary hits served
only as discovery. Benzi–Simoncini matrix-decay and spectral-projector
hits were leads, not imported theorems; their full arguments were not
needed. No failed search certifies novelty or absence of stronger work.

Scoped comparison of the two density work notes, the prior density
assessment, the local quotient audit assessment and histories 492–494
found the recorded derivation and proposed checks, not a completed
independent audit. ATTEMPTS/047's rearrangement stop, 048's insufficient
global norm and 049's gauge-identity obstruction remain unchanged.
They neither establish nor globally prohibit this direct polynomial
and relative-source audit. No cross-notebook result is used.

Decision: the unchanged audit is ready under EXPLORE. Its later RESEARCH
turn may be classified REPRODUCTION when checking the written result;
any uncovered replacement mechanism requires separate review. Accept
only after every essential estimate and normalization is independently
checked, or preserve the precise failed claim and determine its effect.
No lemma, mathematical script, candidate acceptance or mathematical
repair is produced here. Full and supporting Mathlib coverage remains
not checked. The audit could validate or overturn the density input
needed for future compensation tests; the full interacting, continuum
and infrared gaps remain unresolved either way.
