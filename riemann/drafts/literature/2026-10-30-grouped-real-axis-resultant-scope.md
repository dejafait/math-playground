# Grouped real-axis resultant — source comparison

TARGET: Review Planat arXiv:2609.37164v2 Sections 6.1 and 6.7's grouped real-double-zero resultant, identifying whether its finite-exterior certificate can be specified independently of the moving-separator and inherited upper-band premises.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the prior notebook-scoped resultant/chirality duplicate search and Proposition 6.1 assessment; targeted checks of the collective-bridge working record, barrier assessment and inverse-gap stop found no completed fixed-cutoff resultant audit. Web queries "de Bruijn" "real-double-zero" resultant mollifier and "2609.37164" "resultant" "frozen" supplied no stronger inspected theorem; an unrelated polynomial-book result was not used. No novelty inference follows.
SOURCE_EVIDENCE: Michel Planat, arXiv:2609.37164v2, 7 October 2026, https://arxiv.org/html/2609.37164v2 and https://arxiv.org/pdf/2609.37164v2 : Section 6.7 in full, pp.26–28, equation (44), Lemma 6.10/equation (45), proof and frozen-cutoff/reflection/Cauchy cases; Section 6.6 coefficient/domain definitions and repaired handoff, pp.22–24; Section 6.8 and Theorem 6.11/Corollary 6.13/Remark 6.14, pp.28–31. Reused the already inspected Section 6.1 Proposition 6.1, pp.15–16, without reproof. D. H. J. Polymath, arXiv:1904.12438v2, 4 August 2019, https://arxiv.org/html/1904.12438v2 : Theorem 1.3 in full, equations (5)–(24), prefactor/branch definitions and following fixed-cutoff qualification inspected; its saddle proof remains imported.
COMPARISON: The source isolates a pointwise grouped resultant with explicit saddle and true-double-zero charges; its algebraic hypotheses contain neither separator nonvanishing nor an inherited time ledger. The selected disk interface is therefore independently auditable. The newer assembly replaces historical H3 through fresh computations, but retains H1 and directed-enclosure validity; neither global endpoint nor reported reserves are imported.
GAP: The local coefficient reserve, phase denominator and complex-disk error enclosures remain uncertified here. In particular the frozen/local cutoff difference, reflected-face growth and Cauchy derivative budget need a separate mathematical audit before any true-function numerical collision exclusion. Interior exclusion, smaller positive times and zero time remain independent gaps.
REASON: Continue with a bounded audit of the analytic error interface, using the published approximation and source's stated elementary reductions. Citation supplies the proposed criterion but does not validate its asserted disk constants or implementations. No new lemma or calculation was made during this source review.
LITERATURE_REASON: Essential unread Section 6.7 is now inspected; its target differs from collective landing. Section 6.1 coverage is reused. The narrow Section 6.8/6.9 check was needed to distinguish historical H3 from the current assembly.
SCOPE: Ready source coverage for reviewing the stated local resultant and auditing the frozen-index reflection/Cauchy interface on the explicit domain below; excludes coefficient-ledger replay, any new cancellation mechanism and global endpoint import.
COVERED_TARGET: Audit Planat v2 Section 6.7's frozen-cutoff reflection and Cauchy derivative charge on 0.16836<=t<=0.1718, x>=6000284561421.5 and t*log(x/(4*pi))<=5.17, using Polymath Theorem 1.3 and no numerical ledger imports.

## Main gap, target and source decision

The main RH gap remains actual-Xi all-degree positivity. In the heat route,
L489/C489a reduce a hypothetical positive transition to a finite real
multiple zero, without excluding one. This review targets the source's
finite-exterior collision certificate, not contraction or a new endpoint.
A valid local certificate could shrink the remaining spatial region on
one positive-time band. Interior collisions, other times and zero-time
control would remain even after that success.

