# Primitive-source-ratio kernel — source comparison1418

18 November 2026. Literature only; no grouped identity, arithmetic estimate,
endpoint payment or new lemma is established here. The exact target remains
the TARGET of assessment1417. This completes its previously missing bounded
comparison, changing REVIEW_REQUIRED to EXPLORE, not IMPORT or SPECIALIZE.

## Local scope and duplicate check

Read C020c in full, C019 through its complete channel definitions (8),
C019y's hypotheses and complete decomposition (1),(3)-(6), and the relevant
BCR discussion in source-notes1410. Read stop1416 and stop1417 and history1417;
searched the named Jensen assessments/stops for primitive-ratio,
prime-residue, modulus and Kloosterman coverage. No earlier completed
assessment for this grouping was found in those paths. This bounded check
does not establish novelty. Ready1409's oscillatory tools and ordinary-moment
exclusions remain usable without another review of those same inputs.

The exact observable is C020c (2), including (7),(8), not an ordinary zeta
second moment. Its center phase is exp(-2*pi*i*m*v*r/(n*s)); its original
index bounds are m,n<=N*, r,s<=R, v=p*b, with both witness primes in
[sqrt(X)/10,sqrt(X)/5]. The raw denominator n*s is at most N*R.
The reduced denominators and their multiplicities have not been worked out.
Reducing only m/n does not authorize assuming coprimality with r,s,p,b.
The heat factors, cos(tau), g_r*g_s, the two source-dependent intervals,
both Fresnel integrals, boundary correction and remote endpoints are part
of the observable, not errors already covered by a theorem below.

## Search record

Queries used:

- `primes bilinear exponential sums rational fractions prime products growing moduli Bombieri Vinogradov additive characters theorem`
- `Bettin Chandee trilinear forms Kloosterman fractions theorem 2015`

These located the primary sources below. Search snippets and secondary
descriptions were used only to locate sources. Versioned primary HTML
statements and the specified proof passages were then read. No inaccessible
essential source remains for this bounded comparison. The search was not
an exhaustive survey of exponential-sum literature.

## Inspected primary statements and proof cases

