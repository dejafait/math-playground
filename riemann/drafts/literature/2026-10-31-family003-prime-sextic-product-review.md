# Prime sextic product — completed source comparison

TARGET: Audit the prime sextic product identity gamma_1(p)gamma_2(p)=conj(chi_p(4))gamma_3(p)gamma_2(p)^3 for good primary primes.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the exact mixed Jacobi statement, sextic Gauss products and Hasse–Davenport duplication; inspected Cohen Lemma 4.9, Conrad Appendix A and Chan–Long–Yang Lemma 3.2. Narrow local searches of L546/L548, the prime-cubic assessment/notes and prime histories found no completed sextic audit; the cubic scope explicitly excludes it. Queries and access qualifications are below. No novelty is claimed.
SOURCE_EVIDENCE: Cohen, Computational Number Theory in Relation with L-Functions, Definitions 4.2/4.3/4.5 and Lemma 4.9, printed pp. 22–26; Conrad, Gauss and Jacobi sums on finite fields and Z/mZ, Theorem 2.4 and (2.2), p. 3, Appendix A (A.5) and footnote 8, p. 19; Chan–Long–Yang, American Mathematical Monthly 118 (2011), 316–326, Lemma 3.2 and complete proof, pp. 319–320; pinned OpenAI TeX commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, complete lem:prime-gauss-identities, lines 703–769. L556 supplies already audited additive-character conventions.
COMPARISON: Cohen states the exact mixed Jacobi input for arbitrary odd prime-power fields; Conrad gives the equivalent duplication formula. These cover both residue degrees, whereas the inspected published Chan–Long–Yang proof is prime-field only. The pinned source already asserts the entire target. A subsequent local audit is reproduction of known mathematics with character/additive/normalization specialization, not a new identity.
GAP: Source coverage is sufficient; the remaining work is a separate application audit of exact sextic order, quadratic power, nonprincipal product hypotheses, additive-character transport, allowed cancellations, chi_p(4) conjugation and P-normalization for both residue degrees. No product identity is derived or premise discharged in this literature step.
REASON: The essential missing mixed-Jacobi statement has been inspected independently of the claimed target. SPECIALIZE permits the bounded reproduction audit after separate next-turn approval. Cite the finite-field identity rather than reprove it; checking the retained notebook normalization is necessary. Composite propagation and analytic/sign inputs are excluded.
SCOPE: O=Z[omega], lambda=1+2omega, e(z)=exp(2pi i Tr(z/lambda)); good primary p=1 modulo 3 outside fixed S containing primes above 6; P=N(p); H=chi_p defined by the sextic Euler rule; every power zero at zero; gamma_j(p)=P^(-1/2) sum_x H(x)^j e(x/p). Include split and inert primes. Exclude composite propagation, other local Fourier formulas, coefficients, arithmetic uniformity and Xi signs.
LITERATURE_REASON: The target at invocation was REVIEW_REQUIRED and lay outside the ready cubic scope; independent mixed-Jacobi coverage and its finite-field domain were essential unread inputs. This step supplies that coverage; further literature is not the default continuation.

## Inspected primary statements and qualifications

