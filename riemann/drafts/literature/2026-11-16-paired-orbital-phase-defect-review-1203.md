# One-pair orbital phase defect — completed source review1204

TARGET: Review a one-conjugate-pair extension of C030l: determine whether known complex HCIZ/corner results cover an adjacent-rank tilted-mean defect bound C*x*b^2, with absolute C independent of n,k and positive real rates, for x>0 and x*|b|<=1/4 on the positive partition-function branch, before approving one bounded proof or counterexample test.
CHECKED: 2026-11-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact-defect, complex-HCIZ, zero-free, logarithmic-derivative and orbital-tilt searches found no matching uniform adjacent-rank estimate; primary results and scoped duplicates/stops were compared. Queries and read ranges: drafts/working/2026-11-16-paired-orbital-source-review-1204.md. Failed searches do not establish novelty.
SOURCE_EVIDENCE: Inspected Novak arXiv2203.10746v1 Theorem1.2 p6/domain pp2-3 and Theorem4.7 proof; GGN AMBP21(2014) Theorem5.1 pp84-86/Section5.2 pp86-87; Guionnet--Maida corrected author PDF Theorem4 p5/Hypothesis1.1; McSwiggen arXiv1712.03995v4 Theorem1 p4/(2) p2/continuation p10. Reuse C030l's real-rate source assessment1202.
COMPARISON: Complex HCIZ analytic identities and bounded-spectrum small-coupling nonvanishing are known; their domains and normalized large-n expansions do not directly provide the proposed unnormalized C*x*b^2 defect at arbitrary real-rate spread. No inspected theorem or counterexample resolves that exact bound or automatic positivity throughout x|b|<=1/4. C030l's positive-law proof does not apply with complex fields.
GAP: Uniform infinitesimal phase response remains unproved even for the two-real-level diagnostic; finite-b control, full proposed positivity window, arbitrary remaining rates and actual-Xi transfer remain separate. Domain mismatch is not proof of indispensable rate/dimension growth.
REASON: Essential source comparison is now sufficient for a bounded second-order/two-real-level proof-or-obstruction test, without assuming the target or redoing general orbital theory. A separate ready continuation1204 specifies that test for next-turn approval; no mathematical result is derived in this literature turn.
LITERATURE_REASON: The starting REVIEW_REQUIRED target changed real D and probability tilts to a conjugate complex pair, outside assessment1202; essential complex HCIZ/corner comparison and obstruction coverage were missing and were supplied in review1204.

## Original nomination1203, retained as an unproved proposal

The following proposal and its original review instructions are preserved
for scope. The completed comparison below supersedes their unread-source
and approval status; no claim in the proposed estimate has been proved.

### Exact proposed observable, not a mathematical conclusion

Fix finite n>=2, 0<=k<n, positive real a,r_3,...,r_n and real b.
Set D_0=diag(a,a,r_3,...,r_n) and
D_b=diag(a+i*b,a-i*b,r_3,...,r_n). With normalized Haar measure define

    Z_(j,b)(x)=integral_U(n) exp(-x tr(D_b V P_j V*))dV,
    G_(j,b)(x)=-Z'_(j,b)(x)/Z_(j,b)(x),
    E_(k,b)(x)=(G_(k+1,b)-G_(k,b))
                   -(G_(k+1,0)-G_(k,0)).

The proposed question is whether a finite absolute C can guarantee

    |E_(k,b)(x)| <= C*x*b^2

independently of n,k and the positive real rates, when x>0,
x*|b|<=1/4, and both paired partition functions in the quotient are
positive real. That branch restriction is a stated premise for the
comparison, not a nonvanishing theorem established in this nomination.
The review should check whether it is automatic in the proposed range
and whether a known bound has indispensable rate-spread or dimension
dependence. Treat such dependence as evidence, not silently discard it.
The b=0 and endpoint-rank cases must be retained.

This nomination merely specifies the target and observable; no
calculation, lemma, proof, numerical probe or coverage approval is
performed for it in audit1203. Do not infer that the bound is true.
Do not replace the orbital integral by its absolute value or reuse
C030l with complex fields as though its coupling survived.

