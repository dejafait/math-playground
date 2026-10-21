# Source comparison for a conditional Selmer-corank certificate

TARGET: Assess whether central vanishing, root number +1 and a certified nonzero T^2 coefficient of the primitive ordinary p-adic L-function force classical Selmer corank two under L025's E,p and residual-family hypotheses, without assuming rational rank, finite Sha or Selmer corank.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the saved analytic-order assessment, control/divisibility foundations and L002/L004/C016a/L021/L025; targeted searches for Kim Corollary 1.12 parity and ordinary p-adic order at most two located the primary texts inspected below. No exact standalone combined certificate was located; no novelty inference is made.
SOURCE_EVIDENCE: Kim publisher-hosted author PDF dated 2025-05-12, Sections 1.2.2/1.4, Theorem 1.8 and Corollaries 1.11/1.12 with their proofs; Stein--Wuthrich 2013, Sections 3/3.3/6, Proposition 7.2 and Kato Theorem 7.3; Sakamoto 2022, Section 1.1 and Corollary 1.9 proof for witness and root-number conventions; reuse Greenberg Theorems 1.2/1.5 as assessed in foundations/03-cyclotomic-control.md.
COMPARISON: The inspected converse and parity statements concern classical Selmer corank on the same nonvanishing premise; Kato uses the matching primitive ordinary series and classical cyclotomic dual. L004's k=0,n=2 case supplies the existing upper-bound mechanism, without independent rational points.
GAP: No essential source mismatch found for the retained conditional target. The combined application and elementary corank squeeze remain to be written and checked in a later research turn; coefficient production, rational Kummer membership and complex-order equality remain unproved.
REASON: Approve specialization of this known source package for the exact saved target, retaining F and the independent coefficient certificate; no reproof or new mathematical lemma is authorized in this literature turn.
LITERATURE_REASON: The saved target changed from compactness under granted corank to production of that corank from central vanishing, sign and an additional p-adic coefficient; this turn completed the required joint theorem comparison.
SCOPE: Non-CM E/Q, p>=5 ordinary and non-anomalous, surjective E[p], prime-to-p Manin and Tamagawa factors, E(Q_p)[p]=0, and residual Kurihara-family nonvanishing as in L025. Replace granted Selmer corank two by L(E,1)=0, root number +1 and a rigorously nonzero quadratic coefficient in the primitive ordinary cyclotomic normalization. Retain F=S/S_div without assuming it zero.

The source comparison below is complete. It approves a later
specialization of the exact TARGET, subject to the separate next-turn
gate. This literature turn derives no corank or parity assertion.

The main gap is still rational rank equal to complex order in analytic
rank at least two. The proposed intermediate target concerns the other
explicit missing input on the L025 branch: its granted Selmer corank.
If the source comparison supports a later conditional theorem, that
theorem could activate the existing actual-pair construction whenever
the added coefficient certificate is available. Neither availability
from complex order two nor rational Kummer membership is presumed.

Continue only if the inspected statements concern classical Selmer
corank, have the required implication directions, and apply to the same
primitive p-adic L-function. Abandon this combination if it needs finite
Sha, positive rational rank or an already assumed corank-two premise.
A failure to produce the coefficient uniformly is a remaining independent
gap, not a reason to misreport a conditional theorem as a BSD solution.

Reuse the earlier source assessments before browsing. In particular,
do not repeat the parked direct point-valued Kato import, generic
period-index splitting, or removal of F from primitivity. This target
allows F and introduces a genuinely additional, explicitly certified
p-adic hypothesis. L002 and L004 provide the intended upper-bound
inputs; C016a locates the finite-Selmer converse; L021 and the earlier
analytic-order assessment locate the parity comparison. Retrieve only
the needed primary theorem hypotheses and cases where saved evidence
is insufficient. No cross-notebook input is requested.

Mathlib coverage of the proposed combined statement is not checked.

## Completed comparison (2026-10-06)

The main gap, downstream use and test above remain unchanged. This
assessment replaces the granted corank premise only as a proposed later
application; it does not remove L025's arithmetic or residual-family
hypotheses. The target concerns the classical group
S = Sel(Q,E[p^infinity]), not the strict or relaxed Selmer group.

Queries were `"Kim" "Corollary 1.12" "Selmer" parity elliptic`
and `elliptic curve ordinary p-adic L-function order at most two Selmer
corank parity central vanishing`. Search hits served as locators.
Nonprimary discussions and the generalised-Kato search hit supply no
input. No additional unread lead is essential to this conditional test.

