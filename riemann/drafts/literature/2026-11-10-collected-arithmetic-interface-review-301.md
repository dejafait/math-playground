# Collected coefficient bound to arithmetic errors — source comparison completed

TARGET: Review the exact arithmetic meaning and growing-order norm requirements of C999a's full-vector grouping in Ramaré's identity before attempting an error estimate toward L984(H).
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step302 searched Diamond/Steinig/Laguerre sieve, Ramaré asymptotic-sieve uniform order, and Diamond-Steinig convolution error; reused reviews294/296/297/299/300 and stops244/279/296/299. Searches returned the author preprint and already assessed Tao notes, with no inspected complete compensated growing-degree estimate. No novelty inference.
SOURCE_EVIDENCE: O. Ramaré, author preprint28 October2009, https://ramare-olivier.github.io/Maths/V12BombieriSieve.pdf: definition(1), hypotheses(H1)-(H9), Theorems1-2 pp2-6; definitions(8)-(12), Lemma4/(18)-(19) pp7-9; (20), Lemmas19-20 with proofs pp15-17, Lemma24 pp19-20, Section5.1-5.4/(23)-(33) pp20-23, Section6/(34) p24. Exact reading qualifications below.
COMPARISON: The grouped arithmetic factor is the source's mu_(length)*L(full-vector), with raw log-power factors and all j! already in b_n. The source retains product smooth-weight norms, growing divisor-weighted distribution errors and a prime-plus-bilinear observable; it supplies no automatic transfer of C999a's formal decay to L984(H).
GAP: No source-covered exact reconstruction of the complete compensated Laguerre average with controlled grouped signed errors, bilinear removal, sieving complements and uniform growing-order norms has been identified. This is a source-scope limit, not a lower bound or impossibility theorem for those errors.
REASON: Newly inspected Lemmas19-20/24 and (H9)/(34) make the unpaid norm and distribution requirements explicit; park coefficient-only arithmetic payment pending a materially new signed/reconstruction input. A separate audit of the unaudited formal C999a result is independently testable.
LITERATURE_REASON: The changed arithmetic interface requires essential unread smooth-factor, divisor-weight and growing-order distribution contracts outside the ready formal-coefficient assessment; no repetition of the completed root-product calculation is performed.
SCOPE: Completed literature comparison only; no arithmetic identity is newly proved, no estimate specialized at X_n, and no lemma or mathematical script changed. EXPLORE does not approve a dependent arithmetic calculation. New audit nomination is separately assessed in 2026-11-10-collected-root-product-audit-review-302.md and requires next-turn approval.

## Original nomination (step301)

The completed research step301 establishes C999a for precisely the
formal T_n in review297. That proof has full-variable coefficient
recovery and an exponential decay factor, with partition overhead.
Its canonical hypotheses expressly exclude an arithmetic-error
conclusion. It remains unaudited by a later independent critical turn.

The next source review should determine whether an inspected theorem
already supplies an applicable grouped error estimate, what its exact
uniformity in order is, and which unpaid term of L984(H) it could
actually control. Reuse prior coefficient-source readings; do not
reprove the Diamond-Steinig identity or repeat a formal norm test.
Do not assume the source's shorthand identifies formal factors
without checking its exact arithmetic meaning. Full vectors retain
length, but that alone proves no norm estimate or signed cancellation.

Continuation test: nominate a bounded mathematical target only after
the exact factor/error expression and its quantitative requirement
have adequate source coverage. If growth, missing hypotheses or an
inaccessible essential source prevent such a nomination, record the
specific obstruction and park the dependent interface; choose a
materially different independently testable central mechanism.

This step does not nominate a creative proof attempt merely to meet
a scheduling preference. Missing exact arithmetic coverage currently
blocks a justified central creative target. A later nomination must
name its own obstruction, main-goal relevance and decisive bounded
test, with an approved assessment before mathematical work.

Essential continuation artifacts: C999a, review297's full definition,
Ramaré Section2 and the prior formal reviews, L984(H), L981/L982 and
L993. L998, L999, stops296/299, inverse271 and older arithmetic stops
remain evidence in their recorded scopes. No cross-notebook input.

## Completed comparison — step302, 10 November 2026

### Main gap and bounded source test

