# Two-offset paid-arc attempt — working checkpoint

Invocation target and source gate: the unchanged EXPLORE assessment
`drafts/literature/2026-11-02-localized-logarithmic-joint-moment.md`.
Main gap: uniform H versus the exact squared-residue D. Test only the
proposed two-offset family, not arbitrary support or Xi signs.

Take n=12q+3, h=27/(5n), delta in [1/8,3/8], unit residues at the
anchor x and x+i*y for y=+/-h(l+delta), +/-h(l+1-delta), 0<=l<q.
There are M=4q+1=n/3 distinct poles. Set Y_n=q*h<9/20; use Y_n,
not 9/20, for the vertical contour edges: the latter can enclose an
extra shifted-grid pole when delta<1/4. This correction is essential.

Possible mechanism, not yet a completed proof: the anchor is additional
to two shifted grids. For omega=10*pi*n/27 use the sum of kernels
i*omega/(exp(i*omega*y-2*pi*i*delta)-1) and the same with +delta.
Their residues are exactly the 4q nonanchor nodes inside |Re y|<Y_n.
The exact full-polynomial contour has the separate anchor contribution
R^(-1) T_M(x*zeta/R), retaining all M moments.

Use lower height -b=-1/50 and upper height c=1/200. For u=-1,
a=-e+i*s, the product factors relative to s=0 are
(1+i*b_j*s)/(1-i*A_j*s), A_j=1/(e-t_j), b_j=t_j/(U-e*t_j).
On e in [123/100,5/4], b_j<=A_j/2 and g(e)=integral(A+b)<=9/4
is the intended exact scalar check. Thus W(-i*b)<=exp(9*n/200).
All lower-edge kernel frequencies m>=2 then have the intended
negative rate (20*pi/27-9/4)/50>1/1000.

The m=1 term must not be bounded on the lower edge. Shift that entire
term, with the complete T_M, to the upper edge. There g(e)>=g(R)>9/5
is the intended scalar check, so W(i*c)*exp(omega*c) decays at rate
(9/5-10*pi/27)/200>1/1000. The contour is contained in |a|<=4/3<R,
which would give |T_M(a*zeta/R)|<=33 uniformly in M.

Side bounds still to verify exactly: for n>=27, Y_n>=2/5. On e<=d,
the product attenuation is at least half the sum of
(3/8)*(64/625)/(1+64/625) and
(3/8)*(64/225)/(1+64/225), up to an absolute parity correction.
Subtract the growth 9/200; the result should exceed 1/100.
On e>=d, b_j/A_j<=8/11 and A_j>=8/11 give attenuation
7296/397001>1/100. Shifting the first frequency charges at most
(10*pi/27)/200, still leaving rate >1/1000.

Kernel side denominators are uniformly separated because
omega*Y_n=2*pi*q and delta stays in [1/8,3/8]. Horizontal kernel
bounds and the sum of every m>=2 must be written with explicit
uniform constants. If these checks pass, the expected full polynomial
error is C*n*exp(-n/1000), hence c_0(-1)>=1/(2R) eventually,
uniformly in delta. Apply L658 and L661 with sum r_a^2=M=n/3 to
get paid excess at least (261/10000)*n-3log n-C.

No conclusion is accepted at this checkpoint. A finite screen or a
vanishing first harmonic would not decide the target. Preserve the
single-lattice endpoint/full-circle stops. General support, matching
upper bounds, Xi realization and signs remain independent gaps.

## Completed attempt

The full proof is now canonical in L664. The exact scalar upper bound
was sharpened to g(123/100)<11/5. Using only 3<pi<22/7, the tail
rate obtained is >1/2250; the final uniform error is
1000*n*exp(-n/3000), not the initially proposed exp(-n/1000) rate.
This retains a positive fixed anchor limit and the proposed paid
excess 261n/10000-3log n-C. The full finite contour, moving endpoints,
all moments, shifted first frequency, complete higher-frequency tail,
and squared diagonal are written in the canonical proof. Its exact
rational certificate passes. A separate conceptual audit is pending;
the preliminary calculations above are preserved as unfinished-work
history, not additional premises or a second canonical proof.
