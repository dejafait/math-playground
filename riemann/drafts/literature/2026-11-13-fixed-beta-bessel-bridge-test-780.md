# Fixed beta/Bessel discriminator — source scope approved in step781

TARGET: Test whether F(t)=1F2(3/2;1,100;-t^2/4) satisfies every qualitative order-one coefficient/cosine hypothesis of assessment779 and has det(H_1)<0, with exact arithmetic and justified beta/gamma/Bessel specializations.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step781 reused assessment779's exact-statement and stronger-result searches, then checked the prescribed beta-Bessel/52.4865/1F2 target in November13 literature, attempts and history. Only the proposed continuation and parent source screen matched; C040b records a different exhausted fixed test. No novelty inference or broad search repeated.
SOURCE_EVIDENCE: Reused assessment779 and rechecked Sokal JMAA515(2022)126432 p1 and AppendixA Propositions6-7/(12)-(14), pp5-6; Berg math/0412340v1 Theorems5.1-5.2, printed14-15, statements and relevant proof cases; DLMF1.2.8 equations16.5.2/10.9.4/10.16.9/5.9.16 and adjoining domains. Direct citations and source-slot comparison below.
COMPARISON: Known sources cover the general order formula, gamma/beta power-moment laws, beta transform and Bessel cosine identity. They do not establish the simultaneous local premises or this exact H_1 determinant; only those specializations and a single rational sign certificate are authorized. Sokal's decimal threshold cannot replace the certificate.
GAP: Joint-property proof and single exact H_1 certificate remain unperformed. Required differences are factorial/geometric normalization, independent product-law realization, actual L1 density and interchanges, exact composed order, strict all-order differences including n=0, and the finite logarithmic coefficient calculation. Actual-Xi and stronger quantitative hypotheses remain outside scope.
REASON: Separate source review now approves the unchanged target as a bounded known-method specialization; no essential source blocker remains. Import general theorems rather than reprove their moment-divisibility or entire-function theory.
LITERATURE_REASON: This is the required separate approval of assessment780, whose fixed joint-premise target differs from assessment779's class question; it reuses ready parent coverage and checks exact source domains, not an additional broad search on a ready target.
SCOPE: Exactly the fixed function, qualitative premises and H_1 defined below; next-turn classification REPRODUCTION, calculation/standard/high. This approval establishes source sufficiency, not any of the requested mathematical conclusions.

## Exact prospective target, not established conclusions

Use (a)_n=Gamma(a+n)/Gamma(a). Define the prescribed function by
the standard1F2 series. Extract gamma_n from
F(t)=sum_(n>=0)(-1)^n gamma_n t^(2n)/n!, retaining the factor4^(-n).
Put G(w)=1F2(3/2;1,100;-w/4),
S_k=-k[w^k]log G(w) at0, and H_1=((S_2,S_3),(S_3,S_4)).
No sign of this matrix is certified in this assessment.

The obligations are exact entire order one (not merely an upper bound),
F even real with F(0)=1, gamma_n>0, and
(-1)^(r-1)Delta^r log(gamma_n)>0 for all integers n>=0,r>=2.
For every real c>0 the inverse-coefficient powers must be normalized
Stieltjes moments. The cosine representation must have an actual
nonnegative L1 density of mass1 with all moments, not just a measure.
Finally prove det(H_1)<0 or report the exact contrary/failing evidence.

## Applicability and necessary specialization

Reuse the parent assessment's primary evidence. For the cosine premise,
the beta-transform parameters3/2 and100 satisfy its strict ordering;
the remaining0F1 has denominator1, so the source's Bessel parameter0
is admissible. A future proof must justify the resulting density,
normalization and interchanges, including endpoint integrability.
For inverse moments, check a factorization into the ordered beta and
gamma laws actually covered by Berg for every c>0; arbitrary quotients
are not covered. For log differences, justify differentiated integrals
on x>=0 and strictness at n=0. These tasks are pending specializations,
not a new all-degree theorem to be assumed during approval.

For growth use the source's nonterminating positive-parameter order
formula, checking how t^2 composition changes order. For the matrix
use exactly the first four nonconstant coefficients and rational Newton
identities or direct formal logarithm expansion. Any script must save
the full exact certificate and print its sign and required threshold0.
Sokal's decimal threshold is motivation only; any continued-fraction
comparison must check normalization, indexing and earlier nonvanishing.
No general converse in Proposition6 is needed for a direct determinant.
No zero approximation, Conjecture8, actual theta identity, Kawano
certificate or stronger continuous Mellin hypothesis is an input.

