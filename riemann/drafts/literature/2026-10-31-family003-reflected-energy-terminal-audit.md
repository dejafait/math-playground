# Terminal reflected energy — conditional application audit coverage

TARGET: Audit the conditional terminal reflected-energy estimate in family 003 lem:reflected-energy at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, checking the fixed-part exponent, common-profile and mask hypotheses, actual row/width constants and the single O/2 summation charge, while retaining the named structural reflection and hybrid-norm inputs as contracts.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The completed terminal-scope review searched family003 assessments, L531–L540, relevant histories and ATTEMPTS, and compared primary source statements with exact-term/standard-terminology web searches. No matching completed local audit or counterexample was located. Search failures do not establish novelty; details and the distinction between primary evidence and unread leads are in drafts/audits/2026-10-31-family003-reflected-energy-source-notes.md.
SOURCE_EVIDENCE: OpenAI September 30, 2026, commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, build/paper.tex: 6890–7030 marked reflection and all pair-phase/zero-mask cases; 7031–7194 complete hybrid norm statement/proof; 7200–7581 complete terminal data, theorem, proof, row/width comparison and empty-slot case; 2386–2453 complete common-profile lemma/proof/norm consequence; 2460–2469 lattice-tail statement; 2714–2866 full structural extraction cases. L538 Hypotheses 1–4 were read. Goldmakher–Louvel v2 Definition 1/Theorem 1.1/Corollary 1.2 and Xu–Sang v2 definitions (1.1)–(1.2)/Theorem 1.1 were inspected for overlap, not as substitutes for the terminal theorem.
COMPARISON: The source claims this entire terminal estimate, including its fixed-part and aggregate forms. The proposed work checks its application of explicit primitive inputs and its bookkeeping; importing the terminal conclusion or L538's canonical conclusion would bypass that check. General quadratic and arbitrary-coefficient sextic sieves have different coefficient/mask interfaces and do not replace the structured hybrid estimate. Reproduction is warranted by the unresolved external-premise audit, not by novelty.
GAP: Source coverage is adequate for the stated bounded conditional application audit. The implication from the named structural identities and hybrid bound to the terminal estimate, with exact normalization, common Fourier density, source support, positive summation and uniform losses, remains to be checked mathematically. Primitive arithmetic and actual-Xi positivity remain unresolved.
REASON: SPECIALIZE permits a separate reproduction audit of a source-claimed implication. This assessment was written in a literature-only turn and must receive separate next-turn approval before invocation. No new terminal bound has been proved in this review.
SCOPE: Exact product-form disjoint prime slots; fixed base character and puncture independent of k,f; bounded log-length ranges; original element rows and source dual support, including allowed S primes and shared n/b primes; frozen nonresidual parts and separate full reflection sectors; common compact logarithmic profile; all retained, discarded, bounded and empty cases. Retain the explicit inputs below. Exclude a proof of those primitive inputs, other measures/orders, full manuscript closure and Xi signs. No cross-notebook input.

## Precise primary citation and what is imported conditionally

OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
Re(s)>7/8*, 30 September 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[pinned primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Stable labels, rather than line numbers alone, fix each input.

1. Retain `prop:completed-reflection`, `cor:marked-reflection`,
   `eq:unmarked-structural-block` and the uniform source coefficient
   bounds as arithmetic contracts. This includes their full source
   support, ramified valuations, sectors, branch-dependent conductors,
   local Ramanujan choices and zero extensions. Their derivations from
   theta cusp expansions and Gauss identities are not independently
   certified by the proposed audit.
2. Retain `eq:reflection-cross-prime-phase` and
   `eq:reflection-pair-phase` as the exact phase identities. Check their
   stated application: only residual exponent-one row primes move;
   nonresidual exponent-four primes are frozen. Separate classes of
   residual R and active P modulo the full M_ref^2 are fixed. Fixing
   only their product or smaller reciprocity classes is insufficient.
3. Retain `lem:hybrid-energy`, equation `old-eq:4.6b`, with its exact
   hypotheses: K,N,B,L>=1; squarefree primary k,n,P, unrestricted
   primary b; k,P avoid S, while n,b may contain permitted S primes
   other than lambda. Coefficients satisfy |a(P)|,|beta(n,b)|<=1,
   with a independent of k,n,b and beta independent of k,P. The norm
   contains both masks 1_(P,k)=1 and 1_(P,b)=1 and is bounded by
   (KNBL)^epsilon (K+NB)B{N+L+(NL)^(2/3)}. Fixed restrictions and
   divisor multiplicities must preserve the coefficient independence.
   Its full divisor-reduction proof was read for scope, not audited.
4. Import `lem:reflection-common-profile`, its proof and
   `eq:reflection-common-minkowski` with the stated common-density,
   compact logarithmic-box and polynomial-height hypotheses. Import
   `lem:lattice-kernel-tail` on lambda^(-4) O, A>1. Retain the uniform
   source coefficient bound and crude raw arithmetic counts used to
   discard whole dyads, independently of the eventual kernel order.
   These analytic statements may be cited; no generic Fourier reproof
   is needed. The application to this exact family is the test.

L538 identifies the downstream interface, but its conclusion is not an
input to this audit. L539/L540 inherit the terminal contract and cannot
prove it by backward citation. L535–L537 concern different conditional
edges; their conclusions do not establish this terminal arithmetic.

## Source claims to test, without deriving them this turn

Use the exact `par:reflected-energy-data`. The source defines

\[
 T_d=2H+2A_0+2z_a-N_*-N_0-3B_0,\qquad
 u=\min\{v,z_a,(v+z_a)/3\},
\]
\[
 E_{\rm ref}=O/2+\max(H,v+\ell_b)-S_0-B_0+z_a-u-\ell_b
 -2e_\lambda/3-(T_d-v-3\ell_b-e_\lambda)_+/2.
\]

For actual residual-row and dual annuli it claims fixed-part energy
O(Z^(E_ref-O/2+epsilon)), then O(Z^(E_ref+epsilon)) after summing
the frozen parts and local choices. Retention is
v+3ell_b+e_lambda<=T_d+tau_ref. The formula is not asserted on an
arbitrarily enlarged unseparated row range.

The bounded audit must check these interfaces:

- The original primal collision terms vanish before any symbol is
  divided. Inactive marked primes have their own branch conductors.
  Product-form slot coefficients are needed before extraction; the
  separated hybrid a(P) need not remain product-form.
- The non-slot coefficient extraction treats the N_0 and B_0
  assignments differently. Shared squarefree/cube primes retain their
  full remaining cube powers; do not impose (n,b)=1 or a new S-mask.
- One common profile uses the actual row, dual and individual slot
  norms as coordinates. Its small scalar is extracted before squaring;
  the row range is enlarged only within the separated positive norm.
  Match K=Z^H, N=Z^v, B=Z^ell_b, L=Z^z_a to the retained hybrid
  theorem, including bounded scales, empty slots and fixed sectors.
- Remove whole discarded dyads on the original sums using the complete
  lattice tail before Fourier absolute values. Read the actual support
  constants and order dependence; a retained-length count is not a
  bound for the discarded lattice.
- Sum local branches by rowwise divisor Cauchy and powerful parts by
  their positive outer sum. Check the source's O/2 count exactly once;
  the tuples already summed inside the hybrid norm are not counted again.
- Check `eq:actual-residual-row-dyad` and `eq:common-width-charge`,
  retaining log C_res/log Z and log C_width/log Z. The source's local
  table in 7518–7554 and actual frozen products govern this comparison.
  H=M-O is not an assumption. Uniform adjustable small losses, finite
  seminorms and polynomial-height cost must survive moving labels.

## Overlap, limitations and decision test

Goldmakher–Louvel, *A quadratic large sieve inequality over number
fields*, Math. Proc. Cambridge Philos. Soc. 154 (2013), 193–212,
[arXiv:1112.1642v2](https://arxiv.org/pdf/1112.1642v2), Definition 1,
Theorem 1.1 and Corollary 1.2 (PDF pp. 1–2), were read with all the
family hypotheses. Their squarefree quadratic-family bound alone does
not handle the present unrestricted b and two moving masks. No new
application of that theorem is proved here. The source further cites
Heath-Brown, *Kummer's conjecture for cubic Gauss sums*, Israel J. Math.
120A (2000), 97–124, Theorem 2. The original Oxford PDF returned 403;
only the precise cubic-sieve statement recorded in the pinned source
was read. The future audit retains the hybrid bound, so it does not
depend on silently completing that blocked original-source comparison.

Xu–Sang, *A matching lower bound for the sextic large sieve and
structured prime moments*, [arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2),
definitions (1.1)–(1.2) and Theorem 1.1, concerns the unrestricted
sextic operator norm, not this quadratic–cubic norm. Its proof explicitly
uses family003 unmarked moments; it is not independent verification of
the terminal arithmetic. Its balance obstruction gives no counterexample
to the specified structured terminal estimate. No stronger matching
independent theorem was inspected in the bounded search.

Continue only if the stated contracts imply the exact fixed-part bound
and aggregate charge with all coefficient independences and orders intact.
Narrow or stop on a missing independence, unsupported moving local class,
extra power loss, repeated summation charge or circular uniformity input.
Preserve the source and L538 on failure. Even a successful conditional
audit leaves the named arithmetic contracts, manuscript closure and
actual-Xi positivity open. Mathlib matching coverage was not checked.
