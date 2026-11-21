# Source assessment: an analytic symbol for the exact integer-size bump kernel

TARGET: For the original fixed L703 bump, test whether the exact L714 kernel p_n admits an elliptic analytic-symbol expansion on a fixed complex neighborhood of I, after removing exp(n*S(v)) and a fixed power of n, with uniform factorial remainder bounds up to truncation order proportional to n.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 189 searched analytic stationary phase, classical analytic symbols, factorial Stirling remainders, Euler-operator polynomial asymptotics and finite-free strong asymptotics; compared the exact L714 array, audited L715--L716 and five preserved failure records. No matching array theorem was located in this bounded search; no novelty is inferred.
SOURCE_EVIDENCE: Inspected Hitrik--Sjostrand arXiv:1508.00649v1 Section 2.2 equation (2.2.1), pp.32--33, and Section 2.3 Theorems 2.3.1,2.3.3, Lemma 2.3.2 and the deformation/Morse proof, pp.37--40; NIST DLMF 5.11(ii), (5.11.10)--(5.11.11) and its K=1 qualification. Reused existing DLMF (2.10.1) coverage, checking its stated derivative/integrability hypothesis. Precise statements and boundaries below.
COMPARISON: The sources supply all-order local Gaussian remainders and an optimally truncated analytic saddle theorem, unlike merely fixed-order asymptotics. They do not establish a saddle, contour, classical-symbol amplitude or uniform complex-v estimates for this growing array. L715's log limit and L716's nonzero real-interval ratio do not supply these missing hypotheses or the outer signed rate.
GAP: For the unchanged integer-size kernel, test a fixed analytic product domain, admissible saddle contour and uniform separation from poles and competing contributions; then verify the precise S, fixed power, elliptic leading coefficient and factorial estimates. None of these specializations or a singularity-transfer theorem is established here.
REASON: Essential tool comparison is complete for one independently checkable contour/product test on the saved target. The unpaid uniform contour and growing-amplitude estimates are mathematical tasks, not missing source access. EXPLORE is ready for separate continuation approval; this literature turn proves no expansion.
LITERATURE_REASON: The saved REVIEW_REQUIRED target asks for factorial remainders through order proportional to integer size, outside the earlier logarithmic-limit, ratio and Rice/Lindelof assessments; analytic stationary phase supplies new relevant theorem-level comparison.
SCOPE: Exactly TARGET with the original fixed L703 chi, audited L714 (1)--(5) and its coefficient/root inputs, audited L715 F and L716 ratio. Integer sizes n=12q+3 only; no analytic chi, noninteger coefficient continuation, signed lower bound or full-family estimate is assumed.

## Exact proposed test, not an established normalization

Keep U=121/64, A=27/10, d=5/4, u=(3+4i)/10,
alpha=11/8, n=12q+3 and the original fixed I and chi. Define

    ell_D=integral_0^1 [Log(d+u*t)-Log(U*u+d*t)]dt,
    S(v)=ell_D+1+log(U)-d*v/A+F(exp(-u*v/A)),
    p_n(v)=(n*D_n/A)*exp(-n*d*v/A)
                    *sum_(j=0)^(n-1) b_(n,j)*exp(-u*j*v/A)
                                                   /(alpha+u*j/n).

The two logarithms in ell_D use their right-half-plane branches.
F is the audited L715 function on the unit disk. A proposed complex
neighborhood must keep exp(-u*v/A) in that disk. These formulas specify
the target; they assert no relative asymptotic or analytic-symbol result.
The expression for p_n is exactly L714's audited finite inverse.

