# L091 — Uniform literal early-support exclusion for d=6,...,33

## Hypotheses

Let d be an integer with 6<=d<=33. Take L055's 25 indexed pairs,
changing only H_0=40-d and H_24=32670621+d; every J is unchanged.
Let b_i be nonnegative integers with sum b_i=B=9250245, and set
a_i=2+18b_i. Use literal indexed order. Set

\[
\kappa=23/11,\qquad G_i=(27/16)^{J_i}(3/2)^{H_i},\qquad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Suppose real s_0,...,s_25 satisfy s_25=s_0, s_i>=540/11 and,
for every 0<=i<25,

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa,\qquad
4J_i\log2\le\log s_i+\log(11/4).
\tag{1}
\]

All logarithms are natural. Every allocated tail and endpoint, including
closure when its tail is 2, is retained. No minimum, seed, H guard,
integer-junction, parity, valuation, actual-word or primitive-count
premise is imposed. C077a supplies definitions only.

## Conclusion

Every such tuple has b_0=...=b_22=0. More precisely, each hypothetical
first positive recipient j in [1,22] forces its next input's own J
guard to have left-minus-right difference strictly greater than

\[
M_j(d)\ge\frac{5877662392133}{500000000000}>11.75>0.
\tag{2}
\]

L090 already supplies recipient zero. This is a local
RESEARCH/REPRODUCTION specialization under the prior SPECIALIZE
assessment `drafts/literature/2026-10-20-uniform-remaining-early-recipients.md`.
It establishes a changed-range consequence of inspected machinery,
without an originality claim. The separate critical audit below found no
defect within this precise scope.
It supplies no cyclic-order reduction, last-pair or survivor verdict,
actual-word transfer, unrestricted cycle exclusion or universal descent.

## Proof

### Imported cap and standard inputs

Apply audited L090 under exactly (1). Its conclusion and proof (3) give

\[
b_0=0,\qquad s_0<U:=20000000000.
\tag{3}
\]

The cap is established before its assumption b_0>=1. It holds over
the full allocation simplex, uses every cyclic endpoint and has no
offset-sign premise. It remains available after concluding b_0=0.
Specifically, the opposite H changes preserve K=397573379 and
N=630138897; all positive unshifted endpoint ratios telescope, including
closure. With lambda=10584/10^14 and E=552/(4*2^60-23), that proof
gives 0<lambda-E and s_0<kappa/(lambda-E)+kappa<U.
No C/H test-allocation cap, minimum location or later-row growth enters.

Import L084 (2)'s audited, table-independent operands

\[
\ell=693147180559/10^{12}<\log2,\qquad
\log3<u=1098612288669/10^{12},\qquad
\log(11/4)<v=1011600911679/10^{12}.
\tag{4}
\]

The same source supplies U<P(24)<exp(24), where
P(24)=sum_(k=0)^40 24^k/k!. The exact finite U<P(24) comparison
is also reproduced below. Thus (3) implies log s_0<24.

