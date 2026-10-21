# L086 — d=5 literal early-support exclusion

## Hypotheses

Take L055's 25 indexed pairs, changing only H_0=35 and
H_24=32670626. In particular every J is unchanged. Put B=9250245,
kappa=23/11, G_i=(27/16)^{J_i}(3/2)^{H_i} and
Q_i=(12/11)(3/2)^{H_i}+1. Let b_i>=0 be integers summing to B,
and a_i=2+18b_i. Suppose real s_0,...,s_25 satisfy s_25=s_0,
s_i>=540/11 and, in literal indexed order, for every 0<=i<25,

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa,\qquad
4J_i\log2\le\log s_i+\log(11/4).
\tag{1}
\]

These are exactly L085's endpoint/domain/non-strict own-input J
hypotheses, using C077a's definitions only. Every endpoint, including
closure and a possible closing tail 2, is retained. There is no minimum,
seed, H guard, integer-junction, parity, valuation, actual-word or
primitive-count premise.

## Conclusion

Every such tuple has b_0=...=b_22=0. More precisely, for each possible
first positive recipient j=1,...,22, its next input's own J guard has
left-minus-right difference strictly greater than a certified M_j>11.34.
L085 already excludes recipient zero under exactly (1).

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-19-d5-remaining-early-recipients.md`.
It establishes a finite changed-table specialization of the inspected
first-recipient mechanism, with no originality claim beyond the sources
checked. The separate critical audit below found no defect. No cyclic-order reduction,
last-pair verdict, feasibility, integrality or actual-word exclusion is
proved. Universal eventual descent remains unresolved.

## Proof

### Imported cap, analytic inputs and exact scope

Apply audited L085 with the identical table, allocation simplex and all
of (1). It gives

\[
b_0=0,\qquad s_0<U:=20000000000.
\tag{2}
\]

Its cap uses every allocation and cyclic endpoint, including closure;
it requires no offset sign or minimum location. In particular later
tails remain arbitrary. Do not invoke L076's full theorem or C077a's
reduction, since the row0 tail-20 prerequisite fails.

Import L084 (2)'s independently audited analytic operands

\[
\ell=693147180559/10^{12}<\log2,\quad
\log3<u=1098612288669/10^{12},\quad
\log(11/4)<v=1011600911679/10^{12}.
\tag{3}
\]

They are table-independent. L084's degree-40 positive exponential sum
P(24)=sum_(k=0)^40 24^k/k! satisfies U<P(24)<exp(24).
Thus (2) gives log s_0<24. The exact finite U<P(24) comparison is
also reproduced in the certificate below; no logarithm of an unknown
root is approximated.

The upstream formal affine algebra is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only real finite-word algebra is used. The actual parameters are integers
specifying finite words, without any realization assumption. The analytic
operands reuse the inspected positive-real logarithm and exponential
series, [DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), with arguments 2,3,11/4
and positive 24. L085's cap already justifies its positive-domain use of
[DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1).
No coding or analytic theorem is reproved. Specialize L076's audited
first-recipient subargument, equations (8) and its subsequent guard
comparison. Its full theorem is unavailable here, so the needed weaker
prefix and recipient hypotheses must be justified separately below;
this is the reason for spelling out the changed-prefix application.

### Prefix tail 2 and recipient tail 20 are different tests

For any row the shifted tail-2 offset is exactly

\[
\kappa-Q_i/4=81/44-(3/11)(3/2)^{H_i}.
\]

Every potential prefix row 0,...,21 has H_i>=35. Since 3/2>1,
each such offset is at most

\[
81/44-(3/11)(3/2)^{35}
=-150093939512297169/377957122048<0.
\tag{4}
\]

This includes row0, where its tail-20 offset is instead positive.
Indeed its failed old datum remains
Q_0=150094729786279633/94489280512<kappa*2^{20}.
No replacement or repair of this datum is asserted.

Every possible recipient row 1,...,22 has H_i>=72. Consequently

\[
Q_i\ge (12/11)(3/2)^{72}+1
=67585198634830509743348335148655587/12986507827891524337664
>24117248/11=\kappa2^{20}.
\tag{5}
\]

Thus their tail-20 offsets are strictly negative. Equations (4) and (5)
are independently applicable subsets of L084's O and S data, not the
failed conjunction of all S data.

### First positive recipient and the next own-input guard

Suppose some b_j>0 with 1<=j<=22, and take the least such j.
By (2), all b_i for i<j vanish, including b_0. Hence a_i=2 for
i<j, while integrality gives a_j>=20.

At each actual input put n_i=s_i-kappa>=47 and

\[
\eta_i=\kappa-(12/11)(16/27)^{J_i}
                    -(16/27)^{J_i}(2/3)^{H_i}.
\]

As in L085, J_i>=2,H_i>=3 imply 0<eta_i<kappa, since each
base lies in (0,1). Therefore G_i s_i-Q_i=G_i(n_i+eta_i)>0.
This sign is established at the actual input before changing a tail.
Using (4) on the preceding rows and (5) only at the recipient gives

\[
s_{i+1}<(G_i/4)s_i\quad(i<j),\qquad
s_{j+1}\le2^{-20}(G_j s_j-Q_j)+\kappa
          <2^{-20}G_j s_j.
\tag{6}
\]

No auxiliary trajectory or growth premise is used. All actual junctions
and multiplying factors are positive, so the bounds multiply and admit
logarithms. With the literal tail-2 exponents

\[
A_k=\sum_{i<k}(3J_i+H_i),\qquad
D_k=\sum_{i<k}(4J_i+H_i+2),
\]

(2) and (6) imply

\[
\log s_{j+1}<24+A_{j+1}\log3-(D_{j+1}+18)\log2.
\tag{7}
\]

The extra 18 changes only the recipient's comparison tail from 2 to 20.
For j=1 the prefix is exactly row0 at tail 2. For j=22 the prefix
ends at row21, the recipient is row22 and the rejected next guard is
row23's; no tail or offset premise is needed on rows23 or24.

Define the exact rational number

\[
M_j=(D_{j+1}+18+4J_{j+1})\ell-24-v-A_{j+1}u.
\tag{8}
\]

All coefficients A_(j+1) and D_(j+1)+18+4J_(j+1) are positive.
Thus the enclosure directions in (3) and (7) give

\[
4J_{j+1}\log2-\log s_{j+1}-\log(11/4)>M_j.
\tag{9}
\]

For each 1<=k<=23, the incoming prefix contains row0 but not row24.
Relative to L055, both A_k and D_k therefore decrease by exactly 5.
The opposite change at row24 retains the total K,N and full closure,
but does not occur in these prefixes. These are exactly L084's d=5
prefixes; original-table witness heights or margins are not transferred.
The complete arithmetic table below verifies (8).

| j | A_(j+1) | D_(j+1) | 10^12 M_j |
|---:|---:|---:|---:|
|1|176|203|12450647408724|
|2|394|451|11395798591178|
|3|799|910|12151458779670|
|4|1560|1771|11349859676156|
|5|2989|3386|12797557495408|
|6|5680|6426|12011466590705|
|7|10745|12146|12125790009872|
|8|20284|22917|12155391267802|
|9|38253|43205|12022878494861|
|10|72104|81423|13017120473128|
|11|135880|153425|12623103583822|
|12|256034|289075|11524942143638|
|13|482409|544643|11603890545727|
|14|908914|1026148|13384328116205|
|15|1712482|1933339|11896292040470|
|16|3226462|3642550|12917403865927|
|17|6078919|6862836|13347204056436|
|18|11453172|12930106|13711517573589|
|19|21578688|24361319|12213982120984|
|20|40655960|45898625|13090034599974|
|21|76599057|86476620|11769653720662|
|22|144318707|162928784|13286124722184|

Their minimum is

\[
M_4=2837464919039/250000000000>1134/100>0.
\tag{10}
\]

Hence (9) strictly contradicts the non-strict own-input guard at row
j+1 for every possible first recipient. Such a first recipient does
not exist, proving b_1=...=b_22=0; (2) also gives b_0=0.
All later allocations and the closing tail were retained in the cap
and are otherwise unrestricted. Nothing is asserted about existence
or guard satisfaction of the remaining last-pair allocations.

### Finite verification and qualifications

Run `python3 scripts/postspell-word-count/certify_d5_remaining_early_recipients.py`.
The complete certificate is
`scripts/postspell-word-count/d5-remaining-early-recipients-certificate.json`.
All 195 checks pass, with zero failures. It stores the complete changed
table, incoming exponents, all 22 margins, both uniform offset operands,
the retained failed row0 datum, cap operands and all 41 exponential
terms. It reconstructs and matches every needed L084 d5 prefix/margin
and verifies both -5 prefix shifts; source hashes identify the inputs.
Every relevant margin and offset was inspected in full. The quantified
proof is (2)–(9); finite verification is not an independent critical audit.
Analytic enclosures are explicitly imported, not newly certified here.

Both original-table rational witnesses and Attempts 026–032 remain valid.
In particular L084's failed full support criterion is unchanged.
The conclusion concerns only this literal necessary subsystem, without
any arbitrary-order, last-pair, H/seed, arithmetic, actual-word or
universal eventual-descent consequence. The construction checks alone
are distinct from the separate critical audit below.

### Independent critical audit — 2026-10-19, step 349

The prior SPECIALIZE assessment
`drafts/literature/2026-10-19-d5-literal-early-support-critical-audit.md`
licenses this RESEARCH/REPRODUCTION proof audit. No defect was found
in the stated literal endpoint/domain/J scope. This verifies the existing
local input, without adding an exclusion family or claiming progress
beyond the inspected affine and analytic source machinery. The source
citations and their real-domain qualifications above are unchanged.

**Cap quantifiers and support zero.** L085's hypotheses match (1)
exactly, including the integer simplex, both changed H values, every
lower-domain input, every own-input J guard and the closing endpoint.
Its conclusion b_0=0 and proof (4)'s cap hold for every such tuple.
In particular the cap precedes its assumption b_0>=1; importing it
after concluding b_0=0 is legitimate. Subtracting kappa gives
n_(i+1)=2^(-a_i)G_i(n_i+eta_i), with 0<eta_i<kappa and n_i>=47.
The 25 positive ratios telescope only after including closure. The
fixed sum of all tails yields exactly K=397573379,N=630138897,
including a_24=2 when all budget is elsewhere. For i>=1 the own J
guard gives n_i>=(4*2^60-23)/11; the strict positive-real log
inequality gives the residual and cap in (2). No minimum, offset sign,
growth of later rows, or H/seed assumption enters this import.

**Separate offsets and first support.** The preceding rows of a first
recipient j in [1,22] are precisely [0,j-1], all with actual tail 2
because L085 supplies b_0=0. Their H values are at least 35, so (4)
applies, even at row0. Only row j uses the tail-20 offset test; every
such recipient has H_j>=72, giving (5). The positive row0 tail-20
offset and Attempt 032's failed full criterion remain unchanged.
At an actual lower-domain input, eta_i>0 gives G_i s_i-Q_i>0
before replacing a_j by 20. Consequently the tail comparison has
the correct direction even when a_j>20; both multiplier comparisons
in (6) are strict. They bound actual positive junctions, rather than
constructing an auxiliary orbit whose domain would need checking.

**Every prefix, guard and boundary.** Direct sums reconstruct A_k,D_k
for all k=0,...,25. For each used k=j+1 in [2,23], row0 contributes
-5 to each exponent and row24 is absent, so both changes from L055
are exactly -5. The comparison tail adds precisely 18 to D_k.
The next guard uses J_(j+1) at s_(j+1), not the recipient's J_j.
At j=1, only row0 precedes row1 and the failed guard is at input2;
at j=22, rows0–21 precede row22 and the failed guard is at input23.
No comparison offset or growth property is required on rows23 or24.
Those rows and their arbitrary tails are still present in the cap.
Each nonempty early support has one of these first indices. All 22
strict inequalities in (9) contradict the respective non-strict guard,
so their combination with L085 proves the entire stated conclusion.

**Independent finite and analytic verification.** Run
`python3 scripts/postspell-word-count/audit_d5_early_support.py`.
It neither imports nor executes the constructor. It separately transcribes
the full pair table, checks it against L055 and the construction, and
uses direct prefix sums to reconstruct all incoming exponents and all
22 margin records. It also checks the complete printed table above.
Every operand, relation, difference and verdict in all 195 construction
comparisons is reconstructed; integer cross products determine signs.
The source hashes, all constants, both offset operands and failed datum,
all 41 exponential terms, and full summary match. All 235 independent
checks pass with zero failures. These are verification counts, not
separate mathematical advances. The construction certificate is unchanged.

For an independent check of the imported analytic operands, use the
already assessed DLMF 4.6.4 positive-real specialization. For
t=2,3,11/4 and z=(t-1)/(t+1) in (0,1), let

\[
P_t=2\sum_{m=0}^{99}\frac{z^{2m+1}}{2m+1},\qquad
R_t=\frac{2z^{201}}{201(1-z^2)}.
\]

Positivity of the omitted terms gives P_t<log t. Replacing their
denominators by 201 and summing the geometric series gives
log t<P_t+R_t, strictly since later denominators exceed 201.
This is the previously justified remainder, not a new analytic input.
All three intervals lie strictly on the required side of ell,u,v.
Opposite interval endpoints for N log2-K log3 independently verify
both imported Lambda bounds with their full amplified errors.

For each recipient put C=D_(j+1)+18+4J_(j+1)>0 and A=A_(j+1)>0.
The exact logarithmic rejection bound before outward replacement is
X=C log2-24-log(11/4)-A log3. Its difference from (8) is

\[
X-M_j=C(\log2-\ell)+A(u-\log3)+(v-\log(11/4))>0.
\]

The program encloses every summand using the full rational intervals,
checks both resulting endpoints against X's direct enclosure, and
finds for all 22 rows

\[
0<X-M_j<344718069/10^{12}.
\]

Thus large prefix coefficients introduce no hidden sign reversal or
rounding assumption. The minimum rational rejection remains exactly
M_4=2837464919039/250000000000>11.34. The positive exponential
recurrence reconstructs all terms through degree40 at 24 and verifies
their sum exceeds U, so log s_0<24 also retains its strict direction.

The complete evidence is
`scripts/postspell-word-count/d5-early-support-audit-certificate.json`:
all reconstructed construction records, full table/prefix/margin data,
offset and cap operands, 300 logarithm terms, three remainders, both
Lambda endpoints, and both amplified-error endpoints for every recipient.
The complete certificate is verified by the independent program, not
by a preview or a stored pass flag. Full check, constant and margin
records were also inspected. Both original witnesses and Attempts
026–032 remain valid. No order, last-pair, survivor/integer exclusion,
actual-word transfer or universal descent has been added. Direct inputs
and the mathematical argument are unchanged, so DAG.md and PROOF.md
are unchanged; this canonical audit supersedes their pending-audit
wording for L086.

## Mathlib

Full matching coverage is unchecked, not absent. Supporting real-log,
affine and rational-arithmetic facts do not establish this complete
changed-table specialization. No Lean proof is claimed.
