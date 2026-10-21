# L050 — Twenty-word cyclic-height infeasibility

## Hypotheses

All logarithms are natural. Indices are modulo twenty. Let J_i>=2,
H_i>=3 and a_i>=0 be integers with a_i congruent to 2 modulo 18. Put
P_i=4J_i+H_i, K=sum_i(3J_i+H_i), L=sum_i(J_i+a_i), N=K+L.
Let d,K_0,L_0 be positive integers satisfying K=dK_0, L=dL_0 and
K_0>225640000. Assume

\[
\Lambda=N\log2-K\log3>0,\qquad
N<\frac85K+\frac{1380}{1034}.                         \tag{1}
\]

Let s_i>=540/11 be real numbers, h_i=log s_i, with s_0=min_i s_i
and s_20=s_0. Assume

\[
0<h_0<\frac{133}{10}\log N+8+\log20,                 \tag{2}
\]
\[
4J_i\log2\le h_i+\log(11/4),\qquad
H_i\log2<h_i+J_i\log(27/16).                         \tag{3}
\]

For G_i=(27/16)^{J_i}(3/2)^{H_i}, require every exact endpoint

\[
s_{i+1}=2^{-a_i}\left(G_i s_i-\frac{12}{11}(3/2)^{H_i}-1\right)
                  +\frac{23}{11}.                   \tag{4}
\]

These are exactly L046's subsystem (1)–(4) at twenty occurrences,
with its two count-dependent constants changed as displayed. No integer
parity, valuation, residue realization, additional quantitative linear-form
bound or optional inequality from the larger relaxation is assumed.

## Conclusion

This system has no solution. In particular, actual closed concatenations
of twenty allowed postspell words under L041's hypotheses are excluded,
subject to the published inputs and qualifications below. Together with
the preceding exclusions this extends the restricted exclusion through
twenty words. The separate critical audit below found no defect within
the stated hypotheses and published qualifications.

This is local progress by REPRODUCTION within the approved SPECIALIZE
scope; no originality beyond the checked sources is claimed. It does not
prove entry into this language, exclude unrestricted cycles or divergence,
or establish universal eventual descent. It is not a complete Collatz
candidate. L049's survivor for the weaker scalar inequality remains valid.

## Proof

### 1. A coarse finite ceiling, without discarding the tails from N

L046's real-domain argument, through its prefix-count estimate, uses
only the occurrence's own inequalities (3), endpoint (4), a_i>=2 and
s_i>=540/11. These hypotheses are unchanged. In particular, for every
one of our twenty indices it gives

\[
h_{i+1}+1<\rho(h_i+1),\quad \rho=48/25,\qquad
P_i<\frac{15}{4}h_i+3.                              \tag{5}
\]

We import those numerical inequalities from L046, not its eighteen-word
conclusion. Its proof explicitly checks the real domain and both shifts;
no actual integer valuation is needed for this substitution. Applying
(5) along edges 0 through 18 covers all twenty input occurrences. Set

\[
R=\sum_{j=0}^{19}\rho^j
 =\frac{183271938906583091673157351511737}
        {363797880709171295166015625}<503775.
\]

Induction and K=sum(P_i-J_i)<sum P_i give

\[
K<\frac{15}{4}\sum_i(h_i+1)\le\frac{15}{4}R(h_0+1).
                                                               \tag{6}
\]

Using (1) and (2), with all positive coefficients preserved,

\[
N<\frac{399}{5}R\log N+(54+6\log20)R+\frac{1380}{1034}.
\]

Here N>1 by the integer guards. The exponential series gives
 e>163/60>27/10, and (163/60)^3=4330747/216000>20.
Thus log20<3; also 1380/1034<2. Consequently

\[
N<A\log N+B,\qquad A=40201245,\quad B=36271802.     \tag{7}
\]

Let M=10^9. Since (27/10)^21>M, log M<21. For all real t>=M,
F(t)=t-A log t-B has derivative 1-A/t>0, since A<M. Moreover

\[
21A+B=880497947<M,
\]

so F(M)>0 and (7) is impossible on that whole ray. Therefore

\[
0<K<N<M.                                           \tag{8}
\]

This is only a finite ceiling; it is not yet a contradiction with the
primitive odd-count threshold. No upper bound on an individual tail has
been imposed. The length conversion in (1) retains every tail in N.

### 2. Integer total counts separate the logarithms

Use the explicit positive integers

\[
p=9809721694,\qquad q=6189245291.
\]

The certified strict logarithm comparison is

\[
0<r:=q\log3-p\log2<\frac{\log2}{2M}.               \tag{9}
\]

