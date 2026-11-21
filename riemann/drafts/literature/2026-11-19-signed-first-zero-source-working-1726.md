# Signed first-zero dominance: source review1726

19 November 2026. Completed literature-only review of nomination1725's
exact TARGET. No new estimate, lemma, mathematical script or W sign
was derived. All preexisting work is preserved.

## Gap, target, use and discriminating test

The main gap is L030-L032/C032a actual-Xi all-degree positivity. The
intermediate target is a signed first-zero-pair comparison for C032n's
width-ratio derivative on [1,2], at a=1/8 and b=1/4. A strict negative
margin would supply the remaining sign premise of its conditional
formula (19), using C033f's nonvanishing. It would pay one ordered
minor only. Continuous-density Chebyshev use, arbitrary signed
measures, constant-span completeness, positive output, moments and
actual-Xi realization remain independent open steps.

Continue to one bounded proof attempt only after separate approval of
the new assessment1726. Require an explicit uniform upper bound below
zero for the complete W/f^2, including relative errors and the full
E correction. An enclosure containing zero is inconclusive: save its
actual and required bounds and park rather than extend a grid or
repeat a modulus estimate. No sign or numerical margin was tested here.

## Local screening and reused coverage

Read C032n's definitions and complete (15)-(20) attempt, C032j/m's
hypotheses and interfaces, C033f's statement/source qualifications,
C032y's statement/transform interface and count specialization, and
C033c's statement. Reuse source-notes1709/1721/1577 and stop1711.
Scoped searches for first-zero, signed-core, dominant-core and N(20)
in November19 literature/attempt files and C032/C033 files found no
existing certificate for this signed relative target. This is not an
exhaustive archive or novelty claim. No cross-notebook input was used.

Comparison1709 already checks Gaussian composition, nonlinear
preservers and Chebyshev hypotheses against the actual kernel. That
adequate coverage is reused: it does not import automatic TP for this
width family with complex centers. Stop1711 is an absolute-W enclosure
containing zero. C033f now supplies nonvanishing, not relative derivative
control. C033c is an absolute O upper bound, explicitly excluding any
R/E estimate; it does not remove the present gap.

Source-notes1721 supplies Platt--Trudgian2004.09765v1 Theorem1/Section2
and Bellotti--Wong2412.15470v2 Theorem1.1/Section5, including multiplicity,
cutoff completeness and the corrected inclusive counting constants.
Reuse these assessments unchanged. In particular, do not import
C032y's older displayed 9.3675 count constant or treat its spectral
tail as already checked under the replacement count. Its exact paired
resolvent formulas and analytic exchanges remain available under their
stated assumptions; a fresh effective use must justify its own count
bound. No correction of a canonical lemma was attempted in this
literature-only turn, and no claim that its coarse conclusion fails
follows from this source discrepancy.

## New low-zero primary coverage

