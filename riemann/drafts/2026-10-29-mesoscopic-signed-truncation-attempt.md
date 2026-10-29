# Mesoscopic signed truncation calculation, 29 October 2026

Approved target: the exact TARGET in
`literature/2026-10-29-mesoscopic-signed-truncation-coverage.md`.
Classification: RESEARCH / REPRODUCTION; actual task: calculation.

Main gap: initial actual-Xi signs at unbounded heights and global mixed
positivity. Intermediate target: approximate L471's negative mass by
the signed all-zero kernel retained in |t-Re z|<=h, h=(log T)^(-1/4),
with absolute error O(T(log T)^(5/2)). Downstream use: a controlled local
expression for a later cancellation test, which remains unsupplied.
Continue if this error and the zero-safe extension hold uniformly;
park this regime if only the full T(log T)^3 scale or a failed extension
is obtained. Reused source gate, L471, L467 and L464 Section 3; no new
source theorem or novelty claim. Existing displacement, Selberg and
global-envelope stops remain unchanged.

Saved reasoning before write-up: for 0<h<=1, the discarded zeros with
h<|t-gamma|<1 lie in two closed unit intervals. L467 bounds their
multiplicity by 36 log(t+3), giving 36 h^(-2) log(t+3). For positive
ordinates at distance >=1, shells k<=|t-gamma|<k+1 have multiplicity
at most 36 log(t+k+3); sum their k^(-2) weights. Reflect negative
ordinates and sum shells in t+gamma; any zeros on Re z=0 form a finite
compact set and contribute O(t^(-2)). Hence the absolute discarded
kernel is O(h^(-2)log(t+2)). Multiplication by Z^2, the 1-Lipschitz
negative-part map and L471 (8) at j=0 give the desired error.

At a real zero r of order nu, its term is retained near r. Write
Xi(t)=(t-r)^nu g(t): the weighted singular term extends as
nu (t-r)^(2nu-2)g(t)^2/A(t)^2. All other retained terms are bounded
locally before multiplying by Xi^2, even if a cutoff switch occurs at r.
The extension equals Xi'(r)^2/A(r)^2, so its negative part is zero.
Only finitely many zeros enter the retained window over [T,2T]; cutoff
switches are finite and measurable, with endpoint values irrelevant to
the integral. The discarded kernel is uniformly bounded near r, too.

Completed: the full proof is canonical in
[L476](../lemmas/L476-mesoscopic-signed-kernel-truncation.md). The proposed
threshold passes, with no numerical onset or separate critical audit.
No assertion about the size of the retained negative mass,
individual-height signs or higher signs follows. Outcome ADVANCE means
a relevant local approximation input, classified REPRODUCTION; no
advance beyond the checked known mechanism is claimed. The next
continuation is a separately gated critical audit of this application.
