# L097 — Independent cyclic-order rigidity for d34

## Hypotheses

Take the 25 indexed pairs in L055's table, changing only H_0 to 6
and H_24 to 32670655. Every J_i is unchanged. Put r=25,
B=9250245 and kappa=23/11. Let b_i be nonnegative integers with
sum_i b_i=B and a_i=2+18b_i. Let pi be any permutation of
{0,...,24}. Suppose real s_0,...,s_25 satisfy s_25=s_0,
s_k>=540/11 and, for every 0<=k<25,

\[
s_{k+1}=2^{-a_{\pi(k)}}(G_{\pi(k)}s_k-Q_{\pi(k)})+\kappa,
\qquad G_i=(27/16)^{J_i}(3/2)^{H_i},\quad
Q_i=(12/11)(3/2)^{H_i}+1,
\tag{1}
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{2}
\]

All logarithms are natural. Every outgoing indexed pair keeps its
allocation and own input. No H guard, seed, prescribed minimum location,
integer junction, actual word, parity, residue, exact valuation or
primitive-count premise is imposed.

## Conclusion

Every feasible cyclic order is a rotation of 0,...,24 over the full
integer allocation simplex. More precisely, rotation to any smallest
designated junction makes pi the identity. Tails equal to 2 and
repeated junction values are included.

This is a local RESEARCH/REPRODUCTION application of L075, with L084's
independently audited d34 O data. It supplies no new ordering mechanism
or progress beyond those inputs. The separate step434 critical
applicability audit below found no defect. Feasibility, early-support elimination, assembly with the
literal last-pair exclusion, actual-word transfer and universal eventual
descent are not concluded.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-d34-independent-cyclic-order.md`.
Apply audited L075 independently of the failed full C077a sufficient-test
package. Here is the complete hypothesis matching; only the pair table,
not the witness premises or existence conclusion, is imported from L055.

**Table and totals, L075 (1).** This is precisely L084's member d=34.
All J_i are integers, strictly increasing from J_0=8; H_0=6 and
every other H_i>=72, so H_i>=3. The opposite H changes preserve
sum J_i=66061058 and sum H_i=199390205. L084's completed step337
all-member reconstruction certifies

\[
K=\sum_i(3J_i+H_i)=397573379,\quad
N=\sum_i(4J_i+H_i)+2r+18B=630138897.
\tag{3}
\]

In particular sum_i a_i=166504460 for every allowed allocation,
independently of its order. These are L075's same K,N, not counts
inferred from a proposed real tuple or from primitive-orbit premises.

**Independent analytic tests, L075 (2).** Use exactly L084's O constants

\[
\lambda=1323/12500000000000,\quad T=27,\quad
\ell=693147180559/10^{12},\quad
u=1098612288669/10^{12},\quad v=2.
\tag{4}
\]

L084's completed analytic audit proves 0<lambda<Lambda=N log2-K log3,
0<ell<log2, log3<u and log(11/4)<2, retaining all amplified errors.
Its independently certified O cap is

\[
U=23r/(11\lambda)+23/11
=7187500000030429/14553
<500000000000<P(27)<\exp(27),\qquad
P(27)=\sum_{j=0}^{40}27^j/j!.
\tag{5}
\]

Thus all of L075 (2) holds. Neither the failed S datum nor the failed
fixed C/H caps is used; (5) is the distinct independent O cap.

**All tail-2 offsets, L075 (3).** The audited d34 O records include
all 25 rows. At row0 the exact offset is
81/44-(3/11)(3/2)^6=-81/64<0. At every row i=1,...,24,
H_i>=72, and the decreasing offset expression has upper bound

\[
\frac{81}{44}-\frac3{11}(3/2)^{72}
=-\frac{67585198634721895314242333308740579}
        {51946031311566097350656}<0.
\tag{6}
\]

This is exact at row1 and an upper enclosure elsewhere. These are
exactly L075's tail-2 offsets, including changed row24; no sign of an
arbitrary-tail offset or of the failed tail-20 support datum is presumed.

**Every prefix and displacement margin, L075 (4)–(5).** Let
A_k=sum_(i<k)(3J_i+H_i) and D_k=sum_(i<k)(4J_i+H_i+2),
for 0<=k<=23. L084's completed all-member O reconstruction certifies
these precise d34 prefixes and all 24 margins

\[
M_k=4J_{k+1}\ell-27-2-A_k u+D_k\ell>0,
\qquad \min_{0\le k\le23}M_k
=\frac{629441541677}{50000000000}>12.58.
\tag{7}
\]

The complete records include A_0=D_0=0, A_1=30,D_1=40 and
A_23=144318678,D_23=162928755. For every nonempty prefix both
exponents are those of d1 minus 33: row0 is included and row24
is excluded. The audited general prefix identities and all-member
margin reconstruction, rather than L084's d<=4 display alone,
justify (7). The k=0 test is unchanged; the nonempty margin shift
is +33(u-ell), with its positive sign already checked in L084.
Increasing J and ell>0 cover every larger displaced row through
L075's criterion, including the final possible displacement k=23.

The complete relevant evidence is `/tables/33/O` in
`scripts/postspell-word-count/h-transfer-family-certificate.json`
and `/reconstructed_tables/33/O` in
`scripts/postspell-word-count/h-transfer-family-audit-certificate.json`.
Both complete objects were inspected, including all 25 offsets and
24 margins. The mathematical verification imported here is L084's
completed analytic/all-member O audit; no summary flag, preview,
new script or rerun is offered as an independent verification.

**Tuple conditions, L075 (6)–(7).** Our indexed nonnegative integer
allocation, total B, tails a_i, arbitrary permutation, all 25 exact
endpoints (1), lower domains, cyclic closing equality and non-strict
own-input J guards (2) are literally L075's tuple conditions on this
same table. Certificate data do not assert that such a tuple exists.
All hypotheses of L075 now match, so its conclusion gives the asserted
cyclic-order rigidity.

L075 retains all actual allocated tails in the full cyclic product,
including tail 2, and makes comparisons only at actual lower-domain
inputs. Its rotation to a minimum carries each outgoing row, tail and
guard with its input. The old closing edge remains among the rotated
edges; the new closing edge is the old edge immediately before the
chosen minimum. Both cuts remain, also when they coincide, and repeated
values remain separate occurrences. No minimum at indexed row0 is
assumed and no ordering proof is reproved here.

For precise upstream citations, L075 already specializes the formal
real affine identity of Halbeisen–Hungerbuehler, *Optimal bounds for the
length of rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239, section 2, equations (2)–(4), Lemma 2,
pp. 228–229 ([primary paper](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf)).
Its finite integer exponents and nonzero denominator match (3)–(5);
no integer itinerary realization is imported. The positive-real analytic
inputs and certified remainders are reused through L075/L084 from NIST
DLMF [4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.2.19](https://dlmf.nist.gov/4.2.E19) and
[4.6.4](https://dlmf.nist.gov/4.6.E4). No new source retrieval,
current-release check or general affine reproof is needed.

L094 covers d6–33 only and is a method comparison, not a d34 premise.
Attempt032's failed full conjunction and both d0 rational witnesses
remain valid. This independent O application does not repair that
package or establish early-support elimination. A later exclusion could
use this order reduction together with separately proved early-support
elimination and the literal last-pair exclusion; those remain separate
work. Arbitrary tables, unrestricted cycles, entry, divergence and
universal eventual descent remain unresolved.

### Independent critical applicability audit — 2026-10-23, step434

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-d34-independent-order-critical-audit.md`.
This RESEARCH/REPRODUCTION proof audit finds no defect in the application
(1)–(7), within its exact real endpoint/domain/J scope. It validates an
existing local input, with no new ordering mechanism, table exclusion or
progress beyond the imported results. The source coverage is reused;
no external search, certificate tuning or general theorem reproof occurred.

