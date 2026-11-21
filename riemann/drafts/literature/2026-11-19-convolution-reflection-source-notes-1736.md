# Positivity-reflection source review1736: working notes

Literature-only. Exact starting target: Review whether convolution by C032u's nu_1 reflects positivity for finite real signed Borel measures of mass one on [0,infinity), distinguishing general counterexamples from this qualified law.

Main gap: L030-L032/C032a actual-Xi all-degree positivity. Intermediate test: whether positivity can be pulled back through the fixed probability factor nu_1. A positive pullback could support a common-factor/tail obstruction via C032r; neither a continuum factorization nor its tail premise is established. Continue only with applicable source hypotheses or a separately approved actual-law test; abandon automatic reverse inference without them.

Local review: C032u full comparison proof, C032q/r hypotheses and conclusions, C032v hypotheses/conclusion, C032j full cited applicability proof, C032s endpoint hypotheses/conclusion; reused compound-Poisson audit assessment1559 and finite-Levy source notes1552. No new mathematical derivation or lemma.

Source lead: signed convolution inverse of a finite-activity compound-Poisson factor. Search found Trabs, Information bounds for inverse problems with application to deconvolution and Levy models (2015), primary Numdam PDF; Nickl/Sohl compound-Poisson BvM paper; Cekanavicius/Vellaisamy On closeness of two discrete weighted sums. Need inspect exact inverse formula, support conventions and full essential cases before approving a specialization. A finite positive restriction of nu_1's own Levy measure is a prospective test, distinct from C032u's width-difference factor. No actual-law counterexample is established here.

## Completed source evidence