The outcome is source-scope progress only: an independent local test is
specified. No numerical inequality, source manuscript or code archive is
certified. The separate next-turn audit is reproduction/conceptual review,
not a creative proof attempt or a claim beyond the sources checked.

## Retrieved pointwise hypotheses and charges

In Planat Section 6.7 fix real t and freeze N under spatial differentiation.
Let z=(1+ix)/2, nu=z+t*alpha(z)/2=sigma+i*eta,
B=M_t(conj(z)), Theta=arg M_t(z), and
S_N=sum_{q<=N} b_q(t)q^(-nu), b_q=exp(t*log(q)^2/4).
The real-axis normalized approximation is

    H_t/B = f_N+R_N,
    f_N=conj(S_N)+exp(2i*Theta)S_N=exp(i*Theta)V,
    V=2 Re(exp(i*Theta)S_N), real.

The source takes a finite prime set P, either p<=307 or the ten-prime
p<=29 set, and requires r_p=b_p*p^(-sigma)<1 for each prime. It defines

    E=product_{p in P}(1-b_p*p^(-nu)),
    S_hat=E*S_N, Theta_hat=Theta-arg E,
    ell=4 Theta_hat'>0, Z=exp(i*Theta_hat)S_hat,
    L_hat=sum_m beta_m(t)m^(-nu)log m, W=exp(i*Theta_hat)L_hat.

Here beta_m=sum_{d|m, d squarefree over P, m/d<=N}
mu(d)*(product_{p|d}b_p)*b_(m/d). In particular b_2*b_3 is not b_6.
M_t is the nonzero holomorphic prefactor of Polymath (6)–(10), on
C minus (-infinity,1]; local differentiable phases suffice. E nonzero,
B nonzero and a strictly positive ell are essential hypotheses.

Equation (44) defines G_tilde=Z-W/ell+conj(W)/ell. Its stated scalar
majorant uses h(m)=max(1,2 log(m)/ell-1), with coefficient m=1 of
modulus one, and gives |G_tilde|>=1-M. A lower bound ell_hat for ell
may be used in h. Section 6.6's initial corner has N=691004,
H=160N=110560640 and x in [6000284561419.5,6000284561421.5].
Its (41) groups |a_m| through H and uses positive divisor-channel
triangle weights above H, where a_m=beta_m*m^(-sigma). It omits h
below H only under the stated H<exp(ell_hat) condition. No cancellation
of unknown Dirichlet phases is assumed.

