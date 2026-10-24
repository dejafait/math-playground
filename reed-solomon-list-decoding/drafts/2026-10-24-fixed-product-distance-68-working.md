# Distance-68 unchanged-box test — working record

2026-10-24, step 451. RESEARCH / REPRODUCTION, prior SPECIALIZE:
`drafts/literature/2026-10-24-fixed-product-distance-68-shell-psd.md`.
Exact target: Test the complete included-anchor distance-68 shell throughout L112's unchanged product box.

Main gap: arbitrary-center 67/68-agreement safety, bracket 955–957.
Nearer gap: full source PSD of the exact-N product assignment. This
bounded intermediate target tests just the anchor and all supports
disjoint from it. A whole-box pass retains one necessary slice; a fixed
rational direction with negative whole-box upper bound rejects this
prescription. Neither gives a uniform bound or an RS list.

Reuse approved source coverage, L021,L098,L112,L113,L114 and
foundations/04,09,12,14. Prior L106/ATTEMPTS/089 tests different scalar
support; L026/ATTEMPTS/018 tests different conditional coefficients.
Retain all L115–L119 results and audits without modification.

Before calculation: fix n=956,d=68 tail, one-point full head, all 69
tail relations and modes. Source coordinates are i=j=t=68,
s=68-h. The Boolean h=0 value is c68, forbidden h=1,...,4
values zero, and h>=5 values x68^2*xh. Anchor entries are 1,c68;
constant correction is binomial(956,68)*c68^2 exactly once.
Reconstruct all actual sets, six presentations, D and t-s, independently
normalize beta at the endpoint, and check complete multiplicities.
Preserve all 64 original points/scales/endpoints. No solve, scan,
retuning, refinement, added shell or changed assignment. Any straddle
ends inconclusively; a failed sufficient enclosure is not rejection.

## Completed attempt and source application

