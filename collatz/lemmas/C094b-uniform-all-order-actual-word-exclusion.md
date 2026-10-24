# C094b — Uniform all-order full-allocation actual-word exclusion

## Hypotheses

Fix an integer 6<=d<=33. Use L055's complete 25 indexed pairs,
changing only H_0=40-d and H_24=32670621+d; every J_i and every
other H_i is unchanged. Let b_i be nonnegative integers with
sum_(i=0)^24 b_i=B=9250245, and attach a_i=2+18b_i to indexed
outgoing row i. Let pi be any permutation of {0,...,24}.

Use the shortcut map T(n)=n/2 for even positive integers and
T(n)=(3n+1)/2 for odd positive integers. O and E specify actual
input parities. Suppose the concatenation

\[
W_{\pi(0)}\cdots W_{\pi(24)},\qquad
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},
\]

is actual and closed at a positive integer. Require every junction
to be positive, odd and 20 modulo 27, and each final even tail to
be exact. Repeated periods and coincident junctions are allowed.
There is no minimum, seed, least-root, first-return or primitive-period
premise. All logarithms below are natural.

## Conclusion

No such actual closed concatenation exists for any specified d,
any indexed cyclic order and any allocation in the full stated
integer simplex.

This is a local RESEARCH/REPRODUCTION application under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-23-uniform-all-order-actual-word-application.md`.
It transfers audited C094a's real exclusion to this actual-word family;
it claims no advance beyond the inspected source machinery. The separate
critical audit below found no defect. Other tables, universal entry, unrestricted
cycles, divergence and universal eventual descent remain unresolved.
This is not a complete Collatz candidate.

## Proof

Assume such a concatenation exists, starting at n_0. Define

\[
t_0=0,\qquad t_{k+1}=t_k+4J_{\pi(k)}+H_{\pi(k)}+a_{\pi(k)},
\quad n_k=T^{t_k}(n_0),\quad s_k=n_k+\kappa,
\qquad \kappa=23/11.
\tag{1}
\]

Here 0<=k<25 for increments and 0<=k<=25 for junctions.
Each increment is the positive number of letters in that outgoing
word. Thus k labels chronological occurrences even if values coincide.
Actual closure gives n_25=n_0 and s_25=s_0, including when the
representation repeats a shorter period.

Write each junction as n_k=20+27q_k with integer q_k. Positivity
excludes q_k<0, and oddness forces q_k odd. Hence q_k>=1 and

\[
n_k\ge47>1,\qquad s_k\ge47+23/11=540/11
\quad(0\le k\le25).
\tag{2}
\]

L055's complete pair table has J_i>=8 and H_i>=72 for 1<=i<=23.
The replacements give 7<=H_0<=34 and
32670627<=H_24<=32670654. Thus all rows have integer J_i>=2,
H_i>=3, and all attached tails are integers a_i>=2 congruent to
2 modulo 18. The chronological parameters
J'_k=J_pi(k), H'_k=H_pi(k), a'_k=a_pi(k), with r=25, meet
L041's hypotheses by actuality, closure, (2), the stipulated residues
and exact tails. Use only L041's passage “Each occurrence's own
prefix and the transfer to the next” and its audited occurrencewise
scope. Those finite-word necessities are independent of the minimum
selection, seed and cycle-count estimates elsewhere in L041.

Fix any 0<=k<25 and put i=pi(k), J=J_i,H=H_i,a=a_i. Define the
actual prefix states y_k=T^(4J)(n_k), z_k=T^(4J+H)(n_k).
L041's established arbitrary-tail necessities give

\[
y_k+1=(27/16)^J s_k-12/11,\qquad
2^H(2^a n_{k+1}+1)=3^H(y_k+1),
\tag{3}
\]
\[
11n_k+23\ge2^{4J+2},\qquad
2^H\le y_k+1<(27/16)^J s_k.
\tag{4}
\]

The actual even tail gives z_k=2^a n_(k+1). Substituting the first
identity of (3) into the second, then dividing by 2^a and adding
kappa, yields exactly

\[
s_{k+1}=2^{-a_i}(G_i s_k-Q_i)+\kappa,
\quad G_i=(27/16)^{J_i}(3/2)^{H_i},\quad
Q_i=(12/11)(3/2)^{H_i}+1.
\tag{5}
\]

Both negative terms in Q_i remain inside division by the actual
2^a_i; the shift kappa is outside. No endpoint inequality or comparison
tail replaces this equality.

All logarithm arguments below are positive by (2)–(4). Since
11n_k+23=11s_k, the first inequality of (4) gives

\[
4J_i\log2\le\log s_k+\log(11/4).
\tag{6}
\]

The other two bounds of (4) give

\[
H_i\log2\le\log(y_k+1)
 <\log s_k+J_i\log(27/16).
\tag{7}
\]

Thus the H guard is strict even when its lower power bound is an
equality. Each guard uses row i=pi(k), its allocated tail and the same
own input s_k. In particular row18's H guard belongs to its input at
the unique position k with pi(k)=18, wherever that position lies.

The arbitrary k includes k=24. Equation (5) there is the closing
endpoint with s_25=s_0; (6)–(7) there remain guards at s_24 for
outgoing row pi(24). L041's necessity covers every a>=2 with an odd
endpoint, so the closing tail and any other tail may equal 2. No
time occurrence or closing equation has been lost.

Apply audited C094a directly to this chronological real tuple. Its
d, complete indexed table, permutation pi, integer allocation b_i,
budget B and attached tails a_i are identical. Its lower domain and
closure are (2) and s_25=s_0. Its endpoint (1) is (5) at every k,
and its two own-input guards are exactly (6) and the strict consequence
of (7). Every hypothesis holds on the same tuple. C094a excludes that
tuple, giving the contradiction.

No additional rotation is needed: C094a already covers arbitrary pi
and its internal normalization preserves both cuts. Repeated periods
and coincident junction values remain labeled occurrences throughout.
This proves only the stated restricted actual-word exclusion.

### Sources, overlap and qualifications

L055 supplies its complete pair table only, L041 supplies its audited
finite occurrencewise necessities, and C094a supplies its audited
all-order real exclusion. No upstream numeric certificate is rerun.
C093b is the literal-order comparison for the same d range; C089b
is the all-order comparison for d=5. Neither is a theorem premise
for this application. The prior assessment found no identical completed
application in its scoped search; that does not establish novelty.

The reused upstream affine reference is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its previously inspected scope concerns finite nonempty binary words
and affine composition; fixed-point uniqueness requires nonzero
denominator. This application takes no new fixed point, and all
upstream denominator qualifications remain handled by C094a's audited
inputs. L041 already supplies (3)–(4), so neither the affine theorem
nor parity coding needs a reproof. No fresh source retrieval is claimed.

Attempt 032's failed full support criterion remains failed and unused.
The full C077a conjunction is not inferred from actuality. Both original
d=0 rational witnesses use a different table and remain valid. No
minimum/seed, survivor feasibility, shifted-integrality test, primitive
count threshold or realization converse enters. Other tables and all
universal eventual-descent gaps remain open.

### Independent critical audit — 2026-10-23, step 414

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-23-uniform-all-order-actual-word-critical-audit.md`.
The verdict is no defect in this restricted actual-word transfer.
It validates an existing local input, without an additional table
exclusion, new estimate or discovery beyond the checked sources.
C094a's step-410 audit and L041's audited finite-word necessities
are imported; their upstream analytic proofs and numeric certificates
are not independently reconstructed in this audit.

