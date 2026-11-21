# Exact spatial clearing — working step 83

Invocation target and assessment are unchanged from step 82:
`drafts/literature/2026-11-03-inner-spatial-rational-response.md` (EXPLORE).
Main gap: actual-Xi mixed positivity; the immediate unresolved estimate
is the full-cube joint resolvent lower bound against original D.

Test: retain L684's exponentially accurate undisplaced resolvent at
u=-1, but replace its limiting local-node expansion by an exact spatial
polynomial. For central support 2L, write F_e=H_e+E_0 where
H_e=1/(R-x*z)+sum_changed[W_a/(R-a*z)-W_b/(R-b*z)].
Here |E_0|<=1000*n*exp(-n/6000) on |z|<=1/32 by L684 (4).
Clear the 4L changed/old node denominators plus the anchor. The resulting
polynomial has degree at most 4L, and evaluation at z=R/x leaves exactly
the anchor's product of distances. The maximum modulus principle for
the reversed polynomial should bound its observation cost explicitly.

Expected cost is O(L*log(n/L)+L), with no 1/n additive approximation.
Continue if this stays below the known 1/6000 base-error exponent and
the 79/30000 original-D margin for a fixed positive support fraction;
otherwise retain the failed cost as a mechanism-specific obstruction.
No bound is yet asserted in this working checkpoint. All products,
residues, and one displacement vector remain unchanged. The full cube,
L683 audit, H/support and actual-Xi realization/signs remain open.

Local overlap: L670/L671 concern complete angular clearings and their
coefficient/Mahler costs, whereas this test fixes u=-1 and clears only
the finite spatial replacement response. L650's close-pair individual
dual stop must retain its stated broader-family qualifications; no
unpaid pole-isolation norm or arbitrary residue lower bound is assumed.

Completed: the exact extraction works and is recorded canonically in
[L686](../lemmas/L686-exact-spatial-clearing-sparse-displacements.md).
It applies to a fixed small positive fraction of shifted indices at
arbitrary locations, with an absolute onset. The original limiting
approximation is not used. Its displayed full-cube certificate is
negative; no full-cube bound or countersequence is obtained. The
checkpoint retains the unchanged approved target and qualifies the
unproved combined-block continuation.
