# Fixed real source-prime witness — source review1410

Completed review, 18 November 2026. This is a literature-only review of
nomination1409's unchanged (N1), not a calculation or a witness bound.
The assessment replaces nomination1409's review fields; its (N1),
witness, threshold and convention at zero denominator are unchanged.

Ready1402 and source-notes1394 were read and reused. Local targeted reads
covered C019u's exact finite F/E source decomposition, C019r's weight
and hypotheses, C019x's heat/floor setup, C019t's stated qualified
transfer, and stops1405/1407/1408. No full audit of those other proofs
is claimed. The existing diagonal stop is not a full signed norm bound.

Primary sources reached through web access: Soundararajan0708.3990v2,
Section2/(2)-(4), pp4-5; Bettin--Chandee--Radziwill1411.7764v1,
Theorem1 pp1-2 and Section3.1/3.2 openings; Montgomery--Vaughan's
author-hosted Multiplicative Number Theory II draft, G.14/G.16,
printed pp422,426-427 (PDF pp434,438-439). The recent signed-Hardy
resonance lead Hossain--Mahatab--Vatwani2610.36885v1 was pending in
the initial working save; its source comparison is now completed below.

No missing source is being assumed. Shell download failed because the
network host could not resolve; web access supplies the primary texts.
No lemma, mathematical script, canonical argument or DAG edit occurred.

## Search and reuse record

Actual search queries included:

- `Soundararajan extreme values zeta L functions resonance method M1 M2 Theorem 2008 short Dirichlet polynomial`
- `twisted second moment zeta arbitrary coefficients Dirichlet polynomial shifts theorem Bettin Chandee Radziwill`
- `mixed moments Hardy Z shifted product Dirichlet polynomial resonance method`
- `Montgomery Vaughan Hilbert inequality delta mean value Dirichlet polynomials theorem PDF`
- `"zeta" "heat" "mollified" "moment"`
- `"resonance" "Hardy" "shifted" "Dirichlet polynomial"`
- `"Dirichlet polynomials" "variable coefficients" "mean value"`
- `"zeta" "mixed moment" "restricted primes"`
- `"Large values of Hardy" "Selberg class"`
- `Hossain Mahatab "Hardy" "Selberg" arxiv`

These are a bounded search, not an exhaustive bibliography or evidence
of novelty. Discovery summaries were used only to locate primary
texts; their mathematical claims are not inputs. In particular, the
recent Hardy paper was read directly on arXiv after locating its ID.

The ready1402 exclusions for BBLR's ordinary shifted fourth moment,
Bui--Hall's mu-specific double-zero taper, Baluyot's different taper,
Gonek--Ivic's ordinary paired second moment, and the parked unread
Selberg proof are reused without reopening them. Ready1402's inspected
Koesters Appendix A.1-A.3 first/second derivative and integer-sum tools
remain available with their exact hypotheses. They are not general
rational-twist orthogonality theorems. Targeted local searches in those
notes, the Jensen stops and history1409 found no completed matching
fixed-witness evaluation. This does not assert absence elsewhere.

## Primary theorem comparisons

Source height is written S here to avoid confusing it with notebook T.

