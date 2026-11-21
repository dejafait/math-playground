# Exact endpoint-null degree filter — ready test nomination

TARGET: Test eventual definition, normalization control and positive exponential quartet response for the fixed normalized three-degree endpoint-null filter on [n,2n], retaining the exact kernels and all quartet terms.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed step259 theorem-level comparison in 2026-11-10-endpoint-null-degree-filter-review-258.md, including exact/consecutive-degree searches and step233/235/244 failures; no inspected matching theorem and no novelty inference.
SOURCE_EVIDENCE: DLMF18.15.17-20 https://dlmf.nist.gov/18.15#iv (fixed alpha/M, uniform scaled additive error); DLMF10.17 https://dlmf.nist.gov/10.17#i and finite integration https://dlmf.nist.gov/2.3#i; exact connection https://dlmf.nist.gov/18.18.E18; Tao Proposition1.1.2/Exercise1.1.5/Proposition1.1.5 https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-142-tao7-higher-book-05june2012.pdf#page=13 via unchanged review246; Duran Lemma5.2/Theorem1.5 https://arxiv.org/html/2507.22425v1#S5 and Krattenthaler Theorem1/Section2.2 https://link.springer.com/article/10.1007/s11139-021-00514-8 are scope comparisons only. Full contracts and access qualifications remain in parent review258/review246.
COMPARISON: Known tools cover unfiltered bulk and finite-transform ingredients but not the normalized n-dependent filter's conditioning or signed response. Only this missing specialization is proposed; fixed-coefficient exterior asymptotics and a Christoffel identity cannot be imported as its answer.
GAP: Prove or refute eventual d_n!=0, sufficient normalization error control and the signed positive limsup; no actual-zero realization, other-zero dominance, original B_n/criterion transfer or complementary-range estimate is supplied.
REASON: Prepared in step259 and separately approved by literature-only recovery step260 after direct primary URLs were added to this assessment; target and mathematical coverage unchanged. Use existing coverage for one proof attempt rather than repeating searches. Expected classification REPRODUCTION, not a new central signed arithmetic mechanism.
SCOPE: Integers n>=2; K_m(u)=[L_(m-1)^(2)(u)-1]/(m-1); rows a_n=(K_n(n),K_(n+1)(n),K_(n+2)(n)), b_n=(K_n(2n),K_(n+1)(2n),K_(n+2)(2n)); d_n=a_n cross b_n with that orientation; c_n=d_n/sum_j|d_(n,j)| only when d_n!=0; F_n=sum_(j=0)^2 c_(n,j)K_(n+j) on [n,2n]; fixed Q={3/4+i*10^13,3/4-i*10^13,1/4-i*10^13,1/4+i*10^13}, weight1 each. No degree or quartet parameter sweep.

Use the [completed parent assessment](2026-11-10-endpoint-null-degree-filter-review-258.md)
for the full primary-source hypotheses, search record and comparison.
This is a new ready continuation, not a completed proof or an invocation
of research during its literature-only preparation.

The precise diagnostic is Z_n=-Re sum_(q in Q) integral_n^(2n)
exp((q-1)u)F_n(u)du and

    limsup_(n->infinity) log(1+max(Z_n,0))/n > 0.

Eventual definition on all large integers is a separate obligation;
do not silently restrict the family to a favorable subsequence.
Prove both endpoint constraints and normalization from exact values,
then supply the uniform neighboring-degree asymptotics, control of
normalization errors, every constant correction, all quartet terms
and a signed integer subsequence with smaller remainder. Do not
assume nonvanishing, uniform conditioning or frequency independence.
L987's [m,2m] transform is not itself the common [n,2n] transform.

Continue only on rigorously controlled spectral sensitivity. Infinite
exact degeneracy, zero exponential positive rate or an established
normalization obstruction stops this family. A vanishing first term
alone does not prove zero rate; an amplitude-only result or an unpaid
error/sign leaves the attempt unfinished. Save partial reasoning
before lengthy work and do not widen the target to another filter.

Essential local inputs: L985 exact connection; L987 fixed synthetic
benchmark and its checked tools; L988/L989 explain the endpoint
motivation only. L982 and steps233/235/244 are contrasts, not premises.
Downstream arithmetic use would require the F_n compensator and all
prime powers, followed by a separately justified link to original B_n
and L984(H). Actual Xi positivity, low-zero control, other zeros and
both complements remain unresolved. No cross-notebook input.

Full matching Mathlib coverage is not checked. Import general source
results, with only necessary local specialization; no general reproof
is needed. Expected proof_attempt/development routing reflects the
coupled asymptotic and sign obligations. The synthetic scope and
missing original-criterion transfer do not justify creative escalation.

## Separate source-link recovery approval — step260

10 November 2026. This literature-only approval repairs the reported
missing direct URL in the ready assessment. The exact TARGET, SCOPE,
SPECIALIZE decision and continuation/abandonment tests are unchanged.
No new theorem, mathematical calculation or proof audit is claimed.

Reopened the primary DLMF scaled Laguerre formula18.15.17-20 and its
complete uniformity statement: alpha and truncation M are fixed,
0<=x<=1-delta, and the remainder is additive with a Bessel envelope.
Reopened DLMF10.17.1-3 (fixed order and the argument sector) and
DLMF2.3.4-6 (finite endpoints, smooth amplitude, both endpoint terms
and a variation error bound). The latter's fixed-amplitude asymptotic
does not automatically provide uniform control of a moving family;
the later attempt must bound the finite remainder. No differentiation
of a remainder or division by an unexamined small determinant is licensed.
Duran v1 Section5/(5.1),(5.6), Lemma5.2 was reopened: its fixed real
coefficients and compact exterior domain exclude an automatic bulk
application. This is confirmation of existing coverage, not new evidence
against the filter. All other previously inspected contracts, including
Krattenthaler's determinant comparison and
Tao's rational-relation cases, are reused from review258/review246;
no claim that those sources were newly audited is made.

The optional Lindemann-Weierstrass source remains the previously
inspected [Fukshansky notes, Theorem6.2.1, printed p138](https://www1.claremontmckenna.edu/pages/faculty/lenny/papers/GNT_lecture_notes.pdf#page=142).
Its use requires distinct algebraic exponents and algebraic coefficients;
no frequency independence is established by this assessment. Full matching
Mathlib coverage remains unchecked. Local duplicate/failure comparisons
in review258 are reused, with no widened search or revived stopped route.

Coverage is ready for the saved attempt. This administrative repair is
STALLED in mathematical-outcome terms, with zero mathematical exploration
usage. Actual B_n, criterion transfer, other zeros, both complements and
L984(H) remain unpaid. No lemma, mathematical script, PROOF or DAG changed.
