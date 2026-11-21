# Quantitative high-endpoint source comparison604

12 November2026; one literature-only step. This file replaces its saved
unfinished working record. No local compactness, rate or sign is proved.

The main gap remains L030-L032/C032a actual-Xi positivity. The intermediate
target is an explicit norm remainder for C744z(4)'s exact neutral endpoint
compression. Its downstream purpose is a finite signed comparison with a
paid infinite complement. Finite signs, H2, c_* verification, non-neutral
directions and global assembly remain independent gaps.

## Primary statements and essential cases actually read

1. Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, GSM99,
   first edition, PDF version12February2009,317 pages,
   [author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
   Theorem1.3(iii), p41, is Parseval for a complete orthonormal set;
   Theorem1.7, pp43-44, is Hilbert-space orthogonal projection/best
   approximation. Lemma5.5, p128, gives the compact-operator closed
   star-ideal. Theorem6.7, p137, gives compact singular-value expansions.
   Lemma6.8, pp137-138, says compact K and strongly convergent bounded
   operators B_n imply norm convergence B_n K. Read its full proof,
   especially finite-rank reduction, and the following left-shift
   counterexample to unrestricted multiplication on the other side.
   These are qualitative results, with no prescribed N-rate. The neutral
   projections and local compactness hypotheses still need verification.
   Prior representation/inverse coverage of Theorems2.13/2.18 in C744z
   and assessments596/597/601 is reused, not newly reproved.

2. J. Descloux, N. Nassif and J. Rappaz, *On spectral approximation.
   Part2. Error estimates for the Galerkin method*, RAIRO Analyse
   numerique12(2)(1978),113-119,
   [primary journal archive](https://www.numdam.org/article/M2AN_1978__12_2_113_0.pdf).
   Read Section1, including Theorems1-3 and its self-adjoint case;
   Section2's best-approximation, resolvent and invariant-subspace proof
   cases. Its continuous sesquilinear forms a,b live on a complex Banach
   space X, with a coercive, finite-dimensional X_h, operator-consistency
   P1 on X_h and density P2. An isolated nonzero finite-multiplicity
   eigenvalue is selected for Theorems1-3. The projections are a-Galerkin
   projections. Estimates use generic constants and eigenspace
   approximation quantities. They neither establish the missing local
   P1/rate nor identify those projections with our L2 neutral ones.
   This is inspected nonmatching coverage, not an imported local bound.

3. V. Hernandez-Santamaria, S. Jarohs, A. Saldana and L. Sinsch,
   *FEM for1D-problems involving the logarithmic Laplacian: error
   estimates and numerical implementation*, arXiv2311.13079v3,
   19May2025,
   [pinned primary text](https://arxiv.org/html/2311.13079v3).
   Read Theorem1.2, definitions(1.7)-(1.11), Lemmas4.1/4.2 and proofs,
   Theorem1.2's proof and Proposition7.2's statement/min-max proof case.
   Theorem1.2 treats the Dirichlet logarithmic Laplacian on an interval,
   forcing in the bounded weighted log-Holder space Y of(1.8), the
   uniquely solvable alternative of Theorem1.1, and piecewise affine FEM.
   Its energy error is C times ell_mod(h)^alpha times ||f||_Y for small h;
   alpha,C and onset are existential. Lemma4.1 assumes uniform discrete
   inf-sup; Lemma4.2 obtains it non-effectively from uniqueness/density
   by compactness and contradiction. Proposition7.2 asserts fixed-index
   eigenvalue convergence; it is not a uniform norm remainder. None is
   imported for arbitrary L2 inputs, neutral cosine constraints, or our
   digamma multiplier. No independent audit of its eigenvalue proof or
   stiffness-matrix normalization was performed or used.

## Search record, leads and local comparison

Actual queries included `compact operator finite rank orthogonal
projections norm convergence collectively compact Galerkin error estimate
Osborn 1975`, `Boffi finite element approximation eigenvalue problems
compact operator norm estimate Ritz projection 2010 pdf`, `Teschl
mathematical methods quantum mechanics compact embedding quadratic forms
compact resolvent theorem pdf`, `logarithmic Laplacian Galerkin error
eigenvalue approximation`, `Weil neutral compact resolvent finite section
logarithmic`, and the exact title of arXiv2311.13079.

Osborn1975's AMS PDF returned403 and its DOI fetch failed. No theorem
from that unread paper is used; its DNR continuation was accessible.
Boffi2010 remains an unused lead; his author publication listing was
inspected for provenance, not theorem evidence. The external repository
LeonardSEO/semilocal-zeta-operator-theory's FROZEN_SPECIFICATION.md,
dated24July2026, was screened only at Sections3-4: it asserts compact
resolvent and introduces a different quotient/polar-transport axiom.
It supplies no inspected proof of the present norm bound and is unused.
Search snippets, secondary mirrors and that project specification are
not mathematical inputs. No essential source-access blocker remains for
the bounded elementary specialization described below.

Local reads: C744z Sections1-3 and formula(4), C744v Sections3-4,
C744w Section2, C999k Sections1-2, mixed-uniform-tail stop537, and the
relevant source-comparison passage in assessment561. Existing603's
nomination screening and ready form/inverse coverage are reused.
The scalar stop537 does not obstruct a cutoff-dependent norm error.
The diagonal-only and fixed-prefix middle stops in C744z are preserved.
No higher-endpoint certificate was found in these checked paths.

## Specialization still to be attempted

Let H_N be the intersection of H0 with the raw cosine span0:N-1, and
P_N its exact L2 orthogonal projection on H0. The future target is a
bound for the normalized operator S3, with E=A0^-1/2 and the actual
K=P0T|H0,J=P0U|H0 retained. It asks for an explicit epsilon_N tending
to zero for the difference between S3 and the operator equal to its
exact P_N direct-sum P_N compression on the finite space and identity
on its orthogonal complement. This is a target definition, not a result.

The source-covered ingredients are best approximation, Parseval, positive
form representation and bounded-operator products. The missing local
work is quantitative: control the raw high-mode energy of E uniformly;
correct truncation to exact neutrality with a quantified low-mode moment
right inverse; pass to the true orthogonal projection; bound every
diagonal and off-diagonal block, including products crossing the cutoff.
The explicit logarithmic diagonal lower envelope in C744v(5) and moment
formulas in C744w(8)/C999k Section1 make this a concrete specialization,
without requiring an uninspected PDE regularity theorem. No rate,
projection constant or product estimate is established now.

Keep the c_*=8.9e-18 source-computation qualification, the whole-neutral
form/core qualification, and original analytic/arithmetic contracts.
Do not assume P_N commutes with A0 or E. Do not replace the restricted
inverse by a projected unrestricted inverse. Also, P_N E P_N need not
equal a finite Galerkin inverse square root: certified finite entries
would be a subsequent task. C999l/q's free-profile Euclidean margins
cannot be reused as normalized-coordinate margins.

Continue only if an explicit remainder tending to zero pays every block
without a positivity premise for S3. A later sign certificate would need
a certified finite normalized margin gamma_N and total norm/entry error
strictly below min(1,gamma_N). A bound with huge c_*-dependent constants
may be mathematically valid but computationally useless; report its size
honestly. Stop this specific specialization if it leaves uncontrolled
projection/product terms, and preserve partial reasoning. No RH claim
or finite sign follows from source coverage. Full Mathlib coverage is
not checked. No novelty is asserted.