Concretely, seek a fixed complex power beta, fixed neighborhoods
I subset W' with closure(W') compact in W, analytic coefficients a_k
on W, and constants C,c,epsilon>0 such that a_0 is bounded away
from zero on W' and, for all sufficiently large permitted integer n,

    sup_(v in W') |a_k(v)| <= C^(k+1)*k!,
    sup_(v in W') |n^(-beta)*exp(-n*S(v))*p_n(v)
                            -sum_(k=0)^(m-1) a_k(v)*n^(-k)|
                     <= C^(m+1)*m!*n^(-m),
                                      1<=m<=epsilon*n.

Here n^beta uses the real logarithm of the positive integer n.
No value of beta or a_0 is asserted. These inequalities, if proved,
would provide an exponentially accurate optimally truncated analytic
amplitude. An O(1/n) relative error, convergence of logarithms, or a
bound for each fixed truncation order is insufficient for this target.

## Relevance and bounded decision test

The main gap is actual-Xi mixed positivity; the local bottleneck is the
signed fixed-bump integral K_n=integral chi(v)*p_n(v)dv. A fully
controlled elliptic analytic amplitude might permit an analytic
regularity/singularity theorem to detect chi's support edge without
postulating a particular flattening law. That transfer theorem, phase
geometry, possible same-point cancellation, comparison with the audited
actual residue rate, and all other full-response terms would still need
proof. An amplitude expansion alone is not a signed-rate theorem.

Step 189 below completes the requested source comparison and failure
check, while leaving the nomination's mathematical target unchanged.
In particular the attempt must distinguish a theorem uniform only at
fixed expansion order from the factorial bounds above. This review
does not derive that missing mathematics.
Continue only if a theorem or concrete integer-size contour test has
explicit, independently checkable saddle/separation/remainder hypotheses.
Stop or revise the nomination if it merely relabels the L715--L716 limits,
requires analytic chi, assumes the unknown signed rate, or repeats a
recorded failed contour without a new control mechanism.

Essential mathematical inputs for the eventual test are the original
L703 profile, audited L714 finite kernel, audited L715 F and L716 ratio.
L718 explains the routing change but is unaudited and is not a needed
mathematical premise. L717, L714 (6), and L713's envelope/full-family
claims remain outside the audited inputs. Complementary spatial defect,
amplitude/full charge, H/support and Xi realization remain unresolved.
Full matching Mathlib coverage has not been checked.

## Completed source review — step 189, 3 November 2026

### Local overlap and preserved failures

Read L703's fixed-profile hypotheses; L714's hypotheses, conclusions,
finite rational identity, inverse-density proof and coefficient/Euler
identity; L715's statement and coefficient-profile specialization; and
L716's statement, exact resolvent integral and needed tail-bound scope.
Reused the ready polynomial and resolvent literature assessments rather
than repeating their JKM theorem searches. The JKM input remains
arXiv:2504.11593v1, Definition 1.2 and Theorem 2.2(a),(b),(e), through
audited L715. Its weak zero/logarithmic conclusion is insufficient for
the present expansion. The located 2026 journal version is an unread
bibliographic lead, not an upgraded theorem imported here.

Scoped searches of the signed-bump assessments and associated failure
records found no existing factorial expansion for p_n. Read:

- `ATTEMPTS/2026-11-03-signed-bump-rate-inconclusive.md`: exact finite
  inversion does not pay either resolvent or bump cancellation.
- `ATTEMPTS/2026-11-03-signed-bump-common-phase-stop.md`: the unaudited
  L717 winding evidence stops a constant-rotation lower certificate.
- `ATTEMPTS/2026-11-03-signed-bump-gamma-rice-size-stop.md`: unaudited
  L718 records a noninteger coefficient-domain failure; integer-size
  product analysis does not assume that failed continuation.
- `ATTEMPTS/2026-11-03-spatial-boundary-absolute-contour-stop.md`: the
  L713 horizontal absolute envelope is too large. The new test must
  control the inner kernel relatively, not repeat that outer envelope.
- `ATTEMPTS/2026-11-02-positive-blend-signed-saddle-stop.md`: the
  C681c obstruction concerns different blended weights, which remain
  stopped. No change of masses, bump or mixing is proposed.

These records are routing evidence with their original audit status;
no unaudited result becomes an established input. No zero-free-region,
reciprocal-series or parked arithmetic estimate is being reopened.

### Queries, primary statements and relevant proof cases

Queries included `analytic stationary phase theorem analytic symbol
factorial remainder Sjostrand nondegenerate saddle uniform`, `uniform
asymptotic expansion gamma ratio large parameter remainder factorial
bounds Stirling complex arguments`, `Hitrik Sjostrand analytic microlocal
analysis stationary phase analytic symbols factorial remainder theorem`,
`Deleporte analytic symbol stationary phase factorial Proposition`,
`polynomial Euler operators asymptotic analytic`, `finite free strong
asymptotics polynomials`, and `polynomial binomial product coefficients
varying degree analytic saddle point factorial remainder`. Snippets
were used only for discovery. No exact-array match was found.

1. M. Hitrik and J. Sjostrand, *Two Minicourses on Analytic Microlocal
   Analysis*, [arXiv:1508.00649v1](https://arxiv.org/pdf/1508.00649v1),
   4 August 2015, Section 2.2, (2.2.1), pp.32--33; Section 2.3,
   pp.37--40. Their classical analytic coefficients are holomorphic
   with compact-set bounds C^(k+1)k^k; realization truncates at O(1/h).
   Theorem 2.3.1 treats the unit real d-ball B, amplitude holomorphic
   near {lambda*x: x in B, |lambda|<=1}, all integer orders m and
   0<h<=1. Its Gaussian remainder is bounded by
   C_d*h^(d/2+m)*(m+1)^(d/2)*m!*2^m times the amplitude supremum.
   Lemma 2.3.2 requires a holomorphic phase with nondegenerate critical
   point. Theorem 2.3.3 assumes 0 in V compactly contained in U,
   holomorphic phase/amplitude on U, phase(0)=phase'(0)=0,
   nonsingular Hessian, Re(phase)>=0 on V intersect R^d,
   strict positivity on its boundary, and no other critical point
   there. It gives truncation at 1/(C*h) and an exponentially small
   remainder times sup_U|amplitude|. Read its boundary localization,
   Stokes deformation, quadratic decay, Morse-coordinate reduction
   and final Gaussian case. The Gaussian proof itself is referred
   there to Sjostrand's 1982 Chapter 2, not reproduced in these notes.

   **Applicability boundary:** this is a local fixed-phase theorem,
   not a theorem about our n-dependent product. Its statement does
   not give uniform constants over v in a complex neighborhood.
   Those constants require common domains, derivative bounds and
   separation in this application. A bounded holomorphic sequence
   is not automatically a *classical* analytic symbol. No symbol
   membership for our product, parameter-uniform Morse chart, or
   leading determinant/noncancellation is imported. The Gaussian
   all-order estimate and the general theorem's exponential remainder
   are distinct claims; obtaining the target's every-order remainder
   requires tracking both, including the product's own remainder.

2. **Factor/product tools.** Reuse NIST DLMF version 1.2.8,
   [2.10(i), (2.10.1)](https://dlmf.nist.gov/2.10#E1), already assessed
   in the signed-remainder review. Integer endpoints, positive integer
   order m, required derivatives and integrability of f^(2m) give the
   exact Bernoulli integral remainder, componentwise for complex f.
   Also inspected [5.11(ii), (5.11.10)--(5.11.11)](https://dlmf.nist.gov/5.11#E11):
   for |arg z|<=pi/2, the scaled-gamma K-term remainder is bounded
   by (1+zeta(K))*Gamma(K)/(2*(2*pi)^(K+1)*|z|^K) times
   [1+min(sec(arg z),2*sqrt(K))]; at K=1 only the factor 1+zeta(K)
   is replaced by 4. These explicit remainder tools do not verify the arguments
   or branches of any gamma representation of our array.

   **Applicability boundary:** the integer product can instead use
   Euler--Maclaurin after a legal logarithm and a common complex
   neighborhood in the product parameter have been proved. Its
   remainder must be bounded at orders proportional to n. The old
   O(1/n) Riemann-sum argument in L715 cannot be substituted for this.
   No gamma/Rice continuation in size is needed or authorized by
   citing a gamma remainder estimate. All branch, endpoint correction
   and exponentiation estimates remain for research.

The Numdam landing page for Sjostrand, *Singularites analytiques
microlocales*, Asterisque 95 (1982), and the Deleporte--Hitrik--Sjostrand
analytic Bergman paper were located as references, but their relevant
proofs were not inspected. Neither is an essential unread premise:
the explicit cited Hitrik--Sjostrand statements above are the selected
tools. No Bergman, orthogonal-polynomial or fixed-parameter theorem is
claimed to cover this different array. Full matching Mathlib coverage
is not checked; no absence claim is made.

### One bounded mathematical attempt after separate approval

The exact target, S and factorial inequalities above are unchanged.
Keep the original chi and all finite-family constants. Use L714's
audited inverse contour or finite rational identity as the starting
representation, not a noninteger gamma coefficient. The parameter
for the source theorem would be 1/n; L714's physical h is A/n.

The first discriminating test is to exhibit an admissible integer-size
kernel contour with a holomorphically varying isolated saddle on a
fixed neighborhood of all of I, separated uniformly from poles and
other contributions. Record the contour, logarithm domains, Hessian
bound, complementary phase gap and full-tail bound. A local saddle
equation or numerical picture is not that certificate. Any residues
crossed in a deformation must be retained and compared. If this
representation cannot supply such bounds, preserve the exact failed
condition; inability to prove a condition is inconclusive, not a
counterexample to the target.

If that test succeeds, verify the product amplitude with explicit
Euler--Maclaurin or legal Stirling remainders, fixed complex domains
and all orders through epsilon*n. Identify the critical value with
the nominated S, fix the power beta and prove the leading amplitude
bounded away from zero. Mere agreement of real logarithmic limits
cannot identify its complex phase or its polynomial normalization.
Apply the cited general theorems, justifying the specialization;
do not reprove their general calculus. Combine local and full-contour
errors into the displayed every-order inequality, rather than report
only a formal expansion or optimal-truncation heuristic.

Continue this representation only with these explicit positive
margins or an independently checkable route to them. A rigorous
pole pinch, degenerate saddle, incompatible power/phase, or competing
contribution invalidating a required margin would be informative
negative evidence about the template; refuting the expansion itself
requires more. Stop an inconclusive attempt without repeating it
unless a materially new representation or estimate is available.
Do not assume analytic chi, a flattening law, or signed noncancellation.

Even success proves only an inner analytic-amplitude input. Support-edge
singularity transfer, phase geometry, cancellation at a common image,
actual-residue comparison and complementary response remain unpaid,
as do amplitude/full charge, H/support and Xi realization. This review
does not import or prove a signed rate or a result beyond the checked
literature. No lemma or mathematical script is written in step 189.