The exact enclosure procedure and certificate verifying this comparison
are specified below. No best-approximation theorem or new published
cycle threshold is required: only (9) matters.

Write ell=log2. Since Lambda>0 and K>0,
N/K>log3/log2>p/q by (9). Thus z=Nq-Kp is a positive integer,
so z>=1. Using K<M from (8) and r>0,

\[
\Lambda=\frac{\ell z-Kr}{q}
 >\frac{\ell}{2q}>\frac1{3q},                       \tag{10}
\]

where ell>2/3. This is a consequence of integer total counts in the
approved subsystem; it is not an extra assumed lower bound on Lambda.

### 3. All exact cyclic endpoints force a small minimum height

Put n_i=s_i-23/11>=47. These are real numbers; no integer-orbit
interpretation is made. In particular n_0=min_i n_i. Define

\[
\eta_i=\frac{23}{11}-\frac{12}{11}(16/27)^{J_i}
                    -(16/27)^{J_i}(2/3)^{H_i}.
\]

Both powers lie strictly between zero and one. Therefore
0<eta_i<23/11: for the lower bound their two subtracted terms sum
to strictly less than 12/11+1=23/11. Substitution into the retained
endpoint equation (4), with no term dropped, gives

\[
n_{i+1}=\frac{G_i}{2^{a_i}}(n_i+\eta_i).            \tag{11}
\]

All factors are positive. Multiplying all twenty equations (11) and
using n_20=n_0 yields

\[
1=\left(\prod_i G_i/2^{a_i}\right)
                   \prod_i(1+\eta_i/n_i).
\]

By the definitions of K and N,
log prod_i(G_i/2^{a_i})=K log3-N log2=-Lambda. Taking logarithms
and using log(1+t)<t for t>0 therefore gives the exact identity and bound

\[
\Lambda=\sum_i\log(1+\eta_i/n_i)
 <\sum_i\frac{\eta_i}{n_i}
 <\frac{460}{11n_0}.                               \tag{12}
\]

This uses the twentieth closing equation as well as every other endpoint.
It does not assume the optional reciprocal or linear-form constraints of
a larger relaxation. It derives its own bound from (4). Combining (10)
and (12) gives

\[
n_0<\frac{1380q}{11},\qquad
s_0<\frac{1380q+23}{11}=\frac{8541158501603}{11}.
\]

The exact comparison

\[
(27/10)^{28}=\frac{11972515182562019788602740026717047105681}
                   {10000000000000000000000000000}
 >\frac{8541158501603}{11}
\]

and e>27/10 now imply h_0<28. Substituting this into the already
proved (6) yields

\[
K<\frac{15}{4}\,503775\,29
 =\frac{219142125}{4}=54785531.25<225640000.
\]

But K=dK_0>=K_0>225640000. This contradiction proves infeasibility
for all admissible integer parameters and real heights.

### 4. Exact verification of constants

For each t in {2,3}, set x=(t-1)/(t+1). Integration of
2/(1-x^2), or its finite geometric expansion with positive remainder,
gives, for m=48,

\[
B_t=2\sum_{j=0}^{m-1}\frac{x^{2j+1}}{2j+1}
 <\log t
 <B_t+E_t,\qquad
E_t=\frac{2x^{2m+1}}{(2m+1)(1-x^2)}.
\]

Indeed the omitted positive integral is
2 integral_0^x u^{2m}/(1-u^2) du, which is strictly less than E_t
because 1/(1-u^2)<1/(1-x^2) for 0<=u<x. Thus no floating-point
rounding or infinite-series truncation without a remainder is used.
Writing l_t=B_t and u_t=B_t+E_t, exact rational arithmetic verifies

\[
q l_3-p u_2>0,\qquad
q u_3-p l_2<l_2/(2M),\qquad l_2>2/3.
\]

These prove (9) and the final inequality of (10), with signs chosen
according to the positive p,q. The full rational operands, log enclosures,
geometric sum and all numerical checks are in
`scripts/postspell-word-count/twenty-cyclic-height-certificate.json`.
Reproduce with
`python3 scripts/postspell-word-count/certify_twenty_cyclic_heights.py`.
All 13 exact checks pass; their full operands and the two complete log
enclosures were inspected. The analytic induction, monotonicity,
integer separation and closure arguments above remain essential and
are not established merely by passing the script.

An initial certificate used (27/10)^3>20, which is false, to justify
log20<3. That failed check is preserved in
`scripts/postspell-word-count/twenty-cyclic-height-initial-certificate.json`.
The repair uses the stronger already available e>163/60, whose cube
exceeds 20. No failed check or initial numerical diagnostic is counted
as proof. The canonical generator implements the repaired inequality.

