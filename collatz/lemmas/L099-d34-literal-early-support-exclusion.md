# L099 — Literal d34 remaining early-support exclusion

## Hypotheses

Take L055's 25 indexed pairs, changing only H_0=6 and H_24=32670655.
All J_i are unchanged. Let b_i be nonnegative integers with
sum b_i=B=9250245 and put a_i=2+18b_i. Use literal indexed order.
Define

\[
\kappa=23/11,\quad G_i=(27/16)^{J_i}(3/2)^{H_i},\quad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Suppose real s_0,...,s_25 satisfy s_25=s_0, s_i>=540/11 and,
for every 0<=i<25,

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa,\qquad
4J_i\log2\le\log s_i+\log(11/4).
\tag{1}
\]

All logarithms are natural. No minimum, seed, H guard, integer-junction,
parity, valuation, realization or primitive-count premise is imposed.
All actual tails and cyclic endpoints, including closure with tail2,
remain in (1).

## Conclusion

Every such tuple has b_0=...=b_22=0. More precisely, after L098
eliminates recipient zero, a hypothetical first positive recipient
j in 1,...,22 violates its next input's own J guard with strict
left-minus-right difference greater than

\[
M_j\ge\frac{11554173905673}{500000000000}>231/10>0.
\tag{2}
\]

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-24-d34-remaining-early-recipients.md`.
It specializes inspected affine/analytic machinery; no originality beyond
the checked sources is asserted. The separate step442 critical audit
below found no defect in this scope.
Assembly with L097/C096a, actual-word transfer and universal eventual
descent are not conclusions here.

## Proof

### Audited imports and their scope

Apply L098 under the identical table, allocation and hypotheses (1).
Its conclusion and its proof (3), established before assuming b_0>=1,
give

\[
b_0=0,\qquad s_0<U:=20000000000.
\tag{3}
\]

That cap uses only L076 (6)–(7) with L084's independent residual data.
It applies at H_0=6>=3. The totals K=397573379 and N=630138897
include the full tail budget and all 25 cyclic endpoints. Thus the cap
is valid uniformly in all remaining allocations, including a_24=2.
No failed full support test or C/H test-allocation cap is imported.

Import L084 (2) and its independent all-member audit:

\[
\ell=693147180559/10^{12}<\log2,\quad
\log3<u=1098612288669/10^{12},\quad
\log(11/4)<v=1011600911679/10^{12}.
\tag{4}
\]

The positive exponential partial sum also gives

\[
U<\sum_{k=0}^{40}\frac{24^k}{k!}
=\frac{202750314819830504045671593478515759301}
       {7661655986496068058455078125}<e^{24}.
\tag{5}
\]

Hence log s_0<24. The finite U comparison is checked again below;
the analytic enclosures are audited imports, not newly certified here.

The assessed formal-affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section2 equations (2)–(4), Lemma2 pp.228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only finite real affine algebra is needed, without parity realization.
The imported cap uses [DLMF4.5.1](https://dlmf.nist.gov/4.5.E1),
log(1+x)<x for x>0. The saved enclosures and (5) reuse
[DLMF4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), with positive arguments
2,3,11/4 and24. Their primary hypotheses/proof cases were inspected
in the ready assessment; no general analytic or coding theorem needs
reproof. The work below matches the changed table to L076's
first-recipient proof (8). L086/L091 are precedents only; their
conclusions and L091's H>=7 prefix estimate are not imported at d34.

### Distinct prefix and recipient comparisons at H_0=6

Every possible preceding row 0,...,21 has H_i>=6. Thus its tail2
shifted offset satisfies

\[
\kappa-Q_i/4
=81/44-(3/11)(3/2)^{H_i}
\le81/44-(3/11)(3/2)^6=-81/64<0.
\tag{6}
\]

This explicitly includes row0 at H_0=6. Its failed tail20 test is
different: Q_0=2363/176<kappa*2^20 remains a preserved failure.
Every possible recipient row 1,...,22 instead has H_i>=72, so

\[
Q_i\ge(12/11)(3/2)^{72}+1
=\frac{67585198634830509743348335148655587}
       {12986507827891524337664}
>\frac{24117248}{11}=\kappa2^{20}.
\tag{7}
\]

These are distinct independently applicable O/S data subsets of L084,
not its failed full conjunction. Formula (6) is a direct specialization
of the tail2 expression at the actual minimum H; it does not extend
L091's stated range by citation.

Suppose some b_j>0 for 1<=j<=22 and choose the least such j.
By (3), b_i=0 for all i<j, including i=0. Hence those tails equal 2,
while integer b_j>=1 gives a_j>=20.

At each actual input put n_i=s_i-kappa>=47 and

\[
\eta_i=\kappa-(12/11)(16/27)^{J_i}
                   -(16/27)^{J_i}(2/3)^{H_i}.
\]

Since J_i>=2,H_i>=3, each power lies in (0,1) and the two
positive subtracted terms sum to less than 12/11+1=kappa.
Thus 0<eta_i<kappa and G_i s_i-Q_i=G_i(n_i+eta_i)>0.
This actual pre-tail positivity is established before changing any tail.
Using (6) for preceding rows and (7) only at the recipient gives

\[
s_{i+1}<(G_i/4)s_i\quad(i<j),\qquad
s_{j+1}\le2^{-20}(G_j s_j-Q_j)+\kappa
          <2^{-20}G_j s_j.
\tag{8}
\]

Both endpoint subtractions remain inside the tail division and kappa
outside until their signed offset is justified. These inequalities
bound actual positive junctions; no auxiliary trajectory or later-row
growth premise is used.

### All changed prefixes and their next own-input guards

Define the tail2 prefix exponents

\[
A_k=\sum_{i<k}(3J_i+H_i),\qquad
D_k=\sum_{i<k}(4J_i+H_i+2).
\]

Multiplying the positive bounds (8), then using (3)–(5), gives

\[
\log s_{j+1}<24+A_{j+1}\log3-(D_{j+1}+18)\log2.
\tag{9}
\]

Only the recipient comparison adds 18 to the tail2 exponent. Every
used prefix contains row0 and omits row24, so both A and D decrease
by exactly 34 relative to L055's original table. Neither original
witness heights nor a different table's conclusion is substituted.
Define

\[
M_j=(D_{j+1}+18+4J_{j+1})\ell-24-v-A_{j+1}u.
\tag{10}
\]

The coefficients A_(j+1) and D_(j+1)+18+4J_(j+1) are positive.
Consequently (4) and (9), with every amplified analytic error in its
outward direction, imply

\[
4J_{j+1}\log2-\log s_{j+1}-\log(11/4)>M_j.
\tag{11}
\]

The complete exact arithmetic is:

| j | A_(j+1) | D_(j+1) | 10^12 M_j |
|---:|---:|---:|---:|
|1|147|174|24209135543914|
|2|365|422|23154286726368|
|3|770|881|23909946914860|
|4|1531|1742|23108347811346|
|5|2960|3357|24556045630598|
|6|5651|6397|23769954725895|
|7|10716|12117|23884278145062|
|8|20255|22888|23913879402992|
|9|38224|43176|23781366630051|
|10|72075|81394|24775608608318|
|11|135851|153396|24381591719012|
|12|256005|289046|23283430278828|
|13|482380|544614|23362378680917|
|14|908885|1026119|25142816251395|
|15|1712453|1933310|23654780175660|
|16|3226433|3642521|24675892001117|
|17|6078890|6862807|25105692191626|
|18|11453143|12930077|25470005708779|
|19|21578659|24361290|23972470256174|
|20|40655931|45898596|24848522735164|
|21|76599028|86476591|23528141855852|
|22|144318678|162928755|25044612857374|

The minimum is M_4=11554173905673/500000000000>231/10.
Thus (11) strictly contradicts the non-strict own-input J guard
at row j+1 in every case. At j=1 the preceding prefix is just
row0 at tail2, and rejection is at input2. At j=22 the preceding
prefix ends at row21, the recipient is row22, and rejection is at
row23's own input. No comparison-offset sign is needed on rows23
or24. Their arbitrary allocations and the closing equation remain
in the full cap (3).

Every nonempty support among 1–22 has such a least index, so none
exists. With L098's b_0=0 this proves the conclusion over the full
integer allocation simplex. No remaining last-pair feasibility or
exclusion is inferred here.

### Exact evidence and limitations

Run `python3 scripts/postspell-word-count/certify_d34_remaining_early_recipients.py`.
Full evidence is
`scripts/postspell-word-count/d34-remaining-early-recipients-certificate.json`.
All 443 exact checks pass, with zero failures. The constructor rebuilds
the changed table from L055; checks invariant totals and cap; matches
the complete incoming prefixes, separate O/S offset operands and all 22
M_j to L084's audited d34 data; and checks both -34 shifts, positive
coefficients and strict margins. All 22 complete margin records, uniform
offset operands and exact exponential sum were inspected in full.
The program checks the complete relevant imported records rather than
inferring correctness from previews. The quantified proof is (3)–(11);
the finite checks are construction evidence, not independent audit.

Attempt032, all failed S/C/H data, both original d0 rational witnesses
and prior unfinished work remain valid. L097/C096a assembly, actual-word
transfer, other tables and universal eventual descent remain separate
unresolved tasks. No complete candidate resolution is claimed.

### Independent critical audit — 2026-10-24, step442

The unchanged SPECIALIZE assessment
`drafts/literature/2026-10-24-d34-early-support-critical-audit.md`
approved exactly this RESEARCH/REPRODUCTION proof audit. No defect was
found in (3)–(11) or the full-simplex conclusion. This secures an
existing local input; it supplies no new exclusion beyond L099 and no
claim of progress beyond the inspected source machinery. The precise
primary citations and analytic domains above are reused.

**Import before choosing a recipient.** L098 has exactly the same
table, literal chronology, integer budget, lower domain, cyclic
endpoints and own-input non-strict J guards as (1). Its audited cap
(3) precedes its assumption b_0>=1, so both s_0<U and b_0=0 are
available without circularity. The independent cap proof of L076
(6)–(7) needs H_i>=3, not H_i>=7 or a negative support offset.
The two H changes preserve K,N, and the complete tail sum is
50+18B. Every one of the 25 positive unshifted endpoint ratios
enters the cyclic product, including a closing edge with tail2.
Own-input guards for indices1–24 bound the remaining logarithmic
mass; J_1=15 is their least J. The residual is positive and its
strict cap is below U, as independently recomputed below. No
minimum, seed, H guard, integer-junction or growth assumption is used.

**Two signs and the quantified first-recipient step.** At every actual
input, n_i=s_i-kappa>=47 and 0<eta_i<kappa, so the pre-tail bracket
G_i(n_i+eta_i) is positive. This identity is checked before replacing
a tail. Once b_0=0 is known, every hypothetical nonempty support in
indices1–22 has a least index j. All preceding tails are exactly2;
integer b_j>=1 makes the recipient tail at least20. The preceding
rows have H>=6, giving the tail2 offset upper bound -81/64, including
row0. The recipients have H>=72, giving Q_i>kappa*2^20 and a strictly
negative tail20 offset. These different signs are precisely what (8)
uses. The positive row0 tail20 offset is never replaced by a negative
one, and its failed S test remains intact.

All inequalities in (8) concern actual positive junctions and have
positive multipliers. Multiplication therefore bounds the actual
s_(j+1), without constructing a trajectory whose lower domain would
need another proof. The only extra denominator exponent is the
recipient's18. For j=1, only row0 precedes the recipient and input2
is rejected. For j=22, preceding rows end at21 and row23 supplies
the next own-input guard. No offset sign or growth condition is
used on rows23/24; their arbitrary allocations and closure remain
covered by the imported cap. Every hypothetical early support has
one of these22 first indices, so the finite comparisons exhaust
the quantified argument rather than sample the allocation simplex.

**All amplified analytic errors and finite data.** Each used incoming
prefix contains row0 and omits row24. Thus both exponents decrease
by34 from L055, not just their difference. In (11) the coefficient
of log2 is positive and that of log3 is negative. Replacing log2
by ell, log3 by u, and log(11/4) by v therefore lowers the complete
left-minus-right margin, with strictness already supplied by (9).
This remains valid at the largest exponents; no rounding error is
discarded. Each M_j is strictly positive, contradicting precisely
the non-strict guard of outgoing row j+1 at that same input.

Run `python3 scripts/postspell-word-count/audit_d34_remaining_early_recipients.py`.
The auditor neither imports nor executes the constructor. A separate
transcription of L055's25 pairs is compared to the canonical table;
the two H changes, counts, residual and cap are rebuilt. Direct slice
sums reconstruct all25 incoming prefixes and both -34 shifts.
Exact powers at H=6 and H=72 reconstruct the uniform signs and all23
relevant bounded offset records. Integer common-denominator arithmetic
rebuilds all22 full margin records, including their actual next input
and J, and compares every row to both the written table and L084's
audited independent S data. The imported O operands are checked
separately. A factorial formula reconstructs all41 exponential terms,
their exact sum and its strict comparison with U. No failed C/H cap
or full O/S/C conjunction is invoked.

Full evidence is
`scripts/postspell-word-count/d34-remaining-early-recipients-audit-certificate.json`.
All319 comparison records pass with zero failures; this includes
bookkeeping and repeated data comparisons, not319 distinct mathematical
claims. All22 margins pass the required231/10 threshold; their minimum
is exactly11554173905673/500000000000 at j=4. Complete changed rows,
prefixes, cap, uniform sign operands and all22 margin records were
inspected in full. The program compares all relevant construction
data arrays in full and retains actual/required operands, provenance
and the unchanged construction hash. The443 stored construction checks
also pass an internal arithmetic/uniqueness check; their operands are
not separately regenerated by check name. Independent verification
rests on the freshly rebuilt complete mathematical data above, not
those stored success flags.

The analytic log/Lambda intervals remain audited L084 imports; this
audit checks their outward use and source identity, not their series
certification anew. The quantified reasoning is the proof reviewed
above, not an inference from finite checks. Attempt032, failed S/C/H
data, both d0 witnesses and prior unfinished work remain valid.
The direct inputs L055,L076,L084,L098 remain accurate; no argument
or dependency changes, so DAG and PROOF.md receive no status-only
edit. This canonical audit supersedes their earlier pending-audit
description of L099. Assembly with L097/C096a, actual-word transfer,
other tables and universal eventual descent remain unresolved.

## Mathlib

Full matching coverage is unchecked, not absent. Supporting real-log,
affine and rational-arithmetic results do not constitute a formalization
of this quantified specialization. No Lean proof is claimed.