**Table and independent analytic premises.** Read L075's full statement,
proof and completed step281 audit, L084's complete step337 audit and
analytic construction, and L055's complete pair table. Read all 25 d34
rows at `/reconstructed_tables/33/rows` in the existing family audit
certificate. They change exactly H_0=40-34=6 and
H_24=32670621+34=32670655. The unchanged increasing integer J values
start at 8; H_0=6 and every other H is at least 72. Thus all L075
table domains hold. The opposite changes leave sum H and sum J intact;
the exact totals (3) follow with 2r+18B=166504460. The complete
`/reconstructed_tables/33/counts` and `/reconstructed_tables/33/Lambda_interval`
match those operands. L055 is used for its table only, not its witness,
minimum, H/seed conditions or primitive-count assumptions.

L084's completed analytic proof is the imported certification of the
logarithm sums and remainder bounds, rather than an independently rerun
series calculation in this audit. Its positive arguments 2,3,11/4 have
z=1/3,1/2,7/15; the positive 100-term sums and
2z^201/[201(1-z^2)] remainders give outward bounds. In Lambda, the
positive coefficients require N times the lower log2 endpoint minus K
times the upper log3 endpoint for the lower bound. Thus the small
positive Lambda is certified with its amplified errors, not by the
coarse ell,u grid. The same table totals make that certification apply
unchanged here.

Read the complete exact O comparisons at
`/reconstructed_tables/33/checks/85`, `/87`, `/88`, `/89` and `/107`
(the last four abbreviate that same checks prefix). Their actual and
required operands, differences and directions certify respectively
lambda below the lower Lambda endpoint, ell below the log2 lower sum,
u above the log3 upper bound, 2 above the log(11/4) upper bound, and
U below the exp(27) lower sum. These are L075 (2) with the constants
(4), including v=2; the tighter S/C/H v is not substituted. The complete
`/exp_lower/27` value is

