# Independent inverse/count audit — approved source scope2035

TARGET: Independently audit C029t's exact fixed-operator inverse and six rational Rouche disks, including the multiplicity count below Im(t)=-2 and the qualified de Bruijn specialization.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused unchanged discovery2032/assessment2033 searches and exact-operator comparison; inspected C029t scope, C029n finite definitions and stop2034. No new discovery search was necessary for the same fixed audit target.
SOURCE_EVIDENCE: Reused assessment2033 and discovery2032; directly rechecked NIST DLMF18.22.16-18; de Bruijn1950 Lemma2 and complete proof, printed p215; Berkeley Lecture23,22April2026, Rouche statement/proof and multiplicity discussion. URLs and exact inspected scope below.
COMPARISON: C029t specializes the same fixed operator and full U_6; an independent audit must compare the complete new coefficient and contour evidence with the covered statements, rather than treating successful self-checks as independent validation.
GAP: Source scope is approved; independent coefficient normalization, uniqueness/actual degree, six strict rational contour inequalities, complete degree coverage, boundary placement and prefactor/leading-real-part checks remain unperformed.
REASON: Exact source hypotheses cover the proposed finite audit, but neither the difference equation nor the zero-count theorems certify its actual arithmetic. Separate independent replay is necessary; no reproof, new mechanism, degree campaign or uniform conclusion is proposed.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED nomination requires separate approval of the new certificate audit; reuse unchanged coverage and inspect the essential exceptional cases, then return to mathematics.
SCOPE: Finite C029t audit only, under the fixed operator and full C029n coefficients. Known-method specialization, no general theorem novelty. Source review completed2035; no certificate replay or mathematical derivation performed.

The next research turn is approved to use a separate implementation or
direct rational checks of all load-bearing values. Preserve any discrepancy
rather than repair it silently. This approval does not audit the certificate.

Essential local inputs: C029t and C029n. C029m supplies only downstream
context; C029s is contrast. Artifacts are the exact script/certificate
`scripts/pollaczek/shift_inverse_halfplane_2034.py` and
`scripts/pollaczek/shift-inverse-halfplane-2034.json`. Inspect complete
selected certificate values with the shared JSON inspector. Approximate
seeds and previewed JSON do not prove any root count.

Acceptance requires all seven exact output coefficients, the distinct
positive source eigenvalues, both degree claims, six disjoint one-root
disks exhausting the degree, exactly two disks strictly below -2, none
crossing that line, and the correct de Bruijn hypotheses/conclusion.
Reject or qualify C029t on any actual gap; report inconclusive arithmetic
honestly. No eventual-only claim is being audited as established.

Unresolved assumptions outside this target: all-N inverse structure,
eventual uniformity, initialization and qualified compact convergence/
upstream[9]. They remain open even if the finite audit succeeds. Full
matching Mathlib coverage unchecked; no cross-notebook theorem input.

## Primary comparison completed2035

Sources accessed 20 November2026; prior search evidence remains in
assessment2033/discovery2032. No changed hypothesis or broader inverse
family is introduced.

[NIST DLMF18.22.16–18](https://dlmf.nist.gov/18.22#ii) gives the
Meixner-Pollaczek difference equation and its two coefficients. The
existing substitution lambda=3/4, phi=pi/2, x=t/2 is within scope;
polynomial identities permit complex t. Audit the signs and each
degree-dependent eigenvalue separately. The source does not supply
the full weighted sum's inverse coefficients or half-plane count.

[De Bruijn, Duke Math.J.17(3)(1950),197–226](https://repository.tudelft.nl/file/File_524a4d3c-0858-4c55-b425-8c8ce1fb89da),
DOI10.1215/S0012-7094-50-01720-0, Lemma2, printed p215 (PDF page19),
states the polynomial real-part bound from lower-half-plane zeros.
Read the whole proof: common real zeros are removed; degree below
twice the count is trivial; argument variation treats separately the
case of a purely imaginary leading term, which reduces real-part
degree. These cover the cases C029t proposes to use, with nonzero real
part and multiplicities retained. The audit must still verify its W,
shift, prefactor and nonzero real part. Theorem9a's entire-function
assumptions are unnecessary here.

[Berkeley Lecture23,22April2026](https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_23.html),
Rouche theorem and complete proof (HTML lines52–60), counts zeros with
multiplicity for analytic functions on a bounded domain and boundary,
with strict boundary domination. The preceding multiplicity discussion
and following fundamental-theorem-of-algebra application cover the
counting conventions and polynomial degree exhaustion. Polynomials on
circular disks satisfy its analytic/domain hypotheses; actual strict
inequalities, linear coefficient nonvanishing, disjointness and boundary
placement require independent arithmetic. No theorem reproof is needed.

Recorded stop2034 already rejects this fixed finite baseline if correct;
the audit tests reliability of that evidence, not another parameter.
Continue if all stated checks pass; qualify or reject the finite stop
on a real discrepancy, and report inconclusive arithmetic as such.
Full matching Mathlib coverage remains unchecked. This source approval
is local process progress, not a new mathematical result.
