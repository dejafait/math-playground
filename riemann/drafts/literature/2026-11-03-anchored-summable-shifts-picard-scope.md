# Proposed mathematical scope: summability in the existing Picard iteration

TARGET: Test whether Lev's small-sup Picard iteration preserves coefficient l1 for L693's smooth anchor-cancelling prescription, yielding sum_m |e_m|<infinity with |e_m|<=1/8 and unit masses.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step 110's exact summability search and comparisons in drafts/literature/2026-11-03-anchored-fourier-gap-summable-shifts.md. No inspected result states this fixed-anchor l1 conclusion; no originality claim follows.
SOURCE_EVIDENCE: Lev, RMI 38 (2022), Lemma 4.3 p.1984 (4.6), Sections 4.6--4.10 pp.1986--1988, and arXiv:2007.09930v3 (4.10), (4.19)--(4.26), provide the individual coefficient majorants, small-sup fixed point, and derivative/unit-mass prescription. Full relevant proof cases were read in step 110; L693 supplies the audited anchor specialization.
COMPARISON: The source has coefficient-sup output and summable-kernel bounds on individual nonlinear terms, not a stated coefficient-l1 persistence theorem. Original Kargaev weighted zero-prescription results and KL16's l2 construction use different spectral data. Only the regularity difference is proposed for proof.
GAP: Establish l1 persistence and convergence/limit identification for the existing small-sup iteration on smooth data without assuming a small Wiener norm, and then retain the anchor, cap and unit masses in the specialization.
REASON: This is one concrete applicability difference supported by inspected primary estimates, not an assertion that smooth data automatically yield summable shifts. A proof requires more than citing Theorem 4.8; reproving the bounded prescription theorem is unnecessary.
SCOPE: Real shifts, fixed anchor delta_0, half-lattice m+1/2, all unit masses, |e_m|<=1/8, some nonempty gap inside (0,2*pi); a=1/8 and b=3/8 fixed before h. No effective l1 bound, fixed gap width, finite-tail rate, complex frequency or Xi transfer is covered.

This new scope is proposed for separate approval on the following turn;
no mathematical attempt or proof of summability occurred in step 110.
The main target remains actual-Xi all-degree mixed positivity. The
plausible downstream use is finite-tail analysis with actual unit weights;
summability alone would not establish the required finite logarithmic
bound, H/support or Xi realization.

Use the exact primary statements, proof-case reading limits and search
record in the completed source assessment above. Source links:
[published Lev article](https://ems.press/content/serial-article-files/39104),
[arXiv v3 Sections 4.3--4.10](https://arxiv.org/html/2007.09930v3#S4.SS3).
Keep L693's correction S=-exp(pi*i*t)*chi(t) and its fixed-band multiplier
Psi. The data fed to the source's fixed point are the reflected product
(Psi*S)(-t); check the conventions instead of equating them with S.
All constants/cutoffs used to set the small-sup threshold must be fixed
before h is chosen. Additional smallness may reduce that threshold;
no threshold is allowed to depend on the unknown solution or on h.

The bounded test is whether the termwise coefficient estimates control
Picard iterates and their limit in l1 while retaining the source's small
sup radius. Finiteness of an input Wiener norm and smallness of that norm
are different requirements. Establish the actual sufficient condition,
including a complete limit argument, rather than asserting the desired
conclusion. No such estimate is proved in this assessment.

Continue if that condition applies to the exact smooth prescription at
some h>0 and the same fixed-anchor measure results. Stop this proposed
mechanism on an unsupported stronger-norm smallness assumption, altered
masses/anchor, or a failed persistence/limit estimate, preserving the
specific reason. Failure would concern this mechanism only. Tail rates,
rational W, spatial moments, complete charges, H/support and actual-Xi
signs remain unresolved. Mathlib coverage is not checked.
