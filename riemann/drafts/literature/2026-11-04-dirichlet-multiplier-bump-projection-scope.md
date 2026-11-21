# Arithmetic-multiplier localization source review

TARGET: Assess primary-source coverage for whether L637's normalized bump has squared projection o(1), uniformly for T<=X<=2T, onto span_C{Z(t)n^(-it):1<=n<=floor(T^(1/10))} in L2(w_XT dt), retaining the full twisted second-moment Gram matrix.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed two primary source chains: Bettin–Chandee–Radziwill twisted second moment and GCD-matrix spectral comparisons via Altinisik–Buyukkose to Lindqvist–Seip; exact projection/localization and coefficient-uniform searches found no inspected theorem settling this bump projection. Queries and reads appear below; no originality inference.
SOURCE_EVIDENCE: Bettin–Chandee–Radziwill arXiv:1411.7764v1, Theorem 1 pp. 1–2, Section 3.1 p. 9 and Section 3.2 Cases 1–3 pp. 12–15, Section 3.3 pp. 15–16; author manuscript dated 2015-01-15 confirms Theorem 1. Lindqvist–Seip Acta Arith. 84 (1998), Section 2 pp. 150–151, Section 3 theorem/proof pp. 152–153; Altinisik–Buyukkose MIA 19 (2016), introductory hypotheses pp. 117–118 and Theorem 2/proof pp. 119–121.
COMPARISON: Known twisted second moments cover this short dictionary's arithmetic norm, after coefficient normalization and smooth-window specialization; they do not state a microscopic projection limit. The checked GCD spectral theorems do not cover its logarithmically weighted form. The remaining finite arithmetic coercivity and bump-correlation comparison are a bounded specialization task, not an imported projection theorem.
GAP: No projection estimate established. A later attempt must retain all arithmetic correlations and logarithmic terms, charge coefficient normalization in the remainder, justify uniform smooth-window conversion, and prove sufficient coercivity relative to the localized numerator. Signed |W|-weighted transfer and Xi mixed signs remain independent gaps.
REASON: Invocation-start REVIEW_REQUIRED coverage is now supplied for a bounded moment specialization. No new lemma or mathematical script is authorized within this literature turn; the newly ready continuation receives separate supervisor approval next turn.
SCOPE: Exact fixed L637 w,u0,psi,g and actual Hardy Z; T<=X<=2T; arbitrary complex T,X-dependent coefficients; n<=floor(T^(1/10)); full weighted Gram. No derivatives, shifts, RH, inverse-zeta division, changed bump, assumed diagonal dominance or assumed lower eigenvalue.
COVERED_TARGET: Test whether L637's normalized bump has squared projection o(1), uniformly for T<=X<=2T, onto span_C{Z(t)n^(-it):1<=n<=floor(T^(1/10))} in L2(w_XT dt), using the full Bettin–Chandee–Radziwill arithmetic moment form and charged coefficient-uniform remainder.

The nomination below is preserved as invocation-start scope. Its statements
that coverage is unassessed describe the earlier nomination; the completed
comparison at the end supplies the present SPECIALIZE decision. The exact
projection question is unchanged. This turn is LITERATURE / EXPLORATION /
NOVELTY_UNCHECKED; source readiness is not mathematical verification.

## Exact object and intended use

Use L637's actual Hardy Z, weight w_XT(t)=w((t-X)/T), center
a=X+u0*T, L=log T and normalized width-1/L bump g_(T,X). Set

    V_(T,X)=span_C{t -> Z(t) exp(-i*t*log n):1<=n<=floor(T^(1/10))}.

Let Pi_(T,X) be the orthogonal projection onto this finite-dimensional
span in L2(w_XT dt). The proposed later mathematical question is whether

    sup_(T<=X<=2T) ||Pi_(T,X)g_(T,X)||_T^2 -> 0.

This definition assumes neither independence of the generators nor an
inverse-Gram bound. If coordinates are used, the exact Gram entries
contain integral w_XT(t) Z(t)^2 (n/m)^(-it) dt; retain the full matrix
and all arithmetic correlations. Coefficients may depend arbitrarily on
T,X. Independent phases, fixed-vector asymptotics or a leading diagonal
are not substitutes for coefficient-uniform control of this projection.

