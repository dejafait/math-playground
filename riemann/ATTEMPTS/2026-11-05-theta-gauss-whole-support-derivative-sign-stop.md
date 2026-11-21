# Whole-support theta Gaussian derivative-sign cutoff — step545

The complete symbolic specialization, citations and qualifications are
canonical in [L806](../lemmas/L806-theta-gauss-derivative-sign-classification.md).
It uses the actual theta law and no numerical sweep. This is local
progress by reproduction of standard inputs, not a new general theorem.

WHY IT FAILS: For x>0 the 2n-th v derivative vanishes when d<2n,
is a positive constant when d=2n, and has d-2n simple positive
zeros with sign changes when d>2n. Full theta support makes both
signs occur on sets of positive measure in the last case. The sole
nonzero whole-support sign gives a positive Gaussian error at every
x>0, hence no alternating comparison directions from this premise
alone. Exactness below the cutoff does not establish the reference's
hyperbolicity. This parks only the derivative-sign-only mechanism;
it does not sign the actual error above the cutoff, disprove actual
hyperbolicity, or rule out a quantitative one-sided barrier argument.

A different, independently testable question is the actual integrated
error at degree 2n+1, using the two moments beyond the exactness range
rather than a whole-support derivative sign. Its sign transitions
have not been derived or approved here. The proposed source review
must check known moment-defect identities and overlap before any
calculation, and must not claim reference hyperbolicity or root
margins from a signed error alone. Preserve the L795/L796/L805 stops
and L793's missing actual-transfer inputs.
