# Finite-band weighted-defect attempt — step367

Active target: Test the m_n=n equispaced band family for C997q's
exp(-n/64) weighted defect and boundary bounds at subexponential original TV.
Pre-invocation coverage: drafts/literature/2026-11-11-finite-band-defect-test-review-365.md
(EXPLORE, separately approved in step366). One bounded mathematical attempt.

Main gap: L030–L032/C032a actual-Xi positivity, L966/L968 signed forcing,
and unpaid L984(H). Intermediate use: a paid positive-branch point dual
could support signed slope selection; the separate transfers remain open.

C997q(1)–(2) checked directly against audited C997c(1),(4)–(6): finite
variation and compact windows justify Fubini; J'(x)=r q(rx)-q(x), and
exp(-x/4) integral_a^x exp(u/4)du <=4. Both windows, beta terms and
the polynomial subtraction remain. This is not an audit of all C997q.

Chosen mechanism: approximate the target by a centered polynomial in
exp(i t/(4n)), with degree <=n and carrier exp(15it/8). Track the SAME
coefficient-l1 norm and the complete weighted D and Delta. No division
by g_n is permitted. The inspected finite-sum source tools authorize
this approximation test but supply no uniform cost/rate bound.

Continue with a uniform certificate, a rigorous cost/error obstruction,
or a materially refined mechanism supported by evidence. Failure of a
sufficient upper envelope alone is inconclusive. No coefficients or
asymptotic bound have yet been certified at this checkpoint. All prior
unfinished work and stops314/315/364 and C997i/m/p remain intact.

## Saved reasoning before the full write-up

Choose a_n=(7-i)n/2, c_n=exp(-n/4-7in/4),
w(t)=1-exp(i(t-2n)/(4n)), and 0<=m<=n. Test
F_(n,m)(t)=c_n exp(15it/8) sum_(k=0)^m (a_n)_k w(t)^k/k!.
It is in the approved n+1-point grid, with zero coefficients above m.
The finite binomial identity gives its original coefficient variation
exactly; for m>=n/24 it is at least
7 exp(rho*n)/(10 e n), rho=(log168-5)/24>1/400.

For m<n/24, on c in [17/8-16/n,17/8], both w(cn) and
w(c(n+2)) eventually have modulus >=31/1000. Previous/next term
ratios are <=250/651, so each Taylor sum divided by its last term
lies in the disk of radius 250/401 about 1. Its argument has modulus
<7/10, and its modulus is >=151/401. The phase difference of the
two F values consequently lies in [13/2,47/5], away from pi*Z.
As g_n is real on R, projecting perpendicular to F(c(n+2)) prevents
cancellation of the g_n(cn)F(cn) term in the defect.

Reused existing source coverage, without a new source search:
C997e(4) and its step329 audit, with review325's previously inspected
Vanlessen v2 Theorem2.4(b) specialization Q(x)=x, alpha=2, N=n+1.
Only its uniform REAL bulk formula on J=[15/8,17/8], u=0 is needed;
no Gaussian packet, saddle or contour assertion is imported. The
moving point remains inside this SAME fixed J. The leading cosine
has a peak in the interval of length16/n above, yielding
|g_n(cn)|>=c n^(-3/2) exp(3cn/8). The complete target defect is O(n)
after weighting, while the approximant defect is at least
c n^(-3/2) exp(n/64). This is a proposed rigorous subclass stop,
to be written and checked below; arbitrary grid coefficients remain open.

Duplicate check: C997g concerns polynomial SLOPE densities with complete
data-jet annihilation, not these atomic BAND measures and centered
time-domain Taylor coefficients. C997i/m/p and stops314/315/364 do
not give the displayed norm/defect dichotomy. No unrelated covariance
result is used. The lower-window boundary need not be estimated to
refute simultaneous admissibility once original TV or D already fails;
no conclusion about small residual alone follows.

## Completion

The full proof is now canonical in
lemmas/C997r-centered-taylor-band-norm-defect-obstruction.md; the
working calculations above are preserved as unfinished-work history,
not an independent theorem source. The resulting scoped NEGATIVE is
unaudited. Its 21 rational scalar checks pass, with the full /checks
object inspected in the saved certificate. The arbitrary-coefficient
grid problem remains unresolved. The single continuation is an
independent conceptual audit, with a new ready source nomination that
requires separate next-turn approval. No mathematical exploration
counter or supervisor state was changed.