The formal affine source is Halbeisen–Hungerbuehler, *Optimal bounds
for the length of rational Collatz cycles*, Acta Arithmetica 78 (1997),
227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only finite real affine algebra is imported, without parity realization.
The cap uses [DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
log(1+x)<x for x>0; (4) and the exponential lower sum reuse
[DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), at positive real arguments
2,3,11/4 and 24. The prior assessment already inspected these proof
cases; no analytic or coding theorem is reproved.

Specialize L076's first-recipient proof (8) as separated in audited
L086 (4)–(9). L086's theorem remains d5 only. L076's full theorem
and C077a's full conjunction remain unavailable because the row0
tail-20 test fails. The following argument justifies precisely the
changed prefix and recipient hypotheses required here.

### Separate prefix and recipient offsets

Every potential preceding row 0,...,21 has H_i>=7, uniformly over
the approved range. Its tail-2 shifted offset therefore obeys

\[
\kappa-Q_i/4
=81/44-(3/11)(3/2)^{H_i}
\le81/44-(3/11)(3/2)^7=-3969/1408<0.
\tag{5}
\]

This includes row0; its tail-20 offset is a different quantity.
Every possible recipient row 1,...,22 instead has H_i>=72, giving

\[
Q_i\ge(12/11)(3/2)^{72}+1
=\frac{67585198634830509743348335148655587}
        {12986507827891524337664}
>\frac{24117248}{11}=\kappa2^{20}.
\tag{6}
\]

These are separate subsets of the audited L084 O/S data. Row0's
failed tail-20 datum is preserved for every d>=6, since its Q_0 is
smaller than the already failed d5 operand. No full S conclusion is
imported and no stopped constant is tuned.

Suppose some b_j>0 for 1<=j<=22, and choose the least such j.
By (3), b_i=0 for every i<j, including zero, so those tails equal 2.
The nonnegative integer allocation gives a_j>=20.

At each actual lower-domain input put n_i=s_i-kappa>=47 and

\[
\eta_i=\kappa-(12/11)(16/27)^{J_i}
                    -(16/27)^{J_i}(2/3)^{H_i}.
\]

Since J_i>=2,H_i>=3, both bases lie in (0,1); the positive
subtracted terms sum to less than 12/11+1=kappa. Thus
0<eta_i<kappa and G_i s_i-Q_i=G_i(n_i+eta_i)>0.
Establish this sign before replacing the actual recipient's tail.
Equations (5)–(6) then give

\[
s_{i+1}<(G_i/4)s_i\quad(i<j),\qquad
s_{j+1}\le2^{-20}(G_j s_j-Q_j)+\kappa
          <2^{-20}G_j s_j.
\tag{7}
\]

These are bounds on actual positive junctions, not a constructed
comparison trajectory. No domain or growth assumption on auxiliary
inputs or later rows is needed.

### Changed prefixes and strict next-input comparisons

Define the literal tail-2 exponents

\[
A_k(d)=\sum_{i<k}(3J_i+H_i),\qquad
D_k(d)=\sum_{i<k}(4J_i+H_i+2).
\]

Multiplying (7), using (3) and taking logarithms gives

\[
\log s_{j+1}<24+A_{j+1}(d)\log3
                    -(D_{j+1}(d)+18)\log2.
\tag{8}
\]

Only the recipient comparison tail adds 18. For j=1 the preceding
prefix is exactly row0 with tail 2. For j=22 it ends at row21,
and the contradiction below is with outgoing row23 at its own input.
Rows23 and24 require no comparison-offset signs; their arbitrary tails
remain in the cap and closing product.

Put

\[
M_j(d)=(D_{j+1}(d)+18+4J_{j+1})\ell-24-v-A_{j+1}(d)u.
\tag{9}
\]

Both coefficients of the logarithm enclosures are positive. Equations
(4) and (8) therefore imply, with all amplified errors in the stated
outward directions,

\[
4J_{j+1}\log2-\log s_{j+1}-\log(11/4)>M_j(d).
\tag{10}
\]

Each used incoming prefix contains row0 and omits row24. Relative
to L055 both A and D decrease by exactly d. Relative to d5 both
decrease by d-5. Consequently

\[
M_j(d)=M_j(5)+(d-5)(u-\ell),\qquad
u-\ell=405465108110/10^{12}>0.
\tag{11}
\]

Thus every margin increases with d, and the uniform minimum is at
d=6. This is an exact coefficient identity, not inference from sampling.
The complete d6 arithmetic is:

| j | A_(j+1)(6) | D_(j+1)(6) | 10^12 M_j(6) |
|---:|---:|---:|---:|
|1|175|202|12856112516834|
|2|393|450|11801263699288|
|3|798|909|12556923887780|
|4|1559|1770|11755324784266|
|5|2988|3385|13203022603518|
|6|5679|6425|12416931698815|
|7|10744|12145|12531255117982|
|8|20283|22916|12560856375912|
|9|38252|43204|12428343602971|
|10|72103|81422|13422585581238|
|11|135879|153424|13028568691932|
|12|256033|289074|11930407251748|
|13|482408|544642|12009355653837|
|14|908913|1026147|13789793224315|
|15|1712481|1933338|12301757148580|
|16|3226461|3642549|13322868974037|
|17|6078918|6862835|13752669164546|
|18|11453171|12930105|14116982681699|
|19|21578687|24361318|12619447229094|
|20|40655959|45898624|13495499708084|
|21|76599056|86476619|12175118828772|
|22|144318706|162928783|13691589830294|

The smallest value is M_4(6)=5877662392133/500000000000>11.75.
Equations (10)–(11) contradict every possible first recipient's
non-strict own-input J guard in (1). Such a recipient cannot exist.
Together with (3) this proves b_0=...=b_22=0. The proof does not
assert existence or guard satisfaction of any remaining allocation.

### Finite verification and limits

Run `python3 scripts/postspell-word-count/certify_uniform_remaining_early_recipients.py`.
The complete certificate is
`scripts/postspell-word-count/uniform-remaining-early-recipients-certificate.json`.
All 7146 checks pass with zero failures. They reconstruct all 28 changed
tables and all incoming prefixes, match every required prefix and all
616 margins to L084's audited data, check each coefficient sign and
both -d shifts, and match every margin to (11) using L086's complete
d5 certificate. They also retain all failed row0 Q operands, the cap
residual and operands, both uniform offset bounds and all 41 positive
exponential terms. Source hashes identify the input artifacts.
The full d6 margin records and uniform offset operands were inspected;
the program checks all 616 records and complete comparison operands,
not a preview or pass flag. The symbolic proof above covers the entire
allocation simplex without enumeration of allocations. Construction
checks are distinct from the pending independent critical audit.

Attempt 032 and both d0 rational witnesses remain valid. This result
only eliminates early support in the stated literal necessary subsystem.
Cyclic order, last-pair/survivor analysis, actual-word transfer and all
universal eventual-descent gaps remain unresolved here.

### Independent critical audit — 2026-10-20, step 386

The prior SPECIALIZE assessment
`drafts/literature/2026-10-20-uniform-early-support-critical-audit.md`
licenses this RESEARCH/REPRODUCTION audit. No defect was found in the
stated literal endpoint/domain/J implication. This validates the existing
local result; it adds no exclusion, stronger bound or mathematical discovery
beyond the sources checked. Earlier pending-audit descriptions are superseded
by this audit; the argument and its mathematical inputs are unchanged.

**Cap before contradiction.** A separate transcription of L055's 25 pairs
reconstructs all 28 changed tables, with J_i>=2,H_i>=3 and J_i>=15 for
i>=1. Every nonnegative integer allocation of sum B gives K=397573379
and N=630138897. Subtracting kappa from every assumed endpoint gives
n_(i+1)=c_i(n_i+eta_i), where n_i>=47 and 0<eta_i<kappa.
The positive ratios telescope through n_25=n_0. Thus
Lambda=sum log(1+eta_i/n_i), retaining every tail, including a_24=2.
The own-input guards give n_i>=(2^62-23)/11 for all i>=1.
The cited DLMF 4.5.1 applies at each positive eta_i/n_i, yielding
Lambda<kappa/n_0+E. The independently reconstructed positive residual
lambda-E permits inversion, giving s_0<R<U. This argument uses no
b_0>=1 assumption, offset sign, minimum, growth, seed or H guard.
Audited L090's b_0=0 conclusion therefore does not invalidate the cap;
its hypotheses match this lemma on the full allocation simplex.

**Actual inputs, separate signs and boundaries.** If early support remains,
its least index j is in [1,22]. Preceding tails are exactly 2; only the
recipient has a_j>=20 from integrality. For preceding indices 0,...,j-1,
H_i>=7 gives the strictly negative offset upper bound -3969/1408.
For the recipient H_j>=72 gives
Q_j>=67585198634830509743348335148655587/12986507827891524337664
>kappa*2^20. These are different tests. Row0's failed tail-20 test is
retained for all 28 tables; neither the full L076 criterion nor C077a's
conjunction is invoked.

At the actual recipient input G_j s_j-Q_j=G_j(n_j+eta_j)>0, so increasing
the tail reduces the bracket's contribution. This justifies (7) before
any logarithm or multiplication. The prefix comparisons multiply positive
slopes at actual positive junctions; they require no auxiliary trajectory
to satisfy a domain or growth condition. Recipient zero is covered by
L090. For j=1 the only preceding row is row0 at tail 2; for j=22 the
preceding rows stop at row21 and the next guard belongs to outgoing row23
at s_23. Rows23 and24 need no offset sign and retain arbitrary allocations
in the cap. Equality in an original J guard is still strictly contradicted.

**Analytic errors.** Reuse the primary positive-real series and finite
real-affine inputs cited above; no parity realization or new series theorem
is used. For t=2,3,11/4, set z=(t-1)/(t+1), respectively 1/3,1/2,7/15.
The independently regenerated assessed enclosures are

\[
P_t=2\sum_{k=0}^{99}\frac{z^{2k+1}}{2k+1},\qquad
R_t=\frac{2z^{201}}{201(1-z^2)},\qquad
P_t<\log t<P_t+R_t.
\]

Here 0<z<1. Omitted terms are positive; replacing their denominators
by 201 gives the upper geometric remainder, strictly because later
denominators exceed 201. All 300 terms, three complete remainders and
interval endpoints are stored and checked. They certify (4), while
N times the lower log2 endpoint minus K times the upper log3 endpoint
exceeds lambda. The opposite endpoints lie below 10585/10^14. All
amplified errors in this cancellation are retained. The recurrence
t_0=1,t_k=24*t_(k-1)/k independently regenerates all 41 exponential
terms and verifies U<sum t_k<exp(24), hence log s_0<24.

For each recipient put C=D_(j+1)+18+4J_(j+1)>0, A=A_(j+1)>0
and X=C log2-24-log(11/4)-A log3. The exact outward error is

\[
X-M_j(d)=C(\log2-\ell)+A(u-\log3)+(v-\log(11/4)).
\]

All three summands are positive. For all 616 records the complete rational
intervals independently verify 0<X-M_j(d)<1/1000; their endpoints agree
exactly with direct interval evaluation of X minus M_j(d). No decimal
rounding or unaccounted coefficient error establishes a strict margin.
Direct prefix sums contain row0 and omit row24, giving both shifts -d
relative to the original table and -(d-5) relative to d5. Their difference
proves (11) exactly. The minimum remains
M_4(6)=5877662392133/500000000000>47/4. Hence (10) strictly contradicts
the next input's own non-strict guard on the whole allocation simplex.
This supplies no feasibility claim for remaining last-pair allocations.

**Complete independent evidence.** Run
`python3 scripts/postspell-word-count/audit_uniform_early_support.py`.
The full output is
`scripts/postspell-word-count/uniform-early-support-audit-certificate.json`.
The program neither imports nor executes a construction program. Direct
prefix sums and integer-scaled margin numerators, rather than imported
certificate margins, reconstruct all 28 tables and 616 records. All 7146
named construction comparisons are checked with fresh actual and required
operands, relations, differences and verdicts. Exact key sets, lengths and
unique comparison names check completeness. Every construction field is
compared: 57074 leaf comparisons and 2559 further proof checks pass with
zero failures. These counts include repeated data, not distinct mathematical
claims. Every required L084 prefix/margin and d5 margin is separately
matched to the reconstruction; hashes serve only provenance. The printed
d6 table agrees in full.

The certificate retains all reconstructed objects, analytic terms and
remainders, both Lambda endpoints and 616 amplified-error intervals.
The independent program checks complete evidence, not a preview or stored
pass flag. Selected complete cap, boundary and error records were also
inspected. Construction artifacts remain unchanged. Attempt 032 and both
d0 witnesses remain valid. Order reduction, last-pair/survivor analysis,
actual-word transfer and universal eventual descent remain unresolved.

## Mathlib

Full matching coverage is unchecked, not absent. Supporting logarithm,
affine and rational-arithmetic facts do not establish this full
changed-range specialization. No Lean proof is claimed.
