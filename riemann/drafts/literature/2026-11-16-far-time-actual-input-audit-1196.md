# Actual-zero inputs: source coverage1196

TARGET: Audit Polson v24 Lemma 7.8's actual-zero node selection and count (13), including endpoint and multiplicity conventions, for applying C030h within C030b.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused1194/1188/1113/1114 and C030b's1116 audit; searched local literature/working/attempt/history/foundation paths for Rosser, Kadiri, separated low zeros, actual-zero node and count(13). External searches covered Polson separated low zeros, Rosser zero-count constants, Kadiri2005 p329 and Rosser1941 Theorem19. No independent matching node/count audit was located; no novelty or search-completeness claim.
SOURCE_EVIDENCE: Directly read Polson arXiv:1708.02653v24 (11September2026), Section6.2/(10),(13) printed p13 and Lemma7.8/(27) full proof p20; Kadiri Acta Arith.117.4(2005),303-339, p329, Lemma4.3 proof before(38), states the exact quoted Rosser bound and closed upper count; Hasanalizade–Shen–Wong2107.06506v1 Corollary1.2/(1.5) p2 and Section2/(2.1)-(2.3) p3 independently supply an explicit occurrence count; Platt–Trudgian2004.09765v1 Theorem1/Section2 p2 read for finite verification scope. Exact links and retrieval limits below.
COMPARISON: Lemma7.8 and(13) already assert the needed inputs; C030h assumes them and C030b imports their downstream theorem. Kadiri supplies the exact source count as a named Rosser theorem input. HSW supplies a directly inspected primary alternative count, with different constants and main-term normalization that require explicit checking if used. Import the named counting theorem; audit only the source's elementary consequences and occurrence interface, rather than reprove zero counting.
GAP: Verify the interval-existence and squared-node inequalities uniformly for j>=1, the r^2 count for all real r>=1000, and compatibility with C030h's strict tail and multiplicity convention. Source statements and relevant proof cases are now covered; no such inequality is independently certified in1196.
REASON: This separate literature turn closes the changed actual-spectrum coverage gap from1195. Adequate source statements are accessible without retrieving or reproving Rosser's original proof. The primary HSW alternative is available for an independent check; its sufficiency at the fixed cutoffs is an audit obligation, not an assumption. Ready coverage requires separate next-turn approval.
SCOPE: Actual zeta-zero occurrences, arbitrary integer N>=1, conditional line verification through150N for selected nodes and throughT for all low nodes, T>=max(1000,150N); count cutoffs100 and1000, intervals(100j,100j+50], multiplicities and cutoff atoms. Elementary specialization of imported explicit counts and existing occurrence/strip facts only. No proof of Rosser/HSW constants or verification computation; no Theorem7.4 joining comparisons, new height/time choice, or all-degree extension.

## Main gap, use and discriminating test

The main unresolved statement remains actual-Xi Q(q)>=0 in every degree
in L030-L032/C032a. Actual-theta signing and graph realization are
independent gaps. The single intermediate target is the actual-zero
node/count input to C030h; its downstream use is a source reliability
check within C030b's finite theorem, without extending its degree cap.

Continue only after a uniform proof audit meets the exact source
thresholds for every N and real counting height, including N=1 and
endpoint atoms. Preserve a failed scalar inequality, mismatched count
or missing assumption explicitly. Such a failure would affect this
application, not refute RH. No sampled ordinates or numerical sweep
establish this target. No mathematical replay is performed in1196.

## Precise count inputs and their limitations