The main gap is still L030-L032/C032a actual-Xi positivity and
L966/L968 signed forcing. L984(H) asks for an upper bound
a_n<=C_epsilon exp(epsilon n), for every epsilon>0 and every n>=2,
where a_n is the complete mean of P_k(X_n), 2<=k<=n,
X_n=exp(10000(n+1)^4). P_k includes Lambda at every prime power
and subtracts the integral from1 with the exact Laguerre kernel.
L981 pays the later real-cutoff tail; L982 identifies each fixed
index. Neither estimates the retained a_n.

The intermediate target of this turn was source coverage of the
grouped factors and their error norms, not a new error bound.
A favorable comparison could support a later exact, norm-controlled
interface to this a_n. Continue to that mathematics only if its
complete reconstruction and growing-order estimates have an
applicable source contract. Otherwise park automatic payment and
retain the formal result for its separate audit. The latter test
is the outcome here.

### Arithmetic dictionary: what the cited identity actually contains

Read the primary author preprint linked above, version dated
28 October2009; printed page numbers below are PDF page index+1.
Section2/(12)-(16), pp8-9, defines L(ell) as the Dirichlet
convolution of ell_j copies of the arithmetic function m -> (log m)^j.
The source's mu_r is the r-fold Dirichlet convolution of mu.
Its Lambda^(r)(m) means Lambda(m)(log m)^(r-1)/(r-1)!,
not a convolution power of Lambda; see definition(1), p2.

Lemma4, p9, gives the two families with precisely the K_n,H_n,c,w
of review297, and its left side is

    Lambda^(2n) + Lambda^(n) * Lambda^(n).

For the full vector ell the source factor attached to its coefficient
is mu_(|ell|)*L(ell). This identifies the factors already present
in the cited summands, rather than proving a new representation.
Both the first-family length and an ordered pair's total length are
|ell|. Its w and component multinomial factorials are already in
the formal coefficient b_n(ell): L(ell) uses raw log powers, so
inserting another j! normalization would change the expression.
The source's shorthand(18) does not license merging different full
vectors by weight, cancelling mu*1, or changing the length cutoff.
Associativity/collection as an arithmetic-function substitution
would have to be justified in any later application; no new
arithmetic identity or independence claim is established here.

There are two additional issues before this is the desired input.
The left side includes a bilinear term. Moreover its particular
normalized log powers are not the complete Laguerre combination
in L984(H). No inspected source supplies that reconstruction with
its compensator, all orders and full endpoint weights. Coefficient
decay alone is therefore not an arithmetic-error assertion.

### The inspected error and norm contracts

Section1.6/(8)-(10), p7, fixes v=V_sigma(z)/V_sigma0(z),
bar f=f-v f0, and

    r_(d,z)(w,y) = sum_(m<=y/d, (m,P(z))=1) w(m) bar f(dm).

R_z and R_z^0 sum tau_r(d) max_(y<=X)|r_(d,z)(w,y)| over,
respectively, d coprime to the preliminary modulus and d free
of prime factors <=z. The source's coprimality restrictions are
retained; they are not the unrestricted L984 sums.
Section5.1/(23)-(24), p20, compares

    S_1(f,T,ell)=sum_(d<=T, (d,P(z))=1) mu_(|ell|)(d)
                  *sum_(m<=X/d, (m,P(z))=1) L(ell)(m) f(dm)

with v S_1(f0,T,ell). The source bounds the error by
R_z^0(L(ell),bar f,T,|ell|); replacing mu_(|ell|) by tau_(|ell|)
is part of this absolute majorant, not a signed saving.
Equation(19) truncates the convolution power mu_r itself at T;
it does not separately truncate each copy of mu.