**Bettin–Chandee–Radziwill**, *The mean square of the product of the
Riemann zeta function with Dirichlet Polynomials*,
[arXiv:1411.7764v1, Section 3.2](https://arxiv.org/html/1411.7764v1#S3.SS2).
Reuse Theorem 1's statement from source-notes1410. Newly read: gcd extraction
after (3.5), progression Poisson summation, and all three subsequent cases
through (3.7). Their determinant equation gives a progression after gcd
extraction. Poisson produces e(-j*Delta*inverse(n1)/n2), for coprime n1,n2.
The j=0 contribution is combined with the diagonal; it is not discarded.
Large |j| uses smooth integration by parts. Small nonzero j uses Mellin
separation and the trilinear estimate. Thus their arithmetic bound follows
a particular transformation and weight separation. C020c's product phase
has no modular inverse in its present form. No such transformation with
its clipped intervals has been supplied; Theorem 1 does not itself evaluate
this mixed observable. Source symbols j,Delta,n1,n2 here are not C020c's
shift or indices. This is a method comparison, not a replay of their proof.

**Bettin–Chandee**, *Trilinear forms with Kloosterman fractions*,
[arXiv:1502.00769v1, Theorem 1, (1.2), Remark 1/(1.3), Sections 6–7](https://arxiv.org/html/1502.00769v1).
For arbitrary separate sequences supported on [M/2,M], [N/2,N], [A/2,A],
and a nonzero integer vartheta, their coprime sum
sum alpha_m beta_n nu_a e(vartheta*a*inverse(m)/n) is bounded by

\[
 \|\alpha\|_2\|\beta\|_2\|\nu\|_2
 (1+|\vartheta|A/(MN))^{1/2}
 \bigl((AMN)^{7/20+\epsilon}(M+N)^{1/4}
       +(AMN)^{3/8+\epsilon}(AN+AM)^{1/8}\bigr),
\]

for each epsilon>0. Remark 1 permits C1 phase perturbations satisfying
(1.3), with its additional size cost; it is not an arbitrary joint-weight
theorem. Sections 6–7 remove squarefree restrictions and treat both size
orders, using reciprocity and its smooth extra phase. Neither step removes
the sum's coprimality condition. Prime-supported separate sequences are
allowed, but separability, the inverse phase and the actual norm/parameter
budget must first be demonstrated locally. These missing applicability
steps prevent an import. No bound from this source has been applied here.

**Bazin**, *A Bombieri–Vinogradov theorem for exponential sums over
products of k primes*,
[arXiv:2607.15137v1, Theorem 2/(3), Section 2 Lemma 6/(9)–(11)](https://arxiv.org/html/2607.15137v1).
For epsilon,C>0, some b(C) gives the following for
Q<=z^(1/3)(log z)^(-b), theta<=Q^(-3)(log z)^(-b),
1<=k<=(2-epsilon)log log z. With f_k=1_{Omega(n)=k},

\[
 \sum_{u\le Q}\max_{(a,u)=1}\max_{|\lambda|\le\theta}
 \left|\sum_{n\le z}f_k(n)e((a/u+\lambda)n)
 -\frac1{\varphi(u)}\sum_{st=u}\mu(s)t
       \sum_{\substack{n\le z\\t\mid n}}f_k(n)e(\lambda n)\right|
 \ll_{\epsilon,C} z(\log z)^{-C}.
\]

Lemma 6's inspected proof separates every gcd residue stratum through
induced characters and Gauss sums; the displayed divisibility main terms
are retained. This is an averaged modulus statement for f_k, not arbitrary
coefficients on balanced distinct prime pairs. The witness's separate
prime windows, heat amplitudes and endpoint weights are not supplied by
f_2. An applicability argument must also compare actual reduced moduli
with Q, and pay repeated outer weights. No claim that these hypotheses
hold, or that every modulus necessarily violates them, is made here.

**Wright**, *Trilinear Kloosterman fractions I: partially fixed moduli
and unbalanced convolutions*,
[arXiv:2604.25177v1, Definition 1, Theorem 2.1, Corollary 2.2, Section 3 opening](https://arxiv.org/html/2604.25177v1).
Inspected the fixed-factor inverse-phase statement with (m,n*R0)=1,
M<<N^2 and polynomially bounded R0; R0 is not the notebook's R.
Corollary 2.2 requires divisor-bounded separate sequences, one satisfying
the stated Siegel–Walfisz condition, and one of its three size ranges.
Section 3 explicitly retains coprimality and square-full/squarefree
strata. This recent refinement is not a theorem for arbitrary product
phases or arbitrary endpoint weights. Its hypotheses have not been
verified for this target, and no specialization or complete proof audit
is claimed. It is a nonimported lead if an appropriate transformed form
is actually obtained, not essential unread coverage blocking that test.

## Result of comparison and bounded mathematical handoff

The sources provide useful arithmetic tools, not the desired full signed
main form. Source access succeeded. The missing object is a local exact
grouping and a quantitative applicability argument, not an asserted
unknown theorem that must be assumed before trying the grouping. EXPLORE
therefore permits one bounded attempt on the unchanged target. It does
not preapprove any use of a source outside its displayed hypotheses.

The attempt should preserve every tuple while grouping primitive source
ratios, then expose the reduced moduli, all common-factor cases and the
joint weights. An inverse-phase method is available only if a valid
transformation produces that phase and pays its zero modes and other
terms. A direct additive-character method must instead retain its gcd
main terms and show that its actual prime weights, modulus range and
outer summation are covered. In either implementation the entire
Fresnel/boundary/remote expression remains present. No inference from
one positive subfamily, a raw modulus upper bound, or a failed absolute
budget is licensed. Stop1416 and stop1417 keep exactly their old scopes.

Continue that implementation only with an explicit complete signed main
form and total remainder o(Bq^2), or a concrete source-compatible reduction
with a quantified remaining term that this one attempt can discriminate.
If the first needed transformation, weight separation or endpoint payment
cannot be justified, record its exact residual and abandon that
implementation; absence of a matching citation is not a theorem that the
signed sum is large or the whole route impossible. A different target or
source outside this assessed scope requires its own assessment. No source
reproof is justified merely to repeat a quoted theorem.

C020c (2),(7)–(13), C019 (8),(13),(14) and C019y (1),(5) remain essential
unaudited local inputs. The full denominator, O(G,J), UA, E_P and any
actual-P transfer remain independent unpaid steps. A successful mixed
evaluation could inform the fixed-quotient cBq^2 versus O(B) test; it
would not settle actual-Xi all-degree positivity. No mathematical advance
beyond the inspected sources or RH candidate is claimed. Full matching
Mathlib coverage was not checked; no formal-library absence is inferred.
