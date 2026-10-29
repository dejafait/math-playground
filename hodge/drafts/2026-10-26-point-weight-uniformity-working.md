# Point-weight normalization specialization — step 561

Invocation-start gate: SPECIALIZE in drafts/literature/2026-10-26-point-weight-uniformity.md; exact target: Determine whether L111's fixed Kodaira–Spencer normalization forces L168's weights mu_z to be independent of the reduced split point.

Main gap: primitive Hodge realization and existence of the conditional F. Intermediate target: compare the oriented finite Ext trace and L111's actual incoming KS-plane pairing. Downstream use: replace point-dependent coefficients in L168's actual section quartic by one common coefficient, if justified. This does not evaluate section quadrics or the complementary operation.

Inputs read: full L111 and L168, plus targeted upstream normalization searches and ATTEMPTS/092–094. Existing unfinished notebook work is preserved. No cross-notebook input. Reuse the inspected primary residue assessment; no new literature discovery is planned.

Bounded test: for parameters x,y at z write sigma_B=f_z dx wedge dy. L111 (9) identifies the residual middle pairing, before the common relative trace scalar kappa, with -8 lambda f_z(z). L168 (10) gives mu_z=4 kappa^2 tau_z(epsilon_{x,y})/bar(c_0). Need verify the precise orientation comparison between its arrows (-y,x)^t,(x,y) and Nayak–Sastry I C.1–C.2/C.5.4, then apply II 5.4.2. Continue if both local factors have the same parameter coefficient up to one justified global scalar; otherwise preserve symbolic weights and name the mismatch. No equality is yet claimed.

Unresolved: the Ext-to-residue sign and the comparison of the fixed base trace with the primary canonical normalization. Empty/singleton support must remain valid. No actual section values, F existence, genericity or integrability are assumed. No mathematical script is needed for this two-parameter comparison.

Completed specialization: L169 gives the full comparison. Under the fixed resolution arrows the unsigned-transpose complex maps to internal Hom by (1,-I,-1), so the oriented Ext generator has trace -delta_B f_z(z). The actual middle pairing is -8 kappa lambda f_z(z). Their ratio in L168 (10) gives mu_z=delta_B kappa/(2 lambda), independent of z. The common scalar is justified globally by comparing dualizing isomorphisms on the connected projective K3 surface. This is a conditional REPRODUCTION, not an actual section-quartic computation, exclusion or primitive-realization result. A separate critical audit is pending; the newly written audit assessment is REVIEW_REQUIRED.
