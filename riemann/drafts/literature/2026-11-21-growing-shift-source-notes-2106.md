# Growing-shift signed energy: source comparison2106

This completes review2105's exact target. Literature only: no theorem
application, new arithmetic bound, lemma or mathematical script.
Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: C034u's **full** square, at
O_(h,epsilon)(X^(1/2+epsilon)) for every fixed epsilon>0 and all
sufficiently large real X. Such an input would improve arithmetic
energy control; subpower/cumulative control and mixed signs would remain.

## Local object and existing stronger envelope

Read C034r's hypotheses, conclusions and operator/Fourier setup and
C034u's hypotheses, conclusion and complete square expansion/reduction
in section1. Their definitions of h,E,Phi,U_X,C_h are unchanged.
All n,k in (X/2,X] must be retained, with mu(n)mu(k), the factors
X^(-1/2)(nk)^(-1/4)log(X/n)log(X/k), and C_h(log(k/n)).
The result is the squared norm by C034u section1, not a new identity.
Individual primitive sectors need not be positive.

Reused source-notes2096/2101 and their direct-import stops. Audited
C034x/stop2103 excludes the arbitrary-factor replacement, not actual
Möbius cancellation. No repeat of its all-one experiment is proposed.
Read C034v section5/(23)-(26) and C034w's full source Fourier formula.
In fact C034v(26) already gives the stronger-than-unsigned envelope

    ||U_X||_(E->E) <= C sqrt(X) exp(-c_mu f_0(log X)),
    f_0(L)=L^(3/5)(log L)^(-1/5),

uniformly eventually in real X. This is an existing canonical result,
not an inference proved here. Another fixed-log saving would be a
weakening of this available bound, not a useful new energy lemma.
None of these envelopes has the requested fixed power exponent.

## Primary growing-shift theorem and relevant proof cases