**Identical data and occurrence domain.** Read all 25 pairs in L055.
Row0 has J_0=8; rows1 through23 have J_i>=15 and H_i>=72;
row24 has J_24=30998279. The only changes give
7<=H_0<=34 and 32670627<=H_24<=32670654, including d=6 and33.
Consequently every pair satisfies L041's integer J>=2,H>=3 domain.
The same nonnegative integer b_i, sum B=9250245 and a_i=2+18b_i
are used in C094a and C094b. L055 supplies its table, not its special
allocation, rational witness, seed or minimum.

The increments in (1) count exactly the letters in outgoing
W_pi(k), with its attached tail a_pi(k). Iteration composition
therefore makes n_(k+1) the output of that word at n_k. There are
25 labeled input occurrences regardless of equal numerical values or
period repetition. At every junction, n=20+27q>0 implies q>=0;
oddness implies q is odd, hence q>=1. Thus n>=47 and
s=n+23/11>=540/11>0, including the initial input and closing output.
This proves the required lower domain without selecting a minimum.
Using chronological parameters in L041 is just its indexing by
occurrence, with r=25; it requires no ordering of the indexed pairs.

**Finite necessities without the seed.** L041's proof before (7)
explicitly establishes (3)–(4) separately at each outgoing word.
Although an earlier section rotates to a designated minimum for its
seed, this passage uses only the actual finite word and its own input
and output. Its completed own-word audit explicitly verifies independence
from size ordering. Inspection of L031 (4) and its arbitrary-tail
valuation passage confirms that this is not a two-word closure converse
or an E^2-only transport claim. In particular 2^a n_next+1 is odd
for every admitted a>=2. The cited identity gives v_2(y+1)=H and
positive odd u=(y+1)/2^H. With H>=3, the factor
11*2^(H-2)u+3 is odd, so the cited boundary valuation is 4J+2.
These are precisely the hypotheses of the already proved necessities;
no cycle mass, primitive-count estimate or minimum seed is imported.