1. Mathias Trabs, *Information bounds for inverse problems with application
   to deconvolution and Levy models*, Ann. Inst. H. Poincare Probab.
   Statist. 51(4) (2015), 1620–1650,
   [DOI10.1214/14-AIHP627, primary PDF](https://www.numdam.org/article/AIHPB_2015__51_4_1620_0.pdf).
   Inspected Section4.2, equation(4.8), printed p1636; the complete
   Example4.4 and following inverse discussion through Corollary4.5,
   p1637; model(4.2)-(4.3), p1634. For finite jump measure P and
   intensity m=P(R), at time Delta and zero drift, (4.8) is
   exp(-Delta*m) sum Delta^k P^{*k}/k!. The p1637 display gives
   its reflected signed inverse as exp(Delta*m) sum
   (-Delta)^k P(-.)^{*k}/k!. This is a finite signed measure.
   The surrounding score-operator injectivity uses a density for P;
   Example4.4 warns that injectivity on the restricted score space
   can fail for lattice jumps. Neither score-space injectivity nor
   a density of the entire law nu_1 is needed as a proposed import.
   Use only zero drift: no nonzero-drift convention is assessed.
   Reflection in the displayed inverse must be accounted for before
   using a half-line inverse. The source does not discuss this nu_1
   or state positivity reflection.

2. Vydas Cekanavicius and Palaniappan Vellaisamy, *On closeness of two
   discrete weighted sums*, Modern Stochastics: Theory and Applications
   5(2) (2018), 207–224,
   [DOI10.15559/18-VMSTA103, primary full article](https://www.vmsta.org/journal/VMSTA/article/114/read).
   Inspected Section1 immediately after(1), and the complete local
   inverse-use passage(21)-(26) in the proof of Theorem2.1.
   Section1 defines M as finite signed measures on R, convolution
   powers M^0=delta_0, and exp{M}=sum M^{*k}/k!, with total-variation
   estimate ||exp{M}||<=exp(||M||). These definitions are not limited
   to lattice M. In(23)-(24) the authors explicitly use exp{-L}
   as a finite signed inverse of a compound-Poisson law exp{L}.
   That application has symmetric lattice jumps; it is not a theorem
   about nu_1 or about half-line positivity. Import the general
   finite-measure exponential framework, not the paper's discrete
   approximation estimates. Any support and negative-set conclusion
   for the proposed half-line specialization remains to be proved.

3. Jean Bertoin, *Subordinators, Levy processes with no negative jumps,
   and branching processes*, Maphysto2000 course,
   [primary PDF](https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf).
   Reused assessment1559/notes1552; reaccessed Theorem1.2(i)-(ii),
   its complete converse proof pp7–8, and finite-activity discussion
   p9. A positive measure on (0,infinity) satisfying
   integral(1 wedge t) dP(t)<infinity, with nonnegative killing/drift,
   defines a subordinator exponent. The converse constructs the
   Poisson jumps, controls their sum using that integrability, and
   identifies its Laplace transform. Finite total jump mass and zero
   drift give compound Poisson. This permits a future check of a
   positive residual Levy measure. It does not establish a signed
   inverse's sign, or positivity reflection. Mimica2015
   Propositions1.4(iv)/1.8 are reused via1559 for convolution
   transforms and finite positive-measure uniqueness, including zero.

## Applicability and the exact remaining specialization

C032j's retained hypotheses give the positive Levy density ell_1(t)
from H_1(t)>0 and zero killing/drift. No claim about total finite
activity of nu_1 is needed or licensed. The proposed target uses only
the measure P obtained by restricting ell_1(t)dt to [1,3/2], not C032u's difference ell_2-ell_1.
The next research step must verify 0<P(X)<infinity, residual Levy
integrability, the actual transform identification, and convergence
of the imported signed inverse on X. It must check its mass is one,
produce a strictly negative Borel witness, and prove nu_1*lambda is
positive on every Borel set. These are prospective obligations, not
results established during this literature-only turn. Choosing a jump
interval with upper endpoint less than twice its lower endpoint is
a prospective way to isolate the sign witness; its use is unpaid.

Only general finite-signed exponential/inverse tools are source imports.
No located theorem directly resolves the implication for this qualified
law. Thus neither a generic counterexample nor the word 'signed' is
being passed off as an actual-law refutation. No full matching Mathlib
coverage was checked; availability remains unknown. No external source
or local theorem for a continuum common factor or tail obstruction
was found or asserted. C032r's moment equivalence remains conditional
on a positive output and full J_eta cancellation.

## Duplicate/failure comparison and bounded decision

C032u gives a positive width-difference factor and only a sufficient
coefficient range; no optimality or inverse positivity. C032v stops
one particular one-jump majorant, not finite-subfactor removal.
Stop1553 rules out ell_1-ell_2>=0; this target neither reverses that
ordering nor reopens its failed estimate. C033h's ordered-width
annihilator restriction supplies no sign information about an arbitrary
output-half-line signed remainder. The filename hits for zero-extracted
signed inverse212 and signed reflection1289 concern Li contours and
reflection positivity, respectively, not these measure-algebra inverses.
No duplicate actual-law subfactor test was located in this scoped search.
No claim of originality follows.

Continue with the exact finite-subfactor test only after separate
approval of its new assessment. Success requires a finite real signed
mass-one lambda on X, a negative Borel witness, and nu_1*lambda>=0
on all Borel sets under the full qualified inputs. Failure of any
support, normalization or residual-law check abandons this construction;
no positivity-reflection theorem is inferred from such failure.
A successful obstruction would close automatic deconvolution as a
shortcut, not decide C032q's cone, prove RH or exclude all common-factor
methods. No justified creative central proof is ready: positivity and
tails of a continuum remainder are still unpaid. This small known-tool
specialization must not be labeled creative.

## Search and access ledger

Queries inspected: convolution operator signed measures reflects positivity
only Dirac measure positive inverse; deconvolution positivity signed measure;
convolution order embedding measure; convolution reflects positivity;
convolution signed Raikov factors; convolution positive inverse probability
measure; signed convolution factors probability measures; Raikov signed
measures; convolution positivity reflecting; signed measure convolution
exponential inverse; compound Poisson inverse signed measure; convolution
exponential exp Banach algebra measures inverse.

Raubenheimer--van Appel, *On logarithms of measures* (2023), introduction,
Section3 operator paragraph and Theorem3.1, was inspected as a scope lead:
spectral/logarithm results on groups, not this half-line order implication.
Lindner--Pan--Sato arXiv1701.02400v1 introduction/definitions pp1–4 were
inspected; quasi-infinite divisibility assumes a probability law and is
not positivity of an arbitrary signed quotient. No later theorems from
that paper are imported. Nickl/Sohl BvM compound-Poisson and Roos2017
were discovery leads only; the Roos PDF fetch timed out and is optional,
not an essential source blocker. No source access loop is proposed.
Search snippets, abstracts and failed searches were not theorem evidence.

Outcome: EXPLORATION; new usable source coverage and an independently
testable nomination, with the exact-law conclusion still pending.
No lemma, script, proof overview or DAG edit was made.