The main gap is actual-Xi all-degree mixed positivity. A rigorous
vanishing projection would exclude this concrete alternative to the
stopped jet dictionary; a failure could motivate study of its localizing
power. Neither result alone supplies approximation, control in the
|W|-weighted norm, a signed main-term margin or an all-height sign.
These remain unresolved and are not assumed.

Essential local inputs for the source comparison are L637's definitions
and L639's qualified obstruction as comparison evidence. L638's
two-atom relative-error scope is a fixed-dimensional comparison only.
No Beurling-diagnostic lemma is a mathematical input to this target.

## Three alternatives considered

1. Further integer-density/coefficient tests are not selected. L736's
   completed local integer-order test supplies no actual-Xi sign input.
   Preserve `ATTEMPTS/2026-11-04-integer-density-coefficient-diagnostic-closed.md`;
   changing a coefficient or power would not be a new mechanism.
2. L727's local-polynomial margin is central but lacks an independent
   estimate for M_Q. Its tail-only stop separates the small exterior
   error from that unpaid sign. No new margin input was identified,
   so another tail audit is unjustified.
3. The selected arithmetic-multiplier dictionary changes the realization
   question from the derivative span stopped by L639. Existing scoped
   assessments explicitly exclude amplifiers. This projection limit
   can be tested before attempting a signed transfer. Selection is
   neither evidence of success nor a claim that no known result covers it.

The scoped duplicate check also located earlier mollified-sign and
joint-law comparisons, concerning sign-set densities or nonlinear law
transfer. They do not supply this projection estimate. The next review
must compare actual theorem hypotheses and any stronger known result.

## Bounded source task and continuation test

Search the exact statement and standard twisted second moments with
short Dirichlet polynomials, localization/Christoffel functions and
weighted Gram coercivity. Use at most three primary source chains,
starting with the closest twisted-second-moment statement. Inspect
coefficient and length assumptions, the applicable proof case and all
load-bearing uniformity conditions; reuse adequate local coverage.
A fixed-coefficient mean, fourth moment alone or different window
does not automatically cover this target. Do not repeat the optional
blocked derivative-paper access route.

Approve a later bounded attempt only if the exact family and essential
analytic inputs are covered. Its decisive mathematical evidence would
be a uniform o(1) projection bound or a rigorous T_k->infinity,
T_k<=X_k<=2T_k sequence with projection squared >=c>0. A loose upper
bound above zero or an ill-conditioned leading matrix is inconclusive.
If a source already settles it, import that result with its necessary
specialization. Persistent essential source blockage parks the target;
no calculation budget is spent by source discovery.

No projection bound or source approval has been derived here. Full
matching Mathlib coverage is unchecked. Immediate routing is
literature_comparison/standard/high. A creative proof nomination is not
yet justified: independent signed control and exact arithmetic-matrix
coverage are missing. Do not label the projection diagnostic creative
merely to satisfy scheduling preferences.

## Completed primary-source comparison — step 259

### Search and duplicate/failure record

Searches on 4 November 2026 used the following exact queries, grouped into
two source chains rather than further proof development:

- `twisted second moment Riemann zeta Dirichlet polynomial arbitrary coefficients length Bettin Chandee Radziwill theorem`
- `Bettin Chandee Radziwill mean square zeta arbitrary Dirichlet polynomial theorem 1 2017 pdf`
- `"twisted second moment" "gcd" coefficients smooth weight theorem`
- `"mean square" "Dirichlet" "Balasubramanian" "1985" coefficients error`
- `Hardy Z Dirichlet polynomial localized bump orthogonal projection Christoffel function`
- `"zeta" "projection" "Dirichlet polynomials" localized`
- `"zeta" "Christoffel" "Dirichlet polynomials"`
- `gcd matrices smallest eigenvalue gcd sqrt mn alpha 1/2 lower bound Hilberdink`
- `"log" "gcd matrix" "zeta" smallest eigenvalue`
- `"Lindqvist" "Seip" "Note on some" pdf`
- `"twisted second moment" "lower bound" "arbitrary" coefficients`

