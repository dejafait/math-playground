# Difference-of-fourth-powers source comparison

TARGET: Determine the precise known exclusion range for positive primitive a^4+b^p=c^4 with odd prime p>=5, including base-one cases.
CHECKED: 2026-10-06
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Exact difference equation and signature (4,p,4) searches located Darmon Theorem I, Bennett 2021's historical comparison, and Kihel–Levesque Theorem 2.1(i); local foundations 09/14 and ATTEMPTS/001–005 were compared.
SOURCE_EVIDENCE: Read Darmon's author copy https://www.math.mcgill.ca/darmon/pub/Articles/Research/10.Fermat-44p/paper.pdf pp. 1–4, including both Theorem I clauses and proof cases; read Kihel–Levesque https://doi.org/10.4153/CMB-2002-028-1 pp. 247–250, including Theorem 2.1(i) and its m=0 citation to Cao; Cao's publisher download https://mathreports.ca/download/3521/ failed.
COMPARISON: The published stronger statement covers every odd prime, but its essential m=0 proof input remains unread; Darmon's inspected theorem covers p>=11 with p=1 mod 4 or even power base, after full modularity.
GAP: Cao's full proof of the coefficient-one clause, including small primes and odd power base at p=3 mod 4, was not retrieved; no full-range mathematical application is approved here.
REASON: Changed placement requires independent coverage; park the blocked full-range proof review and prepare the independently inspected Darmon subfamily for separate approval.

The main gap is emptiness for every residual positive primitive signature in S^3. The intermediate source target could support an L002 ordered divisor exclusion. Independent mixed-seventh algebra and packet gaps remain. This literature step derives no exclusion and modifies no lemma or mathematical script.

## Inspected sources and qualifications

Henri Darmon, *The equation x^4-y^4=z^p*, C. R. Math. Rep. Acad. Sci. Canada **15** (6) (1993), 286–290, **Theorem I**. [Author copy](https://www.math.mcgill.ca/darmon/pub/Articles/Research/10.Fermat-44p/paper.pdf), internally dated September 9, 2007; [author bibliography](https://www.math.mcgill.ca/darmon/pub/pub.html) confirms publication, but equality with the printed version was not checked. Equation (1) assumes gcd(x,y)=1. Under Shimura–Taniyama, for prime p>=11 there is no nontrivial solution when p=1 mod 4, nor with z even. No coordinate lower bound greater than one is imposed. The proof identifies triviality by a zero coordinate. Pages 2–4 treat odd z by a level-32 CM form and the split-Cartan argument, and even z by the absence of weight-two level-2 forms; the complementary nonsplit case is explicitly unresolved there. Use foundations/02-standard-results.md's separately verified BCDT Theorem A to discharge modularity. Do not attribute full odd-prime coverage to this paper.

O. Kihel and C. Levesque, *On a Few Diophantine Equations Related to Fermat's Last Theorem*, Canadian Mathematical Bulletin **45** (2) (2002), 247–256, **Theorem 2.1(i)**, printed pp. 249–250; [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F27F6AA3C5A3593E4129052D56EDB032/S0008439500016234a.pdf/on_a_few_diophantine_equations_related_to_fermats_last_theorem.pdf), [DOI](https://doi.org/10.4153/CMB-2002-028-1). For odd prime p and nonnegative m, it excludes nonzero pairwise coprime integer solutions of X^4-Y^4=2^m Z^p. No base-one exception is stated. Its proof delegates m=0 to Cao; m>=1 treats m=1,2,3 and m>=4 via factorization, FLT and Ribet. The statement is directly relevant at m=0, but inspecting the m>=1 proof does not inspect the load-bearing m=0 input.

Z. Cao, *The Diophantine equations x^4-y^4=z^p and x^4-1=dy^q*, C. R. Math. Rep. Acad. Sci. Canada **21** (1) (1999), 23–27, is an **unread essential proof lead**. [Publisher index](https://mathreports.ca/keyword/diophantine-equation/) was read; article retrieval timed out, as did its linked [download](https://mathreports.ca/download/3521/), with and without the supplied timestamp. Shell retrieval also failed. No theorem number or proof scope is invented. These are access failures, not mathematical counterevidence.

Michael A. Bennett, *Integers represented by x^4-y^4 revisited*, Bulletin of the Australian Mathematical Society **103** (2021), 38–49, [author PDF](https://personal.math.ubc.ca/~bennett/Bennett-BullAusMS-2021.pdf), p. 38 introduction, explicitly describes the coefficient-one n>=2 coprime family as settled and references Darmon, Darmon–Merel, Ribet and Cao. This corroborates the stronger published range but is not the inspected proof of it. Its coefficient-bearing asymptotic Theorem 1.1 is not substituted for coefficient one at all primes.

Searches included “Diophantine equation x^4 - y^4 = z^p prime Bennett”, “generalized Fermat equation signature (4,p,4) nontrivial solutions”, “Darmon The equation 286 290 x4 y4 pdf”, and exact Cao title searches. Secondary snippets were leads only. Bennett–Skinner's 2004 introduction was inspected as a reference lead, not an additional theorem input.

## Duplicate, failure and continuation comparison

L027 covers only (4,4,p); L012 covers the cube boundary. Neither duplicates the p>=5 difference placement. ATTEMPTS/001's local obstruction and ATTEMPTS/002–004's repeated-cube failures do not preclude this global citation. ATTEMPTS/005's absent spectral data do not enter it. No sign change of an even power is allowed.

For a later application, essential inputs are L002, foundations/01-target-and-scope.md and BCDT Theorem A in foundations/02-standard-results.md. The candidate direct identification is (x,y,z)=(c,a,b); its positivity, coprimality, nontriviality and ordered divisor transfer must be justified in that research turn. The source has no base-one restriction. No reproof of the modular argument is justified.

Continue only within Darmon's inspected clauses; abandon any extension to odd b and p=3 mod 4 without independent coverage. Park the blocked full-range application rather than repeat source retrieval. Mathlib full matching theorem and supporting coverage: not checked. This is useful local source coverage, not new mathematics or a Beal resolution.