## Relevance and bounded decision

Main gap: all-degree actual-Xi algebraic-square positivity in
L030-L032/C032a. A one-pair signed response bound could be an input
to a later comparison of real-rate reference determinants with
conjugate-rate data, before absolute signed-variation estimates lose
the interaction. This is only a plausible intermediate use. A link
to actual squared zeros, summation over pairs, small-phase/time
coverage, determinant nonvanishing at larger times, degree-growing
factor supply and L030 transfer are all unresolved. The bound, even
if true, would establish none of them by itself.

Use C030l and its precise source as the real reference. Reuse
review884 and discovery1202 for the finite-core C.9 overlap and stops
1117/1181/1193/1200/1107 for the existing all-order/graph limitations.
These are local scope comparisons, not hypotheses for a complex
orbital theorem. No cross-notebook input is proposed.

The literature review should check the exact estimate, standard
complex-parameter HCIZ/orbital terminology, stronger comparisons and
known finite-complex-spectrum obstructions before selecting a proof
test. If known, import with its precise assumptions. If unsupported
but source coverage is adequate, a later bounded test may examine
the second-order response and a two-real-level family, preserving
the independently normalized adjacent ranks. If a theorem or explicit
counterexample already forces rate-spread/dimension growth, record
that obstruction and reassess the target. Failure of this proposed
universal bound would concern this mechanism, not actual Xi or RH.

No creative proof attempt is approved yet. After essential coverage,
a genuinely new bounded phase-response test would warrant
proof_attempt/creative only with a precise escalation: loss of
positive corner-law order for conjugate rates blocks the signed
reference comparison, and a uniform bound or a rigorous violating
family discriminates whether this response mechanism merits use.
Do not manufacture a creative label if the review finds known coverage.
Full matching Mathlib coverage is unchecked.

