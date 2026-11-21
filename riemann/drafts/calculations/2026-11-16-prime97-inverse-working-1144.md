# Inverse compression attempt1144 — working checkpoint

Approved exact target: Construct and evaluate one certified compressed whole-line inverse bound for the fixed n=97 one-eighth allocation on the full complex J-domain, retaining explicit frequency and kernel-approximation errors.

Main gap L030-L032/C032a remains actual-Xi all-degree positivity. Test the two-collar sufficient norm threshold 1/(4k), k=2log97/sqrt97, with unchanged a,b,r,w of C750h. Both collars and their off-diagonal block must remain. Whole-line relaxation is sufficient, not equality with a supported inverse. A lower bound above this threshold parks this certificate only. A successful upper bound could pay one activation term; full budgets and realization remain independent.

Fixed before evaluation: frequency cutoff T=256, frequency mesh h=1/64. Kernel approximation is midpoint quadrature on this entire frequency interval; retain an explicit uniform kernel error using total variation of the multiplier and the full spatial separation |x-y|<=2a. Its finite kernel can be bounded by Schur, retaining both collars. For discriminating lower information, evaluate the normalized single-collar indicator's inverse quadratic form on the same frequency grid; use a fourth-derivative Simpson bound on [0,T], and a nonnegative omitted tail (never subtract it). No parameter search or pulse retuning. This is an inverse-space test vector, not an original-domain violating witness.

Planned proof: closed Fourier multiplication form log(2+|t|), its closed supported subspace, restriction bounded by the inverse compression via form Cauchy-Schwarz; correlation bounded by half total collar mass. Lower inverse Rayleigh quotient is valid for arbitrary L2 collar vectors, which need not be in the original form domain. Source inputs are those already inspected in assessment1142/review1143, plus Plancherel and elementary differentiation. Mathlib matching coverage unchecked. No cross-notebook input.

Status: formulation to be justified and certificate to be evaluated. Existing unfinished files preserved.

Completed: C750i contains the full specialization and norm certificate.
The fixed inverse norm lower bound exceeds the required threshold by
>0.02344876; the full upper certificate is1.01442. The initial extra
upper<1 expectation failed and is preserved, not used. No parameter
refinement is justified because exact norm information already rules
out this sufficient criterion. Original supported allocation remains
open. Canonical proof and complete certificates supersede this working
note; this note preserves the before-evaluation choices.
