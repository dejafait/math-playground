# Finite-cosine displacement source review675

Literature-only work on assessment674's frozen finite-cell square.
No displacement relation, new lemma, mathematical script, node set,
matrix entry, error improvement or work saving is derived here.
An initial source checkpoint was saved here before the final comparison.

## Object and local evidence

Read C998g hypotheses and Sections1-4, C998a hypotheses/Section1,
C998e(6)-(8), source-notes670/658 and the hierarchy stop673.
C998g's K_0 integrates the product of two Carleman kernels over
0<t<a; its finite upper-end correction is essential. Its axis
singularity is integrable in the complete square but does not furnish
boundary traces for differentiated kernels. The cosine frequencies
are n*pi/ell on the half cell a=ell/2, with separate parity blocks,
neutral modes0/1 and the exact frozen652 coefficients unchanged.
The target is the whole square contribution with factor1/4.

The scoped12November literature/attempt/history search for finite
cosines, Sylvester/displacement relations and coincident modes found
no earlier completed assessment of this coefficient-space target.
The existing point-evaluator and Duffy stops are prescription-specific.
The hierarchy stop673 is a different source-scope obstruction.
No sibling notebook, supervisor state or cross-notebook theorem was read.

External queries used the combinations `Carleman operator finite interval
cosine Galerkin matrix displacement equation boundary`, `Hankel integral
operator finite interval Fourier Galerkin displacement Sylvester matrix
cosine`, `Carleman displacement operator`, `Galerkin displacement rank`,
`Hankel integral operator cosine matrix elements`, `Carleman Sylvester
equation`, `Kailath Olshevsky partially reconstructible pdf 1997`,
`Hankel finite interval commutator boundary`, and `Galerkin integrable
kernels displacement matrix`; also searched the exact GKO and
Tracy--Widom titles. Many hits concern unrelated Carleman estimates,
linearization or Bessel transforms; none is used as evidence. No exact
finite-cosine square assembly theorem was identified in this bounded
search. This does not establish absence or originality.

## Primary evidence recorded so far

