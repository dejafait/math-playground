# Subendpoint relative Mellin attempt

Approved target: the exact TARGET in
`literature/2026-10-23-subendpoint-relative-mellin-coverage.md`.
This is REPRODUCTION of assessed contour/freezing methods under the
pinned external input, not a claim of originality.

Main gap: global mixed positivity; intermediate target: uniform relative
freezing on 31/32≤m/r≤63/64. A successful arithmetic comparison could
support lower logarithmic-index signs only after an independently
reviewed sector extension. Initial low indices and bounded heights remain.
Continue if the complete relative error tends to zero, including both
residues; otherwise park this implementation with its failed threshold.

Saved unfinished reasoning: set c=m/(2r), σ=1/2+c and A=m!/(2r)^m.
Scalar inversion starts at Re z=1. Shift to c>0, crossing only
z=1/2±ia, with sum 2A Re[exp(2r(1/2+ia))
(1/2+ia)^(-m-1)ζ(1+2ia)]. Exact kernel integral remains one.
Stirling at 2rc=m gives prefactor O(sqrt(r)). On a fixed window
|v|≤δ=1/8, L452 (1) gives integrated relative variation O(r^(-1/6)).
On δ<|v|≤a/2 use L452 proof (8), giving quotient at most
exp(C r^(1/3)), against exponential-in-r kernel tails. Beyond a/2,
L452 (4) gives a complete polynomial bound, uniformly even at shifted
height zero since 1-σ≥1/128. Both residues should be
exp(-2mr+O(r)) before division by the square. These estimates and
uniformity still require complete written justification; no result is
claimed by this saved checkpoint.

Prior failures checked: L304 coefficientwise loss, L330 old derivative
envelopes, L335 fixed-r/unit-phase negativity and L327 unsigned AFE/PSD
obstruction. None has the present actual-zeta coupled-height quantifiers.
Existing assessment supplies exact source comparison and no duplicate.

Completed: L454 writes the uniform O(r^(-1/6)) relative comparison,
the complete contour identity, exp(-r²) relative residue/far-tail bounds
and exp(-r/512+C r^(1/3)) middle-tail bound. The fixed central window
avoids the inadequate global-log bound on a shrinking-window tail.
Full proof and qualifications are canonical in L454; this note does not
replace them. The conditional result awaits separate critical audit.
No sector extension or Laguerre sign is claimed. Mathematical dependency
review retains L303's inversion, L330's quotient/variation mechanism
and L452's bounds; L307 and L453 are method/scope precedents, not imported
changed-band conclusions.
