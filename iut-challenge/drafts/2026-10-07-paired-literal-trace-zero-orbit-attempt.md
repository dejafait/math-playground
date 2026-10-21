# Paired literal trace-zero orbit — working calculation

Completed: the expected branch scales and radii are proved in canonical L027. All 15 finite checks passed in `scripts/coarse-ideal/paired-literal-trace-zero-orbit.json`; ATTEMPTS/021 records the stopped transfer. The saved reasoning below is retained as the pre-verification checkpoint, not a second proof or an active continuation.

Approved target: Determine the exact paired-reference orbit radius of ((pi O) union (3pi J)) intersect ker(Tr) in the unchanged degree-27 two-factor packet.

Coverage: `drafts/literature/2026-10-07-paired-literal-trace-zero-orbit.md`, SPECIALIZE saved before this invocation. Main gap remains original finite B>=A; this tests transfer from the larger envelope to the literal input only. Continue that transfer only for an attained radius above 81; otherwise stop it. Actual-ind3/native identification, original data, behavior outside V, higher powers, pilot transport and essentiality remain independent gaps.

Inputs read: complete L016 table/image/separator, L020 tensor normalization, L025 exact finite-word Gamma and embedded homothety proof, audited L026 span/minimum/attainment. ATTEMPTS/017 and /020 retain the fixed-map and prescribed-coordinate stops. No new source search is needed.

Working reasoning saved before verification: put D=O intersect V, N=(pi J/6) intersect V. The ideal branch (pi O) intersect V is D: its constant coordinate would be in 3Z_3 and is forced to zero; coordinates 1,...,26 remain integral. Since 3D subset H intersect V subset M, its finite-sum orbit span is bounded in 3^(-1)M and is full. L025 gives embedded homothety. The literal point pi in D has phi(pi)=-31/3, so D is not contained in M and the scale should be exactly 3^(-1)M. L026 supplies min v(M)=-4/3 and the finite-sum attainment argument.

The logarithm branch is exactly 18N, because rational scaling preserves V. Its span is 18*(3^(-4)M)=3^(-2)M, as 2 is a Z_3-unit. Its actual finite-word radius is obtained by multiplying L026's actual orbit point by 18, not by replacing input with its span. Expected minima: ideal -7/3, logarithm -10/3, union -10/3, all above required -4. Check the branch identity, phi, ideal exponents, full table minimum and sharp trace-zero point before finalizing. No result outside V is inferred.