Arico--Rodriguez, *A fast solver for linear systems with displacement
structure*, [arXiv:1004.1988v1](https://arxiv.org/pdf/1004.1988v1),
12April2010: read Section2/(4)-(5), Table1, Remark2.1, Section3.1
through Remark3.1 and Algorithm1's input conditions (printed pp3-8).
For known EA-AF=GH*, diagonalizable E,F permit a change to diagonal
displacement matrices. Remark2.1 requires t_i!=s_j for complete
reconstruction; coincident pairs require additional matrix entries.
Remark3.1 stores these entries instead of reconstructing them from
generators. The operation counts concern an already supplied structured
matrix and its Schur complements, not computing singular integrals or
the generators for C998g. Discrete cosine transforms in Table1 do not
assert structure for every matrix of cosine-weighted integrals.
Also inspected Section3.3/Proposition3.2 and the repeated-knot storage
argument through Algorithm3 (pp9-12). Repetition within one knot list
is distinguished from overlap between the two lists: Algorithm3 still
requires t_i!=s_j for every i,j. It does not supply missing Galerkin
diagonal entries.

Blower, *Hankel operators that commute with second-order differential
operators*, [arXiv:0712.1013v1](https://arxiv.org/pdf/0712.1013v1),
6December2007 (manuscript dated7October2007): read Theorem2.1 and
its integration-by-parts argument (2.3)-(2.5), printed pp3-4.
The operator has kernel phi(x+y) on L2(0,infinity); the differential
coefficient a has a(0)=0 and a'''=A a'. A further difference-quotient
condition on b and the displayed ODE for phi give commutation on
C_c^infinity(0,infinity). Equation(2.4) retains the endpoint bracket
before it vanishes in this domain. This is not a finite-cell cosine
matrix identity or a license to drop a nonzero finite upper boundary.

Sweet--Brent, *Error Analysis of a Partial Pivoting Method for Structured
Matrices*, TR-CS-95-03,7June1995,
[arXiv:1005.0667v1](https://arxiv.org/pdf/1005.0667v1),
uploaded5May2010: read Theorem3.6 and its proof, printed pp11-12.
Its Frobenius backward-error bound for the GKO factorization depends
on generator-growth factors and extremal moduli of the Cauchy kernel.
It is neither an entrywise integration error bound nor a universal
stability constant. The earlier conference version25April1995 was
opened only for orientation; all detailed references use this report.
Section5.2's first example (p15) exhibits cancellation between two
generator products, so small displacement rank does not by itself
control numerical error. This example concerns a factorization, not
a counterexample to the proposed integral evaluator.

Tracy--Widom, *Fredholm Determinants, Differential Equations and Matrix
Models*, Communications in Mathematical Physics163(1994),33-72,
DOI10.1007/BF02101734,
[author PDF](https://www.math.ucdavis.edu/~tracy/selectedPapers/1990s/CV49.pdf):
read (1.2)-(1.4), SectionIIA/B through the coincident spatial-point
formula(2.8), and SectionIID's boundary distribution/commutator passage
through(2.32), printed pp34-35,39-41,45. The finite-union-of-intervals
theory retains endpoint terms. Its resolvent formulas assume the inverse
of I-K exists; the determinant discussion invokes smoothness, and the
closed PDE system uses polynomial differentiation relations for the two
kernel functions. Spatial diagonal limits are not cosine-frequency
diagonal entries. No singular-axis limit, finite-cosine Galerkin
closure or certified operation count is supplied by these passages.
Some scanned commutator formulas have corrupt OCR; no exact sign or
formula is imported from those unreadable characters. The readable
hypotheses and explicit need for boundary terms suffice for this
scope comparison, not for a specialization of their PDE system.

## Access and scope decision

The AMS Gohberg--Kailath--Olshevsky1995 PDF returned403; the guessed
author papers directory was inaccessible. These are unread leads,
not theorem evidence. Accessible primary sources above already expose
the reconstruction and boundary qualifications; no dependency on an
unread theorem is proposed. Kailath--Olshevsky, LAA254(1997),251-302,
DOI10.1016/S0024-3795(96)00288-1, was found at its publisher; only its
abstract was available and it is not an imported result. No further
access attempts to these nonessential leads are needed.

The source-scope result is NEGATIVE for a turnkey import. None of the
inspected results simultaneously supplies the frozen K_0 generators,
finite upper-end terms, singular-axis cancellation, frequency-diagonal
data and a certified error/work bound. In particular, neither the
known physical diagonal in C998e(6) nor continuous kernel displacement
can stand in for the unproved finite cosine matrix relation. A
multiplication-operator commutator is also not a theorem that its
finite cosine compression has the same displacement representation;
that applicability has not been checked. These are qualifications,
not new nonexistence, rank, complexity or instability results for K_0.

Assessment674 is completed EXPLORE: known tools and the bounded search
permit a finite analytic closure test, not an import of fast assembly.
The first essential unproved input is the finite-cell boundary relation
and its singular cutoff limit. No inaccessible theorem is needed to
*test* that relation using ordinary finite-interval integration by
parts, the audited integral representation and the existing absolute
integrability bounds. Their differentiation and boundary-limit
hypotheses must be proved in the future attempt; Fubini alone is
insufficient. No general theorem is to be reproved. Reuse658 only if
Si/Ci definitions or primitives occur, with its zero-mode/branch
qualifications; its stopped point-evaluator work count is not reused
as an algorithm.

## One bounded continuation, awaiting separate approval

The exact continuation is in assessment675: test an integration-by-parts
closure only for pairs (0,0),(0,2),(2,2),(2,4),(1,1),(1,3).
These are specified tasks, not newly calculated entries. They cover
zero frequency, coincident frequency and distinct same-parity modes
in both blocks. At a strictly positive cutoff the kernel must first
meet the finite smooth integration-by-parts hypotheses. Retain all
axis and finite-end terms until combined limits are justified. A
spatial coincident-node rule is not a frequency-diagonal rule.

Continue only if every selected entry has an exact reduction to
explicit endpoint data and convergent one-variable integrals, with
every removed-cutoff error or exact limit justified. Stop at the
first unclosed two-variable singular correction, failed limit or
missing independent diagonal datum; retain the failed expression.
Passing these cases would justify investigating general closure, not
prove it. No256-mode implementation, arbitrary-mode identity, claimed
low rank, nodes, precision choice or quantitative certificate is
authorized by this restricted test. The original1e-10/20000000 target
remains the eventual requirement, not an achieved or relaxed bound.
Here closure requires shared, explicitly defined one-variable moments
of boundary/kernel data. Merely using Fubini to write the original
integral of two Carleman outputs, or renaming that product as a moment,
does not pass. The proposed data must be specifiable without two such
outputs or unknown mode-pair Galerkin entries. This prevents repeating
the already known square representation as purported progress.

The new ready continuation needs separate next-turn source approval.
This is established-method development, not a new central signed-S3
mechanism. The central gap remains actual-Xi positivity/signed remote
plus induced coupling; no justified creative mechanism emerged from
this computational source review. Existing652/657/660/662/672 stops,
673 hierarchy stop and674 audit are preserved in their exact scopes.
No lemma, DAG or PROOF change is appropriate because the argument did
not change. Mathlib full matching coverage is unchecked; no absence
claim or cross-notebook import is made.
