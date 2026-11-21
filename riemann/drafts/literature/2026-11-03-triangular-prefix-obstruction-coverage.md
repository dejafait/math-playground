# Triangular prefix obstruction: completed source comparison, step 239

TARGET: Assess paper 47/v1 Section 7's Mellin-filter obstruction for the anchored triangular Möbius prefix residual, including scalar-anchor cancellation, zero multiplicities and the exact growth threshold.
CHECKED: 2026-11-03
DECISION: IMPORT
SEARCH_EVIDENCE: On 2026-11-03 searched Pintz 2608.24878 Theorem 6.1 and Selberg Mobius prefix oscillation Nyman Beurling; read the exact paper-47/v1 proof and its cited Pintz/v2 proof. Scoped local searches found only the earlier statement-level lead, not a completed prefix-obstruction proof. No priority claim.
SOURCE_EVIDENCE: bramble_trace, rStation paper 47/v1, 24 October 2026, Section 7, Proposition 4/(37)--(48), Corollary 5/(49)--(51); Pintz, arXiv:2608.24878v2, 1 September 2026, Theorem 6.1/(6.16)--(6.23), Lemma 4.1/(4.1)--(4.4), and (5.3)--(5.4), inspected in primary HTML.
COMPARISON: Paper 47 exactly matches L729's anchored triangular family and states a drift-uniform all-cutoff lower bound, including fixed multiple zeros. Pintz supplies the cancellation method but its stated theorem has different hypotheses and kernel. The subpower-growth corollary is RH-equivalent, not an independent residual upper estimate.
GAP: No unconditional subpower or full-norm upper bound follows. The manuscript's causal-kernel support, contour shifts, multiplicity residue and finite-prefix transfer still require a local conceptual audit before canonical import; its upper-growth corollary is outside that audit.
REASON: Stop treating the growth characterization as a new upper-bound mechanism; retain the separately testable Proposition 4 proof as a bounded known-source audit. This completes missing essential source coverage without deriving mathematics.
SCOPE: Source comparison only in this turn. IMPORT identifies an exact cited statement, not local verification of the manuscript. The separate audit assessment covers only Proposition 4 and (39), not the optimal-prefix Theorems 1--2, Corollary 5's upper bound, or norm decay.

## Primary sources and exact statement