\[
P(27)=\frac{1112436109266660239093546627471481746956608769015849}
 {2106019961293006716393905717248000000000}.
\]

Its positive omitted terms give P(27)<exp(27). The inspected fractions
retain U<500000000000<P(27), as required in (5). No C/H cap or failed
S test enters. The precise upstream affine and DLMF citations above
retain their finite-word/nonzero-denominator and positive-real domains;
no integer itinerary theorem or scalar-ordering optimizer is imported.

**Complete finite O evidence.** Read, with `--full`, both `/tables/33/O`
in `scripts/postspell-word-count/h-transfer-family-certificate.json`
and `/reconstructed_tables/33/O` in
`scripts/postspell-word-count/h-transfer-family-audit-certificate.json`.
All constants, 25 offset records and 24 margin records agree. These
complete objects, together with L084's completed all-member reconstruction,
are the evidence imported here; a preview or PASS flag alone is not used
as proof. No constructor or audit program was rerun and no new numerical
certificate or mathematical script was written.

At row0 the exact tail-2 offset is -81/64. At rows1–24 the recorded
H_floor=72 is at most the actual H. Since (3/2)^H increases with H,
the negative coefficient makes (6) an upper bound on the actual offset.
It is exact at row1 and strictly negative, hence proves all 24 remaining
signs, including the changed row24. This matches L075 (3), which never
requires an arbitrary-tail offset sign. In particular it does not reuse
the failed tail-20 support test.

Every margin record has k=0,...,23 and displaced row k+1, with the
same A_k,D_k and rational expression as L075 (4)–(5). The empty prefix
is zero; each nonempty prefix includes changed row0 and omits row24.
Relative to d1 both exponents decrease by 33, so the margin change is
+33(u-ell)>0; relative to d0 they decrease by 34. These directions
match the full records, including (A_1,D_1)=(30,40) and
(A_23,D_23)=(144318678,162928755). The final record is
40328783789098646307/10^12. All 24 margins are positive; their
minimum is the k=0 value 629441541677/50000000000>12.58.
This uses the complete d34 reconstruction, not L084's d<=4 display.
For any larger displaced row j>k, increasing J and ell>0 give
M_(k,j)>=M_k. Thus the 24 weakest tests cover all 300 eligible pairs.

**Tuple, strictness and both cuts.** The b_i are indexed by outgoing
row, are nonnegative integers of sum B, and give exactly a_i=2+18b_i.
The arbitrary permutation, all 25 lower domains, all endpoints including
s_25=s_0, and every non-strict own-input J guard match L075 (6)–(7)
literally. Subtracting kappa gives n_k>=47. L075's positive eta_i and
the full cyclic product retain every actual allocated tail, even tail 2,
and bound any designated minimum by log s_min<27. There is no premise
that indexed row0 initially carries that minimum.

For a minimum occurrence q, let x_k=s_((q+k) mod25) and
rho(k)=pi((q+k) mod25), with x_25=x_0. Keep b indexed by row.
The outgoing row rho(k), its tail and its J guard stay at x_k. The
old edge24 becomes rotated edge (24-q) mod25; the new closing edge
is old edge (q-1) mod25. This checks all endpoints, including q=0
when the cuts coincide and q=24. Repeated values are separate
occurrences and the reasoning applies to any chosen minimum occurrence.

L075 compares tails at actual inputs where G_i s-Q_i>0, and uses
only the certified negative tail-2 offset for strictness. Before a
first displacement the actual rows are the literal prefix, so its
upper log bound uses precisely these A_k,D_k even with arbitrary
allocated tails. A first displaced position is at most 23 and its
row is larger than that position. The empty-prefix case uses the
strict minimum bound; the final case uses the checked k=23 prefix
and row24 test. The strictly positive difference in L075 (15)
contradicts the same row's non-strict own-input J guard. Undoing the
rotation gives exactly L097's conclusion, without H/seed, minimum-location,
integer-junction, primitive, feasibility or realization assumptions.

The scope comparison checked histories431/432/406 and Attempt032;
L094's d6–33 audit is a methodological comparison, not a d34 premise.
Attempt032's failed full package and both d0 witnesses are unchanged.
The direct inputs remain L055 (table), L075 and L084. No argument or
dependency changed, so PROOF.md and DAG.md remain unchanged; this audit
supersedes their pending-audit wording for L097 only. Early-support
elimination, assembly with the last-pair exclusion, broader actual-word
transfer and universal eventual descent remain unresolved. Full matching
Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage for this simultaneous cyclic endpoint/own-input
guard statement remains unchecked. Supporting finite-product and
positive-real logarithm facts are not a matching theorem. Unknown
coverage is not evidence of absence; no formalization claim is made.