K. Matomäki, M. Radziwiłł and T. Tao, *An averaged form of Chowla's
conjecture*, Algebra & Number Theory9(9)(2015),2167-2196,
[publisher version, DOI10.2140/ant.2015.9.2167](https://msp.org/ant/2015/9-9/ant-v9-n9-p04-p.pdf).
Read Theorems1.1/1.2/1.6, definitions of M, the Möbius extension after
(1-12), Section5's H<=H0 and H>H0 cases, (5-3)/(5-4), Remark5.2,
and Proposition5.3 including its entire proof; pp2168-2173,2184-2186.
For integer k>=1 and 10<=H<=Z, Theorem1.1(1-3), with the explicit
Möbius extension on p2173, states

    sum_(1<=h_2,...,h_k<=H)
      |sum_(1<=n<=Z) mu(n)prod_(j=2)^k mu(n+h_j)|
    <<_k [loglog H/log H + (log Z)^(-1/3000)] H^(k-1)Z.

Theorem1.6 permits bounded other factors but retains its pretentious
distance term and affine-parameter restrictions. Section5 restores
the omitted typical-factorization complement at cost (5-4).
Remark5.2's exceptional-tuple power saving keeps H<=H0 and a weak
individual bound O(k A^2 delta Z); it is not power cancellation in Z.
The two H cases do not remove this tradeoff. No general theorem proof
or effective constant is independently audited or imported here.

## Almost-all intervals: the logarithmic phase is covered

K. Matomäki, M. Radziwiłł, X. Shao, T. Tao and J. Teräväinen,
*Higher uniformity of arithmetic functions in short intervals II.
Almost all intervals*, [arXiv:2411.05770v2](https://arxiv.org/html/2411.05770v2),
23January2026. Read Theorem1.1(i),(iv), Corollary1.2(i), Theorem3.1,
Lemma3.2 and the Möbius-relevant small/large-|T| cases in §§3.4-3.5,
including the unweighted/prime-weighted distinction.
In Theorem3.1(i), Z>=3, Z^(1/3+eta)<=H<=Z, eta>0 small and fixed,
|T|<=Z^C, C>0 fixed: the maximal-progression Möbius sum

    |sum_(x<n<=x+H) mu(n)n^(-iT)|* <= H(log Z)^(-A)

outside a real-start set of measure O_(A,eta,C)(Z(log Z)^(-A)),
for each fixed A>0. Thus the actual logarithmic phase has direct
coverage. Small T uses bounded phase variation and mean squares;
large T still chooses W=log^(100A)Z for Möbius, unlike divisor sums.
Part(ii) adds a prime-divisibility weight and cannot replace mu itself.
Theorem1.1(iv)'s shorter range gives eta_0 H for fixed eta_0>0,
not a power remainder. Later nilsequence proof machinery is unread;
none is needed to reject these quantitative direct imports.

## Newer global-shift lead checked at its exact scope

Jizhou Guo, *Logarithmic Chowla Correlations Across All Shift Scales*,
[arXiv:2608.23500v4](https://arxiv.org/html/2608.23500v4),
1September2026. Read Theorem1.1, Corollary1.2, Theorems1.3/1.5/1.6,
and complete Lemmas11.4-11.5/Thm1.6 proofs. This is a manuscript,
not an independently verified theorem input. Its global theorem
concerns lambda(n)lambda(n+h)/n, with a fixed power-log saving and
one sparse exceptional set; the threshold may be ineffective.
Thm1.6: fixed theta>1/3, 1<p<infinity, integer H>=x^theta, L>=0,
|b|<=1: the normalized shift-window p-moment of
sup_(y<=x)|sum_(n<=y)lambda(n)b(n+h)/n| is O_(p,theta)(1).
Its high-prefix tail is only log^(-A)x. The proof keeps bad and
boundary blocks; Lemma11.4 explicitly converts fixed integer-length
real-start exceptions and uses square-divisor transfer. This does not
convert every moving real-X weighted window. The global theorem's
other analytic inputs are unread; no Möbius specialization or GRH
clause is imported. Statement-level scope already prevents direct use.

## Weight, exceptional-set and threshold comparison

The first source does address growing additive shifts, so the earlier
fixed-form limitation is no longer the only comparison. Nevertheless,
its remainder is logarithmic. Summing fixed-shift little-o estimates
uniformly was never justified and is not used here. The improved
exceptional-shift counts do not simultaneously supply the required
power for individual ordinary correlations. Neither the fixed delta
nor the fixed logarithmic exponent may vary with Z without new bounds.

C034u also requires a ratio weight depending jointly on n,k and a
moving common window. Merely setting k=n+h in a theorem for unweighted
prefixes does not pay this variation and both endpoints. A legitimate
weighted use would require uniform partial-sum control and bounded
variation losses for the actual C_h/logarithmic factors, with all
positive/negative shifts and the diagonal accounted for. No such
application is claimed. Even granting a bounded weight-transfer cost
would not turn the displayed logarithmic remainders into the proposed
fixed power; this is a comparison of theorem strengths, not a new upper.

The second source controls a measure of bad real starts, with constants
uniform for a **fixed** allowed T. One prescribed real start can still
be bad. Passing to all |T|<=4log X would also need an integral/Fubini
or discretization argument; a common exceptional set is not asserted
by Thm3.1. The source's stronger nilsequence suprema cover polynomial
phases but do not silently make n^(-iT) a polynomial phase.
Guo's integer-start argument is real evidence that endpoint conversion
can sometimes be paid; it is not evidence for this moving weighted
window or for a power bound. These qualifications do not prove that
every possible averaged argument fails.

Park these **direct imports**. There is no source-access blocker.
The full signed target, all primitive upper sectors, subpower and
cumulative estimates, completed-vector transfer at improved strength,
and actual-Xi mixed signs remain open. No RH candidate is produced.
Full matching Mathlib coverage of this weighted arithmetic energy was
not checked; unknown availability is not absence.

## Searches, outcome and bounded continuation

Queries: `Matomaki Radziwill Tao averaged form Chowla conjecture theorem
1.1 H X log log H log H`; `Higher uniformity arithmetic functions short
intervals II almost all intervals theorem Mobius exceptional set`;
`Mobius correlations growing shifts power saving average square root
2026 theorem`; `Mobius short interval variance power saving mean square
X H theorem correlations`; exact Guo title. Followed primary statements
before proof cases. Secondary summaries/GitHub/rStation hits were
locators only. *Averages of the Möbius Function on Shifted Primes* and
references in Guo remain unread leads, not premises. No novelty claim.

Local duplicate searches were confined to C034 and November21
signed/gamma assessments and stops, plus nomination2078. The source
screen changes the decision: the almost-all sequel is no longer an
unread blocker; direct growing-shift/short-interval imports are parked
for quantitative and quantifier mismatches. Label NEGATIVE, not a new
mathematical obstruction. No mathematical exploration turn was spent.

Three options considered: another full-shift direct import (parked by
the inspected statements); extracting a fixed-log partial upper
(already weaker than C034v(26)); coefficient-preserving prime-conditioned
cross covariance (a distinct, unassessed partial target). Select the
last for separate source coverage in review2106. It isolates one
actual-state cross term rather than replacing coefficients by arbitrary
factors. No claim that its estimate holds or implies the full norm.
The untouched divisibility sectors and their recombination remain
independent gaps. Missing exact coverage blocks a justified creative
proof attempt now; no routine audit or repeated log refinement follows.