Local comparison read L637's hypotheses and inverse-cost proof, L639's
hypotheses, conclusion and opening Gram analysis, and the relevant primary
input sections of the two November 1 assessments named above. Targeted
searches in those dated assessments and Hardy/jet attempt records found
no matching arithmetic-multiplier projection result. L637's TV envelope
stop and L639's jet-space stop do not settle this dictionary. The November 1
signed short-interval review concerns signed fourth moments and sign mass,
not this projection. No shared or sibling mathematical notebook was read.

### Chain 1: exact twisted-second-moment input

S. Bettin, V. Chandee and M. Radziwill, *The mean square of the product of
the Riemann zeta-function with Dirichlet polynomials*, J. reine angew.
Math. 729 (2017), 51–79, DOI 10.1515/crelle-2014-0133.
Primary versions inspected: [arXiv:1411.7764v1](https://arxiv.org/pdf/1411.7764v1)
(first page dated 1 December 2014), Theorem 1, printed pp. 1–2;
[author manuscript](https://www.math.mcgill.ca/radziwill/BCR.pdf)
(first page dated 15 January 2015), same theorem. Publication metadata
checked at the [publisher](https://doi.org/10.1515/crelle-2014-0133).
This review imports the stated arithmetic theorem; it does not certify
the entire manuscript or reprove its Kloosterman estimates.

Source notation: smooth phi supported in [1,2], N=Y^theta,
A(s)=sum_(n<=N) a_n n^(-s), a_n <<_epsilon n^epsilon, theta<17/33.
For each fixed positive epsilon, Theorem 1 gives

    integral_R |zeta(1/2+it) A(1/2+it)|^2 phi(t/Y) dt
      = sum_(d,e<=N) a_d conjugate(a_e)/[d,e]
          * integral_R [log(t*(d,e)^2/(2*pi*d*e))+2*gamma]
                                      phi(t/Y) dt
        + O_(epsilon,phi)(Y^(3/20+epsilon) N^(33/20)
                           + Y^(1/3+epsilon)).

Here (d,e) is gcd and [d,e] is lcm; gamma is Euler's constant.
The formula includes every pair, not only d=e. There is no RH or
nonvanishing assumption. Source coefficient bounds are part of the
hypotheses, not a license for an arbitrary uncharged constant.

Relevant proof cases actually inspected: Section 3 opening and Lemma 1
(p. 8); Section 3.1 diagonal expression (3.1) (p. 9); Section 3.2's
integration-by-parts truncation (pp. 9–10), zero-frequency residue and
combination with (3.1) (Case 1, pp. 12–14), high-frequency integrations
by parts (Case 2, p. 14), Mellin separation of phi and coefficient norms
in Proposition 1/(3.7) (Case 3, p. 15); Section 3.3 closing bound
(pp. 15–16). These cases support using bounded coefficient families and
bounded smooth-weight seminorms. The source's complete logarithm and
constant term must be kept when testing a smallest eigenvalue. An
entrywise asymptotic alone is not the required quadratic-form estimate.

For the later application, L637's Z is real and has Z(t)^2 equal to
|zeta(1/2+it)|^2 on the real axis. A multiplier sum c_n n^(-it)
corresponds to source coefficients a_n=sqrt(n)*c_n. To meet the source
coefficient hypothesis, normalize the nonzero finite vector by
B=max_(n<=N)|sqrt(n)c_n| before invoking the theorem, then restore its
quadratic scale B^2 in both sides and the error. The zero vector is
separate and trivial. This explains applicability only: this review
does not prove a coefficient-norm remainder or projection bound.
Using the theorem with unnormalized arbitrary a_n is prohibited.

The source's fixed [Y,2Y] support also needs an explicit conversion:
w_XT is supported in [T,3T]. A later specialization must use finitely
many overlapping dyadic smooth windows and the compact family X/T in
[1,2], retaining their bounded derivative/Mellin seminorms. Section 3.2's
weight dependence is through those operations, not a chosen microscopic
window. All physical windows remain of size comparable to T. No source
result at a width 1/log T is asserted. The microscopic function occurs
only in the numerator of the projection. The length floor(T^(1/10)) is
strictly inside the source range at each comparable dyadic scale; padding
with zero coefficients is allowed. Uniformity and normalization costs
must still be written in a later mathematical proof.

The paper recalls Balasubramanian–Conrey–Heath-Brown's theta<1/2 result;
that original paper was not independently read. It is an unread older
lead, not an extra premise. No longer-length, shifted, special-shape or
conjectural theorem from BCR is used. A fourth-moment theorem would not
replace the norm lower bound required here.

### Chain 2: GCD-matrix bounds and their scope

E. Altinisik and S. Buyukkose, *On bounds for the smallest and the
largest eigenvalues of GCD and LCM matrices*, Math. Inequal. Appl. 19
(2016), 117–125, [DOI 10.7153/mia-19-09 / primary PDF](https://files.ele-math.com/articles/mia-19-09.pdf).
Read introductory matrix definitions pp. 117–118 and Theorem 2 with
its proof pp. 119–121. It concerns the unweighted matrix ((i,j)) on
{1,...,n}; it is not the logarithmic BCR form. No eigenvalue estimate
from this paper is imported, and no correctness audit of that theorem
was undertaken. Its references led to the following closer comparison.

P. Lindqvist and K. Seip, *Note on some greatest common divisor
matrices*, Acta Arith. 84 (1998), 149–154,
[primary article PDF mirror](https://pdfs.semanticscholar.org/1f99/1c42c18d79424f6d631055510f36b1f66cfc.pdf).
Read Section 2 pp. 150–151 and Section 3 theorem/proof pp. 152–153.
For M_s=((gcd(m,n))^(2s)/(mn)^s), the sharp uniform positive lower
spectral bound in that theorem assumes s>1. For 1/2<s<=1 its smallest
eigenvalue has liminf zero. Section 2 explicitly excludes s<=1/2 from
its L2 norm representation. The gcd/sqrt(mn) kernel suggested by BCR
would sit at s=1/2, and BCR additionally has a logarithmic factor.
Thus neither the uniform s>1 bound nor that norm representation can
be imported at the required endpoint. This does not prove failure of
the projection target, or exclude a sufficiently weak finite-N bound.
The proof's Riesz-basis input is not imported here.

The guessed publisher-host PDF returned 403; the full article was
accessible at the mirror above. A shell download of BCR failed DNS,
but both primary BCR versions and the complete relevant cases were
read through the web tool. No essential source blocker remains. No
bulk PDF/text file was obtained or fabricated.

### What is ready, and what remains a mathematical question

SPECIALIZE approves only the COVERED_TARGET after the supervisor's
separate continuation approval. The known result supplies the arithmetic
moment comparison. The unproved difference is sufficient quantitative
coercivity of its full logarithmic form, with its error charged after
normalization, and comparison to the actual width-1/log T bump pairings.
This is a routine moment/projection specialization in purpose, not a
new creative sign mechanism. The weak finite-size estimate needed may
be investigated with elementary divisor identities or the complete
moment form; no positive bound is assumed or claimed here. No arithmetic
moment theorem needs to be reproved. If a new essential external theorem
is needed outside this scope, stop dependent mathematics for its review.

Continue this bounded attempt only if it produces a uniform o(1)
projection bound, or a rigorous sequence with projection squared >=c>0.
Failure of a chosen lower-bound estimate, positive entries, numerical
conditioning, or an upper bound staying above zero is inconclusive.
Record the exact unpaid inequality and stop that calculation mechanism
if it cannot pay the projection ratio; do not silently reduce N, change
w or replace the space. No actual-Xi mixed positivity, signed margin,
|W|-weighted realization or RH candidate follows from either outcome.
Full matching Mathlib coverage remains unchecked; generic finite
Hilbert-space projection machinery is not the analytic result sought.

No new lemma, mathematical proof or mathematical script was written in
this literature step. The main argument and DAG therefore do not change.