**Converse and parity.** Chan-Ho Kim, *The structure of Selmer groups
and the Iwasawa main conjecture for elliptic curves*, author text dated
2025-05-12, [Sections 1.2.2/1.4, printed pp. 4--6](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=4),
and [Corollaries 1.11/1.12, printed pp. 8--9](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8),
were inspected with their proofs and Theorem 1.8's statement.
Both corollaries require p >= 5, surjective E[p], prime-to-p Manin
constant and nonzero integral Kurihara collection. Corollary 1.11 states
S finite iff L(E,1) != 0; Corollary 1.12 equates corank S and complex
order modulo two. Neither assumes finite Sha or positive rational rank.
The former's proof uses Theorem 1.8 and the central modular symbol;
the latter uses the Kurihara functional equation. Their extra ordinary
consequences need not supply the retained witness.

**Witness applicability.** Reuse L021's matching of the residual witness
to Kim's nonzero integral collection, not C016a's additional fixed
two-prime premise. The exact definitions were rechecked in Kim Section
1.4 and Ryotaro Sakamoto, *p-Selmer group and modular symbols*, Documenta
Math. 27 (2022), 1891--1922,
[Section 1.1, pp. 1892--1894](https://ems.press/content/serial-article-files/29299?nt=1#page=2).
Sakamoto's P_(1,0) has cyclic residual p-torsion and ell = 1 mod p;
Kim's P_1 requires ell = 1 and a_ell = ell+1 mod p. The period and
discrete-log conventions are those already justified in L021/C016a.
Minimality and a count of two primes are unnecessary for the corollaries.
Sakamoto's Corollary 1.9 proof records w(E)=(-1)^ord_(s=1)L(E,s).
Use Kim's classical-corank parity, rather than silently replacing it
with Sakamoto's residual-dimension statement or rational-rank parity.

**Upper bound and normalization.** William Stein and Christian Wuthrich,
*Algorithms for the arithmetic of elliptic curves using Iwasawa theory*,
Math. Comp. 82 (2013), 1757--1792,
[Sections 3/3.3, pp. 1762--1766](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6),
[Section 6, pp. 1775--1776](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=19),
and [Proposition 7.2/Kato Theorem 7.3, p. 1778](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=22)
were inspected. The ordinary series uses the unit root, real Neron
period, trivial Teichmuller branch and T=kappa(gamma)^(s-1)-1.
Its characteristic series belongs to the classical cyclotomic dual.
For p >= 5, residual surjectivity supplies full p-adic surjectivity;
Theorem 7.3 states L_p=f_X d with d in Lambda at semistable p.
Good ordinary reduction meets that condition. The original input is
Kato, Asterisque 295 (2004), Theorem 17.4, as recorded in foundations/05;
its full original proof was not reread. There is no reverse-divisibility
input or exceptional-zero adjustment here.

Reuse L002's complete arithmetic specialization and L004's coefficient
argument, including the k=0 case; their relevant proof passages were
read. Greenberg's control/cotorsion assessment in foundations/03 remains
adequate. The nonzero quadratic coefficient must be certified for this
exact primitive series and generator. A numerical preview, a coefficient
of a series with removed factors, or an uncertified approximation is
insufficient. Lower coefficients are not extra premises; the proposed
application must justify every order comparison rather than presuppose
that the p-adic order is two. L004 already states the rigorous error
criterion v_p(a_2-b) >= N > v_p(b), if an approximation is used.

## Approval boundary and remaining gaps

The inspected inputs supply the needed infinitude test, classical-corank
parity test and upper-bound mechanism on the retained assumptions. No
essential coverage is blocked. SPECIALIZE authorizes only their joint
application and the identified elementary corank comparison in the next
research turn; that turn should be classified REPRODUCTION. No original
theorem or beyond-source discovery is claimed. A reproof of Kim or Kato
is unnecessary; import them with the citations above.

Duplicates and failures: L004 already handles a certificate with rational
points; C016a applies the finite-Selmer converse after a stronger
two-prime premise; L021 and ATTEMPTS/021 show why primitivity alone
does not remove F. The earlier analytic-order-to-Kurihara assessment
did not add a certified p-adic coefficient. This target adds that
independent hypothesis and permits F; it does not reopen any exhausted
point-extraction or finite-defect-removal route.

Continue by checking the conditional corank squeeze with inputs
L002/L004 and the cited corollaries, preserving L021's witness matching.
Abandon the application if its proof needs finite Sha, rational rank,
an assumed corank or a different cyclotomic normalization. Even if it
works, availability of a_2 != 0 from complex order two, rationality of
L025's limiting pair, finite Sha and the exact Clay target remain
independent unresolved claims. No PROOF.md or DAG.md change is made.
