# Axial signed probe contraction — working checkpoint

The saved SPECIALIZE target and assessment remain unchanged: compute the
complete remaining order-g^2 response and its cutoff logarithm. This one
bounded calculation tests L027's actual signed one-internal-action-pair
contraction on interior axial plaquettes, rather than its coefficient norm.
The main gap remains ultraviolet control of the interacting response and
the reflected error <= c_box/2.

Intermediate target: evaluate the summed axial loop for both actual L010
probes at admitted meshes, retaining the exact forest covariance and the
three contributions in common-path/curvature coordinates. Plausible use:
test whether the external residual and heat structure suppress the growing
curvature coefficient, and select a justified analytic estimate to pursue.
Continue if the separated contributions supply a discriminating test of
boundedness; abandon an inference from tensor growth if the signed response
does not exhibit that growth. Finite-mesh numerical evidence will not prove
boundedness, a sign, a logarithmic coefficient or a cancellation.

Inputs: L027's exact response formula, L025's covariance order, L018's
linear lift and actual B_i,A matrices, and L026's relative modes/forest.
L011 and L019 retain all other jets and cancellations as unresolved
obligations. L023's one-sided heat consistency has no asserted rate and
cannot alone compensate the growing forest coefficient. L024's radial
diagonal proof does not cover this nonlinear ordered action vertex.
ATTEMPTS/011–012 stop only raw-loop and tensor-only O(1) bounds. Histories
034–036 contain no evaluation of these actual W entries. Reuse the ready
assessment; no general flow-renormalization theorem is reproved.

Completed outcome EXPLORATION, REPRODUCTION. The full-mode covariance
representation was evaluated in floating-point arithmetic, followed by
64 independent signed trace samples at each of N=24,32. The canonical
estimator justification and numerical qualifications are in L027's
additional verification subsection; no new lemma was created. The
certificate is scripts/combined-ward-response/axial-signed-response-certificate.json,
with complete covariance arrays in its two local NPZ artifacts. Fourteen
checks and two stored-evidence audits pass. The complete checks, failures,
piece means and standard errors were inspected; all stored sample entries
were reread and their summaries recomputed.

The signed triplet/shear total means are (722.76,19994.46) at N=24
and (7976.96,56039.92) at N=32, with respective standard errors
(188.96,130.33) and (308.13,377.08). Common path means dominate the
three-piece decomposition at these meshes. The triplet curvature mean
changes from -1331.27 to +557.94. These observations do not certify
nonvanishing, a sign or asymptotic growth. In particular bounded e does
not make its summed contribution small, and growing h does not dictate
the sign or size of the total. No route is rigorously excluded by these
two numerical samples. This is local numerical reproduction with no
progress beyond the assessed sources claimed.

The selected continuation mechanism is an analytic estimate of the actual
exterior factors, preserving the same screened target. It would need a
quantitative smooth-mode residual rate (not supplied by L023's o(1)),
pointwise/neighbor-difference control after the straight-forest lift, and
summation of the common path, mixed and curvature terms. Second-order
consistency is a hypothesis to verify, not an established input.
The test is whether these explicit exterior estimates yield an all-mesh
bound on this selected class. If they fail, identify the offending actual
stencil or boundary term before claiming a surviving logarithm. No further
mesh sweep or fit is justified by this two-mesh diagnostic alone.

Still unresolved: boundary and transverse plaquettes, the other connected
pairing class, coordinate-Haar and other action/residual/flow jets and L019
cancellations, the full logarithm and absence of faster growth, finite
matching, the reflected error <= c_box/2, and the exact continuum target.
