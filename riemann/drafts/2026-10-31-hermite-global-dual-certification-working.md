# Approved finite dual screen: certification work

Target is unchanged: certify complete evaluation pairings at (N,x)=(64,163/4),(128,271/4),(256,447/4), using L564 and L567. Existing exact constraints are retained. No uniform-family or Xi transfer claim.

Plan: exact rational outward interval arithmetic; composite closed Newton–Cotes with 257 equally spaced nodes on each length-1/32 panel of [0,4]. Cauchy derivative bounds on radius-1/2 circles give a fully explicit interpolation remainder; theta indices k>=25 and u>=4 receive separate positive bounds. Integrate all moments through 512 and evaluate the entire finite Hermite sums with rational arithmetic. Save the complete certificate. No result is yet certified. If interval signs fail, retain the enclosures and refine or park rather than infer feasibility.

For complex z within distance 1/2 of [0,4], |Im z|<=1/2 and -1/2<=Re z<=9/2. The positive-u theta formula is analytic there: cos(2 Im z)>=cos(1)>1/2 and pi exp(2 Re z)/2>1/2. Normal convergence follows from k^4 exp(-k^2/2). A deliberately loose uniform bound |exp(-z^2/4)Phi_R(z)|<=2^60 suffices. Thus each full-line moment remainder is <=8*2^60*(9/2)^(2n)*16^(-257). Complete details and tail bounds must be checked and placed canonically before any sign claim.
