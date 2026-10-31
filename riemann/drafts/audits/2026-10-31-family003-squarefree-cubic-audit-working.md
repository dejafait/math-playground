# Squarefree cubic normalization — application audit

Approved target: L548's composite cubic normalization and unit modulus,
under the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-31-family003-squarefree-cubic-normalization-review.md`.
Main gap: actual-Xi all-degree positivity. This finite application can
remove one retained premise, leaving coefficients, remaining Gauss inputs,
arithmetic uniformity and signed-Xi transfer independent.

In-progress reasoning: for each good p the Euler definition gives
chi_p(x)^2=(x/p)_3 on units; both sides vanish on nonunits. Products
therefore agree on the whole composite quotient. Since n avoids S,
lambda is a unit modulo n; reindex the composite sum by y=lambda x.
The required phase is chi_n(lambda)^(-2), with no factorization of
Gauss sums. Import DR v3 (2.1)–(2.2) directly for the norm. Check n=1
by the explicit empty-modulus conventions rather than a nonprincipal
character theorem. No source blocker is currently identified.

Continuation test: all these equalities must hold for every ideal-
squarefree primary n outside S, including conjugate prime factors and
both residue degrees. A missing restriction or extra phase prevents
discharge. The complete argument and final disposition will be saved
in canonical L548; this working note is not a proof certificate.

Completed: the full specialization is now in L548, subsection
"Squarefree composite cubic normalization and modulus". The test
passes, including the zero extension, conjugate factors, both residue
degrees and n=1. The canonical proof imports the composite norm and
uses a single unit reindexing, not a CRT factorization. No mathematical
script was needed. The remaining premises retain their separate status.