Sources carried forward:
[Sra author v3](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
LemmaC.7/TheoremC.8 and (C.17)/C.9, pp25-28;
[Olshanski2013](https://www.heldermann-verlag.de/jlt/jlt23/olshla2e.pdf),
Corollary3.2 p1017. At nomination1203, complex-rate extensions were
unread leads; completed comparison1204 follows.

## Completed primary-source comparison1204

1. **Exact complex identity, not stochastic order.** C. McSwiggen,
   *A new proof of Harish-Chandra's integral formula*,
   [arXiv:1712.03995v4, 27 April 2020](https://arxiv.org/pdf/1712.03995v4),
   Theorem1 p4, treats Cartan elements of a complexified semisimple Lie
   algebra, normalized Haar measure and the Killing-form pairing.
   Its U(N) trace convention is (2), p2, initially with distinct real
   diagonal entries. The proof's continuation after (24), p10, concerns
   the discriminant-multiplied identity. A repeated-spectrum quotient
   requires a removable-limit argument; substitution into a zero
   Vandermonde denominator is invalid. The formula supplies no positive
   coupling, nonvanishing quotient or adjacent-rank inequality.

2. **Strongest inspected complex nonvanishing theorem.** J. Novak,
   *Topological Expansion of Oscillatory BGW and HCIZ Integrals at Strong
   Coupling*, [arXiv:2203.10746v1, 21 March 2022](https://arxiv.org/pdf/2203.10746v1),
   (1.2), pp2-3 and Theorem1.2, p6, uses
   I_N=integral exp(z*N*Tr(AUBU^-1))dU. On the closed polydisc
   |z|<=epsilon, |a_i|,|b_i|<=1, some absolute epsilon>0 gives
   nonvanishing for every N and uniform large-N logarithmic expansions.
   Eigenvalue repetitions are not excluded by this polydisc statement.
   Read the Theorem4.7 proof's nonvanishing reduction: a normalized
   integral within1 of1 handles large N, followed by shrinking the disc
   for the finitely many remaining dimensions. This is not a proof
   audit of its critical coefficient bounds. The inspected 2020 predecessor,
   [arXiv:2006.04304v1](https://arxiv.org/pdf/2006.04304v1),
   Conjecture1.1/Theorem1.4 pp2,6, has the same bounded-field scope;
   it is not an additional independent estimate.

   For applicability comparison only, using A=-D_b/M, B=P_j and
   z=x*M/n, M>=max_i|(D_b)_ii|, matches the exponent. The theorem's
   small-coupling condition then restricts x*M/n. The proposed phase
   restriction alone does not impose that condition. Centering the real
   rates can remove a common scalar but does not bound their spread.
   Moreover, a large-N free-energy expansion is not the desired
   finite-n, adjacent-rank, separately normalized derivative estimate.
   This excludes a direct import from the inspected statement, not
   the possibility of a useful further specialization or a better bound.

3. **Earlier convergence criterion and finite complex zeros.**
   I. P. Goulden, M. Guay-Paquet and J. Novak,
   *Monotone Hurwitz Numbers and the HCIZ Integral*, AMBP21(2014),71-89,
   [publisher PDF](https://www.numdam.org/article/AMBP_2014__21_1_71_0.pdf),
   Section3.4 p79 assumes complex diagonal matrices with operator norms
   uniformly <=M and convergent normalized moments ((M,0)-regularity).
   Theorem5.1, pp84-86, additionally assumes eventual nonvanishing on
   |z|<R and concludes compact-uniform convergence of N^-2 log I_N
   on radius min(R,1/(54*M^2)). Read its two-circle/Cauchy and
   Borel--Caratheodory proof cases: nonvanishing is a premise there.
   Section5.2, pp86-87, computes imaginary zeros when one real simple
   spectrum is an arithmetic progression and the other is real simple.
   Its displayed zero list must exclude z=0, where I_N(0)=1 and the
   determinant quotient is removable. This is evidence against a global
   zero-free inference, not a counterexample to the proposed paired-rate,
   projection-spectrum, small-phase bound. Novak2022 supplies later
   local nonvanishing; do not retain the 2014 lack of a general proof
   as a current source blocker.

4. **Low-rank complex asymptotics have different hypotheses.**
   A. Guionnet and M. Maida, *A Fourier view on the R-transform and
   related asymptotics of spherical integrals*, JFA222(2005),435-490,
   [corrected author PDF dated13February2012](https://perso.ens-lyon.fr/aguionne/rgfend.pdf),
   Theorem4 p5: beta=1, uniformly bounded real spectral sequence E_N,
   weak convergence to compactly supported non-Dirac mu_E and Dudley
   distance o(N^-1/2). It gives rank-one complex-parameter asymptotics
   in a sufficiently small disc. Hypothesis1.1 and the theorem were
   inspected; the author publication page flags a published Theorem3
   typo, so no second-order constant is imported from that version.
   This beta=1 asymptotic does not supply a unitary beta=2 finite-n
   rank-k/rank-(k+1) defect with an arbitrary real background.

### Decision and limits

No inspected theorem covers the exact estimate, and no rigorous violating
family was found in the sources. The full positive-branch assumption is
retained: automatic positivity on the whole phase window remains an
unanswered part of the proposal. It need not be assumed for all times to
pose a local b-to-zero diagnostic, whose local legitimacy must itself be
justified in the next mathematical attempt.

Proceed only to the nominated two-real-level infinitesimal response test
in assessment1204. A rigorous unbounded family there would refute the
universal full estimate; a uniform bound there would settle only this
restricted necessary test. No response formula, bound, positivity lemma,
counterexample, general HCIZ reproof, actual-Xi transfer or Mathlib
theorem match was produced here. Sources are external stated results,
not independently audited proofs. No persistent essential access blocker
remains for this bounded diagnostic. Other retrieved leads, including
two-projection Jacobi reductions and rank-deficient contour formulas,
are not imported or required inputs. Full matching Mathlib coverage
remains unchecked. This is completed source coverage, not progress beyond
the checked literature or a resolution of RH.
