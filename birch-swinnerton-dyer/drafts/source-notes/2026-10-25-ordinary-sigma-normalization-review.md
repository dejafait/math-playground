# Ordinary sigma normalization source review — step 495

Completed literature-only comparison. New source coverage supports a
replacement input, not a mathematical repair of L119. Its positive-rank
hold remains in force pending a separate approved mathematical step.

The main gap is rank versus complex analytic order for arbitrary E/Q.
The intermediate target is the exact canonical ordinary-height input to
L119. Its downstream use is the regulator handoff to L003/L118. Continue
only with a precise primary-source conversion or replacement; otherwise
park this dependent handoff and choose independent work.

Read L119's hypotheses, precision/convention paragraph and step-494 audit,
foundations/04, the prior audit/stop and relevant prior assessments.
Finite algebra, Kummer and the k=0 case are not reopened. Existing changes
and unfinished computations are preserved.

Web-extracted primary PDFs are accessible. A local PDF download failed
DNS; no local capture was produced. Screenshot calls returned reference
strings or text containing an image placeholder, without an image content
block; an initial alternate-connector call also failed. Original-layout
inspection was therefore not achieved. No visual verification is claimed.

## Primary statements and applicable cases

**Mazur--Stein--Tate.** Barry Mazur, William Stein and John Tate,
*Computation of p-Adic Heights and Log Convergence*, Documenta Mathematica,
Extra Volume Coates (2006), 577--614,
[publisher PDF](https://ems.press/content/book-chapter-files/27479).
Read pp.578--581: cyclotomic character, Iwasawa logarithm, equation (1.1),
polarization, Theorem 1.3 and equations (1.7)--(1.9), including footnote 4.
For E/Q, good ordinary p>=5 and a non-torsion point reducing to zero at p
and to the identity component at every bad prime, the source gives

\[
 h_{MST}(P)=p^{-1}\log_p(\sigma(P)/d(P))
          =-\tfrac12(P,P)_{MST},
\]

with pairing (P,Q)_{MST}=h_{MST}(P)+h_{MST}(Q)-h_{MST}(P+Q).
Theorem 1.3 characterizes sigma by integrality, leading term t, oddness
under group inversion and its differential equation. The printed constant
is c=(b_2-E_2(E,omega))/12; its coordinate is wp=x+b_2/12.
Footnote 4 reports a sign error in MT91; it does not correct SW.

Also read Sections 2.1 pp.582--583 and 2.6--2.8 pp.585--587: the height
comes from composing a universal pairing with an idele-class functional;
admissibility is removed by multiplication and bilinearity. The
cyclotomic functional over Q is p^{-1}log_p composed with the cyclotomic
character. Section 3.1 pp.588--590 uses the shifted coordinate explicitly;
Section 3.2 pp.590--591 uses a short Weierstrass basis for Frobenius.
These primary statements provide a canonical cyclotomic replacement,
without prescribing a correction to SW. The
[author PDF](https://wstein.org/papers/pheight/pheight.pdf) starts at p.585
rather than p.577; the cited page numbers above are the publisher's.

**Harvey.** David Harvey, *Efficient computation of p-adic heights*,
[arXiv:0708.3404v1](https://arxiv.org/pdf/0708.3404v1), 24 August 2007.
Reinspected integral-model/differential hypotheses and Theorems 1--3,
pp.1--2; Section 2.1 equation (2), p.3; Section 2.2 equation (3), p.4;
and Section 5's admissible-multiple reduction, pp.11--12. His p>=5
ordinary hypothesis and usual differential match L119's more restrictive
minimal integral model. His sigma equation uses exactly the constant
printed in MST. His introduction explicitly states h_H=2p*h_MST.
For M>=2, Theorem 3 uses sigma modulo I_(M'+1), M'=M+2v_p(n),
n=lcm(#E(F_p), lcm of Tamagawa numbers), to produce h_H modulo p^M.
Theorem 2 requires E_2 modulo p^(d-3) for sigma modulo I_d, d>=4.
Existing zero/torsion exceptions and the full Section 5 precision contract
remain as audited in L119; no new implementation check was performed.

**Stein--Wuthrich.** William Stein and Christian Wuthrich,
*Algorithms for the arithmetic of elliptic curves using Iwasawa theory*,
Math. Comp. 82 (2013), 1757--1792,
[published offprint](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf).
Reinspected Section 3.5 p.1767 (eta=x*omega and phi=F/p), Section 4
pp.1769--1770 (Bernardi sigma and linear height family), Section 4.1
equation (4.1) and its continuation p.1771, and Section 4.4 p.1774.
The extracted text retains the previously recorded b_2 discrepancy.
The
[author preprint](https://wstein.org/papers/shark/shark.pdf), Section 4.1,
pp.14--15, retains the same displayed exponential. Neither extraction
authenticates a proposed corrected formula. Retain the discrepancy as a
qualification; do not import its E_2/eigenvector ratio on a general model
or use its scalar-comparison sentence to override the explicit MST
normalization. Foundations/04's existing characteristic-order input is
reused only for canonical ordinary regulator nonvanishing, not a refined
leading coefficient.

## Search, failures and scope decision

Queries included `Harvey Efficient computation p-adic heights Stein
Wuthrich sigma b2 E2 errata`, `Mazur Stein Tate computation p-adic heights
2006 sigma E2`, `"Stein" "Wuthrich" "errata" sigma`,
`"mcom2649" correction`, `"Wuthrich" "sigma" "b_2"`,
`"iwasawa-alg" errata`, and `"p-adic sigma function" "mazur"
filetype:pdf 1991`. Checked the relevant entries on
[Wuthrich's publication page](https://www.maths.nottingham.ac.uk/plp/pmzcw/)
and [Stein's paper archive](https://wstein.org/papers/shark/).
No relevant author-issued correction was located in this bounded search;
this is not evidence that none exists. The linked LaTeX source was
inaccessible. The intended contents were not inferred from its filename.

Mazur--Tate, *The p-adic sigma function*, Duke Math. J. 62 (1991),
663--688, [DOI](https://doi.org/10.1215/S0012-7094-91-06229-0), remains
indirectly read through MST's precise statements. Project Euclid returned
an access-interstitial iframe and its blocked target; an attempted author
PDF was inaccessible. No direct MT91 proof or independent errata reading
is claimed. This is nonessential for importing the explicit MST
construction and its stated canonical cyclotomic formula. A proposed
correction of SW itself would still require further source evidence.

Reused prior finite-certificate discovery and failure coverage; the
step-494 audit and ATTEMPTS/057 preserve the failed literal comparison.
L001, L003 and audited L118 remain available inputs. No theorem in this
review provides actual arithmetic data, uniform height nondegeneracy or
comparison with arbitrary complex analytic order. Mathlib coverage for
these complete canonical-height identifications is not checked.

The decision is SPECIALIZE for a *replacement handoff*: import MST's
canonical pairing and Harvey's explicit normalization, then in a later
research step check their scalar relation to L119's retained q=-h_H,
absolute precision and foundations/04. No need to reprove the sigma or
height construction. Literal Harvey/SW equality is not certified here;
no log_E squared correction or sign-only conversion is derived today.
The new repair assessment requires separate approval before invocation.
