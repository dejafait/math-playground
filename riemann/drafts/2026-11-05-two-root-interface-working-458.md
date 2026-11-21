# Two-root interface — step458 working checkpoint

Approved target: the exact TARGET of
`literature/2026-11-05-two-root-reciprocal-coefficient-interface.md`.
Main gap: actual-Xi all-degree mixed positivity. This calculation seeks
only a root-independent coefficient form, with no sign inference.

Provisional algebra, pending complete proof/check: write a=alpha_1,
b=alpha_2, s=a+b, t=ab and P=z^2-sz+t. If B_5 is the degree-five
Taylor polynomial of P^2/g, complete-tail cancellation should identify
M=E^-1(J+EKE)E^-1 with the divided-difference matrix of -B_5/z^5
at a,b (diagonal derivatives). Expansion suggests

    H=[[u_2,u_3],[u_3,u_4]], W=[[1,-b],[1,-a]],
    M=W H W^T, det(W)=b-a !=0.

To finish: justify the canceled analytic tail without evaluating the
uncanceled inverse series at a root; verify all six coefficient
contributions and the explicit congruence, including singular H and
nullity. Close this one attempt afterward; no higher-order extension,
model sweep or automatic sign test is authorized. Existing L781/L783
and automatic-sign stops remain unchanged. No cross-notebook input.

Completed: full proof is canonical in L785. The proposed block and map
hold under the exact hypotheses, including singular H; all four exact
formal checks passed with zero residuals. This working checkpoint is
retained as unfinished-reasoning history, not an additional proof source.
The one attempt is closed, pending a separately approved critical audit.
