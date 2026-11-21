# Fixed gamma-node construction1700: working checkpoint

Completed later in this step: canonical proof is C033e; exact arithmetic
certificate scripts/gamma-midpoint/node-rational-certificate-1700.json
passes all16 comparisons. The preliminary reasoning below is preserved;
its formerly pending inequalities are now proved in the canonical file.

Approved target: construct and certify the prescribed4096-node rational
approximation under assessment1698, COVERED_TARGET. Research/reproduction;
no new source search or change of target. Existing work is preserved.

Candidate: P(z)=sum_(k=0)^2336 z^k/k!, replace G by P(-sigma*v^2-v/2),
cosh(wv) by (P(wv)+P(-wv))/2, and exp(-2v) by P(-2v).
All arguments have modulus<=520. Imported Cauchy Taylor remainder on
r=520,rho=1040 is bounded by2*2^2080*2^-2337=2^-256,
using e<3<4. Need complete denominator/product/sum proof before acceptance.

At all prescribed nodes, C033b gives B>=1/33, v>=1/512;
D=v(1-exp(-2v))=2v^2 B>=1/(33*2^17)>2^-23.
Perturbation of D is <=16*2^-256, suggesting Dtilde>2^-24.
With C=cosh(wv)-1, |C|<=2^65, G<=1, numerator error<=2^66*eps.
Proposed quotient error<=2^90*eps+2^116*eps<=2^117*eps;
sum weights total16, giving2^-135<1/64. These inequalities need a
complete replay; no numerical evaluation of the huge polynomial is needed.

Downstream: gamma node component only; coefficient propagation, other
terms, variation-2 residual<1/2 and actual-Xi realization remain open.
Stop construction upon failed separation or sum bound; nodes/domain fixed.
