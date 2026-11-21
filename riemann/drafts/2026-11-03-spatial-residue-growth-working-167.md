# Full spatial residue comparison — working record, step 167

The invocation-start EXPLORE scope is
`drafts/literature/2026-11-03-spatial-doubling-growth-attempt-scope.md`.
The exact approved target remains B_sp(n)=o(n), s=65/64, on |u|=1/2
for the one fixed L703 profile and the complete L666 family.

Main gap: actual-Xi all-degree positivity. Intermediate target: retain
the crossed spatial-resolvent residue and compare the complete spatial
maxima near i/2. A sublinear bound could pay L707's complementary
Jensen defect; a positive linear lower rate would stop this sufficient
mechanism. Amplitude/full charge, L657 accounting, H/support and Xi
realization remain independent. Neither conclusion is currently proved.

Inputs read: L666's exact family, L703's fixed profile, L709's entire
phase-sensitive proof, and the saved parent literature comparison.
L708's real-frequency identity and convolution proof are being reused.
Preserve the pole-free-extension stop and the two-arc complement stop;
neither decides the signed residue. No changed external theorem is used.

Proposed bounded test: for y_z=X+ic=-i(d+R/z), the upper contour
crosses a residue proportional to W_n(u,y_z) exp(-i n*y_z*v/A).
Only real v may be paired with S_e(v). Near the prescribed positive
bump its centered exponential rate is Phi_c(X)+c*omega_*/A.
First compare this rate on the spatial circles with the actual unit
normalization. This rate is only a diagnostic until the remaining
contour, both omitted physical tails, high frequencies, bump
cancellation and finite moment remainder have all been paid.

Continuation test: seek a strict positive rate margin after a matching
unit-disk upper bound, or a uniform sublinear signed ratio estimate.
If neither is obtained, preserve the exact obstruction and identify a
new quantitative input before another attempt. A large residue alone
does not lower-bound the complete signed maximum.

## Completed attempt

[L710](../lemmas/L710-signed-spatial-residue-and-centered-bump-reduction.md)
now proves the full signed residue reduction. The spatial pole lies
in the upper halfplane, so its inverse transform has a negative
halfline component. In particular the zero comb sample is nonzero;
it and all negative samples are included. The positive bump is paired
only on real frequencies. The remaining upper contour, the two high
frequency tails, both omitted physical tails and the exact finite
geometric remainder are paid in the stated normalized error.

The coefficient of the centered bump transform grows at least
exp(n/5000) on a fixed outer spatial disk and a fixed angular arc.
The whole-rectangle product upper bound and coefficient rate margin
are certified with complete Simpson/Taylor/logarithm remainders in
`scripts/one-sided-hankel/spatial-residue-rates-167.json`; all 13 checks
pass. The floating screen in `scripts/one-sided-hankel/spatial-residue-diagnostic-167.json`
is preserved as diagnostic evidence only and is not an input.

No growth lower bound follows without controlling the centered bump
transform. Its positivity on the imaginary axis does not bound its
modulus at the relevant complex points. Nor does the endpoint rate
bound S_(n,1): the remainder decomposition is local in spatial z.
L710's final section records one explicit sufficient pair of thresholds
for the bump maximum and the complete unit maximum. Both are unpaid.
An entire-function lower-bound theorem is not imported; if a new
essential theorem is needed, its source comparison requires a separate
literature turn. No actual B_sp decision or RH candidate is obtained.

The unchanged ready target can now be developed using this complete
signed formula. Repeating a coefficient-only estimate would not help.
The next bounded test must address the two quantitative inequalities
in L710 (19), or supply a different informative full-ratio bound.
Retain the actual L703 profile, n=12q+3, M=n/3, L666's full family,
L706's finite-n integrability, audited L708 and unaudited L709/L710.