### 5. Applicability and source qualifications

L041's all-r actual-word bridge at r=20 supplies exactly (1)–(4),
positive odd residue-20 junctions n_i>=47, integer represented counts,
and primitive scaling. Its cyclic relabeling selects the smallest
**designated junction**, permits ties, and retains every independent
exact tail. Repeated periods and coincident junctions remain separate
time occurrences. Its nontriviality check holds because n_i>=47 lies
outside the invariant shortcut cycle {1,2}. The full local-minimum
count is not set to twenty, and no designated junction is identified
with the global orbit minimum.

The inherited primary sources, used through L041, are Christian Hercher,
*There are no Collatz m-Cycles with m <= 91*, JIS 26 (2023), Article
23.3.5, [Theorem 16 and proof, pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
and John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005), 51–70,
[Corollary 2 and proof p. 53, Lemma 12 and proof p. 61, nonminimal-period conventions p. 52](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
Corollary 2 supplies K_0>225640000 for a nontrivial positive integer
primitive cycle; it is imposed as a necessary condition in our relaxation,
not asserted as a theorem about real cycles. The other imports supply
L041's original seed and length conversion. The published height
x_min>301*2^50, distributed [Ro] computations and Roosendaal communication,
continued-fraction denominators 225644606 and 397573379, and Rhin/Crandall
originals retain their recorded qualifications. Their original certificates
and external Lean builds are not independently verified. The inspected
Hercher correction leaves Theorem 16 unchanged; Theorem 21 is unused.
Our separate explicit p,q comparison is certified locally and does not
purport to reverify those published computations.

The ready assessment also supplies Lorenz Halbeisen and Norbert
Hungerbühler, *Optimal bounds for the length of rational Collatz cycles*,
Acta Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[published Lemmas 1/2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf):
a prescribed nonempty binary word has affine map
(3^K n+phi)/2^N and fixed point phi/(2^N-3^K).
This is the cited known closure formula, not a local reproof. The present
contradiction needs no candidate fixed point or rational parity theorem:
(11)–(12) simply multiply the twenty equations already assumed, retaining
their particular offsets. Thus this general coding citation is background,
not an additional mathematical premise in the dependency graph.

The approved source comparison was saved before this attempt in
`drafts/literature/2026-10-10-twenty-cyclic-height-feasibility.md`.
No new constraint or word count was added. Attempts 021–023 remain
valid stops for their specified weaker comparisons. Further counts,
optimality, integer realizability and universal descent are not addressed.

### Separate critical audit — 2026-10-10

The pre-invocation SPECIALIZE coverage was
`drafts/literature/2026-10-10-twenty-cyclic-height-infeasibility-audit.md`.
Verdict: **no defect found within the stated hypotheses and imported
qualifications**. This is a REPRODUCTION audit, with no repaired argument,
stronger word-count exclusion or claim of originality. The full proof and
generator, L041's relevant proof/audit and L046's real-domain proof/audit
were checked. Ready source coverage was reused; no new external theorem
or additional constraint is invoked.

The numerical transfer in L046 applies separately at every real s_i:
subtract the positive offset terms in (4), then bound the remaining
positive G_i s_i/2^{a_i} by G_i s_i/4. The lower bound s_i>=540/11
absorbs the +23/11 shift. Its own-index substitutions have positive
coefficients log(27/16), delta and delta-1, where delta=log3/log2;
they require no valuation of a real height. Its prefix estimate likewise
uses only (3). Nineteen edges, indexed 0 through 18, give the bounds
for all twenty inputs indexed 0 through 19. The strict K estimate
follows from P_i<(15/4)h_i+3<(15/4)(h_i+1) and J_i>=2.
The exact closed-form sum is
R=(48^20-25^20)/(23*25^19), agreeing with the displayed fraction.
Multiplying the K bound by 8/5 gives the factor 6, hence exactly
(399/5)R log N+(54+6log20)R+1380/1034. All substitutions are
upper bounds with positive multipliers; N>=260 ensures log N>0.

The repaired log20 guard uses the degree-five exponential partial sum
163/60 and its positive omitted tail. Its cube is 4330747/216000>20;
(27/10)^3=19683/1000<20 is still preserved as a failed initial check.
The weaker e>27/10 is adequate for log(10^9)<21. Thus (7) has
A=40201245 and B=36271802, with A<10^9 and
21A+B=880497947<10^9. On the entire real ray t>=10^9,
1-A/t>0 and F(10^9)>119502053. This proves the strict ceiling
K<N<10^9, independently of whether any integer sample is tested.

For the logarithms, integrating the finite geometric identity gives
the exact positive remainder in section 4. The strict upper bound
follows by replacing 1/(1-u^2) by 1/(1-x^2) inside that integral;
the integrands differ on an interval of positive length. The generator
passes rational arguments, so its division does not introduce a float.
The complete 48-term enclosures and both residual operands were read
and recomputed. Independently, 64-term Horner evaluations at x=1/3
and x=1/5 enclose log2 and log(3/2). Writing
r=(q-p)log2+q log(3/2), with q-p<0, the lower endpoint uses the
upper log2 enclosure, and the upper endpoint uses its lower enclosure.
They certify 9/10^11<r<1/10^10 and r<log2/(2*10^9).
Both independent residual endpoints lie strictly inside the original
certified interval. No floating-point or best-approximation premise
is needed.

Since Lambda>0 and K>0, N/K>log3/log2>p/q. Integer N,K,p,q
therefore give z=Nq-Kp>=1, without requiring coprimality or bounds
on z. The identity q Lambda=(log2)z-Kr has the stated minus sign.
Using K<10^9 and the strict residual upper bound gives
q Lambda>log2/2>1/3. No optional lower linear-form constraint
has entered the real system.

For closure, subtract 23/11 from (4) and substitute s_i=n_i+23/11.
Dividing its offset by G_i gives exactly
eta_i=23/11-(12/11)(16/27)^{J_i}-(16/27)^{J_i}(2/3)^{H_i}.
Both subtracted terms are positive and their sum is strictly below
12/11+1=23/11, so 0<eta_i<23/11. All n_i>=47 are positive.
Multiplication of all twenty equations cancels prod_i n_i because
n_20=n_0; this remains valid with ties or repeated states. The total
exponents in prod_i(G_i/2^{a_i}) are precisely sum_i(3J_i+H_i)=K
and sum_i(4J_i+H_i+a_i)=N. Taking logarithms therefore gives (12),
and n_i>=n_0 yields the strict upper bound 460/(11n_0).
Combining it with Lambda>1/(3q) gives n_0<1380q/11, hence
s_0<8541158501603/11. The exact power comparison in section 3
then proves h_0<28. The already established occurrence sum gives
K<219142125/4=54785531.25<225640000, contradicting K=dK_0>=K_0.
This covers all allowed parameters; it is not a finite feasibility search.

For actual words, L041 supplies the seed with log20, the length
constant 69*20/1034, both own-index bounds and all exact shifted
endpoints. Positive odd residue-20 junctions are at least 47.
Cyclic relabeling to their minimum preserves each outgoing word and
its independent exact tail, including ties. Primitive period reduction
counts time occurrences and gives K=dK_0,L=dL_0 with d>=1; it does
not discard repeated words. The primitive orbit is nontrivial because
it contains a junction outside {1,2}. The cited Simons–de Weger
Corollary 2 therefore supplies its odd-count threshold. No source
theorem about integer cycles was applied directly to arbitrary real
heights, no global minimum was substituted for a designated junction,
and the full cyclic minimum count was not set to twenty.

Reproduce with
`python3 scripts/postspell-word-count/audit_twenty_cyclic_heights.py`.
The original thirteen-check certificate regenerates byte for byte,
SHA-256 `6b8fb12cb4e92ebdf16d13b0af957dbc3a65058c76dea1a1c512b48144080013`.
The audit checks its complete mathematical operands, saved flags and
summary fields, the independent logarithm computation and the preserved
failure. All 37 audit checks pass; full values and no failures are saved
in `scripts/postspell-word-count/twenty-cyclic-height-audit-certificate.json`.
The analytic reasoning above remains essential; certificate success alone
does not prove it. Published computations, Rhin/Crandall originals and
external Lean builds retain the preceding qualifications.

L049 and Attempts 019/021–023 remain valid for their weaker systems.
No argument or direct dependency changed; PROOF.md and DAG.md are
unchanged. This canonical verdict supersedes only the overview's pending
L050 audit wording. Unrestricted word counts/cycles, entry, divergence
and universal eventual descent remain open.

## Mathlib

Matching coverage of the full simultaneous subsystem, its closure-derived
bound and the inherited cycle inputs has not been checked. Elementary
logarithm, finite-product and rational-arithmetic facts support this proof,
but no matching Lean declaration or formal verification is asserted.
Unknown availability is not evidence of absence.