**Endpoint and signs.** From (3), division first by 2^H gives
2^a n_next=(3/2)^H(y+1)-1. Substitution of its other identity gives
2^a n_next=G_i s_k-(12/11)(3/2)^H-1.
Hence (5) is C094a (1) exactly: the entire Q_i is divided by the
actual 2^a_i and kappa is added afterwards. No offset has changed sign
or been moved outside that division.

For J, 11s_k>=2^(4J+2) implies
4J log2<=log s_k+log11-2log2=log s_k+log(11/4).
For H, the imported lower power bound and the positive subtraction
12/11 give 2^H<=y_k+1<(27/16)^J s_k. Strict monotonicity of log
gives H log2<=log(y_k+1)<log s_k+J log(27/16).
Thus the required final H inequality stays strict even if its first
inequality is equality. Every logarithm has a positive argument.
Both guards use i=pi(k) at s_k, not s_(k+1). In particular the
unchanged row18 pair (693015,3295208) is tested at the unique
chronological input carrying that outgoing row, including if k=24.

**Closure and invocation.** For k=24 the same actual finite word
ends at n_25=n_0. Its endpoint is therefore exactly the closing
equation s_25=s_0, and both guards stay at s_24. The necessity
proofs require only a>=2, so a=2 at this or any other occurrence
is covered. Repeated periods and coincident values introduce no
omitted edge or distinctness premise.

C094a now receives precisely its own d, table, permutation, full
integer allocation and real tuple, with every lower domain, endpoint,
closing equality, weak J guard and strict H guard established above.
Its audited contradiction applies directly. Its internal rotation
and both cuts need not be reconstructed or added as hypotheses here.
No feasibility, minimum/seed, integer-junction test, failed full C077a
conjunction, primitive threshold or realization converse enters.

**Scope and documentation.** C093b and C089b are narrower comparisons,
not additional premises; the scoped histories and working note record
construction and proposed review, not an earlier completed C094b audit.
Attempt 032 and both original d0 witnesses remain valid. The precise
Halbeisen–Hungerbuehler citation and inspected hypotheses above are
reused through existing inputs; no new fixed point, affine reproof or
fresh external inspection is claimed. Direct inputs remain L041,L055
and C094a, as recorded in the DAG; L031 was inspected only to check
L041's proof scope. No mathematical argument or dependency changed,
so PROOF.md and DAG.md are unchanged. This canonical audit supersedes
their pending C094b-audit wording. Other tables, universal entry,
unrestricted cycles, divergence and eventual descent remain unresolved.
Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching Mathlib coverage for this table-specific actual-word
exclusion is unchecked. Supporting affine, finite permutation and
positive-real logarithm facts are not a matching theorem. Unknown
coverage is not absence; no formal verification is claimed.