**Soundararajan**, [*Extreme values of zeta and L-functions*,
arXiv:0708.3990v2](https://arxiv.org/html/0708.3990v2), 4 April 2008,
Section2, (2)-(4), PDF pp4-5. Read the moment definitions, Fourier
decay proof and both equal/unequal-product cases through (4), and
Theorem2.1's statement. For fixed smooth nonnegative Phi supported
in [1,2], equal to one on [5/4,7/4], and
R(y)=sum_(n<=N) r(n)n^(-iy), N<=S^(1-epsilon), (2) evaluates the
ordinary resonator norm and (3) the ordinary zeta mixed moment.
The latter is

\[
 S\widehat\Phi(0)\sum_{mk=n\le N}
       \frac{r(m)\overline{r(n)}}{\sqrt{k}}
 +O\!\left(S^{1/2}\sum_{n\le N}|r(n)|^2\right).
\]

Theorem2.1 optimizes over r; it is not a lower bound for every fixed
choice. Our signed witness is prescribed, has moving heat amplitudes
and W, and is paired with actual Jensen values. Neither (3) nor the
optimization evaluates its correlation or denominator. The Fourier
separation step needs verification for the actual frequency set;
an isolated diagonal cannot substitute for it. No specialization or
new proof of this source result is claimed.

**Bettin--Chandee--Radziwill**, [*The mean square of the product of the
Riemann zeta function with Dirichlet polynomials*,
arXiv:1411.7764v1](https://arxiv.org/html/1411.7764v1), PDF dated
28 November 2014. The generated HTML carries a different display date;
the cited version is identified by the PDF header. Read (1.1),
Theorem1 pp1-2, and Section3's approximate-functional-equation setup,
(3.1), and the opening unequal-product cases (3.2)-(3.3), pp8-9.
For ordinary |zeta(1/2+iy)A(1/2+iy)|^2, fixed smooth phi supported
in [1,2], coefficients a_n<<_epsilon n^epsilon and length
N=S^vartheta, vartheta<17/33, Theorem1 gives the gcd/lcm main form
with error O_epsilon(S^(3/20+epsilon)N^(33/20)+S^(1/3+epsilon)).
The proof explicitly combines diagonal and off-diagonal contributions
in that main term. Arbitrary fixed coefficients therefore do not
license dropping unequal products. This is an unshifted ordinary
second-moment theorem, not the moving-heat, two-point, signed (N1).
No mixed polarization, heat comparison or direct import is performed.

**Montgomery--Vaughan**, [*Multiplicative Number Theory II: Primes and
Sieves*, author-hosted draft](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf),
472 PDF pages, accessed 18 November 2026; version date not identified.
Read G.14, the ordered-frequency definition (G.25)-(G.26), and
G.16/(G.27)-(G.28), printed pp422,426-427. For distinct real lambda_n,
delta_n=min_(m!=n)|lambda_m-lambda_n|, G.16 states

\[
 \left|\sum_{m\ne n}\frac{x_m y_n}{\lambda_m-\lambda_n}\right|
 \le\frac{3\pi}{2}
 \left(\sum_n\frac{|x_n|^2}{\delta_n}\right)^{1/2}
 \left(\sum_n\frac{|y_n|^2}{\delta_n}\right)^{1/2}.
\]

G.14 uses a common positive separation and constant pi/delta.
These are available finite-frequency tools, not an evaluation of
(N1). Equal frequencies must be grouped before their use. The
actual rational frequencies, time-dependent amplitudes, cutoffs and
variation must still be handled; no numerical separation bound or
Gram coercivity for this witness is asserted. We did not audit the
proof or infer a specialized time-norm lower bound from these statements.

**Hossain--Mahatab--Vatwani**, [*Large values of Hardy's Function from
the Selberg class*, arXiv:2610.36885v1](https://arxiv.org/html/2610.36885v1),
27 October 2026. Read Theorem1.2, Section2.3's resonator definition,
Lemma2.10's statement and positive equal-product reduction,
Proposition2.12 with its proof, and Lemma3.2/(3.3)-(3.6) with its
full cutoff and second-derivative proof. Theorem1.2 concerns ordinary
degree-one Selberg-class functions and separate positive/negative
maxima. Proposition2.12 assumes both a large F-weighted resonator
moment and a negligible signed Hardy moment; these are hypotheses,
not automatic positivity. Lemma3.2 uses N=floor(S^(1/4)), fixed
primitive character and fixed smooth Phi; its proof retains the
moving entry endpoint and pays amplitude variation. Lemma2.10
chooses r(n)=a_F(n)f(n) with its prescribed nonnegative squarefree f.
Our fixed real witness is not that resonator. No theorem here pays
its shifted signed correlation, W, heat amplitudes or actual-P error.
The general degree-two case and other cited results are not imported
or reviewed as premises. No source proof is being independently certified.

## Coverage decision and limits

EXPLORE is justified for exactly nomination1409's fixed (N1).
Standard L2 Cauchy--Schwarz duality supplies the intended framework;
ready1402's finite oscillatory-integral tools supply a direct approach.
The primary comparisons above identify what those tools do and do
not establish. There is no essential inaccessible theorem being used.
The novelty status is unchecked: the search found no full matching
evaluation, which does not establish originality.

Any future finite expansion must keep conjugate and nonconjugate
channels in both integrals, their complement correlations, exact
rational twists and equal-frequency grouping, all four original
linear tapers in W, source entry domains, and each own heat time.
Ordinary positive |R|^2 resonance and unrestricted optimization do
not apply by naming this a witness. Orthogonal-projection or diagonal
dominance claims would need proofs. The numerator's sign is not supplied
by the nonnegative denominator. This is a list of unpaid hypotheses,
not a newly derived expansion, cancellation or obstruction.

C019x's already audited source-prime cutoff facts can be reused.
Its diagonal weight is from H^2, while the proposed integrals retain
W and its rational twists; no identity transfers its growth to (N1).
C019t is still an unaudited claimed L2 pair transfer. A future use
must preserve C019j/k/l/s,L320 and L018/L021 contracts, and explicitly
justify its application to this witness, including zero-denominator
cases. No witness transfer or normalization estimate is proved here.

Continue only toward a rigorous cBq^2 lower bound or a rigorous O(B)
bound for this fixed quotient. A weaker upper envelope or a missed
lower threshold is inconclusive. Preserve the first unpaid signed
term if neither test closes; repeating requires a materially new input
or refined mechanism. Do not optimize or change the witness within
this coverage. The full M2, subsequent sign density, ordered root
selection, reciprocal mapping and bulk separation remain open.

No Mathlib matching theorem was checked; supporting L2 inequalities
would not formalize this quotient evaluation. No new result, lemma,
mathematical script or RH candidate is produced. Newly completed
coverage must receive the supervisor's separate approval before the
creative mathematical attempt, with the target text unchanged.

## Recovery1411 — direct URLs in the assessment

The supervisor rejected the ready assessment for lacking a direct source
URL in that file. Its SOURCE_EVIDENCE now contains the four direct links
already recorded above. All resolved on 18 November 2026; targeted web
retrieval confirmed Soundararajan Theorem2.1, BCR Theorem1, G.16/(G.27),
and Hossain--Mahatab--Vatwani Proposition2.12 and Lemma3.2 locations.
No changed hypothesis or newly relevant theorem required repeating the
prior search or proof-case review. This fixes traceability only: the
existing EXPLORE scope and every unpaid signed term remain unchanged.
No new mathematics, source-proof certification or novelty claim follows.
