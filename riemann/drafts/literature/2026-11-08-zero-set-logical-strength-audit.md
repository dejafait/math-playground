# Strict zero-set condition: bounded logical audit

TARGET: Audit whether the strict normalized-defect zero-set condition is equivalent to RH, retaining simple and multiple off-line Xi zeros and the open interval 0<t<1/4.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed step123 exact-condition, modulus-monotonicity, stationary-set and transversality search in 2026-11-08-normalized-defect-zero-set-barrier.md. Targeted November8 defect/interpolation/failure/history searches found no completed logical audit of this exact condition; no originality inference.
SOURCE_EVIDENCE: Sondow-Dumitrescu arXiv:1005.1104 Theorem1/Corollary1 and Section3 full proof pp2-4; Matiyasevich-Saidak-Zvengrowski arXiv:1205.2773v1 Section2 Lemmas2.1/2.3, Corollary2.4 and Theorem1.1 proof pp3-4; van Hemert raw manuscript 20July2026 Section2 defect identity and Section6 zero case, lines130-204,445-469. Reuse DLMF1.9.30/31 and1.10.1 through the ready frequency-interpolation assessment. URLs and limits below.
COMPARISON: The known monotonicity theorem and the local analytic defect identity cover the tools, not the exact conditional inequality. The remaining specialization is to test both implications without assuming nonvanishing at a hypothetical Xi zero or asserting a second-derivative sign from monotonicity alone.
GAP: Exact logical strength of the proposed strict condition is unproved here. The audit must evaluate its implications at arbitrary-multiplicity off-line zeros and check any reverse implication from the precise source product argument; it must retain positive normalizers and t-regularity.
REASON: A terminal circularity check can decide whether this is an independent input before further theta-sign research. No general crossing lemma, proof of the actual-theta condition or fresh numerical experiment is warranted. A local specialization is necessary because no inspected source states the exact normalized condition.
SCOPE: Only a proof audit of the conditional assertion below for the actual Xi of L018/L020 and C_y,A_0 of L898-L900. No altered strictness, exclusion of Xi zeros, simplicity hypothesis, endpoint extension, frequency band or new positivity premise. This assessment is newly written and receives separate next-turn approval before invocation.

The assertion to audit, without presuming it, is

    For every real x and every 0<t<1/4:
    C_(sqrt(t))(x)=0 implies
    d/dt[C_(sqrt(t))(x)/A_0(sqrt(t))]<0.

The main gap is L030-L032/C032a all-degree mixed positivity. The
bounded target here is logical scope, not an attempt to prove that
inequality. Its use is to reject a circular premise or expose exactly
what independent information it could add. Proving an equivalence
would not be progress toward proving its sides. A failed implication
must be documented with its precise hypothesis or contact case.

## Ready coverage and scope comparison

Reuse the full citations and primary cases in the completed
[step123 comparison](2026-11-08-normalized-defect-zero-set-barrier.md).
The cited primary links are
[Sondow-Dumitrescu](https://arxiv.org/pdf/1005.1104),
[Matiyasevich-Saidak-Zvengrowski v1](https://arxiv.org/pdf/1205.2773v1),
and [van Hemert's retrieved raw manuscript](https://raw.githubusercontent.com/LeonardSEO/certified-riemann-xi-positivity/main/paper/main.tex).
Sondow-Dumitrescu's open zero-free half-plane hypothesis cannot be
silently supplied under the proposed condition. The short Xi product
proof in1205.2773 explicitly gives a strict real logarithmic-derivative
sign when its zero-location hypothesis holds. Its Lemma2.1 has an
explicit nonvanishing restriction, and its Lemma2.3 converse is weak.
Use those exact statements, not a general claim that a strictly
increasing differentiable function has strictly positive derivative.

Van Hemert Section2 supplies the actual-kernel defect identity and
polynomial-exponential domination; Section6 treats a hypothetical
Xi zero in the open height strip without assuming simplicity.
It does not evaluate the newly proposed derivative there. No finite
computed band or unverified Section11 equivalence assertion is a
substitute for the two directions of this audit. The raw source's
revision and peer-review status remain unverified.

The already inspected
[DLMF Cauchy formulas](https://dlmf.nist.gov/1.9#iii) and
[analytic Taylor theorem](https://dlmf.nist.gov/1.10.E1), version1.2.8,
are reusable through
`2026-11-08-frequency-weighted-xi-defect-interpolation.md`.
Only ordinary analytic differentiation is needed. Import the standard
tools, without a new proof of Cauchy's formula, Taylor's theorem or
the Hadamard product. This is a local hypothesis/chain-rule audit,
not a creative sign mechanism or a claim beyond known methods.

Read L018 and L020's full statements/proofs in preparing this
nomination: L018 gives exact zero correspondence, preserved
multiplicities, symmetry and exclusion of the strip boundaries;
L020 supplies the actual Fourier representation and fixed-order
domination. Essential local inputs are L018, L020, L898-L900, with
L899's positive normalizers. L312 and C900a are contrasts only.
Do not add dependency edges for those contrasts or for this nomination.
No cross-notebook input.

## Discriminating audit and stopping rule

At a hypothetical off-line zero, use the squared modulus rather
than a logarithmic quotient. Check whether the condition is even
compatible with a simple zero and with a multiple zero. Treat the
strict inequality literally: a zero derivative is not acceptable.
Track y>0, the change t=y^2, the real positive normalizer, and any
term that vanishes specifically on the zero set. Check actual
differentiability by the existing analytic/domination arguments;
Lipschitz continuity alone would not establish it everywhere.

For the reverse implication, inspect the exact sign supplied by
the source under RH and whether the antecedent can occur. Do not
replace this with a new crossing argument or assume a boundary
margin. Retain all real x, central real zeros and arbitrary
multiplicity. The open t interval requires no theorem at t=0 or1/4;
L018's boundary exclusion is the relevant zero-location input.

Stop after this one two-direction logical test. If the condition
is equivalent to RH, retire it as an independent premise absent
a materially new theta-specific estimate. If not, record the exact
failed direction and do not presume any sign mechanism survives.
No actual theta sign, negative example, equivalence, derivative
formula or lemma is established in this literature nomination.
The missing independent theta estimate blocks creative routing;
do not manufacture one for scheduling balance. Full matching and
supporting Mathlib coverage remains unchecked.
