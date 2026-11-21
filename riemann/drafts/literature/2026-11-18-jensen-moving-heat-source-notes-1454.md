# Conditional moving-heat transfer — source notes1454

18 November 2026. Literature-only review of nomination1453's saved target.
No specialization, new lemma, mathematical script or moment bound is
established here. The main gap is actual-Xi all-degree positivity
L030--L032/C032a; the exceptional-root deficit also remains unresolved.

## Exact question and saved boundary

Use C020l's positive integer-d sequence, X, q, B, J, fixed prime
window, L=floor(X^(1/1000)), original alpha and individual linear
tapers. Write Q_Z(t)=P_Z(t)M(t)^2, with exactly C020l's E_p(Z).
The proposed premise is

    sup_(Z in J) integral_J |Q_Z(t)|^4 dt <= C Bq^2.

This is an unproved premise, not an output of C020l. The desired
conditional conclusion is integral_J |Q_t(t)|^4 dt=O(Bq^2), with
an absolute constant and one original integer-d onset. The source
review must not replace the prime support, mollifier or hard interval.
Only one moving parameter is in scope. C019y's two own heat times,
shifted intervals and shifted fourfold coefficients are different.

Local reads: C020l hypotheses, (1)--(11), coefficient/heat portion of
audit1450; C019z hypotheses and audit1435's scale/heat range; C019p's
audited absolute-convolution range; review1447 and source-notes1410;
the saved attempt1453 and the scoped stop records1431/1437/1446.
No cross-notebook input is used. The startup PROOF and DAG were used
before these ranges; their mathematical assembly is unchanged.

## Primary source selected for a bounded test

Montgomery--Vaughan, *Multiplicative Number Theory II: Primes and
Sieves*, author-hosted draft, version date unidentified, Section19.1,
Lemma19.1, (19.5)--(19.6), printed pp150--151 (PDF pp162--163,
one-based). [Primary PDF, p162](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=162).
Read the complete statement and proof, including both subinterval
integrations and endpoint cases. For a<b, continuous complex f with
piecewise continuous bounded first derivative on [a,b], (19.6) states

    |f(x)| <= (b-a)^(-1) integral_a^b |f(u)| du
                       + integral_a^b |f'(u)| du,  a<=x<=b.

Its midpoint version (19.5) has half the derivative coefficient; it
cannot be used at arbitrary x. The proof uses the two endpoint kernels
and retains both. Only (19.6), including x=a or b, is proposed here. The source
has no arithmetic, complex-neighborhood or periodicity hypothesis.
It charges the derivative integral; it does not estimate that integral
for a family from frozen norms. No source reproof is proposed.

## Applicability question left for research

The proposed source substitution is the real nonnegative function
f(Z)=|Q_Z(t)|^4 for each fixed t, on [a,b]=J, at x=t. Its exact
parameter derivative, not the total derivative of Q_t(t), is at issue.
The finite fixed prime support and positive Z range are retained;
there is no moving entry floor in this P_Z. Checking differentiability,
the uniform constants and the ensuing integration is part of the
future specialization, not a result claimed in this literature step.

The explicit additional quantity to test is

    V_d = integral_(t in J) integral_(Z in J)
                    |partial_Z (|Q_Z(t)|^4)| dZ dt.

The proposed threshold is V_d=O(Bq^2), with one absolute constant.
This is the derivative term in the selected source framework, not an
assumption already contained in the frozen bound. No bound for V_d,
no derivative identity for E_p, and no sufficiency proof for the actual
family is derived here. In particular, C019z's audited
E_p(Z)=1+O(q^-2) controls coefficients, not this mixed absolute norm.
Do not infer a weighted prime-polynomial fourth moment by multiplying
the unweighted norm by a coefficient supremum. Such a multiplier claim
would itself need justification. A real-parameter approach is available;
complex extension is neither assumed nor required by the cited input.

Continue the proposed single test only if the original frozen premise
and exact heat structure pay V_d at Bq^2 (or provide a different fully
accounted application of this same source inequality). Otherwise save
the first unpaid norm and achieved bound, and park this implementation.
Failure of its sufficient variation estimate does not refute the
conditional transfer or the original moment. A bound with growing
logarithmic or X factors is not the requested uniform threshold.

