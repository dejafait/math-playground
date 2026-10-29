# Step 553 — bounded quadratic-lift working record

Approved input: the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-25-quadratic-isotropic-lift-extremal-test.md`.
Only its formal endpoint and actual quadratic-bracket sign test are in scope.

Main gap: algebraic realization and existence of the proposed F remain open.
Intermediate target: universal homogeneous quadratic lifting at dimensions
48,800,20. Downstream use: distinguish polynomial compatibility from L165's
pointwise lifting; any actual exclusion still needs the actual point quadrics.
Test: an exact 21-square quartic outside the closed 20-square locus disproves
universal lifting; otherwise this comparison supplies no obstruction.

Calculation: dim Sym^2(C^48)=1176. FOST Corollary 1.7 gives affine
dimensions 20*1176-190=23330 and 21*1176-210=24486, difference 1156.
Both k=20,21 satisfy k<=n=47. The exact 21-square image cannot be contained
in the closed 20-square locus, since neither can its closure. Choose a tuple
in the complementary inverse image. Over C diagonalize both prescribed
nondegenerate symmetric forms and pad its 21 coordinates with 779 zeros.
A quadratic lift to a 20-dimensional space would contradict that selection,
after absorbing the minus sign by multiplication by i. No explicit tuple,
genericity of actual beta, or dominance for 800 squares is needed.

Actual sign check: for odd x, graded Jacobi gives 3[x,[x,x]]=0.
Cyclic invariance gives <[x,x],[x,x]>=<x,[x,[x,x]]>=0.
The polarized degree-four identity has all three pair-partition terms
with plus signs. L165's actual orthogonal splitting then yields
S(R[x,x],R[x,x])+Q_U(A[x,x],A[x,x])=0. Bracket versus Yoneda square
rescales BOTH components by 1/2. No full Kuranishi identity is needed.

Completed after this save: full closure/form and actual sign arguments are
canonical in `lemmas/L167-homogeneous-quadratic-serre-lift-test.md`.
The changed argument overview and ID-only DAG record that result. A new
separate critical-audit proposal is REVIEW_REQUIRED; the actual quartic,
F existence and global realization remain unknown. Existing unfinished
files and scalar/cyclicity-only stops remain intact. Documentation checks
are mechanical and do not supply the pending mathematical audit.
