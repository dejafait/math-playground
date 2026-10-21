# Upper-face companion support-separation attempt

STEP_ID: YM-20261006-056-companion-support-separation

Reuse the unchanged SPECIALIZE assessment literature/2026-09-26-current-target.md.
The main gap is the complete Ward response and its cutoff dependence; the
intermediate test is whether the two d-containing lines of L040(3) vanish
in the a^2-scaled upper-face sum. A positive test would leave its exact
three-dimensional H,L trace for comparison with L039. Retain all colors
and transverse strips. Continue if separated Green columns and compact
residual consistency close the sum; otherwise isolate the failing term.
L040 and ATTEMPTS/013 distinguish this test from the failed interior
exterior bound. L024's local projection estimate is only a comparison.

Work in progress: L029(10) identifies the d row as a top circulation.
A partial transverse spectral expansion should give a smooth extension
of Sigma r_d of size O(a^3) on the compact residual support, including
five physical derivatives. L028's centered consistency would then give
A_0 Sigma r_d = O(a^7) entrywise and O(a^5) in ordinary l2. The H,L
Green columns have l2 norm O(a^-1); the d column has norm O(a^-1)
by the spectral gap and curvature projection. These would bound every
V entry with a d index by O(a^4). These are proposed estimates until
proved with the mixed Dirichlet/Neumann endpoint formulas.

The two selected lines also contain u_f v_h and u_c v_b. A uniform
relative form bound on L040's scalar compressed residual would give
|v_h|+|v_l|+|v_b|=O(a^-1). With L040(13), this would remove all
selected terms at a^2 scale except u_c v_b, for which it gives only
O(1) after summation. No diagonal regularity or signed cancellation
is assumed. The full companion limit, L019 compensation, other jets,
full logarithm, finite matching, reflected error <=c_box/2 and the
continuum and infrared construction remain unresolved.

Completed: L041 proves the proposed separated-column estimates, including
the Neumann and Dirichlet endpoint inverse formulas. Its compressed
relative form estimate bounds the H,L residual block by O(a^-1).
The borderline u_c v_b sum closes by the exact identity
v_b=(Z(v)-Z(v'))/2: the flowed coefficient has neighboring difference
O(a^3), so pinned summation by parts gives an O(a^-1) signed sum.
Consequently both d-containing lines together are O(a^-1), and their
a^2-scaled sum tends to zero. The full proof and qualifications are in
../lemmas/L041-upper-face-companion-separated-terms.md; the proposals
above are retained as the reasoning checkpoint, not unresolved premises.
Exact checks pass for 24 endpoint inverse cases and 616 pinned bilinear
basis pairs. They do not numerically certify the asymptotic proof.
The H,L-only trace is the remaining companion target; its scaled limit
and all slower terms still require work under the unchanged assessment.