## Other inspected comparisons, not mathematical premises

Visintin, *Notes on Sobolev Spaces*, filename Sobolev2010.pdf, version
date not identified: printed p10/PDF p10, the one-dimensional
W^(1,1)(0,1) point-evaluation argument and square-boundary discussion;
Theorem4.8, s>1/p, bounded Lipschitz domain. [Author PDF](https://visintin.maths.unitn.it/Sobolev2010.pdf#page=10).
Read that argument in full and the theorem statement. The general
trace proof is marked omitted. The interval argument also charges a
derivative norm; a general two-variable trace norm is stronger than
the stated frozen premise. The omitted theorem proof is not needed
or imported.

Kinnunen, *Sobolev Spaces*, author-hosted2026 notes, Theorem2.34,
printed p55/PDF p58: absolute continuity is equivalent to an integral
representation with an L1 derivative. Also read Theorem2.36 and
Remarks2.37(2), printed pp55--56, for the one-dimensional W^(1,p)
interpretation. [Author PDF](https://math.aalto.fi/~jkkinnun/files/sobolev_spaces.pdf#page=58).
These are supporting regularity statements, not an arithmetic norm
payment. The full ACL proof was not inspected or imported.

Vybiral, *A diagonal embedding theorem for function spaces with
dominating mixed smoothness*, author-hosted preprint, version date
unidentified: introduction (1.1)--(1.2), Theorem3.1 printed p6 and
Theorem4.1 printed p12. [Author PDF](https://people.fjfi.cvut.cz/vybirja2/publ/Vybiral5.pdf).
Read their statements, not the complete proofs. They require positive
mixed smoothness and corresponding function-space norms; these are
not supplied by the frozen premise. No theorem or endpoint case from
this paper is used. A future use requires its complete applicable
proof cases and a separate norm comparison.

Reuse1447's exclusions of ordinary-zeta/Watt inputs and1410/C020l's
G.16 finite-frequency input without reopening their source assessments.
G.16 can estimate a specified fixed coefficient array, but it is not
an automatic diagonal or coefficient-multiplier theorem. It remains
available for a future explicitly quantified derivative-norm test.

## Discovery and duplication checks

Actual queries included:

- `Dirichlet polynomial variable coefficients partial summation maximal mean value heat weights fourth moment`
- `Sobolev inequality interval supremum integral derivative Lp fundamental theorem calculus parameter maximal estimate`
- `"Sobolev" "sup" "Dirichlet" "derivative" polynomial`
- `Sobolev trace diagonal mixed norm derivative parameter Lp interval theorem`
- `"Bernstein" "exponential sums" "local" "Lp" inequality`
- `"Sobolev" "inequality" "F" "Dirichlet polynomials" Gallagher`
- `"sup" "integral" "derivative" "Sobolev–Gallagher" inequality`
- `"Sobolev" "Lemma 1.4" Iwaniec Kowalski`
- `"heat" "Dirichlet polynomial" "fourth moment" weights`
- `"parameter" "frozen" "diagonal" "Sobolev" bound`
- `"Dirichlet polynomials" "variable coefficients" "derivatives"`

Search summaries are discovery aids, not evidence for theorem claims.
Bernstein/exponential-sum, Gallagher's original large-sieve paper and
Iwaniec--Kowalski leads were not inspected at theorem level and supply
no premise. The directly inspected Lemma19.1 supplies the selected
tool, so none of those unread leads is essential to this bounded test.
No full matching conditional heat-transfer theorem was found in this
bounded search; neither absence nor novelty follows.

Stops1431/1437/1446 concern respectively arithmetic completion,
absolute-neighbor costs and whole-window low-height energy; attempt1453
retains unpaid signed near modes. None is permission to resume those
implementations, and none proves that this conditional analytic test
fails. No matching completed local transfer was located in the narrow
Jensen assessment/attempt search. Full matching Mathlib is unchecked.

The coverage decision is EXPLORE for one real-parameter variation
test. The standard source inequality is known mathematics; the exact
uniform transfer and its variation payment remain unproved. No
mathematical exploration budget resets, informative lower obstruction,
RH candidate or progress beyond the inspected sources is asserted.
Next coverage is newly written and requires the supervisor's separate
approval before a mathematical invocation.
