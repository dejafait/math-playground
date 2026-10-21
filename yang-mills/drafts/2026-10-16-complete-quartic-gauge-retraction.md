# Complete quartic probe: bounded joint-retraction attempt

The approved target is the unchanged complete L011 quartic response for
both actual L010 probes. The main gap remains the interacting reflected
comparison and continuum/infrared construction. Seek a finite signed
reduction useful for a later cubic estimate; a reduction alone supplies
neither bounded scaled values nor convergence.

Work in progress, saved before exact checks: put z in the co-closed
Gaussian, phi=Phi z, y=Rz. Gauge-transform exp(h y_e) by
exp(-h phi_tail) on the left and exp(h phi_head) on the right. Its
logarithm is h z+h^2 b+h^3 c+O(h^4), with b as in L183 and c given
by the complete three-exponential BCH polynomial. Gauge invariance of
the complete flowed numerator should give

    F_(i,4)(Rz)=F_(i,4)(z)+dF_(i,3)(z)[b]
                         +<b,B_i b>+2<B_i z,c>.

No individual L011(12) term is transferred. Retain all pinned endpoints
and all flow integrals in the complete F jets. The residual is the
unchanged r_0=<z,Az>, including both insertion subtractions.

Normalization warning to verify: with t=2SAz, a single-polynomial
quadratic-tilt derivative is (1/2)E[dP[t]], unlike the single-side
cross-cubic contraction used in L181. Differentiate Phi z as well as z.
Continue if the full BCH/retraction and Gaussian contraction agree in
independent exact checks. Abandon any reduction that deletes c, the
quadratic b term, an observable jet, or a boundary/zero-time contribution.
No cubic estimate is yet established. Preserve ATTEMPTS/010 and 039–045.

Completed: the saved reduction is proved with every cubic BCH endpoint
term in [L212](../lemmas/L212-complete-quartic-probe-gauge-retraction.md).
That canonical file also gives the full signed response derivative and
single tensor contraction. Eight rational gauge/loop fixtures and two
direct correlated/singular Gaussian moment checks pass in
`scripts/combined-ward-response/complete-quartic-retraction-certificate.json`;
the complete records were inspected. The single-polynomial tilt has
the factor 1/2, with no correction to L181's different cross-cubic rule.
This establishes a finite input only; no bound or convergence is proved.
Continue on the unchanged covered target by estimating the entire L212
signed contraction before separating its correlated gauge jets. Its
co-closed flow terms still require endpoint control. No new assessment
or outside target was derived or approved in this mathematical step.