The relevant newly inspected norm is (20), p15: for C^1 g on [1,X],
||g||=max(sup|g|, integral_1^X |g'|). For a convolution of k smooth
factors, Section4.2 uses the PRODUCT of their individual norms.
It is not the supremum norm of the convolved arithmetic function.
Section5.1, p21, explicitly records this product for L(ell) as
(log X)^(2n). Thus the coefficient polydisc |Y_j|<=1 in C999a
is not an established unit ball for these arithmetic factors.
No asymptotic comparison at X_n or new weighted coefficient norm
is derived in this literature turn.

Read both cases of Lemma19's partial-summation proof, and Lemma20's
full hyperbola/induction argument, pp16-17: k=1 uses Lemma19;
the k-1 step retains the difference of two remainder values and
changes the divisor index to r+k-1 at the smaller level
X(D/X)^k, 1<=D<=X. Lemma24, pp19-20, combines this with the
sieve comparison of Lemma23. Its conditions include D0/D>=z and
Delta(e+er delta)^(1/delta)<=1/2; its displayed bound retains
R(f,D0,r+k), v R(f0,D0,r+k), the product norm, and the explicit
sigma-versus-sigma0 and sieve-remainder terms. Lemma23's statement
and proof were read for those restrictions. No favorable uniform
distribution remainder is a conclusion of these lemmas.

Theorem1, p4, assumes (H1)-(H5). These include model/dimension
conditions, nonnegative f,f0 in (H3), and, with tau_r the ordinary
divisor function and R defined in(4),

    R(f,D0,2n)+v R(f0,D0,2n) <= A Fhat(X)/log X.       (H4)

Its parameters satisfy X>=e^20, n>=1, D0=X^(1-delta), z=X^delta,
0<delta<=1/(4n), and the preliminary modulus uses primes below z.
Additional displayed conditions are n^2 delta log(1/delta)<=1/6,
2n+1<=delta log X, and 4^(1/delta)Delta<=1/2. The conclusion
compares the sieved combined observable with its model, with scale
Fhat(X)(log X)^(2n-1)v/(2n-1)!, not with L984's compensator.
Theorem2, p5, removes preliminary sieving only under the additional
(H6)-(H8) prime-power, dimension and boundedness assumptions.
Neither theorem is applied here: none of these hypotheses is
verified for a proposed L984 weight/model. In particular (H1),
(H2), (H5) and, for Theorem2, (H6)-(H8) must not be dropped just
because (H4) is the highlighted obstacle.

Read (H9), p6, and its complete Holder/divisor proof in Section6,
p24/(34). Its weaker divisor-index input still requires both
pointwise remainder control C Fhat(X)/d and a level-one weighted
sum <=A' Fhat(X)/(log X)^2; the resulting parameter is

    A = sqrt(C (2 log X)^(4n^2) A').

This is a conditional conversion, not an n-uniform small-error
theorem. Section5.1/(25) retains (37n^2)^n and distribution/model
terms after the source's unmerged estimates; Section5.2-5.4 retains
the separate truncation tail, T^2>=X, and its chosen delta/T
constraints. Read those displayed bounds and the proofs around
(23)-(33); no sharper claim obtained by inserting C999a is imported.
Oscillating weights are discussed on p2 and in Theorem3's application:
the nonnegativity workaround requires controlled domination/linear
combination. It is not a general exemption for growing Laguerre
weights. No theorem about that changed class is claimed.

PDF text for these statements/proofs was inspectable. Screenshot
requests for PDF indices7/15/20 returned no inspectable images,
with index15 reporting a timeout. We do not use a missing image
or infer a disputed norm constant from it. The quoted power in(34),
the norm convention and the theorem hypotheses are legible in the
primary text. No essential source-access blocker remains for this
scoped comparison; an unrelated full-paper audit is not claimed.

### Duplicate check, decision and remaining limits

Reuse reviews294/296/297 for the higher-uniformity, Tao fixed-order,
and unmerged-versus-collected distinctions; do not repeat them as
new evidence. New queries were `"Diamond" "Steinig" "Laguerre"
sieve`, `"Ramaré" "asymptotic sieve" "uniform" order`, and
`"Diamond Steinig" "convolution" error`. The original1970 proof,
generic book mirrors and search snippets are unread leads, not
stronger imported theorems. No exhaustive-search or novelty claim.
Stops244 and279 retain their separate scopes; the old coefficient
stops296/299 do not contradict the later formal C999a bound.

The new decision-changing evidence is the exact smooth-product norm,
the increased divisor index and (H9)'s growing-order conversion,
together with the retained combined observable. These park the
automatic coefficient-decay-to-L984 payment route on the sources
checked. This is an informative source-scope negative, not proof
that every grouped signed estimate fails. Reopening requires an
exact complete reconstruction and a materially new controlled signed
input, not the already completed formal norm test.

C999a itself remains unaudited; its later conceptual audit is an
independent bounded target with reusable source coverage, not another
attempt at the parked arithmetic interface. No justified creative
central attempt is currently nominated: exact signed arithmetic
coverage/reconstruction remains missing, and an essential audit is
still outstanding. Do not relabel the audit creative to fill a quota.

Mathlib: supporting Mahler results remain as recorded in C999a and
review299; full matching coverage of the arithmetic interface and of
the complete C999a statement is unchecked and unknown. No Lean
replay, new lemma, script, numerical evidence, or RH candidate is
part of this turn. PROOF.md and DAG.md need no change because the
mathematical assembly and its established inputs are unchanged.