The assessed imports are Schrijver, *New code upper bounds from the
Terwilliger algebra and semidefinite programming*, IEEE TIT 51 (2005),
2859–2866, DOI [10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Theorem 1 (50)–(51), III.A (52)–(59), III.B (64), pp.6–7;
Brouwer–Cioaba–Ihringer–McGinnis,
[arXiv:1709.09011v2](https://arxiv.org/pdf/1709.09011v2), §1.2 p.3,
§3 opening formulas p.10, §3.4 multiplicities p.12; Brouwer–Haemers,
*Spectra of Graphs* (2012), [author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
§11.2 pp.162–163 and Theorem 2.7.1(i) p.36; Polak,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), §1.1 (1)–(3),
Proposition 1.1 and full indicator proof p.2 (proved constant-weight
conclusion, retaining the displayed A(n,d) qualification); Rump,
*Acta Numerica* 19 (2010), DOI
[10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
§5.5 (5.16)–(5.17) p.28. These were reused under the prior assessment;
no fresh literature extraction or reproof was needed. Full matching
Mathlib coverage remains not checked, not asserted absent.

Fix A of size 68. Its disjoint 68-subsets form the entire tail layer,
with S=binomial(956,68). For B,C in that layer put r=|B\\C|. Each
r=0,...,68 occurs. Permutations fixing A act transitively on pairs
with this r, so a representative covers each complete relation of the
prescribed invariant recipe. In mask order 0,...,7 for membership
in A,B,C, the full atoms are

    (888-r,68,r,0,r,0,68-r,0).

The A-anchored source coordinates and coefficient are

    (i,j,t,s)=(68,68,68,68-r), h=r,
    D=v_r=binomial(68,r)binomial(888,r).

Every one of the six presentations has its own checked D and third
pair, t-s=r, and the same full ordered count g_i*D=S*v_r. The six
r=0 presentations include the i=0 coincident row and both endpoint
repetitions; the Boolean value is c68, not a cubic product. The other
entries are zero for 1<=r<=4 and x68^2*xr for r>=5. Thus, with R_r
the tail relation matrices, the normalized union matrix is

    [[1, c68*1^T], [c68*1, C]],
    C=sum_r K_r R_r,
    K_0=c68, K_1=...=K_4=0, K_r=x68^2*xr (r>=5).

The one-point head is handled by Schrijver's surviving k=0 index,
not by a Johnson theorem outside n>=2d. Its head beta is exactly 1.
The tail satisfies 956>=2*68. The complete imported tail spectrum is

    E_k(r)=sum_(h=0)^r (-1)^h binomial(k,h)
                       binomial(68-k,r-h)binomial(888-k,r-h),
    m_k=binomial(956,k)-binomial(956,k-1), 0<=k<=68.

All m_k are positive and sum to S. The source-normalized beta is
beta_(68,68,k)^(68-r,956)/binomial(956-2k,68-k); all 69 denominators
are strictly positive. Independent reconstruction checks every one
of the 4761 eigenmatrix entries against this different formula, every
identity and valency, and all 4761 trace-orthogonality identities.
This checks a finite specialization of imported results, not a new
spectral theorem.

The positive-anchor congruence subtracts c68^2*J. Consequently the
complete Schur coordinates used in the attempt are

    sigma_k=sum_r E_k(r)K_r - 1_(k=0)*S*c68^2.

Both source cross directions equal S*c68, and the source constant
shell entry is S*sum_r v_r*K_r. The full constant block is therefore
[[1,S*c68],[S*c68,S*sum_r v_r*K_r]], whose second congruence entry is
S*sigma_0. The anchor correction is retained once, with no shell
inverse or discarded singular mode.

Each original positive endpoint is exactly l_i,u_i from L112. Entry
intervals are [c68,c68], [0,0], or [l68^2*lr,u68^2*ur]. A signed
coefficient E_k(r) uses the upper entry endpoint in a lower sum when
it is negative, and the lower endpoint otherwise; upper sums reverse
these choices. Subtract the exact constant correction afterward.
Repeated factors are allowed by expression inclusion. These bounds
enclose the full original box; overestimation is not a PSD failure.

## Evidence and stopping decision

Reproduction commands, from this notebook:

    python3 scripts/finite-support/fixed_product_distance_68.py
    python3 scripts/finite-support/verify_fixed_product_distance_68.py

Full certificates are `scripts/finite-support/fixed-product-distance-68.json`
and `scripts/finite-support/fixed-product-distance-68-verification.json`.
The constructor's 97 checks and independent verifier's 10606 checks
pass with zero failures. All 69 relations, 414 actual presentations,
69 modes, canonical pairs, exact N and rho, every original point/scale/
endpoint and retained root/lower audit binding are checked. The verifier
imports no constructor routine and consumes every complete relevant
entry, coefficient, mode and interval endpoint, not previews or flags.
All coefficient-trace identities and the complete anchor congruence
are checked independently. Original L115–L119 artifacts are untouched.

Modes k=47,...,68 have strictly positive whole-box lower endpoints.
Their least normalized lower endpoint is at k=47 and lies in
[426459,426460)/10^6. Modes k=0,...,46 all strictly straddle zero.
There are no strictly negative upper endpoints and no zero intervals.
The complete positive minimum fraction, constant-mode interval,
k=46 interval and empty failure list were inspected with the JSON
inspector's selected --full mode; every other load-bearing value was
consumed by the complete independent reconstruction.

Outcome: EXPLORATION, RESEARCH / REPRODUCTION, actual type calculation.
There is no whole-shell PSD verdict, no fixed negative direction,
no new useful lemma, and no argument change warranting PROOF or DAG
edits. The interval straddles terminate precisely this test, with no
midpoint sign, alternative enclosure, refinement, retuning or rerun
to rescue it. This spends one mathematical EXPLORATION turn. It does
not refute PSD or the product root, and changes neither the 955–957
bracket nor any earlier pass or stop. Full PSD, global uniqueness,
stronger distributions, measures, packing and RS realization remain open.

Proposed next direction is a different, global Johnson-kernel comparison
for the full included-anchor matrix, subject to REVIEW_REQUIRED source
assessment. No such bound or sufficiency theorem was derived or approved
in this turn; this is not a continuation of the stopped endpoint sum.