Habiba Kadiri, *Une region explicite sans zeros pour la fonction zeta
de Riemann*, Acta Arithmetica117.4(2005),303-339,
[author-hosted published PDF, p329](https://www.cs.uleth.ca/~kadiri/articles/zero-free-region-riemann-zeta-acta-2005.pdf#page=27),
Lemma4.3 proof immediately before(38), gives the exact statement used
by Polson. For u>=2, with N(u) counting nontrivial zeros whose imaginary
parts belong to[0,u], it quotes Rosser's theorem in the form

    M(u)=u/(2*pi)*log(u/(2*pi*e))+7/8,
    E(u)=0.137*log(u)+0.443*log(log(u))+1.588,
    |N(u)-M(u)|<=E(u).

Import this precisely cited statement as a standard named theorem,
not as an original fact. Kadiri's different N1/N2 simplifications
(38)-(41), subsequent reciprocal-ordinate sums and zero-free-region
theorem are not inputs. Its interval notation includes the upper
endpoint. Multiplicity must be reconciled with the independently
inspected argument-principle count below and the local convention;
no simplicity premise is authorized.

The original is Barkley Rosser, *Explicit bounds for some functions
of prime numbers*, Amer.J.Math.63.1(1941),211-232,
[DOI10.2307/2371291](https://doi.org/10.2307/2371291), Theorem19, p223.
The original theorem page and its count definition were NOT read.
A public issue scan was located via an external bibliography used
only as a locator. The [archive issue](https://archive.org/details/sim_american-journal-of-mathematics_1941-01_63_1)
and an OCR wrapper opened, but theorem-range retrieval timed out;
PDF/page-number downloads redirected to an inaccessible archive host,
and JSTOR exposed no theorem text. A direct shell fetch failed DNS.
An AMS Rosser–Schoenfeld1975 lead returned403 and is unused. These
failures give no theorem evidence. Do not repeat the blocked original
retrieval as the next action: Kadiri's exact published statement and
the following directly inspected primary theorem suffice for the
bounded specialization/audit, without certifying Rosser's proof.

Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong, *Counting zeros
of the Riemann zeta function*, J.Number Theory235(2022),219-241,
[arXiv:2107.06506v1,14July2021](https://arxiv.org/pdf/2107.06506v1#page=2),
Corollary1.2/(1.5), p2, states for every T>=e:

    F(T)=T/(2*pi)*log(T/(2*pi*e)),
    B(T)=0.1038*log(T)+0.2573*log(log(T))+9.3675,
    |N(T)-F(T)|<=B(T).

This has no7/8 in its center. Section2/(2.1)-(2.3), p3, identifies
the symmetric |gamma|<=T count with twice the positive count and
with the argument-principle count of the entire completion; its
contour calculation is initially away from zeros. The introductory
definition includes0<gamma<=T. Multiplicities are thus included;
the cardinality notation must not be read as counting only distinct
ordinates. Use the stated corollary, with explicit endpoint handling
in the replay if passing from nonzero contour heights. The constants,
Maple calculations and finite computations in its proof remain
imported. Its different error term cannot simply be inserted into
Polson's printed scalar chain with unchanged intermediate constants.
If used for independent checking, verify its own fixed-width and
r^2 inequalities uniformly at the required cutoffs. That permitted
specialization is part of this same actual-input target, not a new
zero-count theorem or an approval of a new lemma this turn.

## Source proof cases to replay after approval

[Polson v24, printed p13](https://arxiv.org/pdf/1708.02653v24#page=13)
defines the multiplicity-weighted positive count before(10) and
asserts(13). [Lemma7.8/(27), printed p20](https://arxiv.org/pdf/1708.02653v24#page=20)
has been read in full. The following are source assertions for the
future audit, not passed inequalities:

    r>=100:
    M(r+50)-M(r)>7*(log(r)-2),
    E(r+50)+E(r)<(6/5)*log(r)+19/5,
    N(r+50)-N(r)>(29/5)*log(r)-89/5>1.
    r>=1000:
    N(r)+1<=r^2/6+0.58*r+3.463<r^2.                 (13)

Audit the derivative/integral comparison and elementary logarithmic
estimates, including their strictness at r=100 and1000. Differences
of inclusive counts must count exactly(r,r+50], retaining all zero
occurrences. Selecting one occurrence in each prescribed interval
must yield distinct nodes despite any multiplicity elsewhere.
Check the conditional reality, 10000<a_j<=22500N^2 and separation
|a_j-a_l|>=10000|j-l|, uniformly in N. Keep an occurrence at gamma=T
in the low part; the high tail of C030h is gamma>T. No assertion of
an empty endpoint, simple zeros or rounded numerical ordinates is
available as a shortcut.

C030g already supplies the local positive-occurrence convention,
with one exponent per positive zero occurrence, an off-line quartet
contributing two conjugate nodes, and no factor two in this count.
Use L018/L026 only as existing strip/symmetry/no-zero-ordinate inputs
when required; inspect their relevant proofs before relying on any
unread claim. C030h's hypotheses still require reality of ALL low
exponents throughT, not merely reality of the N selected nodes.
Its remaining tau/rho/delta thresholds are not certified by the
present input target. C030b's joining arithmetic remains outside.

[Platt–Trudgian, arXiv:2004.09765v1, Theorem1 and Section2, p2](https://arxiv.org/pdf/2004.09765v1#page=2)
provide finite line verification through3000175332800, with Turing
completeness and interval arithmetic. This supports finite heights
within that range; arbitrary N retains conditional verification.
No computation is rerun and no all-height reality is inferred.

## Reuse, duplicates, stops and Mathlib

1194 assessed the conditional tail tools,1195 completed C030h, and
1113/1114/1116 assessed/audited C030b's cited finite application.
1188/1190 and C030g cover coarse convergence and occurrence bookkeeping,
not these fixed-cutoff scalar consequences. The targeted local
search found reading/application records but no independent matching
node/count certification. None of those completed results is reopened.

Stops1117/1181/1193 remain preserved. Their missing coefficient-uniform
signed mechanism is not supplied by this finite input audit. No
concrete new central mechanism and bounded transfer test is ready;
the creative-routing preference cannot turn this specialization into
creative work. Once approved, the next action is mathematics rather
than further browsing for the same already covered input.

Full matching Mathlib coverage for the actual node/count statement,
Rosser's explicit theorem and the finite verification is unchecked.
C030g's supporting convergence coverage does not formalize them.
No absence claim or formal certification is made. This assessment
approves source scope for a later REPRODUCTION audit only and records
no mathematical advance beyond the sources checked.
