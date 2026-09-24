# Triple-product diagonal checkpoint — 2026-09-13

Earlier work through L161 is complete and preserved. For finite nonnegative
amplitudes write S=Σ A_n², D2=Σ_k(Σ_ab=k A_a A_b)² and
D3=Σ_k(Σ_abc=k A_a A_b A_c)². Inclusion–exclusion for the three
coordinate equalities in arm=bsn gives W=D3−3 S D2+2 S³.
Each single equality has mass S D2; every double intersection and the
triple intersection have mass S³. Thus 0≤W≤D3.

Planned elementary Gaussian-window bound: A_n≤C N^(−1/2), all products
are ≤(bN)³, hence D3≤C N^(−3)Σ_(k≤(bN)³)d3(k)².
Prove d3(k)²≤d9(k) by mapping 3-by-3 nonnegative exponent matrices
onto their row/column margins. Then Σ_(k≤X)d9(k)≤X(1+log X)^8.
This gives O((1+log T)^8), not a uniform fixed-cutoff bound.

Resume: check the margin-surjection argument, write the finite identity
and analytic bound, and run an exact integer multiplicity regression.

Completed as L162. The finite identity and logarithmic eighth-power upper
bound are proved; the regression passed 21 weighted cases. No sharp
exponent or uniform cutoff-correlation bound is claimed.
