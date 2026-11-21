# Canonical-system support extension: completed source comparison

TARGET: Compare Suzuki's canonical-system Hamiltonian theorem with a neutral-Weil support extension from length 8log3 to 9log3, identifying any independent signed boundary estimate and every RH or Fredholm-invertibility assumption.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step318 located the exact reference [8] in Suzuki 1907.07302v2 and searched Suzuki/Hamiltonian/canonical-system/Weil/support/boundary terms; compared the named local parameter, square-order, realization, Schur and IMS stops. No inspected theorem supplies the nominated independent signed boundary estimate; this is bounded source evidence, not a mathematical impossibility or novelty claim.
SOURCE_EVIDENCE: Suzuki, Hamiltonians arising from L-functions in the Selberg class, arXiv:1606.05726v3 (1 October 2020), Sections 2.1-2.6/3, Theorems 2.1-2.4, Proposition 4.2 and its full proof pp.14-15, Section 5.1 standing assumptions and Proposition 5.1 proof pp.17-18; Suzuki 1907.07302v2 (6 March 2020), Theorem 1.1 and full Section 2 proof pp.3-4, Theorem 1.2 and reference [8]. Primary URLs and exact scope below.
COMPARISON: The ratio-kernel Hamiltonian is constructed only on a determinant-nonvanishing interval; the unconditional proof gives a small interval, and the global norm proof uses an inner symbol. L740 instead realizes the limiting exponential logarithmic-derivative kernel, and L744(6) is its parameter-zero complete energy. No source theorem identifies Hamiltonian positivity with the required neutral-energy boundary sign or transfers it across these operators.
GAP: No independent signed boundary estimate for length 8log3 to 9log3 was located. Seed signs, quantitative invertibility on that interval, a justified parameter-limit/energy bridge and iteration uniformity remain unproved; the squared determinant ratio supplies none of them.
REASON: New primary theorem/proof-case comparison changes the route: park direct Hamiltonian support propagation rather than deriving a boundary sign from an already invertible interval or the conditional global isometry. EXPLORE records the completed bounded comparison; it authorizes no new mathematical target.
SCOPE: Literature-only comparison for TARGET. No imported sign theorem, new lemma, mathematical script, source-proof audit, changed DAG/PROOF argument, RH candidate or automatic support-extension approval.

## Purpose and exact boundary of the proposed review

The completed step317 task was solely L750's conceptual audit, with
canonical proof and certificate checks there. This nomination neither
changes that result nor establishes a Hamiltonian, operator identity,
boundary estimate or extension theorem. Main gap: unconditional signs
of the complete Weil energy on unrestricted support, hence actual-Xi
positivity. A local support-extension estimate could be an intermediate
input even while its positivity seed and iteration uniformity remain
unproved. The lengths 8log3 and 9log3 nominate one test, not a theorem
that either interval already has positivity.

First locate the exact primary paper referenced by the existing Suzuki
source comparison. Read its theorem hypotheses and the proof case
that constructs or extends the Hamiltonian before larger passages.
Record its version, theorem/page numbers and direct primary URL. Reuse
unchanged source assessments for the previous operators; do not repeat
their construction or search for quota balance. If the cited paper
does not treat such extension, record that mismatch rather than invent
a theorem under a familiar title.

Essential local inputs, to read only as needed, are L740's actual
finite-window causal realization, L741's complete-energy normalization,
and L744 (6)'s arbitrary-fixed-window smooth formula. L618 can be used
only if the source requires its exact reflected operator conventions;
do not infer a semigroup law from scalar symbols. L750 is contrast:
its stopped corrected partition rule is not a premise for an unrelated
Hamiltonian theorem. No conditional spectral consequence of L742 is
an unconditional input. Existing theorem names and hypotheses must be
matched before proposing any mathematical specialization.

Compare narrowly with the retained records
[parameter descent](../../ATTEMPTS/2026-11-04-suzuki-parameter-descent-source-limit.md),
[square order](../../ATTEMPTS/2026-11-04-suzuki-small-window-square-order-stop.md),
[realization without signs](../../ATTEMPTS/2026-11-04-suzuki-realization-only-sign-gap.md),
[the generic Schur comparison](2026-11-04-joint-energy-mechanism-nomination.md),
and [the audited fixed IMS stop](../../ATTEMPTS/2026-11-04-fixed-corrected-ims-propagation-stop.md).
These are scope restrictions, not global prohibitions on canonical
systems. A positive Hamiltonian constructed only after assuming the
missing Fredholm/contractivity sign would not pay the present gap.

Continue toward a mathematical attempt only if the primary comparison
identifies an explicit independently testable signed boundary quantity
for the proposed finite extension, with complete prime and pole
normalization and no target-equivalent global assumption. A generic
existence theorem, a restatement of the positivity criterion, or an
unpaid off-diagonal block is a decisive scope failure: park this lead
without another approval or formal-factorization turn. An essential
inaccessible source is SOURCE_BLOCKED, not a mathematical conclusion.