Lemma 6.10 defines V_hat=2 Re Z and
G_star=V_hat/2-i*V_hat'/(2 Theta_hat'). It states both bounds

    |G_tilde-G_star| <= (4/ell)(|sigma'|+|eta'-1/2|)|L_hat|,
    |G_star| <= |E|*epsilon/2
                  +(2/ell)(|E'|*epsilon+|E|*epsilon_1)

where the second bound is only at a true multiple real zero and assumes
|R_N|<=epsilon, |R_N'|<=epsilon_1. Its proof uses q=q'=0 and the
reality of V,V'; it does not bound R_N' by differentiating epsilon.
These are source statements with proof inspected, not locally audited
results. The source's strict certificate compares 1-M with these two
charges (and charges any transport separately); M<1 alone is insufficient.

## Essential true-function cases and independent domain

Polymath Theorem 1.3 applies for 0<t<=1/2, real part x>=200 and
0<=Im w<=1, with N_local=floor(sqrt(Re(w)/(4*pi)+t/16)).
Equations (23)–(24) explicitly bound e_A+e_B and e_C,0. The theorem
following (24) warns that the approximation is holomorphic only while
its cutoff is fixed. Its proof is imported; a pointwise error bound
for N_local is not automatically a derivative bound for frozen N.

Planat freezes N=N_local at the real centre and writes, for complex w,
u=(1-iw)/2, F_N(u)=sum_{n<=N}b_n*n^(-u-t*alpha(u)/2),
f_N(w)=F_N(u)+gamma(w)F_N(1-u), gamma=M_t(1-u)/M_t(u).
Section 6.7 gives the exact fixed-N reflection identity

    R_N(conj(w))=conj(R_N(w))/conj(gamma(w)).

The source uses radius r=0.14142. On the upper half disk it bounds the
local approximation error by E_global using Theorem 1.3's explicit
formulas, sigma_floor=1.6318 and a second-chirality bound at most one
after extracting the first coefficient. It asserts that the e_C,0 upper
envelope is maximal at y=0. The lower half requires reflection, with

    G <= exp(r*(L/2+(t*L/4+3.21)/(x-6))) < 8.770232,
    L=log(x/(4*pi)).

The disk may cross one cutoff transition. The difference of the local
and frozen models is an unmollified two-chirality entering pair;
the source charges P=1.3e-6 at real centres and its disk growth separately.
Its claimed Cauchy budget is

    epsilon=E_global,
    epsilon_1 <= (E_global+P)*G/r.

E_global is to be an actual uniform upper-half-disk envelope from the
published error sums, not merely the real-centre value or a printed
program scalar. The source's phase/cutoff envelopes, their closed edges,
and the precise use of G for both terms are audit obligations, not facts
verified in this review. The mollified scalar jump is a different
transport allowance and cannot replace P. Section 6.2 explicitly records
that earlier distinction as a correction; Section 6.6 also records a
withdrawn handoff margin caused by omitted row multiplicity. Neither
old margin is available for reuse.

For the next audit use 0.16836<=t<=0.1718,
x>=6000284561421.5, C=t*L<=5.17. This is a fixed numerical exterior
domain, with no separator nonvanishing assertion. It lies on the safe
side of the source's x>=x_s(t) condition, where its explicit geometric
function is x_s(t)=6000284561420.5+31/120-(1921/2000)t.
Only that formula specifies location; H1 is not assumed. Both real parts
of u and 1-u stay positive on the small disks and their imaginary parts
are far from the prefactor branch cut. Any detailed inequalities needed
to validate the above charges belong to the separate audit, including
cutoff equality and a transition crossing on either side of the centre.
Negative real centres can use evenness after the positive-side audit;
reflection in Im w for Cauchy is a distinct, already stated issue.

## Comparison, bounded test and limits

Theorem 6.11's historical assembly assumes H1 (separator), H2 (new local
band), H3 (inherited upper band) and H4 (explicit far tail). Inspection
of Section 6.8 and Corollary 6.13 changes the inherited-ledger conclusion:
the newer assembly supplies replacement exterior computations rather
than retaining H3. It still assumes H1 and correct directed enclosures.
Neither agreement at two precisions nor reported reserves establishes
those mathematical premises. No companion archive was loaded, no source
blockage was encountered and no global numerical endpoint is imported.

Continue by auditing exactly the fixed-N disk interface on the domain
above, with E_global specified from Theorem 1.3's finite error sums and
explicit rational/exponential envelopes. The discriminating test is
whether the stated P and G suffice to establish the displayed derivative
charge at all centres, including cutoff equality/transition cases.
Accept a rigorously justified symbolic interface or a precise corrected
charge as useful progress; stop this application if it needs an interior
zero-free premise or an essential inaccessible producer. A failure of a
printed constant is evidence against that budget, not a disproof of RH
or of all possible resultant methods. Do not replay coefficient ledgers
until this interface is sound.

The current sources specify a collision-sensitive mechanism but do not
justify a new creative mechanism yet. The immediate blocker is analytic
error validity, which this conceptual audit can test independently.
L058/L488 fix F(lambda,z)=8 H_(4lambda)(2z); L489/C489a and C493a
provide transition/tail context only, not premises asserting the desired
local exclusion. Original strip and saddle estimates retain their
imported-proof qualifications. Full matching Mathlib coverage was not
checked; its availability is unknown. No lemma, mathematical script,
DAG edge or PROOF.md argument was changed in this literature-only turn.