Stop after this fixed test. Joint premises plus a negative determinant
would refute only the stated generic implication. A nonnegative matrix,
failed premise or incomplete certificate closes this discriminator
without parameter, precision, degree or adjacent-minor sweeps.
Downstream use is to identify whether a theta-specific bridge remains
necessary; actual-Xi L030-L032/C032a and global assembly remain open.
Essential notebook context is L030-L032/C032a; C040b is contrast only,
not a mathematical premise. No cross-notebook input. Matching Mathlib
coverage is unchecked. Source approval completed in step781; route as calculation/standard/high,
with REPRODUCTION classification; this is not a creative proof attempt.

## Separate source-scope review, 13 November 2026 — step781

Reuse the queries, stronger-result comparison and unread-lead distinctions
in `2026-11-13-order-one-qualitative-bridge-scope-779.md`. Assessment778
and C040b were checked specifically for the normalization and prior stop:
that order4/3 model passed its prescribed H_3 test, so it is closed.
The present order-one family was nominated by a different primary
obstruction, not by tuning that model. KPS's extra separated
Bernstein-Pick hypothesis remains outside the proposed premises;
its earlier assessed scope is reused without reopening the source route.

[Sokal, published author PDF](https://discovery.ucl.ac.uk/id/eprint/10150527/1/Sokal_1-s2.0-S0022247X22004462-main.pdf),
JMAA515(2022)126432, p1 gives exact entire order1/(q-p+1) for
nonterminating p<=q, with denominator parameters avoiding nonpositive
integers. AppendixA, pp5-6, uses logarithmic-derivative moments;
(12)-(14) and the b1=1,delta=1/2 example motivate this test.
The source's normalization and continued-fraction sequence are different
from the displayed H_1 convention. No determinant sign is imported.
The finite germ calculation avoids needing the general converse in
Proposition6, Conjecture8, or earlier continued-fraction nonvanishing.
Exact order after the t^2 composition still needs justification.

[Berg, *On powers of Stieltjes moment sequences, II*](https://arxiv.org/pdf/math/0412340v1),
arXiv v1/17December2004, internal date27August2018, Theorems5.1-5.2,
printed14-15, supplies (a)_n^c for a>0 and
((a)_n/(b)_n)^c for 0<a<b, every real c>0. The corresponding
probability Mellin transforms are [Gamma(a+z)/Gamma(a)]^c and
[Gamma(a+z)Gamma(b)/(Gamma(a)Gamma(b+z))]^c on Re(z)>-a.
The gamma proof applies its Bernstein-function theorem to a+s;
the beta proof uses (a+s)/(b+s), bounded moments and product convolution.
This includes c>2 even when the gamma moment problem is indeterminate:
uniqueness of a representing moment measure is unnecessary here.
The prospective source slots are gamma a=100 and beta a=1,b=3/2;
their domains include all nonnegative integers. Establishing that their
product and a positive scale give exactly gamma_n^(-c) is left to
the next calculation. No closure under arbitrary quotients is assumed.

NIST DLMF1.2.8, release15September2026, was rechecked at the exact
equations and adjacent hypotheses. [16.5.2](https://dlmf.nist.gov/16.5#E2)
requires p<=q and Re(b0)>Re(a0)>0; it integrates the lower
hypergeometric function at zt over0<t<1 with normalized beta weight.
Here its intended slots are p=0,q=1,a0=3/2,b0=100, and remaining
denominator1. These are distinct from the inverse-moment beta slots.
[10.16.9](https://dlmf.nist.gov/10.16#E9) connects that 0F1 with
J_nu, using denominator nu+1; [10.9.4](https://dlmf.nist.gov/10.9#E4)
is the Poisson cosine integral, Re(nu)>-1/2. The intended nu=0
is admissible without a branch ambiguity. These identities cover the
proposed transformation, but do not supply its final density proof:
derive the density by a change of variables and justify nonnegativity,
mass1, endpoint integrability, all moments and Fubini/Tonelli explicitly.

[DLMF5.9.16](https://dlmf.nist.gov/5.9#E16), in the adjoining
Re(z)>0 domain, is the digamma integral. Differentiating and taking
finite differences needs local domination and strict sign at every
n>=0,r>=2. Those are elementary specialization obligations, not
already established all-order inequalities. The exact normalized
series and first four coefficients must be retained in the certificate;
no zero-sum interpretation or actual-Xi input is necessary.

The web reader rejected TeX downloads as an unsupported content type;
the complete relevant formulas and domains were available in the HTML
equations, so this caused no essential access gap. Primary proofs and
statements were used; snippets and the decimal obstruction were not
certificates. No mathematical derivation or script was performed in
this approval. Matching Mathlib coverage remains unchecked. The
unchanged TARGET above is now ready; no further approval turn is needed
unless its scope changes.