No justified creative proof target has yet been obtained. If the review
does expose a new independent boundary mechanism, a separately gated
proof_attempt/creative may be appropriate: its obstruction is the
signed cost of increasing support in the complete actual form, and
its bounded test must be the explicit 8log3-to-9log3 quantity with a
stated threshold. Otherwise do not manufacture a creative attempt.
Full matching Mathlib coverage is not checked. The next task is
literature_comparison, standard/high; no new coverage is approved here.

## Completed comparison — 4 November 2026, step318

The nomination above is preserved as the question and its original
stopping test. Its present-tense references to unread coverage describe
the starting state, not a remaining source-access blocker. The source
was accessible. The outcome is NEGATIVE: a new hypothesis/operator
mismatch parks this direct implementation. It is not a theorem ruling
out canonical systems or neutral support propagation.

### Exact source and primary cases read

The Hamiltonian lead in reference [8] of
[Suzuki, Integral operators arising from the Riemann zeta function,
arXiv:1907.07302v2](https://arxiv.org/pdf/1907.07302v2), p.10,
is **Hamiltonians arising from L-functions in the Selberg class**.
Use [arXiv:1606.05726v3](https://arxiv.org/pdf/1606.05726v3),
1 October 2020, 23 printed pages; the article appeared in J. Funct.
Anal. 281 (2021), no.8, 109116. Its version matters: the old 2020
paper's reference to Proposition 4.4 is not the numbering of v3's
Proposition 5.1. No result was inferred from that numbering alone.
The earlier arXiv:1204.1827v2 was located and opened as a bibliographic
lead, but its theorems/proofs were not used; the exact cited v3 suffices.
PDF screenshot calls returned no usable images; the quoted formulas
and proofs were read through primary PDF text extraction, with HTML
used to check the Hermite--Biehler notation. No local certificate was run.

In the following, use F for the source's L-function to avoid confusing
it with our support length L. Section 2.1, pp.5-6, defines S_R as
nonconstant Selberg-class functions real on the real axis, with real
completed function there. The zeta specialization belongs to this class,
has degree d_zeta=1 and root number +1. The source completion omits
our constant factor 1/2; that constant cancels from every ratio here.
This checks a normalization, not a new analytic input.

Theorem 2.1, p.7, assumes F in S_R, omega>0, positive integer nu,
and nu*omega*d_F>1. Its kernel has Fourier symbol

    Theta_(omega,nu)(z)
      = epsilon_F^nu [xi_F(1/2-omega-iz)/xi_F(1/2+omega-iz)]^nu.

It proves self-adjoint Hilbert--Schmidt finite sections K[t], vanishing
for t<=0, and existence of tau>0 such that both 1+K[t] and 1-K[t]
are invertible for 0<=t<tau. Formula (2.10), p.7, then defines

    H(t)=diag(1/gamma(t), gamma(t)),
    gamma(t)=[det(1+K[t])/det(1-K[t])]^2.

Theorem 2.2, p.8, constructs the entire solution on that same interval,
with the initial entire function recovered by (2.13). Section 3, p.9,
spells out the general construction assumptions K1-K5: an entire
Fourier transform of a real C1 rapidly decaying function, a real
continuous exponential-growth ratio kernel, causality, piecewise C1
regularity with locally integrable derivative, and exclusion of both
eigenvalues +1 and -1 throughout [0,tau). K5 is an input to this
construction. Positive diagonal entries of H are not a proof of K5
at the next endpoint. We do not import a trace-class assertion from
Hilbert--Schmidt alone; only the source's stated Fredholm construction
is being compared, and no local determinant is defined or evaluated.

Read Proposition 4.2 and its complete proof, pp.14-15. It assumes only
the same F,omega,nu conditions, not RH. A putative eigenvector is
supported in [-t,t]. Its untruncated output g is estimated on a shifted
Fourier line v>1/2+omega using

    M_v = sup_u |Theta_(omega,nu)(u+iv)|,
    ||g exp(-v x)||_2 <= M_v exp(v t) ||f||_2.

The eigenvector equation gives the reverse comparison on [-t,t];
the contradiction uses M_v^2 exp(4vt)<1. Formula (4.3) makes M_v
small for sufficiently large v; t must then be sufficiently small
relative to the fixed v. This is a sufficient small-window test.
No constants establishing it at t=4log3 or (9/2)log3 are given or
verified here. Failure to verify that sufficient test at those values
is not evidence that invertibility or the energy sign fails there.

Section 5.1, p.16, explicitly assumes the strict Hermite--Biehler
condition with no real zeros; this makes Theta inner in the upper
half-plane and the full reflected Fourier operator an L2 isometry.
This is unconditional for omega>1/2 (Proposition 2.2, p.6), and follows
from GRH(F) for smaller positive omega. Read Proposition 5.1's whole
proof, pp.17-18: the isometry first bounds the compression by one;
equality would force its output to have compact support; Lemma 5.2
excludes a nonzero compact output; compact self-adjointness then yields
norm strictly below one. The lemma's noncompact-support conclusion
is stated without innerness, but the preceding norm comparison is
not. Omitting that standing assumption would invalidate the import.
We checked Lemma 5.2's statement and how the proof is used, not the
subtle zero-count argument of its Lemma 5.1 input. No independent
source-proof certification of either lemma is claimed or needed for
this negative applicability comparison.

Theorem 2.3, pp.8-9, retains the Hermite--Biehler premise for
0<omega<=1/2 and gives the global kernel limit. Theorem 2.4, p.9,
requires a sequence omega_n decreasing to zero, nu_n*omega_n*d_F>1,
nonvanishing of both determinants at every t>=0, AND the vanishing
terminal reproducing-kernel condition for z in the upper half-plane.
Together these are an equivalence with GRH(F). Nonvanishing alone or
positive diagonal Hamiltonians alone must not be called RH here.
The equivalence is compared as stated, not independently reproved.

In the 2020 integral-operator paper, Theorem 1.1, printed p.2, already
assumes determinant nonvanishing. Its boundary values satisfy
m(t)=1/Phi(t,t)=Psi(t,t). The full Section 2 proof, pp.3-4, was read:
nonvanishing of Phi(t,t) is obtained using invertibility of 1-K[t]
in the homogeneous differentiated equation; the logarithmic ODE for
Phi(t,t) subsequently expresses the existing solution through boundary
resolvents. Neither step provides an independent bound on the
resolvent before invertibility is known. Theorem 1.2, p.3, constructs
the exponential kernel for theta>1 and asserts some local tau; it is
not an unconditional all-window theorem.

### Comparison with the actual neutral energy

Local inputs read: L740 (1)-(8), L741 (1)-(6) and its external-source
qualification, and L744 through (7). Their domain/sign conclusions
are used only in the scopes already written. L618 was not needed:
L740 already states the required exact conventions. L742 is not an
input. L750's result is used only as a contrast via its retained stop.

The source finite-section geometry sees its causal kernel on [0,2t);
L740 identifies our translated interval length as L=2t. Thus the
nominated endpoints correspond geometrically to t=4log3 and
(9/2)log3. This does not identify the kernels: the Hamiltonian paper
uses a shifted xi ratio raised to integer nu, while L740 uses
exp(-2theta xi'/xi), and L744(6) is the Hermitian energy of its
parameter-zero generator. The scalar limiting motivation is explicit
in the 2020 paper, p.2; no norm, resolvent, Hamiltonian, derivative or
signed-energy limit follows just from that motivation. We derive
none of those missing bridges in this literature turn.

For exact-neutral smooth f on (0,L), the object needing a lower bound
is precisely the already written L744(6): the full digamma multiplier
minus every prime-power delay, with BOTH exponential moments zero.
The pole vanishes by those exact constraints, not by deleting a
completion term from a nonneutral form. Source formulas retain their
own gamma/completion/arithmetic ratio; they do not isolate our
complete signed boundary contribution. No inspected theorem supplies
its sign at the proposed extension, or assumes neutrality in place
of innerness. Positivity of H, a nonzero boundary resolvent, and a
nonnegative neutral Weil energy are different assertions here.
No transfer between them has been established.

The recorded parameter-descent, small-window square-order,
realization-only, generic-Schur and exact corrected-IMS stops were
read in their nominated paths. None is a global ban. The new evidence
is specifically the Hamiltonian's K5/innerness dependence and the
ratio-versus-generator mismatch. The hypothesis comparison suffices
to park this direct citation route; it is not a counterexample to
any mathematical support-extension theorem.

### Decision and future scope

No independent signed boundary estimate with a paid threshold emerged.
The original continuation test therefore fails. Park this Hamiltonian
lead without another determinant-positivity, formal-limit or resolvent
rephrasing turn. Reopening requires a quantitative independent signed
input, plus a justified bridge to L744's full form. Seed positivity,
finite-window invertibility at the nominated lengths, and uniform
iteration remain separate unresolved assumptions.

Full matching Mathlib coverage is not checked. There is no lemma or
sign theorem to formalize from this comparison. Supporting canonical
system, Fourier or determinant facts are not a matching boundary
extension theorem. No mathematical script, lemma, DAG edge or PROOF
argument changed. Original nominations and prior evidence remain.

An independent fixed-window supersolution source question is nominated
in `2026-11-04-neutral-supersolution-certificate-coverage.md`. Its
coverage is REVIEW_REQUIRED, not a selected supersolution or an
approved creative proof target. The older nodal/ground-state comparison
must be reused: generic pole-free Markov structure is already covered
and cannot count as a new mechanism. The changed question must yield
a concrete paid certificate for neutral tests or be parked promptly.
