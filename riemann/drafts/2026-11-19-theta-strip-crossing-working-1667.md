# Theta-strip crossing attempt1667 — saved reasoning

Approved exact target: Test whether the actual theta kernel Phi admits holomorphic continuation to |u-(R+i*pi/4)|<1/100, agreeing with the strip kernel below the boundary, for every sufficiently large real R.

Use assessment1665 (SPECIALIZE) and notes1666. The same series is Phi in C048a and P in C828a. Only C828a(5) is needed: with H(u)=exp(u/2)Theta(exp(2u)), H''-H/4=2Phi on S={|Im u|<pi/4}.

Provisional contradiction: if f extends Phi to the stated disk D, choose a in its connected lower half U=D intersect S. The constant-coefficient inhomogeneous ODE has a holomorphic solution F throughout the convex disk with initial data H(a), H'(a), using the entire sinh convolution against f. It agrees with H on U by uniqueness. Then exp(-u/2)F(u), in the coordinate tau=i exp(2u), continues theta3(0|tau) through the real point tau0=-exp(2R). The coordinate derivative 2tau0 is nonzero; its local inverse sends upper tau to the lower side of the u boundary. This contradicts the natural-boundary input.

Still to finish: write the exact convolution and verify its factors, analyticity and initial data; give a concrete inverse coordinate and upper/lower overlap check; ensure the natural-boundary theorem covers theta3 at argument zero and all finite real tau0; explicitly conclude the fixed-radius large-R quantifier. No claim yet recorded as a lemma. This would stop this crossing prerequisite, not supply a signed Xi estimate. Existing unfinished work remains untouched.

Completed later in this same step: these provisional checks are written in [C828b](../lemmas/C828b-actual-theta-boundary-disk-obstruction.md), which is now the canonical proof. The obstruction covers every real R and the fixed radius1/100. Outcome NEGATIVE/REPRODUCTION; a separate critical audit remains outstanding. The saved reasoning above is retained as the checkpoint made before the full write-up.