FLINT, official documentation, checked 19 November 2026,
[acb_dirichlet/zeta-zeros, API contract and Example](https://flintlib.org/doc/acb_dirichlet/zeta-zeros.html).
The contract for acb_dirichlet_zeta_zeros requires starting index n>=1;
consecutive indices refer to zeros of zeta in the critical strip,
not just discovered critical-line roots. It states rigorous isolation,
completeness between returned zeros, simplicity and critical-line
location in examined Gram blocks. The documented checked example
starts at n=1 and reports the first two ordinate balls:

    [14.1347251417346937904572519836 +/- 3.76e-29],
    [21.0220396387715549926284795939 +/- 3.10e-30].

Thus this is adequate source coverage for the planned coarse import:
one simple positive-ordinate zero in (14,15), no other through 20.
This applicability inference uses the consecutive-zero contract as
well as the balls; a coordinate table alone would not suffice. The
external calculation and library correctness are imported, not
independently rerun or formally verified here. No local zero program
was run and no extra precision is needed for that separation.

The [algorithm documentation](https://flintlib.org/doc/algorithms/special-functions/zeta-zeros.html),
sections Gram points/blocks and Turing's method, was read for the
relevant cases. The low branch uses the known first126 Gram-law
verification; it is not an application at height20 of Theorem1's
Turing integral bound, whose hypothesis is t2>t1>=168*pi.
The corresponding code was inspected at fixed commit
[1d432c3bba36d1a29f6453ebfaa00e43f58c278f](https://github.com/flintlib/flint/blob/1d432c3bba36d1a29f6453ebfaa00e43f58c278f/src/acb_dirichlet/isolate_hardy_z_zero.c),
constants and the complete _separated_gram_list/_separated_list cases
(lines25-31,922-998), plus create_gram_node's enclosing sign check
(lines163-213). The code selects the Gram branch for 1<=n<=126,
bracketing n by Gram indices n-2 and n-1; the Rosser and Turing branches
are separate. This inspection identifies the historical low-count
input; source reading is not a replay certificate for the whole library.

Juan Arias de Reyna, *Programs for Riemann's zeta function*, in
*Leven met getallen*, CWI (2012), pp102-112,
[primary final PDF](https://ir.cwi.nl/pub/19724/19724D.pdf), Section2,
pp104-106 and Theorem2.1, was inspected as the algorithm's cited
background. N counts multiplicity and includes the ordinate endpoint;
counting and sign changes are separate requirements. The paper's
mpmath examples are not substituted for FLINT's rigorous contract.
No further historical verification proof is claimed from this reading.

## Changed signed-relative scope

Suvrit Sra, *Some positivity properties of Riemann Xi under smoothing*,
[fixed2611.00345v1](https://hexagonmath.org/pdf/2611.00345v1), released
11 November2026: reuse Theorem3.3, p6, and coverage1721. Reopened
Section3.1 and AppendixC.2-C.3, pp21-22, LemmasC.2-C.3 with their
proofs, and AppendixC.5's relevant near-origin proof, p24. Vertical
displacement and counting give absolute cumulative/profile envelopes;
the origin proof retains a positive anchor against an unverified tail.
They do not supply a width derivative of the nonlinear kernel or a
relative W/f^2 margin. The final semigroup step preserves cumulative
positivity, not the sought signed quotient derivative. The specified
new comparison is therefore not a citation-only import of Theorem3.3.
Its fixed-v1 and external-computation qualifications remain in force.

C032n(16)-(17), including signs and the cancellation of its normalization
constant, still require checking in the later attempt; this source
review does not audit those formulas. C032m/n supply the compact-width
analytic interface. C032y's exact resolvent interface and assessed
DLMF7.7.2/7.2.3/7.4.3 coverage1577 may support E control; no whole-plane
uncorrected Cauchy integral, boundary principal value, or uncontrolled
erfc asymptotic is approved. The effective E difference remains a
local proof obligation, not a missing named theorem. Likewise the
first-core sign and quantitative relative p/A derivative errors must
be proved, rather than inferred from the source's positive profile.

## Discovery record, inaccessible leads and decision

Queries included `Riemann zeta first zero rigorous N(20) 1 Turing
verification`, `zeta zeros Gaussian smoothing first zero dominance width
derivative ratio Wronskian`, exact `"zeta" "N(20)" zeros`,
`Hutchinson 1925 zeta first zeros 14.134 21.022 pdf`,
`"zeta" Gaussian "Wronskian" smoothing dominance`,
`"Gaussian" "zeta" "first zero" dominance derivative`,
`"Xi under smoothing" "width" "ratio"`, and
`"sinh" "Gaussian" "zeta" "Wronskian"`. These bounded searches
located no matching signed nonlinear relative theorem. Search snippets,
nonrigorous lists and other research notebooks were discovery only;
none is a mathematical input. Failed searches do not establish novelty.

Johansson1309.2877v1 was opened as a high-precision lead, but its
low-zero completeness proof was not inspected and is not imported.
Hutchinson (1925), DOI10.1090/S0002-9947-1925-1501297-5, publisher PDF
returned403; JSTOR's PDF was inaccessible. Gram (1903),
DOI10.1007/BF02421310, ProjectEuclid redirected to a service notice;
the Zenodo record was inaccessible. These remain unread historical
leads, not asserted theorem coverage. An initial guessed Hutchinson
identifier1501298-3 was wrong and supplied no evidence. Neither the
inaccessible originals nor the high-precision lead is essential once
the official FLINT certified contract/example is retained explicitly
as the external computational input. Do not spend another turn solely
retrying those access paths.

Decision EXPLORE for one finite-scope signed comparison: low-zero
separation is covered; full-divisor analytic/counting interfaces are
available; no matching signed theorem was found in the bounded screen.
The missing sign/relative estimates are precisely the research target,
not hypotheses being approved as true. No reproof of Gaussian heat flow,
zero counting, or the external first-zero computation is justified.
Full matching Mathlib coverage is unchecked/unknown. This is source
progress locally, not progress beyond the cited mathematics and not an
RH candidate. A new central creative attempt remains unjustified:
the present minor has no proved bridge paying actual-Xi positivity.