[bramble_trace, *A logarithmic-prefix Nyman–Beurling criterion and
transferred zero bounds*, paper 47/v1](https://rstation.ai/problems/riemann_hypothesis/papers/47/v1)
is explicitly labeled v1, 24 October 2026. Read Section 1's definitions
(1)--(3), Section 2's comparison, and all of Section 7, (37)--(51),
including both proofs; Section 8's limitations and references [11]--[15]
were also inspected. Its displayed reviewer acceptance is not an input.
Sections 3--6's optimal-prefix transfer proofs are not needed or imported.

Its rho_k and H agree literally with L729. Its f_N equals L729's g_N
because rho_1=0. Write ell=log N and R_N=ceil(N log N), integer N>=2.
The source's prefix norm through R is the norm on [1,R+1), namely
sum_(j<=R)|v(j)|²/[j(j+1)], not the interval [1,R]. Its two errors are

    Q_N^head=||1-f_N||_(<=N)²,  Q_N=||1-f_N||_(<=R_N)².

Proposition 4 states: for each fixed nontrivial zeta zero rho=beta+i gamma
with beta>=1/2, there are c_rho>0 and an onset N_rho such that every
integer N>=N_rho satisfies

    inf_(a in C) J_N(a)>=c_rho N^(2 beta-1),
    J_N(a)=sum_(j<=N)|a j-psi(j)|²/[j(j+1)].                 (source 38)

Here psi(x)=sum_(n<=x)Lambda(n); a can depend on N. It states in (39)
that both prescribed errors are >>_rho N^(2 beta-1)/(log N)².
No RH, simplicity, finite-off-line-zero hypothesis or derivative moment
is assumed. Constants and onsets depend on the fixed zero; there is no
uniformity for growing height or multiplicity and no actual off-line
zero is supplied. At beta=1/2 this is only a log^(-2) lower obstruction.

## What was read in the essential proof cases

The following records the manuscript's argument and future audit
obligations, not a new proof or a locally certified theorem.

In (41)--(43) it sets m=ord_rho zeta, kappa=beta-1/4,
z=s+rho-kappa, and uses

    G(s)=(z-1)² zeta(z)/[(s-kappa)^m (s+1)^8],
    r(H)=(2pi i)^(-1) integral_(Re s=3) exp(Hs)G(s) ds.

It claims G holomorphic on Re s>-1: the zeta pole at z=1 is removed
and the zero of order m at z=rho removes the displayed denominator.
Moving to Re s=0 gives a bounded r, using Re z=1/4 and integrability
of G(it). Moving right to A->infinity instead gives r(H)=0 for H<=0,
including H=0, with bound C_rho exp(AH)A^(-m-5).
Unlike a Gaussian tail estimate, this is claimed exact causal support.
The contour justification, constants for large A and horizontal limits
must be checked locally; no unproved support statement is imported here.

The proof treats unbounded complex anchors first using Chebyshev's
psi(j)<=C_0 j: for |a|>=C_0+1 it obtains J_N(a)>=N/2. It then restricts
to |a|<=C_0+1, where h_a(x)=a floor(x)-psi(x)=O(x) uniformly. Its
initial absolutely convergent Mellin identity is, for Re z>1,

    integral_1^infinity h_a(x)x^(-z-1) dx
      =a zeta(z)/z+zeta'(z)/(z zeta(z)).                 (source 44)

In (45) the causal kernel confines its integral V to [1,Y], Y=N+1,
before using Fubini on Re s=3. The transformed integrand is

    Y^s (z-1)² [a zeta(z)²+zeta'(z)]
       /[z (s-kappa)^m (s+1)^8].                       (source 45)

The source shifts to Re s=-1/8, where Re z=1/8. It distinguishes
the removed z=1 pole, the excluded z=0 pole on Re s=-1/4,
and s=-1. Other zeta zeros are no longer denominator poles.
At s=kappa it asserts that the anchor term is regular while the
derivative term leaves one simple pole for every multiplicity m, with

    V=C_rho Y^kappa+O_rho(Y^(-1/8)),
    C_rho=(rho-1)² zeta^(m)(rho)
          /[rho (m-1)! (kappa+1)^8] !=0.              (source 46)

The error is claimed uniform in the bounded complex anchors. The
nonvanishing residue, continuation, absolute vertical integrals and
horizontal limits need an analytic audit, not just a symbolic check.
In (47)--(48) the stated representing weight has squared integral
integral_1^(N+1) x^(-1/2)|r(log((N+1)/x))|² dx=O_rho(N^(1/2));
the source uses weighted Cauchy--Schwarz against exactly J_N(a).
It concludes (38) from 2kappa-1/2=2beta-1.

For the final specialization (after (48)), the source defines
alpha_N=sum_(k<=N)mu(k)(1-log k/ell)/k, retaining k=1. Its finite
divisor identity is

    ell(1-f_N(j))=(ell alpha_N)j-psi(j),  1<=j<=N.

This is the anchor a=ell alpha_N, not an assumed constant or a dropped
term. The k=N coefficient is zero. The exact endpoint and this identity
are part of the proposed audit. No bound on alpha_N is needed for the
claimed lower estimate. Nothing in L730/L731 supplies that estimate.

## Pintz: precise comparison, not a direct specialization

[J. Pintz, *Oscillation of partial sums of the Möbius function and zeros
of Riemann's zeta function*, arXiv:2608.24878v2](https://arxiv.org/html/2608.24878v2),
dated 1 September 2026, Theorem 6.1 requires rho_0=1-eta_0+i gamma_0,
gamma_0>0, 0<eta_0<1/10, 2eta_0<kappa<1/2-2eta_0,
Y large and Y_0=Y exp(3). It states

    integral_1^Y_0 |M(x)| / [x^(1-kappa+beta_0)/gamma_0] dx
      >> kappa Y^kappa /
         [gamma_0^(C(eta_0+kappa)^(3/2)) (log(gamma_0 Y))^C].

Its (6.17) uses (z-1)zeta(z)/[(s-kappa)(s+1)^4], with
z=s+rho_0-kappa. Its (6.18) includes exp(s²/log Y).
Read the complete (6.19)--(6.23): the Mellin transform of M is
1/(z zeta(z)); multiplication removes unwanted zero poles, and
the residue in (6.20) is (1-1/rho_0)(1+kappa)^(-4)
exp(kappa²/log Y)Y^kappa. The Gaussian kernel has a nonzero physical
tail: (6.21)--(6.22) bound it beyond Y exp(3); (6.23) uses the
Korobov--Vinogradov-type estimate. These hypotheses do not cover all
beta>=1/2, complex drift, or an exactly supported first-N-cell test.
Paper 47 attributes the method and supplies its own rational-kernel
adaptation. Its Proposition 4 cannot be cited as a direct instance of
Pintz's Theorem 6.1. A local replay would be justified by the manuscript's
changed observable, causal kernel and multiplicity handling, not novelty.

## Exact growth threshold and its limits

Corollary 5/(40) states, with theta=sup Re(rho) over nontrivial zeros,

    lim log(2+Q_N^head)/log N
      =lim log(2+Q_N)/log N=2theta-1.

It expressly makes subpower growth N^(o(1)) along even one subsequence
equivalent to RH. This is growth, not convergence to zero. The lower
direction uses fixed zeros followed by a supremum, not estimates uniform
in zero height. For theta<1 its upper direction (49)--(51) invokes
M(x),psi(x)-x=O_epsilon(x^(theta+epsilon)) and
B_N=ell alpha_N-1=O_epsilon(N^(theta-1+epsilon)), with theta+epsilon<1.
The tail representation for B_N uses the two convergent Mobius moments;
(50) retains indices N<k<=j and (51) pays for N<j<=ceil(N log N).
For theta=1 it separately uses Chebyshev/PNT and a trivial coefficient
bound. Neither case sets theta=1/2 unconditionally.

Pintz Section 4, Lemma 4.1/(4.1)--(4.4) and (5.3)--(5.4) were
read for the cited fixed-half-plane argument. The source explicitly
omits the Borel--Caratheodory/three-circle proof, referring to Titchmarsh
Theorem 14.2; that book proof was not retrieved here. This is not
essential to the separate Proposition 4 audit, which uses ordinary
zeta/zeta-prime polynomial bounds, not the upper-growth argument.
Corollary 5's upper proof and its classical moment inputs remain locally
unaudited and are not proposed as a canonical input in the next step.

## Decision, duplicate checks and continuation

The original nomination sought a prefix obstruction independent of the
unpaid residual. Proposition 4 supplies an exactly stated candidate for
that narrow audit, conditional only on whichever fixed zero is tested.
The global subpower characterization instead restates RH and is parked
as an upper-bound mechanism. This source comparison is informative
negative evidence for that use, not a disproof of the prescribed family.

The dyadic-energy, neutral-tail and saturation assessments were searched
only for this named lead and their recorded stops; they contained no
completed prefix proof. L729's definitions and relevant divisor identities
were read; L730/L731's neutral information was not substituted for a
prefix bound. The full-update, sqrt(N)-tail and saturation stops remain.
Search snippets and unrelated hits were not used as theorem evidence.
The BCF/RH-and-moment comparison remains covered by the parent assessment;
it was reused rather than browsed again. Daval arXiv:2404.15520
Proposition 4/Corollary 1 is a source-referenced lead, not inspected or
needed for the self-contained Proposition 4 proof. No exhaustive overlap
or originality conclusion follows from these searches.

The separate continuation is
[the causal-prefix audit assessment](2026-11-03-triangular-prefix-obstruction-audit.md).
Continue only if its bounded replay validates support, contour bounds,
the drift-independent residue for arbitrary m, and the exact endpoint
transfer. Stop at the first failed case, retaining it rather than repairing
the source with unreviewed mathematics. This audit would document a known
obstruction; it would not prove mixed positivity or a norm upper bound.
No justified new creative upper-bound mechanism emerged; that remains
the blocker to creative routing. Newly saved ready coverage requires the
supervisor's separate next-turn approval before mathematical invocation.

LITERATURE_REASON: The saved changed target required its essential unread
primary proof. This turn completes that coverage; further browsing on
Proposition 4 is unnecessary unless an audit finds a specific missing input.

Mathlib: matching causal-filter obstruction and fixed-half-plane theorem
coverage were not checked; availability is unknown. Named contour-shift,
Mellin/Fubini and Cauchy--Schwarz tools are supporting inputs, not evidence
of a full matching formal theorem.

## Original nomination context retained

The intended object uses H=L²((1,infinity),dy/y²) and the actual
ordinary Möbius coefficients in L729's

    g_N=sum_(n<=N)mu(n)(1-log(n)/log(N))rho_n.

The nomination requested the source's precise initial-prefix restriction of 1-g_N; the
prefix endpoint and normalization must be extracted, not guessed. Keep
the scalar anchor, all complete-norm tails and the distinction between
an obstruction to this prescribed family and an obstruction to optimal
Nyman--Beurling approximation. RH and convergence of this particular
family are not interchangeable assumptions.

Essential local context: the paragraph headed “Reuse, unread leads and
decision” in `2026-11-03-triangular-mobius-dyadic-energy-contraction.md`
records the paper-47 lead without proof coverage. The completed
`2026-11-03-prime-representer-saturation-comparison.md` separates
RH-equivalent attainment from any arithmetic estimate. L729 defines the
family; L730/L731 supply no initial-prefix growth assertion. The
full-update and sqrt(N) stops are retained.

Plausible downstream use: a source-justified prefix obstruction could
identify which zero-sensitive arithmetic estimate must change, or rule
out an unproductive prescribed-family target. It would not establish
mixed positivity, an RH counterexample, a full norm upper bound or a
new creative mechanism by itself.

Bounded test: first retrieve the primary definitions, exact theorem and
its essential pole-cancellation/multiplicity proof cases, then the cited
Pintz theorem with all hypotheses. Continue only if these support a
precisely stated independently testable target. If the claim merely
restates RH or depends on the missing residual bound, park it and retain
that evidence. No calculation is preapproved by this nomination.

The nomination's literature reason was that this changed target had an essential unread primary
proof and exact hypotheses; the ready saturation assessment does not
cover it. Creative priority persists, but no justified new upper-bound
mechanism has yet been identified. Do not relabel known-source
obstruction extraction as creative work.

Its original Mathlib status was not checked; availability unknown.
