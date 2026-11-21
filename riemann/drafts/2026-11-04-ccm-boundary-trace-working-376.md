# Step376 — exact trial trace specialization in progress

Approved target: specialize periodic endpoint averaging and Bernoulli jump
subtraction for L761 at lambda=sqrt(13), with an effective all-N trace tail.
The unchanged approved assessment is
`literature/2026-11-04-ccm-boundary-trace-specialization.md` (SPECIALIZE).
This is REPRODUCTION, not a new central RH mechanism.

Main gap: actual-Xi positivity and initial signs. Downstream use: clarify
the trial denominator before any ground/trial comparison. Continue if all
one-sided data, seam/cutoff jumps and explicit derivative costs can be paid;
stop this implementation if it needs an unavailable trace. No denominator
nonvanishing or ground convergence is assumed. Preserve C761a's miss and
the 96-mode failure/112-mode success.

Inputs read: L761's exact hypotheses, mode isolation, normalization and
coefficient transport; L759's basis; L760's boundary row; C761a's stated
miss; the parent source comparison and fixed-cell failure. No duplicate
all-N result occurs in the relevant CCM notes. Reused source coverage:
Lebl4.3.1, Batenkov2015 Proposition6, DLMF24.8.2–3; Osipov–Rokhlin v1
Theorem1/(27), Theorem3/Remark6 were reopened only to check the exact
integral normalization used in this specialization.

Partial reasoning (not yet a completed claim): use x=log(lambda*u),
F(x)=k(e^x/lambda), period L. On 0<x<L only r=1,...,12 contribute,
with cutoffs alpha_r=log(13/r); r=1 ends at the seam and r=13 has no
inward contribution. F(0+)=lambda^(-1/2) sum_(r=1)^12 h(r/lambda),
F(L-)=sqrt(lambda)h(lambda). Interior jumps are
-sqrt(lambda/r)h(lambda), r=2,...,12. Derivative jumps must also be kept.

Proposed effective derivative route: L761 gives chi_0,chi_4<726 and
I_0,I_4>7/10 in its signs. The ODE energy identity bounds psi' on
[-1/2,1/2], hence |psi(0)|<23. Equation(27) at zero then bounds the
finite-Fourier eigenvalue away from zero, allowing explicit differentiated
integral bounds. This is about exact modes, never endpoint transport of
an L2 error. Remaining work: complete this argument, mean/row normalization,
Bernoulli coefficient signs and the conditional tail, then record a full
canonical proof and an honest checkpoint.

Completed this same attempt in L762: exact midpoint, all jumps and mean,
finite-Fourier denominator>1/100 and trace error<34000000/N for N>=1.
The full proof and qualifications are canonical there; the preceding
paragraphs preserve the earlier unfinished state. No independent audit,
limiting denominator lower bound or ground comparison is claimed.
