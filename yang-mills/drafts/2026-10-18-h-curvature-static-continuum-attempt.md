# H static trace — bounded ordered-column attempt

Started 2026-10-18 under the pre-existing EXPLORE assessment
`drafts/literature/2026-10-18-h-curvature-static-continuum-rate.md`.
Work only on its exact TARGET. No additional source review is needed.

The construction gap remains the ultraviolet-uniform interacting
reflected estimate <=c_box/2 and the independent continuum/infrared
requirements. The intermediate target is the complete L097 static
trace error <=C_i N^(5/2)log(eN)^2. Combining it with L233 would
control this H subtraction, without controlling other components.

Inputs inspected: L097 in full; L224 sections 2–7, including its
separate audit; L233's definition and accepted replacement scope;
ATTEMPTS/029–030/032. L008 and L028 supply the actual local curvature
insertion. The scalar estimates and modal estimates are imported
through the assessed L224/L222 coverage, not rediscovered.

Unfinished mechanism: cycle the exact trace to the compact M_T
insertion and compare columns A_(k,N)e_p=P_N zeta_(k,N)^* S_N e_p
with A_(k,x)e_p=P_infinity z_(v_k(x))^* S_infinity e_p.
First replace S_N e_p using its buffered O(N^(-3/2)) column error.
Freeze the adjoint path coefficient on this S column using its finite
second spatial squared moment; the proposed error is O(a p(k)).
For the last P comparison, the frozen intermediate column has
r^(-3) decay: its near l1 norm is O(p(k)log(eN)), its far l2 norm
O(p(k)N^(-3/2)), and each buffered P column error is O(N^(-3/2)).
These would give a total column error O(p(k)[a+N^(-3/2)log(eN)]).

Still to verify before claiming a result: both finite path adjoints
on missing boundary input/output slots, the complete finite-range
M_T pair expansion including both clovers and staggered shifts,
the trace orientation/normalization, and actual modal errors and
physical endpoint quadrature before the full heat sum. No H dipole
decomposition, projection commutation or varying-mass limit is used.
Pass only if the complete row count meets the original threshold;
otherwise record the first failed inequality without signed growth.

Completed: the complete argument is now canonical in
[L234](../lemmas/L234-h-static-trace-ordered-column-continuum-rate.md).
The ordered column comparison and actual local stencil count give
O(N^2), stronger than the approved threshold. This initial note is
preserved as a reasoning checkpoint; it is not a second proof.
The new result awaits a separate critical audit.
