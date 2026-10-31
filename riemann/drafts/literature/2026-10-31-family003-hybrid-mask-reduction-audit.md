# Hybrid moving-mask reductions — conditional audit coverage

TARGET: Audit the conditional implication from lem:completed-quadratic-reduction and eq:cubic-large-sieve to the two moving-mask reductions and old-eq:4.6b in family 003 at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, preserving original source support, coefficient independence, divisor charges and bounded or empty quotient cases.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the terminal assessment's inspected Goldmakher–Louvel and Xu–Sang comparisons; searched ATTEMPTS and relevant family003 assessments, notes, L541 and immediate history for the exact masked implication. No completed matching local audit was found; failed searches imply no novelty. See drafts/audits/2026-10-31-family003-hybrid-mask-source-notes.md.
SOURCE_EVIDENCE: Pinned build/paper.tex: entire completed-quadratic-reduction statement 2518–2566 and essential support/normalization proof 2567–2626; cubic-large-sieve display and support/orientation qualifications 7036–7053; entire hybrid statement and proof 7054–7194. The original Heath-Brown Theorem 2 remains unread; its pinned displayed formulation is expressly retained, not independently verified.
COMPARISON: The source already claims the entire hybrid norm and both mask reductions. The needed quadratic input is its weighted arbitrary-complex-coefficient estimate, not the bounded-coefficient norm corollary. General quadratic/sextic results do not directly supply this structured two-mask implication. A conditional reproduction audit is justified to test the retained L541 contract, not to claim novelty.
GAP: Essential source coverage is complete for this bounded conditional audit. Zero identities, permissible support enlargements, independence after fixing divisors and h,t, and all charges still require mathematical verification. Both primitive estimates, their independent arithmetic proofs, uniformity beyond the fixed hypotheses, global manuscript closure and Xi signs remain outside the audit.
REASON: SPECIALIZE approves the scope of a separate reproduction audit of a source-claimed implication. This assessment is newly written during a literature turn and requires separate next-turn approval before research; no hybrid estimate was derived here.
SCOPE: Fixed finite S and fixed support-comparison constants; K,N,B,L>=1; squarefree primary k,n,P, unrestricted primary b; k,P avoid S, n,b retain allowed S-primes other than lambda and may share primes. Bounded a(P), beta(n,b), with a independent of k,n,b and beta independent of k,P; only independence-preserving fixed supports/sectors. Retain the two exact estimates below, their stated uniformity, source zero/multiplicative/reciprocity conventions and standard ideal/divisor counts. Exclude proving either primitive estimate, structural reflection, other measures/orders, global closure and Xi signs.
LITERATURE_REASON: This interior hybrid implication was excluded from the terminal audit; its essential weighted quadratic theorem interface had not previously been inspected for this application. That missing coverage is now supplied; unchanged additional browsing is not justified.

Primary citation: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, 30 September 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[pinned primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Stable labels fix the inputs; line numbers locate the inspected version.

## Retained estimates and required interfaces

1. `lem:completed-quadratic-reduction`,
   `eq:completed-quadratic-reduction`: arbitrary complex beta independent
   of the squarefree good row, with fixed original (n,b)-support.
   Write b=gt^2, c=(n,g), n=cm, g=ch and c=rc'; c,m,h are pairwise
   coprime squarefree, while g,t may share primes. With q_c asymp C,
   q_g asymp G, q_t asymp T and B asymp GT^2, its block output is

   \[
   (KNB)^\epsilon T\sum_{q_t\asymp T}
   \sum_{\substack{r\ {\rm sf},\ (r,S)=1\\q_r\ll\min(K,C)}}
   \left(\frac K{q_r}+\frac{NG}{C^2}\right)\frac C{q_r}
   \sum_{(c',m,h)\in\mathcal D_r(t)}
   |\beta(rc'm,rc'ht^2)|^2.
   \]

   D_r(t) means reconstruction into the original support and dyads,
   with all stated squarefreeness/coprimality conditions. Constants
   are uniform in coefficients and permitted fixed restrictions for
   fixed S and comparison constants. Fixed sectors/bounded row scalars
   are allowed; empty ranges vanish and bounded ranges include units.
   The primitive includes the row-t restriction and full row-c divisor
   expansion; it does not leave a new residual row-c' mask. Its S-part
   split is internal: output m,h are the original ideals, and c' keeps
   its original S-part. The bounded-beta corollary is insufficient.
2. `eq:cubic-large-sieve`: for arbitrary complex coefficient c_b,
   squarefree primary a,b with q_a<=U, q_b<=V, retain the norm bound
   (UV)^epsilon {U+V+(UV)^(2/3)} sum_b |c_b|^2 and its stated
   reciprocity/conjugation orientation. The stars mean ideal
   squarefreeness, not squarefree rational norm. No rational-prime or
   extra S-exclusion is allowed. Fixed coefficient support is zero
   extension, not a monotonicity claim for arbitrary masked sums.
   This is the pinned formulation citing Heath-Brown, *Kummer's
   conjecture for cubic Gauss sums*, Israel J. Math. 120A (2000),
   97–124, Theorem 2; the original is not independently imported.

## Source-claimed application to test next turn

Check the whole chain 7085–7194, without treating its conclusion as an
input. The target norm is the left side of `old-eq:4.6b`, containing
q_P^(-1/2), chi_k(nb)^3, chi_P(n)^(-2), and both masks
1_(P,k)=1 and 1_(P,b)=1. Required output is
(KNBL)^epsilon (K+NB)B{N+L+(NL)^(2/3)} for every epsilon>0.

- Test `eq:hybrid-mark-mask-reduction`: complete D divisor expansion,
  rowwise Cauchy and the outer q_D^(-1) charge. After P=DP', k=Dk',
  a_D must remain tuple-only and beta_D source-only. Preserve zeros
  in both D-character factors and (D,b); do not reinstate (P',k').
- Test the application of the retained weighted reduction at K/q_D
  to beta_D times the inner P'-polynomial. This coefficient is not
  assumed bounded. Check `eq:hybrid-after-quadratic-reduction` with
  its full T sum_t, r range, K/(q_D q_r)+NG/C^2 and C/q_r factors.
  Original source support survives until a positive upper bound.
- Test the zero-preserving identity at 7151–7157, the tuple-only
  r-factor, and the fixed ht coefficient mask after fixing h,t,D,r.
  Only then discard |beta_D|^2<=1 and group c',m by squarefree
  j=c'm=n/r. Its permitted S-primes must remain. Enlarging the
  positive j-range must not introduce a j-dependent P'-coefficient.
- Replay the coefficient mass, grouping multiplicities, h and t
  counts and `old-eq:4.6c`; verify D/r dyadic summation, adjustable
  epsilon losses and the full B charge. No new power loss is allowed.
  Check empty and bounded quotient scales with fixed comparison
  constants, including possible positive subunit centers, rather
  than dropping a nonempty unit case by convention.

Continue only if the exact bound follows with those supports and
independences. Stop or narrow on an extra moving mask, unsupported
restriction, extra power or failed bounded-range normalization; preserve
the conditional input on failure. Success reproduces the source
implication only. It would permit a later reduction of L541 Hypothesis 2,
not immediate use of L541/L538 backwards, primitive verification or RH.
Mathlib coverage was not checked. No cross-notebook input.
