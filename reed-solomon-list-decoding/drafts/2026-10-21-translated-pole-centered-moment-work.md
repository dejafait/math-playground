# Centered translated-pole collision work — step 388

Approved target: Assess whether the centered second moment of L102's full translated-pole class distribution can certify a uniform fiber bound at T.

Main gap: arbitrary-center safety at 67/68 agreements; this step only tests L102's family. Ready assessment: drafts/literature/2026-10-20-translated-pole-centered-second-moment.md. Inputs: L102, C012a and foundations/02. Existing absolute and projective stops remain intact.

Working reduction (not yet verified): with s=67, C=binomial(1024,s), D=(65537-1)*65537^2 and mu=C/D, V=sum_z(N(z)-mu)^2=sum_z N(z)^2-C^2/D=D^(-1)sum_(chi!=1)|W_chi|^2. For ordered disjoint r-subsets A,B, let K_r count equal residues modulo (X-3)^3. Then sum_z N(z)^2=sum_(r=0)^67 binomial(1024-2r,67-r) K_r. Common factors are units since 3 is outside H. K_0=1 and K_1=K_2=K_3=0 by the degree of the difference of two monic polynomials. All larger overlap classes remain unknown.

Next within this bounded attempt: verify exact normalization, all overlap weights, positive mean gap and the required collision tolerance; save a complete arithmetic certificate. No bulk bound or actual large fiber is asserted. A sufficient upper energy bound would exclude this family only. Failure of an upper allowance would not lower-bound V. If only this reduction is obtained, report EXPLORATION and charge the existing mathematical budget.

Completed: canonical proof and qualifications are now in L104; 13030 exact checks pass. Only the reduction and scale diagnostic were obtained. The bulk estimate remains unresolved, so outcome is EXPLORATION and the next estimate is REVIEW_REQUIRED. The checkpoint and history 388 record continuation scope.