Henri Cohen, *Computational Number Theory in Relation with L-Functions*,
[author-hosted course PDF](https://www.math.u-bordeaux.fr/~cohen/rennes2.pdf),
Lemma 4.9, printed p. 26, states for odd q, the quadratic character eta,
and nontrivial A:

\[
 A(4)J(A,A)=J(A,\eta).
\]

Its equivalent Gauss formula, requiring additionally A!=eta, is
G(A)G(A eta)=A(4)^(-1)G(eta)G(A^2).
Definitions 4.3/4.5, pp. 23–24, give zero at zero for nonprincipal
characters but one for the principal character. The future application
must therefore check every character used is nonprincipal before
identifying conventions. The domain is all finite fields of odd
prime-power size. The lemma is stated without proof and assigned as
an exercise; no proof in these notes is claimed inspected. The PDF has
no inspected version date; accessed 2026-10-31.

Keith Conrad, *Gauss and Jacobi sums on finite fields and Z/mZ*,
[author PDF](https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf),
Appendix A, (A.5), p. 19, states the same duplication relation as
G(A^2)=A(2)^2 G(A)G(A eta)/G(eta), for nontrivial A and odd q.
Footnote 8 discusses A=eta. This formula is stated rather than proved
there. Theorem 2.4 requires AB nonprincipal; equation (2.2) requires A
nonprincipal. Reuse L556's inspection and additive-character transport.
All characters here are zero at zero. No new quadratic Gauss phase
or lifting theorem is needed merely to cite these inputs.

Heng Huat Chan, Ling Long and YiFan Yang, *A Cubic Analogue of the
Jacobsthal Identity*, **American Mathematical Monthly** 118 (2011),
no. 4, 316–326, DOI 10.4169/amer.math.monthly.118.04.316,
[institutional PDF](https://ir.lib.nycu.edu.tw/server/api/core/bitstreams/a28f9c57-9f67-45ee-9c95-c5e3484d6884/content),
Lemma 3.2 and complete proof, pp. 319–320, states the same Jacobi
identity over F_ell for odd rational prime ell, with zero extensions
specified in Section 2. Its proof counts roots using
(2x-1)^2=1-4y and drops the sum of A. Although its displayed lemma
says character without excluding the principal one, that cancellation
uses nontriviality. Retain that hypothesis, as Cohen does. No principal
case is imported. This proof was inspected only in its stated prime-field
domain; Cohen provides the separate all-prime-power statement, so no
extension of this proof is being derived here. Its cited Berndt–Evans–Williams
Theorem 2.1.4 is an unread upstream reference, not an inspected book input.

The claimed target source is OpenAI, *The Quasi-Riemann Hypothesis*,
30 September 2026,
[pinned TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Read the entire prime lemma and proof, lines 703–769; the relevant
mixed step is 736–745. It uses the quadratic power H^3, a mixed
Jacobi relation, Gauss–Jacobi products and the inverse cubic pair.
The full normalized target is already its second asserted identity.
This is a report of its proof, not a local verification. L556 already
fixes the cubic unit and additive character; the next audit must not
silently substitute absolute values for phases.

## Search record, local comparison and Mathlib

Queries included `Gauss Jacobi sums quadratic duplication identity
J chi phi chi 4 J chi chi finite fields`, `sextic Gauss sums gamma1
gamma2 cubic Jacobi Hasse Davenport`, and exact mixed-Jacobi variants.
The all-field theorem above supplies the required coverage. An Evans
1979 PDF fetch timed out; that source is not an input. Search hits for
a recent hypergeometric paper and automated course notes were not used
as theorem evidence. No failed search supports a novelty inference.

L546 Hypothesis 2 and L548's retained finite Gauss inputs are the
intended interfaces. The ready cubic assessment and L556 cover a
different identity and are reused only for their established conventions.
No completed sextic audit or sextic failure was found in the narrowly
searched prime assessment/working/history paths. No claim is made
about the entire archive or any sibling notebook.

Reused L556's Mathlib support record. Newly inspected the official
[JacobiSum/Basic.lean](https://raw.githubusercontent.com/leanprover-community/mathlib4/master/Mathlib/NumberTheory/JacobiSum/Basic.lean),
including `jacobiSum_mul_nontrivial` and
`jacobiSum_eq_gaussSum_mul_gaussSum_div_gaussSum` hypotheses. The latter
requires fields, nonzero image of the field cardinality, nonprincipal
product and primitive additive character. These are supporting results.
A bounded search for quadratic/duplication coverage in that file found
no matching mixed identity; availability elsewhere remains unchecked.
No Lean verification was run.

## Bounded continuation

Use L556's field/additive-character normalization, L546 Hypothesis 2
and L547/L548's character conventions. Audit the exact target for both
residue degrees, checking the finite-field theorem hypotheses,
nonzero denominators, conjugation of H(4) and every power of P.
L556's cubic value may be cited if needed; no composite or analytic
conclusion follows. Preserve and stop the proposed discharge if any
sign, character or normalization mismatch remains. A norm identity or
unspecified root of unity is insufficient.

The downstream use is to reduce one more finite-Gauss premise in the
reflected coefficient route. Actual-Xi all-degree positivity, raw
coefficients, arithmetic-uniform closure and signed transfer remain
independent gaps. This assessment supplies coverage only; the mathematical
application remains unaudited. Newly ready coverage awaits the supervisor's
separate approval turn. No lemma/script or argument overview is changed.
No cross-notebook input.
