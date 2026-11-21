# Neutral Gaussian smoothing: bounded domain specialization

TARGET: Specialize the unconditional Guinand-Weil formula to Gaussian-smoothed complex compact tests with both exponential moments zero, justifying the complete prime-power sum, the zero-time limit and two heat-time derivatives.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed Gaussian-flow discovery assessment's exact/full-line and heat-domain searches, theorem reads and local duplicate checks; no additional search or originality claim is needed for this narrowed standard specialization.
SOURCE_EVIDENCE: https://arxiv.org/html/2403.17803v1#S2.SS2 — Carneiro-Milinovich Lemma 4, proof attributed to Iwaniec-Kowalski Theorem 5.12; https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf#page=135 — Hunter revision 2014-06-18, Proposition 5.3 and Theorem 5.4, printed pp.129-130; direct statements rechecked in step 326.
COMPARISON: The known results supply an unconditional analytic-strip formula and Schwartz heat evolution, but do not check this complex convolution square, both exponential moments, normalization, weighted tails or differentiation of the complete pairing.
GAP: Verify exactly those applicability and domination steps on each bounded time interval, including right derivatives at zero; no starting sign, monotonicity or unrestricted positivity claim is covered.
REASON: A full-line identity with controlled differentiated tails is needed before a new Gaussian sign mechanism can be formulated or tested; import the known formula and heat theorem rather than reprove them.
SCOPE: Fixed complex f in C_c^infinity(R) with both integrals exp(+/-x/2)f(x)dx zero; G_tau(x)=(4pi tau)^(-1/2)exp(-x^2/(4tau)), f_tau=G_tau*f for tau>0 and f_0=f; each fixed finite interval [0,T]. No uniformity over supports, unbounded times or arbitrary Schwartz initial data.

## Exact later task and discriminator

The main gap is unconditional complete neutral Weil positivity. This
task supplies the domain-and-differentiation bridge before any new
Gaussian sign estimate. Independent starting sign and backward
propagation remain separate unproved steps; no creative target is ready.

Use L018's completion and L744(6) only for the compact-time-zero
normalization comparison. Define the full-line energy through the
imported unconditional formula rather than extending the finite-window
operator by assertion. Apply Hunter's linear theorem to real and
imaginary parts separately. Prove exponential-weight integrability and
preservation of both moments; ordinary Schwartz convergence alone is
insufficient for weighted moments.

Retain complex tests. The convolution-square Fourier transform must
have a holomorphic extension using reflected conjugation, not a
nonholomorphic absolute square at complex zeros. Retain multiplicities,
complex ordinates, both poles until exact vanishing is justified, the
gamma/scalar term and all prime powers. Convert the source's Fourier
convention exp(-2pi i x xi) to L744's exp(-i xi x) explicitly.

The proposed conclusion is an exact identity with two continuous
heat-time derivatives on each [0,T], understood as right derivatives
at zero. Seek complete integrable/summable majorants for all relevant
zero-side and arithmetic-side derivatives, uniform on that interval.
Check the source strip analyticity and decay for each differentiated
test. Standard Gaussian integrals, Fourier convolution and derivative
theorems and dominated convergence are permitted named inputs. A finite
arithmetic cutoff at positive time or a numerical tail preview fails
the test. No mathematical program is needed.

Continue if exact neutrality and the differentiated identity have no
unpaid remainder. If an endpoint, moment claim or interchange fails,
preserve that obstruction and narrow the conclusion. No favourable sign,
starting sign or RH consequence may be inferred from the identity.

## Sources, duplication and classification

The completed discovery assessment gives direct links, full hypotheses,
proof cases actually read and unread references. Lemma 4 is imported by
citation; its book proof is not independently reproduced. Hunter covers
unweighted heat evolution, while the weighted applicability difference
is the later work. Connes--Consani Proposition C.1 is an RH-equivalence
warning, not a positivity input. L058-L060/L616-L617 deform Xi itself;
L740 is causal; L744 is compact; earlier Gaussian-regulator assessments
concern different families. No cross-notebook input is proposed.

This is REPRODUCTION, not a claim beyond checked known mathematics.
Full matching Mathlib coverage is unchecked. Written in step 325; direct-source
coverage reviewed separately in step 326. The unchanged target is ready for
a later mathematical invocation; its conclusions have not been proved here.


## Separate source-link recovery review — step 326

LITERATURE_REASON: Supervisor recovery identified missing direct URLs in this
ready assessment; repair source accessibility and verify the cited statements
for the unchanged target, without another discovery search.

Opened both primary URLs above on 2026-11-04. Rechecked the complete Lemma 4
statement and proof attribution, and Hunter's Schwartz hypotheses, endpoint
convention, Proposition 5.3 and Theorem 5.4 with its proof. Lemma 4 needs
strip analyticity and decay of order greater than one; it retains complex
zero ordinates, pole evaluations, gamma/scalar terms and every prime power.
It does not assume RH; neighboring Lemma 5 does and is excluded. Hunter
gives smooth Schwartz heat evolution up to zero, not exponential-weight
control. The complex-data extension, weighted moments and differentiated
full pairing remain exactly the applicability work specified above.

Reuse the discovery assessment's searches, duplicate comparison and stops;
no changed hypothesis or new mechanism warrants repeating them. Neither
source is blocked. SPECIALIZE is retained. This is a process repair, not
new source-scope evidence, a mathematical advance or a sign result. No
lemma, mathematical script, DAG or argument-overview change is needed.
